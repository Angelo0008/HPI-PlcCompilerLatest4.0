#%%
from Imports import *
import DateAndTimeManager
import Sql

def ReadInspectionData(itemCode, lotNumber):
    global totalAverage3
    global totalAverage4
    global totalAverage5
    global totalAverage10

    global totalMinimum3
    global totalMinimum4
    global totalMinimum5
    
    global totalMaximum3
    global totalMaximum4
    global totalMaximum5

    totalAverage3 = 0
    totalAverage4 = 0
    totalAverage5 = 0
    totalAverage10 = 0

    totalMinimum3 = 0
    totalMinimum4 = 0
    totalMinimum5 = 0
    
    totalMaximum3 = 0
    totalMaximum4 = 0
    totalMaximum5 = 0

    try:
        if itemCode == "EM0580107P":
            EM3PData = Sql.SelectAllDataFromTable("em0580107p_inspection")
        elif itemCode == "EM0660047P":
            pass
        elif itemCode == "EM0660045P":
            pass

        filteredData = EM3PData[(EM3PData["Lot_Number"].isin([str(lotNumber)]))]
        filteredData = filteredData.head(1)

        totalMinimum3 = filteredData["Inspection_3_Resistance_Minimum"].values[0]
        totalAverage3 = filteredData["Inspection_3_Resistance_Average"].values[0]
        totalMaximum3 = filteredData["Inspection_3_Resistance_Maximum"].values[0]

        totalMinimum4 = filteredData["Inspection_4_Dimension_Minimum"].values[0]
        totalAverage4 = filteredData["Inspection_4_Dimension_Average"].values[0]
        totalMaximum4 = filteredData["Inspection_4_Dimension_Maximum"].values[0]

        totalMinimum5 = filteredData["Inspection_5_Dimension_Minimum"].values[0]
        totalAverage5 = filteredData["Inspection_5_Dimension_Average"].values[0]
        totalMaximum5 = filteredData["Inspection_5_Dimension_Maximum"].values[0]

        totalAverage10 = filteredData["Inspection_10_Pull_Test"].values[0]

        print(f"Inspection 3 Minimum:{totalMinimum3}")
        print(f"Inspection 3 Average:{totalAverage3}")
        print(f"Inspection 3 Maximum:{totalMaximum3}")
        print(f"Inspection 4 Minimum:{totalMinimum4}")
        print(f"Inspection 4 Average:{totalAverage4}")
        print(f"Inspection 4 Maximum:{totalMaximum4}")
        print(f"Inspection 5 Minimum:{totalMinimum5}")
        print(f"Inspection 5 Average:{totalAverage5}")
        print(f"Inspection 5 Maximum:{totalMaximum5}")
        print(f"Inspection 10 Average:{totalAverage10}")

    except Exception as error:
        print(error)


# Sql.SqlConnection()
# ReadInspectionData("EM0580107P", "CAT-4J15DI")


#%%
