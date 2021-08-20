import os

def adjustDownloadFile(record, index, value, is_space):
    try:
        with open('download.dat', 'r') as openfile:
            with open('download--adjusted.dat', 'w') as builtfile:
                for line in openfile:
                    if line.startswith(record):
                        index = int(index)
                        x = line[index-1]
                        if is_space.upper() == 'Y':
                            if x.isspace():
                                line=line[::index-1]+value+line[index::]
                        else:
                            line=line[::index-1]+value+line[index::]
                    builtfile.write(line)
    except:
        print("An unexpected error occured")

if __name__ == "__main__":
    print("United Systems Download File Adjustment Tool [Version 0.0.1]")
    print("(c) 2021 United Systems and Software, Inc.")
    print()

    print("Searching for Download.dat file . . .")
    if os.path.isfile('download.dat'):
        print("download.dat file found. ")
    else:
        print("download.dat file not found. Please place Upload.dat file in the same directory as this tool.")
        os.system("pause")
        quit()
    record = input('Enter the record in the file to be adjusted (CUS, MTR): ')
    index = input('Enter the index to adjust (10, 34): ')
    value = input('Enter the new value to be placed at that index (W, L): ')
    is_space = input('Do you want to update only if the value is currently blank? (Y or N): ')

    adjustDownloadFile(record, index, value, is_space)
    print('Adjusted download file entered into new file: download--adjusted.dat')
    
    os.system('pause')
