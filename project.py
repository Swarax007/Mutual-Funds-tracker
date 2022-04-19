import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pyttsx3
# import docx
speaker=pyttsx3.init()
speaker.say("Hello Parikshit Mahalle Bro kaisa hai bhidu ")
speaker.runAndWait()
print("What is your salary")
sal=input("Enter your salary :")
print("What are your Household expenses")
exp=input("Enter your expenses :")
print("What are your Liablities ")
liab=input("Enter your Liablities")
print("What are your savings")
sav=input("Enter your savings :")
x=['expenses','liablities','savings']
y=[int(exp),int(liab),int(sav)]
plt.plot(x,y)
plt.xlabel('Salary distribution')
plt.ylabel('Amount in rupees')
plt.title('Finance portfolio')
plt.show()
if int(exp)<=int(sal)/2:
    sp=pyttsx3.init()
    sp.say("You    have   balanced   expenses")
    sp.runAndWait()
else:
    sp = pyttsx3.init()
    sp.say("You   have    unbalanced    expenses   and   they   must   be   reduced   to  atleast   half   of   your   salary")
    sp.runAndWait()
if int(liab)<=int(sal)/3:
    sp=pyttsx3.init()
    sp.say("You have balanced assets and liablities")
    sp.runAndWait()
else:
    sp = pyttsx3.init()
    sp.say("You have unbalanced spendings on liablities and they must be reduced to atleast one third of your salary")
    sp.runAndWait()
if int(sav) >= int(sal) / 5:
     sp = pyttsx3.init()
     sp.say("You have good money to invest")
     sp.runAndWait()
else:
     sp = pyttsx3.init()
     sp.say("You have less amount of savings as compared to your salary ")
     sp.runAndWait()



print("Enter your domains of investment ")
print("Mutual funds")
print("Gold")
choice=input("Enter your answer :")
if choice=='Mutual funds':
    print("Select your plans for mutual fund")
    print("High risk-High Return")
    print("Low risk-High Return")
    print("High risk-Low Return")
    print("Low risk-Low Return")
    plan=input("Enter your plan :")
    if plan== 'High risk-High Return':
        book="Book2.xlsx"
        df = pd.read_excel(book,sheet_name="Sheet2")
        print(df)
    if plan== 'Low risk-High Return' :
        book = "Book2.xlsx"
        df = pd.read_excel(book, sheet_name="Sheet1")
        print(df)
    if plan== 'High risk-Low Return':
        book = "Book2.xlsx"
        df = pd.read_excel(book, sheet_name="Sheet3")
        print(df)
    if plan=='Low risk-Low Return':
        book = "Book2.xlsx"
        df = pd.read_excel(book, sheet_name="Sheet4")
        print(df)
        print("Do you want graphical analysis of your Plan ")
data=input("Enter your  plan : ")
time=input("Enter time period for which you want invest in years :  ")
if data=='High risk-High Return' and  int(time)==1:
    x=['Quant Small Cap','UTI Flexi Cap','ICICI Prudential Tech','IIFL Focused Equity','Kotak Small Cap','Aditya Birla Sun Life Digital','Tata Digital India Fund','Axis Midcap Direct Plan','IDFC Sterling','Nippon India Small Cap']
    y=[163.5,74.81,136.16,63.9,120.84,116.26,114.31,59.27,105.04,102.71]
    plt.plot(x,y)
    plt.xlabel("High risk-High Return funds")
    plt.ylabel("% returns in 1 year")
    plt.show()
if data=='High risk-High Return' and int(time)==3:
    y=['Quant Small Cap Fund','UTI Flexi Cap Fund Direct Growth','ICICI Prudential Technology Fund','IIFL Focused Equity Fund Direct Growth Fund','Kotak Small Cap Fund','Aditya Birla Sun Life Digital India Fund','Tata Digital India Fund','Axis Midcap Direct Plan Growth','IDFC Sterling Value Fund','Nippon India Small Cap Fund']
    x=[19.86,16.63,27.79,18.48,13.71,26.95,27.25,16.80,4.51,9.12]
    plt.plot(x, y)
    plt.ylabel("High risk-High Return funds")
    plt.xlabel("% returns in 3 year")
    plt.show()
if data=='High risk-High Return' and int(time)==5:
    y=['Quant Small Cap Fund','UTI Flexi Cap Fund Direct Growth','ICICI Prudential Technology Fund','IIFL Focused Equity Fund Direct Growth Fund','Kotak Small Cap Fund','Aditya Birla Sun Life Digital India Fund','Tata Digital India Fund','Axis Midcap Direct Plan Growth','IDFC Sterling Value Fund','Nippon India Small Cap Fund']
    x=[14.26,17.11,21.48,19.10,17.34,22.35,20.25,18.83,14.43,18.5]
    plt.plot(x, y)
    plt.ylabel("High risk-High Return funds")
    plt.xlabel("% returns in 5 year")
    plt.show()
if data=='Low risk -High Return' and int(time)==1:
    y=['Quant Absolute Fund','Quant Mid Cap Fund','JM Equity Hybrid Fund','Kotak Equity Hybrid Fund','BOI AXA Mid & Small Cap Equity & Debt Fund','Nippon India Equity Hybrid Fund','HDFC Childrens Gift Fund','HDFC Hybrid Equity Fund','UTI Hybrid Equity Fund','Aditya Birla Sun Life Equity Hybrid 95 Fund']
    x=[82.99,81.16,72.19,60.73,58.76,53.53,52.75,52.02,51.73,51.39]
    plt.plot(x, y)
    plt.ylabel("Low risk-High Return funds")
    plt.xlabel("% returns in 1 year")
    plt.show()
if data=='Low risk -High Return' and int(time)==3 :
    y=['Quant Absolute Fund','Quant Mid Cap Fund','JM Equity Hybrid Fund','Kotak Equity Hybrid Fund','BOI AXA Mid & Small Cap Equity & Debt Fund','Nippon India Equity Hybrid Fund','HDFC Childrens Gift Fund','HDFC Hybrid Equity Fund','UTI Hybrid Equity Fund','Aditya Birla Sun Life Equity Hybrid 95 Fund']
    x=[18.57,15.37,9.19,10.79,5.53,1.12,9.6,7.35,6.49,6.28]
    plt.plot(x, y)
    plt.ylabel("Low risk-High Return funds")
    plt.xlabel("% returns in 3 year")
    plt.show()
if data == 'Low risk -High Return' and int(time) == 5:
    y=['Quant Absolute Fund','Quant Mid Cap Fund','JM Equity Hybrid Fund','Kotak Equity Hybrid Fund','BOI AXA Mid & Small Cap Equity & Debt Fund','Nippon India Equity Hybrid Fund','HDFC Childrens Gift Fund','HDFC Hybrid Equity Fund','UTI Hybrid Equity Fund','Aditya Birla Sun Life Equity Hybrid 95 Fund']
    x=[16.16,14.29,9.67,12.4,10.8,7.18,12.91,11.23,10.37,10.07]
    plt.plot(x, y)
    plt.ylabel("Low risk-High Return funds")
    plt.xlabel("% returns in 5 year")
    plt.show()
if data== 'High risk -Low Return' and int(time) == 1:
    y=['HDFC Multi - Asset Fund','Aditya Birla Sun Life Regular Savings Fund','Baroda Treasury Advantage Fund','JM Low Duration Fund','UTI Regular Savings Fund','Kotak debt hydrid fund','SBI Debt Hybrid Fund','IDBI Equity Savings Fund','HDFC Hybrid Debt Fund','UTI Dual Advantage FTF - Series III - I']
    x=[42.5,28.37,26.97,26.22,23.43,23,22.91,22.21,21.23,20.92]
    plt.plot(x, y)
    plt.ylabel("High risk-Low Return funds")
    plt.xlabel("% returns in 1 year")
    plt.show()
if data == 'High risk -Low Return' and int(time) == 3 :
    y=['HDFC Multi - Asset Fund','Aditya Birla Sun Life Regular Savings Fund','Baroda Treasury Advantage Fund','JM Low Duration Fund','UTI Regular Savings Fund','Kotak debt hydrid fund','SBI Debt Hybrid Fund','IDBI Equity Savings Fund','HDFC Hybrid Debt Fund','UTI Dual Advantage FTF - Series III - I']
    x=[9.47,6.03,-8.6,5.62,5.27,8.98,7.42,6.22,7.14,4.24]
    plt.plot(x, y)
    plt.ylabel("High risk-Low Return funds")
    plt.xlabel("% returns in 3 year")
    plt.show()
if data == 'High risk -Low Return' and int(time) == 5:
    y=['HDFC Multi - Asset Fund', 'Aditya Birla Sun Life Regular Savings Fund', 'Baroda Treasury Advantage Fund','JM Low Duration Fund','UTI Regular Savings Fund','Kotak debt hydrid fund','SBI Debt Hybrid Fund','IDBI Equity Savings Fund','HDFC Hybrid Debt Fund','UTI Dual Advantage FTF - Series III - I']
    x=[9.62,8.63,-2.26,6.29,7.32,9.37,8.24,5.79,8.36,6.79]
    plt.plot(x, y)
    plt.ylabel("High risk-Low Return funds")
    plt.xlabel("% returns in 5 year")
    plt.show()
if data=='Low risk -Low Return' and int(time) == 1 :
    y=['HDFC Money Market Fund','Aditya Birla Sun Life Money Manager Fund','Tata Money Market Fund','ICICI Prudential Money Market Fund','Axis Money Market Fund','UTI Money Market Fund','DSP Savings Fund','Nippon India Money Market Fund','SBI Magnum Ultra Short Duration Fund','Nippon India Ultra Short Duration Fund']
    x=[5.94,5.87,5.77,5.6,5.49,5.48,5.46,5.35,5.17,4.99]
    plt.plot(x, y)
    plt.ylabel("Low risk-Low Return funds")
    plt.xlabel("% returns in 1 year")
    plt.show()
if data == 'Low risk -Low Return' and int(time) == 3 :
    y=['HDFC Money Market Fund','Aditya Birla Sun Life Money Manager Fund','Tata Money Market Fund','ICICI Prudential Money Market Fund','Axis Money Market Fund','UTI Money Market Fund','DSP Savings Fund','Nippon India Money Market Fund','SBI Magnum Ultra Short Duration Fund','Nippon India Ultra Short Duration Fund']
    x=[7.03,7.19,4.43,6.9,6.80,6.93,6.57,6.99,6.87,4.14]
    plt.plot(x, y)
    plt.ylabel("Low risk-Low Return funds")
    plt.xlabel("% returns in 3 year")
    plt.show()
if data == 'Low risk -Low Return' and int(time) == 5 :
    y=['HDFC Money Market Fund','Aditya Birla Sun Life Money Manager Fund','Tata Money Market Fund','ICICI Prudential Money Market Fund','Axis Money Market Fund','UTI Money Market Fund','DSP Savings Fund','Nippon India Money Market Fund','SBI Magnum Ultra Short Duration Fund','Nippon India Ultra Short Duration Fund']
    x=[6.93,7.14,5.43,6.94,6.30,6.95,6.43,6.97,6.9,4.93]
    plt.plot(x, y)
    plt.ylabel("Low risk-Low Return funds")
    plt.xlabel("% returns in 5 year")
    plt.show()
else:
    x = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
    y = [26400, 31050, 29600, 28006, 26343, 28623, 29667, 31438, 35220, 48651]
    plt.plot(x, y)
    plt.xlabel("Financial year")
    plt.ylabel("Price of gold")
    plt.title("Gold Rates comparison")
    plt.show()
amt=input("Enter amount you want to invest monthly : ")
sch=input("Enter name of mutual fund")
dur=input("Duration for which you want to invest : ")
x = int(amt) * 163.5 * 12/100
if sch=='Quant Small Cap Fund' and dur==1:
   print("None")
else :
    print("Your amount will become be",x)
y=int(amt) * 74.81 * 12/100
