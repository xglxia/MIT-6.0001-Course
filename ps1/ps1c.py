# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 20:47:46 2021

@author: Guoli
"""

#total_cost = float(input("Please enter a total cost for the house: "))
annual_salary = float(input("Please enter your annual salary: "))
#portion_saved = float(input("Please enter portion saved of your salary(in a decimal form): "))
#semi_annual_salary_rise = float(input("Please enter your semi annual salary rise ina decial form: "))

total_cost = 1000000
portion_down_payment = total_cost * 0.25
#monthly_salary_saved = annual_salary * 1/12 * portion_saved
current_savings = 0


r = 0.04
n = 1
low = 0
high = 1
portion_saved = (low +high)/2.0
steps = 0



for n in range(36):
    monthly_salary_saved = annual_salary * 1/12 * portion_saved 
      
    monthly_investment_savings = (current_savings + monthly_salary_saved) * r/12
          
    monthly_saved = monthly_investment_savings + monthly_salary_saved
          
    current_savings = current_savings + monthly_saved     
    if (n+1) % 6 == 0:
        annual_salary = annual_salary + annual_salary * 0.07
        monthly_salary_saved = annual_salary * 1/12 * portion_saved
           
    if abs(current_savings - portion_down_payment) > 100:
         
        if current_savings < portion_down_payment:
             low = portion_saved
        else:
             high = portion_saved 
             
    portion_saved = (low +high)/2.0
    n = n + 1
    steps = steps + 1
         
    
          
          
             

#print("It is imposiible to do it")
    
    
print(portion_saved)
print(steps)