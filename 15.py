acases = 24*60*60
cases = 0
for fh in range(2):
    for lh in range(10):
        for fm in range(6):
            for lm in range(10):
                for fs in range(6):
                    for ls in range(10):
                        time = f'{fh}{lh}:{fm}{lm}:{fs}{ls}'
                        if "16" in str(time) and "37" in str(time):
                            cases += 1
                            print(str(time))

for lh in range(4):
    for fm in range(6):
        for lm in range(10):
            for fs in range(6):
                for ls in range(10):
                    time = f'2{lh}:{fm}{lm}:{fs}{ls}'
                    if "16" in str(time) and "37" in str(time):
                        cases += 1
                        print(str(time))
probability = cases / acases
print("Вероятность того что на часах будет и 16 и 37=", probability)