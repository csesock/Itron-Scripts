import os, sys, time

original = []

def getReadings(digits):
    digits = int(digits)
    try:
        with open('upload.dat', 'r') as openfile:
            with open('corrected.txt', 'w') as builtfile:
                for line in openfile:
                    if line.startswith('RDG'):
                        #original.append(line[33:43])
                        if digits == 0:
                            reading = line[33:43] #Reading N*10 Bytes 34-43
                            #print(reading)
                            original.append(reading)
                            builtfile.write(reading+'\n')
                        elif digits == 1:
                            reading = str('0')+line[33:42]
                            #print(reading)
                            builtfile.write(reading+'\n')
                        elif digits == 2:
                            reading = str('00')+line[33:41]
                            #print(reading)
                            builtfile.write(reading+'\n')
    except FileNotFoundError:
        print("Error: File Not Found")
    except:
        print("Unknown Error Exists")
                
def enterCorrectedReadings(digits):
    try:
        correct = []
        with open('corrected.txt', 'r') as cor:
            for line in cor:
                correct.append(line.strip().rstrip())
        with open('upload.dat', 'r') as openfile:
            with open('upload--corrected.dat', 'w') as builtfile:
                counter = 0
                rdg = ""    # RDG 34:43 -> 33:43
                rff = ""    # RFF 73:82 -> 72:82
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
    try:
        with open('upload--corrected.dat', 'r') as openfile:
            rdg = ""
            rff = ""
            counter = 1
            index = 0
            print("Line # \tNew Reading \tOriginal Reading")
            print("----------------------------------------------")
            for line in openfile:
                if line.startswith('RDG'):
                    rdg = line[33:43]
                if line.startswith('RFF'):
                    rff = line[72:82]
                    print(str(counter)+"\t"+rdg+"\t"+rff)
                    #print(str(counter)+'\t'+rdg+'\t'+original[index])
                counter+=1
                index+=1
    except:
        print('ERROR')

if __name__ == "__main__":
    print("Reading Adjustment Tool v0.0.1")
    #filename = input("Enter the name of the file (should be upload.dat by default): ").strip()
    digits = input("Enter the number of digits to drop from all current readings: ")
    print("Gathering adjusted readings...")
    getReadings(digits)
    
    print("Entering corrected readings into new upload file...")
    time.sleep(2)
    enterCorrectedReadings(digits)
    
    print("Corrected readings entered into new file : upload -- corrected.dat")
    answer = input("Would you like to compare adjusted readings? (Y or N): ")
    print()
    if answer.upper() == "Y":
        testReadings()
    os.system("pause")