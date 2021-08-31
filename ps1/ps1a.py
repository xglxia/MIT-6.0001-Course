# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 11:21:06 2021

@author: Guoli
"""

total_cost = float(input("Please enter a total cost for the house: "))
annual_salary = float(input("Please enter your annual salary: "))
portion_saved = float(input("Please enter portion saved of your salary(in a decimal form): "))

portion_down_payment = total_cost * 0.25
monthly_salary_saved = annual_salary * 1/12 * portion_saved
current_savings = 0


r = 0.04
n = 0

while current_savings < portion_down_payment:
      monthly_investment_savings = (current_savings + monthly_salary_saved) * r/12
      monthly_saved = monthly_investment_savings + monthly_salary_saved
      n = n+1
      current_savings = current_savings + monthly_saved
    

    
print(f'You need to save {n} months to pay for your dream house')