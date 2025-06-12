"""
Design a digital library system that tracks which users borrow which books, when, and for how long. 
Each user has a unique ID and can borrow up to a certain number of books at a time (e.g., max 3). 
Each book has a title, author, unique book ID, and a limited number of physical copies.

You’ll receive a sequence of actions in a data file. Your task is to:

Track book availability

Ensure borrowing rules are enforced (e.g., no more than 3 active books per user, or borrowing books that are 
out of stock)

Log borrowing and returning

Optionally, calculate overdue books (assume each borrow has a max duration of 14 days)
"""