# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser
    class here. You should generate an instance of
    your FastaParser class and assert that it properly
    reads in the example Fasta File.
    """
    head0 = '>seq0' #define headers and sequences for the first and last two sequences in test.fa
    seq0 = 'TGATTGAATCTTTTGAGGGTCACGGCCCGGAAGCCAGAATTTCGGGGTCCTCTGTGGATATTAATCGAGCCCACACGGTGTGAGTTCAGCGGCCCCCGCA'
    head1 = '>seq1'
    seq1 = 'TCCGCCCGCTGTGCTGACGAGACTAGCAGGGAAATAAATAGAGGGTTTAGTTATACTCAGTAGGCAGTTCGATGGCTTATATCTAACTTCTTATTCCGAT'
    head98 = '>seq98'
    seq98 = 'CGAGCGAGAAACGCGCTAACTAGCAACCGGAACAACAATGCTGGGTTGAATTTGATTCGCACCCGACGATCACTAGAGAGTTTATCTGGGACTCCGGGAC'
    head99 = '>seq99'
    seq99 = 'CAAACCGGCGATGCGGGTACTCCCTACAAGTTGGACTCCGCAGCGAACGCCGCAGGGGCCATTATACGGCGGTCTTGGCGGCGTCGACCAGGCCGGTCCA'
    
    fasta = '../project1/data/test.fa'
    out = FastaParser(fasta)
    out_list = [tup for tup in out] #convert output into a list of tuples
    
    assert out_list[0] == (head0,seq0) #check that the headers and sequences are equivalent
    assert out_list[1] == (head1,seq1)
    assert out_list[98] == (head98,seq98)
    assert out_list[99] == (head99,seq99)
        

def test_FastqParser():
    """
    Write your unit test for your FastqParser
    class here. You should generate an instance of
    your FastqParser class and assert that it properly
    reads in the example Fastq File.
    """
    
    head0 = '@seq0' #define headers and sequences for the first and last two sequences in test.fq
    seq0 = 'TGTGGTCGTATAGTTATTGTCATAAATTACACAGAATCGCGATTCTCCGCGTCCACCAATCTTAGTGCACCACAGCATCGACCCGATTTATGACGCTGAG'
    qual0 = '''*540($=*,=.062565,2>'487')!:&&6=,6,*7>:&132&83*8(58&59>'8!;28<94,0*;*.94**:9+7"94(>7='(!5"2/!%"4#32='''
    head1 = '@seq1'
    seq1 = 'CCCCGGACGACTGATCCCGATAGAGCTCACTCTTCGAGGCAAGCAGACCCATATCGTCCTGCTGGCAACGCTATCCGGGTGCGAGTAAATCGAAACCTCG'
    qual1 = ''''(<#/0$5&!$+,:=%7=50--1;'(-7;0>=$(05*9,,:%0!<),%646<8#%"."-'*-0:.+*&$5!'8)(%3*+9/&/%=363*,6$20($97,"'''
    head98 = '@seq98'
    seq98 = 'AACCTGCCCGTAGCCTTTAGGTAGCCCGTCTACATGTCCTCCAGTACAGTGGAAGCTCCTACATCAACTGATCAAATAACATCGCAGCACTATATGTCAC'
    qual98 = '''39$$8'':7:0;0%/7$89-<3',:)1"0'=2'!#5><>+6/=99#>8-$76(6$2'+=;$-))753#99,=+4+1=:5.08*$*:4=,>)/)':8,<48'''
    head99 = '@seq99'
    seq99 = 'CCGAGTTTTGTAGTGGGCTCAACTGAAATCCTATTCTTAGACGATTGGTCATAAAACCCTTTCACTGTACGGACGTAGACCCTGCTCCGTCTTCCAGCAG'
    qual99 = '''2$7)*5:"=+++!:.=>!5>79)8!566$!3*/4$=4.%=//;900$9)!%)4%$=0":02"0=!0#/>+*1$1$39!.8+9<'1$*1$321&<'&9,)2'''
    
    fastq = '../project1/data/test.fq'
    out = FastqParser(fastq)
    out_list = [tup for tup in out] #convert output into a list of tuples

    assert out_list[0] == (head0,seq0,qual0) #check that the headers, sequences, and qualities are equivalent
    assert out_list[1] == (head1,seq1,qual1)
    assert out_list[98] == (head98,seq98,qual98)
    assert out_list[99] == (head99,seq99,qual99)

