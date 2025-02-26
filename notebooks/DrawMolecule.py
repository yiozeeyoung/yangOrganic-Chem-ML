from rdkit import Chem
from rdkit.Chem import Draw
import os

m = Chem.MolFromSmiles('Cc1ccccc1')
img = Draw.MolToImage(m)

# 指定保存路径
# 例如，保存到 "D:/MLearing/ogchem/yangOrganic-Chem-ML/results"
save_path = "D:/MLearing/ogchem/yangOrganic-Chem-ML/results/molecule.png"


# 保存图片
img.save(save_path)

print(f"image saved to：{save_path}")