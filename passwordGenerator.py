import random

literyDuze = "abcdefghijklmnoprstquwxyz"
literyMale = literyDuze.upper()
znaki = ".,/!@#$%^&*()-=_+\|[]{}<>?`~:;'K"

lenght = 100

while True:
    password = ""
    for i in range(lenght):
        password = password + random.choice([random.choice(literyDuze), random.choice(literyMale), random.choice(znaki)])

    print(f"Your genereter password is:\n{password}")

    if input() == "q":
        break
