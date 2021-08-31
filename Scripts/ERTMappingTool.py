import os

def mapERTNumber(ert_number):
    ert_number = int(ert_number)
    if ert_number < 1400000:
        print('ERT number too small')
        return
    elif ert_number >= 14000000 and ert_number < 16149999:
        return '40W'
    elif ert_number >= 16150000 and ert_number < 16273848:
        return '60W'
    elif ert_number >= 16500000 and ert_number < 18999998:
        return '40W'
    elif ert_number >= 18999999 and ert_number < 19999999:
        return '60W'
    elif ert_number >= 20000000 and ert_number < 20206987:
        return '40W'
    elif ert_number >= 202206988 and ert_number < 20851501:
        return '40W/50W'
    elif ert_number >= 21029490 and ert_number < 22909999:
        return '50W'
    elif ert_number >= 23000000 and ert_number < 23164999:
        return '50W'
    elif ert_number >= 23165000 and ert_number < 23499999:
        return '60W'
    elif ert_number >= 23500000 and ert_number < 25999999:
        return '40W/50W'
    elif ert_number >= 26000000 and ert_number < 31999999:
        return '60W'
    elif ert_number >= 32000000 and ert_number < 32499999:
        return '100W Phase 2'
    elif ert_number >= 32500000 and ert_number < 32999999:
        return 'Reserved for 100W Phase 2'
    elif ert_number >= 33000000 and ert_number < 33197976:
        return '100W Phase 3 (x.16 and older firmware)'    
    elif ert_number >= 33197977 and ert_number < 34099999:
        return '100W Phase 3 (x.17 and older firmware)'
    elif ert_number >= 34100000 and ert_number < 46000000:
        return '100W Phase 3.5'
    elif ert_number >= 46000001 and ert_number < 46499999:
        return '100W w/Leak Sensor Phase 2'
    elif ert_number >= 46500000 and ert_number < 46505670:
        return '100W w/Leak Sensor Phase 3 (x.16 and older firmware)'
    elif ert_number >= 46505671 and ert_number < 53899999:
        return '100W w/Leak Sensor Phase 3 (x.17 and newer firmware)'
    elif ert_number >= 53900000 and ert_number < 55999999:
        return '60W'
    elif ert_number >= 56000000 and ert_number < 57649999:
        return '50W'
    elif ert_number >= 57650000 and ert_number < 57999999:
        return '60W'
    elif ert_number >= 66000000 and ert_number < 66249999:
        return '50W'
    elif ert_number >= 67108700 and ert_number < 67349999:
        return 'Reserved for 100W phase 3.5'
    elif ert_number >= 67350000 and ert_number < 67399999:
        return 'Reserved for 100W phase 3.5LS'
    elif ert_number >= 67400000 and ert_number < 69499999:
        return '100W Phase 4'
    elif ert_number >= 69500000 and ert_number < 69749999:
        return '100W Phase 4 w/LS'
    elif ert_number >= 70000000 and ert_number < 78999999:
        return '100W Phase 4'
    elif ert_number >= 79000000 and ert_number < 79999999:
        return '100W Phase 4 w/LS'
    elif ert_number >79999999:
        print("ERT number too large")
        return

if __name__=='__main__':
    print("ERT Mapping Tools [version 0.0.1]")
    ert_number = input("Enter the ERT number to search: ")
    print(mapERTNumber(ert_number))
    os.system('pause')
