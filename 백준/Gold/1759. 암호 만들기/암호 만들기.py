def password(length, idx):
    if length == l:
        mo_cnt = 0
        ja_cnt = 0
        for i in password_lst:
            if i in aeiou_lst:
                mo_cnt += 1
            elif i not in aeiou_lst :
                ja_cnt += 1

        if mo_cnt >= 1 and ja_cnt >= 2 :
            for k in password_lst:
                print(k, end='')
            print()
            return
        return

    for jdx in range(idx, c): #c == len(word_lst)
        password_lst[length] = word_lst[jdx]
        password(length+1,jdx+1)

l, c = map(int, input().split())
aeiou_lst = list("aeiou")
password_lst = [0 for _ in range(l)]
word_lst = sorted((list(map(str, input().split()))))
password(0,0)
