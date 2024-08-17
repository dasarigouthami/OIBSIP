def calculate(w,h):
    bmi=w/(h**2)
    return bmi
def category(bmi):
    if bmi<18.5:
        return "underweight"
    elif 18.5<=bmi<24.9:
        return "normal weight"
    elif 25<=bmi<29.9:
        return "overweight"
    else:
        return "obese"
def user_input():
    w=float(input("enter the weight in kgs: "))
    h=float(input("Enter the height in meters: "))
    return w,h
def main():
    w,h=user_input()
    bmi=calculate(w,h)
    group=category(bmi)
    print(f"your BMI is:{bmi:.2f}")
    print(f"you are classified as:{group}")
if __name__=="__main__":
    main()
