import librosa
import jupyter
import numpy
import time
import os
import warnings
from multiprocessing import Pool
warnings.filterwarnings('ignore')
#cd C:\Users\klise\Downloads\vox2_test_aac (1)\test
def getmfcc(path):
    y,sr=librosa.core.load(path)
    mfcc=numpy.empty(0)
    mfcc=librosa.feature.mfcc(y,sr)
    numpy.save(path[:-4],mfcc)
sp=[]                
t=time.time()
fn=os.getcwd()
res=fn+'res'
os.mkdir(res)
for f1 in os.listdir(fn):
    os.mkdir(res+"\\"+f1)
    for f2 in os.listdir(fn+"\\"+f1):
        os.mkdir(res+"\\"+f1+"\\"+f2)
        for el in os.listdir(fn+"\\"+f1+"\\"+f2):
            sp.append(fn+"\\"+f1+"\\"+f2+"\\"+el)   
with Pool() as executor:
    executor.map(getmfcc,sp)        
        
print(time.time()-t)



