# 람다(lambda) 

lambda 인자 : 표현식

>> def sum( x, y):

>>   return x + y



>> sum(x , y)

>> 30

람다(lambda)식으로 표현 했을 경우

>> (lambda x,y: x + y) (10,20)

>> 30

# map()

map(함수, 리스트)

map 은 함수와 리스트를 인자로 받아 리스트로부터 원소를 꺼내 함수에 적용한 다음 , 결과를 새 리스트에 담아준다

>>> list(map(lambda x: x ** 2, range(5)))

[0, 1, 4, 9, 16]

# reduce()

reduce(함수 , 시퀀스)

>> from functools import reduce < 꼭 써줘야함

>> reduce(lambda x,y: x+y , [0,1,2,3,4,5])

>> 15

위에서 reduce 는 요소 두개를 계속 더하면서 결과를 누적한다

# filter()

filter(함수, 리스트)

>>> list(filter(lambda x: x < 5, range(10))) 

결과값 : [0, 1, 2, 3, 4]

위의 filter에서는 range(10) 으로 전달받은 리스트에서 5보다 작은 값만 걸러서 출력해준다

x < 5 가 '참' 인 숫자만 출력함

>>> list(filter(lambda x: x % 2, range(10)))

위 filter에서는 range(10) 으로 전달받은 리스트와 참 = 1 , 거짓 = 0 인 자료형을 가지고 나머지가 1 즉 '참' 으로 나오는 홀수만 출력해준다..


