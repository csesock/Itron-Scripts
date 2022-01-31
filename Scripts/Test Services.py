from __future__ import print_function
import psutil
import time, threading, os

itron_services = [ 
    'FCSAdjustHighLowLimits',
    'FCSAdministrator',
    'FCSAdvancedAMRExport',
    'FCSApplyOutOfRouteReads',
    'FCSBackupRoute',
    'FDCommunicationService',
    'FCSDailyAssignments',
    'FCSDeleteRoute',
    'FCSExport',
    'FCSForceComplete',
    'FCSGenerateAdvAMRRequests',
    'FCSGenerateStatistics',
    'FCSImport',
    'FCSImportCommonReading',
    'FCSImportPreprocessor',
    'FCSIntervalDataExport',
    'FCSLeakSensorExport',
    'FCSOutOfRouteReadsExport',
    'FCSRestoreRoute',
    'FCSRouteSmartService',
    'FCSSKMS',
    'FCSTemporaryRouting',
    'Itron.Mobile.FCS.MobileServices']

def getService(name):
    service = None
    try:
        service = psutil.win_service_get(name)
        service = service.as_dict()
    except Exception as ex:
        # raise psutil.NoSuchProcess if no service with such name exists
        print(str(ex))
    return service

def monitorServices():
    for service in itron_services:
        status = getService(service)['status']
        if status != 'running':
            print("Service: "+str(service)+" is not running. Status: "+status)
    threading.Timer(5, monitorServices()).start()

def main():
    #print("Service".rjust(35)+"\tStatus")
    #print("                          -------------------------")
    for service in itron_services:
        service_data = getService(service)
        print(service+" "+service_data['status'].rjust(35))
    os.system('pause')
    #monitorServices()

if __name__== "__main__":
    main()
