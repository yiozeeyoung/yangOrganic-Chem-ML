from rdkit import Chem
from rdkit.Chem import Descriptors

smiles = "CCO"
mol = Chem.MolFromSmiles(smiles)
logp = Descriptors.MolLogP(mol)
print(f"LogP: {logp}")