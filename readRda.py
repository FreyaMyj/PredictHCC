import rdata
import numpy as np
import pandas as pd

clinical = rdata.read_rda("Dataset/TCGA-LIHC/lihc_clinical.rda")
clinical = clinical['clinical']
df = pd.DataFrame.from_dict(clinical)
df.to_csv("Dataset/TCGA-LIHC/lihc_clinical.csv", index=False)

mutation = rdata.read_rda("Dataset/TCGA-LIHC/lihc_maf.rda")
mutation = mutation['maf']
df = pd.DataFrame.from_dict(mutation)
df.to_csv("Dataset/TCGA-LIHC/lihc_maf.csv", index=False)

exp = rdata.read_rda("Dataset/TCGA-LIHC/lihc_exp.rda")
