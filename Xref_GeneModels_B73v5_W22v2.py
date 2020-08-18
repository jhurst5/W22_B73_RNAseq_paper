import sys
import pandas as pd


xref = pd.read_csv(sys.argv[1], sep='\t')
xref = xref[['B73(Zm00001d.2)', 'W22(Zm00004b.1)', 'v4_gene_model', 'v3_gene_model', 'v2_gene_model', 'v1_gene_model']]


v4 = pd.read_csv(sys.argv[2], sep='\t')


d45 = {i[0].split(':')[1]: i[1].split(':')[1] for i in zip(v4['V4'], v4['V5'])}


def translate(x):
    if x in d45.keys():
        return d45[x]
    else:
        return 'NA'


xref['V5_from_d2'] = xref['B73(Zm00001d.2)'].apply(lambda x: translate(x))
xref['V5_from_d1'] = xref['v4_gene_model'].apply(lambda x: translate(x))


def match_check(x, y):
    if x == 'NA' and y == 'NA':
        return 'NA'
    elif x == 'NA':
        return y
    elif y == 'NA':
        return x
    elif x == y:
        return x
    elif x != y:
        return x + ',' + y
    else:
        return 'check'


xref['match'] = xref.apply(lambda x: match_check(x['V5_from_d2'], x['V5_from_d1']), axis=1)


xref.to_csv(sys.argv[3], sep='\t', index=False)
