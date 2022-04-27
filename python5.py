import random
import time

menu_list = []
menu_list_set = set(menu_list)

print("5개의 메뉴를 추가해주세요! 5개가 입력되면 오늘의 메뉴를 추천해드려요.")
print("동일한 메뉴는 안돼요!")
print()


while True:
    menu = input("메뉴 추가: ")
    menu_list.append(menu)
    new_menu_list_set = menu_list_set | set([menu])

    if menu_list_set == new_menu_list_set:
        del menu_list[-1]
        print("이미 있는 메뉴예요! 다른 메뉴를 입력해주세요.")
        print("현재 메뉴 수 = ", len(menu_list))
        print()

    else:
        menu_list_set = new_menu_list_set

        print("현재 메뉴 수 = ", len(menu_list))
        print()
       
        if len(menu_list) == 5:
            break

for second in [3,2,1]:
    print(second)
    time.sleep(1)
print()

print(menu_list)
print("오늘의 메뉴는?")
print()

for second in [3,2,1]:
    print(second)
    time.sleep(1)
print()

choice = random.choice(menu_list)
print("오늘의 메뉴는 ", menu_list.index(choice)+1, "번째 메뉴, ", choice, "입니다.")