
def baskin():
    import random
    # 컴퓨터가 먼저 숫자를 말할지, 플레이어가 먼저 숫자를 말할지는 랜덤으로 정한다.
    # 0 or 1을 반환
    # 31이 되면 스탑
    sequence = random.randint(0,1) # player or computer random sequence
    number = [] # add number
    number_31 = 0 # current min number
    win_num = [2, 6, 10, 14, 18, 22, 26, 30] # victory number in 31game
    while True:
        
        if sequence == 0:
            player = int(input('1~3중 입력하세요:'))
            player_num = input('수를 입력하세요(ex)1,2,3): ').split(',')
            if player > 3 or player < 0 :
                print('다시 입력하세요')
                continue
            elif len(player_num) != player:
                print('개수가 맞지않습니다')
                continue
            else :
                for i in range(player):
                    number_31 += 1
                    number.append(int(player_num[i]))
                    if number_31 > 31:
                        break
                    print(f'player: {int(player_num[i])}')
            sequence += 1 # next computer

        elif sequence == 1:
            
            if number == []:
                com = 2
            else:    
                for i , n in enumerate(win_num): # victory algorithm 
                    if number_31 < n <= number_31 + 3:
                        com = n - number_31
                        break
                    else:
                        com = random.randint(1,3)
                        
            
            for i in range(com):

                number_31 += 1
                number.append(number_31)
                if number_31 > 31:
                    break
                print(f'computer: {number_31}')
            
            sequence -= 1 # next player
            
        if number_31 >= 31:
            break

    if sequence == 0:
        print('player WIN')
    else:
        print('Computer WIN')
    print(number)



baskin()
