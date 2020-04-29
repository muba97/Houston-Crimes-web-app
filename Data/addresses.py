import pandas as pd
import csv
import matplotlib.pyplot as plt


def main():
    csvfiles = ['jan17.csv','feb17.csv','mar17.csv','apr17.csv','may17.csv','jun17.csv','jul17.csv','aug17.csv','sep17.csv','oct17.csv','nov17.csv','dec17.csv']
    months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    for i in range(len(csvfiles)):
        addresses(csvfiles[i],months[i], i)


def Premises(months, data):
    storage = []
    temp = 0
    for i in data.index:
        Block = (str(data['BlockRange'][i]))[:4]
        street = str(data['StreetName'][i])
        Type = str(data['Type'][i])

        if('UNK' in Block or 'Unkown' in street):
            temp += 1
        elif('-' in Type):
            storage.append (Block + ' ' + street + ' ' + 'Houston TX')
    
        else:
            storage.append (Block + ' ' + street + ' ' + Type + ' ' + 'Houston TX')
    
    df = pd.DataFrame(storage, columns= ['Address'])
        
    df.to_csv(r'./address/{}'.format(months), index = False, header= True)
    print(temp)



def addresses(filename,months, i):
    
    currentFile = pd.read_csv('./csvfiles/{}'.format(filename))
    dframe = pd.DataFrame(currentFile)
    Premises(months, dframe)      

if __name__ == '__main__': main()