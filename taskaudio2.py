import librosa
import jupyter
import numpy
import time
import os
import warnings
from concurrent.futures import ThreadPoolExecutor
warnings.filterwarnings('ignore')
#cd C:\Users\klise\Downloads\vox2_test_aac (1)\test
def getmfcc(path,dr):
    y,sr=librosa.core.load(path)
    mfcc=numpy.empty(0)
    mfcc=librosa.feature.mfcc(y,sr)
    numpy.save(dr,mfcc)
                
t=time.time()
fn=os.getcwd()
res=fn+'res'
os.mkdir(res)
for f1 in os.listdir(fn):
    os.mkdir(res+"\\"+f1)
    for f2 in os.listdir(fn+"\\"+f1):
        os.mkdir(res+"\\"+f1+"\\"+f2)
        with ThreadPoolExecutor(max_workers=4) as pool:
            for el in os.listdir(fn+"\\"+f1+"\\"+f2):
                pool.submit(getmfcc,fn+"\\"+f1+"\\"+f2+"\\"+el,res+"\\"+f1+"\\"+f2+"\\"+el[:-4])
                        
print(time.time()-t)




