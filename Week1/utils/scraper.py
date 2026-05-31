import json
import re

import requests
from bs4 import BeautifulSoup


def _parse_duration(duration_str):
    """Convert ISO 8601 duration (PT45M, PT1H30M) to human-readable string."""
    if not duration_str:
        return "N/A"
    hours = re.search(r"(\d+)H", duration_str)
    minutes = re.search(r"(\d+)M", duration_str)
    h = int(hours.group(1)) if hours else 0
    m = int(minutes.group(1)) if minutes else 0
    if h and m:
        return f"{h}h {m} min"
    elif h:
        return f"{h}h"
    return f"{m} min"


def _find_recipe_node(data):
    """Recursively find a node with @type containing 'Recipe'."""
    if isinstance(data, list):
        for item in data:
            result = _find_recipe_node(item)
            if result:
                return result
    elif isinstance(data, dict):
        recipe_type = data.get("@type", "")
        if isinstance(recipe_type, list):
            recipe_type = " ".join(recipe_type)
        if "Recipe" in recipe_type:
            return data
        if "@graph" in data:
            return _find_recipe_node(data["@graph"])
    return None


def _parse_instructions(raw):
    """Flatten various instruction formats into a list of strings."""
    if not raw:
        return []
    if isinstance(raw, str):
        return [raw]
    steps = []
    for item in raw:
        if isinstance(item, str):
            steps.append(item)
        elif isinstance(item, dict):
            if item.get("@type") == "HowToSection":
                for sub in item.get("itemListElement", []):
                    text = sub.get("text", sub.get("name", "")) if isinstance(sub, dict) else str(sub)
                    if text:
                        steps.append(text)
            else:
                text = item.get("text", item.get("name", ""))
                if text:
                    steps.append(text)
    return steps


def _parse_number(value):
    """Extract the first number from a string like '500 calories' or '30g'."""
    if not value:
        return 0
    match = re.search(r"[\d.]+", str(value))
    return int(float(match.group())) if match else 0


def scrape_recipe(url):
    """
    Fetch a recipe page and extract structured data from its JSON-LD markup.
    Returns a recipe dict on success, or None on failure.
    """
    try:
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            )
        }
        response = requests.get(url, headers=headers, timeout=12)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        recipe_node = None
        for script in soup.find_all("script", type="application/ld+json"):
            try:
                data = json.loads(script.string or "")
                recipe_node = _find_recipe_node(data)
                if recipe_node:
                    break
            except (json.JSONDecodeError, TypeError):
                continue

        if not recipe_node:
            return None

        name = recipe_node.get("name", "Custom Recipe")
        total_time = recipe_node.get("totalTime") or recipe_node.get("cookTime", "")
        cook_time = _parse_duration(total_time)
        ingredients = recipe_node.get("recipeIngredient", [])
        instructions = _parse_instructions(recipe_node.get("recipeInstructions", []))

        nutrition = recipe_node.get("nutrition", {}) or {}
        macros = {
            "cal": _parse_number(nutrition.get("calories", 0)),
            "protein": _parse_number(nutrition.get("proteinContent", 0)),
            "carbs": _parse_number(nutrition.get("carbohydrateContent", 0)),
            "fat": _parse_number(nutrition.get("fatContent", 0)),
        }

        return {
            "id": f"custom_{abs(hash(url)) % 1_000_000}",
            "name": name,
            "time": cook_time,
            "cal": macros["cal"] if macros["cal"] else "N/A",
            "is_custom": True,
            "ingredients": [{"emoji": "🥗", "name": ing} for ing in ingredients[:12]],
            "macros": macros,
            "instructions": instructions[:6],
            "shopping": [
                {
                    "cat": "Ingredients",
                    "items": [{"name": ing, "qty": "as needed"} for ing in ingredients],
                }
            ],
        }

    except requests.exceptions.Timeout:
        return {"error": "The request timed out. Check the URL and try again."}
    except requests.exceptions.HTTPError as e:
        return {"error": f"Could not access that page ({e.response.status_code})."}
    except Exception:
        return None
