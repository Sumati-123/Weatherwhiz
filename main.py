import data
import userInput
import display


def getWeather():
    d = userInput.getDatesFromUser()
    extractedJson = data.getJsonFromDate(d)
    weathers = []
    for i in extractedJson:
        des = i["weather"][0]["description"]
        hour = i["dt_txt"].split(" ")[1]
        weathers.append((des, hour))
    if len(weathers) == 0:
        print("No data present for this date")
        return     
    display.show(f"the weather according to time on {d}", weathers)


def getWindSpeed():
    d = userInput.getDatesFromUser()
    extractedJson= data.getJsonFromDate(d)
    windSpeeds = []
    for i in extractedJson:
        des = i["wind"]["speed"]
        hour = i["dt_txt"].split(" ")[1]
        windSpeeds.append((des, hour))
   if len(windSpeeds) == 0:
        print("No data present for this date")
        return         
    display.show(f"the windspeed acccording to time on {d}",windSpeeds)


def getPressure():
    d = userInput.getDatesFromUser()
    extractedJson = data.getJsonFromDate(d)
    pressures = []
    for i in extractedJson:
        des = i["main"]["pressure"]
        hour= i["dt_txt"].split(" ")[1]
        pressures.append((des, hour))
    if len(pressures) == 0:
        print("No data present for this date")
        return
    display.show(f"the pressure acccording to time on {d}",pressures)



if __name__ == "__main__":
    jsondata = data.fetchJSON()

    while True:
        print("1. Get weather \n2. Get Wind Speed\n3. Get Pressure\n0. Exit")

        a = int(input())

        if a == 1:
            getWeather()
        elif a == 2:
            getWindSpeed()
        elif a == 3:
            getPressure()
        elif a == 0:
            break
        else:
            print("invalid input")
