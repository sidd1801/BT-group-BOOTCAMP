# solution.py

def calculate_overall_sales():
    # Land distribution
    acres_per_crop = 16  # 80 acres / 5 crops

    # ---- TOMATOES ----
    tomato_30 = 0.30 * acres_per_crop * 10          # 30% at 10 t/acre
    tomato_70 = 0.70 * acres_per_crop * 12          # 70% at 12 t/acre
    tomato_total_tonnes = tomato_30 + tomato_70
    tomato_revenue = tomato_total_tonnes * 1000 * 7  # price per kg

    # ---- POTATOES ----
    potato_tonnes = acres_per_crop * 10
    potato_revenue = potato_tonnes * 1000 * 20

    # ---- CABBAGE ----
    cabbage_tonnes = acres_per_crop * 14
    cabbage_revenue = cabbage_tonnes * 1000 * 24

    # ---- SUNFLOWER ----
    sunflower_tonnes = acres_per_crop * 0.7
    sunflower_revenue = sunflower_tonnes * 1000 * 200

    # ---- SUGARCANE ----
    sugarcane_tonnes = acres_per_crop * 45
    sugarcane_revenue = sugarcane_tonnes * 4000  # price per tonne

    total_sales = (
        tomato_revenue
        + potato_revenue
        + cabbage_revenue
        + sunflower_revenue
        + sugarcane_revenue
    )

    return total_sales


def calculate_chemical_free_sales_upto_11_months():
    # Only tomatoes, potatoes, cabbage, sunflower are chemical-free at 11 months
    acres_per_crop = 16

    # ---- TOMATOES ----
    tomato_30 = 0.30 * acres_per_crop * 10
    tomato_70 = 0.70 * acres_per_crop * 12
    tomato_revenue = (tomato_30 + tomato_70) * 1000 * 7

    # ---- POTATOES ----
    potato_revenue = acres_per_crop * 10 * 1000 * 20

    # ---- CABBAGE ----
    cabbage_revenue = acres_per_crop * 14 * 1000 * 24

    # ---- SUNFLOWER ----
    sunflower_revenue = acres_per_crop * 0.7 * 1000 * 200

    chemical_free_total = (
        tomato_revenue + potato_revenue + cabbage_revenue + sunflower_revenue
    )

    return chemical_free_total


if __name__ == "__main__":
    print("Overall Sales:", calculate_overall_sales())
    print("Chemical-Free Sales (11 months):", calculate_chemical_free_sales_upto_11_months())
