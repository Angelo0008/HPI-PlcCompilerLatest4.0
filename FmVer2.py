#%%
from Imports import *
import DateAndTimeManager
import Sql

def ReadInspectionData(itemCode, lotNumber):
    global totalAverage1
    global totalAverage2
    global totalAverage3
    global totalAverage4
    global totalAverage5
    global totalAverage6
    global totalAverage7

    global totalMinimum1
    global totalMinimum2
    global totalMinimum3
    global totalMinimum4
    global totalMinimum5
    global totalMinimum6
    global totalMinimum7
    
    global totalMaximum1
    global totalMaximum2
    global totalMaximum3
    global totalMaximum4
    global totalMaximum5
    global totalMaximum6
    global totalMaximum7

    totalAverage1 = 0
    totalAverage2 = 0
    totalAverage3 = 0
    totalAverage4 = 0
    totalAverage5 = 0
    totalAverage6 = 0
    totalAverage7 = 0

    totalMinimum1 = 0
    totalMinimum2 = 0
    totalMinimum3 = 0
    totalMinimum4 = 0
    totalMinimum5 = 0
    totalMinimum6 = 0
    totalMinimum7 = 0
    
    totalMaximum1 = 0
    totalMaximum2 = 0
    totalMaximum3 = 0
    totalMaximum4 = 0
    totalMaximum5 = 0
    totalMaximum6 = 0
    totalMaximum7 = 0

    if itemCode == "FM05000102-00A" or itemCode == "FM05000102-01A":
        FMData = Sql.SelectAllDataFromTable("fm05000102_inspection")

    filteredData = FMData[(FMData["Lot_Number"].isin([str(lotNumber)]))]
    filteredData = filteredData.head(1)

    totalMinimum1 = filteredData["Inspection_1_Minimum"].values[0]
    totalAverage1 = filteredData["Inspection_1_Average"].values[0]
    totalMaximum1 = filteredData["Inspection_1_Maximum"].values[0]

    totalMinimum2 = filteredData["Inspection_2_Minimum"].values[0]
    totalAverage2 = filteredData["Inspection_2_Average"].values[0]
    totalMaximum2 = filteredData["Inspection_2_Maximum"].values[0]

    totalMinimum3 = filteredData["Inspection_3_Minimum"].values[0]
    totalAverage3 = filteredData["Inspection_3_Average"].values[0]
    totalMaximum3 = filteredData["Inspection_3_Maximum"].values[0]

    totalMinimum4 = filteredData["Inspection_4_Minimum"].values[0]
    totalAverage4 = filteredData["Inspection_4_Average"].values[0]
    totalMaximum4 = filteredData["Inspection_4_Maximum"].values[0]

    totalMinimum5 = filteredData["Inspection_5_Minimum"].values[0]
    totalAverage5 = filteredData["Inspection_5_Average"].values[0]
    totalMaximum5 = filteredData["Inspection_5_Maximum"].values[0]

    totalMinimum6 = filteredData["Inspection_6_Minimum"].values[0]
    totalAverage6 = filteredData["Inspection_6_Average"].values[0]
    totalMaximum6 = filteredData["Inspection_6_Maximum"].values[0]

    totalMinimum7 = filteredData["Inspection_7_Minimum"].values[0]
    totalAverage7 = filteredData["Inspection_7_Average"].values[0]
    totalMaximum7 = filteredData["Inspection_7_Maximum"].values[0]

    print(f"Inspection 1 Minimum:{totalMinimum1}")
    print(f"Inspection 1 Average:{totalAverage1}")
    print(f"Inspection 1 Maximum:{totalMaximum1}")

    print(f"Inspection 2 Minimum:{totalMinimum2}")
    print(f"Inspection 2 Average:{totalAverage2}")
    print(f"Inspection 2 Maximum:{totalMaximum2}")

    print(f"Inspection 3 Minimum:{totalMinimum3}")
    print(f"Inspection 3 Average:{totalAverage3}")
    print(f"Inspection 3 Maximum:{totalMaximum3}")

    print(f"Inspection 4 Minimum:{totalMinimum4}")
    print(f"Inspection 4 Average:{totalAverage4}")
    print(f"Inspection 4 Maximum:{totalMaximum4}")

    print(f"Inspection 5 Minimum:{totalMinimum5}")
    print(f"Inspection 5 Average:{totalAverage5}")
    print(f"Inspection 5 Maximum:{totalMaximum5}")

    print(f"Inspection 6 Minimum:{totalMinimum6}")
    print(f"Inspection 6 Average:{totalAverage6}")
    print(f"Inspection 6 Maximum:{totalMaximum6}")

    print(f"Inspection 7 Minimum:{totalMinimum7}")
    print(f"Inspection 7 Average:{totalAverage7}")
    print(f"Inspection 7 Maximum:{totalMaximum7}")

    # return filteredData

# Sql.SqlConnection()
# ReadInspectionData("FM05000102-01A", "072324A-40")
#%%