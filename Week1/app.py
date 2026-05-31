import streamlit as st

from data.cuisines import CUISINES
from data.recipes import RECIPE_DATA, get_shopping
from utils.scraper import scrape_recipe

# ── Constants ────────────────────────────────────────────────────────────────

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
SLOT_COLORS = ["#2980b9", "#e67e22", "#27ae60"]
SLOT_BG = ["#e8f4fd", "#fef9e7", "#f0fff0"]
SLOT_LABELS = ["Recipe 1", "Recipe 2", "Recipe 3"]
RECIPE_EMOJIS = ["1️⃣", "2️⃣", "3️⃣"]
CAT_ICONS = {"Proteins": "🥩", "Produce": "🥦", "Pantry": "🫙", "Dairy": "🧀", "Ingredients": "🥗", "Other": "📦"}
MAX_RECIPES = 3


def assign_days(num_recipes):
    """Distribute Mon–Fri across recipes as evenly as possible."""
    return [i % num_recipes for i in range(5)]


def build_shopping_list(selected_recipes):
    """Combine and scale shopping lists for all selected recipes."""
    if not selected_recipes:
        return []
    combined = {}
    assignments = assign_days(len(selected_recipes))
    for slot_idx, recipe in enumerate(selected_recipes):
        days_count = assignments.count(slot_idx)
        servings = days_count * 2  # 2 people per day
        if recipe.get("is_custom"):
            shop_data = recipe.get("shopping", [])
        else:
            shop_data = get_shopping(recipe["id"], servings)
        for cat_block in shop_data:
            cat = cat_block["cat"]
            if cat not in combined:
                combined[cat] = []
            for item in cat_block["items"]:
                combined[cat].append({**item, "slot_idx": slot_idx, "recipe_name": recipe["name"]})
    return [{"cat": cat, "items": items} for cat, items in combined.items()]


# ── Page config ──────────────────────────────────────────────────────────────

st.set_page_config(
    page_title="Meal Prep Planner",
    page_icon="🥗",
    layout="centered",
)

# ── Custom CSS ───────────────────────────────────────────────────────────────

st.markdown("""
<style>
    .main .block-container { max-width: 700px; padding-top: 1rem; }
    .app-header {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        color: white;
        padding: 20px 16px 16px;
        border-radius: 14px;
        text-align: center;
        margin-bottom: 20px;
    }
    .app-header h1 { font-size: 22px; margin: 4px 0; color: white; }
    .app-header p { font-size: 12px; opacity: 0.7; margin: 2px 0 0; }
    .recipe-badge {
        display: inline-block;
        border-radius: 20px;
        padding: 3px 10px;
        font-size: 11px;
        font-weight: 700;
        color: white;
        margin: 3px;
    }
    .ingredient-card {
        background: var(--card-bg, #f8f8f8);
        border-radius: 12px;
        padding: 12px 6px;
        text-align: center;
        margin-bottom: 6px;
    }
    .ingredient-card .ing-emoji { font-size: 26px; }
    .ingredient-card .ing-name { font-size: 11px; font-weight: 600; color: #444; margin-top: 4px; }
    .shop-item {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 12px;
        border-radius: 10px;
        margin-bottom: 5px;
        border: 1px solid #eee;
    }
    .stButton button { border-radius: 20px; }
    div[data-testid="stTabs"] button { font-size: 13px; }
</style>
""", unsafe_allow_html=True)

# ── Session state ─────────────────────────────────────────────────────────────

if "selected_recipes" not in st.session_state:
    st.session_state.selected_recipes = []
if "checked_items" not in st.session_state:
    st.session_state.checked_items = set()
if "active_cuisine" not in st.session_state:
    st.session_state.active_cuisine = "Italian"
if "custom_recipe" not in st.session_state:
    st.session_state.custom_recipe = None
if "url_error" not in st.session_state:
    st.session_state.url_error = ""

# ── Header ───────────────────────────────────────────────────────────────────

badges_html = ""
for i, r in enumerate(st.session_state.selected_recipes):
    color = SLOT_COLORS[i]
    badges_html += f'<span class="recipe-badge" style="background:{color};">{RECIPE_EMOJIS[i]} {r["name"]}</span>'

st.markdown(f"""
<div class="app-header">
    <div style="font-size:32px;">🥗</div>
    <h1>Meal Prep Planner</h1>
    <p>2 people · Mon–Fri · up to 3 recipes</p>
    <div style="margin-top:10px;">{badges_html}</div>
</div>
""", unsafe_allow_html=True)

# ── Tabs ─────────────────────────────────────────────────────────────────────

recipe_count = len(st.session_state.selected_recipes)
tab_label_2 = f"🍽️ Recipes ({recipe_count})" if recipe_count else "🍽️ Recipes"

tab1, tab2, tab3 = st.tabs(["🥬 Ingredients", tab_label_2, "🛒 Shopping List"])

# ════════════════════════════════════════════════════════════════════════════
# TAB 1 — INGREDIENTS
# ════════════════════════════════════════════════════════════════════════════

with tab1:
    mode = st.radio(
        "mode",
        ["🍽️ Choose Cuisine", "🔗 Drop a Recipe Link"],
        horizontal=True,
        label_visibility="collapsed",
    )

    # ── Cuisine mode ──────────────────────────────────────────────────────

    if mode == "🍽️ Choose Cuisine":
        st.markdown("##### Select a Cuisine")
        cuisine_cols = st.columns(len(CUISINES))
        for i, (name, data) in enumerate(CUISINES.items()):
            with cuisine_cols[i]:
                active = st.session_state.active_cuisine == name
                btn_type = "primary" if active else "secondary"
                if st.button(f"{data['emoji']}\n{name}", key=f"cuisine_{name}", use_container_width=True, type=btn_type):
                    st.session_state.active_cuisine = name
                    st.rerun()

        cuisine = CUISINES[st.session_state.active_cuisine]
        st.markdown(f"##### Base Ingredients — {st.session_state.active_cuisine} {cuisine['emoji']}")

        ing_cols = st.columns(4)
        for i, ing in enumerate(cuisine["ingredients"]):
            with ing_cols[i % 4]:
                st.markdown(f"""
                <div class="ingredient-card" style="background:{cuisine['color']}; border:1px solid {cuisine['accent']}33;">
                    <div class="ing-emoji">{ing['emoji']}</div>
                    <div class="ing-name">{ing['name']}</div>
                </div>
                """, unsafe_allow_html=True)

        st.info(f"👉 Go to **Recipes** and pick up to **3 recipes** for your week.")

    # ── Custom URL mode ───────────────────────────────────────────────────

    else:
        st.markdown("##### Drop a Recipe Link 🔗")
        st.caption("Paste any recipe URL. We'll read the page, extract the ingredients, and add it to your lineup. Works with AllRecipes, Food Network, NYT Cooking, Tasty, and most recipe sites.")

        url_input = st.text_input(
            "Recipe URL",
            placeholder="https://www.allrecipes.com/recipe/...",
            label_visibility="collapsed",
        )

        fetch_col, _ = st.columns([1, 3])
        with fetch_col:
            fetch_clicked = st.button(
                "Fetch Recipe",
                disabled=not url_input.strip() or len(st.session_state.selected_recipes) >= MAX_RECIPES,
                use_container_width=True,
            )

        if fetch_clicked and url_input.strip():
            with st.spinner("Reading your recipe..."):
                result = scrape_recipe(url_input.strip())
            if result is None:
                st.session_state.url_error = "Couldn't find recipe data on that page. Try a different URL."
                st.session_state.custom_recipe = None
            elif "error" in result:
                st.session_state.url_error = result["error"]
                st.session_state.custom_recipe = None
            else:
                st.session_state.custom_recipe = result
                st.session_state.url_error = ""

        if st.session_state.url_error:
            st.error(f"⚠️ {st.session_state.url_error}")

        if st.session_state.custom_recipe:
            cr = st.session_state.custom_recipe
            with st.container(border=True):
                st.markdown(f"**{cr['name']}**")
                st.caption(f"⏱ {cr['time']} · ~{cr['cal']} cal/serving")

                ing_cols = st.columns(4)
                for i, ing in enumerate(cr["ingredients"][:8]):
                    with ing_cols[i % 4]:
                        st.markdown(f"""
                        <div class="ingredient-card">
                            <div class="ing-emoji">{ing['emoji']}</div>
                            <div class="ing-name">{ing['name'][:20]}</div>
                        </div>
                        """, unsafe_allow_html=True)

                already_added = any(r["id"] == cr["id"] for r in st.session_state.selected_recipes)
                if already_added:
                    st.success("✓ Added to your recipes")
                elif len(st.session_state.selected_recipes) >= MAX_RECIPES:
                    st.warning("Max 3 recipes selected. Remove one to add this.")
                else:
                    if st.button(f"➕ Add to My Recipes ({len(st.session_state.selected_recipes)}/3)", use_container_width=True, type="primary"):
                        st.session_state.selected_recipes.append(cr)
                        st.session_state.checked_items = set()
                        st.rerun()
        else:
            st.markdown("""
            <div style="text-align:center; padding:30px; background:#fafafa; border-radius:12px; border:1px dashed #ddd; margin-top:10px;">
                <div style="font-size:36px;">🌐</div>
                <div style="font-size:13px; color:#888; margin-top:8px;">Works with AllRecipes, Food Network, Tasty, NYT Cooking, and most recipe sites.</div>
            </div>
            """, unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════
# TAB 2 — RECIPES
# ════════════════════════════════════════════════════════════════════════════

with tab2:
    # Selection counter
    counter_html = ""
    for i in range(MAX_RECIPES):
        if i < len(st.session_state.selected_recipes):
            color = SLOT_COLORS[i]
            counter_html += f'<span style="display:inline-flex;align-items:center;justify-content:center;width:26px;height:26px;border-radius:50%;background:{color};color:white;font-size:11px;font-weight:700;margin:0 3px;">✓</span>'
        else:
            counter_html += f'<span style="display:inline-flex;align-items:center;justify-content:center;width:26px;height:26px;border-radius:50%;background:#e0e0e0;color:#888;font-size:11px;font-weight:700;margin:0 3px;">{i+1}</span>'

    st.markdown(f"""
    <div style="background:#f8f8f8;border-radius:12px;padding:12px 16px;margin-bottom:16px;display:flex;justify-content:space-between;align-items:center;">
        <div>
            <div style="font-size:13px;font-weight:700;color:#333;">Select up to 3 recipes</div>
            <div style="font-size:11px;color:#888;margin-top:2px;">Mix cuisines or add a custom link</div>
        </div>
        <div>{counter_html}</div>
    </div>
    """, unsafe_allow_html=True)

    # Cuisine filter
    filter_cols = st.columns(len(CUISINES))
    for i, (name, data) in enumerate(CUISINES.items()):
        with filter_cols[i]:
            active = st.session_state.active_cuisine == name
            if st.button(f"{data['emoji']} {name}", key=f"filter_{name}", use_container_width=True,
                         type="primary" if active else "secondary"):
                st.session_state.active_cuisine = name
                st.rerun()

    st.markdown("---")

    # Recipe cards
    cuisine_data = CUISINES[st.session_state.active_cuisine]
    for recipe in cuisine_data["recipes"]:
        slot_idx = next(
            (i for i, r in enumerate(st.session_state.selected_recipes) if r["id"] == recipe["id"]),
            -1,
        )
        is_selected = slot_idx >= 0
        border_color = SLOT_COLORS[slot_idx] if is_selected else "#e8e8e8"
        bg_color = SLOT_BG[slot_idx] if is_selected else "#fafafa"
        text_color = SLOT_COLORS[slot_idx] if is_selected else "inherit"

        with st.container(border=False):
            st.markdown(f"""
            <div style="border:2px solid {border_color};border-radius:14px;background:{bg_color};padding:13px 14px 8px;margin-bottom:4px;">
            """, unsafe_allow_html=True)

            col1, col2 = st.columns([3, 1])
            with col1:
                slot_badge = f'<span style="background:{SLOT_COLORS[slot_idx]};color:white;border-radius:10px;padding:1px 8px;font-size:10px;font-weight:700;margin-right:6px;">{SLOT_LABELS[slot_idx]}</span>' if is_selected else ""
                st.markdown(f'{slot_badge}<span style="font-weight:700;color:{text_color};">{recipe["name"]}</span>', unsafe_allow_html=True)
                st.markdown(f'<span style="font-size:12px;opacity:0.65;">⏱ {recipe["time"]} · ~{recipe["cal"]} cal/serving</span>', unsafe_allow_html=True)
            with col2:
                can_add = len(st.session_state.selected_recipes) < MAX_RECIPES
                if is_selected:
                    if st.button("✓ Added", key=f"btn_{recipe['id']}", type="primary", use_container_width=True):
                        st.session_state.selected_recipes = [
                            r for r in st.session_state.selected_recipes if r["id"] != recipe["id"]
                        ]
                        st.session_state.checked_items = set()
                        st.rerun()
                else:
                    if st.button("+ Add", key=f"btn_{recipe['id']}", disabled=not can_add, use_container_width=True):
                        st.session_state.selected_recipes.append(recipe)
                        st.session_state.checked_items = set()
                        st.rerun()

            st.markdown("</div>", unsafe_allow_html=True)

            # Expandable details
            detail = RECIPE_DATA.get(recipe["id"])
            if detail:
                with st.expander("View details"):
                    macros = detail["macros"]
                    m1, m2, m3, m4 = st.columns(4)
                    m1.metric("🔥 Cal", macros["cal"])
                    m2.metric("💪 Protein", f"{macros['protein']}g")
                    m3.metric("🍞 Carbs", f"{macros['carbs']}g")
                    m4.metric("🫙 Fat", f"{macros['fat']}g")
                    st.markdown("**Instructions**")
                    for step_i, step in enumerate(detail["instructions"]):
                        st.markdown(f"{step_i + 1}. {step}")

        st.markdown("<div style='margin-bottom:6px;'></div>", unsafe_allow_html=True)

    # Weekly schedule
    if st.session_state.selected_recipes:
        st.markdown("---")
        st.markdown("#### 📅 Your Weekly Meal Schedule")
        assignments = assign_days(len(st.session_state.selected_recipes))
        for day_i, day in enumerate(DAYS):
            recipe_idx = assignments[day_i]
            recipe = st.session_state.selected_recipes[recipe_idx]
            color = SLOT_COLORS[recipe_idx]
            col_a, col_b = st.columns([1, 2])
            col_a.markdown(f"**{day}**")
            col_b.markdown(f'<span style="background:{color};color:white;border-radius:20px;padding:3px 12px;font-size:12px;font-weight:700;">{RECIPE_EMOJIS[recipe_idx]} {recipe["name"]}</span>', unsafe_allow_html=True)

        if st.button("🛒 Build Shopping List →", use_container_width=True, type="primary"):
            st.info("Click the **🛒 Shopping List** tab above to see your list.")

# ════════════════════════════════════════════════════════════════════════════
# TAB 3 — SHOPPING LIST
# ════════════════════════════════════════════════════════════════════════════

with tab3:
    if not st.session_state.selected_recipes:
        st.markdown("""
        <div style="text-align:center;padding:60px 20px;color:#888;">
            <div style="font-size:48px;">🛒</div>
            <div style="font-size:15px;font-weight:600;margin-top:12px;">No recipes selected yet</div>
            <div style="font-size:13px;margin-top:6px;">Head to Recipes and pick 1–3 meals for the week.</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        # Recipe summary
        assignments = assign_days(len(st.session_state.selected_recipes))
        for i, recipe in enumerate(st.session_state.selected_recipes):
            days_count = assignments.count(i)
            color = SLOT_COLORS[i]
            bg = SLOT_BG[i]
            st.markdown(f"""
            <div style="background:{bg};border:1px solid {color}33;border-radius:10px;padding:9px 14px;margin-bottom:7px;display:flex;justify-content:space-between;align-items:center;">
                <div>
                    <span style="background:{color};color:white;border-radius:10px;padding:1px 8px;font-size:10px;font-weight:700;margin-right:6px;">{SLOT_LABELS[i]}</span>
                    <span style="font-size:13px;font-weight:600;color:#333;">{recipe['name']}</span>
                </div>
                <span style="font-size:12px;color:#888;">{days_count} day{'s' if days_count != 1 else ''}</span>
            </div>
            """, unsafe_allow_html=True)

        st.caption("Check off items as you shop")
        st.markdown("---")

        shopping_list = build_shopping_list(st.session_state.selected_recipes)
        total_items = sum(len(block["items"]) for block in shopping_list)
        checked_count = len(st.session_state.checked_items)

        for block in shopping_list:
            cat = block["cat"]
            icon = CAT_ICONS.get(cat, "📦")
            st.markdown(f"**{icon} {cat}**")

            for item in block["items"]:
                slot_idx = item["slot_idx"]
                item_key = f"{cat}_{item['name']}_{slot_idx}"
                is_checked = item_key in st.session_state.checked_items
                accent = SLOT_COLORS[slot_idx]

                col_check, col_name, col_qty = st.columns([0.5, 3, 1.5])
                with col_check:
                    checked = st.checkbox(
                        "",
                        value=is_checked,
                        key=f"chk_{item_key}",
                        label_visibility="collapsed",
                    )
                    if checked and item_key not in st.session_state.checked_items:
                        st.session_state.checked_items.add(item_key)
                        st.rerun()
                    elif not checked and item_key in st.session_state.checked_items:
                        st.session_state.checked_items.discard(item_key)
                        st.rerun()

                with col_name:
                    name_style = "text-decoration:line-through;color:#aaa;" if is_checked else "color:#333;"
                    st.markdown(
                        f'<span style="{name_style}">{item["name"]}</span>'
                        f'<br><span style="font-size:10px;color:{accent};font-weight:600;">'
                        f'{RECIPE_EMOJIS[slot_idx]} {item["recipe_name"]}</span>',
                        unsafe_allow_html=True,
                    )
                with col_qty:
                    qty_color = "#bbb" if is_checked else accent
                    st.markdown(f'<span style="font-size:12px;font-weight:700;color:{qty_color};">{item["qty"]}</span>', unsafe_allow_html=True)

            st.markdown("<div style='margin-bottom:8px;'></div>", unsafe_allow_html=True)

        # Progress bar
        st.markdown("---")
        progress = checked_count / total_items if total_items else 0
        st.markdown(f"**{checked_count} of {total_items} items checked**")
        st.progress(progress)

        if checked_count == total_items and total_items > 0:
            st.success("✅ All done! Time to cook!")

        if st.button("↺ Reset List", use_container_width=False):
            st.session_state.checked_items = set()
            st.rerun()
