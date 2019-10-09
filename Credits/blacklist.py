

from Credits.models import Models


class Blacklist:
    def __init__(self):
        self.blacklist = Models()


    def check_customer(self, pesel: str):
        query = f"select c.FirstName, c.LastName, c.City, c.PESEL, b.reason from blacklist b left join client c on b.ClientId = c.IdClient where pesel = {pesel}"
        return self.blacklist.read_sql(query)








