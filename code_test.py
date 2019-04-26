# Staging area to test pieces of code


def alignment_check():

    alignmentList = ['LG - Lawful Good',
                     'NG - Neutral Good',
                     'CG - Chaotic Good',
                     'LN - Lawful Neutral',
                     'TN - True Neutral',
                     'CN - Chaotic Neutral',
                     'LE - Lawful Evil',
                     'NE - Neutral Evil',
                     'CE - Chaotic Evil',
                     ]

    for l in alignmentList:
        print(l)
    alignment = input('Enter character alignment: ')

    for a in alignmentList:
        if (alignment[:2].upper() or alignment[5:].title()) in (a[:2] or a[5:]):
            return a[5:].title()
    if alignment not in alignmentList:
        print('\nPlease select from this list:')
        return alignment_check()


alignments = alignment_check()
print(alignments)
