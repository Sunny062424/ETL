import pandas as pd
from sqlalchemy import create_engine
import cx_Oracle
import numpy as np
engine = create_engine('oracle://sunny:sunny@localhost:1521/XE')
#sqlq = "select * from TT1"
dataframeName=pd.read_sql_query("select * from TT1", engine)
print(dataframeName)
