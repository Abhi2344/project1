age = int(input("enter your age"))

gender = input("what is you gender if male type m if female type f")

m_status = input("if married type y else type N")

if gender=="f":

    print("you can only work in urban areas")

elif gender=="m" and (age>=20 and age<40):

    print("you can work from anywhere")

elif gender=="m" and (age>=40 and age<=60):

    print("you can work in urban areas only")

elif not(age<20 and age>60):

    print("error")
