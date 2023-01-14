#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        tuple_ = (0, None)
    else:
        tuble_ = (len(sentence), sentence[:1])
    return(tuble_)
