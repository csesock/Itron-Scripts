# Author: Chris Sesock on 7/30/2021
# This tool will truncate n number of digits from an upload.dat file
# and then create a new file with the corrected readings.
#

import os, sys
from time import sleep

original = []
correct = []

def load(n):
    for i in range(n):
        sleep(0.1)
        print(f"{i/n*100:.1f} %", end="\r")  

def getReadings(digits):
    try:
        with open('upload.dat', 'r') as openfile:
            for line in openfile:
                if line.startswith('RDG'):
                    reading = line[33:43] #Reading N*10 Bytes 34-43
                    original.append(reading)
        #with open('corrected.txt', 'w') as builtfile:
        for i in original:
            c = str(i[:-digits]).rjust(10, '0') #truncates n digits from the right of the value, pads to required length (10)
            #builtfile.write(c+'\n')
            correct.append(c)
    except FileNotFoundError:
        print("Error: File Not Found")
                
def enterCorrectedReadings(digits):
    counter = 0
    try:
        with open('upload.dat', 'r') as openfile:
            with open('upload--corrected.dat', 'w') as builtfile:
                for line in openfile:
                    if line.startswith('RDG'):
                        line = line.replace(line[33:43], correct[counter])
                        counter+=1
                    builtfile.write(line)
    except FileNotFoundError:
        print("Error: File Not Found")
    except FileExistsError:
        print("Error: File Already Exists")
    except:
        print("Unknown Error Occured")
        return

def testReadings():
    counter=1
    try:
        with open('Reading changes.txt', 'w') as builtfile:
            builtfile.write("Line # \tOriginal Reading \tAdjusted Reading\n")
            builtfile.write("----------------------------------------------\n")
            for i in range(len(original)):
                line = str(counter)+'\t'+original[i]+'\t\t'+correct[i]+'\n'
                builtfile.write(line)
                counter+=1
    except:
        print("An Error Occured")

if __name__ == "__main__":
    print("United Systems Reading Adjustment Tool [Version 0.0.3]")
    print("(c) 2021 United Systems and Software, Inc.")
    print()
    print("Searching for upload.dat file...")
    load(10)  
    if os.path.isfile('upload.dat'):
        print("Upload.dat file found. ")
    else:
        print("Upload.dat file not found. Please place upload.dat file in the same directory as this tool.")
        os.system("pause")
        quit()
    digits = int(input("Enter the number of digits to drop from all current readings: "))
    print("Gathering adjusted readings...")
    getReadings(digits)
    load(10)    
    print("Entering corrected readings into new upload file...")
    load(10)
    enterCorrectedReadings(digits)
    print("Corrected readings entered into new file : upload -- corrected.dat")
    testReadings()
    print("Readings adjusted. See 'Reading changes.txt' for reading comparisons.")
    os.system("pause")
