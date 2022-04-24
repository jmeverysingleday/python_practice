fruit = {}

while True:
    type = input("Enter a fruit type (q to quit): ")

    if type == "q":
        break
    else:
        weight = input("Enter the weight in kg: ")
        fruit[type] = weight

print(fruit)

    