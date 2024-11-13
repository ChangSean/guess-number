#guess number
#產生一個隨機整數1~100(不要印出來)
#讓使用者重複輸入數字去猜
#猜對的話 印出"恭喜答對了!"
#猜錯的話 告訴使用者 比答案大/小

import random

n = random.randint(1, 100)
count = 0
while True:
	count = count + 1
	number = input('請輸入您心裡想到0~100的數字:')
	number = int(number)
	if number == n:
		print('恭喜答對了!')
		print('這是你猜的第', count ,'次~')
		break
	elif number > n:
		print('請輸入小一點的數字')
	elif number < n:
		print('請輸入大一點的數字')
	print('這是你猜的第', count ,'次~')