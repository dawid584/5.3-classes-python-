import email
from os import name
from faker import Faker
fake = Faker(['th_TH', 'pl_PL'])
class BaseContact:

   def __init__(self , name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

   def label_length(self):
        print("długość imienia:  " + str(len(self.name)))

   def contact(self):
       print(f'Wybieram numer +48 {self.phone} i dzwonię do {self.name}') 
       print(f'Wizytówka prywatna {self.name} , +48{self.phone} , {self.email}')

class BusinessContact(BaseContact):
    def __init__(self,name, phone, email,company_position, company_name, company_number):
        super().__init__(name , phone , email)
        self.company_position = company_position
        self.company_name = company_name
        self.company_number = company_number

    def contact(self):
        print(f'Wybieram numer służbowy +48 {self.phone} i dzwonię do {self.company_number}')  
        print(f'Wizytówka służbowa {self.company_position} , +48{self.company_number} , {self.company_name}')




def create_contacts(n, contact_type ):
    
    lista_of_contacts = []
    for i in range(n):
         if contact_type == "priv":
               card = BaseContact( name = fake.name() , phone= fake.msisdn()[3:] , email= fake.email()) # tu trzeba skorzystać z fakera
               lista_of_contacts.append(card)
         elif contact_type == "biz":
               cars = BusinessContact(company_position = fake.job() ,company_name = fake.company() , company_number = fake.msisdn()[3:] , name = fake.name() , phone= fake.msisdn()[3:] , email= fake.email() ) # tu dane generowane z fakera 
    return lista_of_contacts  

c = BaseContact( name = fake.name() , phone= fake.msisdn()[3:]  , email= fake.email() )
c.contact()
c.label_length()

card = BusinessContact(company_position =fake.job(), company_name= fake.company() ,  company_number= fake.msisdn()[3:] , name = fake.name() , phone= fake.msisdn()[3:] , email= fake.email())
card.contact()



create_contacts(n=10, contact_type="biz")    




       

