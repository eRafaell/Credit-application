import sys
from Credits.client import Client
from Credits.blacklist import Blacklist
from Credits.loan import Loan
from Credits.models import Models
from Credits.income import Income
from Credits.expenses import Expenses


class Menu:
    '''Display a menu and respond to choice when run'''

    def __init__(self):
        self.client = Client()
        self.blacklist = Blacklist()
        self.loan = Loan()
        self.models = Models()
        self.income = Income()
        self.expenses = Expenses()
        self.choices = {
            "1": self.create_a_loan_application,
            "2": self.show_history,
            "3": self.search_customer,
            "4": self.check_customer,
            "5": self.quit
        }

    def display_menu(self):
        print("""
Credit Menu
1. Create a loan application
2. Show history
3. Search customer
4. Check customer
5. Quit
""")

    def run(self):
        """Display the menu and respond to choices"""
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print(f'{choice} is not a valid choice')

    def create_a_loan_application(self):
        li_client = self.client.add_client()
        print(li_client)
        li_income = self.income.add_income()
        print(li_income)
        li_expenses = self.expenses.add_expenses()
        print(li_expenses)
        li_loan = self.loan.add_loan(li_expenses, li_income)
        print(li_loan)
        print("\n")
        if len(li_client) == 8 and len(li_income) == 9 and len(li_expenses) == 4 and len(li_loan) == 8:
            self.models.create_sql_client(li_client)
            self.models.create_sql_income(li_income)
            self.models.create_sql_expenses(li_expenses)
            self.models.create_sql_loan(li_loan)
            if li_loan[7] == "Granted":
                print("There is permission to grant a loan")
                sys.exit(0)
            else:
                print("Unfortunately there is no permission to grant a loan")
                sys.exit(0)
        else:
            print("something went wrong")
            sys.exit(0)

    def show_history(self):
        select_all_history = self.loan.show_history()
        print("Loans history: ")
        print("\n".join(f"Client: {a} {b}, Id_Loan: {c}" for a, b, c in select_all_history))
        print("\n")
        print("to learn more about some loan, please give the loan id number from the listed")

        id_number = int(input("Give the loan id number: "))
        print("_______________________________________________________________________")
        print("\n")
        personal_data = self.loan.show_personal_data(id_number)

        if len(personal_data) > 0:
            print(f"Details for loan number: {id_number} - Personal data: ")
            print("\n".join(f" 1. Client full name: {a} {b}\n 2. City: {c}\n 3. Street: {d}\n 4. sex: {e}\n "
                            f"5. Marital Status: {f}\n 6. PESEL: {g}" for a, b, c, d, e, f, g in personal_data))
            loan_data = self.loan.show_loan_data(id_number)
            print(f"Information about Loan: ")
            print("\n".join(f" 7. Id Loan: {a}\n 8. Borrow Amount: {b} PLN\n 9. Installments Number: {c}\n "
                            f"10. Interest Rate: {d} %\n 11. Monthly Installment: {e} PLN\n "
                            f"12. Total Amount To Give Back: {f} PLN\n 13. Status: {g}"
                            for a, b, c, d, e, f, g in loan_data))
            income_data = self.loan.show_income(id_number)
            print(f"Information about client income and employment: ")
            print("\n".join(f" 14. Employer: {a}\n 15. Employment Street: {b}\n 16. NIP: {c}\n "
                            f"17. Employment Type: {d}\n 18. Net Salary: {e} PLN\n 19. Spouse Salary: {f} PLN"
                            for a, b, c, d, e, f in income_data))
            expenses_data = self.loan.show_expenses(id_number)
            print(f"Information about client expenses: ")
            print("\n".join(f" 20. All Monthly Credits: {a} PLN\n 21. All Monthly Bills: {b} PLN"
                            for a, b in expenses_data))
            print("_______________________________________________________________________")

        else:
            print("wrong id number")

        Menu().run()

    def search_customer(self):
        search_client = input("Please, give PESEL number: ")
        if self.models.check_pesel(search_client) == True:
            print("Pesel is correct")
            show_client = self.client.show_client(search_client)

            if len(show_client) > 0:
                print("\n")
                print("\n".join(f" 1. Client full name: {a} {b}\n 2. PESEL: {c}\n 3. City: {d}\n 4. Street: {e}\n "
                                f"5. Sex: {f}\n 6. Company: {g}\n 7. Company city: {h}\n 8. Company street: {i}\n "
                                f"9. NIP: {j}\n 10. Id Loan: {k}"
                                for a, b, c, d, e, f, g, h, i, j, k in show_client))
            else:
                print("There is no that client")

        else:
            print("pesel is incorrect")
            Menu().run()

    def check_customer(self):
        print('Check the customer if one has been blacklisted!!', '\n')
        pesel = input("To check the customer enter their pesel number: ")
        result = self.blacklist.check_customer(pesel)
        if len(result) > 0:
            print("\n")
            dictionary = {"First Name": result[0][0], "Last Name": result[0][1], "City": result[0][2],
                          "PESEL": result[0][3], "Reason of being on blacklist": result[0][4]}
            print("\n".join(f"{k} -> {v}" for k, v in dictionary.items()))
            print("\n")
            print("The customer has been blacklisted. Unfortunately, there is no approval to grant a loan")
            sys.exit(0)
        else:
            print("The customer has not been blacklisted. You can create a loan application")

    def quit(self):
        print('Thank you for visiting us today.')
        Menu().run()


if __name__ == "__main__":
    Menu().run()
