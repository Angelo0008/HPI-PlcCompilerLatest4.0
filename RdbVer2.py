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

        rdbTeslaTotalAverage1 = filteredCheckSheet["Rod_Blk_Tesla_1_Average_Data"].values[0]
        rdbTeslaTotalAverage2 = filteredCheckSheet["Rod_Blk_Tesla_2_Average_Data"].values[0]
        rdbTeslaTotalAverage3 = filteredCheckSheet["Rod_Blk_Tesla_3_Average_Data"].values[0]
        rdbTeslaTotalAverage4 = filteredCheckSheet["Rod_Blk_Tesla_4_Average_Data"].values[0]

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

        print(f"Tesla Minimum 1:{rdbTeslaTotalMinimum1}")
        print(f"Tesla Minimum 2:{rdbTeslaTotalMinimum2}")
        print(f"Tesla Minimum 3:{rdbTeslaTotalMinimum3}")
        print(f"Tesla Minimum 4:{rdbTeslaTotalMinimum4}")

        print(f"Tesla Maximum 1:{rdbTeslaTotalMaximum1}")
        print(f"Tesla Maximum 2:{rdbTeslaTotalMaximum2}")
        print(f"Tesla Maximum 3:{rdbTeslaTotalMaximum3}")
        print(f"Tesla Maximum 4:{rdbTeslaTotalMaximum4}")

def ReadInspectionData():
    if ModelCode == "RDB5200200":
        RDB5200200Data = Sql.SelectAllDataFromTable("rd05200200_inspection")
        filteredData = RDB5200200Data[(RDB5200200Data["Lot_Number"].isin([str(materialLotNumber)]))]
        return materialLotNumber

Sql.SqlConnection()

ReadCheckSheet("20250807-A", "RDB5200200")
ReadInspectionData()
#%%