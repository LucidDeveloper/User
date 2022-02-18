
'''
@ author 
Gianni M. Javier
'''
# Create a file with the User class, including the __init__ and make_deposit methods
# Class/Bllueprint for Object/Instance of a Class
class User:
    def __init__(self, first_name,last_name,balance): # Special Method defined in Python, works as Class Constructor
        self.first_name = first_name # Attributes created with every Instantiation of an Object/Instance of a class
        self.last_name = last_name
        self.balance = balance
        
# Make_deposit(self, amount) - have this method increase the user's balance by the amount specified
    def make_deposit(self,amount):
        self.balance += amount 
        return self

# Add a make_withdrawal method to the User class      
# Make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
    def make_withdrawal(self,amount):
        self.balance -= amount
        return self

# Add a display_user_balance method to the User class
# Display_user_balance(self) - have this method print the user's name and account balance to the terminal
# eg. "User: Guido van Rossum, Balance: $150
    def display_user_balance(self):
        print(f'User: {self.first_name} {self.last_name}, Balance: ${self.balance}')
        return self

# BONUS: transfer_money(self, other_user, amount) - 
# have this method decrease the user's balance by the amount and 
# add that amount to other other_user's balance
    def transfer_money(self,other_user,amount):
        self.balance -= amount
        other_user.balance += amount
        return self

# Create 3 instances of the User class
gianni = User("Gianni","Javier",10000)    # instance of the class aka an object
eya = User("Andrea","Avila",10000)
bruno = User("Bruno", "Avila", 10000)

# Have the first user make 3 deposits and 1 withdrawal and then display their balance
gianni.make_deposit(500).make_deposit(1000).make_deposit(2500).make_withdrawal(1000).display_user_balance()

# Have the second user make 2 deposits and 2 withdrawals and then display their balance
eya.make_deposit(1000).make_deposit(1000).make_withdrawal(500).make_withdrawal(250).display_user_balance()

# Have the third user make 1 deposits and 3 withdrawals and then display their balance
bruno.make_deposit(1000).make_withdrawal(500).make_withdrawal(500).make_withdrawal(500).display_user_balance()

# BONUS: Add a transfer_money method; 
# have the first user transfer money to the third user 
# and then print both users' balances
gianni.transfer_money(bruno,1000)
gianni.display_user_balance()
bruno.display_user_balance()