# -*- coding: utf8 -*-

from Board import *
from GameAI import *
from MonteCarlo import *

import time

def main():
    state = Board(3, 3)
    markList = [X_MARK, O_MARK]
    turn = 0
    maxPlayer = True

    monteCarlo = MonteCarlo(time=3)

    #state.setMark(X_MARK, (2, 2))
    #state.setMark(O_MARK, (2, 0))
    #turn += 1
    #maxPlayer = False

    human = input()

    while True:

        state.showBoard()

        if state.isWin() or state.isFull():
            break

        nowMark = markList[turn]

        if turn == human:
            y, x = map(int, raw_input().split())

            state.setMark(nowMark, (y, x))
        else:
            start = time.time()

            if nowMark == X_MARK:
                info = monteCarlo.get_play(state, nowMark)
                pass
            else:
                info = minimax(state, 9, maxPlayer, True)
                pass

            #info = minimax(state, 9, maxPlayer, True)
            #info = alphabeta(state, 9, -INFINITE, INFINITE, maxPlayer, True)
            #info = monteCarlo.get_play(state, nowMark)

            gap = time.time() - start

            state.setMark(nowMark, info[1])

            print "Info:", info
            print "Gap :", gap

        print

        turn = (turn + 1) % 2
        maxPlayer = not maxPlayer


    print "Win:", state.isWin()


if __name__ == "__main__":
    main()
