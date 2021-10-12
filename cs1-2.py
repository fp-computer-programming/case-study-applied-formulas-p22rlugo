# Ryan Lugo: RJL 10/12/21

principle_investment = int(input("What's the principle investment?: "))
rate_prompt = float(input("What's the interest rate?: "))
number_of_times = int(input("What's the number of times that interest is compounded per unit?: "))
time = float(input("What's the amount of time the money is invested in?: "))

rate = rate_prompt / 100
compound_formula = principle_investment ((1 + (rate / number_of_times))**(number_of_times * time)) 

print("This is the value of the account at this date: ")