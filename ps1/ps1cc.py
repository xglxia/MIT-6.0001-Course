# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 10:55:52 2021

@author: Guoli
"""

def f(current):
    #monthly_salary_saved = 0
    #annual_salary = float(input("Please enter your annual salary: "))
    annual_salary1 = annual_salary
    for i in range(1,37):
        
        if i % 6 == 0:
            annual_salary1 = annual_salary1 * (1+ 0.07)
            
        #else:
            #annual_salary1 = annual_salary
            #monthly_salary_saved = annual_salary1 * 1/12 * portion_saved
        monthly_salary_saved = annual_salary1 * 1/12 * portion_saved
        monthly_investment_savings = (current + monthly_salary_saved) * r/12    
        monthly_saved = monthly_investment_savings + monthly_salary_saved   
        current = current + monthly_saved   
        i = i + 1
    return current
    

    
total_cost = 1000000
portion_down_payment = total_cost * 0.25
r = 0.04
n = 36
low = 0
high = 1
portion_saved = (low +high)/2.0
steps = 0
current = 0
annual_salary = float(input("Please enter your annual salary: "))
#monthly_salary = annual_salary *1/12
#monthly_salary_saved = 0
#current_savings = f(current)

if annual_salary < 70000:
    print("It is impossible to do it")
else:

    while abs(f(current) - portion_down_payment) > 100:
        #current_savings = f(current)    
        if f(current) < portion_down_payment:
            low = portion_saved
        else:
            high = portion_saved 
        portion_saved = (low +high)/2.0
        steps = steps + 1
        print(f(current))
    
    print(f'The best portion_saved is {portion_saved}')
    print(steps)
    
    
    
    
    
    
    
    
    
    
    
    
    
    