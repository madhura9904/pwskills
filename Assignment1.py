#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1
#cLass is a basic structure or template for a single type of variable or methods
#We assign a class to a object which is one specific type of object
class student_det:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
details=student_det('John',15,8)
details.name
details.age
details.grade


# In[5]:


#2
#4 pillars of oops:abstraction, encapsulation, inheritance, and polymorphism


# In[6]:


#3
#init function is an Object or a method to pass data obtained from user to class 
class marks:
    def __init__(self,marks):
        self.marks=marks
m=marks(40)
m.marks


# In[7]:


#Self is used to refer to the attributes and methods of a given class 


# In[19]:


#Inheritance:
#It is one of the pillars of oops where the attributes of the parent class is inherited by the child class when the parent class is called.
#c1 called in c2,c2 called by c3
#Multilabel Inheritance:c3 contains all 2 classes
class c1:
    def tc1(self):
        print('Hi')
        
class c2(c1):
    def tc2(self):
        print('Hello')

class c3(c2):
    def tc3(self):
        print('Welcome')
obj=c3
c3.tc1
##c1+c2=c3
#Multiple inheritance:Access both classes in c3
class c1:
    def tc1(self):
        print('Hi')
        
class c2:
    def tc2(self):
        print('Hi2')

class c3(c1,c2):
    pass


# In[ ]:




