import sys

Pattern = "GTGCCG"
Text = "AGCGTGCCGAAATATGCCGCCAGACCTGCTGCGGTGGCCTCGCCGACTTCACGGATGCCAAGTGCATAGAGGAAGCGAGCAAAGGTGGTTTCTTTCGCTTTATCCAGCGCGTTAACCACGTTCTGTGCCGACTTT"
d = 3

def ApproximatePatternCount(Pattern, Text, d):
    return len([i for i in range(0, len(Text) - len(Pattern) + 1) if HammingDistance(Text[i:i + len(Pattern)], Pattern) <= d])

def HammingDistance(p,q):
    return sum(i!=j for i,j in zip(p,q))

lines = sys.stdin.read().splitlines()
print(ApproximatePatternCount(lines[0],lines[1],int(lines[2])))
