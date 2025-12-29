items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}

def greedy_algorithm(items, budget):
    ratios = {item: info["calories"] / info["cost"] for item, info in items.items()}
    sorted_items = sorted(ratios.items(), key=lambda x: x[1], reverse=True)

    total_cost = 0
    total_calories = 0
    selected_items = []

    for item, _ in sorted_items:
        if total_cost + items[item]["cost"] <= budget:
            selected_items.append(item)
            total_cost += items[item]["cost"]
            total_calories += items[item]["calories"]

    return selected_items, total_calories


budget = 100
selected_items, total_calories = greedy_algorithm(items, budget)
print("Greedy Algorithm")
print("Selected Items:", selected_items)
print("Total Calories:", total_calories)


def dynamic_programming(items, budget):
    dp = [0] * (budget + 1)
    selected_items = [[] for _ in range(budget + 1)]

    for item, info in items.items():
        cost = info["cost"]
        calories = info["calories"]
        for current_budget in range(budget, cost - 1, -1):
            if dp[current_budget - cost] + calories > dp[current_budget]:
                dp[current_budget] = dp[current_budget - cost] + calories
                selected_items[current_budget] = selected_items[
                    current_budget - cost
                ] + [item]

    optimal_items = selected_items[budget]
    total_calories = dp[budget]

    return optimal_items, total_calories

selected_items, total_calories = dynamic_programming(items, budget)
print("Dynamic Programming")
print("Selected Items:", selected_items)
print("Total Calories:", total_calories)