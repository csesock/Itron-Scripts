# Author: Chris Sesock on 7/30/2021
# This tool will truncate n number of digits from an upload.dat file
# and then create a new file with the corrected readings.
#
import os, sys
from time import sleep

original = []
correct = []

def getReadings(digits):
    try:
        with open('upload.dat', 'r') as openfile:
            for line in openfile:
                if line.startswith('RDG'):
                    reading = line[33:43]       #Reading N*10 Bytes 34-43
                    original.append(reading)
        for i in original:
            correct.append(str(i[:-digits]).rjust(10, '0'))
    except FileNotFoundError:
        print("Error: File Not Found")
                
def enterCorrectedReadings(digits):
    counter = 0
    try:
        with open('upload.dat', 'r') as openfile:
            with open('Upload - Corrected.dat', 'w') as builtfile:
                for line in openfile:
                    if line.startswith('RDG'):
                        line = line.replace(line[33:43], correct[counter])
                        counter+=1
                    builtfile.write(line)
    except:
        print("Unknown Error Occured")
        return

def testReadings():
    counter=1
    try:
        with open('Reading Changes.txt', 'w') as builtfile:
            builtfile.write("Line # \tOriginal Reading \tAdjusted Reading\n")
            builtfile.write("----------------------------------------------\n")
            for i in range(len(original)):
                line = str(counter)+'\t'+original[i]+'\t\t'+correct[i]+'\n'
                builtfile.write(line)
                counter+=1
    except:
        print("Unknown Error Occured")

def testReadingsExcel():
    counter = 1
    try:
        with open('Reading Changes.csv', 'w') as builtfile:
            builtfile.write('Line,Original Reading,Adjusted Reading\n')
            for i in range(len(original)):
                line = str(counter)+','+original[i]+','+correct[i]+'\n'
                builtfile.write(line)
                counter+=1
    except:
        print("Unknown Error Occured")

if __name__ == "__main__":
    print("United Systems Reading Adjustment Tool [Version 0.0.4]")
    print("(c) 2021 United Systems and Software, Inc.")
    print()
    print("Searching for Upload.dat file . . .")
    if os.path.isfile('upload.dat'):
        print("Upload.dat file found. ")
    else:
        print("Upload.dat file not found. Please place Upload.dat file in the same directory as this tool.")
        os.system("pause")
        quit()
    digits = int(input("Enter the number of digits to drop from all current readings: "))
    getReadings(digits) 
    enterCorrectedReadings(digits)
    testReadingsExcel()
    print()
    print("Corrected readings entered into new file: Upload - Corrected.dat")
    print("See 'Reading changes.txt' for reading comparisons.")
    os.system("pause")