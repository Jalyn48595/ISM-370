# -*- coding: utf-8 -*-
"""370_Mod_2_In-class.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TFOpHsIHpVberN05WD98Kw9Z4UYzkEGt

Title: Employee Salary Increase Description: Calculate employee increases and new information. Created by Jalyn Buthman
"""

#create employee dictionary
employee_data = {
    "e01": {"name": "Ryan", "salary": 90000},
    "e02": {"name": "Daniel", "salary": 85000},
    "e03": {"name": "Kayla", "salary": 95000}
}

#practice working with dictionary of dictionaries
#print (f"The employee's salary is ${employee_data['e03']['salary']:,.2f}")

#initialize variables
salary_increase = 0.05

#use a for loop to increase the salary for each employee
for key, value in employee_data.items():
  value['salary'] *= (salary_increase +1 )
  print (f"Employee ID: {key}")
  print(f"Name: {value['name']}")
  print(f"New salary: ${value['salary']:,.2f}")
  print()