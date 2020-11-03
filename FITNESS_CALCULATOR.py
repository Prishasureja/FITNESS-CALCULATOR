#!/usr/bin/env python
# coding: utf-8

# In[94]:


from tkinter import*

class fitness:
    
    def __init__(self, root):
        
        
        
        self.l0=Label(root, text="FITNESS FORM", bg="orange",font=("bold",20))
        self.l0.place(x=140,y=20)

        self.l1=Label(root, text="NAME:", bg="orange",font=("bold",10))
        self.l1.place(x=20,y=100)

        self.e1= Entry(root)
        self.e1.place(x=70,y=100)

        self.l2=Label(root, text="AGE:", bg="orange",font=("bold",10))
        self.l2.place(x=260,y=100)

        self.e2= Entry(root)
        self.e2.place(x=300,y=100)

        self.l3=Label(root, text="GENDER:", width=10, bg="orange",anchor=W,font=("bold",10))
        self.l3.place(x=20,y=150)
        self.var=IntVar()
        self.r1=Radiobutton(root, text="Male", bg="orange", padx=5,variable=self.var, value=1)
        self.r1.place(x=150,y=150)
        self.r2=Radiobutton(root, text="Female", bg="orange", padx=5,variable=self.var, value=2)
        self.r2.place(x=240,y=150)

        self.l4=Label(root, text="Enter the details:-", bg="orange",font=("Times New Roman",15))
        self.l4.place(x=145,y=200)

        self.l5=Label(root, text="Weight(kg):",width=10, anchor=W, bg="orange",font=("bold",10))
        self.l5.place(x=20,y=250)

        self.e5= Entry(root)
        self.e5.place(x=120,y=250)

        self.l6=Label(root, text="Height(m):",width=10, anchor=W, bg="orange",font=("bold",10))
        self.l6.place(x=20,y=270)

        self.e6= Entry(root)
        self.e6.place(x=120,y=270)

        self.l7=Label(root, text="BP:", width=10, anchor=W, bg="orange",font=("bold",10))
        self.l7.place(x=20,y=290)

        self.e7= Entry(root)
        self.e7.place(x=120,y=290)

        self.l8=Label(root, text="Pulse Rate:",width=10, bg="orange",anchor=W, font=("bold",10))
        self.l8.place(x=20,y=310)

        self.e8= Entry(root)
        self.e8.place(x=120,y=310)

        self.l9=Label(root, text="RBC Count:", width=10, bg="orange",anchor=W,font=("bold",10))
        self.l9.place(x=20,y=330)

        self.e9= Entry(root)
        self.e9.place(x=120,y=330)

        self.l10=Label(root, text="WBC Count:", width=10, bg="orange",anchor=W,font=("bold",10))
        self.l10.place(x=20,y=350)

        self.e10= Entry(root)
        self.e10.place(x=120,y=350)

        self.l11=Label(root, text="Platelets:", width=10, bg="orange",anchor=W,font=("bold",10))
        self.l11.place(x=20,y=370)

        self.e11= Entry(root)
        self.e11.place(x=120,y=370)

        self.l12=Label(root, text="HB:" ,width=10,bg="orange", anchor=W,font=("bold",10))
        self.l12.place(x=20,y=390)

        self.e12= Entry(root)
        self.e12.place(x=120,y=390)

        self.l13=Label(root, text="Uric Acid:", width=10, bg="orange",anchor=W,font=("bold",10))
        self.l13.place(x=20,y=410)

        self.e13= Entry(root)
        self.e13.place(x=120,y=410)

        self.l14=Label(root, text="Cholesterol:", width=10, bg="orange",anchor=W,font=("bold",10))
        self.l14.place(x=20,y=430)

        self.e14= Entry(root)
        self.e14.place(x=120,y=430)
        
        
        self.b=Button( text='Generate Report', width=15, height=2,bg='gray', fg='black', relief='ridge', activebackground='white',activeforeground='red', command=self.display)
        self.b.place(x=350,y=410)
        
        self.e1.bind('<Return>', self.display)
        self.e2.bind('<Return>', self.display)
        self.e5.bind('<Return>', self.display)
        self.e6.bind('<Return>', self.display)
        self.e7.bind('<Return>', self.display)
        self.e8.bind('<Return>', self.display)
        self.e9.bind('<Return>', self.display)
        self.e10.bind('<Return>', self.display)
        self.e11.bind('<Return>', self.display)
        self.e12.bind('<Return>', self.display)
        self.e13.bind('<Return>', self.display)
        self.e14.bind('<Return>', self.display)
#*******************************************************************************************************************        
    def display(self):
        top=Toplevel()
        top.title("REPORT")
        top.configure(bg='black')
       
        top.geometry('385x500')
        #********************************************************************************
        
        x=int(self.e7.get())
        self.str1=''
        if 90<=x<140:
            self.str1+='medium'
        if x>=140:
                self.str1+='high'
        if x<90:
                self.str1+='low'
         
        self.bp = Label(top, text="BP(High/Medium/Low):", width=25, bg="orange",anchor=W,font=("bold", 10))
        self.bp.place(x=20, y=10)
        self.e15 = Entry(top)
        self.e15.place(x=240, y=10)
        self.e15.insert(0,self.str1)
        #********************************************************************************
        
        x1=int(self.e8.get())
        self.str2=''
        if 60<=x1<100:
            self.str2+='medium'
        if x1>=100:
                self.str2+='high'
        if x1<60:
                self.str2+='low'


        self.pulse = Label(
            top, text="Pluse Rate(High/Medium/Low):",width=25, bg="orange",anchor=W, font=("bold", 10))
        self.pulse.place(x=20, y=30)
        self.e16 = Entry(top)
        self.e16.place(x=240, y=30)
        self.e16.insert(0,self.str2)
        #********************************************************************************

        x2=float(self.e9.get())
        self.str3=''
        if 4.4<=x2<5.5:
            self.str3+='medium'
        if x2>=5.5:
                self.str3+='high'
        if x2<4.4:
                self.str3+='low'
        self.rbc = Label(
            top, text="RBC Count(High/Medium/Low):", width=25, bg="orange",anchor=W,font=("bold", 10))
        self.rbc.place(x=20, y=50)

        self.e17 = Entry(top)
        self.e17.place(x=240, y=50)
        self.e17.insert(0,self.str3)
        #********************************************************************************
        
        x3=int(self.e10.get())
        self.str4=''
        if 4500<=x3<11000:
            self.str4+='medium'
        if x3>=11000:
            self.str4+='high'
        if x3<4500:
            self.str4+='low'
        self.wbc = Label(top, text="WBC Count(High/Medium/Low):", width=25, bg="orange",anchor=W,font=("bold", 10))
        self.wbc.place(x=20, y=70)

        self.e18 = Entry(top)
        self.e18.place(x=240, y=70)
        self.e18.insert(0,self.str4)
        #********************************************************************************

        x4=int(self.e11.get())
        self.str5=''
        if 150000<=x4<350000:
            self.str5+='medium'
        if x4>=350000:
            self.str5+='high'
        if x4<150000:
            self.str5+='low'
        self.platelets = Label(
            top, text="Platelets(High/Medium/Low):", width=25, bg="orange",anchor=W,font=("bold", 10))
        self.platelets.place(x=20, y=90)

        self.e19 = Entry(top)
        self.e19.place(x=240, y=90)
        self.e19.insert(0,self.str5)
        #********************************************************************************

        x5=float(self.e12.get())
        self.str6=''
        if 13.5<=x5<17.5:
            self.str6+='medium'
        if x5>=17.5:
            self.str6+='high'
        if x5<13.5:
            self.str6+='low'
        self.hb = Label(top, text="HB(High/Medium/Low):", width=25, bg="orange",anchor=W,font=("bold", 10))
        self.hb.place(x=20, y=110)

        self.e20 = Entry(top)
        self.e20.place(x=240, y=110)
        self.e20.insert(0,self.str6)
        #********************************************************************************
        
        x6=float(self.e13.get())
        self.str7=''
        if 3.4<=x6<7:
            self.str7+='medium'
        if x6>=7:
            self.str7+='high'
        if x6<3.4:
            self.str7+='low'
        self.uric = Label(
            top, text="Uric Acid(High/Medium/Low):", width=25, bg="orange",anchor=W,font=("bold", 10))
        self.uric.place(x=20, y=130)

        self.e21 = Entry(top)
        self.e21.place(x=240, y=130)
        self.e21.insert(0,self.str7)
        #********************************************************************************

        x7=int(self.e14.get())
        self.str8=''
        if 125<=x7<200:
            self.str8+='medium'
        if x7>=200:
            self.str8+='high'
        if x7<125:
            self.str8+='low'
       
        self.coles = Label(top, text="Cholesterol(High/Medium/Low):", width=25, bg="orange",anchor=W,font=("bold", 10))
        self.coles.place(x=20, y=150)

        self.e22 = Entry(top)
        self.e22.place(x=240, y=150)
        self.e22.insert(0,self.str8)
        #********************************************************************************

        x9=float(self.e5.get())
        x10=float(self.e6.get())
        self.str9=''
        bmi=(x9/x10**2)
        if bmi < 18.5:
            self.str9="You are underweight"
        elif 18.5 <= bmi < 25:
            self.str9="You are normal"
        elif 25 <= bmi < 30:
            self.str9="You are overweight"
        elif 30<= bmi > 30:
            self.str9="You are obese"
        self.bmi = Label(top, text="BMI:", width=25, bg="orange",anchor=W,font=("bold", 10))
        self.bmi.place(x=20, y=170)
        
        self.e22 = Entry(top)
        self.e22.place(x=240, y=170)
        self.e22.insert(0,self.str9)
        
        #********************************************************************************
root = Tk()
root.title("FITNESS")
root.configure(bg='black')
mb=fitness(root)
mb=display()
root.geometry('480x500')
root.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




