# -*- coding: utf8 -*-

EMPTY  = '-'
X_MARK = 'X'
O_MARK = 'O'

INFINITE = 999999

class Board:

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
