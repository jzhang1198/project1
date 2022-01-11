# write tests for transcribes

from seqparser import (
        transcribe,
        reverse_transcribe)


def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    testcase1 = 'ACTGAACCC' #some testcases
    testcase2 = 'ATGCATGCA' 
    out1 = 'UGACUUGGG' #the expected output of said testcases
    out2 = 'UACGUACGU'
    
    assert transcribe(testcase1) == out1
    assert transcribe(testcase2) == out2


def test_reverse_transcribe():
    testcase1 = 'ACTGAACCC' #some testcases
    testcase2 = 'ATGCATGCA' 
    out1 = 'GGGUUCAGU' #the expected output of said testcases
    out2 = 'UGCAUGCAU'
    
    assert reverse_transcribe(testcase1) == out1
    assert reverse_transcribe(testcase2) == out2
