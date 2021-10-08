from __future__ import print_function

import tkinter as tk
from tkinter import ttk
import os
import psutil
import time, threading

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

def getServicesStatus():
    zero_if_working = 0
    for service in itron_services:
        value = printService(service)
        zero_if_working += value
    if zero_if_working == 0:
        status.set("Online")
        status_output.config(fg="green")
    elif zero_if_working > 0 and zero_if_working < len(itron_services):
        status.set("Mixed")
        status_output.config(fg="orange")
    elif zero_if_working == len(itron_services):
        status.set("Offline")
        status_output.config(fg="red")
    threading.Timer(3, getServicesStatus).start()

def getService(name):
    service = None
    try:
        service = psutil.win_service_get(name)
        service = service.as_dict()
    except Exception as ex:
        # raise psutil.NoSuchProcess if no service with such name exists
        print(str(ex))

    return service

def printService(s):
    service = getService(s)
    
    if service and service['status'] == 'running':
        return 0
    else: 
        return 1

window = tk.Tk()
window.geometry('330x100')
window.title('Itron Services Monitor')

status_label = tk.Label(text='Services Status: ').place(x=100, y=30)
status = tk.StringVar()
status_output = tk.Label(textvariable=status)
status_output.place(x=190, y=30)
status.set('None')

##update_button = tk.Button(text="Update", command=lambda:getServicesStatus()).place(x=240, y=27)
##
##start_services_button = tk.Button(text="Start Services", command=lambda:startServices()).place(x=80, y=80)
##stop_services_button = tk.Button(text="Stop Services", command=lambda:stopServices()).place(x=170, y=80)

if __name__=="__main__":
    getServicesStatus()
    window.mainloop()
