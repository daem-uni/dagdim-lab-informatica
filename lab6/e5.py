def calculate_balance(initial_balance, interest, years):
    for i in range(years):
        initial_balance = initial_balance * (interest + 1)

    return initial_balance
