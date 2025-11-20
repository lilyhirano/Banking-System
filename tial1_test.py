
from banking_system import BankingSystem, Account


bank = BankingSystem()

print(bank.create_account(1, "urMama"))
print(bank.create_account(2, "urPapa"))
print(bank.create_account(1, "urMama"))

print(bank.deposit(5, "urMama",543289080932489894890))
print(bank.deposit(8, "urMamaf",5432890))

print(bank.transfer(87,"urMama", "urPapa", 1))





