#!/usr/bin/env python
# coding: utf-8

# In[39]:


import json
class Swiggy:
    def __init__(self,who_are_you,email,password):
        self.email=email
        self.password=password
        self.who_are_you=who_are_you
        self.login()
    def login(self):
        if who_are_you==1:
            print("Welcome Seller")
            print(" "*45)
            if(password=="myEcommerceWeb"):
                Sdata={email:password}
                with open("Seller_details.json",'a') as file:
                    seller_file=json.dumps(Sdata)
                    file.write(seller_file)
                print("Great!__________Credentials Accepted!!_________________")
                self.Menu()
            else:
                print("Invalid credentials!please enter correct email and password ")
       
        else:
            print("Welcome Buyer")
            print(" "*45)
            if(password=="Ecommercebuy"):
                Bdata={email:password}
                with open("Buyer_details.json",'a') as file:
                    Buyer_file=json.dumps(Bdata)
                    file.write(Buyer_file)
                print("Great!__________Credentials Accepted!!_________________")
                self.Menu()
            else:
                print("Invalid credentials!please enter correct email and password ")
        
    def Menu(self):
        if(who_are_you==1):
            print(" "*45)
            print("Your Menu")
            print("0.Exit Menu")
            print("1.Upload details")
            print("2.Show details of inventory")
            print("Please enter your choice")
            choice=int(input())
            if(choice==1):
                self.Upload_detail()
            else:
                self.Show_details()
        else:
            print(" "*45)
            print("Your Menu")
            print("0.Exit Menu")
            print("i.Search Product")
            print("ii.Fiter Product")
            print("iii.Order product")
            Choice=input("Enter your choice: ")
            if(Choice=="i"):
                self.SearchProduct()
            elif(Choice=="ii"):
                self.FilterProduct()
            else:
                self.OrderProduct()
    def Upload_detail(self):
        self.dictt=[]
        d={"Name_of_Comics":input("Enter the name of comics: "),"Price":input("Price of the comics: "),"author":input("Enter the name of Author"),"description":input("Please enter a short description: ")
        ,"story line":input("Please enter story line briefly: "),"language":input("Please enter the language of your comic:"),
        "category":input("Enter the category: ")}
        with open('details.json') as f:
            data = json.load(f)
        data.append(d)
        with open('details.json', 'w') as f:
            json.dump(data, f)
    def Show_details(self):
        with open('details.json','r')as g:
            show=json.load(g)
            print(show)
    def SearchProduct(self):
        word=input("Enter your word to search:")
        with open('details.json','r') as f:
            search=json.load(f)
            for i in list(search):
                for j in i:
                    if(i[j]==word):
                        print(i)
                        break
    def FilterProduct(self):
        print("1.filter by name of comics")
        print("2.filter by price")
        print("3.Filter by category")
        print("4.filter by language")
        filterr=int(input("Enter by which you want to filter"))
        with open('details.json','r') as f:
            filee=json.load(f)
        if(filterr==1):
            name=input("Please enter the name of comic: ")
            for i in list(filee):
                if (i["Name_of_Comics"]==name):
                    print(i)
        elif(filterr==2):
            price=input("Enter the amount that you wish to filter the books")
            for i in list(filee):
                if (i["Price"]==price):
                    print(i)
        elif(filterr==3):
            category=input("Enter the category to filter")
            for i in list(filee):
                if (i["category"]==category):
                    print(i)
        else:
            language=input("Enter the language to filter")
            for i in list(filee):
                if (i["language"]==language):
                    print(i)
    def OrderProduct(self):
        order=input("Please enter your choice of comic book")
        with open('details.json','r') as f:
            my_file=json.load(f)
            for i in list(my_file):
                for j in i:
                    if i[j]==order:
                        print("Order Taken!!Thanks for Shopping\n Looking forward for more orders")
                        break
                else:
                    break
            
            print("Oops,Out of stock,We will notify you once the inventory is refilled!!")
            
        
            
            
        
    
                
            
    
        
            


who_are_you=int(input("Hey!! Welcome to Swiggy\n Please press 1 if you are a seller!!\n Press 2 if you want to buy any product!!"))
print("-"*45)
print("Enter your email and password credentials")
print(" "*45)
email=input("Enter Email_id:")
print(" "*45)
password=input("Enter Password:")
print("-"*45)
B=Swiggy(email,password,who_are_you)
            
            
            
            

        
        
    
    


# In[ ]:





# In[ ]:




