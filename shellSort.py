# -*- coding: cp936 -*-

#!/usr/bin/env python

#@Kang
#test 2

'''Shell Sort'''

def insert_sort(key, data):
    '''Insert sort algorithm'''
    
    for i in range(1, len(key)):
        temp = key[i]    #data[i] is to insert
        temp_data = data[i]
        j = i - 1
        while j >= 0 and temp < key[j]:
            key[j + 1] = key[j]
            data[j + 1] = data[j]
            j = j - 1
        if j != i - 1:
            key[j + 1] = temp     #insert temp
            data[j + 1] = temp_data

def shell_sort(key, data, n = None):
    '''Shell sort algorithm'''
    
    if n == None:
        n = len(key) / 2
        if n % 2 == 0:
            n = n + 1
    n=int(n)
    for i in range(0, n):
        newkey = key[i:len(key):n]
        newdata = data[i:len(key):n]
        insert_sort(newkey, newdata)
        key[i:len(key):n] = newkey
        data[i:len(key):n] = newdata
    if n != 1:
        d = n / 2
        if d % 2 == 0:
            d = d + 1
        shell_sort(key, data, d)
        
citylist= ["harbin","qqhr", "daqing","mudanjiang", "jixi", "jiamusi", "hegang", "shuangyashan","yichun","suihua"]
for cityCount in range(len(citylist)):
    for fileCount in range(7,8):
        filename1="D:\yihong\Data_Geosoft\DataSet\ActivitySpace\\alldays\with_id\\" +citylist[cityCount] + "alldays_ActSpaceID.txt"
        filename2="D:\yihong\Data_Geosoft\DataSet\ActivitySpace\\alldays\with_id\\AgeSorted\\" +citylist[cityCount] + "alldays_ActSpaceAgeSorted.txt"
        infile=open(filename1,'r')
        outfile=open(filename2,'w')
        lines=infile.readlines()
        infile.close()
    
        flag=len(lines)-2
        lines=[]
    #flag=12751930-2
    
        key=[0 for col in range(flag)]
        data=[0 for col in range(flag)] 
    
    #import data and get the key
        infile=open(filename1,'r')
        line=infile.readline()
        for i in range(flag):
            line=infile.readline()
            data[i]=line
            key[i]=int(line.split('\t')[0])
             
 
        shell_sort(key,data)
        print 2

        for i in range(flag):
            outfile.write(data[i])
            print i   
        infile.close()
        outfile.close()
                       


print('***  End  ***')
