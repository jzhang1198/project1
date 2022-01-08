# DNA -> RNA Transcription


def transcribe(seq: str) -> str:
    rna = ''
    bp = {'A' : 'U',
          'T' : 'A',
          'C' : 'G',
          'G' : 'C'}
    
    for base in seq:
        rna += bp[base]
    return rna


def reverse_transcribe(seq: str) -> str:
    dna = ''
    bp = {'U' : 'A',
          'A' : 'T',
          'C' : 'G',
          'G' : 'C'}
    for base in seq:
        dna += bp[base]
    return dna

