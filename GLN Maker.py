#!/usr/bin/env python
# coding: utf-8
# code to create Global Location Numbers including check digit using
# a GS1 Company Prefix and internal identifier
# GLNs are 13-digit location identifiers used with GS1 Standards

def GLNMaker(prefix, internalID):
    if len(str(prefix)) + len(str(internalID)) == 12:
        GLN = str(prefix) + str(internalID)
        checksum = 0
        index = 1
        for i in GLN:
            if index%2 == 0:
                checksum = checksum + int(i)*3
            else:
                checksum = checksum + int(i)
            index += 1
        checkdigit = 10 - int(str(checksum)[-1:])
        if checkdigit == 10:
            checkdigit = 0
        GLN = GLN + str(checkdigit)
        return(GLN)
    else:
        pass




#example
locations = [1414,3576,3922,4139,3760,4100,4232,4163,4326,4281,4045]
for i in range(len(restaurants)):
    print(GLNMaker("01234568", restaurants[i]))
    




