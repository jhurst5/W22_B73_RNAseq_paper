from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import sys
from random import randint


output_directory = sys.argv[2]

reference = SeqIO.to_dict(SeqIO.parse(sys.argv[1], 'fasta'))
gene_list = list(SeqIO.index(sys.argv[1], 'fasta'))


def get_random_seq(gene):

    read_list = []
    limit = len(reference[gene].seq)

    for i in range(0,10000):
        start = randint(0,limit-300)
        end = start+300

        fake_read = reference[gene].seq[start:end]
        record = SeqRecord(fake_read, 'read_%i' % (i+1), '', '')
        read_list.append(record)

    SeqIO.write(read_list, output_directory + gene + '.fasta', 'fasta')


get_random_seq(sys.argv[3])
