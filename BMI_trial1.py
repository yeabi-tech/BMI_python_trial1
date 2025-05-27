 #BMI with (weight,name,height)inputs
name=input("enter your name: ")
Weight =int(input("enter your weight in kg: "))
height=float(input("enter height in meters: "))
BMI=(Weight )/(height)
if BMI>0:
    if(BMI<40):
        print(name+",you are skinny.you need to gain muscles")
    elif(BMI<60):
        print(name+",you are thin")
    elif(BMI<80):
        print(name+",you are midsize")
    else:
        print(name+",just input facts")


print(f"Here is your BMI {BMI}")





