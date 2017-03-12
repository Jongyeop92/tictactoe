EMPTY  = '-'
X_MARK = 'X'
O_MARK = 'O'
class BoardState:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = self.makeBoard(width, height)

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

    def showBoard(self):
        for row in self.board:
            print ''.join(row)
        print


def test():
    
    state = BoardState(3, 3)

    assert state.getBoard() == [[EMPTY, EMPTY, EMPTY],
                                [EMPTY, EMPTY, EMPTY],
                                [EMPTY, EMPTY, EMPTY]]

    assert state.getPossiblePositionList() == [(0, 0), (0, 1), (0, 2),
                                               (1, 0), (1, 1), (1, 2),
                                               (2, 0), (2, 1), (2, 2)]

    state.setMark(X_MARK, (0, 0))

    assert state.getPossiblePositionList() == [        (0, 1), (0, 2),
                                               (1, 0), (1, 1), (1, 2),
                                               (2, 0), (2, 1), (2, 2)]

    state.showBoard()
    

    state.setMark(O_MARK, (2, 1))

    assert state.getPossiblePositionList() == [        (0, 1), (0, 2),
                                               (1, 0), (1, 1), (1, 2),
                                               (2, 0),         (2, 2)]

    state.showBoard()

    print "Success"

if __name__ == "__main__":
    test()
