def bmi(weight, height):
    # გამოვთვლით BMI მნიშვნელობას, გავყოთ წონა (weight) სიგრძის კვადრატზე (height**2)
    bmi_value = weight / height ** 2

    # თუ BMI მნიშვნელობა <= 18.5, დავაბრუნებთ "Underweight" (სუსტ წონაში)
    if bmi_value <= 18.5:
        return "Underweight"
    
    # თუ BMI მნიშვნელობა <= 25.0 და უფრო დიდი ვიდრე 18.5, დავაბრუნებთ "Normal" (ნორმალური წონა)
    elif bmi_value <= 25.0:
        return "Normal"
    
    # თუ BMI მნიშვნელობა <= 30.0 და უფრო დიდი ვიდრე 25.0, დავაბრუნებთ "Overweight" (ზედმეტი წონა)
    elif bmi_value <= 30.0:
        return "Overweight"
    
    # თუ BMI მნიშვნელობა 30.0-ზე მეტი, დავაბრუნებთ "Obese" (მოყავება)
    return "Obese"
