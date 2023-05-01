import numpy as np
import sqlite3 as sql
import pandas as pd
from argparse import ArgumentParser

class DataHantering:
    
    def __init__(self, csv_path:str,db_path:str, name:str): #constructor
        self.df = pd.read_csv(csv_path)
        self.db = sql.connect(db_path)
        self.name = name
        self.cur = self.db.cursor()

    def seperate_col(self, columnName, seperator): #seperate (vaccines) function
        self.columnName = columnName
        self.seperator = seperator
        split = self.df[self.columnName].str.split(self.seperator, expand = True)
        self.df = self.df.join(split)
        del self.df[self.columnName]
        
    def create_database(self): #creates database
        try: #checks if database already exists
            self.df.to_sql(self.name, self.db)
        except Exception:
            pass
    
    def fillNA(self):   # replace all null values with zero
        self.df = self.df.fillna(0)

    def delete_Rows(self): # removes the given rows that have got a lot of zero values
        try:
            self.cur.execute(f"""DELETE FROM covid_database 
                            WHERE people_vaccinated_per_hundred = 0 AND
                            total_vaccinations_per_hundred = 0 AND
                            daily_vaccinations_per_million = 0 """)
        except Exception:
            pass
        self.db.commit()
    
    
       

    
      
