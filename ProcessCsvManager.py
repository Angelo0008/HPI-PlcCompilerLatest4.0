from Imports import *
import PiMachineManager
import DateAndTimeManager
import Sql
import ColumnCreator

from Em2p import em2P
from Em3p import em3P
from Fm import fM
from Dfb import dFB
from Dfb import Tensile
from Rdb import rDB
from Csb import cSB

import Em2pVer2
import Em3pVer2
import FmVer2
import RdbVer2
import CsbVer2
import DfbVer2

dfVt1 = ""
dfVt2 = ""
dfVt3 = ""
dfVt4 = ""
dfVt5 = ""
dfVt6 = ""

process1Row = 0
process2Row = 0
process3Row = 0
process4Row = 0
process5Row = 0
process6Row = 0

tempDfVt1 = ""
tempDfVt2 = ""
tempDfVt3 = ""
tempDfVt4 = ""
tempDfVt5 = ""
tempDfVt6 = ""

ngProcess = ""
    
process1Status = ""
process2Status = ""
process3Status = ""
process4Status = ""
process5Status = ""
process6Status = ""
isRepairedWithNG = False
piStatus = ""

canCompile = False

programRunning = True

excelData = ""
compiledFrame = ""

previousDate = None
previousTime = None

# %%
def ReadCsv():
    global dfVt1
    global dfVt2
    global dfVt3
    global dfVt4
    global dfVt5
    global dfVt6

    global process1Row
    global process2Row
    global process3Row
    global process4Row
    global process5Row
    global process6Row

    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

    # vt1Directory = (r'\\192.168.2.19\ai_team\AI Program\Outputs\FC1 CSV\VT1')
    # os.chdir(vt1Directory)
    # dfVt1 = pd.read_csv('log000_1.csv', encoding='latin1')

    dfVt1 = Sql.SelectAllDataFromTable("process1_data")
    dfVt1.columns = ["Process 1 DATA No",
        "Process 1 DateTime",
        "Process 1 DATE",
        "Process 1 TIME",
        "Process 1 Model Code",
        "Process 1 S/N",
        "Process 1 ID",
        "Process 1 NAME",
        "Process 1 Regular/Contractual",
        "Process 1 Em2p",
        "Process 1 Em2p Lot No",
        "Process 1 Em3p",
        "Process 1 Em3p Lot No",
        "Process 1 Harness",
        "Process 1 Harness Lot No",
        "Process 1 Frame",
        "Process 1 Frame Lot No",
        "Process 1 Bushing",
        "Process 1 Bushing Lot No",
        "Process 1 ST",
        "Process 1 Actual Time",
        "Process 1 NG Cause",
        "Process 1 Repaired Action"]
    
    dfVt1 = dfVt1.drop(['Process 1 DateTime'], axis=1)
    
    # vt2Directory = (r'\\192.168.2.19\ai_team\AI Program\Outputs\FC1 CSV\VT2')
    # os.chdir(vt2Directory)
    # dfVt2 = pd.read_csv('log000_2.csv', encoding='latin1')

    dfVt2 = Sql.SelectAllDataFromTable("process2_data")
    dfVt2.columns = ["Process 2 DATA No",
        "Process 2 DateTime",
        "Process 2 DATE",
        "Process 2 TIME",
        "Process 2 Model Code",
        "Process 2 S/N",
        "Process 2 ID",
        "Process 2 NAME",
        "Process 2 Regular/Contractual",
        "Process 2 M4x40 Screw",
        "Process 2 M4x40 Screw Lot No",
        "Process 2 Rod Blk",
        "Process 2 Rod Blk Lot No",
        "Process 2 Df Blk",
        "Process 2 Df Blk Lot No",
        "Process 2 Df Ring",
        "Process 2 Df Ring Lot No",
        "Process 2 Washer",
        "Process 2 Washer Lot No",
        "Process 2 Lock Nut",
        "Process 2 Lock Nut Lot No",
        "Process 2 ST",
        "Process 2 Actual Time",
        "Process 2 NG Cause",
        "Process 2 Repaired Action"]
    
    dfVt2 = dfVt2.drop(['Process 2 DateTime'], axis=1)

    # vt3Directory = (r'\\192.168.2.19\ai_team\AI Program\Outputs\FC1 CSV\VT3')
    # os.chdir(vt3Directory)
    # dfVt3 = pd.read_csv('log000_3.csv', encoding='latin1')

    dfVt3 = Sql.SelectAllDataFromTable("process3_data")
    dfVt3.columns = ["Process 3 DATA No",
        "Process 3 DateTime",
        "Process 3 DATE",
        "Process 3 TIME",
        "Process 3 Model Code",
        "Process 3 S/N",
        "Process 3 ID",
        "Process 3 NAME",
        "Process 3 Regular/Contractual",
        "Process 3 Frame Gasket",
        "Process 3 Frame Gasket Lot No",
        "Process 3 Casing Block",
        "Process 3 Casing Block Lot No",
        "Process 3 Casing Gasket",
        "Process 3 Casing Gasket Lot No",
        "Process 3 M4x16 Screw 1",
        "Process 3 M4x16 Screw 1 Lot No",
        "Process 3 M4x16 Screw 2",
        "Process 3 M4x16 Screw 2 Lot No",
        "Process 3 Ball Cushion",
        "Process 3 Ball Cushion Lot No",
        "Process 3 Frame Cover",
        "Process 3 Frame Cover Lot No",
        "Process 3 Partition Board",
        "Process 3 Partition Board Lot No",
        "Process 3 Built In Tube 1",
        "Process 3 Built In Tube 1 Lot No",
        "Process 3 Built In Tube 2",
        "Process 3 Built In Tube 2 Lot No",
        "Process 3 Head Cover",
        "Process 3 Head Cover Lot No",
        "Process 3 Casing Packing",
        "Process 3 Casing Packing Lot No",
        "Process 3 M4x12 Screw",
        "Process 3 M4x12 Screw Lot No",
        "Process 3 Csb L",
        "Process 3 Csb L Lot No",
        "Process 3 Csb R",
        "Process 3 Csb R Lot No",
        "Process 3 Head Packing",
        "Process 3 Head Packing Lot No",
        "Process 3 ST",
        "Process 3 Actual Time",
        "Process 3 NG Cause",
        "Process 3 Repaired Action"]
    
    dfVt3 = dfVt3.drop(['Process 3 DateTime'], axis=1)

    # vt4Directory = (r'\\192.168.2.19\ai_team\AI Program\Outputs\FC1 CSV\VT4')
    # os.chdir(vt4Directory)
    # dfVt4 = pd.read_csv('log000_4.csv', encoding='latin1')

    dfVt4 = Sql.SelectAllDataFromTable("process4_data")
    dfVt4.columns = ["Process 4 DATA No",
        "Process 4 DateTime",
        "Process 4 DATE",
        "Process 4 TIME",
        "Process 4 Model Code",
        "Process 4 S/N",
        "Process 4 ID",
        "Process 4 NAME",
        "Process 4 Regular/Contractual",
        "Process 4 Tank",
        "Process 4 Tank Lot No",
        "Process 4 Upper Housing",
        "Process 4 Upper Housing Lot No",
        "Process 4 Cord Hook",
        "Process 4 Cord Hook Lot No",
        "Process 4 M4x16 Screw",
        "Process 4 M4x16 Screw Lot No",
        "Process 4 Tank Gasket",
        "Process 4 Tank Gasket Lot No",
        "Process 4 Tank Cover",
        "Process 4 Tank Cover Lot No",
        "Process 4 Housing Gasket",
        "Process 4 Housing Gasket Lot No",
        "Process 4 M4x40 Screw",
        "Process 4 M4x40 Screw Lot No",
        "Process 4 PartitionGasket",
        "Process 4 PartitionGasket Lot No",
        "Process 4 M4x12 Screw",
        "Process 4 M4x12 Screw Lot No",
        "Process 4 Muffler",
        "Process 4 Muffler Lot No",
        "Process 4 Muffler Gasket",
        "Process 4 Muffler Gasket Lot No",
        "Process 4 VCR",
        "Process 4 VCR Lot No",
        "Process 4 ST",
        "Process 4 Actual Time",
        "Process 4 NG Cause",
        "Process 4 Repaired Action"]
    
    dfVt4 = dfVt4.drop(['Process 4 DateTime'], axis=1)

    # vt5Directory = (r'\\192.168.2.19\ai_team\AI Program\Outputs\FC1 CSV\VT5')
    # os.chdir(vt5Directory)
    # dfVt5 = pd.read_csv('log000_5.csv', encoding='latin1')

    dfVt5 = Sql.SelectAllDataFromTable("process5_data")
    dfVt5.columns = ["Process 5 DATA No",
        "Process 5 DateTime",
        "Process 5 DATE",
        "Process 5 TIME",
        "Process 5 Model Code",
        "Process 5 S/N",
        "Process 5 ID",
        "Process 5 NAME",
        "Process 5 Regular/Contractual",
        "Process 5 Rating Label",
        "Process 5 Rating Label Lot No",
        "Process 5 ST",
        "Process 5 Actual Time",
        "Process 5 NG Cause",
        "Process 5 Repaired Action"]
    
    dfVt5 = dfVt5.drop(['Process 5 DateTime'], axis=1)

    # vt6Directory = (r'\\192.168.2.19\ai_team\AI Program\Outputs\FC1 CSV\VT6')
    # os.chdir(vt6Directory)
    # dfVt6 = pd.read_csv('log000_6.csv', encoding='latin1')

    dfVt6 = Sql.SelectAllDataFromTable("process6_data")
    dfVt6.columns = ["Process 6 DATA No",
        "Process 6 DateTime",
        "Process 6 DATE",
        "Process 6 TIME",
        "Process 6 Model Code",
        "Process 6 S/N",
        "Process 6 ID",
        "Process 6 NAME",
        "Process 6 Regular/Contractual",
        "Process 6 Vinyl",
        "Process 6 Vinyl Lot No",
        "Process 6 ST",
        "Process 6 Actual Time",
        "Process 6 NG Cause",
        "Process 6 Repaired Action"]
    
    dfVt6 = dfVt6.drop(['Process 6 DateTime'], axis=1)

    dfVt1 = dfVt1[dfVt1["Process 1 Regular/Contractual"].str.contains("REG", na = False)]
    # dfVt1 = dfVt1[(dfVt1["Process 1 DATE"].isin([dateToday]))]
    dfVt1 = dfVt1[(dfVt1["Process 1 DATE"].isin([DateAndTimeManager.dateToRead]))]

    dfVt2 = dfVt2[dfVt2["Process 2 Regular/Contractual"].str.contains("REG", na = False)]
    # dfVt2 = dfVt2[(dfVt2["Process 2 DATE"].isin([dateToday]))]
    dfVt2 = dfVt2[(dfVt2["Process 2 DATE"].isin([DateAndTimeManager.dateToRead]))]

    dfVt3 = dfVt3[dfVt3["Process 3 Regular/Contractual"].str.contains("REG", na = False)]
    # dfVt3 = dfVt3[(dfVt3["Process 3 DATE"].isin([dateToday]))]
    dfVt3 = dfVt3[(dfVt3["Process 3 DATE"].isin([DateAndTimeManager.dateToRead]))]

    dfVt4 = dfVt4[dfVt4["Process 4 Regular/Contractual"].str.contains("REG", na = False)]
    # dfVt4 = dfVt4[(dfVt4["Process 4 DATE"].isin([dateToday]))]
    dfVt4 = dfVt4[(dfVt4["Process 4 DATE"].isin([DateAndTimeManager.dateToRead]))]

    dfVt5 = dfVt5[dfVt5["Process 5 Regular/Contractual"].str.contains("REG", na = False)]
    # dfVt5 = dfVt5[(dfVt5["Process 5 DATE"].isin([dateToday]))]
    dfVt5 = dfVt5[(dfVt5["Process 5 DATE"].isin([DateAndTimeManager.dateToRead]))]

    dfVt6 = dfVt6[dfVt6["Process 6 Regular/Contractual"].str.contains("REG", na = False)]
    # dfVt6 = dfVt6[(dfVt6["Process 6 DATE"].isin([dateToday]))]
    dfVt6 = dfVt6[(dfVt6["Process 6 DATE"].isin([DateAndTimeManager.dateToRead]))]

def RowAnalyzer():
    global tempDfVt1
    global tempDfVt2
    global tempDfVt3
    global tempDfVt4
    global tempDfVt5
    global tempDfVt6

    global process1Status
    global process2Status
    global process3Status
    global process4Status
    global process5Status
    global process6Status
    global isRepairedWithNG

    global canCompile

    if tempDfVt1["Process 1 Repaired Action"].values[0] == "-" and tempDfVt2["Process 2 Repaired Action"].values[0] == "-" and tempDfVt3["Process 3 Repaired Action"].values[0] == "-" and tempDfVt4["Process 4 Repaired Action"].values[0] == "-" and tempDfVt5["Process 5 Repaired Action"].values[0] == "-" and tempDfVt6["Process 6 Repaired Action"].values[0] == "-":
        if tempDfVt1["Process 1 NG Cause"].values[0] == "-":
            print("Process1 Good")
            process1Status = "Good"
            if tempDfVt2["Process 2 NG Cause"].values[0] == "-":
                print("Process2 Good")
                process2Status = "Good"
                if tempDfVt3["Process 3 NG Cause"].values[0] == "-":
                    print("Process3 Good")
                    process3Status = "Good"
                    if tempDfVt4["Process 4 NG Cause"].values[0] == "-":
                        print("Process4 Good")
                        process4Status = "Good"
                        if tempDfVt5["Process 5 NG Cause"].values[0] == "-":
                            print("Process5 Good")
                            process5Status = "Good"
                            if tempDfVt6["Process 6 NG Cause"].values[0] == "-":
                                print("Process6 Good")
                                process6Status = "Good"
                            else:
                                print("Process6 NG")
                                process6Status = "NG"
                        elif tempDfVt5["Process 5 NG Cause"].values[0].replace(' ', '') == "NGPRESSURE":
                            print("Process5 NG PRESSURE")
                            process5Status = "NG PRESSURE"
                        elif tempDfVt5["Process 5 NG Cause"].values[0].replace(' ', '') == "NGFLOW":
                            print("Process5 NG FLOW")
                            process5Status = "NG FLOW"
                        elif tempDfVt5["Process 5 NG Cause"].str.replace(" ", "").str.lower().str.contains("water").any():
                            print("Process5 WATER MARK")
                            process5Status = "WATER MARK"
                        elif tempDfVt5["Process 5 NG Cause"].str.replace(" ", "").str.lower().str.contains("corrosion").any():
                            print("Process5 CORROSION")
                            process5Status = "CORROSION"
                        elif tempDfVt5["Process 5 NG Cause"].str.replace(" ", "").str.lower().str.contains("black").any():
                            print("Process5 BLACKSPOT")
                            process5Status = "BLACKSPOTS"
                        else:
                            print("Process5 NG")
                            process5Status = "NG"
                    else:
                        print("Process4 NG")
                        process4Status = "NG"
                else:
                    print("Process3 NG")
                    process3Status = "NG"
            else:
                print("Process2 NG")
                process2Status = "NG"
        else:
            print("Process1 NG")
            process1Status = "NG"
    else:
        print("Repaired")

        if tempDfVt1["Process 1 Repaired Action"].values[0] != "-":
            process1Status = "Repaired"
            process2Status = ""
            process3Status = ""
            process4Status = ""
            process5Status = ""
            process6Status = ""
        if tempDfVt2["Process 2 Repaired Action"].values[0] != "-":
            process1Status = ""
            process2Status = "Repaired"
            process3Status = ""
            process4Status = ""
            process5Status = ""
            process6Status = ""
        if tempDfVt3["Process 3 Repaired Action"].values[0] != "-":
            process1Status = ""
            process2Status = ""
            process3Status = "Repaired"
            process4Status = ""
            process5Status = ""
            process6Status = ""
        if tempDfVt4["Process 4 Repaired Action"].values[0] != "-":
            process1Status = ""
            process2Status = ""
            process3Status = ""
            process4Status = "Repaired"
            process5Status = ""
            process6Status = ""
        if tempDfVt5["Process 5 Repaired Action"].values[0] != "-":
            process1Status = ""
            process2Status = ""
            process3Status = ""
            process4Status = ""
            process5Status = "Repaired"
            process6Status = ""
        if tempDfVt6["Process 6 Repaired Action"].values[0] != "-":
            process1Status = ""
            process2Status = ""
            process3Status = ""
            process4Status = ""
            process5Status = ""
            process6Status = "Repaired"

        #Checking Again For NG Process
        if tempDfVt1["Process 1 NG Cause"].values[0] != "-":
            process1Status = "NG"
            isRepairedWithNG = True
        elif tempDfVt2["Process 2 NG Cause"].values[0] != "-":
            process2Status = "NG"
            isRepairedWithNG = True
        elif tempDfVt3["Process 3 NG Cause"].values[0] != "-":
            process3Status = "NG"
            isRepairedWithNG = True
        elif tempDfVt4["Process 4 NG Cause"].values[0] != "-":
            process4Status = "NG"
            isRepairedWithNG = True
        elif tempDfVt5["Process 5 NG Cause"].values[0].replace(' ', '') == "NGPRESSURE":
            print("Repaired With NG PRESSURE__________________________________________________________________________________________________________________")
            process5Status = "NG PRESSURE"
            isRepairedWithNG = True
        elif tempDfVt5["Process 5 NG Cause"].values[0] != "-":
            process5Status = "NG"
            isRepairedWithNG = True
        elif tempDfVt6["Process 6 NG Cause"].values[0] != "-":
            process6Status = "NG"
            isRepairedWithNG = True
    canCompile = True

def CsvOrganize():
    global dfVt1
    global dfVt2
    global dfVt3
    global dfVt4
    global dfVt5
    global dfVt6

    global process1Row
    global process2Row
    global process3Row
    global process4Row
    global process5Row
    global process6Row

    global tempDfVt1
    global tempDfVt2
    global tempDfVt3
    global tempDfVt4
    global tempDfVt5
    global tempDfVt6

    global ngProcess
    
    global process1Status
    global process2Status
    global process3Status
    global process4Status
    global process5Status
    global process6Status
    global isRepairedWithNG
    global piStatus

    global canCompile

    global programRunning

    process1Status = ""
    process2Status = ""
    process3Status = ""
    process4Status = ""
    process5Status = ""
    process6Status = ""
    isRepairedWithNG = False
    piStatus = ""

    isVt1Blank = False
    isVt2Blank = False
    isVt3Blank = False
    isVt4Blank = False
    isVt5Blank = False
    isVt6Blank = False
 
    # ReadPI In PiRow Value
    try:
        PiMachineManager.tempdfPi = PiMachineManager.dfPi.iloc[[PiMachineManager.piRow], :]
    except IndexError:
        pass

    if "INSPECTION ONLY" in PiMachineManager.tempdfPi["PROCESS_S_N"].values:
        piStatus = "INSPECTION ONLY"
        print("INSPECTION ONLY")
    else:
        try:
            print(f"Process1 Row: {process1Row}")
            print(f"Process2 Row: {process2Row}")
            print(f"Process3 Row: {process3Row}")
            print(f"Process4 Row: {process4Row}")
            print(f"Process5 Row: {process5Row}")
            print(f"Process6 Row: {process6Row}")
            
            #Checking If There's Value In tempDfVt1 To 6
            tempDfVt1 = dfVt1.iloc[[process1Row], :]
            tempDfVt2 = dfVt2.iloc[[process2Row], :]
            tempDfVt3 = dfVt3.iloc[[process3Row], :]
            tempDfVt4 = dfVt4.iloc[[process4Row], :]
            tempDfVt5 = dfVt5.iloc[[process5Row], :]
            tempDfVt6 = dfVt6.iloc[[process6Row], :]

            RowAnalyzer()
        except:
            #Checking What tempDfVt Is Blank
            try:
                tempDfVt1 = dfVt1.iloc[[process1Row], :]
                isVt1Blank = False
            except:
                try:
                    print("VT1 Blank")
                    isVt1Blank = True
                    tempDfVt1 = dfVt1.iloc[[len(dfVt1) - 1], :]
                    tempDfVt1["Process 1 Repaired Action"] = "-"
                    tempDfVt1["Process 1 NG Cause"] = "-"
                except:
                    print("VT1 Blank")
                    isVt1Blank = True
            try:
                tempDfVt2 = dfVt2.iloc[[process2Row], :]
                isVt2Blank = False
            except:
                try:
                    print("VT2 Blank")
                    isVt2Blank = True
                    tempDfVt2 = dfVt2.iloc[[len(dfVt2) - 1], :]
                    tempDfVt2["Process 2 Repaired Action"] = "-"
                    tempDfVt2["Process 2 NG Cause"] = "-"
                except:
                    print("VT2 Blank")
                    isVt2Blank = True
            try:
                tempDfVt3 = dfVt3.iloc[[process3Row], :]
                isVt3Blank = False
            except:
                try:
                    print("VT3 Blank")
                    isVt3Blank = True
                    tempDfVt3 = dfVt3.iloc[[len(dfVt3) - 1], :]
                    tempDfVt3["Process 3 Repaired Action"] = "-"
                    tempDfVt3["Process 3 NG Cause"] = "-"
                except:
                    print("VT3 Blank")
                    isVt3Blank = True
            try:
                tempDfVt4 = dfVt4.iloc[[process4Row], :]
                isVt4Blank = False
            except:
                try:
                    print("VT4 Blank")
                    isVt4Blank = True
                    tempDfVt4 = dfVt4.iloc[[len(dfVt4) - 1], :]
                    tempDfVt4["Process 4 Repaired Action"] = "-"
                    tempDfVt4["Process 4 NG Cause"] = "-"
                except:
                    print("VT4 Blank")
                    isVt4Blank = True
            try:
                tempDfVt5 = dfVt5.iloc[[process5Row], :]
                isVt5Blank = False
            except:
                try:
                    print("VT5 Blank")
                    isVt5Blank = True
                    tempDfVt5 = dfVt5.iloc[[len(dfVt5) - 1], :]
                    tempDfVt5["Process 5 Repaired Action"] = "-"
                    tempDfVt5["Process 5 NG Cause"] = "-"
                except:
                    print("VT5 Blank")
                    isVt5Blank = True
            try:
                tempDfVt6 = dfVt6.iloc[[process6Row], :]
                isVt6Blank = False
            except:
                try:
                    print("VT6 Blank")
                    isVt6Blank = True
                    tempDfVt6 = dfVt6.iloc[[len(dfVt6) - 1], :]
                    tempDfVt6["Process 6 Repaired Action"] = "-"
                    tempDfVt6["Process 6 NG Cause"] = "-"
                except:
                    print("VT6 Blank")
                    isVt6Blank = True

            #No Data In Next Row
            if isVt1Blank == True and isVt2Blank == True and isVt3Blank == True and isVt4Blank == True and isVt5Blank == True and isVt6Blank == True:
                print("No More To Read")
                canCompile = False
            else:
                RowAnalyzer()

            # #Blank At Process2, Process3, Process4, Process5
            # elif isVt1Blank == False and isVt2Blank == True and isVt3Blank == True and isVt4Blank == True and isVt5Blank == True and isVt6Blank == True and tempDfVt1["Process 1 Repaired Action"].values[0] == "-":
            #     if tempDfVt1["Process 1 NG Cause"].values[0] != "-":
            #         print("Process 1 Proceed With NG")
            #         process1Status = "NG"
            #         canCompile = True
            #     else:
            #         print("Pending In Process 1")
            #         canCompile = False

            # #Blank At Process3, Process4, Process 5
            # elif isVt1Blank == False and isVt2Blank == False and isVt3Blank == True and isVt4Blank == True and isVt5Blank == True and isVt6Blank == True and tempDfVt2["Process 2 Repaired Action"].values[0] == "-":
            #     if tempDfVt2["Process 2 NG Cause"].values[0] != "-":
            #         print("Process 2 Proceed With NG")
            #         process1Status = "Good"
            #         process2Status = "NG"
            #         canCompile = True
            #     else:
            #         print("Pending In Process 1 and Process 2")
            #         canCompile = False
            # #Blank At Process4, Process5
            # elif isVt1Blank == False and isVt2Blank == False and isVt3Blank == False and isVt4Blank == True and isVt5Blank == True and isVt6Blank == True and tempDfVt3["Process 3 Repaired Action"].values[0] == "-":
            #     if tempDfVt3["Process 3 NG Cause"].values[0] != "-":
            #         print("Process 3 Proceed With NG")
            #         process1Status = "Good"
            #         process2Status = "Good"
            #         process3Status = "NG"
            #         canCompile = True
            #     else:
            #         print("Pending In Process 1 and Process 2 and Process 3")
            #         canCompile = False
            # #Blank At Process5
            # elif isVt1Blank == False and isVt2Blank == False and isVt3Blank == False and isVt4Blank == False and isVt5Blank == True and isVt6Blank == True and tempDfVt4["Process 4 Repaired Action"].values[0] == "-":
            #     if tempDfVt4["Process 4 NG Cause"].values[0] != "-":
            #         print("Process 4 Proceed With NG")
            #         process1Status = "Good"
            #         process2Status = "Good"
            #         process3Status = "Good"
            #         process4Status = "NG"
            #         canCompile = True
            #     else:
            #         print("Pending In Process 1 and Process 2 and Process 3 and Process 4")
            #         canCompile = False
            # #Blank At Process6       
            # elif isVt1Blank == False and isVt2Blank == False and isVt3Blank == False and isVt4Blank == False and isVt5Blank == False and isVt6Blank == True and tempDfVt4["Process 4 Repaired Action"].values[0] == "-":
            #     if tempDfVt5["Process 5 NG Cause"].values[0] != "-":
            #         print("Process 5 Proceed With NG")
            #         process1Status = "Good"
            #         process2Status = "Good"
            #         process3Status = "Good"
            #         process4Status = "Good"
            #         process5Status = "NG"
            #         canCompile = True
            #     else:
            #         print("Pending In Process 1 and Process 2 and Process 3 and Process 4 and Process 5")
            #         canCompile = False
            



            # #Repair Process 1
            # elif isVt1Blank == False and isVt2Blank == True and isVt3Blank == True and isVt4Blank == True and isVt5Blank == True and isVt6Blank == True and tempDfVt1["Process 1 Repaired Action"].values[0] != "-":
            #         print("Pending Repair At Process 1")
            #         canCompile = False
            # elif isVt1Blank == False and isVt2Blank == False and isVt3Blank == True and isVt4Blank == True and isVt5Blank == True and isVt6Blank == True and tempDfVt1["Process 1 Repaired Action"].values[0] != "-":
            #         print("Pending Repair At Process 1, Pending In Process 2")
            #         canCompile = False
            # elif isVt1Blank == False and isVt2Blank == False and isVt3Blank == False and isVt4Blank == True and isVt5Blank == True and isVt6Blank == True and tempDfVt1["Process 1 Repaired Action"].values[0] != "-":
            #         print("Pending Repair At Process 1, Pending In Process 2, Pending In Process 3")
            #         canCompile = False
            # elif isVt1Blank == False and isVt2Blank == False and isVt3Blank == False and isVt4Blank == False and isVt5Blank == True and isVt6Blank == True and tempDfVt1["Process 1 Repaired Action"].values[0] != "-":
            #         print("Pending Repair At Process 1, Pending In Process 2, Pending In Process 3, Pending In Process 4")
            #         canCompile = False
            # elif isVt1Blank == False and isVt2Blank == False and isVt3Blank == False and isVt4Blank == False and isVt5Blank == False and isVt6Blank == True and tempDfVt1["Process 1 Repaired Action"].values[0] != "-":
            #         print("Pending Repair At Process 1, Pending In Process 2, Pending In Process 3, Pending In Process 4, Pending In Process 6")
            #         canCompile = False
            # #Repair Process 2
            # elif isVt1Blank == True and isVt2Blank == False and isVt3Blank == True and isVt4Blank == True and isVt5Blank == True and isVt6Blank == True and tempDfVt2["Process 2 Repaired Action"].values[0] != "-":
            #         print("Pending Repair At Process 2")
            #         canCompile = False
            # elif isVt1Blank == True and isVt2Blank == False and isVt3Blank == False and isVt4Blank == True and isVt5Blank == True and isVt6Blank == True and tempDfVt2["Process 2 Repaired Action"].values[0] != "-":
            #         print("Pending Repair At Process 2, Process 3")
            #         canCompile = False
            # elif isVt1Blank == True and isVt2Blank == False and isVt3Blank == False and isVt4Blank == False and isVt5Blank == True and isVt6Blank == True and tempDfVt2["Process 2 Repaired Action"].values[0] != "-":
            #         print("Pending Repair At Process 2, Process 3, Process 4")
            #         canCompile = False
            # elif isVt1Blank == True and isVt2Blank == False and isVt3Blank == False and isVt4Blank == False and isVt5Blank == False and isVt6Blank == True and tempDfVt2["Process 2 Repaired Action"].values[0] != "-":
            #         print("Pending Repair At Process 2, Process 3, Process 4, Process 5")
            #         canCompile = False
            # elif isVt1Blank == True and isVt2Blank == False and isVt3Blank == False and isVt4Blank == False and isVt5Blank == False and isVt6Blank == False and tempDfVt2["Process 2 Repaired Action"].values[0] != "-":
            #         process2Status = "Repaired"
            #         canCompile = True
            # #Repair Process 3
            # elif isVt1Blank == True and isVt2Blank == True and isVt3Blank == False and isVt4Blank == True and isVt5Blank == True and isVt6Blank == True and tempDfVt3["Process 3 Repaired Action"].values[0] != "-":
            #         print("Pending Repair At Process 3")
            #         canCompile = False
            # elif isVt1Blank == True and isVt2Blank == True and isVt3Blank == False and isVt4Blank == False and isVt5Blank == True and isVt6Blank == True and tempDfVt3["Process 3 Repaired Action"].values[0] != "-":
            #         print("Pending Repair At Process 3, Process 4")
            #         canCompile = False
            # elif isVt1Blank == True and isVt2Blank == True and isVt3Blank == False and isVt4Blank == False and isVt5Blank == False and isVt6Blank == True and tempDfVt3["Process 3 Repaired Action"].values[0] != "-":
            #         print("Pending Repair At Process 3, Process 4, Process 5")
            #         canCompile = False
            # elif isVt1Blank == True and isVt2Blank == True and isVt3Blank == False and isVt4Blank == False and isVt5Blank == False and isVt6Blank == False and tempDfVt3["Process 3 Repaired Action"].values[0] != "-":
            #         process3Status = "Repaired"
            #         canCompile = True
            # #Repair Process 4
            # elif isVt1Blank == True and isVt2Blank == True and isVt3Blank == True and isVt4Blank == False and isVt5Blank == True and isVt6Blank == True and tempDfVt4["Process 4 Repaired Action"].values[0] != "-":
            #         print("Pending Repair At Process 4")
            #         canCompile = False
            # elif isVt1Blank == True and isVt2Blank == True and isVt3Blank == True and isVt4Blank == False and isVt5Blank == False and isVt6Blank == True and tempDfVt4["Process 4 Repaired Action"].values[0] != "-":
            #         print("Pending Repair At Process 4, Process 5")
            #         canCompile = False
            # elif isVt1Blank == True and isVt2Blank == True and isVt3Blank == True and isVt4Blank == False and isVt5Blank == False and isVt6Blank == False and tempDfVt4["Process 4 Repaired Action"].values[0] != "-":
            #         process4Status = "Repaired"
            #         canCompile = True
            # #Repair Process 5
            # elif isVt1Blank == True and isVt2Blank == True and isVt3Blank == True and isVt4Blank == True and isVt5Blank == False and isVt6Blank == True and tempDfVt5["Process 5 Repaired Action"].values[0] != "-":
            #         print("Pending Repair At Process 5")
            #         canCompile = False
            # elif isVt1Blank == True and isVt2Blank == True and isVt3Blank == True and isVt4Blank == True and isVt5Blank == False and isVt6Blank == False and tempDfVt5["Process 5 Repaired Action"].values[0] != "-":
            #         process5Status = "Repaired"
            #         canCompile = True
            # #Repair Process 6
            # elif isVt1Blank == True and isVt2Blank == True and isVt3Blank == True and isVt4Blank == True and isVt5Blank == True and isVt6Blank == False and tempDfVt6["Process 6 Repaired Action"].values[0] != "-":
            #         process6Status = "Repaired"
            #         canCompile = True
            # else:
            #     canCompile = False

            if not canCompile:
                programRunning = False

            # print("Program Stopped")
            # programRunning = False
            # canCompile = False

def ReadPreviousDateAndTime():
    global previousDate
    global previousTime

    piRowDiff = 1
    while True:
        try:
            previousTempDfPiRow = PiMachineManager.dfPi.iloc[[PiMachineManager.piRow - piRowDiff], :]

            previousDate = previousTempDfPiRow["DATE"].values

            previousTime = previousTempDfPiRow["TIME"].values[0]
            previousTime = datetime2.strptime(previousTime, "%H:%M:%S")
            previousTime = previousTime + timedelta(seconds=1)
            previousTime = previousTime.strftime("%H:%M:%S")

            break
        except:
            piRowDiff += 2

def CompileCsv():
    global excelData
    global compiledFrame

    global process1Row
    global process2Row
    global process3Row
    global process4Row
    global process5Row
    global process6Row

    global process1Status
    global process2Status
    global process3Status
    global process4Status
    global process5Status
    global process6Status
    global isRepairedWithNG
    global piStatus

    #GETTING DATE TODAY
    DateAndTimeManager.GetDateToday()

    # GETTING EM2P INSPECTION DATA
    Em2pVer2.ReadInspectionData(tempDfVt1["Process 1 Em2p"].values[0], tempDfVt1["Process 1 Em2p Lot No"].values[0])

    #GETTING EM3P INSPECTION DATA
    Em3pVer2.ReadInspectionData(tempDfVt1["Process 1 Em3p"].values[0], tempDfVt1["Process 1 Em3p Lot No"].values[0])

    #GETTING FM INSPECTION DATA
    FmVer2.ReadInspectionData(tempDfVt1["Process 1 Frame"].values[0], tempDfVt1["Process 1 Frame Lot No"].values[0])

    #GETTING DFB INSPECTION DATA
    DfbVer2.ReadDfbSnap(tempDfVt2["Process 2 Df Blk"].values[0], tempDfVt2["Process 2 Df Blk Lot No"].values[0])
    DfbVer2.ReadInspectionData(tempDfVt2["Process 2 Df Blk"].values[0])
    DfbVer2.ReadTensileData(tempDfVt2["Process 2 Df Blk"].values[0])

    #GETTING TENSILE FOR DFB
    tensile = Tensile()
    # tensile.GettingData(tempDfVt2["Process 2 Df Blk"].values[0], dfb.dfbLotNumber2[:-3])

    #GETTING RDB INSPECTION DATA
    RdbVer2.ReadCheckSheet(tempDfVt2["Process 2 Rod Blk Lot No"].values[0], tempDfVt2["Process 2 Rod Blk"].values)
    RdbVer2.ReadInspectionData()

    #GETTING CSB INSPECTION DATA
    CsbVer2.ReadInspectionData(tempDfVt3["Process 3 Casing Block"].values[0], tempDfVt3["Process 3 Casing Block Lot No"].values[0])

    excelData = {
        # "DATETIME": pd.to_datetime(PiMachineManager.tempdfPi['DATE'] + ' ' + PiMachineManager.tempdfPi['TIME']),
        "DATETIME": "",
        "DATE": PiMachineManager.tempdfPi["DATE"].values,
        "TIME": PiMachineManager.tempdfPi["TIME"].values,
        "MODEL CODE": PiMachineManager.tempdfPi["MODEL_CODE"].str.replace('"', '', regex=False),
        "PROCESS S/N": PiMachineManager.tempdfPi["PROCESS_S_N"].values,
        "S/N": PiMachineManager.tempdfPi["S_N"].values,
        "PASS/NG": PiMachineManager.tempdfPi["PASS_NG"].values,
        "VOLTAGE MAX (V)": PiMachineManager.tempdfPi["VOLTAGE_MAX_V"].values,
        "WATTAGE MAX (W)": PiMachineManager.tempdfPi["WATTAGE_MAX_W"].values,
        "CLOSED PRESSURE_MAX (kPa)": PiMachineManager.tempdfPi["CLOSED_PRESSURE_MAX_kPa"].values,
        "VOLTAGE Middle (V)": PiMachineManager.tempdfPi["VOLTAGE_Middle_V"].values,
        "WATTAGE Middle (W)": PiMachineManager.tempdfPi["WATTAGE_Middle_W"].values,
        "AMPERAGE Middle (A)": PiMachineManager.tempdfPi["AMPERAGE_Middle_A"].values,
        "CLOSED PRESSURE Middle (kPa)": PiMachineManager.tempdfPi["CLOSED_PRESSURE_Middle_kPa"].values,
        "VOLTAGE MIN (V)": PiMachineManager.tempdfPi["VOLTAGE_MIN_V"].values,
        "WATTAGE MIN (W)": PiMachineManager.tempdfPi["WATTAGE_MIN_W"].values,
        "CLOSED PRESSURE MIN (kPa)": PiMachineManager.tempdfPi["CLOSED_PRESSURE_MIN_kPa"].values,

        "Process 1 S/N": tempDfVt1["Process 1 S/N"].values,
        "Process 1 ID": tempDfVt1["Process 1 ID"].values,
        "Process 1 NAME": tempDfVt1["Process 1 NAME"].values,
        "Process 1 Em2p": tempDfVt1["Process 1 Em2p"].values,
        "Process 1 Em2p Lot No": tempDfVt1["Process 1 Em2p Lot No"].values,
        "Process 1 Em2p Inspection 3 Average Data": Em2pVer2.totalAverage3,
        "Process 1 Em2p Inspection 4 Average Data": Em2pVer2.totalAverage4,
        "Process 1 Em2p Inspection 5 Average Data": Em2pVer2.totalAverage5,
        "Process 1 Em2p Inspection 10 Average Data": Em2pVer2.totalAverage10,
        "Process 1 Em2p Inspection 3 Median Data": "",
        "Process 1 Em2p Inspection 4 Median Data": "",
        "Process 1 Em2p Inspection 5 Median Data": "",
        "Process 1 Em3p": tempDfVt1["Process 1 Em3p"].values,
        "Process 1 Em3p Lot No": tempDfVt1["Process 1 Em3p Lot No"].values,
        "Process 1 Em3p Inspection 3 Average Data": Em3pVer2.totalAverage3,
        "Process 1 Em3p Inspection 4 Average Data": Em3pVer2.totalAverage4,
        "Process 1 Em3p Inspection 5 Average Data": Em3pVer2.totalAverage5,
        "Process 1 Em3p Inspection 10 Average Data": Em3pVer2.totalAverage10,
        "Process 1 Em3p Inspection 3 Median Data": "",
        "Process 1 Em3p Inspection 4 Median Data": "",
        "Process 1 Em3p Inspection 5 Median Data": "",
        "Process 1 Harness": tempDfVt1["Process 1 Harness"].values,
        "Process 1 Harness Lot No": tempDfVt1["Process 1 Harness Lot No"].values,
        "Process 1 Frame": tempDfVt1["Process 1 Frame"].values,
        "Process 1 Frame Lot No": tempDfVt1["Process 1 Frame Lot No"].values,
        "Process 1 Frame Inspection 1 Average Data": FmVer2.totalAverage1, 
        "Process 1 Frame Inspection 2 Average Data": FmVer2.totalAverage2, 
        "Process 1 Frame Inspection 3 Average Data": FmVer2.totalAverage3, 
        "Process 1 Frame Inspection 4 Average Data": FmVer2.totalAverage4, 
        "Process 1 Frame Inspection 5 Average Data": FmVer2.totalAverage5, 
        "Process 1 Frame Inspection 6 Average Data": FmVer2.totalAverage6, 
        "Process 1 Frame Inspection 7 Average Data": FmVer2.totalAverage7, 
        "Process 1 Frame Inspection 1 Median Data": "", 
        "Process 1 Frame Inspection 2 Median Data": "", 
        "Process 1 Frame Inspection 3 Median Data": "", 
        "Process 1 Frame Inspection 4 Median Data": "", 
        "Process 1 Frame Inspection 5 Median Data": "", 
        "Process 1 Frame Inspection 6 Median Data": "", 
        "Process 1 Frame Inspection 7 Median Data": "", 
        "Process 1 Bushing": tempDfVt1["Process 1 Bushing"].values,
        "Process 1 Bushing Lot No": tempDfVt1["Process 1 Bushing Lot No"].values,
        "Process 1 ST": tempDfVt1["Process 1 ST"].values,
        "Process 1 Actual Time": tempDfVt1["Process 1 Actual Time"].values,
        "Process 1 NG Cause": tempDfVt1["Process 1 NG Cause"].values,
        "Process 1 Repaired Action": tempDfVt1["Process 1 Repaired Action"].values,

        "Process 2 S/N": tempDfVt2["Process 2 S/N"].values,
        "Process 2 ID": tempDfVt2["Process 2 ID"].values,
        "Process 2 NAME": tempDfVt2["Process 2 NAME"].values,
        "Process 2 M4x40 Screw": tempDfVt2["Process 2 M4x40 Screw"].values,
        "Process 2 M4x40 Screw Lot No": tempDfVt2["Process 2 M4x40 Screw Lot No"].values,
        "Process 2 Rod Blk": tempDfVt2["Process 2 Rod Blk"].values,
        "Process 2 Rod Blk Lot No": tempDfVt2["Process 2 Rod Blk Lot No"].values,
        "Process 2 Rod Blk Tesla 1 Average Data": RdbVer2.rdbTeslaTotalAverage1,
        "Process 2 Rod Blk Tesla 2 Average Data": RdbVer2.rdbTeslaTotalAverage2,
        "Process 2 Rod Blk Tesla 3 Average Data": RdbVer2.rdbTeslaTotalAverage3,
        "Process 2 Rod Blk Tesla 4 Average Data": RdbVer2.rdbTeslaTotalAverage4,
        "Process 2 Rod Blk Tesla 1 Median Data": "",
        "Process 2 Rod Blk Tesla 2 Median Data": "",
        "Process 2 Rod Blk Tesla 3 Median Data": "",
        "Process 2 Rod Blk Tesla 4 Median Data": "",
        "Process 2 Rod Blk Inspection 1 Average Data": RdbVer2.rdbTotalAverage1,
        "Process 2 Rod Blk Inspection 2 Average Data": RdbVer2.rdbTotalAverage2,
        "Process 2 Rod Blk Inspection 3 Average Data": RdbVer2.rdbTotalAverage3,
        "Process 2 Rod Blk Inspection 4 Average Data": RdbVer2.rdbTotalAverage4,
        "Process 2 Rod Blk Inspection 5 Average Data": RdbVer2.rdbTotalAverage5,
        "Process 2 Rod Blk Inspection 6 Average Data": RdbVer2.rdbTotalAverage6,
        "Process 2 Rod Blk Inspection 7 Average Data": RdbVer2.rdbTotalAverage7,
        "Process 2 Rod Blk Inspection 8 Average Data": RdbVer2.rdbTotalAverage8,
        "Process 2 Rod Blk Inspection 9 Average Data": RdbVer2.rdbTotalAverage9,
        "Process 2 Rod Blk Inspection 1 Median Data": "",
        "Process 2 Rod Blk Inspection 2 Median Data": "",
        "Process 2 Rod Blk Inspection 3 Median Data": "",
        "Process 2 Rod Blk Inspection 4 Median Data": "",
        "Process 2 Rod Blk Inspection 5 Median Data": "",
        "Process 2 Rod Blk Inspection 6 Median Data": "",
        "Process 2 Rod Blk Inspection 7 Median Data": "",
        "Process 2 Rod Blk Inspection 8 Median Data": "",
        "Process 2 Rod Blk Inspection 9 Median Data": "",
        "Process 2 Df Blk": tempDfVt2["Process 2 Df Blk"].values,
        "Process 2 Df Blk Lot No": tempDfVt2["Process 2 Df Blk Lot No"].values,
        "Process 2 Df Blk Inspection 1 Average Data": DfbVer2.totalAverage1,
        "Process 2 Df Blk Inspection 2 Average Data": DfbVer2.totalAverage2,
        "Process 2 Df Blk Inspection 3 Average Data": DfbVer2.totalAverage3,
        "Process 2 Df Blk Inspection 4 Average Data": DfbVer2.totalAverage4,
        "Process 2 Df Blk Inspection 1 Median Data": "",
        "Process 2 Df Blk Inspection 2 Median Data": "",
        "Process 2 Df Blk Inspection 3 Median Data": "",
        "Process 2 Df Blk Inspection 4 Median Data": "",
        "Process 2 Df Blk Tensile Rate Of Change Average" : DfbVer2.rateOfChangeTotalAverage,
        "Process 2 Df Blk Tensile Rate Of Change Median" : "",
        "Process 2 Df Blk Tensile Start Force Average" : DfbVer2.startForceTotalAverage,
        "Process 2 Df Blk Tensile Start Force Median" : "",
        "Process 2 Df Blk Tensile Terminating Force Average" : DfbVer2.terminatingForceTotalAverage,
        "Process 2 Df Blk Tensile Terminating Force Median" : "",
        "Process 2 Df Ring": tempDfVt2["Process 2 Df Ring"].values,
        "Process 2 Df Ring Lot No": tempDfVt2["Process 2 Df Ring Lot No"].values,
        "Process 2 Washer": tempDfVt2["Process 2 Washer"].values,
        "Process 2 Washer Lot No": tempDfVt2["Process 2 Washer Lot No"].values,
        "Process 2 Lock Nut": tempDfVt2["Process 2 Lock Nut"].values,
        "Process 2 Lock Nut Lot No": tempDfVt2["Process 2 Lock Nut Lot No"].values,
        "Process 2 ST": tempDfVt2["Process 2 ST"].values,
        "Process 2 Actual Time": tempDfVt2["Process 2 Actual Time"].values,
        "Process 2 NG Cause": tempDfVt2["Process 2 NG Cause"].values,
        "Process 2 Repaired Action": tempDfVt2["Process 2 Repaired Action"].values,

        "Process 3 S/N": tempDfVt3["Process 3 S/N"].values,
        "Process 3 ID": tempDfVt3["Process 3 ID"].values,
        "Process 3 NAME": tempDfVt3["Process 3 NAME"].values,
        "Process 3 Frame Gasket": tempDfVt3["Process 3 Frame Gasket"].values,
        "Process 3 Frame Gasket Lot No": tempDfVt3["Process 3 Frame Gasket Lot No"].values,
        "Process 3 Casing Block": tempDfVt3["Process 3 Casing Block"].values,
        "Process 3 Casing Block Lot No": tempDfVt3["Process 3 Casing Block Lot No"].values,
        "Process 3 Casing Block Inspection 1 Average Data": CsbVer2.totalAverage1,
        "Process 3 Casing Block Inspection 1 Median Data": "",
        "Process 3 Casing Gasket": tempDfVt3["Process 3 Casing Gasket"].values,
        "Process 3 Casing Gasket Lot No": tempDfVt3["Process 3 Casing Gasket Lot No"].values,
        "Process 3 M4x16 Screw 1": tempDfVt3["Process 3 M4x16 Screw 1"].values,
        "Process 3 M4x16 Screw 1 Lot No": tempDfVt3["Process 3 M4x16 Screw 1 Lot No"].values,
        "Process 3 M4x16 Screw 2": tempDfVt3["Process 3 M4x16 Screw 2"].values,
        "Process 3 M4x16 Screw 2 Lot No": tempDfVt3["Process 3 M4x16 Screw 2 Lot No"].values,
        "Process 3 Ball Cushion": tempDfVt3["Process 3 Ball Cushion"].values,
        "Process 3 Ball Cushion Lot No": tempDfVt3["Process 3 Ball Cushion Lot No"].values,
        "Process 3 Frame Cover": tempDfVt3["Process 3 Frame Cover"].values,
        "Process 3 Frame Cover Lot No": tempDfVt3["Process 3 Frame Cover Lot No"].values,
        "Process 3 Partition Board": tempDfVt3["Process 3 Partition Board"].values,
        "Process 3 Partition Board Lot No": tempDfVt3["Process 3 Partition Board Lot No"].values,
        "Process 3 Built In Tube 1": tempDfVt3["Process 3 Built In Tube 1"].values,
        "Process 3 Built In Tube 1 Lot No": tempDfVt3["Process 3 Built In Tube 1 Lot No"].values,
        "Process 3 Built In Tube 2": tempDfVt3["Process 3 Built In Tube 2"].values,
        "Process 3 Built In Tube 2 Lot No": tempDfVt3["Process 3 Built In Tube 2 Lot No"].values,
        "Process 3 Head Cover": tempDfVt3["Process 3 Head Cover"].values,
        "Process 3 Head Cover Lot No": tempDfVt3["Process 3 Head Cover Lot No"].values,
        "Process 3 Casing Packing": tempDfVt3["Process 3 Casing Packing"].values,
        "Process 3 Casing Packing Lot No": tempDfVt3["Process 3 Casing Packing Lot No"].values,
        "Process 3 M4x12 Screw": tempDfVt3["Process 3 M4x12 Screw"].values,
        "Process 3 M4x12 Screw Lot No": tempDfVt3["Process 3 M4x12 Screw Lot No"].values,
        "Process 3 Csb L": tempDfVt3["Process 3 Csb L"].values,
        "Process 3 Csb L Lot No": tempDfVt3["Process 3 Csb L Lot No"].values,
        "Process 3 Csb R": tempDfVt3["Process 3 Csb R"].values,
        "Process 3 Csb R Lot No": tempDfVt3["Process 3 Csb R Lot No"].values,
        "Process 3 Head Packing": tempDfVt3["Process 3 Head Packing"].values,
        "Process 3 Head Packing Lot No": tempDfVt3["Process 3 Head Packing Lot No"].values,
        "Process 3 ST": tempDfVt3["Process 3 ST"].values,
        "Process 3 Actual Time": tempDfVt3["Process 3 Actual Time"].values,
        "Process 3 NG Cause": tempDfVt3["Process 3 NG Cause"].values,
        "Process 3 Repaired Action": tempDfVt3["Process 3 Repaired Action"].values,

        "Process 4 S/N": tempDfVt4["Process 4 S/N"].values,
        "Process 4 ID": tempDfVt4["Process 4 ID"].values,
        "Process 4 NAME": tempDfVt4["Process 4 NAME"].values,
        "Process 4 Tank": tempDfVt4["Process 4 Tank"].values,
        "Process 4 Tank Lot No": tempDfVt4["Process 4 Tank Lot No"].values,
        "Process 4 Upper Housing": tempDfVt4["Process 4 Upper Housing"].values,
        "Process 4 Upper Housing Lot No": tempDfVt4["Process 4 Upper Housing Lot No"].values,
        "Process 4 Cord Hook": tempDfVt4["Process 4 Cord Hook"].values,
        "Process 4 Cord Hook Lot No": tempDfVt4["Process 4 Cord Hook Lot No"].values,
        "Process 4 M4x16 Screw": tempDfVt4["Process 4 M4x16 Screw"].values,
        "Process 4 M4x16 Screw Lot No": tempDfVt4["Process 4 M4x16 Screw Lot No"].values,
        "Process 4 Tank Gasket": tempDfVt4["Process 4 Tank Gasket"].values,
        "Process 4 Tank Gasket Lot No": tempDfVt4["Process 4 Tank Gasket Lot No"].values,
        "Process 4 Tank Cover": tempDfVt4["Process 4 Tank Cover"].values,
        "Process 4 Tank Cover Lot No": tempDfVt4["Process 4 Tank Cover Lot No"].values,
        "Process 4 Housing Gasket": tempDfVt4["Process 4 Housing Gasket"].values,
        "Process 4 Housing Gasket Lot No": tempDfVt4["Process 4 Housing Gasket Lot No"].values,
        "Process 4 M4x40 Screw": tempDfVt4["Process 4 M4x40 Screw"].values,
        "Process 4 M4x40 Screw Lot No": tempDfVt4["Process 4 M4x40 Screw Lot No"].values,
        "Process 4 PartitionGasket": tempDfVt4["Process 4 PartitionGasket"].values,
        "Process 4 PartitionGasket Lot No": tempDfVt4["Process 4 PartitionGasket Lot No"].values,
        "Process 4 M4x12 Screw": tempDfVt4["Process 4 M4x12 Screw"].values,
        "Process 4 M4x12 Screw Lot No": tempDfVt4["Process 4 M4x12 Screw Lot No"].values,
        "Process 4 Muffler": tempDfVt4["Process 4 Muffler"].values,
        "Process 4 Muffler Lot No": tempDfVt4["Process 4 Muffler Lot No"].values,
        "Process 4 Muffler Gasket": tempDfVt4["Process 4 Muffler Gasket"].values,
        "Process 4 Muffler Gasket Lot No": tempDfVt4["Process 4 Muffler Gasket Lot No"].values,
        "Process 4 VCR": tempDfVt4["Process 4 VCR"].values,
        "Process 4 VCR Lot No": tempDfVt4["Process 4 VCR Lot No"].values,
        "Process 4 ST": tempDfVt4["Process 4 ST"].values,
        "Process 4 Actual Time": tempDfVt4["Process 4 Actual Time"].values,
        "Process 4 NG Cause": tempDfVt4["Process 4 NG Cause"].values,
        "Process 4 Repaired Action": tempDfVt4["Process 4 Repaired Action"].values,
        
        "Process 5 S/N": tempDfVt5["Process 5 S/N"].values,
        "Process 5 ID": tempDfVt5["Process 5 ID"].values,
        "Process 5 NAME": tempDfVt5["Process 5 NAME"].values,
        "Process 5 Rating Label": tempDfVt5["Process 5 Rating Label"].values,
        "Process 5 Rating Label Lot No": tempDfVt5["Process 5 Rating Label Lot No"].values,
        "Process 5 ST": tempDfVt5["Process 5 ST"].values,
        "Process 5 Actual Time": tempDfVt5["Process 5 Actual Time"].values,
        "Process 5 NG Cause": tempDfVt5["Process 5 NG Cause"].values,
        "Process 5 Repaired Action": tempDfVt5["Process 5 Repaired Action"].values,
        
        "Process 6 S/N": tempDfVt6["Process 6 S/N"].values,
        "Process 6 ID": tempDfVt6["Process 6 ID"].values,
        "Process 6 NAME": tempDfVt6["Process 6 NAME"].values,
        "Process 6 Vinyl": tempDfVt6["Process 6 Vinyl"].values,
        "Process 6 Vinyl Lot No": tempDfVt6["Process 6 Vinyl Lot No"].values,
        "Process 6 ST": tempDfVt6["Process 6 ST"].values,
        "Process 6 Actual Time": tempDfVt6["Process 6 Actual Time"].values,
        "Process 6 NG Cause": tempDfVt6["Process 6 NG Cause"].values,
        "Process 6 Repaired Action": tempDfVt6["Process 6 Repaired Action"].values,

        "Process 1 SERIAL NO" : tempDfVt1["Process 1 S/N"].values,
        "Process 2 SERIAL NO" : tempDfVt2["Process 2 S/N"].values,
        "Process 3 SERIAL NO" : tempDfVt3["Process 3 S/N"].values,
        "Process 4 SERIAL NO" : tempDfVt4["Process 4 S/N"].values,
        "Process 5 SERIAL NO" : tempDfVt5["Process 5 S/N"].values,
        "Process 6 SERIAL NO" : tempDfVt6["Process 6 S/N"].values
    }
    excelData = pd.DataFrame(excelData)

    try:
        excelData["DATETIME"] = pd.to_datetime(PiMachineManager.tempdfPi['DATE'].values + ' ' + PiMachineManager.tempdfPi['TIME'].values)
    except:
        pass

    if piStatus == "INSPECTION ONLY":
        PiMachineManager.piRow += 1

        for column in ColumnCreator.process1Column:
            excelData[column] = piStatus
        for column in ColumnCreator.process2Column:
            excelData[column] = piStatus
        for column in ColumnCreator.process3Column:
            excelData[column] = piStatus
        for column in ColumnCreator.process4Column:
            excelData[column] = piStatus
        for column in ColumnCreator.process5Column:
            excelData[column] = piStatus
        for column in ColumnCreator.process6Column:
            excelData[column] = piStatus

        excelData["Process 1 SERIAL NO"] = piStatus
        excelData["Process 2 SERIAL NO"] = piStatus
        excelData["Process 3 SERIAL NO"] = piStatus
        excelData["Process 4 SERIAL NO"] = piStatus
        excelData["Process 5 SERIAL NO"] = piStatus
        excelData["Process 6 SERIAL NO"] = piStatus
    else:
        if process1Status == "Good":
            process1Row += 1
        if process2Status == "Good":
            process2Row += 1
        if process3Status == "Good":
            process3Row += 1
        if process4Status == "Good":
            process4Row += 1
        if process5Status == "Good":
            process5Row += 1
            PiMachineManager.piRow += 1
        if process6Status == "Good":
            process6Row += 1
            # excelData["DATETIME"] = pd.to_datetime(PiMachineManager.tempdfPi['DATE'] + ' ' + PiMachineManager.tempdfPi['TIME'])

        if isRepairedWithNG:
            if process1Status == "Repaired":
                if process2Status == "NG":
                    ReadPreviousDateAndTime()

                    ngProcess = "NG AT PROCESS2"
                    process1Row += 1
                    process2Row += 1

                    excelData["DATETIME"] = pd.to_datetime(previousDate + ' ' + previousTime)
                    excelData["DATE"] = previousDate
                    excelData["TIME"] = previousTime
                    excelData["MODEL CODE"] = ngProcess
                    excelData["PROCESS S/N"] = tempDfVt2["Process 2 S/N"].values
                    excelData["S/N"] = ngProcess
                    excelData["PASS/NG"] = ngProcess
                    excelData["VOLTAGE MAX (V)"] = ngProcess
                    excelData["WATTAGE MAX (W)"] = ngProcess
                    excelData["CLOSED PRESSURE_MAX (kPa)"] = ngProcess
                    excelData["VOLTAGE Middle (V)"] = ngProcess
                    excelData["WATTAGE Middle (W)"] = ngProcess
                    excelData["AMPERAGE Middle (A)"] = ngProcess
                    excelData["CLOSED PRESSURE Middle (kPa)"] = ngProcess
                    excelData["VOLTAGE MIN (V)"] = ngProcess
                    excelData["WATTAGE MIN (W)"] = ngProcess
                    excelData["CLOSED PRESSURE MIN (kPa)"] = ngProcess

                    for column in ColumnCreator.process3Column:
                        excelData[column] = ngProcess
                    for column in ColumnCreator.process4Column:
                        excelData[column] = ngProcess
                    for column in ColumnCreator.process5Column:
                        excelData[column] = ngProcess
                    for column in ColumnCreator.process6Column:
                        excelData[column] = ngProcess

                    # excelData["Process 1 SERIAL NO"] = ngProcess
                    # excelData["Process 2 SERIAL NO"] = ngProcess
                    excelData["Process 3 SERIAL NO"] = ngProcess
                    excelData["Process 4 SERIAL NO"] = ngProcess
                    excelData["Process 5 SERIAL NO"] = ngProcess
                    excelData["Process 6 SERIAL NO"] = ngProcess

                elif process3Status == "NG":
                    ReadPreviousDateAndTime()

                    ngProcess = "NG AT PROCESS3"
                    process1Row += 1
                    process2Row += 1
                    process3Row += 1

                    excelData["DATETIME"] = pd.to_datetime(previousDate + ' ' + previousTime)
                    excelData["DATE"] = previousDate
                    excelData["TIME"] = previousTime
                    excelData["MODEL CODE"] = ngProcess
                    excelData["PROCESS S/N"] = tempDfVt3["Process 3 S/N"].values
                    excelData["S/N"] = ngProcess
                    excelData["PASS/NG"] = ngProcess
                    excelData["VOLTAGE MAX (V)"] = ngProcess
                    excelData["WATTAGE MAX (W)"] = ngProcess
                    excelData["CLOSED PRESSURE_MAX (kPa)"] = ngProcess
                    excelData["VOLTAGE Middle (V)"] = ngProcess
                    excelData["WATTAGE Middle (W)"] = ngProcess
                    excelData["AMPERAGE Middle (A)"] = ngProcess
                    excelData["CLOSED PRESSURE Middle (kPa)"] = ngProcess
                    excelData["VOLTAGE MIN (V)"] = ngProcess
                    excelData["WATTAGE MIN (W)"] = ngProcess
                    excelData["CLOSED PRESSURE MIN (kPa)"] = ngProcess

                    for column in ColumnCreator.process4Column:
                        excelData[column] = ngProcess
                    for column in ColumnCreator.process5Column:
                        excelData[column] = ngProcess
                    for column in ColumnCreator.process6Column:
                        excelData[column] = ngProcess

                    # excelData["Process 1 SERIAL NO"] = ngProcess
                    # excelData["Process 2 SERIAL NO"] = ngProcess
                    # excelData["Process 3 SERIAL NO"] = ngProcess
                    excelData["Process 4 SERIAL NO"] = ngProcess
                    excelData["Process 5 SERIAL NO"] = ngProcess
                    excelData["Process 6 SERIAL NO"] = ngProcess

                elif process4Status == "NG":
                    ReadPreviousDateAndTime()

                    ngProcess = "NG AT PROCESS4"
                    process1Row += 1
                    process2Row += 1
                    process3Row += 1
                    process4Row += 1

                    excelData["DATETIME"] = pd.to_datetime(previousDate + ' ' + previousTime)
                    excelData["DATE"] = previousDate
                    excelData["TIME"] = previousTime
                    excelData["MODEL CODE"] = ngProcess
                    excelData["PROCESS S/N"] = tempDfVt4["Process 4 S/N"].values
                    excelData["S/N"] = ngProcess
                    excelData["PASS/NG"] = ngProcess
                    excelData["VOLTAGE MAX (V)"] = ngProcess
                    excelData["WATTAGE MAX (W)"] = ngProcess
                    excelData["CLOSED PRESSURE_MAX (kPa)"] = ngProcess
                    excelData["VOLTAGE Middle (V)"] = ngProcess
                    excelData["WATTAGE Middle (W)"] = ngProcess
                    excelData["AMPERAGE Middle (A)"] = ngProcess
                    excelData["CLOSED PRESSURE Middle (kPa)"] = ngProcess
                    excelData["VOLTAGE MIN (V)"] = ngProcess
                    excelData["WATTAGE MIN (W)"] = ngProcess
                    excelData["CLOSED PRESSURE MIN (kPa)"] = ngProcess

                    for column in ColumnCreator.process5Column:
                        excelData[column] = ngProcess
                    for column in ColumnCreator.process6Column:
                        excelData[column] = ngProcess

                    # excelData["Process 1 SERIAL NO"] = ngProcess
                    # excelData["Process 2 SERIAL NO"] = ngProcess
                    # excelData["Process 3 SERIAL NO"] = ngProcess
                    # excelData["Process 4 SERIAL NO"] = ngProcess
                    excelData["Process 5 SERIAL NO"] = ngProcess
                    excelData["Process 6 SERIAL NO"] = ngProcess

                elif process5Status == "NG PRESSURE":
                    ReadPreviousDateAndTime()

                    ngProcess = "NG PRESSURE AT PROCESS5"
                    process1Row += 1
                    process2Row += 1
                    process3Row += 1
                    process4Row += 1
                    process5Row += 1
                    PiMachineManager.piRow += 1

                    excelData["DATETIME"] = pd.to_datetime(previousDate + ' ' + previousTime)
                    excelData["DATE"] = previousDate
                    excelData["TIME"] = previousTime
                    excelData["MODEL CODE"] = ngProcess
                    # excelData["PROCESS S/N"] = ngProcess
                    excelData["S/N"] = ngProcess
                    excelData["PASS/NG"] = ngProcess
                    excelData["VOLTAGE MAX (V)"] = ngProcess
                    excelData["WATTAGE MAX (W)"] = ngProcess
                    excelData["CLOSED PRESSURE_MAX (kPa)"] = ngProcess
                    excelData["VOLTAGE Middle (V)"] = ngProcess
                    excelData["WATTAGE Middle (W)"] = ngProcess
                    excelData["AMPERAGE Middle (A)"] = ngProcess
                    excelData["CLOSED PRESSURE Middle (kPa)"] = ngProcess
                    excelData["VOLTAGE MIN (V)"] = ngProcess
                    excelData["WATTAGE MIN (W)"] = ngProcess
                    excelData["CLOSED PRESSURE MIN (kPa)"] = ngProcess

                    for column in ColumnCreator.process6Column:
                        excelData[column] = ngProcess

                    # excelData["Process 1 SERIAL NO"] = ngProcess
                    # excelData["Process 2 SERIAL NO"] = ngProcess
                    # excelData["Process 3 SERIAL NO"] = ngProcess
                    # excelData["Process 4 SERIAL NO"] = ngProcess
                    # excelData["Process 5 SERIAL NO"] = ngProcess
                    excelData["Process 6 SERIAL NO"] = ngProcess

                elif process5Status == "NG":
                    ngProcess = "NG AT PROCESS5"
                    process1Row += 1
                    process2Row += 1
                    process3Row += 1
                    process4Row += 1
                    process5Row += 1
                    PiMachineManager.piRow += 1

                    for column in ColumnCreator.process6Column:
                        excelData[column] = ngProcess

                    # excelData["Process 1 SERIAL NO"] = ngProcess
                    # excelData["Process 2 SERIAL NO"] = ngProcess
                    # excelData["Process 3 SERIAL NO"] = ngProcess
                    # excelData["Process 4 SERIAL NO"] = ngProcess
                    # excelData["Process 5 SERIAL NO"] = ngProcess
                    excelData["Process 6 SERIAL NO"] = ngProcess

                elif process6Status == "NG":
                    ngProcess = "NG AT PROCESS6"
                    process1Row += 1
                    process2Row += 1
                    process3Row += 1
                    process4Row += 1
                    process5Row += 1
                    process6Row += 1
                    PiMachineManager.piRow += 1

            elif process2Status == "Repaired":
                if process3Status == "NG":
                    ReadPreviousDateAndTime()

                    repairedProcess = "REPAIRED AT PROCESS2"
                    ngProcess = "NG AT PROCESS3"
                    process2Row += 1
                    process3Row += 1

                    excelData["DATETIME"] = pd.to_datetime(previousDate + ' ' + previousTime)
                    excelData["DATE"] = previousDate
                    excelData["TIME"] = previousTime
                    excelData["MODEL CODE"] = ngProcess
                    excelData["PROCESS S/N"] = tempDfVt3["Process 3 S/N"].values
                    excelData["S/N"] = ngProcess
                    excelData["PASS/NG"] = ngProcess
                    excelData["VOLTAGE MAX (V)"] = ngProcess
                    excelData["WATTAGE MAX (W)"] = ngProcess
                    excelData["CLOSED PRESSURE_MAX (kPa)"] = ngProcess
                    excelData["VOLTAGE Middle (V)"] = ngProcess
                    excelData["WATTAGE Middle (W)"] = ngProcess
                    excelData["AMPERAGE Middle (A)"] = ngProcess
                    excelData["CLOSED PRESSURE Middle (kPa)"] = ngProcess
                    excelData["VOLTAGE MIN (V)"] = ngProcess
                    excelData["WATTAGE MIN (W)"] = ngProcess
                    excelData["CLOSED PRESSURE MIN (kPa)"] = ngProcess

                    for column in ColumnCreator.process1Column:
                        excelData[column] = repairedProcess
                    for column in ColumnCreator.process4Column:
                        excelData[column] = ngProcess
                    for column in ColumnCreator.process5Column:
                        excelData[column] = ngProcess
                    for column in ColumnCreator.process6Column:
                        excelData[column] = ngProcess

                    excelData["Process 1 SERIAL NO"] = repairedProcess
                    # excelData["Process 2 SERIAL NO"] = ngProcess
                    # excelData["Process 3 SERIAL NO"] = ngProcess
                    excelData["Process 4 SERIAL NO"] = ngProcess
                    excelData["Process 5 SERIAL NO"] = ngProcess
                    excelData["Process 6 SERIAL NO"] = ngProcess
                    
                elif process4Status == "NG":
                    ReadPreviousDateAndTime()

                    repairedProcess = "REPAIRED AT PROCESS2"
                    ngProcess = "NG AT PROCESS4"
                    process2Row += 1
                    process3Row += 1
                    process4Row += 1

                    excelData["DATETIME"] = pd.to_datetime(previousDate + ' ' + previousTime)
                    excelData["DATE"] = previousDate
                    excelData["TIME"] = previousTime
                    excelData["MODEL CODE"] = ngProcess
                    excelData["PROCESS S/N"] = tempDfVt4["Process 4 S/N"].values
                    excelData["S/N"] = ngProcess
                    excelData["PASS/NG"] = ngProcess
                    excelData["VOLTAGE MAX (V)"] = ngProcess
                    excelData["WATTAGE MAX (W)"] = ngProcess
                    excelData["CLOSED PRESSURE_MAX (kPa)"] = ngProcess
                    excelData["VOLTAGE Middle (V)"] = ngProcess
                    excelData["WATTAGE Middle (W)"] = ngProcess
                    excelData["AMPERAGE Middle (A)"] = ngProcess
                    excelData["CLOSED PRESSURE Middle (kPa)"] = ngProcess
                    excelData["VOLTAGE MIN (V)"] = ngProcess
                    excelData["WATTAGE MIN (W)"] = ngProcess
                    excelData["CLOSED PRESSURE MIN (kPa)"] = ngProcess

                    for column in ColumnCreator.process1Column:
                        excelData[column] = repairedProcess
                    for column in ColumnCreator.process5Column:
                        excelData[column] = ngProcess
                    for column in ColumnCreator.process6Column:
                        excelData[column] = ngProcess

                    excelData["Process 1 SERIAL NO"] = repairedProcess
                    # excelData["Process 2 SERIAL NO"] = ngProcess
                    # excelData["Process 3 SERIAL NO"] = ngProcess
                    # excelData["Process 4 SERIAL NO"] = ngProcess
                    excelData["Process 5 SERIAL NO"] = ngProcess
                    excelData["Process 6 SERIAL NO"] = ngProcess

                elif process5Status == "NG PRESSURE":
                    ReadPreviousDateAndTime()

                    repairedProcess = "REPAIRED AT PROCESS2"
                    ngProcess = "NG PRESSURE AT PROCESS5"
                    process2Row += 1
                    process3Row += 1
                    process4Row += 1
                    process5Row += 1
                    PiMachineManager.piRow += 1

                    excelData["DATETIME"] = pd.to_datetime(previousDate + ' ' + previousTime)
                    excelData["DATE"] = previousDate
                    excelData["TIME"] = previousTime
                    excelData["MODEL CODE"] = ngProcess
                    # excelData["PROCESS S/N"] = tempDfVt5["Process 5 S/N"].values
                    excelData["S/N"] = ngProcess
                    excelData["PASS/NG"] = ngProcess
                    excelData["VOLTAGE MAX (V)"] = ngProcess
                    excelData["WATTAGE MAX (W)"] = ngProcess
                    excelData["CLOSED PRESSURE_MAX (kPa)"] = ngProcess
                    excelData["VOLTAGE Middle (V)"] = ngProcess
                    excelData["WATTAGE Middle (W)"] = ngProcess
                    excelData["AMPERAGE Middle (A)"] = ngProcess
                    excelData["CLOSED PRESSURE Middle (kPa)"] = ngProcess
                    excelData["VOLTAGE MIN (V)"] = ngProcess
                    excelData["WATTAGE MIN (W)"] = ngProcess
                    excelData["CLOSED PRESSURE MIN (kPa)"] = ngProcess

                    for column in ColumnCreator.process1Column:
                        excelData[column] = repairedProcess
                    for column in ColumnCreator.process6Column:
                        excelData[column] = ngProcess
                    
                    excelData["Process 1 SERIAL NO"] = repairedProcess
                    # excelData["Process 2 SERIAL NO"] = ngProcess
                    # excelData["Process 3 SERIAL NO"] = ngProcess
                    # excelData["Process 4 SERIAL NO"] = ngProcess
                    # excelData["Process 5 SERIAL NO"] = ngProcess
                    excelData["Process 6 SERIAL NO"] = ngProcess

                elif process5Status == "NG":
                    repairedProcess = "REPAIRED AT PROCESS2"
                    ngProcess = "NG AT PROCESS5"
                    process2Row += 1
                    process3Row += 1
                    process4Row += 1
                    process5Row += 1
                    PiMachineManager.piRow += 1

                    for column in ColumnCreator.process1Column:
                        excelData[column] = repairedProcess
                    for column in ColumnCreator.process6Column:
                        excelData[column] = ngProcess

                    excelData["Process 1 SERIAL NO"] = repairedProcess
                    # excelData["Process 2 SERIAL NO"] = ngProcess
                    # excelData["Process 3 SERIAL NO"] = ngProcess
                    # excelData["Process 4 SERIAL NO"] = ngProcess
                    # excelData["Process 5 SERIAL NO"] = ngProcess
                    excelData["Process 6 SERIAL NO"] = ngProcess

                elif process6Status == "NG":
                    repairedProcess = "REPAIRED AT PROCESS2"
                    
                    process2Row += 1
                    process3Row += 1
                    process4Row += 1
                    process5Row += 1
                    process6Row += 1
                    PiMachineManager.piRow += 1

                    for column in ColumnCreator.process1Column:
                        excelData[column] = repairedProcess

                    excelData["Process 1 SERIAL NO"] = repairedProcess
                    # excelData["Process 2 SERIAL NO"] = ngProcess
                    # excelData["Process 3 SERIAL NO"] = ngProcess
                    # excelData["Process 4 SERIAL NO"] = ngProcess
                    # excelData["Process 5 SERIAL NO"] = ngProcess
                    # excelData["Process 6 SERIAL NO"] = ngProcess

            elif process3Status == "Repaired":
                if process4Status == "NG":
                    ReadPreviousDateAndTime()

                    repairedProcess = "REPAIRED AT PROCESS3"
                    ngProcess = "NG AT PROCESS4"
                    process3Row += 1
                    process4Row += 1

                    excelData["DATETIME"] = pd.to_datetime(previousDate + ' ' + previousTime)
                    excelData["DATE"] = previousDate
                    excelData["TIME"] = previousTime
                    excelData["MODEL CODE"] = ngProcess
                    excelData["PROCESS S/N"] = tempDfVt4["Process 4 S/N"].values
                    excelData["S/N"] = ngProcess
                    excelData["PASS/NG"] = ngProcess
                    excelData["VOLTAGE MAX (V)"] = ngProcess
                    excelData["WATTAGE MAX (W)"] = ngProcess
                    excelData["CLOSED PRESSURE_MAX (kPa)"] = ngProcess
                    excelData["VOLTAGE Middle (V)"] = ngProcess
                    excelData["WATTAGE Middle (W)"] = ngProcess
                    excelData["AMPERAGE Middle (A)"] = ngProcess
                    excelData["CLOSED PRESSURE Middle (kPa)"] = ngProcess
                    excelData["VOLTAGE MIN (V)"] = ngProcess
                    excelData["WATTAGE MIN (W)"] = ngProcess
                    excelData["CLOSED PRESSURE MIN (kPa)"] = ngProcess

                    for column in ColumnCreator.process1Column:
                        excelData[column] = repairedProcess
                    for column in ColumnCreator.process2Column:
                        excelData[column] = repairedProcess
                    for column in ColumnCreator.process5Column:
                        excelData[column] = ngProcess
                    for column in ColumnCreator.process6Column:
                        excelData[column] = ngProcess

                    excelData["Process 1 SERIAL NO"] = repairedProcess
                    excelData["Process 2 SERIAL NO"] = repairedProcess
                    # excelData["Process 3 SERIAL NO"] = ngProcess
                    # excelData["Process 4 SERIAL NO"] = ngProcess
                    excelData["Process 5 SERIAL NO"] = ngProcess
                    excelData["Process 6 SERIAL NO"] = ngProcess

                elif process5Status == "NG PRESSURE":
                    ReadPreviousDateAndTime()

                    repairedProcess = "REPAIRED AT PROCESS3"
                    ngProcess = "NG PRESSURE AT PROCESS5"
                    process3Row += 1
                    process4Row += 1
                    process5Row += 1
                    PiMachineManager.piRow += 1

                    excelData["DATETIME"] = pd.to_datetime(previousDate + ' ' + previousTime)
                    excelData["DATE"] = previousDate
                    excelData["TIME"] = previousTime
                    excelData["MODEL CODE"] = ngProcess
                    # excelData["PROCESS S/N"] = ngProcess
                    excelData["S/N"] = ngProcess
                    excelData["PASS/NG"] = ngProcess
                    excelData["VOLTAGE MAX (V)"] = ngProcess
                    excelData["WATTAGE MAX (W)"] = ngProcess
                    excelData["CLOSED PRESSURE_MAX (kPa)"] = ngProcess
                    excelData["VOLTAGE Middle (V)"] = ngProcess
                    excelData["WATTAGE Middle (W)"] = ngProcess
                    excelData["AMPERAGE Middle (A)"] = ngProcess
                    excelData["CLOSED PRESSURE Middle (kPa)"] = ngProcess
                    excelData["VOLTAGE MIN (V)"] = ngProcess
                    excelData["WATTAGE MIN (W)"] = ngProcess
                    excelData["CLOSED PRESSURE MIN (kPa)"] = ngProcess

                    for column in ColumnCreator.process1Column:
                        excelData[column] = repairedProcess
                    for column in ColumnCreator.process2Column:
                        excelData[column] = repairedProcess
                    for column in ColumnCreator.process6Column:
                        excelData[column] = ngProcess

                    excelData["Process 1 SERIAL NO"] = repairedProcess
                    excelData["Process 2 SERIAL NO"] = repairedProcess
                    # excelData["Process 3 SERIAL NO"] = ngProcess
                    # excelData["Process 4 SERIAL NO"] = ngProcess
                    # excelData["Process 5 SERIAL NO"] = ngProcess
                    excelData["Process 6 SERIAL NO"] = ngProcess

                elif process5Status == "NG":
                    repairedProcess = "REPAIRED AT PROCESS3"
                    ngProcess = "NG AT PROCESS5"
                    process3Row += 1
                    process4Row += 1
                    process5Row += 1
                    PiMachineManager.piRow += 1

                    for column in ColumnCreator.process1Column:
                        excelData[column] = repairedProcess
                    for column in ColumnCreator.process2Column:
                        excelData[column] = repairedProcess
                    for column in ColumnCreator.process6Column:
                        excelData[column] = ngProcess

                    excelData["Process 1 SERIAL NO"] = repairedProcess
                    excelData["Process 2 SERIAL NO"] = repairedProcess
                    # excelData["Process 3 SERIAL NO"] = ngProcess
                    # excelData["Process 4 SERIAL NO"] = ngProcess
                    # excelData["Process 5 SERIAL NO"] = ngProcess
                    excelData["Process 6 SERIAL NO"] = ngProcess

                elif process6Status == "NG":
                    repairedProcess = "REPAIRED AT PROCESS3"
                    ngProcess = "NG AT PROCESS6"
                    process3Row += 1
                    process4Row += 1
                    process5Row += 1
                    process6Row += 1
                    PiMachineManager.piRow += 1

                    for column in ColumnCreator.process1Column:
                        excelData[column] = repairedProcess
                    for column in ColumnCreator.process2Column:
                        excelData[column] = repairedProcess

                    excelData["Process 1 SERIAL NO"] = repairedProcess
                    excelData["Process 2 SERIAL NO"] = repairedProcess
                    # excelData["Process 3 SERIAL NO"] = ngProcess
                    # excelData["Process 4 SERIAL NO"] = ngProcess
                    # excelData["Process 5 SERIAL NO"] = ngProcess
                    # excelData["Process 6 SERIAL NO"] = ngProcess

            elif process4Status == "Repaired":
                if process5Status == "NG PRESSURE":
                    ReadPreviousDateAndTime()

                    repairedProcess = "REPAIRED AT PROCESS4"
                    ngProcess = "NG PRESSURE AT PROCESS5"
                    process4Row += 1
                    process5Row += 1
                    PiMachineManager.piRow += 1

                    excelData["DATETIME"] = pd.to_datetime(previousDate + ' ' + previousTime)
                    excelData["DATE"] = previousDate
                    excelData["TIME"] = previousTime
                    excelData["MODEL CODE"] = ngProcess
                    # excelData["PROCESS S/N"] = ngProcess
                    excelData["S/N"] = ngProcess
                    excelData["PASS/NG"] = ngProcess
                    excelData["VOLTAGE MAX (V)"] = ngProcess
                    excelData["WATTAGE MAX (W)"] = ngProcess
                    excelData["CLOSED PRESSURE_MAX (kPa)"] = ngProcess
                    excelData["VOLTAGE Middle (V)"] = ngProcess
                    excelData["WATTAGE Middle (W)"] = ngProcess
                    excelData["AMPERAGE Middle (A)"] = ngProcess
                    excelData["CLOSED PRESSURE Middle (kPa)"] = ngProcess
                    excelData["VOLTAGE MIN (V)"] = ngProcess
                    excelData["WATTAGE MIN (W)"] = ngProcess
                    excelData["CLOSED PRESSURE MIN (kPa)"] = ngProcess

                    for column in ColumnCreator.process1Column:
                        excelData[column] = repairedProcess
                    for column in ColumnCreator.process2Column:
                        excelData[column] = repairedProcess
                    for column in ColumnCreator.process3Column:
                        excelData[column] = repairedProcess
                    for column in ColumnCreator.process6Column:
                        excelData[column] = ngProcess

                    excelData["Process 1 SERIAL NO"] = repairedProcess
                    excelData["Process 2 SERIAL NO"] = repairedProcess
                    excelData["Process 3 SERIAL NO"] = repairedProcess
                    # excelData["Process 4 SERIAL NO"] = ngProcess
                    # excelData["Process 5 SERIAL NO"] = ngProcess
                    excelData["Process 6 SERIAL NO"] = ngProcess

                elif process5Status == "NG":
                    repairedProcess = "REPAIRED AT PROCESS4"
                    ngProcess = "NG AT PROCESS5"
                    process4Row += 1
                    process5Row += 1
                    PiMachineManager.piRow += 1

                    for column in ColumnCreator.process1Column:
                        excelData[column] = repairedProcess
                    for column in ColumnCreator.process2Column:
                        excelData[column] = repairedProcess
                    for column in ColumnCreator.process3Column:
                        excelData[column] = repairedProcess
                    for column in ColumnCreator.process6Column:
                        excelData[column] = ngProcess

                    excelData["Process 1 SERIAL NO"] = repairedProcess
                    excelData["Process 2 SERIAL NO"] = repairedProcess
                    excelData["Process 3 SERIAL NO"] = repairedProcess
                    # excelData["Process 4 SERIAL NO"] = ngProcess
                    # excelData["Process 5 SERIAL NO"] = ngProcess
                    excelData["Process 6 SERIAL NO"] = ngProcess
                    
                elif process6Status == "NG":
                    repairedProcess = "REPAIRED AT PROCESS4"
                    process4Row += 1
                    process5Row += 1
                    process6Row += 1
                    PiMachineManager.piRow += 1

                    for column in ColumnCreator.process1Column:
                        excelData[column] = repairedProcess
                    for column in ColumnCreator.process2Column:
                        excelData[column] = repairedProcess
                    for column in ColumnCreator.process3Column:
                        excelData[column] = repairedProcess

                    excelData["Process 1 SERIAL NO"] = repairedProcess
                    excelData["Process 2 SERIAL NO"] = repairedProcess
                    excelData["Process 3 SERIAL NO"] = repairedProcess
                    # excelData["Process 4 SERIAL NO"] = ngProcess
                    # excelData["Process 5 SERIAL NO"] = ngProcess
                    # excelData["Process 6 SERIAL NO"] = ngProcess
                    
            elif process5Status == "Repaired":
                if process6Status == "NG":
                    repairedProcess = "REPAIRED AT PROCESS5"
                    process5Row += 1
                    process6Row += 1
                    PiMachineManager.piRow += 1

                    for column in ColumnCreator.process1Column:
                        excelData[column] = repairedProcess
                    for column in ColumnCreator.process2Column:
                        excelData[column] = repairedProcess
                    for column in ColumnCreator.process3Column:
                        excelData[column] = repairedProcess
                    for column in ColumnCreator.process4Column:
                        excelData[column] = repairedProcess

                    excelData["Process 1 SERIAL NO"] = repairedProcess
                    excelData["Process 2 SERIAL NO"] = repairedProcess
                    excelData["Process 3 SERIAL NO"] = repairedProcess
                    excelData["Process 4 SERIAL NO"] = repairedProcess
                    # excelData["Process 5 SERIAL NO"] = ngProcess
                    # excelData["Process 6 SERIAL NO"] = ngProcess
                
            # elif process6Status == "Repaired":
            #     pass

            process1Status = ""
            process2Status = ""
            process3Status = ""
            process4Status = ""
            process5Status = ""
            process6Status = ""

        if process1Status == "NG":
            ReadPreviousDateAndTime()

            ngProcess = "NG AT PROCESS1"
            process1Row += 1

            excelData["DATETIME"] = pd.to_datetime(previousDate + ' ' + previousTime)
            excelData["DATE"] = previousDate
            excelData["TIME"] = previousTime
            excelData["MODEL CODE"] = ngProcess
            excelData["PROCESS S/N"] = tempDfVt1["Process 1 S/N"].values
            excelData["S/N"] = ngProcess
            excelData["PASS/NG"] = ngProcess
            excelData["VOLTAGE MAX (V)"] = ngProcess
            excelData["WATTAGE MAX (W)"] = ngProcess
            excelData["CLOSED PRESSURE_MAX (kPa)"] = ngProcess
            excelData["VOLTAGE Middle (V)"] = ngProcess
            excelData["WATTAGE Middle (W)"] = ngProcess
            excelData["AMPERAGE Middle (A)"] = ngProcess
            excelData["CLOSED PRESSURE Middle (kPa)"] = ngProcess
            excelData["VOLTAGE MIN (V)"] = ngProcess
            excelData["WATTAGE MIN (W)"] = ngProcess
            excelData["CLOSED PRESSURE MIN (kPa)"] = ngProcess

            for column in ColumnCreator.process2Column:
                excelData[column] = ngProcess
            for column in ColumnCreator.process3Column:
                excelData[column] = ngProcess
            for column in ColumnCreator.process4Column:
                excelData[column] = ngProcess
            for column in ColumnCreator.process5Column:
                excelData[column] = ngProcess
            for column in ColumnCreator.process6Column:
                excelData[column] = ngProcess

            # excelData["Process 1 SERIAL NO"] = ngProcess
            excelData["Process 2 SERIAL NO"] = ngProcess
            excelData["Process 3 SERIAL NO"] = ngProcess
            excelData["Process 4 SERIAL NO"] = ngProcess
            excelData["Process 5 SERIAL NO"] = ngProcess
            excelData["Process 6 SERIAL NO"] = ngProcess
            
        if process2Status == "NG":
            ReadPreviousDateAndTime()

            print("ng")
            ngProcess = "NG AT PROCESS2"
            process2Row += 1

            excelData["DATETIME"] = pd.to_datetime(previousDate + ' ' + previousTime)
            excelData["DATE"] = previousDate
            excelData["TIME"] = previousTime
            excelData["MODEL CODE"] = ngProcess
            excelData["PROCESS S/N"] = tempDfVt2["Process 2 S/N"].values
            excelData["S/N"] = ngProcess
            excelData["PASS/NG"] = ngProcess
            excelData["VOLTAGE MAX (V)"] = ngProcess
            excelData["WATTAGE MAX (W)"] = ngProcess
            excelData["CLOSED PRESSURE_MAX (kPa)"] = ngProcess
            excelData["VOLTAGE Middle (V)"] = ngProcess
            excelData["WATTAGE Middle (W)"] = ngProcess
            excelData["AMPERAGE Middle (A)"] = ngProcess
            excelData["CLOSED PRESSURE Middle (kPa)"] = ngProcess
            excelData["VOLTAGE MIN (V)"] = ngProcess
            excelData["WATTAGE MIN (W)"] = ngProcess
            excelData["CLOSED PRESSURE MIN (kPa)"] = ngProcess

            for column in ColumnCreator.process3Column:
                excelData[column] = ngProcess
            for column in ColumnCreator.process4Column:
                excelData[column] = ngProcess
            for column in ColumnCreator.process5Column:
                excelData[column] = ngProcess
            for column in ColumnCreator.process6Column:
                excelData[column] = ngProcess
    
            # excelData["Process 1 SERIAL NO"] = ngProcess
            # excelData["Process 2 SERIAL NO"] = ngProcess
            excelData["Process 3 SERIAL NO"] = ngProcess
            excelData["Process 4 SERIAL NO"] = ngProcess
            excelData["Process 5 SERIAL NO"] = ngProcess
            excelData["Process 6 SERIAL NO"] = ngProcess

        if process3Status == "NG":
            ReadPreviousDateAndTime()

            ngProcess = "NG AT PROCESS3"
            process3Row += 1

            excelData["DATETIME"] = pd.to_datetime(previousDate + ' ' + previousTime)
            excelData["DATE"] = previousDate
            excelData["TIME"] = previousTime
            excelData["MODEL CODE"] = ngProcess
            excelData["PROCESS S/N"] = tempDfVt3["Process 3 S/N"].values
            excelData["S/N"] = ngProcess
            excelData["PASS/NG"] = ngProcess
            excelData["VOLTAGE MAX (V)"] = ngProcess
            excelData["WATTAGE MAX (W)"] = ngProcess
            excelData["CLOSED PRESSURE_MAX (kPa)"] = ngProcess
            excelData["VOLTAGE Middle (V)"] = ngProcess
            excelData["WATTAGE Middle (W)"] = ngProcess
            excelData["AMPERAGE Middle (A)"] = ngProcess
            excelData["CLOSED PRESSURE Middle (kPa)"] = ngProcess
            excelData["VOLTAGE MIN (V)"] = ngProcess
            excelData["WATTAGE MIN (W)"] = ngProcess
            excelData["CLOSED PRESSURE MIN (kPa)"] = ngProcess

            for column in ColumnCreator.process4Column:
                excelData[column] = ngProcess
            for column in ColumnCreator.process5Column:
                excelData[column] = ngProcess
            for column in ColumnCreator.process6Column:
                excelData[column] = ngProcess

            # excelData["Process 1 SERIAL NO"] = ngProcess
            # excelData["Process 2 SERIAL NO"] = ngProcess
            # excelData["Process 3 SERIAL NO"] = ngProcess
            excelData["Process 4 SERIAL NO"] = ngProcess
            excelData["Process 5 SERIAL NO"] = ngProcess
            excelData["Process 6 SERIAL NO"] = ngProcess

        if process4Status == "NG":
            ReadPreviousDateAndTime()

            ngProcess = "NG AT PROCESS4"
            process4Row += 1

            excelData["DATETIME"] = pd.to_datetime(previousDate + ' ' + previousTime)
            excelData["DATE"] = previousDate
            excelData["TIME"] = previousTime
            excelData["MODEL CODE"] = ngProcess
            excelData["PROCESS S/N"] = tempDfVt4["Process 4 S/N"].values
            excelData["S/N"] = ngProcess
            excelData["PASS/NG"] = ngProcess
            excelData["VOLTAGE MAX (V)"] = ngProcess
            excelData["WATTAGE MAX (W)"] = ngProcess
            excelData["CLOSED PRESSURE_MAX (kPa)"] = ngProcess
            excelData["VOLTAGE Middle (V)"] = ngProcess
            excelData["WATTAGE Middle (W)"] = ngProcess
            excelData["AMPERAGE Middle (A)"] = ngProcess
            excelData["CLOSED PRESSURE Middle (kPa)"] = ngProcess
            excelData["VOLTAGE MIN (V)"] = ngProcess
            excelData["WATTAGE MIN (W)"] = ngProcess
            excelData["CLOSED PRESSURE MIN (kPa)"] = ngProcess

            for column in ColumnCreator.process5Column:
                excelData[column] = ngProcess
            for column in ColumnCreator.process6Column:
                excelData[column] = ngProcess

            # excelData["Process 1 SERIAL NO"] = ngProcess
            # excelData["Process 2 SERIAL NO"] = ngProcess
            # excelData["Process 3 SERIAL NO"] = ngProcess
            # excelData["Process 4 SERIAL NO"] = ngProcess
            excelData["Process 5 SERIAL NO"] = ngProcess
            excelData["Process 6 SERIAL NO"] = ngProcess

        if process5Status == "NG PRESSURE":
            ReadPreviousDateAndTime()

            ngProcess = "NG PRESSURE AT PROCESS5"
            process5Row += 1
            PiMachineManager.piRow += 1

            excelData["DATETIME"] = pd.to_datetime(previousDate + ' ' + previousTime)
            excelData["DATE"] = previousDate
            excelData["TIME"] = previousTime
            excelData["MODEL CODE"] = ngProcess
            # excelData["PROCESS S/N"] = ngProcess
            excelData["S/N"] = ngProcess
            excelData["PASS/NG"] = ngProcess
            excelData["VOLTAGE MAX (V)"] = ngProcess
            excelData["WATTAGE MAX (W)"] = ngProcess
            excelData["CLOSED PRESSURE_MAX (kPa)"] = ngProcess
            excelData["VOLTAGE Middle (V)"] = ngProcess
            excelData["WATTAGE Middle (W)"] = ngProcess
            excelData["AMPERAGE Middle (A)"] = ngProcess
            excelData["CLOSED PRESSURE Middle (kPa)"] = ngProcess
            excelData["VOLTAGE MIN (V)"] = ngProcess
            excelData["WATTAGE MIN (W)"] = ngProcess
            excelData["CLOSED PRESSURE MIN (kPa)"] = ngProcess

            for column in ColumnCreator.process6Column:
                excelData[column] = ngProcess

            # excelData["Process 1 SERIAL NO"] = ngProcess
            # excelData["Process 2 SERIAL NO"] = ngProcess
            # excelData["Process 3 SERIAL NO"] = ngProcess
            # excelData["Process 4 SERIAL NO"] = ngProcess
            # excelData["Process 5 SERIAL NO"] = ngProcess
            excelData["Process 6 SERIAL NO"] = ngProcess

        if process5Status == "WATER MARK":
            ReadPreviousDateAndTime()

            ngProcess = "WATER MARK AT PROCESS5"
            process5Row += 1
            PiMachineManager.piRow += 1

            excelData["DATETIME"] = pd.to_datetime(previousDate + ' ' + previousTime)
            excelData["DATE"] = previousDate
            excelData["TIME"] = previousTime
            excelData["MODEL CODE"] = ngProcess
            # excelData["PROCESS S/N"] = ngProcess
            excelData["S/N"] = ngProcess
            excelData["PASS/NG"] = ngProcess
            excelData["VOLTAGE MAX (V)"] = ngProcess
            excelData["WATTAGE MAX (W)"] = ngProcess
            excelData["CLOSED PRESSURE_MAX (kPa)"] = ngProcess
            excelData["VOLTAGE Middle (V)"] = ngProcess
            excelData["WATTAGE Middle (W)"] = ngProcess
            excelData["AMPERAGE Middle (A)"] = ngProcess
            excelData["CLOSED PRESSURE Middle (kPa)"] = ngProcess
            excelData["VOLTAGE MIN (V)"] = ngProcess
            excelData["WATTAGE MIN (W)"] = ngProcess
            excelData["CLOSED PRESSURE MIN (kPa)"] = ngProcess

            for column in ColumnCreator.process6Column:
                excelData[column] = ngProcess

            # excelData["Process 1 SERIAL NO"] = ngProcess
            # excelData["Process 2 SERIAL NO"] = ngProcess
            # excelData["Process 3 SERIAL NO"] = ngProcess
            # excelData["Process 4 SERIAL NO"] = ngProcess
            # excelData["Process 5 SERIAL NO"] = ngProcess
            excelData["Process 6 SERIAL NO"] = ngProcess

        if process5Status == "CORROSION":
            ReadPreviousDateAndTime()

            ngProcess = "CORROSION AT PROCESS5"
            process5Row += 1
            PiMachineManager.piRow += 1

            excelData["DATETIME"] = pd.to_datetime(previousDate + ' ' + previousTime)
            excelData["DATE"] = previousDate
            excelData["TIME"] = previousTime
            excelData["MODEL CODE"] = ngProcess
            # excelData["PROCESS S/N"] = ngProcess
            excelData["S/N"] = ngProcess
            excelData["PASS/NG"] = ngProcess
            excelData["VOLTAGE MAX (V)"] = ngProcess
            excelData["WATTAGE MAX (W)"] = ngProcess
            excelData["CLOSED PRESSURE_MAX (kPa)"] = ngProcess
            excelData["VOLTAGE Middle (V)"] = ngProcess
            excelData["WATTAGE Middle (W)"] = ngProcess
            excelData["AMPERAGE Middle (A)"] = ngProcess
            excelData["CLOSED PRESSURE Middle (kPa)"] = ngProcess
            excelData["VOLTAGE MIN (V)"] = ngProcess
            excelData["WATTAGE MIN (W)"] = ngProcess
            excelData["CLOSED PRESSURE MIN (kPa)"] = ngProcess

            for column in ColumnCreator.process6Column:
                excelData[column] = ngProcess

            # excelData["Process 1 SERIAL NO"] = ngProcess
            # excelData["Process 2 SERIAL NO"] = ngProcess
            # excelData["Process 3 SERIAL NO"] = ngProcess
            # excelData["Process 4 SERIAL NO"] = ngProcess
            # excelData["Process 5 SERIAL NO"] = ngProcess
            excelData["Process 6 SERIAL NO"] = ngProcess

        if process5Status == "BLACKSPOTS":
            ReadPreviousDateAndTime()

            ngProcess = "BLACKSPOTS AT PROCESS5"
            process5Row += 1
            PiMachineManager.piRow += 1

            excelData["DATETIME"] = pd.to_datetime(previousDate + ' ' + previousTime)
            excelData["DATE"] = previousDate
            excelData["TIME"] = previousTime
            excelData["MODEL CODE"] = ngProcess
            # excelData["PROCESS S/N"] = ngProcess
            excelData["S/N"] = ngProcess
            excelData["PASS/NG"] = ngProcess
            excelData["VOLTAGE MAX (V)"] = ngProcess
            excelData["WATTAGE MAX (W)"] = ngProcess
            excelData["CLOSED PRESSURE_MAX (kPa)"] = ngProcess
            excelData["VOLTAGE Middle (V)"] = ngProcess
            excelData["WATTAGE Middle (W)"] = ngProcess
            excelData["AMPERAGE Middle (A)"] = ngProcess
            excelData["CLOSED PRESSURE Middle (kPa)"] = ngProcess
            excelData["VOLTAGE MIN (V)"] = ngProcess
            excelData["WATTAGE MIN (W)"] = ngProcess
            excelData["CLOSED PRESSURE MIN (kPa)"] = ngProcess

            for column in ColumnCreator.process6Column:
                excelData[column] = ngProcess

            # excelData["Process 1 SERIAL NO"] = ngProcess
            # excelData["Process 2 SERIAL NO"] = ngProcess
            # excelData["Process 3 SERIAL NO"] = ngProcess
            # excelData["Process 4 SERIAL NO"] = ngProcess
            # excelData["Process 5 SERIAL NO"] = ngProcess
            excelData["Process 6 SERIAL NO"] = ngProcess

        if process5Status == "NG":
            ngProcess = "NG AT PROCESS5"
            process5Row += 1
            PiMachineManager.piRow += 1

            # excelData["DATE"] = ngProcess
            # excelData["TIME"] = ngProcess
            # excelData["MODEL CODE"] = ngProcess
            # excelData["PROCESS S/N"] = ngProcess
            # excelData["S/N"] = ngProcess
            # excelData["PASS/NG"] = ngProcess
            # excelData["VOLTAGE MAX (V)"] = ngProcess
            # excelData["WATTAGE MAX (W)"] = ngProcess
            # excelData["CLOSED PRESSURE_MAX (kPa)"] = ngProcess
            # excelData["VOLTAGE Middle (V)"] = ngProcess
            # excelData["WATTAGE Middle (W)"] = ngProcess
            # excelData["AMPERAGE Middle (A)"] = ngProcess
            # excelData["CLOSED PRESSURE Middle (kPa)"] = ngProcess
            # excelData["dB(A) 1"] = ngProcess
            # excelData["dB(A) 2"] = ngProcess
            # excelData["dB(A) 3"] = ngProcess
            # excelData["VOLTAGE MIN (V)"] = ngProcess
            # excelData["WATTAGE MIN (W)"] = ngProcess
            # excelData["CLOSED PRESSURE MIN (kPa)"] = ngProcess

            for column in ColumnCreator.process6Column:
                excelData[column] = ngProcess

            # excelData["Process 1 SERIAL NO"] = ngProcess
            # excelData["Process 2 SERIAL NO"] = ngProcess
            # excelData["Process 3 SERIAL NO"] = ngProcess
            # excelData["Process 4 SERIAL NO"] = ngProcess
            # excelData["Process 5 SERIAL NO"] = ngProcess
            excelData["Process 6 SERIAL NO"] = ngProcess

        if process6Status == "NG":
            ngProcess = "NG AT PROCESS6"
            process6Row += 1
            excelData["DATE"] = ngProcess
            excelData["TIME"] = ngProcess
            excelData["MODEL CODE"] = ngProcess
            excelData["PROCESS S/N"] = ngProcess
            excelData["S/N"] = ngProcess
            excelData["PASS/NG"] = ngProcess
            excelData["VOLTAGE MAX (V)"] = ngProcess
            excelData["WATTAGE MAX (W)"] = ngProcess
            excelData["CLOSED PRESSURE_MAX (kPa)"] = ngProcess
            excelData["VOLTAGE Middle (V)"] = ngProcess
            excelData["WATTAGE Middle (W)"] = ngProcess
            excelData["AMPERAGE Middle (A)"] = ngProcess
            excelData["CLOSED PRESSURE Middle (kPa)"] = ngProcess
            excelData["VOLTAGE MIN (V)"] = ngProcess
            excelData["WATTAGE MIN (W)"] = ngProcess
            excelData["CLOSED PRESSURE MIN (kPa)"] = ngProcess

        if process1Status == "Repaired":
            repairedProcess = "REPAIRED AT PROCESS1"
            process1Row += 1
            process2Row += 1
            process3Row += 1
            process4Row += 1
            process5Row += 1
            process6Row += 1
            PiMachineManager.piRow += 1

            # excelData["DATE"] = repairedProcess
            # excelData["TIME"] = repairedProcess
            # excelData["MODEL CODE"] = repairedProcess
            # excelData["PROCESS S/N"] = repairedProcess
            # excelData["S/N"] = repairedProcess
            # excelData["PASS/NG"] = repairedProcess
            # excelData["VOLTAGE MAX (V)"] = repairedProcess
            # excelData["WATTAGE MAX (W)"] = repairedProcess
            # excelData["CLOSED PRESSURE_MAX (kPa)"] = repairedProcess
            # excelData["VOLTAGE Middle (V)"] = repairedProcess
            # excelData["WATTAGE Middle (W)"] = repairedProcess
            # excelData["AMPERAGE Middle (A)"] = repairedProcess
            # excelData["CLOSED PRESSURE Middle (kPa)"] = repairedProcess
            # excelData["dB(A) 1"] = repairedProcess
            # excelData["dB(A) 2"] = repairedProcess
            # excelData["dB(A) 3"] = repairedProcess
            # excelData["VOLTAGE MIN (V)"] = repairedProcess
            # excelData["WATTAGE MIN (W)"] = repairedProcess
            # excelData["CLOSED PRESSURE MIN (kPa)"] = repairedProcess

        if process2Status == "Repaired":
            repairedProcess = "REPAIRED AT PROCESS2"
            process2Row += 1
            process3Row += 1
            process4Row += 1
            process5Row += 1
            process6Row += 1
            PiMachineManager.piRow += 1

            # excelData["DATE"] = repairedProcess
            # excelData["TIME"] = repairedProcess
            # excelData["MODEL CODE"] = repairedProcess
            # excelData["PROCESS S/N"] = repairedProcess
            # excelData["S/N"] = repairedProcess
            # excelData["PASS/NG"] = repairedProcess
            # excelData["VOLTAGE MAX (V)"] = repairedProcess
            # excelData["WATTAGE MAX (W)"] = repairedProcess
            # excelData["CLOSED PRESSURE_MAX (kPa)"] = repairedProcess
            # excelData["VOLTAGE Middle (V)"] = repairedProcess
            # excelData["WATTAGE Middle (W)"] = repairedProcess
            # excelData["AMPERAGE Middle (A)"] = repairedProcess
            # excelData["CLOSED PRESSURE Middle (kPa)"] = repairedProcess
            # excelData["dB(A) 1"] = repairedProcess
            # excelData["dB(A) 2"] = repairedProcess
            # excelData["dB(A) 3"] = repairedProcess
            # excelData["VOLTAGE MIN (V)"] = repairedProcess
            # excelData["WATTAGE MIN (W)"] = repairedProcess
            # excelData["CLOSED PRESSURE MIN (kPa)"] = repairedProcess

            for column in ColumnCreator.process1Column:
                excelData[column] = repairedProcess

            excelData["Process 1 SERIAL NO"] = repairedProcess
            # excelData["Process 2 SERIAL NO"] = repairedProcess
            # excelData["Process 3 SERIAL NO"] = repairedProcess
            # excelData["Process 4 SERIAL NO"] = repairedProcess
            # excelData["Process 5 SERIAL NO"] = repairedProcess
            # excelData["Process 6 SERIAL NO"] = repairedProcess

        if process3Status == "Repaired":
            repairedProcess = "REPAIRED AT PROCESS3"
            process3Row += 1
            process4Row += 1
            process5Row += 1
            process6Row += 1
            PiMachineManager.piRow += 1

            # excelData["DATE"] = repairedProcess
            # excelData["TIME"] = repairedProcess
            # excelData["MODEL CODE"] = repairedProcess
            # excelData["PROCESS S/N"] = repairedProcess
            # excelData["S/N"] = repairedProcess
            # excelData["PASS/NG"] = repairedProcess
            # excelData["VOLTAGE MAX (V)"] = repairedProcess
            # excelData["WATTAGE MAX (W)"] = repairedProcess
            # excelData["CLOSED PRESSURE_MAX (kPa)"] = repairedProcess
            # excelData["VOLTAGE Middle (V)"] = repairedProcess
            # excelData["WATTAGE Middle (W)"] = repairedProcess
            # excelData["AMPERAGE Middle (A)"] = repairedProcess
            # excelData["CLOSED PRESSURE Middle (kPa)"] = repairedProcess
            # excelData["dB(A) 1"] = repairedProcess
            # excelData["dB(A) 2"] = repairedProcess
            # excelData["dB(A) 3"] = repairedProcess
            # excelData["VOLTAGE MIN (V)"] = repairedProcess
            # excelData["WATTAGE MIN (W)"] = repairedProcess
            # excelData["CLOSED PRESSURE MIN (kPa)"] = repairedProcess

            for column in ColumnCreator.process1Column:
                excelData[column] = repairedProcess
            for column in ColumnCreator.process2Column:
                excelData[column] = repairedProcess

            excelData["Process 1 SERIAL NO"] = repairedProcess
            excelData["Process 2 SERIAL NO"] = repairedProcess
            # excelData["Process 3 SERIAL NO"] = repairedProcess
            # excelData["Process 4 SERIAL NO"] = repairedProcess
            # excelData["Process 5 SERIAL NO"] = repairedProcess
            # excelData["Process 6 SERIAL NO"] = repairedProcess

        if process4Status == "Repaired":
            repairedProcess = "REPAIRED AT PROCESS4"
            process4Row += 1
            process5Row += 1
            process6Row += 1
            PiMachineManager.piRow += 1

            # excelData["DATE"] = repairedProcess
            # excelData["TIME"] = repairedProcess
            # excelData["MODEL CODE"] = repairedProcess
            # excelData["PROCESS S/N"] = repairedProcess
            # excelData["S/N"] = repairedProcess
            # excelData["PASS/NG"] = repairedProcess
            # excelData["VOLTAGE MAX (V)"] = repairedProcess
            # excelData["WATTAGE MAX (W)"] = repairedProcess
            # excelData["CLOSED PRESSURE_MAX (kPa)"] = repairedProcess
            # excelData["VOLTAGE Middle (V)"] = repairedProcess
            # excelData["WATTAGE Middle (W)"] = repairedProcess
            # excelData["AMPERAGE Middle (A)"] = repairedProcess
            # excelData["CLOSED PRESSURE Middle (kPa)"] = repairedProcess
            # excelData["dB(A) 1"] = repairedProcess
            # excelData["dB(A) 2"] = repairedProcess
            # excelData["dB(A) 3"] = repairedProcess
            # excelData["VOLTAGE MIN (V)"] = repairedProcess
            # excelData["WATTAGE MIN (W)"] = repairedProcess
            # excelData["CLOSED PRESSURE MIN (kPa)"] = repairedProcess

            for column in ColumnCreator.process1Column:
                excelData[column] = repairedProcess
            for column in ColumnCreator.process2Column:
                excelData[column] = repairedProcess
            for column in ColumnCreator.process3Column:
                excelData[column] = repairedProcess

            excelData["Process 1 SERIAL NO"] = repairedProcess
            excelData["Process 2 SERIAL NO"] = repairedProcess
            excelData["Process 3 SERIAL NO"] = repairedProcess
            # excelData["Process 4 SERIAL NO"] = repairedProcess
            # excelData["Process 5 SERIAL NO"] = repairedProcess
            # excelData["Process 6 SERIAL NO"] = repairedProcess

        if process5Status == "Repaired":
            repairedProcess = "RE PI"
            process5Row += 1
            process6Row += 1
            PiMachineManager.piRow += 1

            # excelData["DATE"] = repairedProcess
            # excelData["TIME"] = repairedProcess
            # excelData["MODEL CODE"] = repairedProcess
            # excelData["PROCESS S/N"] = repairedProcess
            # excelData["S/N"] = repairedProcess
            # excelData["PASS/NG"] = repairedProcess
            # excelData["VOLTAGE MAX (V)"] = repairedProcess
            # excelData["WATTAGE MAX (W)"] = repairedProcess
            # excelData["CLOSED PRESSURE_MAX (kPa)"] = repairedProcess
            # excelData["VOLTAGE Middle (V)"] = repairedProcess
            # excelData["WATTAGE Middle (W)"] = repairedProcess
            # excelData["AMPERAGE Middle (A)"] = repairedProcess
            # excelData["CLOSED PRESSURE Middle (kPa)"] = repairedProcess
            # excelData["dB(A) 1"] = repairedProcess
            # excelData["dB(A) 2"] = repairedProcess
            # excelData["dB(A) 3"] = repairedProcess
            # excelData["VOLTAGE MIN (V)"] = repairedProcess
            # excelData["WATTAGE MIN (W)"] = repairedProcess
            # excelData["CLOSED PRESSURE MIN (kPa)"] = repairedProcess

            for column in ColumnCreator.process1Column:
                excelData[column] = repairedProcess
            for column in ColumnCreator.process2Column:
                excelData[column] = repairedProcess
            for column in ColumnCreator.process3Column:
                excelData[column] = repairedProcess
            for column in ColumnCreator.process4Column:
                excelData[column] = repairedProcess

            excelData["Process 1 SERIAL NO"] = repairedProcess
            excelData["Process 2 SERIAL NO"] = repairedProcess
            excelData["Process 3 SERIAL NO"] = repairedProcess
            excelData["Process 4 SERIAL NO"] = repairedProcess
            # excelData["Process 5 SERIAL NO"] = repairedProcess
            # excelData["Process 6 SERIAL NO"] = repairedProcess

        if process6Status == "Repaired":
            repairedProcess = "REPAIRED AT PROCESS6"
            process6Row += 1
            PiMachineManager.piRow += 1

            # excelData["DATE"] = repairedProcess
            # excelData["TIME"] = repairedProcess
            # excelData["MODEL CODE"] = repairedProcess
            # excelData["PROCESS S/N"] = repairedProcess
            # excelData["S/N"] = repairedProcess
            # excelData["PASS/NG"] = repairedProcess
            # excelData["VOLTAGE MAX (V)"] = repairedProcess
            # excelData["WATTAGE MAX (W)"] = repairedProcess
            # excelData["CLOSED PRESSURE_MAX (kPa)"] = repairedProcess
            # excelData["VOLTAGE Middle (V)"] = repairedProcess
            # excelData["WATTAGE Middle (W)"] = repairedProcess
            # excelData["AMPERAGE Middle (A)"] = repairedProcess
            # excelData["CLOSED PRESSURE Middle (kPa)"] = repairedProcess
            # excelData["dB(A) 1"] = repairedProcess
            # excelData["dB(A) 2"] = repairedProcess
            # excelData["dB(A) 3"] = repairedProcess
            # excelData["VOLTAGE MIN (V)"] = repairedProcess
            # excelData["WATTAGE MIN (W)"] = repairedProcess
            # excelData["CLOSED PRESSURE MIN (kPa)"] = repairedProcess

            for column in ColumnCreator.process1Column:
                excelData[column] = repairedProcess
            for column in ColumnCreator.process2Column:
                excelData[column] = repairedProcess
            for column in ColumnCreator.process3Column:
                excelData[column] = repairedProcess
            for column in ColumnCreator.process4Column:
                excelData[column] = repairedProcess
            for column in ColumnCreator.process5Column:
                excelData[column] = repairedProcess

            excelData["Process 1 SERIAL NO"] = repairedProcess
            excelData["Process 2 SERIAL NO"] = repairedProcess
            excelData["Process 3 SERIAL NO"] = repairedProcess
            excelData["Process 4 SERIAL NO"] = repairedProcess
            excelData["Process 5 SERIAL NO"] = repairedProcess
            # excelData["Process 6 SERIAL NO"] = repairedProcess
        
    PiMachineManager.compiledFrame = pd.concat([PiMachineManager.compiledFrame, excelData], ignore_index=True)

    # process1Status = ""
    # process2Status = ""
    # process3Status = ""
    # process4Status = ""
    # process5Status = ""
    # process6Status = ""

def ResetVariables():
    global dfVt1
    global dfVt2
    global dfVt3
    global dfVt4
    global dfVt5
    global dfVt6

    global process1Row
    global process2Row
    global process3Row
    global process4Row
    global process5Row
    global process6Row

    global tempDfVt1
    global tempDfVt2
    global tempDfVt3
    global tempDfVt4
    global tempDfVt5
    global tempDfVt6

    global ngProcess
        
    global process1Status
    global process2Status
    global process3Status
    global process4Status
    global process5Status
    global process6Status
    global isRepairedWithNG
    global piStatus

    global canCompile

    global programRunning

    global excelData
    global compiledFrame

    global previousDate
    global previousTime

    dfVt1 = ""
    dfVt2 = ""
    dfVt3 = ""
    dfVt4 = ""
    dfVt5 = ""
    dfVt6 = ""

    process1Row = 0
    process2Row = 0
    process3Row = 0
    process4Row = 0
    process5Row = 0
    process6Row = 0

    tempDfVt1 = ""
    tempDfVt2 = ""
    tempDfVt3 = ""
    tempDfVt4 = ""
    tempDfVt5 = ""
    tempDfVt6 = ""

    ngProcess = ""
        
    process1Status = ""
    process2Status = ""
    process3Status = ""
    process4Status = ""
    process5Status = ""
    process6Status = ""
    isRepairedWithNG = False
    piStatus = ""

    canCompile = False

    programRunning = True

    excelData = ""
    compiledFrame = ""

    previousDate = None
    previousTime = None
    
