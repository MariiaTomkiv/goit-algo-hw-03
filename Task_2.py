import random

def get_numbers_tickets():
    try:        
        min = int(input("Введіть ціле число від 1 до 1000: "))
        if min >= 1:
            max = int(input("Введіть ціле число від 1 до 1000: "))
            if max >= 1 and max <= 1000:
                quantaty = int(input("Введіть ціле число в межах від 1 до 1000: "))
                if quantaty >= 1 and quantaty <= 1000:
                        vin_numbers = []
                        count = 0
                        while count < quantaty:
                             c = random.randint(min, max)
                             vin_numbers.append(c)
                             count = count +1
                        vin_numbers.sort()
                        print(vin_numbers)
                else: 
                     print("Введіть коректне число")
            else:
                 print("Введіть коректне число")
        else:
             print("Введіть коректне число")

    except:
        print("Введіть коректне число!")

get_numbers_tickets()