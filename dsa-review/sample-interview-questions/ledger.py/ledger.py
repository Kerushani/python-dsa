"""
“You’ve been asked to build a simplified investment allocation engine for Wealthsimple. The engine receives a list of client investment 
instructions from a file. Each instruction includes:
a client_id
the account_type (e.g., TFSA, RRSP, Non-Registered)
a list of investment_targets (each with a symbol and percentage allocation)
and an available_funds amount.

Your task is to:
Parse each client’s investment instruction.
Validate that the total allocation is 100%.
For valid instructions, calculate how many whole units of each stock to buy using the available funds and store the result.
If the allocation does not sum to 100%, ignore that instruction and log the client_id as an error.

Assume fixed prices per stock symbol (you can hardcode them).

Return:

A list of successful client allocations (client_id → stock → units purchased).
A list of client IDs with allocation errors.”
"""