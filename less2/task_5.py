for i in range(32, 128, 10):
    s=''
    for j in range(0,10):
        s=f'{s}{i}:{chr(i)}\t'
        i+=1
        if i == 129:
            break
    print(s)



