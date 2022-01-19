#입력값
s = "one4seveneight"
# 숫자 대칭하는 문자열
num_str = ['zero','one','two','three','four','five','six','seven','eight','nine']
#빈 딕셔너리를 생성
all_num = {}
#0~9까지 숫자를 돌면서 딕셔너리에 zero : 0 형식으로 저장함
for i in range(10):
    all_num[num_str[i]] = i
# 문자열을 저장할 변수
a = ''
# 결과값을 저장할 변수
c = ''
#입력값을 돌면서 숫자와 문자를 구분하여 숫자는
# c (결과값)에 저장하고 문자열은 a 에 붙여서 저장한다
# 만약 a 가 num_str에 있을경우 대칭되는 숫자로 변경해주고 결과값에 더한다
for i in s:
    if i.isdigit():
        c += i
    elif i.isalpha():
        a += i
        if a in num_str:
            c+= str(all_num[a])
            a = ""
#마지막에 int로 타입을 전환한다
print(int(c))

########################################################################

def solution(s):
    num_dict = {
    'zero':'0',
    'one': '1',
    'two':'2',
    'three':'3',
    'four':'4',
    'five':'5',
    'six':'6',
    'seven':'7',
    'eight':'8',
    'nine':'9'
    }
    for i in num_dict:
        if s.find(i) >= 0: s = s.replace(i, num_dict[i])
    return int(s)
