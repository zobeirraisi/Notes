import os
from natsort import natsorted
ROOT='img'
FList = natsorted(os.listdir(ROOT))
# print(FList)
# FListC = FList[1:]
# print(FListC)


m = 10001
for i in FList:
    m=str(m).zfill(5)
    fileExtension = os.path.splitext(i)[1]
    os.rename(os.path.join(ROOT,i),os.path.join(ROOT,str(m)+fileExtension))

    m = int(m)+1
print('done')
