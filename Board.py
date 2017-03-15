# -*- coding: utf8 -*-

EMPTY  = '-'
X_MARK = 'X'
O_MARK = 'O'

DRAW = 'draw'

INFINITE = 999999

class Board:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = self.makeBoard(width, height)
        self.lastMark = None
        self.lastPosition = None
        self.WIN_COUNT = 3
        self.directionPairList = [[(-1, 0), ( 1,  0)],
                                  [(-1, 1), ( 1, -1)],
                                  [( 0, 1), ( 0, -1)],
                                  [( 1, 1), (-1, -1)]]

    def makeBoard(self, width, height):
        board = []

        for i in range(height):
            board.append([EMPTY] * width)

        return board

    def getBoard(self):
        return self.board

    def getBoardStr(self):
        return '\n'.join(''.join(row) for row in self.board)

    def getNextPlayer(self):
        if self.lastMark == None or self.lastMark == O_MARK:
            return X_MARK
        else:
            return O_MARK

    def getPossiblePositionList(self, mark=None):
        positionList = []
        
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] == EMPTY:
                    positionList.append((y, x))

        return positionList

    def setMark(self, mark, position):
        y, x = position
        self.board[y][x] = mark
        self.lastMark = mark
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

        if self.isFull():
            return DRAW

        return None

    def isInBoard(self, y, x):
        return 0 <= y and y < self.height and 0 <= x and x < self.width
