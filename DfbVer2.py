#%%
from Imports import *
import DateAndTimeManager
import Sql

def ReadDfbSnap(itemCode, lotNumber):
    global dfLotNum

    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

    dfLotNum = 0

    DFBSnapData = Sql.SelectAllDataFromTable("dfb_snap_data")

    filteredData = DFBSnapData[(DFBSnapData["DATE"].isin([str(lotNumber)]))]
    filteredData = filteredData[(filteredData["ITEM_BLOCK_CODE"].isin([str(itemCode)]))]

    filteredData = filteredData.head(1)

    dfLotNum = filteredData["DF_RUBBER"].values[0]
    dfLotNum = dfLotNum[:-3]

    print(lotNumber)
    print(dfLotNum)

def ReadInspectionData(itemCode):
    global totalAverage1
    global totalAverage2
    global totalAverage3
    global totalAverage4

    global totalMinimum1
    global totalMinimum2
    global totalMinimum3
    global totalMinimum4

    global totalMaximum1
    global totalMaximum2
    global totalMaximum3
    global totalMaximum4

    totalAverage1 = 0
    totalAverage2 = 0
    totalAverage3 = 0
    totalAverage4 = 0

    totalMinimum1 = 0
    totalMinimum2 = 0
    totalMinimum3 = 0
    totalMinimum4 = 0

    totalMaximum1 = 0
    totalMaximum2 = 0
    totalMaximum3 = 0
    totalMaximum4 = 0

    if itemCode == "DFB6600600":
        DFBData = Sql.SelectAllDataFromTable("df06600600_inspection")

        filteredData = DFBData[(DFBData["Lot_Number"].isin([str(dfLotNum)]))]
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

def ReadTensileData(itemCode):
    global rateOfChangeTotalAverage
    global rateOfChangeTotalMinimum
    global rateOfChangeTotalMaximum

    global startForceTotalAverage
    global startForceTotalMinimum
    global startForceTotalMaximum

    global terminatingForceTotalAverage
    global terminatingForceTotalMinimum
    global terminatingForceTotalMaximum

    rateOfChangeTotalAverage = 0
    rateOfChangeTotalMinimum = 0
    rateOfChangeTotalMaximum = 0

    startForceTotalAverage = 0
    startForceTotalMinimum = 0
    startForceTotalMaximum = 0

    terminatingForceTotalAverage = 0
    terminatingForceTotalMinimum = 0
    terminatingForceTotalMaximum = 0

    if itemCode == "DFB6600600":
        DFBTensileData = Sql.SelectAllDataFromTable("dfb_tensile_data")

        filteredData = DFBTensileData[(DFBTensileData["DF_LOT_NO"].isin([str(dfLotNum)]))]
        filteredData = filteredData.head(1)

        rateOfChangeTotalMinimum = filteredData["RATE_OF_CHANGE_MIN"].values[0]
        rateOfChangeTotalAverage = filteredData["RATE_OF_CHANGE_AVE"].values[0]
        rateOfChangeTotalMaximum = filteredData["RATE_OF_CHANGE_MAX"].values[0]

        startForceTotalMinimum = filteredData["START_FORCE_MIN"].values[0]
        startForceTotalAverage = filteredData["START_FORCE_AVE"].values[0]
        startForceTotalMaximum = filteredData["START_FORCE_MAX"].values[0]

        terminatingForceTotalMinimum = filteredData["TERMINATING_FORCE_MIN"].values[0]
        terminatingForceTotalAverage = filteredData["TERMINATING_FORCE_AVE"].values[0]
        terminatingForceTotalMaximum = filteredData["TERMINATING_FORCE_MAX"].values[0]

        print(f"RATE OF CHANGE MINIMUM: {rateOfChangeTotalMinimum}")
        print(f"RATE OF CHANGE AVERAGE: {rateOfChangeTotalAverage}")
        print(f"RATE OF CHANGE MAXIMUM: {rateOfChangeTotalMaximum}")

        print(f"START FORCE MINIMUM: {startForceTotalMinimum}")
        print(f"START FORCE AVERAGE: {startForceTotalAverage}")
        print(f"START FORCE MAXIMUM: {startForceTotalMaximum}")

        print(f"TERMINATING FORCE MINIMUM: {terminatingForceTotalMinimum}")
        print(f"TERMINATING FORCE AVERAGE: {terminatingForceTotalAverage}")
        print(f"TERMINATING FORCE MAXIMUM: {terminatingForceTotalMaximum}")

#%%
# Sql.SqlConnection()
# ReadDfbSnap("DFB6600600", "20241128-A")
# ReadInspectionData("DFB6600600")
# ReadTensileData("DFB6600600")

# %%
