from typing import List

from Credits.models import Models
from Credits.blacklist import Blacklist

import sys


class Client:
    def __init__(self):
        self.client = Models()
        self.checking = Blacklist()

    def show_client(self, pesel: str):
        query = f"""select c.FirstName, c.LastName, c.PESEL, c.City, c.Street, c.Sex, i.Employer, i.EmploymentCity, 
      i.EmploymentStreet, i.NIP, l.IdLoan from client c 
      left join income i on c.IdClient = i.ClientId 
      join loan l on c.IdClient = l.ClientId 
      where c.PESEL = {pesel};
      """
        return self.client.read_sql(query)

    def get_id_client(self):
        query = "select max(IdClient) from Client"
        idclient = self.client.read_sql(query)
        if len(idclient) > 0:
            idclient = str(idclient).strip('[(,)]')
            idclient = int(idclient.replace(",", "")) + 1
            return idclient
        else:
            return 1

    def add_client(self):
        client_list = []
        id = self.get_id_client()
        client_list.append(id)
        pesel = input("Please, enter a PESEL number: ")
        result = self.checking.check_customer(pesel)
        if len(result) > 0:
            print("The customer has been blacklisted. Unfortunately, there is no approval to grant a loan")
            sys.exit(0)
        else:

            if self.client.check_pesel(pesel) == False:
                print("Pesel number is incorrect")
                answer = input(
                    "Please click 'q' if you want to end application or any other button to enter PESEL again: ")
                if answer.lower() == "q":
                    sys.exit(0)
                else:
                    return self.add_client()
            else:
                print("Pesel number is correct")

        first_name = input("Please, enter a first name: ")
        if len(first_name) <= 50:
            client_list.append(first_name.capitalize())
        else:
            print("First name is too long. We cannot continue")
            sys.exit(0)
        last_name = input("Please, enter a last name: ")
        if len(last_name) <= 50:
            client_list.append(last_name.capitalize())
        else:
            print("Last name is too long. We cannot continue")
            sys.exit(0)
        city = input("Please, enter a city: ")
        if len(city) <= 20:
            client_list.append(city.capitalize())
        else:
            print("City name is too long. We cannot continue")
            sys.exit(0)
        street = input("Please, enter a street: ")
        if len(street) <= 30:
            client_list.append(street.capitalize())
        else:
            print("Street name is too long. We cannot continue")
            sys.exit(0)
        sex = input("Please, enter your gender [W] for woman or [M] for man: ")
        if len(sex) == 1:
            if sex.upper() == "W" or sex.upper() == "M":
                client_list.append(sex.capitalize())
            else:
                print("wrong abbreviation")
                sys.exit(0)
        else:
            print("Gender abbreviation is too long. We cannot continue")
            sys.exit(0)
        marital_status = input("Please, enter a marital status: ")
        if len(marital_status) <= 30:
            client_list.append(marital_status.capitalize())
        else:
            print("Martial status name is too long. We cannot continue")
            sys.exit(0)
        client_list.append(pesel)
        return client_list


