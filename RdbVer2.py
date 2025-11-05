#%%
from Imports import *
import DateAndTimeManager
import Sql

def ReadCheckSheet(lotNumber, modelCode):
    global materialLotNumber

    global rdbTeslaTotalAverage1
    global rdbTeslaTotalAverage2
    global rdbTeslaTotalAverage3
    global rdbTeslaTotalAverage4

    global rdbTeslaTotalMedian1
    global rdbTeslaTotalMedian2
    global rdbTeslaTotalMedian3
    global rdbTeslaTotalMedian4

    global rdbTeslaTotalMinimum1
    global rdbTeslaTotalMinimum2
    global rdbTeslaTotalMinimum3
    global rdbTeslaTotalMinimum4

    global rdbTeslaTotalMaximum1
    global rdbTeslaTotalMaximum2
    global rdbTeslaTotalMaximum3
    global rdbTeslaTotalMaximum4

    global ModelCode

    ModelCode = modelCode

    if modelCode == "RDB5200200":
        #Removing Not Needed Values
        lotNumber = lotNumber.replace('-', '')
        lotNumber = lotNumber.replace(' ', '')

        RDB5200200CheckSheet = Sql.SelectAllDataFromTable("rdb5200200_checksheet")

        filteredCheckSheet = RDB5200200CheckSheet[(RDB5200200CheckSheet["Prod_Date"].str.replace('-', '').isin([str(lotNumber)]))]

        materialLotNumber = filteredCheckSheet["Material_Lot_Number"].values[0]
        materialLotNumber = materialLotNumber[:-3]

        rdbTeslaTotalAverage1 = filteredCheckSheet["Rod_Blk_Tesla_1_Average_Data"].values[0]
        rdbTeslaTotalAverage2 = filteredCheckSheet["Rod_Blk_Tesla_2_Average_Data"].values[0]
        rdbTeslaTotalAverage3 = filteredCheckSheet["Rod_Blk_Tesla_3_Average_Data"].values[0]
        rdbTeslaTotalAverage4 = filteredCheckSheet["Rod_Blk_Tesla_4_Average_Data"].values[0]

        rdbTeslaTotalMedian1 = filteredCheckSheet["Rod_Blk_Tesla_1_Median_Data"].values[0]
        rdbTeslaTotalMedian2 = filteredCheckSheet["Rod_Blk_Tesla_2_Median_Data"].values[0]
        rdbTeslaTotalMedian3 = filteredCheckSheet["Rod_Blk_Tesla_3_Median_Data"].values[0]
        rdbTeslaTotalMedian4 = filteredCheckSheet["Rod_Blk_Tesla_4_Median_Data"].values[0]

        rdbTeslaTotalMinimum1 = filteredCheckSheet["Rod_Blk_Tesla_1_Minimum_Data"].values[0]
        rdbTeslaTotalMinimum2 = filteredCheckSheet["Rod_Blk_Tesla_2_Minimum_Data"].values[0]
        rdbTeslaTotalMinimum3 = filteredCheckSheet["Rod_Blk_Tesla_3_Minimum_Data"].values[0]
        rdbTeslaTotalMinimum4 = filteredCheckSheet["Rod_Blk_Tesla_4_Minimum_Data"].values[0]

        rdbTeslaTotalMaximum1 = filteredCheckSheet["Rod_Blk_Tesla_1_Max_Data"].values[0]
        rdbTeslaTotalMaximum2 = filteredCheckSheet["Rod_Blk_Tesla_2_Max_Data"].values[0]
        rdbTeslaTotalMaximum3 = filteredCheckSheet["Rod_Blk_Tesla_3_Max_Data"].values[0]
        rdbTeslaTotalMaximum4 = filteredCheckSheet["Rod_Blk_Tesla_4_Max_Data"].values[0]

        print(f"Tesla Average 1:{rdbTeslaTotalAverage1}")
        print(f"Tesla Average 2:{rdbTeslaTotalAverage2}")
        print(f"Tesla Average 3:{rdbTeslaTotalAverage3}")
        print(f"Tesla Average 4:{rdbTeslaTotalAverage4}")

        print(f"Tesla Median 1:{rdbTeslaTotalMedian1}")
        print(f"Tesla Median 2:{rdbTeslaTotalMedian2}")
        print(f"Tesla Median 3:{rdbTeslaTotalMedian3}")
        print(f"Tesla Median 4:{rdbTeslaTotalMedian4}")

        print(f"Tesla Minimum 1:{rdbTeslaTotalMinimum1}")
        print(f"Tesla Minimum 2:{rdbTeslaTotalMinimum2}")
        print(f"Tesla Minimum 3:{rdbTeslaTotalMinimum3}")
        print(f"Tesla Minimum 4:{rdbTeslaTotalMinimum4}")

        print(f"Tesla Maximum 1:{rdbTeslaTotalMaximum1}")
        print(f"Tesla Maximum 2:{rdbTeslaTotalMaximum2}")
        print(f"Tesla Maximum 3:{rdbTeslaTotalMaximum3}")
        print(f"Tesla Maximum 4:{rdbTeslaTotalMaximum4}")

def ReadInspectionData():
    global rdbTotalAverage1
    global rdbTotalAverage2
    global rdbTotalAverage3
    global rdbTotalAverage4
    global rdbTotalAverage5
    global rdbTotalAverage6
    global rdbTotalAverage7
    global rdbTotalAverage8
    global rdbTotalAverage9

    global rdbTotalMedian1
    global rdbTotalMedian2
    global rdbTotalMedian3
    global rdbTotalMedian4
    global rdbTotalMedian5
    global rdbTotalMedian6
    global rdbTotalMedian7
    global rdbTotalMedian8
    global rdbTotalMedian9

    global rdbTotalMinimum1
    global rdbTotalMinimum2
    global rdbTotalMinimum3
    global rdbTotalMinimum4
    global rdbTotalMinimum5
    global rdbTotalMinimum6
    global rdbTotalMinimum7
    global rdbTotalMinimum8
    global rdbTotalMinimum9

    global rdbTotalMaximum1
    global rdbTotalMaximum2
    global rdbTotalMaximum3
    global rdbTotalMaximum4
    global rdbTotalMaximum5
    global rdbTotalMaximum6
    global rdbTotalMaximum7
    global rdbTotalMaximum8
    global rdbTotalMaximum9





    rdbTotalAverage1 = 0
    rdbTotalAverage2 = 0
    rdbTotalAverage3 = 0
    rdbTotalAverage4 = 0
    rdbTotalAverage5 = 0
    rdbTotalAverage6 = 0
    rdbTotalAverage7 = 0
    rdbTotalAverage8 = 0
    rdbTotalAverage9 = 0

    rdbTotalMedian1 = 0
    rdbTotalMedian2 = 0
    rdbTotalMedian3 = 0
    rdbTotalMedian4 = 0
    rdbTotalMedian5 = 0
    rdbTotalMedian6 = 0
    rdbTotalMedian7 = 0
    rdbTotalMedian8 = 0
    rdbTotalMedian9 = 0

    rdbTotalMinimum1 = 0
    rdbTotalMinimum2 = 0
    rdbTotalMinimum3 = 0
    rdbTotalMinimum4 = 0
    rdbTotalMinimum5 = 0
    rdbTotalMinimum6 = 0
    rdbTotalMinimum7 = 0
    rdbTotalMinimum8 = 0
    rdbTotalMinimum9 = 0

    rdbTotalMaximum1 = 0
    rdbTotalMaximum2 = 0
    rdbTotalMaximum3 = 0
    rdbTotalMaximum4 = 0
    rdbTotalMaximum5 = 0
    rdbTotalMaximum6 = 0
    rdbTotalMaximum7 = 0
    rdbTotalMaximum8 = 0
    rdbTotalMaximum9 = 0

    if ModelCode == "RDB5200200":
        RDB5200200Data = Sql.SelectAllDataFromTable("rd05200200_inspection")
        filteredData = RDB5200200Data[(RDB5200200Data["Lot_Number"].astype(str).str[:-3].isin([str(materialLotNumber)]))]

        rdbTotalMinimum1 = filteredData["Inspection_1_Minimum"].values[0]
        rdbTotalAverage1 = filteredData["Inspection_1_Average"].values[0]
        rdbTotalMedian1 = filteredData["Inspection_1_Median"].values[0]
        rdbTotalMaximum1 = filteredData["Inspection_1_Maximum"].values[0]

        rdbTotalMinimum2 = filteredData["Inspection_2_Minimum"].values[0]
        rdbTotalAverage2 = filteredData["Inspection_2_Average"].values[0]
        rdbTotalMedian2 = filteredData["Inspection_2_Median"].values[0]
        rdbTotalMaximum2 = filteredData["Inspection_2_Maximum"].values[0]

        rdbTotalMinimum3 = filteredData["Inspection_3_Minimum"].values[0]
        rdbTotalAverage3 = filteredData["Inspection_3_Average"].values[0]
        rdbTotalMedian3 = filteredData["Inspection_3_Median"].values[0]
        rdbTotalMaximum3 = filteredData["Inspection_3_Maximum"].values[0]

        rdbTotalMinimum4 = filteredData["Inspection_4_Minimum"].values[0]
        rdbTotalAverage4 = filteredData["Inspection_4_Average"].values[0]
        rdbTotalMedian4 = filteredData["Inspection_4_Median"].values[0]
        rdbTotalMaximum4 = filteredData["Inspection_4_Maximum"].values[0]

        rdbTotalMinimum5 = filteredData["Inspection_5_Minimum"].values[0]
        rdbTotalAverage5 = filteredData["Inspection_5_Average"].values[0]
        rdbTotalMedian5 = filteredData["Inspection_5_Median"].values[0]
        rdbTotalMaximum5 = filteredData["Inspection_5_Maximum"].values[0]

        rdbTotalMinimum6 = filteredData["Inspection_6_Minimum"].values[0]
        rdbTotalAverage6 = filteredData["Inspection_6_Average"].values[0]
        rdbTotalMedian6 = filteredData["Inspection_6_Median"].values[0]
        rdbTotalMaximum6 = filteredData["Inspection_6_Maximum"].values[0]

        rdbTotalMinimum8 = filteredData["Inspection_8_Breaking_Test_Minimum"].values[0]
        rdbTotalAverage8 = filteredData["Inspection_8_Breaking_Test_Average"].values[0]
        rdbTotalMedian8 = filteredData["Inspection_8_Breaking_Test_Median"].values[0]
        rdbTotalMaximum8 = filteredData["Inspection_8_Breaking_Test_Maximum"].values[0]

        print(f"Inspection 1 Minimum {rdbTotalMinimum1}")
        print(f"Inspection 1 Average {rdbTotalAverage1}")
        print(f"Inspection 1 Median {rdbTotalMedian1}")
        print(f"Inspection 1 Maximum {rdbTotalMaximum1}")
        
        print(f"Inspection 2 Minimum {rdbTotalMinimum2}")
        print(f"Inspection 2 Average {rdbTotalAverage2}")
        print(f"Inspection 2 Median {rdbTotalMedian2}")
        print(f"Inspection 2 Maximum {rdbTotalMaximum2}")

        print(f"Inspection 3 Minimum {rdbTotalMinimum3}")
        print(f"Inspection 3 Average {rdbTotalAverage3}")
        print(f"Inspection 3 Median {rdbTotalMedian3}")
        print(f"Inspection 3 Maximum {rdbTotalMaximum3}")

        print(f"Inspection 4 Minimum {rdbTotalMinimum4}")
        print(f"Inspection 4 Average {rdbTotalAverage4}")
        print(f"Inspection 4 Median {rdbTotalMedian4}")
        print(f"Inspection 4 Maximum {rdbTotalMaximum4}")

        print(f"Inspection 5 Minimum {rdbTotalMinimum5}")
        print(f"Inspection 5 Average {rdbTotalAverage5}")
        print(f"Inspection 5 Median {rdbTotalMedian5}")
        print(f"Inspection 5 Maximum {rdbTotalMaximum5}")

        print(f"Inspection 6 Minimum {rdbTotalMinimum6}")
        print(f"Inspection 6 Average {rdbTotalAverage6}")
        print(f"Inspection 6 Median {rdbTotalMedian6}")
        print(f"Inspection 6 Maximum {rdbTotalMaximum6}")

        print(f"Inspection 8 Minimum {rdbTotalMinimum8}")
        print(f"Inspection 8 Average {rdbTotalAverage8}")
        print(f"Inspection 8 Median {rdbTotalMedian8}")
        print(f"Inspection 8 Maximum {rdbTotalMaximum8}")

# Sql.SqlConnection()

# ReadCheckSheet("20241017-A", "RDB5200200")
# ReadInspectionData()
#%%