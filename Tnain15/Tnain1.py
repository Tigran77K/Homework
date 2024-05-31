#Create a Python class representing a Hospital account with methods to schedule visit and remove schedule
class HospitalAccount:
    names = []
    dates = []
    def __init__(self, name, date):
        if name not in self.names and date not in self.dates:
            self.name = name
            self.date = date
            self.names.append(self.name)
            self.dates.append(self.date)
        else:
            raise ValueError("Account already exists")
    def get_account(self):
        if self.name in self.names and self.date in self.dates:
            return self.name , self.date
        else:
            raise ValueError("Account not found")
    def remove_account(self, name, date):
        if name in self.names and date in self.dates:
            self.names.remove(name)
            self.dates.remove(date)
            print("Account removed")
        else:
            raise ValueError("Account not found")

ac1 = HospitalAccount("Jon", "2021")
ac2 = HospitalAccount("Tom", "2022")
ac3 = HospitalAccount("Bob", "2023")

ac3.remove_account("Bob", "2023")
ac1.remove_account("Jon", "2021")
ac2.remove_account("Tom", "2022")












