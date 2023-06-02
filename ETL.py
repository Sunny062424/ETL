import os
import pandas as pd
from sqlalchemy import create_engine,types

#특정 파일 경로(path)에 있는 문서 확인하기
path = "./dataset2/"
file_list = os.listdir(path)
print ("file_list: {}".format(file_list))

dataName=[]#데이터 원본이름 저장 배열
dataName.append(file_list)
dataFrameList=[] #for문으로 데이터프레임화 한 데이터들을 저장할 배열


for i in range(len(file_list)):
    try:
        if file_list[i].split(".")[1]=='csv':
            datas=pd.read_csv(path+'{}'.format(file_list[i]), encoding = 'utf-8')
    
        elif file_list[i].split(".")[1]=='xlsx':
            datas=pd.read_excel(path+'{}'.format(file_list[i]), engine='openpyxl')
        dataFrameList.append(datas)
    except Exception as e:
        print("error")
        
# DB 접속 정보        
id = "sunny"
pw = "sunny"
ip = "localhost"
port = "1521"
dbName = "xe" 
# DB 커넥션 열기
engine_orcl = create_engine('oracle+cx_oracle://{}:{}@{}:{}/{}'.format(id,pw,ip,port,dbName)    ) 

for i in range(len(dataFrameList)):
    tableName = dataName[0][i].split(".")[0].lower()+ "_sy"
    dataInsert = dataFrameList[i]

    objectColumns = list(dataInsert.columns[dataInsert.dtypes == 'object'])
    typeDict={}
    maxLen = 100

for i in range(0, len(objectColumns)):
    # dataFrameList[i].str.len().max() 최대치 사용할 경우
    typeDict[ objectColumns[i] ] = types.VARCHAR(100)

dataInsert.to_sql(name=tableName, if_exists="replace", dtype=typeDict, con=engine_orcl, index=False)
