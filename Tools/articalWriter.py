import pyperclip


def maker1(keysAndValues: list, bikeName: str) -> str:
    finalArtical=""
    articalValue={
        'Cooling system': "Generally, the cooling system works for 3 necessary functions. First, it removes heat from the engine; second, it maintains the engine operating temperature wherever it works most efficiently; and eventually, it brings the engine up to the proper operating temperature as quickly as doable the -bikeName- used a -Cooling system- cooling system for these functions. ",
        'Engine details': "The engine is the heart of your car. the main function of the engine is to give energy to the vehicles. here bike -bikeName- is used -Engine details-.",
        'Engine type': "There are many bike engine types. such as fule type and electrical type.in bike -bikeName- used -Engine type-.",
        'Max RPM': "RPM stands for revolutions per minute. In cars, rpm measures how many times the engine's crankshaft makes one full rotation every minute. this bike's maximum RPM is -Max RPM-.",
        'Power': "In the context of automobiles, power is often described as horsepower. Bike -bikeName- was released with the horsepower of -Power-.",
        'Top speed': " And this bike can reach maximum speed is -Top speed-.",
        'Transmission type final drive': "The meaning of the final drive of bike is simply the last step in the process of transferring engine power to a bike's rear wheel.Main type of the transmissions are Chain, Belt or Shaft. and here -Transmission type final drive- is used for this transmission.",
        'Category': "This bike is a -Category-. ",
        'Model': "-bikeName- is developed by -Model-. ",
        'Price as new': "The the market price of the bike -bikeName- is -Price as new-. ",
        'Rating': "currently the bike have a rating is -Rating-. ",
        'Year': "This bike published at -Year-. ",
        'Frame type': "The body part is the important factor for the attractiveness and safety of the body here the bike use -Frame type-. ",
        'Front brakes': "here used -Front brakes- for the front brakes. ",
        'Rear brakes': "And the -Rear brakes- for the rear brakes.",
        'Dry weight': "Bike -bikeName- around the weight is -Dry weight-. ",
        'Overall height': "And the height, length, and width respectly -Overall height-, ",
        'Overall length': "-Overall length-, ",
        'Overall width': "and -Overall width-. ",
        'Power weight ratio': "weight ratio is the amount of power a vehicle has relative to its weight . here -Power weight ratio- used.",
    }
    # print(list(articalValue.keys())[0])
    for i in list(keysAndValues.keys()):
        if i in list(articalValue.keys()):

            # finalArtical+=articalValue[i].replace("-bikeName-",bikeName).replace("-"+i+"-",articalValue.get(i))
            finalArtical += articalValue[i].replace(
                "-bikeName-", bikeName).replace("-"+i+"-", keysAndValues[i])
    return finalArtical
    pass


def maker2(keysAndValues: list, bikeName: str) -> str:
    finalArtical = ""
    articalValue = {
        'Dry weight': "Bike -bikeName- around the weight is -Dry weight-. ",
        'Overall height': "And the height, length, and width respectly -Overall height-, ",
        'Overall length': "-Overall length-, ",
        'Overall width': "and -Overall width-. ",
        'Power weight ratio': "weight ratio is the amount of power a vehicle has relative to its weight . here -Power weight ratio- used.",
        }
    # print(list(articalValue.keys())[0])
    for i in list(keysAndValues.keys()):
        if i in list(articalValue.keys()):

            # finalArtical+=articalValue[i].replace("-bikeName-",bikeName).replace("-"+i+"-",articalValue.get(i))
            finalArtical += articalValue[i].replace(
                "-bikeName-", bikeName).replace("-"+i+"-", keysAndValues[i])
    return finalArtical
    pass

if __name__=="__main__":
    bikeName = "Acabion Da Vinci 650-VI 2011"
    keys = {
        'Dry weight':"*****", 
        'Overall height':"*****", 
        'Overall length':"*****", 
        'Overall width':"*****", 
        'Power weight ratio':"*****",
            }
    artical = maker2(keys, bikeName)
    print(artical)
    pyperclip.copy(artical)
