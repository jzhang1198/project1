# DNA -> RNA Transcription


def transcribe(seq: str) -> str:
    rna = ''
    for base in seq:
        if base == 'T':
            rna += 'U'
        else:
            rna += base
    return rna


def reverse_transcribe(seq: str) -> str:
    dna = ''
    for base in seq:
        if base == 'U':
            dna += 'T'
        else:
            dna += base
    return dna
