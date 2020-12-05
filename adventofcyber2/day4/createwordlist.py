
with open('wordlist.txt', 'w') as file:
    for month in range(1, 13):
        for day in range(1, 31):
            file.write('2020'+str(month) + str(day) + '\n')
