import math


def _it1_shopping(s):
    return [
        {"cat": "Proteins", "items": [
            {"name": "Ground beef (80/20)", "qty": f"{s * 0.3:.1f} lbs"},
            {"name": "Parmesan cheese", "qty": f"{math.ceil(s * 0.8)} oz"},
        ]},
        {"cat": "Produce", "items": [
            {"name": "Yellow onion", "qty": f"{math.ceil(s * 0.3)} large"},
            {"name": "Garlic", "qty": f"{math.ceil(s * 0.2)} heads"},
            {"name": "Fresh basil", "qty": "1 bunch"},
        ]},
        {"cat": "Pantry", "items": [
            {"name": "Spaghetti", "qty": f"{s * 0.3:.1f} lbs"},
            {"name": "Canned crushed tomatoes", "qty": f"{math.ceil(s * 0.4)} cans (28oz)"},
            {"name": "Tomato paste", "qty": f"{math.ceil(s * 0.2)} cans (6oz)"},
            {"name": "Olive oil", "qty": "1 bottle"},
            {"name": "Red wine (cooking)", "qty": "1 bottle"},
            {"name": "Italian seasoning", "qty": "1 jar"},
        ]},
    ]


def _it2_shopping(s):
    return [
        {"cat": "Proteins", "items": [
            {"name": "Chicken breast", "qty": f"{s * 0.4:.1f} lbs"},
            {"name": "Parmesan cheese", "qty": f"{math.ceil(s * 0.6)} oz"},
        ]},
        {"cat": "Produce", "items": [
            {"name": "Fresh basil", "qty": f"{math.ceil(s / 5)} bunches"},
            {"name": "Garlic", "qty": "1 head"},
            {"name": "Lemon", "qty": f"{math.ceil(s * 0.2)}"},
        ]},
        {"cat": "Pantry", "items": [
            {"name": "Penne pasta", "qty": f"{s * 0.3:.1f} lbs"},
            {"name": "Pesto (jar)", "qty": f"{math.ceil(s * 0.2)} jars (6oz)"},
            {"name": "Sun-dried tomatoes", "qty": "1 jar"},
            {"name": "Olive oil", "qty": "1 bottle"},
            {"name": "Pine nuts", "qty": "4 oz"},
        ]},
    ]


def _it3_shopping(s):
    return [
        {"cat": "Produce", "items": [
            {"name": "Yellow onion", "qty": f"{math.ceil(s * 0.3)} large"},
            {"name": "Carrots", "qty": f"{math.ceil(s * 0.4)} medium"},
            {"name": "Garlic", "qty": f"{math.ceil(s * 0.2)} heads"},
            {"name": "Baby spinach", "qty": f"{math.ceil(s / 5) * 2} oz bags"},
        ]},
        {"cat": "Pantry", "items": [
            {"name": "Cannellini beans (canned)", "qty": f"{math.ceil(s * 0.6)} cans (15oz)"},
            {"name": "Crushed tomatoes", "qty": f"{math.ceil(s * 0.3)} cans (28oz)"},
            {"name": "Ditalini pasta", "qty": f"{s * 0.15:.1f} lbs"},
            {"name": "Vegetable broth", "qty": f"{math.ceil(s * 0.4)} cartons (32oz)"},
            {"name": "Olive oil", "qty": "1 bottle"},
            {"name": "Dried rosemary", "qty": "1 jar"},
        ]},
        {"cat": "Dairy", "items": [
            {"name": "Parmesan cheese", "qty": f"{math.ceil(s * 0.6)} oz"},
        ]},
    ]


def _mx1_shopping(s):
    return [
        {"cat": "Proteins", "items": [
            {"name": "Chicken breast", "qty": f"{s * 0.4:.1f} lbs"},
            {"name": "Mexican cheese blend", "qty": f"{math.ceil(s * 1.2)} oz"},
        ]},
        {"cat": "Produce", "items": [
            {"name": "Limes", "qty": f"{math.ceil(s * 0.6)}"},
            {"name": "Cilantro", "qty": "1 bunch"},
            {"name": "Avocados", "qty": f"{math.ceil(s * 0.5)}"},
            {"name": "Jalapeño", "qty": f"{math.ceil(s * 0.2)}"},
        ]},
        {"cat": "Pantry", "items": [
            {"name": "Jasmine rice", "qty": f"{s * 0.4:.1f} lbs"},
            {"name": "Black beans (canned)", "qty": f"{math.ceil(s * 0.6)} cans (15oz)"},
            {"name": "Corn (frozen)", "qty": f"{s * 0.2:.1f} lbs"},
            {"name": "Salsa", "qty": f"{math.ceil(s * 0.2)} jars (16oz)"},
            {"name": "Cumin", "qty": "1 jar"},
            {"name": "Chili powder", "qty": "1 jar"},
        ]},
    ]


def _mx2_shopping(s):
    return [
        {"cat": "Produce", "items": [
            {"name": "Tomatoes", "qty": f"{math.ceil(s * 0.6)} medium"},
            {"name": "Red onion", "qty": f"{math.ceil(s * 0.2)} large"},
            {"name": "Jalapeño", "qty": f"{math.ceil(s * 0.3)}"},
            {"name": "Cilantro", "qty": f"{math.ceil(s / 5)} bunches"},
            {"name": "Avocados", "qty": f"{math.ceil(s * 0.8)}"},
            {"name": "Limes", "qty": f"{math.ceil(s * 0.8)}"},
            {"name": "Garlic", "qty": "1 head"},
        ]},
        {"cat": "Pantry", "items": [
            {"name": "Black beans (canned)", "qty": f"{math.ceil(s * 0.8)} cans (15oz)"},
            {"name": "Flour tortillas (large)", "qty": f"{s * 2} count"},
            {"name": "Cumin", "qty": "1 jar"},
            {"name": "Olive oil", "qty": "1 bottle"},
        ]},
        {"cat": "Dairy", "items": [
            {"name": "Mexican cheese blend", "qty": f"{math.ceil(s * 1.2)} oz"},
            {"name": "Sour cream", "qty": f"{math.ceil(s * 1.6)} oz"},
        ]},
    ]


def _mx3_shopping(s):
    return [
        {"cat": "Proteins", "items": [
            {"name": "Beef sirloin", "qty": f"{s * 0.4:.1f} lbs"},
            {"name": "Mexican cheese blend", "qty": f"{math.ceil(s)} oz"},
        ]},
        {"cat": "Produce", "items": [
            {"name": "Bell peppers (mixed)", "qty": f"{math.ceil(s * 0.8)} large"},
            {"name": "Yellow onion", "qty": f"{math.ceil(s * 0.4)} large"},
            {"name": "Limes", "qty": f"{math.ceil(s * 0.6)}"},
            {"name": "Cilantro", "qty": "1 bunch"},
            {"name": "Garlic", "qty": "1 head"},
        ]},
        {"cat": "Pantry", "items": [
            {"name": "Flour tortillas", "qty": f"{s * 2} count"},
            {"name": "Salsa", "qty": "1 jar (16oz)"},
            {"name": "Cumin", "qty": "1 jar"},
            {"name": "Chili powder", "qty": "1 jar"},
            {"name": "Olive oil", "qty": "1 bottle"},
        ]},
    ]


def _as1_shopping(s):
    return [
        {"cat": "Proteins", "items": [
            {"name": "Chicken thighs (boneless)", "qty": f"{s * 0.4:.1f} lbs"},
        ]},
        {"cat": "Produce", "items": [
            {"name": "Broccoli", "qty": f"{math.ceil(s * 0.3)} heads"},
            {"name": "Garlic", "qty": f"{math.ceil(s * 0.2)} heads"},
            {"name": "Fresh ginger", "qty": "1 knob"},
            {"name": "Green onion", "qty": f"{math.ceil(s / 5)} bunches"},
        ]},
        {"cat": "Pantry", "items": [
            {"name": "Jasmine rice", "qty": f"{s * 0.4:.1f} lbs"},
            {"name": "Soy sauce", "qty": "1 bottle"},
            {"name": "Mirin", "qty": "1 bottle"},
            {"name": "Sesame oil", "qty": "1 bottle"},
            {"name": "Teriyaki sauce", "qty": f"{math.ceil(s / 5)} bottles"},
            {"name": "Sesame seeds", "qty": "1 bag"},
        ]},
    ]


def _as2_shopping(s):
    return [
        {"cat": "Proteins", "items": [
            {"name": "Beef sirloin", "qty": f"{s * 0.35:.1f} lbs"},
        ]},
        {"cat": "Produce", "items": [
            {"name": "Garlic", "qty": f"{math.ceil(s * 0.2)} heads"},
            {"name": "Carrots", "qty": f"{math.ceil(s * 0.4)} medium"},
            {"name": "Broccoli", "qty": f"{math.ceil(s * 0.2)} heads"},
            {"name": "Snap peas", "qty": f"{math.ceil(s * 1.2)} oz"},
            {"name": "Green onion", "qty": f"{math.ceil(s / 5)} bunches"},
        ]},
        {"cat": "Pantry", "items": [
            {"name": "Lo mein noodles", "qty": f"{s * 0.2:.1f} lbs"},
            {"name": "Soy sauce", "qty": "1 bottle"},
            {"name": "Sesame oil", "qty": "1 bottle"},
            {"name": "Oyster sauce", "qty": "1 bottle"},
            {"name": "Chili paste", "qty": "1 jar"},
        ]},
    ]


def _as3_shopping(s):
    return [
        {"cat": "Proteins", "items": [
            {"name": "Extra-firm tofu", "qty": f"{math.ceil(s * 0.4)} blocks (14oz)"},
            {"name": "Eggs", "qty": f"{math.ceil(s * 0.4)} eggs"},
        ]},
        {"cat": "Produce", "items": [
            {"name": "Garlic", "qty": f"{math.ceil(s * 0.2)} heads"},
            {"name": "Carrots", "qty": f"{math.ceil(s * 0.3)} medium"},
            {"name": "Green onion", "qty": f"{math.ceil(s / 5)} bunches"},
        ]},
        {"cat": "Pantry", "items": [
            {"name": "Jasmine rice", "qty": f"{s * 0.4:.1f} lbs"},
            {"name": "Frozen peas", "qty": f"{s * 0.1:.1f} lbs"},
            {"name": "Soy sauce", "qty": "1 bottle"},
            {"name": "Sesame oil", "qty": "1 bottle"},
        ]},
    ]


def _md1_shopping(s):
    return [
        {"cat": "Proteins", "items": [
            {"name": "Chicken breast", "qty": f"{s * 0.4:.1f} lbs"},
            {"name": "Feta cheese", "qty": f"{math.ceil(s * 1.0)} oz"},
        ]},
        {"cat": "Produce", "items": [
            {"name": "Cucumber", "qty": f"{math.ceil(s * 0.4)} large"},
            {"name": "Cherry tomatoes", "qty": f"{math.ceil(s * 0.5)} cups"},
            {"name": "Red onion", "qty": f"{math.ceil(s * 0.2)} large"},
            {"name": "Lemon", "qty": f"{math.ceil(s * 0.4)}"},
            {"name": "Garlic", "qty": "1 head"},
            {"name": "Fresh parsley", "qty": "1 bunch"},
        ]},
        {"cat": "Pantry", "items": [
            {"name": "Quinoa", "qty": f"{s * 0.3:.1f} lbs"},
            {"name": "Kalamata olives", "qty": "1 jar"},
            {"name": "Olive oil", "qty": "1 bottle"},
            {"name": "Dried oregano", "qty": "1 jar"},
            {"name": "Hummus", "qty": f"{math.ceil(s * 0.5)} tubs (10oz)"},
        ]},
    ]


def _md2_shopping(s):
    return [
        {"cat": "Produce", "items": [
            {"name": "Fresh parsley", "qty": f"{math.ceil(s / 4)} bunches"},
            {"name": "Fresh cilantro", "qty": f"{math.ceil(s / 5)} bunches"},
            {"name": "Garlic", "qty": f"{math.ceil(s * 0.3)} heads"},
            {"name": "Red onion", "qty": f"{math.ceil(s * 0.3)} large"},
            {"name": "Lemon", "qty": f"{math.ceil(s * 0.5)}"},
            {"name": "Cucumber", "qty": f"{math.ceil(s * 0.3)} large"},
            {"name": "Tomatoes", "qty": f"{math.ceil(s * 0.4)} medium"},
        ]},
        {"cat": "Pantry", "items": [
            {"name": "Chickpeas (canned)", "qty": f"{math.ceil(s * 0.8)} cans (15oz)"},
            {"name": "Pita bread", "qty": f"{s} count"},
            {"name": "Hummus", "qty": f"{math.ceil(s * 0.5)} tubs (10oz)"},
            {"name": "Olive oil", "qty": "1 bottle"},
            {"name": "Cumin", "qty": "1 jar"},
            {"name": "Coriander", "qty": "1 jar"},
        ]},
        {"cat": "Dairy", "items": [
            {"name": "Feta cheese", "qty": f"{math.ceil(s * 0.8)} oz"},
            {"name": "Greek yogurt (for tzatziki)", "qty": f"{math.ceil(s * 0.6)} cups"},
        ]},
    ]


def _md3_shopping(s):
    return [
        {"cat": "Proteins", "items": [
            {"name": "Lamb shoulder (cubed)", "qty": f"{s * 0.4:.1f} lbs"},
        ]},
        {"cat": "Produce", "items": [
            {"name": "Bell peppers (mixed)", "qty": f"{math.ceil(s * 0.6)} large"},
            {"name": "Red onion", "qty": f"{math.ceil(s * 0.3)} large"},
            {"name": "Zucchini", "qty": f"{math.ceil(s * 0.4)} medium"},
            {"name": "Lemon", "qty": f"{math.ceil(s * 0.4)}"},
            {"name": "Garlic", "qty": "1 head"},
            {"name": "Fresh mint", "qty": "1 bunch"},
        ]},
        {"cat": "Pantry", "items": [
            {"name": "Basmati rice", "qty": f"{s * 0.4:.1f} lbs"},
            {"name": "Olive oil", "qty": "1 bottle"},
            {"name": "Cumin", "qty": "1 jar"},
            {"name": "Smoked paprika", "qty": "1 jar"},
            {"name": "Cinnamon", "qty": "1 jar"},
        ]},
        {"cat": "Dairy", "items": [
            {"name": "Greek yogurt (marinade)", "qty": f"{math.ceil(s * 0.5)} cups"},
            {"name": "Feta cheese", "qty": f"{math.ceil(s * 0.6)} oz"},
        ]},
    ]


def _in1_shopping(s):
    return [
        {"cat": "Proteins", "items": [
            {"name": "Chicken breast", "qty": f"{s * 0.4:.1f} lbs"},
        ]},
        {"cat": "Produce", "items": [
            {"name": "Yellow onion", "qty": f"{math.ceil(s * 0.3)} large"},
            {"name": "Garlic", "qty": f"{math.ceil(s * 0.2)} heads"},
            {"name": "Fresh ginger", "qty": "1 knob"},
            {"name": "Cilantro", "qty": "1 bunch"},
        ]},
        {"cat": "Pantry", "items": [
            {"name": "Basmati rice", "qty": f"{s * 0.4:.1f} lbs"},
            {"name": "Canned crushed tomatoes", "qty": f"{math.ceil(s * 0.4)} cans (28oz)"},
            {"name": "Garam masala", "qty": "1 jar"},
            {"name": "Turmeric", "qty": "1 jar"},
            {"name": "Cumin", "qty": "1 jar"},
            {"name": "Chili powder", "qty": "1 jar"},
        ]},
        {"cat": "Dairy", "items": [
            {"name": "Plain yogurt (marinade)", "qty": f"{math.ceil(s * 0.4)} cups"},
            {"name": "Heavy cream", "qty": f"{math.ceil(s * 0.3)} cups"},
        ]},
    ]


def _in2_shopping(s):
    return [
        {"cat": "Produce", "items": [
            {"name": "Yellow onion", "qty": f"{math.ceil(s * 0.3)} large"},
            {"name": "Garlic", "qty": f"{math.ceil(s * 0.2)} heads"},
            {"name": "Fresh ginger", "qty": "1 knob"},
            {"name": "Tomatoes", "qty": f"{math.ceil(s * 0.4)} medium"},
            {"name": "Cilantro", "qty": "1 bunch"},
            {"name": "Dried red chili", "qty": f"{math.ceil(s * 0.2)}"},
        ]},
        {"cat": "Pantry", "items": [
            {"name": "Red lentils", "qty": f"{s * 0.3:.1f} lbs"},
            {"name": "Basmati rice", "qty": f"{s * 0.4:.1f} lbs"},
            {"name": "Cumin seeds", "qty": "1 jar"},
            {"name": "Mustard seeds", "qty": "1 jar"},
            {"name": "Turmeric", "qty": "1 jar"},
            {"name": "Ghee or butter", "qty": f"{math.ceil(s * 0.2)} oz"},
        ]},
    ]


def _in3_shopping(s):
    return [
        {"cat": "Proteins", "items": [
            {"name": "Paneer", "qty": f"{math.ceil(s * 0.4)} blocks (14oz)"},
        ]},
        {"cat": "Produce", "items": [
            {"name": "Yellow onion", "qty": f"{math.ceil(s * 0.3)} large"},
            {"name": "Garlic", "qty": f"{math.ceil(s * 0.2)} heads"},
            {"name": "Fresh ginger", "qty": "1 knob"},
            {"name": "Cilantro", "qty": "1 bunch"},
        ]},
        {"cat": "Pantry", "items": [
            {"name": "Naan bread", "qty": f"{s} count"},
            {"name": "Canned crushed tomatoes", "qty": f"{math.ceil(s * 0.4)} cans (28oz)"},
            {"name": "Cashews", "qty": f"{math.ceil(s * 0.5)} oz"},
            {"name": "Garam masala", "qty": "1 jar"},
            {"name": "Turmeric", "qty": "1 jar"},
            {"name": "Kasuri methi (dried fenugreek)", "qty": "1 jar"},
        ]},
        {"cat": "Dairy", "items": [
            {"name": "Butter", "qty": f"{math.ceil(s * 0.3)} oz"},
            {"name": "Heavy cream", "qty": f"{math.ceil(s * 0.4)} cups"},
        ]},
    ]


RECIPE_DATA = {
    "it1": {
        "instructions": [
            "Brown 1.5 lbs ground beef with diced onion and garlic.",
            "Add canned tomatoes, tomato paste, red wine, seasoning. Simmer 25 min.",
            "Cook spaghetti al dente. Drain and divide into containers.",
            "Top with bolognese and parmesan.",
        ],
        "macros": {"cal": 620, "protein": 38, "carbs": 72, "fat": 18},
        "get_shopping": _it1_shopping,
    },
    "it2": {
        "instructions": [
            "Season chicken breast with salt, pepper, garlic powder. Grill or pan-sear.",
            "Cook penne pasta. Reserve 1 cup pasta water.",
            "Toss pasta with pesto, loosening with pasta water.",
            "Slice chicken and divide with pasta. Top with parmesan and sun-dried tomatoes.",
        ],
        "macros": {"cal": 580, "protein": 42, "carbs": 65, "fat": 16},
        "get_shopping": _it2_shopping,
    },
    "it3": {
        "instructions": [
            "Sauté onion, garlic, and carrots in olive oil.",
            "Add canned tomatoes, cannellini beans, broth, and pasta. Simmer 20 min.",
            "Season with rosemary, salt, pepper. Add spinach last 2 min.",
            "Divide into containers. Drizzle olive oil and top with parmesan.",
        ],
        "macros": {"cal": 490, "protein": 22, "carbs": 78, "fat": 12},
        "get_shopping": _it3_shopping,
    },
    "mx1": {
        "instructions": [
            "Season chicken with cumin, chili powder, garlic powder. Grill or bake at 400°F for 25 min.",
            "Cook jasmine rice. Season black beans with cumin and lime juice.",
            "Roast corn at 425°F for 15 min.",
            "Divide rice into containers. Top with chicken, beans, corn, salsa, and cheese.",
        ],
        "macros": {"cal": 650, "protein": 48, "carbs": 70, "fat": 14},
        "get_shopping": _mx1_shopping,
    },
    "mx2": {
        "instructions": [
            "Warm black beans with cumin, garlic, lime juice, and salt.",
            "Dice tomatoes, onion, jalapeño, cilantro into pico de gallo.",
            "Warm tortillas. Mash avocado with lime and salt.",
            "Pack 2 tortillas per container with beans, pico, cheese, and guacamole.",
        ],
        "macros": {"cal": 520, "protein": 18, "carbs": 76, "fat": 16},
        "get_shopping": _mx2_shopping,
    },
    "mx3": {
        "instructions": [
            "Slice beef sirloin, bell peppers, and onions into strips.",
            "Marinate beef in lime, cumin, chili powder, garlic for 30 min.",
            "Sear beef in cast iron 3-4 min. Cook veggies in same pan.",
            "Divide into containers with warmed tortillas, salsa, and cheese.",
        ],
        "macros": {"cal": 590, "protein": 44, "carbs": 52, "fat": 20},
        "get_shopping": _mx3_shopping,
    },
    "as1": {
        "instructions": [
            "Marinate chicken thighs in soy sauce, mirin, sesame oil, garlic, ginger for 30 min.",
            "Cook jasmine rice. Blanch broccoli for 2 min.",
            "Pan-fry chicken 5-6 min per side. Brush with teriyaki glaze.",
            "Divide into containers. Top with chicken, broccoli, and sesame seeds.",
        ],
        "macros": {"cal": 610, "protein": 46, "carbs": 68, "fat": 14},
        "get_shopping": _as1_shopping,
    },
    "as2": {
        "instructions": [
            "Cook lo mein noodles. Rinse with cold water, toss with sesame oil.",
            "Slice beef sirloin thin. Stir-fry in hot wok 2-3 min. Set aside.",
            "Stir-fry garlic, carrots, broccoli, snap peas for 4 min. Add beef back.",
            "Toss with garlic soy sauce. Divide into containers. Top with green onion.",
        ],
        "macros": {"cal": 570, "protein": 40, "carbs": 62, "fat": 16},
        "get_shopping": _as2_shopping,
    },
    "as3": {
        "instructions": [
            "Press and cube tofu. Pan-fry until golden, 4 min per side.",
            "Cook jasmine rice. Scramble eggs and set aside.",
            "Stir-fry garlic, carrots, peas, and green onion. Add rice and soy sauce.",
            "Add tofu and eggs. Toss together. Divide. Drizzle sesame oil.",
        ],
        "macros": {"cal": 480, "protein": 24, "carbs": 72, "fat": 14},
        "get_shopping": _as3_shopping,
    },
    "md1": {
        "instructions": [
            "Marinate chicken in lemon juice, olive oil, oregano, and garlic for 30 min.",
            "Grill or pan-sear chicken 5-6 min per side until cooked through.",
            "Cook quinoa. Slice cucumber, halve tomatoes, pit olives.",
            "Assemble bowls with quinoa, sliced chicken, veggies, feta, hummus, and a lemon drizzle.",
        ],
        "macros": {"cal": 580, "protein": 44, "carbs": 52, "fat": 18},
        "get_shopping": _md1_shopping,
    },
    "md2": {
        "instructions": [
            "Blend chickpeas, parsley, cilantro, garlic, cumin, coriander, and salt. Form into patties.",
            "Pan-fry falafel patties in olive oil 3-4 min per side until golden.",
            "Make tzatziki: grate cucumber, mix with yogurt, garlic, dill, lemon.",
            "Plate with warm pita, falafel, hummus, tzatziki, sliced tomatoes, and cucumber.",
        ],
        "macros": {"cal": 510, "protein": 18, "carbs": 72, "fat": 16},
        "get_shopping": _md2_shopping,
    },
    "md3": {
        "instructions": [
            "Cube lamb, marinate in yogurt, lemon, garlic, cumin, and paprika for 1 hour.",
            "Thread lamb onto skewers alternating with bell peppers, onion, and zucchini.",
            "Grill skewers 8-10 min, turning every 2-3 min.",
            "Serve over basmati rice with feta crumbles and fresh mint.",
        ],
        "macros": {"cal": 620, "protein": 46, "carbs": 48, "fat": 20},
        "get_shopping": _md3_shopping,
    },
    "in1": {
        "instructions": [
            "Marinate chicken in yogurt, garam masala, turmeric, chili powder for 1 hour. Broil 12-15 min.",
            "Sauté onion, garlic, ginger until golden. Add tomatoes and spices, cook 10 min.",
            "Add cream, simmer 5 min. Add broiled chicken, simmer 10 more min.",
            "Serve over basmati rice. Garnish with fresh cilantro.",
        ],
        "macros": {"cal": 640, "protein": 48, "carbs": 58, "fat": 22},
        "get_shopping": _in1_shopping,
    },
    "in2": {
        "instructions": [
            "Rinse red lentils. Simmer with water, turmeric, and salt for 20 min until soft.",
            "Heat ghee in a pan. Fry cumin seeds, mustard seeds, dried chili until they pop.",
            "Add garlic, ginger, onion, tomatoes. Cook 8 min. Pour over lentils and stir.",
            "Serve dal over basmati rice. Top with fresh cilantro.",
        ],
        "macros": {"cal": 490, "protein": 22, "carbs": 82, "fat": 10},
        "get_shopping": _in2_shopping,
    },
    "in3": {
        "instructions": [
            "Cube paneer. Pan-fry in butter until golden on all sides. Set aside.",
            "Blend tomatoes and cashews into a smooth sauce.",
            "Cook onion, garlic, ginger until golden. Add tomato-cashew sauce, spices, and cream.",
            "Add paneer, simmer 10 min. Finish with kasuri methi. Serve with warm naan.",
        ],
        "macros": {"cal": 560, "protein": 24, "carbs": 46, "fat": 28},
        "get_shopping": _in3_shopping,
    },
}


def get_shopping(recipe_id, servings):
    """Return shopping list for a recipe scaled to number of servings."""
    data = RECIPE_DATA.get(recipe_id)
    if not data or "get_shopping" not in data:
        return []
    return data["get_shopping"](servings)
