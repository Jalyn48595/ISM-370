# -*- coding: utf-8 -*-
"""370_Mod1_Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hJoRklqow055EHaisHtUKlHgrek9Rwey

Jalyn Buthman
Module 1 Project
"""

#marketing channel variables
social_media = 5000
email_marketing =  3000
advertising = 2000

while True:
#user input variable for target audience
  user_target_audience = input("Please enter your target audience (Gen Z, Millennials, Gen X): ")

#if statement to select a target audience
  if user_target_audience == 'Gen Z':
    print (f'You have selected Gen Z as your target audience.\n')
  elif user_target_audience == 'Millennials':
    print (f'You have selected Millennials as your target audience.\n')
  elif user_target_audience == 'Gen X':
    print (f'You have selected Gen X as your target audience.\n')
#error handling
  else:
    print (f'The input {user_target_audience} was not recognized. Please try again.\n')

#user input variable for campaign goal
  user_campaign_goal = input("Please enter your campaign goal (Brand Awareness, Lead Generation, Sales): ")

#if statement to select a campaign goal
  if user_campaign_goal == 'Brand Awareness':
    brand_social_media = social_media * 1.2
    brand_advertising = advertising * 1.15
    brand_allocated_budget = brand_social_media + brand_advertising
    brand_initial_total_budget = social_media + advertising
    brand_remaining_budget = brand_allocated_budget - brand_initial_total_budget
    print (f'\nBrand Awareness Budget Overview:\nAllocated Budget: ${brand_allocated_budget:,.2f}\nRemaining Overall Budget: ${brand_remaining_budget:,.2f}\n')
  elif user_campaign_goal == 'Lead Generation':
    lead_email_marketing = email_marketing * 1.3
    lead_allocated_budget = lead_email_marketing
    lead_initial_total_budget = email_marketing
    lead_remaining_budget = lead_allocated_budget - lead_initial_total_budget
    print (f'\nLead Generation Budget Overview:\nAllocated Budget: ${lead_allocated_budget:,.2f}\nRemaining Overall Budget: ${lead_remaining_budget:,.2f}\n')

  elif user_campaign_goal == 'Sales':
    sales_social_media = social_media * 1.1
    sales_advertising = advertising * 1.1
    sales_email_marketing = email_marketing * 1.1
    sales_allocated_budget = sales_social_media + sales_advertising + sales_email_marketing
    sales_initial_total_budget = social_media + email_marketing + advertising
    sales_remaining_budget = sales_allocated_budget - sales_initial_total_budget
    print (f'\nSales Budget Overview:\nAllocated Budget: ${sales_allocated_budget:,.2f}\nRemaining Overall Budget: ${sales_remaining_budget:,.2f}\n')
#error handling
  else:
    print(f'\nThe input "{user_campaign_goal}" was not recognized. Please try again.\n')

#initial total budget = the sum of the original budgets
#allocated budget = the sum of the budgets with increased amounts
#remaining budget = allocated sum - initial total budget