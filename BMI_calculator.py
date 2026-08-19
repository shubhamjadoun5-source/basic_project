def get_bmi():
    user_weight=int(input("Enter a weghit(KG): "))
    user_height=float(input("Enter a Height(m): "))

    return user_weight, user_height

def calculate_bmi(user_weight, user_height):
    bmi=user_weight / (user_height * user_height)

    return bmi

def get_category(bmi):
    if bmi >= 30:
        bmi_cat = "Obese"
    elif bmi >= 25:
        bmi_cat ="Over Weight"
    elif bmi >= 18.5 :
        bmi_cat = "Normal"
    else: 
        bmi_cat = "Under Weight"

    return bmi_cat

def show_result(user_weight, user_height, bmi, bmi_cat):
    print("Total Weight: ", user_weight)
    print("Total Height: ", user_height)
    print("BMI: ", bmi)
    print("BMI Category: ", bmi_cat)

weight, height = get_bmi()
bmi = calculate_bmi(weight, height)
category = get_category(bmi)
show_result(weight, height, bmi, category)