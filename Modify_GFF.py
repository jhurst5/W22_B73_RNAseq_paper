import pandas as pd
import sys


def len_from_cigar(x):
    CIGAR = [char for char in x]
    rolling_len = 0
    BP = []
    for item in CIGAR:
        if item.isalpha() == False:
            BP.append(item)
        elif item == 'M' or item == 'D':
            rolling_len += int(''.join(BP))
            BP = []
        elif item == "I":
            rolling_len += 0
            BP = []
        else:
            raise NameError('<<<Unknown CIGAR char>>>')
    return rolling_len


gff = pd.read_csv(sys.argv[1], sep='\t', comment='#', header=None)
gff = gff[gff[2] == 'gene']

zeins = pd.read_csv(sys.argv[2], sep='\t')
zeins['LEN'] = zeins['CIGAR'].apply(lambda x: len_from_cigar(x))
zeins['STOP'] = zeins.apply(lambda x: x['START'] + x['LEN'], axis=1)


excluded_row_list = []
included_row_list = []
for index, row in zeins.iterrows():

    start = row['START']
    stop = row['STOP']
    chrom = row['CHROM']
    gene = row['GENE']
    print(gff.head())
    current_gff = gff[gff[0] == chrom]

    zein_range = [a for a in range(start, stop+1)]

    for i, r in current_gff.iterrows():

        g_start = r[3]
        g_stop = r[4]

        feature_range = [q for q in range(g_start, g_stop+1)]

        overlap = set(zein_range).intersection(set(feature_range))

        if len(overlap) == 0:
            included_row_list.append(r)

        if len(overlap) > 0:
            excluded_row_list.append(r)
            gff.drop(i, inplace=True)


excluded_df = pd.DataFrame(excluded_row_list)
included_df = pd.DataFrame(included_row_list)


print(excluded_df.shape)
print(included_df.shape)
print(gff.shape)


gff.to_csv(sys.argv[3], sep='\t', index=False)
excluded_df.to_csv(sys.argv[4], sep='\t', index=False)

