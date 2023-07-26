from datetime import date, datetime


def getDatesFromUser():
    while True:
        date_raw = input('Enter date (DD-MM-YYYY): ')
        try:
            return datetime.strptime(date_raw, "%d-%m-%Y").date()
        except ValueError:
            print("Invalid Date")
