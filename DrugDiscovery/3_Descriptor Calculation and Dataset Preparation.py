import pandas as pd

df = pd.read_csv('acetylcholinesterase_04_bioactivity_data_class_pIC50.csv')
df

selection = ['canonical_smiles','molecule_chembl_id']
df_selection = df[selection]
df_selection.to_csv('molecule.smi', sep='\t', index=False, header=False)


#wget https://github.com/dataprofessor/bioinformatics/raw/master/padel.zip
#wget https://github.com/dataprofessor/bioinformatics/raw/master/padel.sh
#unzip padel.zip

#cat molecule.smi | head -5
#cat molecule.smi | wc -l

#cat padel.sh
#bash padel.sh
#ls -l


df_X = pd.read_csv('descriptors_output.csv')
df_X
df_X = df_X.drop(columns=['Name'])
df_X

df_Y = df['pIC50']
df_Y


dataset = pd.concat([df_X,df_Y], axis=1)
dataset

dataset.to_csv('acetylcholinesterase_06_bioactivity_data_class_pIC50_pubchem_fp.csv', index=False)
