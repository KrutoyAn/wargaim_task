
if __name__ == "__main__":
    with open('input.txt', "r", encoding="utf-8") as f:
        s = (f.read())
        a = s.split('\n')
        k = [x.replace(';', ' ') for x in a]
        for i in k:
            for j in i:
                if j == '2':
                    print(i)
