#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scipy import sparse
from scipy import linalg
from scipy import matrix
from scipy.sparse.linalg.eigen.arpack import *

import math
import sys
import pickle
import re

numEig = 120
# maxWordID = 33852
# maxDocID = 304887

uMat = pickle.load(open("uMat.p"))
uMatT = pickle.load(open("uMatT.p"))
sigMat = pickle.load(open("sigMat.p"))
wordIDToWord = pickle.load(open("wordIDToWord.p"))
wordToWordID = pickle.load(open("wordToWordID.p"))

maxWordID = len(wordIDToWord)

# print "load finished"

# print "matrix construction finished"

for coID in range(maxWordID):

    targetWord = wordIDToWord[coID]

    # if re.search("^[a-zA-Z!?-]*$", targetWord):
    #    continue
    
    outString = targetWord
    for j in range(numEig):
        u = uMat[coID, j]
        sig = sigMat[j, j]
        sigInv = 1.0 / sig

        val = u * sigInv
        element = "ev" + str(j) + "\t" + str(val)

        outString = outString + "\t" + element
        
    print outString
