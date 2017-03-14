# -*- coding: utf8 -*-

import copy
import random
import time

EMPTY  = '-'
X_MARK = 'X'
O_MARK = 'O'


class BoardState:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = self.makeBoard(width, height)
        self.lastPosition = None
        self.WIN_COUNT = 3
        self.directionPairList = [[(-1, 0), ( 1,  0)],
                                  [(-1, 1), ( 1, -1)],
                                  [( 0, 1), ( 0, -1)],
                                  [( 1, 1), (-1, -1)]]

    def getBoard(self):
        return self.board

    def makeBoard(self, width, height):
        board = []

        for i in range(height):
            board.append([EMPTY] * width)

        return board

    def getPossiblePositionList(self):
        positionList = []
        
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] == EMPTY:
                    positionList.append((y, x))

        return positionList

    def setMark(self, mark, position):
        y, x = position
        self.board[y][x] = mark
        self.lastPosition = position

    def showBoard(self):
        for row in self.board:
            print ''.join(row)
        print

    def isFull(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] == EMPTY:
                    return False
        return True

    def isWin(self):
        if self.lastPosition == None: return None
        
        y, x = self.lastPosition
        nowMark = self.board[y][x]

        for directionPair in self.directionPairList:
            sameMarkCount = 1
            for direction in directionPair:
                dy, dx = direction
                nowY, nowX = y, x

                while self.isInBoard(nowY + dy, nowX + dx):
                    nowY += dy
                    nowX += dx
                    
                    if self.board[nowY][nowX] == nowMark:
                        sameMarkCount += 1
                    else:
                        break

            if sameMarkCount == self.WIN_COUNT:
                return nowMark

        return None

    def isInBoard(self, y, x):
        return 0 <= y and y < self.height and 0 <= x and x < self.width


def alphabeta(state, depth, alpha, beta, maxPlayer, firstCall=False):
    result = state.isWin()

    if result:
        if result == X_MARK:
            return 1 + depth
        else:
            return -1 - depth
    elif state.isFull() or depth == 0:
        return 0

    if maxPlayer:
        nowMark = X_MARK
    else:
        nowMark = O_MARK

    bestInfo = None
    possiblePositionList = state.getPossiblePositionList()
    random.shuffle(possiblePositionList)

    for position in possiblePositionList:
        copyState = copy.deepcopy(state)
        copyState.setMark(nowMark, position)
        value = alphabeta(copyState, depth - 1, alpha, beta, not maxPlayer)

        if maxPlayer and alpha < value:
            alpha = value
            bestInfo = (alpha, position)

            if beta <= alpha:
                break
        elif not maxPlayer and beta > value:
            beta = value
            bestInfo = (beta, position)

            if beta <= alpha:
                break

    if bestInfo == None:
        bestInfo = (value, position)
        
    if firstCall:
        return bestInfo
    else:
        return bestInfo[0]


def main():
    state = BoardState(3, 3)
    markList = [X_MARK, O_MARK]
    turn = 0
    maxPlayer = True

    #state.setMark(X_MARK, (2, 2))
    #state.setMark(O_MARK, (2, 0))

    human = input()

    while True:

        state.showBoard()

        if state.isWin() or state.isFull():
            break

        if turn == human:
            y, x = map(int, raw_input().split())

            state.setMark(markList[turn], (y, x))
        else:
            start = time.time()
            info = alphabeta(state, 9, -9999, 9999, maxPlayer, True)
            gap = time.time() - start

            state.setMark(markList[turn], info[1])

            print "Info:", info
            print "Gap :", gap

        print

        turn = (turn + 1) % 2
        maxPlayer = not maxPlayer


    print "Win:", state.isWin()


if __name__ == "__main__":
    main()
