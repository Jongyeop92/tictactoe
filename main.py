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

    #state.setMark(X_MARK, (2, 2))
    #state.setMark(O_MARK, (2, 0))
    #turn += 1
    #maxPlayer = False

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

            #info = minimax(state, 9, maxPlayer, True)
            info = alphabeta(state, 9, -INFINITE, INFINITE, maxPlayer, True)

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
