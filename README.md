# W22_B73_RNAseq_paper



------------------------
Make_Simulated_FASTQ.py
------------------------

This script was used to produce simulated FASTQs for the simulation anlysis.
It makes a FASTQ of random fragments from a gene model, in order to test alignment reliability.

Argument 1 is a set of set gene models to simulate reads for.

Argument 2 is the directory to store the output FASTQ's in.

Argument 3 is the specific gene model from Argument 1 to fragment.



--------------
Modify_GFF.py
--------------

This script was used to add the previously annotated zein gene copies to the GFF of published references.
It adds the zein copy, while removing any gene model that might overlap.

Argument 1 is the GFF of the desired reference.

Argument 2 is the SAM file of the new gene models aligned to the reference.

Argument 3 is the where to output the new modified GFF.

Argument 4 is the where to output the gene models which were removed from the original GFF.



------------------------------------
Library_size_by_expression_corr.tsv
------------------------------------

This file contains Pearson R^2 and p-values for zein expression by library size in the NAM expression data.


------------
metrics.csv
------------

This file contains basic quality control information on the RNAseq libraries used in the study.

---------------------------------------------
Read_Alignment_and_Quatification_Commands.txt
---------------------------------------------

This file contains the commands used for HISAT2, StringTie2, and DESeq2.

