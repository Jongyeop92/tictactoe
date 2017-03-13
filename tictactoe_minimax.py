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


def test():
    
    state = BoardState(3, 3)

    assert state.getBoard() == [[EMPTY, EMPTY, EMPTY],
                                [EMPTY, EMPTY, EMPTY],
                                [EMPTY, EMPTY, EMPTY]]
    
    assert state.getPossiblePositionList() == [(0, 0), (0, 1), (0, 2),
                                               (1, 0), (1, 1), (1, 2),
                                               (2, 0), (2, 1), (2, 2)]

    assert state.isWin() == None

    state.setMark(X_MARK, (0, 0))

    assert state.getBoard() == [[X_MARK, EMPTY, EMPTY],
                                [ EMPTY, EMPTY, EMPTY],
                                [ EMPTY, EMPTY, EMPTY]]

    assert state.getPossiblePositionList() == [        (0, 1), (0, 2),
                                               (1, 0), (1, 1), (1, 2),
                                               (2, 0), (2, 1), (2, 2)]

    #state.showBoard()
    

    state.setMark(O_MARK, (2, 1))

    assert state.getBoard() == [[X_MARK,  EMPTY, EMPTY],
                                [ EMPTY,  EMPTY, EMPTY],
                                [ EMPTY, O_MARK, EMPTY]]

    assert state.getPossiblePositionList() == [        (0, 1), (0, 2),
                                               (1, 0), (1, 1), (1, 2),
                                               (2, 0),         (2, 2)]

    #state.showBoard()

    assert state.isFull() == False

    for y in range(3):
        for x in range(3):
            state.setMark(X_MARK, (y, x))

    assert state.isFull() == True
    assert state.getPossiblePositionList() == []
    assert state.isWin() == X_MARK


    assert state.isInBoard(0, 0) ==  True
    assert state.isInBoard(2, 2) ==  True
    assert state.isInBoard(3, 3) == False

    newState = copy.deepcopy(state)
    assert id(state) != id(newState)
    assert id(state.getBoard()) != id(newState.getBoard())
    

    print "Success on company"


def minimax(state, depth, maxPlayer, firstCall=False):
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

    bestInfoList = []
    possiblePositionList = state.getPossiblePositionList()

    for position in possiblePositionList:
        copyState = copy.deepcopy(state)
        copyState.setMark(nowMark, position)
        value = minimax(copyState, depth - 1, not maxPlayer)

        if bestInfoList == []:
            bestInfoList = [(value, position)]
        else:
            bestValue = bestInfoList[0][0]

            if value == bestValue:
                bestInfoList.append((value, position))
            elif (maxPlayer and value > bestValue) or (not maxPlayer and value < bestValue):
                bestInfoList = [(value, position)]

    if firstCall:
        print "bestInfoList:", bestInfoList
        return random.choice(bestInfoList)
    else:
        return bestInfoList[0][0]
    

def main():
    state = BoardState(3, 3)
    markList = [X_MARK, O_MARK]
    turn = 0
    maxPlayer = True

    state.setMark(X_MARK, (2, 2))
    state.setMark(O_MARK, (2, 0))
    #turn += 1
    #maxPlayer = False

    while True:

        if state.isWin() or state.isFull():
            break

        start = time.time()
        info = minimax(state, 9, maxPlayer, True)
        gap = time.time() - start

        state.setMark(markList[turn], info[1])

        print
        state.showBoard()

        print "Info:", info
        print "Gap :", gap
        print
        print

        turn = (turn + 1) % 2
        maxPlayer = not maxPlayer


    print "Win:", state.isWin()


if __name__ == "__main__":
    #test()
    main()
