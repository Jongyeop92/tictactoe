# -*- coding: utf8 -*-

from Board import *

import copy
import random

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
