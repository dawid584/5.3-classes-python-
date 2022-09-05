import email
from posixpath import supports_unicode_filenames
from typing_extensions import Self
from unicodedata import name

data = ""

data_1 =""

class  BaseContact:
    
    def __init__(self , name , surname , telephone_number , email ):
        self.name = name
        self.surname = surname
        self.telephone_number = telephone_number
        self.email = email
    def __str__(self) -> str:
        return f' Wizytówka prywatna Imie Nazwisko: {self.name} {self.surname}   number telefonu {self.telephone_number} , email {self.email} , długść imienia i nazwiska {len(self.name)+ len(self.surname)}'
        
  
    def contact(self):
            
            print("Wybieram numer {self.telephone_number}  i dzwonię do {self.name} {self.surname}")                       
    contact()


    


class BusinessContact(BaseContact):
    def __init__(self  , company_position , company_name , company_number , *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.company_position = company_position
       self.company_name = company_name
       self.company_number = company_number
       
      
    def contact_2(self):
        print(f"Wybieram numer firmowy {self.company_number}  i dzwonię do {self.name} {self.surname}")  
    contact_2()

    def __str__(self) -> str:
        return f' Wizytówka słuzbowa Imie Nazwisko: {self.name} {self.surname}  stanowisko {self.company_position} nazwa firmy {self.company_name} number telefonu {self.company_number} długść imienia i nazwiska {len(self.name)+ len(self.surname)}'

data = BusinessContact( "Jan" , "Kowalski" , "Logistyk" , "Mac-Trans" , +48456128796  )
data_1 = BaseContact("Jan" , "Kowalski" , +66123456779 , "email@gmail.com" )
print(data_1)
print(data)




        