import random
answer = random.randint(0,99)
min = 0 
max =99

for i in range(10):
    guess = int(input("숫자를 입력하세요 (범위:%d~%d):" %(min,max)))
    if(guess<answer):
        print("틀렸습니다 더 큰 숫자입니다")
        min =guess
    elif(guess >answer):
        print("틀렸습니다 더 작은 숫자입니다")
        max=guess
    else:
        print("정답입니다 %d번 만에 맞추셨습니다" % (i+1))
        break
    
print("게임 끝")