import heapq
import streamlit as st
import pandas as pd

foods = [
    {"food": "Oats (100g)", "cost": 35, "protein": 12, "calories": 380, "veg": True},
    {"food": "Rice (100g)", "cost": 15, "protein": 2, "calories": 360, "veg": True},
    {"food": "Wheat Roti (1 pc)", "cost": 8, "protein": 3, "calories": 120, "veg": True},
    {"food": "Dal (100g cooked)", "cost": 25, "protein": 9, "calories": 120, "veg": True},
    {"food": "Chana (100g)", "cost": 18, "protein": 19, "calories": 364, "veg": True},
    {"food": "Rajma (100g)", "cost": 20, "protein": 15, "calories": 330, "veg": True},
    {"food": "Soya Chunks (50g)", "cost": 25, "protein": 26, "calories": 170, "veg": True},
    {"food": "Paneer (100g)", "cost": 60, "protein": 22, "calories": 360, "veg": True},
    {"food": "Milk (200ml)", "cost": 12, "protein": 6, "calories": 122, "veg": True},
    {"food": "Curd (100g)", "cost": 15, "protein": 4, "calories": 98, "veg": True},
    {"food": "Potato (100g)", "cost": 10, "protein": 2, "calories": 87, "veg": True},
    {"food": "Spinach (100g)", "cost": 15, "protein": 3, "calories": 23, "veg": True},
    {"food": "Broccoli (100g)", "cost": 30, "protein": 3, "calories": 34, "veg": True},
    {"food": "Carrot (100g)", "cost": 12, "protein": 1, "calories": 41, "veg": True},
    {"food": "Apple (1 pc)", "cost": 20, "protein": 0, "calories": 95, "veg": True},
    {"food": "Banana (1 pc)", "cost": 8, "protein": 1, "calories": 105, "veg": True},
    {"food": "Orange (1 pc)", "cost": 15, "protein": 1, "calories": 62, "veg": True},
    {"food": "Peanuts (50g)", "cost": 15, "protein": 13, "calories": 280, "veg": True},
    {"food": "Almonds (30g)", "cost": 25, "protein": 6, "calories": 170, "veg": True},
    {"food": "Cashews (30g)", "cost": 30, "protein": 5, "calories": 160, "veg": True},
    {"food": "Walnuts (30g)", "cost": 35, "protein": 4, "calories": 180, "veg": True},
    {"food": "Peanut Butter (2 tbsp)", "cost": 20, "protein": 8, "calories": 188, "veg": True},
    {"food": "Bread (2 slices)", "cost": 12, "protein": 6, "calories": 150, "veg": True},
    {"food": "Biscuits (4 pcs)", "cost": 10, "protein": 2, "calories": 120, "veg": True},
    {"food": "Eggs (2 pcs)", "cost": 12, "protein": 13, "calories": 155, "veg": False},
    {"food": "Boiled Egg (1 pc)", "cost": 6, "protein": 6, "calories": 70, "veg": False},
    {"food": "Chicken Breast (100g)", "cost": 40, "protein": 31, "calories": 165, "veg": False},
    {"food": "Chicken Curry (150g)", "cost": 60, "protein": 25, "calories": 280, "veg": False},
    {"food": "Fish (100g)", "cost": 60, "protein": 22, "calories": 200, "veg": False},
    {"food": "Prawns (100g)", "cost": 80, "protein": 24, "calories": 99, "veg": False},
    {"food": "Mutton (100g)", "cost": 120, "protein": 25, "calories": 250, "veg": False},
    {"food": "Salmon (100g)", "cost": 100, "protein": 25, "calories": 207, "veg": False},
    {"food": "Tuna (100g)", "cost": 90, "protein": 25, "calories": 132, "veg": False},
    {"food": "Sardines (100g)", "cost": 70, "protein": 24, "calories": 208, "veg": False},
    {"food": "Turkey Breast (100g)", "cost": 80, "protein": 29, "calories": 135, "veg": False},
    {"food": "Lean Beef (100g)", "cost": 110, "protein": 26, "calories": 250, "veg": False},
    {"food": "Hemp Seeds (30g)", "cost": 30, "protein": 10, "calories": 170, "veg": True},
    {"food": "Chia Seeds (20g)", "cost": 20, "protein": 4, "calories": 97, "veg": True},
    {"food": "Buckwheat (100g)", "cost": 40, "protein": 13, "calories": 343, "veg": True},
    {"food": "Barley (100g)", "cost": 25, "protein": 12, "calories": 354, "veg": True},
    {"food": "Black Beans (100g)", "cost": 22, "protein": 21, "calories": 339, "veg": True},
    {"food": "Lentils (100g)", "cost": 18, "protein": 9, "calories": 116, "veg": True},
    {"food": "Peas (100g)", "cost": 18, "protein": 5, "calories": 81, "veg": True},
    {"food": "Quinoa (100g)", "cost": 75, "protein": 14, "calories": 120, "veg": True},
    {"food": "Tofu (100g)", "cost": 40, "protein": 12, "calories": 76, "veg": True},
    {"food": "Greek Yogurt (150g)", "cost": 35, "protein": 10, "calories": 130, "veg": True},
    {"food": "Muesli (50g)", "cost": 30, "protein": 5, "calories": 180, "veg": True},
    {"food": "Sprouts (100g)", "cost": 20, "protein": 8, "calories": 120, "veg": True},
    {"food": "Avocado (1/2)", "cost": 40, "protein": 2, "calories": 160, "veg": True},
    {"food": "Sweet Potato (100g)", "cost": 20, "protein": 2, "calories": 86, "veg": True},
    {"food": "Mixed Beans Salad (150g)", "cost": 45, "protein": 12, "calories": 210, "veg": True},
]


def get_top_foods(eligible_foods: list, limit: int = 5) -> list:
    """Use a min-heap to keep the most protein-efficient foods."""
    min_heap = []

    for item in eligible_foods:
        score = item["protein"] / item["calories"] if item["calories"] else 0
        entry = (score, item["food"], item)

        if len(min_heap) < limit:
            heapq.heappush(min_heap, entry)
        elif entry[0] > min_heap[0][0]:
            heapq.heapreplace(min_heap, entry)

    return [food for _, _, food in sorted(min_heap, key=lambda x: x[0], reverse=True)]


def get_meal_plan(budget: int, tcalories: int, diet_type: str):
    valid_diet_types = {"veg", "nonveg", "both"}
    if diet_type not in valid_diet_types:
        raise ValueError("diet_type must be one of: veg, nonveg, both")

    filtered = [
        item for item in foods
        if diet_type == "both"
        or (diet_type == "veg" and item["veg"])
        or (diet_type == "nonveg" and not item["veg"])
    ]

    # Try to meet calories and budget by adding nutrient-dense options first.
    filtered = sorted(filtered, key=lambda item: (item["protein"], item["calories"]), reverse=True)

    meal_plan = []
    total_cost = 0
    total_calories = 0
    total_protein = 0

    for item in filtered:
        if total_cost + item["cost"] <= budget and total_calories + item["calories"] <= tcalories:
            meal_plan.append(item)
            total_cost += item["cost"]
            total_calories += item["calories"]
            total_protein += item["protein"]

        if total_calories >= tcalories:
            break

    top_foods = get_top_foods(filtered, limit=5)
    return meal_plan, total_cost, total_protein, total_calories, top_foods


def format_currency(value: int) -> str:
    return f"₹{value:,}"


def main():
    st.set_page_config(page_title="Diet Planner", page_icon="🍒", layout="wide")
    st.title("Diet Planner")
    st.write("Build a simple meal plan based on your budget, calorie goals, and diet preference.")

    with st.sidebar:
        st.header("Planner settings")
        budget = st.number_input("Daily budget (₹)", min_value=0, value=200, step=5)
        calories_target = st.number_input("Calories target", min_value=100, value=1200, step=50)
        diet_type = st.selectbox("Diet type", ["veg", "nonveg", "both"], index=0)
        show_food_table = st.checkbox("Show available foods", value=True)

    meal_plan, total_cost, total_protein, total_calories, top_foods = get_meal_plan(budget, calories_target, diet_type)

    if len(meal_plan) == 0:
        st.warning("No meal plan could be created with the current budget and calorie target. Try increasing your budget or lowering the calorie target.")
    else:
        st.subheader("Suggested Meal Plan")
        plan_df = pd.DataFrame(meal_plan)
        plan_df = plan_df.assign(veg=plan_df["veg"].map({True: "Yes", False: "No"}))
        st.table(plan_df.rename(columns={"food": "Food", "cost": "Cost (₹)", "protein": "Protein (g)", "calories": "Calories", "veg": "Vegetarian"}))

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total Cost", format_currency(total_cost))
        col2.metric("Total Protein", f"{total_protein} g")
        col3.metric("Total Calories", f"{total_calories} kcal")
        col4.metric("Calories Goal", f"{calories_target} kcal")

        if total_cost > budget:
            st.error("The suggested plan exceeds your budget. Adjust your inputs to fit your budget.")
        elif total_calories < calories_target:
            st.info("The plan could not provide the full calorie target with the available foods and budget.")

    st.subheader("Top Protein-Efficient Foods")
    top_food_df = pd.DataFrame(
        [
            {
                "Food": item["food"],
                "Cost (₹)": item["cost"],
                "Protein (g)": item["protein"],
                "Calories": item["calories"],
                "Vegetarian": "Yes" if item["veg"] else "No",
            }
            for item in top_foods
        ]
    )
    st.dataframe(top_food_df.reset_index(drop=True))

    if show_food_table:
        st.subheader("Available Foods")
        available_df = pd.DataFrame(
            [item for item in foods if diet_type == "both" or (diet_type == "veg" and item["veg"]) or (diet_type == "nonveg" and not item["veg"])]
        )
        available_df = available_df.rename(columns={"food": "Food", "cost": "Cost (₹)", "protein": "Protein (g)", "calories": "Calories", "veg": "Vegetarian"})
        available_df["Vegetarian"] = available_df["Vegetarian"].map({True: "Yes", False: "No"})
        st.dataframe(available_df.reset_index(drop=True))


if __name__ == "__main__":
    main()