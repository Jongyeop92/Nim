# -*- coding: utf8 -*-


import random


def getPerfectWinList(num, count):

    perfectWinList = []

    perfectWinNum = num - 1

    while perfectWinNum > 0:
        perfectWinList.append(perfectWinNum)

        perfectWinNum -= count + 1
        
    return list(reversed(perfectWinList))


def test():

    assert getPerfectWinList(31, 3) == [2, 6, 10, 14, 18, 22, 26, 30]
    assert getPerfectWinList(10, 2) == [3, 6, 9]
    assert getPerfectWinList( 5, 1) == [2, 4]
    

    print "Success"


def main():

    print "Nim(일명 베스킨라빈스 게임) - 마지막 숫자를 부르면 지는 게임"
    print
    print

    yourTurn = input("선공(0)/후공(1)을 결정하세요: ")

    playerList = [None, None]
    playerList[yourTurn]           = "당신"
    playerList[(yourTurn + 1) % 2] = "컴퓨터"

    #num   = random.randint(10, 31)
    #count = random.randint(2, 9)
    num = 31
    count = 3

    print
    print "총 숫자는 %d, 부를수 있는 수의 개수는 %d 입니다." % (num, count)
    print

    perfectWinList = getPerfectWinList(num, count)

    turn   = 0
    nowNum = 0
    
    while True:
        print "현재 숫자: %d" % nowNum
        print

        if turn % 2 == yourTurn:
            while True:
                selectCount = input("부를 수의 개수를 입력하세요(1 ~ %d): " % count)

                if 1 <= selectCount and selectCount <= count:
                    break

                print "잘못된 입력입니다. 다시 입력하세요."
        else:
            selectCount = None

            for i in range(1, count + 1):
                if nowNum + i in perfectWinList:
                    selectCount = i
                    break

            if selectCount == None:
                selectCount = random.randint(1, count)

        print playerList[turn % 2], ": %d 선택" % selectCount

        nowNum += selectCount

        if nowNum >= num:
            print "%s의 패배!" % playerList[turn % 2]
            break
        
        turn += 1


if __name__ == "__main__":
    #test()
    main()
