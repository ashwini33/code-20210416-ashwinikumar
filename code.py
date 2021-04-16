def bmi(mass_in_kg, height_in_centimeter):
    """
    This function returns the bmi.
    """
    height_in_meter = height_in_centimeter/100
    bmi= mass_in_kg/(height_in_meter**2)
    bmi = round(bmi, 3)
    return bmi

def bmi_category(bmi):
    """
    This funciton return the bmi category.
    """
    if bmi <= 18.4:
        return "UnderWeight"
    elif bmi >=18.5 and bmi <= 24.9:
        return "NormalWeight"
    elif bmi >= 25 and bmi <= 29.9:
        return "OverWeight"
    elif bmi >=30 and bmi <=34.9:
        return "ModeratelyObese"
    elif bmi >=35 and bmi <= 39.9:
        return "SeverelyObese"
    else:
        return "VerySeverelyObese"
    
def health_risk(bmi):
    """
    This funciton returns the health risk
    """
    if bmi <= 18.4:
        return "MalnutritionRisk"
    elif bmi >=18.5 and bmi <= 24.9:
        return "LowRisk"
    elif bmi >= 25 and bmi <= 29.9:
        return "EnhancedRisk"
    elif bmi >=30 and bmi <=34.9:
        return "MediumRisk"
    elif bmi >=35 and bmi <= 39.9:
        return "HighRisk"
    else:
        return "VeryHighRisk"
def isOverWeight(bmi):
    if bmi >= 25 and bmi <= 29.9:
        return True
    else:
        return False

def getOverWeightNumber(data):
    import pandas as pd
    df = pd.read_json(data)
    
    ## Adding required column
    df["BMI"] = bmi(df.WeightKg, df.HeightCm)
    df["BMICategory"] = df.BMI.apply(bmi_category)
    df["HealthRisk"] = df.BMI.apply(health_risk)
    
    ## print the current data frame
    print(df)
    
    ## export the current data frame to csv file
    df.to_csv("analysedData.csv", index=False)
    
    print("#################################################################")
    
    # Get and Print number of over weight people
    numberOfOverWeightPeople = sum(df.BMI.apply(lambda x: isOverWeight(x)))
    print(f"Number of Over weight people is: {numberOfOverWeightPeople}")

    # return the number of over weight people in case other function requires it
    return numberOfOverWeightPeople


getOverWeightNumber("health_data.json")

    
