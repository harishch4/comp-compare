import os
from platform import processor
import pandas as pd
import json
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, FLOAT

processorEngine = create_engine('sqlite:///processor.db', echo = True)
processorMeta = MetaData()
processor = Table(
    'processors', processorMeta, 
    Column('id', Integer, primary_key = True), 
    Column('processorName', String), 
    Column('mdComputers', FLOAT), 
    Column('pcShop', FLOAT), 
    Column('tinkPC', FLOAT), 
    Column('vedant', FLOAT), 
    Column('tpsTech', FLOAT), 
)

def dumpProcessors():
    processorMeta.create_all(processorEngine)
    root_path = os.environ['CUSTOMPC_HOME']
    filepath = root_path + "/jsonFiles/final_processors.json"
    print(filepath)
    with open(filepath) as f:
        data = json.load(f)
        conn = processorEngine.connect()
        for key in data.keys():
            prices=[]
            for value in data[key]:
                prices.append(value)
            ins = processor.insert().values(processorName=key,mdComputers=prices[0],pcShop=prices[1],tinkPC=prices[2],vedant=prices[3],tpsTech=prices[4])
            try:
                result = conn.execute(ins)
                print("Done : "+ key)
            except Exception as e: print(e)


# dumpProcessors()