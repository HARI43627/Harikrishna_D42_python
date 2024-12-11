# Exercise 10
pounds = float(input("Please enter amount in pounds: "))
conversion_rate = 1.37  # Example conversion rate, update if needed
dollars = pounds * conversion_rate
print(f"\u00a3{pounds} are ${dollars:.2f}")