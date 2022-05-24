
def search_mod(numb, x):
    new_num = []
    round_digit = 0
    count = 0
    new_count = 0
    flag = True

    while flag:
        round_digit += 1
        for i in numb:
            digit = digital_sum(i)
            if (i % x == 0 and digit == True):
                count += 1
            elif get_duo_int(i, x) == True:
                count += 1
            else:
                new_num.append(i)

        new_count = count
        count = 0
        x = new_count
        numb = new_num
        new_num = []

        if new_count == 0:
            flag = False

    return round_digit

def digital_sum(num):
    if (num % 9) or num and 9:
        return True
    else:
        return False

def get_duo_int(n, k):
    flag = False
    while n > 0:
        if n % 10 == k:
            flag = True
            break
        n //= 10
    if flag:
        return True
    else:
        return False

x = 3
numb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


##########
#x = int(input())
#numb = [i for i in range(int(input("Начало: ")), int(input("Конец: ")) + 1)] # for range
##########


if __name__ == "__main__":
    print(search_mod(numb, x))
