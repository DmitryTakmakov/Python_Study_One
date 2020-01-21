business_income = int(input("Please enter your business' income:\n"))
business_spendings = int(input("Please enter your business' spendings:\n"))

if business_income > business_spendings:
    print('Congratulations! You run a successful business!')
    print(f'Your business earned approximately {business_income // business_spendings} times more than it costs to run it')
    employees = int(input("Okay now, how many people do you employ?\n"))
    print(f'That means that each employee earned you around {business_income // employees} moneys')
    print(f'Also, you can now pay them {(business_income - business_spendings) // employees} moneys')
elif business_income == business_spendings:
    print("You need to reconsider your life choices")
else:
    print("You've lost money! Go do something else!")
