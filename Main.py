import DataHanteringClass

if __name__ == "__main__":
    
    test = DataHanteringClass.DataHantering("vaccin_covid.csv", 
                                    "covid_database.db","covidVaccin")
    
# loads in all the different methods
    test.seperate_col("vaccines", ",") # states what we are seperating by

    test.create_database()
    
    test.fillNA()

    test.delete_Rows()