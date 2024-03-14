print('DZ15')

while True:
    inputtedNumber = int(input('Enter your number '))

    if not(0 <= inputtedNumber < 8640000):
        print('You are wrong')
    else:
        denominator = inputtedNumber
        divider = {"days": 86400, "hours": 3600, "minutes": 60, "seconds": 1}
        res = {}

        for key, value in divider.items():
            if key == "days":
                res[key], denominator = divmod(denominator, value)
                if res[key] % 10 == 1 and res[key] != 11:
                    res[key] = str(res[key]) + " день"
                elif 2 <= res[key] % 10 <= 4 and (res[key] < 10 or res[key] >= 20):
                    res[key] = str(res[key]) + " дні"
                else:
                    res[key] = str(res[key]) + " днів"
            else:
                res[key], denominator = divmod(denominator, value)
                res[key] = str(res[key]).zfill(2)

        print(f"{res['days']}, {res['hours']}:{res['minutes']}:{res['seconds']}")
        print('Thank you for using')
        break