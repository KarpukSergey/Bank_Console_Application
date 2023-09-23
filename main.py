import csv
import os


class Client:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def __str__(self):
        return f"|\tInfo Client\n|Name: {self._name}\n|Balance: {self._balance}$"


class Bank:
    new_obj_client = []

    def __init__(self):
        self.__list_client = []

    def add_client(self):
        name = input("Enter name: ")
        balance = input("Enter balance: ")
        new_client = Client(name, balance)
        self.__list_client.append(new_client)

    def find_client(self):
        try:
            name = input("Enter the name you want to find: ")
            if 0 > len(name) > 30:
                raise ValueError()
            for find in self.__list_client:
                if find._name == name:
                    print(find)
                else:
                    return None
        except ValueError as s:
            print("Error! The name entered is incorrect")

    def save_client(self, file_name: str):
        if not file_name.endswith('.csv'):
            file_name = file_name + '.csv'
        header = ['Name', 'Balance']
        with open(file_name, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader()
            for i in self.__list_client:
                info = {'Name': i._name, 'Balance': i._balance}
                writer.writerow(info)

    def init_data(self, file_name):
        client_from_file = []
        if not file_name.endswith('.csv'):
            file_name = file_name + '.csv'
        if file_name not in os.listdir():
            raise FileNotFoundError(f"This file does not exist")
        else:
            with open(file_name, 'r', newline='') as file:
                reader = csv.DictReader(file)
                for client in reader:
                    new_obj = []
                    for i in client.values():
                        new_obj.append(i)
                    self.new_obj_client.append(Client(*new_obj))
        for user in self.new_obj_client:
            print(user)

    def menu(self):
        while True:
            print(f"\tMenu Bank\n"
                  f"1. Add a client\n"
                  f"2. Find a client\n"
                  f"3. Save data to a file\n"
                  f"4. Download data from the file\n"
                  f"5. Exit")
            try:
                choice = int(input("Enter the selection: "))
                if choice == 1:
                    print(f"\tAdd a client")
                    self.add_client()
                elif choice == 2:
                    print(f"\tFind a client")
                    self.find_client()
                elif choice == 3:
                    print(f"\tSave data to a file")
                    file_name = str(input("Enter the file name: "))
                    self.save_client(file_name)
                elif choice == 4:
                    print(f"\tDownload data from the file")
                    file_name = str(input("Enter the file name: "))
                    self.init_data(file_name)
                elif choice == 5:
                    print("\tExit")
                    break
                else:
                    print("I don't know such a command, enter the choice from 1 to 5")
            except ValueError as s:
                print("Error! Incorrect selection")


if __name__ == '__main__':
    b1 = Bank()
    b1.menu()