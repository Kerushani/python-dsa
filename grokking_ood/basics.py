"""
Basic concepts of obejct oriented programming:
objects: objects represent a real-world entitiy and the basic building
block of oop. For example, an online shopping system will have objects such as a shopping cart, customer, product item, etc.

Class: class is the protottype or bluepint of an object. it is a template deifintion of the attribute sand the methods 
of an object. For example, in the online shopping system, the customer object will have attributes like shipping address, credit card, etc. and 
methods for placing an order, cancelling an order, etc.

"""

# simple code snippet
class ShoppingCart(object):
    def __init__(self):
        self.total = 0
        self.items = {}
    
    def add_item(self, item_name, quantity, price):
        self.total += (quantity*price)
        self.items.update({item_name: quantity})
    
    def remove_item(self, item_name, quantity, price):
        self.total -= (quantity*price)
        if quantity > self.items[item_name]:
            del self.items[item_name]
        self.items[item_name] -= quantity
    
    def checkout(self, cash_paid):
        balance = 0
        if cash_paid < self.total:
            return "You paid {} but card amount is {}".format(cash_paid, self.total)
        balance = cash_paid - self.total
        return "Exchange amount: {}".format(balance)

# driver code
cart = ShoppingCart()

cart.add_item("A", 10, 50)
cart.add_item("B", 5, 20)

cart.remove_item("B", 1, 20)

cart_res = cart.checkout(600)

print("Total cart amount:", cart.total)
print("Cart items:", cart.items)

print(cart_res)

"""
four principles of ood: encapsulation, abstraction, inheritance, and polymorphism
important design principles: Dont repeat yourself, you aren't gonna need it, keep it simple stupid, SOLID(single responsiblity principle, open closed princple, liskov substitution princple, interface segregation principle)

polymorphism: ability of an OBJECT to take different forms and thus 
depending upon the context, to respond to the same message in diffeent ways. Take the example of a chess game;
a chess piece can take many forms, like bishop, castle, or knoight, and all of these pieces will respond differently to the "move" message
"""

# example of polymorphism:

class Bishops:
    def move(self):
        print("Bishops can move diagonally")
class Knights:
    def move(self):
        print("Knights can move two squares vertically and one square horizontally, or two squares horizontally and one square vertically")

# common interface
def move_test(chess_peice):
    chess_peice.move()

# initalize objects
bishop = Bishops()
knight = Knights()

# passing the object
move_test(bishop)
move_test(knight)

"""
the point here is that we're passing the objects to the common interface
"""


"""
!OBJECT ORIENTED ANALYSIS AND DESIGN!
this is a structured method of analyzing and designing a system by applying object oriented concepts. This
design process consists of an investigation into the objects constitiuting the system. It starts by first identifying the objects
of the system and then figuring out the interactions between vrious objects

The process of object oriented analysis and design can be described as
1. Identifying the objects in the system
2. defining the relationships between objects
3. establishing the interface of each object (functions in between the peices of code that you can pass an object to for a common result)
4. making a design, which can be converted to executables using object oritented languages

UML Diagrams of focus: Use case diagram (high level functional behaviour of the system), class diagram, activity diagram, sequenct diagram (interaction among classes in terms of an exchange of messages over time)
"""