import csv
f=open(filen,'wb')
url=dp1['url'][0]
#Calling the feature extraction function
ret_dict=feature_extract(url)
#print ret_dict



#processing URL's
w = csv.DictWriter(f, ret_dict.keys())
w.writeheader()
w.writerow(ret_dict)
def process_URL_list(dataframe):
    for i in range(1,len(dp1)):
        url=dp1['url'][i]
        bool=dp1['label'][i]
        if url!='':
            print 'working on: '+url           
            ret_dict=feature_extract(url)
            w.writerow(ret_dict)


#This part is user pc based and is soleley depend on your python skill to modify it your personel use.
            
"""
basepath="C:\Users\SHUBHAM\Desktop\Minor\data"
filename="featurenow.csv"
f2=os.path.join(basepath,filename)
base="C:\Users\SHUBHAM\Desktop\Minor\data"
fl="new3.csv"
filen=os.path.join(base,fl)
f=open(f2,'wb')
datf=pd.read_csv(filen)
url=datf['url'][0]
ret_dict=feature_extract(url)
ret_dict['malicious']=1
#print ret_dict
w = csv.DictWriter(f, ret_dict.keys())
w.writeheader()
w.writerow(ret_dict)
"""
for i in range(len(datf)):
    if datf['url'][i]!='':
        bools=datf['label'][i]
        retdict=feature_extract(datf['url'][i])
        if bools==1:
            retdict['malicious']=1
        elif bools==0:
            retdict['malicious']=0
        w.writerow(retdict)
