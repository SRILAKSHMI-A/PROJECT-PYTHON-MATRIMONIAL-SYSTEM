#!/usr/bin/env python
# coding: utf-8

# In[7]:


import csv
class Matrimony:
    my_file="database.csv"
    def Menu(self):
        print("__________________WELCOME TO OUR MATRIMONIAL SITE______________________")
        print("Menu")
        print("0.Exit Menu")
        print("1.Insertion")
        print("2.Modification")
        print("3.Retrieval")
        print("4.Searching")
        print("5.Recommendation")
        print("6.Deletion")
        print("Enter your choice")
        self.choice=int(input())
        if not type(self.choice) is int:
            raise Exception("Please enter only integers")
        return self.choice
    def Insertion(self):
        print("Enter the details as mentioned below")
        Name=input("Enter your Name:")
        Age=input("Enter your age:")
        Occupation=input("Enter your Occupation:")
        hobbies=input("Enter your hobbies")
        likes=input("Enter your likes")
        dislikes=input("Enter your dislikes")
        Mother_tongue=input("Enter your Mother_tongue")
        salary=input("Enter your salary")
        with open(b.my_file,'a',newline="") as f:
            insert=csv.writer(f)
            insert.writerow([Name,Age,Occupation,hobbies,likes,dislikes,Mother_tongue,salary])
        print("All the details are saved successfully")
    def Retrieval(self):
        with open(b.my_file,'r') as f:
            data=csv.reader(f)
            print("Data stored")
            for i in list(data):
                print(*i)
    def Modification(self):
        with open(b.my_file,'r') as f:
            data=csv.reader(f)
            print(list(data))
            M=input("Enter what you want to modify:")
            new=input()
            my_list=[new if M in i else i for i in list(data)]
        with open(b.my_file,'w',newline="") as g:
            modify=csv.writer(g)
            modify.writerows(my_list)
        with open(b.my_file,'r') as n:
            new_read=csv.reader(n)
            for i in list(new_read):
                print(*i)
            print("your request has been modified")
    def Searching(self):
        with open(b.my_file,'r') as f:
            data=csv.reader(f)
            Search=input("Enter what you want to Search:")
            print([i for i in list(data) if Search in i])
            
    def Deletion(self):
        with open(b.my_file,'r') as f:
            data=csv.reader(f)
            Delete=input("Enter what you want to delete:")
            My_List=[i for i in list(data) if Delete not in i]
        with open(b.my_file,'w',newline="") as v:
            dell=csv.writer(v)
            dell.writerows(My_List)
        with open(b.my_file,'r') as g:
            delll=csv.reader(g)
            for i in list(delll):
                print(i)
        
    def Recommendation(self):
        print("We would like to recommend few profiles based on your profile details")
        with open(b.my_file,'r') as f:
            data=csv.reader(f)
            for i in list(0,10):
                if data[i]==data[i+1]:
                    print(data[i])

            
        
            
        


while(1==1):
    b=Matrimony()
    choice=b.Menu()
    
    if choice==0:
        print("End")
        break
    elif choice==1:
        b.Insertion()
    elif choice==2:
        b.Modification()
    elif choice==3:
        b.Retrieval()
    elif choice==4:
        b.Searching()
    elif choice==5:
        b.Recommendation()
    else:
        b.Deletion()
        
    


# In[ ]:





# # 
