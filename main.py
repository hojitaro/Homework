def q1():
    aisatsu = ['こんちゃ', 'Hello, World!', 'Hey, guys!', 'あっ、あっ...あ。(コミュ障)', 'ｸｿﾜﾛﾁ']
    for i in range(0, len(aisatsu), 2):
        print(aisatsu[i])


def q2():
    for i in range(9, 0, -1):
        for j in range(9, 0, -1):
            print(i * j)


def q3():
    for i in range(9):
        calc_multi(i + 1)


def calc_multi(a):
    for i in range(9):
        print(a * (i + 1))


if __name__ == '__main__':
    print('----- q1 -----')
    q1()  # 問１
    print('----- q2 -----')
    q2()  # 問２
    print('----- q3 -----')
    q3()  # 問３

