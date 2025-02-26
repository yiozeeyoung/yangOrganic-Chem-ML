from rdkit.Chem import Descriptors
descriptor_list = [x[0] for x in Descriptors.descList]
print(len(descriptor_list))  # 输出描述符总数
print(descriptor_list)       # 输出所有描述符名称