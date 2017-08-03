# coding:utf-8


def calculate_bmi(weight=70,high=1.75):
    bmi = weight/high**2
    print ("BMI is :%.2f"%bmi)

def Input_Weight_High():
    weight = float(raw_input("Please input your weight:\n"))
    high = float(raw_input("Please input your High:\n"))
    return weight,high
calculate_bmi(*Input_Weight_High())
