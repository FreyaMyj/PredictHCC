import rdata
import numpy as np
import pandas as pd

from tools.readRda import ReadRda

clinical_file = 'Dataset/TCGA-LIHC/lihc_clinical.rda'
clinical_para = 'clinical'
clinical_csv = 'Dataset/TCGA-LIHC/lihc_clinical.csv'

clinical = ReadRda(clinical_file, clinical_para, clinical_csv)
# clinical.to_csv()
clinical_df = clinical.read()

maf_file = 'Dataset/TCGA-LIHC/lihc_maf.rda'
maf_para = 'mutation'
maf_csv = 'Dataset/TCGA-LIHC/lihc_maf.csv'

maf = ReadRda(maf_file, maf_para, maf_csv)
# maf.to_csv()
maf_df = maf.read()
