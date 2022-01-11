# DNA -> RNA Transcription


def transcribe(seq: str) -> str:
    rna = '' #create the empty string to become the transcribed sequence
    bp = {'A' : 'U', #create a dictionary defining base pair combinations
          'T' : 'A',
          'C' : 'G',
          'G' : 'C'}
    
    for base in seq: #iterate through bases in input sequence and append complimentary bases to rna
        rna += bp[base] 
    return rna


def reverse_transcribe(seq: str) -> str:
    rna = '' #create the empty string to become the reverse transcribed sequence
    bp = {'A' : 'U', #create a dictionary defining base pair combinations
          'T' : 'A',
          'C' : 'G',
          'G' : 'C'}
    for base in seq: #iterate through the bases in the input sequence and append complimentary bases to dna
        rna += bp[base]
    return rna[::-1] #output dna in reverse order

