#%%
from Imports import *
import DateAndTimeManager
import Sql

def ReadInspectionData(itemCode, lotNumber):
    global totalAverage1
    
    global totalMinimum1

    global totalMaximum1

    totalAverage1 = 0
    
    totalMinimum1 = 0

    totalMaximum1 = 0


    try:
        if itemCode == "CSB6400802":
            CSBData = Sql.SelectAllDataFromTable("csb6400802_inspection")

        filteredData = CSBData[(CSBData["Lot_Number"].isin([str(lotNumber)]))]
        filteredData = filteredData.head(1)

        totalMinimum1 = filteredData["Inspection_1_Minimum"].values[0]
        totalAverage1 = filteredData["Inspection_1_Average"].values[0]
        totalMaximum1 = filteredData["Inspection_1_Maximum"].values[0]

        print(f"Inspection 1 Minimum:{totalMinimum1}")
        print(f"Inspection 1 Average:{totalAverage1}")
        print(f"Inspection 1 Maximum:{totalMaximum1}")

    except Exception as error:
        print(error)

# Sql.SqlConnection()
# ReadInspectionData("CSB6400802", "102824A")

#%%