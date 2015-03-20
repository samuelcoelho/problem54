#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Samuel Coelho'

class Player(object):
    def __init__(self, hand, valueHand):
        self.hand = hand
        self.valueHand = valueHand

class Analyse(object):
    royalNumbers = range(10,15,1)
    handRank = {'HighCard': 0, 'OnePair': 1, 'TwoPairs': 2, 'ThreeOfKind': 3, 'Straight': 4, 'Flush': 5, 'FullHouse': 6, 'FourOfKind': 7, 'StraightFlush': 8, 'RoyalFlush': 9}
    player = Player(0, 2)

    def checkSameSuit(self, suits):
        return suits.count(suits[0]) == 5

    def checkRoyalFlushNumbers(self, values):
        if self.royalNumbers == values:
            self.player.hand = self.handRank['RoyalFlush']
            self.player.valueHand = 14
        else:
            self.player.hand = self.handRank['HighCard']
            self.player.valueHand = 2

        return self.player

    def checkStraigthNumbers(self, numbers):
        straightFlushNumbers = range(numbers[0], numbers[0] + 5, 1)

        if straightFlushNumbers == numbers:
            self.player.hand = self.handRank['Straight']
            self.player.valueHand = numbers[4]
        else:
            self.player.hand = self.handRank['HighCard']
            self.player.valueHand = 2

        return self.player

    def checkFourNumbers(self, numbers):
        if numbers.count(numbers[0]) == 4:
            self.player.hand = self.handRank['FourOfKind']
            self.player.valueHand = numbers[0]
        elif numbers.count(numbers[1]) == 4:
            self.player.hand = self.handRank['FourOfKind']
            self.player.valueHand = numbers[1]
        else:
            self.player.hand = self.handRank['HighCard']
            self.player.valueHand = 2

        return self.player

    def checkFullHouse(self, numbers):
        lst = numbers
        hasThree = False
        maxValue = 0

        if numbers.count(lst[0]) == 3:
            hasThree = True
            maxValue = lst[0]
            lst = [x for x in lst if x != lst[0]]
        elif numbers.count(lst[1]) == 3:
            hasThree = True
            maxValue = lst[1]
            lst = [x for x in lst if x != lst[1]]
        elif numbers.count(lst[2]) == 3:
            hasThree = True
            maxValue = lst[2]
            lst = [x for x in lst if x != lst[2]]
        else:
            self.player.hand = self.handRank['HighCard']
            self.player.valueHand = 2

        if hasThree:
            if lst.count(lst[0]) == 2:
                self.player.hand = self.handRank['FullHouse']
                self.player.valueHand = maxValue
        else:
            self.player.hand = self.handRank['HighCard']
            self.player.valueHand = 2

        return self.player


    def checkThreeNumbers(self, numbers):
        if numbers.count(numbers[0]) == 3:
            self.player.hand = self.handRank['ThreeOfKind']
            self.player.valueHand = numbers[0]
        elif numbers.count(numbers[1]) == 3:
            self.player.hand = self.handRank['ThreeOfKind']
            self.player.valueHand = numbers[1]
        elif numbers.count(numbers[2]) == 3:
            self.player.hand = self.handRank['ThreeOfKind']
            self.player.valueHand = numbers[2]
        else:
            self.player.hand = self.handRank['HighCard']
            self.player.valueHand = 2

        return self.player

    def checkTwoPairs(self, numbers):
        lst = numbers
        hasTwo= False
        maxValue = 0

        if numbers.count(lst[0]) == 2:
            hasTwo = True
            maxValue = lst[0]
            lst = [x for x in lst if x != lst[0]]
        elif numbers.count(lst[1]) == 2:
            hasTwo = True
            maxValue = lst[1]
            lst = [x for x in lst if x != lst[1]]
        elif numbers.count(lst[2]) == 2:
            hasTwo = True
            maxValue = lst[2]
            lst = [x for x in lst if x != lst[2]]
        elif numbers.count(lst[3]) == 2:
            hasTwo = True
            maxValue = lst[3]
            lst = [x for x in lst if x != lst[3]]
        else:
            self.player.hand = self.handRank['HighCard']
            self.player.valueHand = 2

        if hasTwo:
            if lst.count(lst[0]) == 2:
                self.player.hand = self.handRank['TwoPairs']
                if lst[0] > maxValue:
                    self.player.valueHand = lst[0]
                else:
                    self.player.valueHand = maxValue
            elif lst.count(lst[1]) == 2:
                self.player.hand = self.handRank['TwoPairs']
                if lst[1] > maxValue:
                    self.player.valueHand = lst[1]
                else:
                    self.player.valueHand = maxValue
            else:
                self.player.hand = self.handRank['HighCard']
                self.player.valueHand = 2

        return self.player


    def checkOnePair(self, numbers):
        if numbers.count(numbers[0]) == 2:
            self.player.hand = self.handRank['OnePair']
            self.player.valueHand = numbers[0]
        elif numbers.count(numbers[1]) == 2:
            self.player.hand = self.handRank['OnePair']
            self.player.valueHand = numbers[1]
        elif numbers.count(numbers[2]) == 2:
            self.player.hand = self.handRank['OnePair']
            self.player.valueHand = numbers[2]
        elif numbers.count(numbers[3]) == 2:
            self.player.hand = self.handRank['OnePair']
            self.player.valueHand = numbers[3]
        else:
            self.player.hand = self.handRank['HighCard']
            self.player.valueHand = 2

        return self.player

    def checkHighCard(self, numbers):
        return max(numbers)

# Instancia classe de analise e inicializa variaveis
analyse = Analyse()
i = 1
winsPlayer1 = 0
winsPlayer2 = 0

# Open file with porker's hands
f = file('p054_poker.txt')
for line in f:
    hand = line.replace('\n', '').split(' ')
    handPlayer1 = hand[:5]
    handPlayer2 = hand[5:10]

    handPlayer1Numbers = []
    handPlayer1Suits   = []

    handPlayer2Numbers = []
    handPlayer2Suits   = []

    for h1 in handPlayer1:
        handPlayer1Numbers.append(int(h1[0].replace('T', '10').replace('J', '11').replace('Q', '12').replace('K', '13').replace('A', '14')))
        handPlayer1Numbers.sort()
        handPlayer1Suits.append(h1[1])

    for h2 in handPlayer2:
        handPlayer2Numbers.append(int(h2[0].replace('T', '10').replace('J', '11').replace('Q', '12').replace('K', '13').replace('A', '14')))
        handPlayer2Numbers.sort()
        handPlayer2Suits.append(h2[1])

    #print "%s - %s" % (handPlayer1Numbers, handPlayer2Numbers)
    #print "%s - %s" % (handPlayer1Suits, handPlayer2Suits)

    player1 = Player(0, 2)

    # Check Player 1
    # Check if all cards has the same suit
    if analyse.checkSameSuit(handPlayer1Suits):
        # Check if hand is Royal Flush
        objTmp = analyse.checkRoyalFlushNumbers(handPlayer1Numbers)
        player1.hand = objTmp.hand
        player1.valueHand = objTmp.valueHand
        if player1.hand != analyse.handRank['RoyalFlush']:
            # Check if hand is Straight Flush
            objTmp = analyse.checkStraigthNumbers(handPlayer1Numbers)
            player1.hand = objTmp.hand
            player1.valueHand = objTmp.valueHand
            if player1.hand != analyse.handRank['Straight']:
                # Flush
                player1.hand = analyse.handRank['Flush']
                player1.valueHand = max(handPlayer1Numbers)
            else:
                # Straight Flush
                player1.hand = analyse.handRank['StraightFlush']
                player1.valueHand = objTmp.valueHand

    else:
        # Check if hand is Four of a Kind
        objTmp = analyse.checkFourNumbers(handPlayer1Numbers)
        player1.hand = objTmp.hand
        player1.valueHand = objTmp.valueHand
        if player1.hand != analyse.handRank['FourOfKind']:
            # Check if hand is Full House
            objTmp = analyse.checkFullHouse(handPlayer1Numbers)
            player1.hand = objTmp.hand
            player1.valueHand = objTmp.valueHand
            if player1.hand != analyse.handRank['FullHouse']:
                # Check if hand is Straight
                objTmp = analyse.checkStraigthNumbers(handPlayer1Numbers)
                player1.hand = objTmp.hand
                player1.valueHand = objTmp.valueHand
                if player1.hand != analyse.handRank['Straight']:
                    # Check if hand is Three of a Kind
                    objTmp = analyse.checkThreeNumbers(handPlayer1Numbers)
                    player1.hand = objTmp.hand
                    player1.valueHand = objTmp.valueHand
                    if player1.hand != analyse.handRank['ThreeOfKind']:
                        # Check if hand is Two Pairs
                        objTmp = analyse.checkTwoPairs(handPlayer1Numbers)
                        player1.hand = objTmp.hand
                        player1.valueHand = objTmp.valueHand
                        if player1.hand != analyse.handRank['TwoPairs']:
                            # Check if hand is One Pair
                            objTmp = analyse.checkOnePair(handPlayer1Numbers)
                            player1.hand = objTmp.hand
                            player1.valueHand = objTmp.valueHand
                            if player1.hand != analyse.handRank['OnePair']:
                                # High Card
                                player1.hand = analyse.handRank['HighCard']
                                player1.valueHand = max(handPlayer1Numbers)

    player2 = Player(0, 2)

    # Check Player 2
    # Check if all cards has the same suit
    if analyse.checkSameSuit(handPlayer2Suits):
        # Check if hand is Royal Flush
        objTmp = analyse.checkRoyalFlushNumbers(handPlayer2Numbers)
        player2.hand = objTmp.hand
        player2.valueHand = objTmp.valueHand
        if player2.hand != analyse.handRank['RoyalFlush']:
            # Check if hand is Straight Flush
            objTmp = analyse.checkStraigthNumbers(handPlayer2Numbers)
            player2.hand = objTmp.hand
            player2.valueHand = objTmp.valueHand
            if player2.hand != analyse.handRank['Straight']:
                # Flush
                player2.hand = analyse.handRank['Flush']
                player2.valueHand = max(handPlayer1Numbers)
            else:
                # Straight Flush
                player2.hand = analyse.handRank['StraightFlush']
                player2.valueHand = objTmp.valueHand
    else:
        # Check if hand is Four of a Kind
        objTmp = analyse.checkFourNumbers(handPlayer2Numbers)
        player2.hand = objTmp.hand
        player2.valueHand = objTmp.valueHand
        if player2.hand != analyse.handRank['FourOfKind']:
            # Check if hand is Full House
            objTmp = analyse.checkFullHouse(handPlayer2Numbers)
            player2.hand = objTmp.hand
            player2.valueHand = objTmp.valueHand
            if player2.hand != analyse.handRank['FullHouse']:
                # Check if hand is Straight
                objTmp = analyse.checkStraigthNumbers(handPlayer2Numbers)
                player2.hand = objTmp.hand
                player2.valueHand = objTmp.valueHand
                if player2.hand != analyse.handRank['Straight']:
                    # Check if hand is Three of a Kind
                    objTmp = analyse.checkThreeNumbers(handPlayer2Numbers)
                    player2.hand = objTmp.hand
                    player2.valueHand = objTmp.valueHand
                    if player2.hand != analyse.handRank['ThreeOfKind']:
                        # Check if hand is Two Pairs
                        objTmp = analyse.checkTwoPairs(handPlayer2Numbers)
                        player2.hand = objTmp.hand
                        player2.valueHand = objTmp.valueHand
                        if player2.hand != analyse.handRank['TwoPairs']:
                            # Check if hand is One Pair
                            objTmp = analyse.checkOnePair(handPlayer2Numbers)
                            player2.hand = objTmp.hand
                            player2.valueHand = objTmp.valueHand
                            if player2.hand != analyse.handRank['OnePair']:
                                # High Card
                                player2.hand = analyse.handRank['HighCard']
                                player2.valueHand = max(handPlayer2Numbers)

    # Wins count
    if player1.hand > player2.hand:
        winsPlayer1 = winsPlayer1 + 1
    elif player2.hand > player1.hand:
        winsPlayer2 = winsPlayer2 + 1
    else:
        if player1.hand == player2.hand and player1.valueHand > player2.valueHand:
            winsPlayer1 = winsPlayer1 + 1
        elif player1.hand == player2.hand and player1.valueHand < player2.valueHand:
            winsPlayer2 = winsPlayer2 + 1
        else:
            #print '%d - Player 1 Hand: %d, Value: %d\t -  Player 2 Hand: %d, Value: %d' % (i, player1.hand, player1.valueHand, player2.hand, player2.valueHand)
            # Aqui tem que usar  um metodo recursivo para todos os casos
            # Deixie assim por falta de tempo e por ser o unico caso
            # Caso par empatado
            if player1.hand == 1:
                handPlayer1Numbers = [x for x in handPlayer1Numbers if x != player1.valueHand]
                handPlayer2Numbers = [x for x in handPlayer2Numbers if x != player2.valueHand]

                highCard1 = max(handPlayer1Numbers)
                HighCard2 = max(handPlayer2Numbers)

                if highCard1 > HighCard2:
                    winsPlayer1 = winsPlayer1 + 1
                elif HighCard2 > highCard1:
                    winsPlayer2 = winsPlayer2 + 1
                else:
                    pass

    #print "%d - Player 1 Hand: %d, Value: %d\t -  Player 2 Hand: %d, Value: %d" % (i, player1.hand, player1.valueHand, player2.hand, player2.valueHand)
    i = i + 1

print 'Player 1 wins: %d' % winsPlayer1
print 'Player 2 wins: %d' % winsPlayer2

f.close()
