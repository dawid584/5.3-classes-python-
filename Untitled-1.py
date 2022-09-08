from posixpath import supports_unicode_filenames
from typing_extensions import Self
from unicodedata import name
from faker import Faker
fake = Faker(['th_TH', 'pl_PL'])

from faker import Faker

class BaseContact:
    def __init__(self , name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    #property
    def label_length(self):
       print("długość imienia:  " + len(self.name))
    self.label_length()     
  

    def contact(self): 
       print(f'Wybieram numer +48 {self.phone} i dzwonię do {self.name}') 
       print(f'Wizytówka prywatna {self.name} , +48{self.phone} , {self.email}')
    
    self.contact()

class BusinessContact(BaseContact):
    def __init__(self, name, phone, email, company_position, company_name, company_number):
       super().__init__(name, phone, email)
       self.company_position = company_position
       self.company_name = company_name
       self.company_number = company_number
       
    def contact(self): 
       print(f'Wybieram numer służbowy +48 {self.phone} i dzwonię do {self.company_number}')  
       print(f'Wizytówka służbowa {self.company_position} , +48{self.company_number} , {self.company_name}')
    self.contact()
    
def fake_contacts(is_business, amount):
    fake = Faker(['th_TH', 'pl_PL'])
    company_position = fake.job()
    company_name = fake.company()
    email = fake.email()
    name = fake.name()
    company_number = fake.msisdn()[3:]
    telephone_number = fake.msisdn()[3:]

    lista_of_contacts = []
    
    for i in range(amount):
        if is_business:
          card = BusinessContact(name, telephone_number, email, company_number, company_position, company_name)
        else:
          card = BaseContact(name, telephone_number, email)
        lista_of_contacts.append(card)

    return lista_of_contacts



n = int(input('wpisz '))

fake_contacts(True, n) # biznesowe kontakty
fake_contacts(False, n) # normalne kontakty