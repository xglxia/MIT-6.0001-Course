# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 20:47:46 2021

@author: Guoli

Collaborator: Joshua William Fleming
"""
#Assignment 1
#Part C
#Task: Determine the required savings rate to afford downpayment in 3 years.
annual_salary = float(input('Please enter your annual salary:'))
while annual_salary < 0 :
    print('Your annual salary should be a positive number.')
    annual_salary = float(input('Please enter your annual salary.'))
total_cost =1000000
sa_raise = 0.07
portion_down_payment = 0.25 
current_savings = 0 #Initialise savings to 0
num_months = 36
annual_return = 0.04 
def downpayment(p,a,n):
    '''
    Calculates the downpayment saved in n months with annual salary a for given a saving rate p as an integer 0 to 10000
    corresponding to a decimal percentage of p/10000.
    Inputs: The integer p, annual salary a, number of months n
    Outputs: The downpayment saved in 36 months.
    '''
    portion_saved = p/10000
    current_savings = 0
    for i in range(1,n+1):
        current_savings = current_savings*(1+(annual_return/12)) + (a/12)*(portion_saved)
        if i%6 == 0 :
            a = a*(1+sa_raise) 
    return current_savings    
if downpayment(10000, annual_salary, 36) < total_cost*portion_down_payment :
    print('Given your current finanical circumstances, it is impossible to reach your goal.')
else:
    tol = 100 #tolerance
    step_counter = 0 #number of iterations required to reach the tolerance
    low = 0
    high = 10000
    guess = (high+low)/2
    while abs(downpayment(guess, annual_salary, 36) - total_cost*portion_down_payment) >= tol:
        if downpayment(guess, annual_salary, 36) < total_cost*portion_down_payment :
            low = guess
        else:
            high = guess
        guess = (high + low)/2.0
        step_counter += 1
    print('To reach your goal of saving',total_cost*portion_down_payment,'you need to save',guess/100,'%','of your monthly salary.')
    print('The number of iterations required was', step_counter)



