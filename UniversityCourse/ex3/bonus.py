"""
program: bonus.py
date: 2024-11-14
"""

def calculate_bonus(profit):
    if profit <= 100000:
        return profit * 0.1
    elif profit <= 200000:
        return 100000 * 0.1 + (profit - 100000) * 0.075
    elif profit <= 400000:
        return 100000 * 0.1 + 100000 * 0.075 + (profit - 200000) * 0.05
    elif profit <= 600000:
        return 100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + (profit - 400000) * 0.03
    elif profit <= 1000000:
        return 100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + 200000 * 0.03 + (profit - 600000) * 0.015
    else:
        return 100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + 200000 * 0.03 + 400000 * 0.015 + (profit - 1000000) * 0.01

profit = float(input("Enter the profit: "))
bonus = calculate_bonus(profit)
print(f"Bonus: {bonus}")
