from __future__ import print_function

import tkinter as tk
from tkinter import ttk
import os
import psutil
import time, threading


##itron_services = [ 
##    'FCSAdjustHighLowLimits',
##    'FCSAdministrator',
##    'FCSAdvancedAMRExport',
##    'FCSApplyOutOfRouteReads',
##    'FCSBackupRoute',
##    'FDCommunicationService',
##    'FCSDailyAssignments',
##    'FCSDeleteRoute',
##    'FCSExport',
##    'FCSForceComplete',
##    'FCSGenerateAdvAMRRequests',
##    'FCSGenerateStatistics',
##    'FCSImport',
##    'FCSImportCommonReading',
##    'FCSImportPreprocessor',
##    'FCSIntervalDataExport',
##    'FCSLeakSensorExport',
##    'FCSOutOfRouteReadsExport',
##    'FCSRestoreRoute',
##    'FCSRouteSmartService',
##    'FCSSKMS',
##    'FCSTemporaryRouting',
##    'Itron.Mobile.FCS.MobileServices']

##def getServicesStatus():
##    zero_if_working = 0
##    for service in itron_services:
##        value = printService(service)
##        zero_if_working += value
##    if zero_if_working == 0:
##        status.set("Online")
##        status_output.config(fg="green")
##    elif zero_if_working > 0 and zero_if_working < len(itron_services):
##        status.set("Mixed")
##        status_output.config(fg="orange")
##    elif zero_if_working == len(itron_services):
##        status.set("Offline")
##        status_output.config(fg="red")
##    threading.Timer(3, getServicesStatus).start()

def getSingleServiceStatus(name, textvar, label):
    getService(name, textvar, label)
    threading.Timer(10, getSingleServiceStatus('FCSAdjustHighLowLimits', status1, output1)).start()

def getService(name, textvar, label):
    service = None
    try:
        service = psutil.win_service_get(name)
        service = service.as_dict()
    except Exception as ex:
        # raise psutil.NoSuchProcess if no service with such name exists
        print(str(ex))
    if service and service['status'] == 'running':
        #return 0
        textvar.set("Online")
        label.config(fg="green")
    else:
        #return 1
        textvar.set("Offline")
        label.config(fg="red")

window = tk.Tk()
window.geometry('280x520')
window.title('Itron Services Monitor')

status_label = tk.Label(text='Services: ').place(x=90, y=20)
status = tk.StringVar()
status_output = tk.Label(textvariable=status)
status_output.place(x=140, y=20)
status.set('None')

service1 = ttk.Label(text='FCSAdjustHighLowLimits').place(x=20, y=60)
service2 = ttk.Label(text='FCSAdvancedAMRExport').place(x=20, y=80)
service3 = ttk.Label(text='FCSApplyOutOfRouteReads').place(x=20, y=100)
service4 = ttk.Label(text='FCSBackupRoute').place(x=20, y=120)
service5 = ttk.Label(text='FDCommunicationService').place(x=20, y=140)
service6 = ttk.Label(text='FCSDeleteRoute').place(x=20, y=160)
service7 = ttk.Label(text='FCSExport').place(x=20, y=180)
service8 = ttk.Label(text='FCSForceComplete').place(x=20, y=200)
service9 = ttk.Label(text='FCSGenerateAdvAMRRequests').place(x=20, y=220)
service10 = ttk.Label(text='FCSGenerateStatistics').place(x=20, y=240)
service11 = ttk.Label(text='FCSImport').place(x=20, y=260)
service12 = ttk.Label(text='FCSImportCommonReading').place(x=20, y=280)
service13 = ttk.Label(text='FCSImportPreprocessor').place(x=20, y=300)
service14 = ttk.Label(text='FCSIntervalDataExport').place(x=20, y=320)
service15 = ttk.Label(text='FCSLeakSensorExport').place(x=20, y=340)
service16 = ttk.Label(text='FCSOutOfRouteReadsExport').place(x=20, y=360)
service17 = ttk.Label(text='FCSRestoreRoute').place(x=20, y=380)
service18 = ttk.Label(text='FCSRouteSmartService').place(x=20, y=400)
service19 = ttk.Label(text='FCSSKMS').place(x=20, y=420)
service20 = ttk.Label(text='FCSTemporaryRouting').place(x=20, y=440)
service21 = ttk.Label(text='Itron.Mobile.FCS.MobileServices').place(x=20, y=460)

status1 = tk.StringVar()
status2 = tk.StringVar()
status3 = tk.StringVar()
status4 = tk.StringVar()
status5 = tk.StringVar()
status6 = tk.StringVar()
status7 = tk.StringVar()
status8 = tk.StringVar()
status9 = tk.StringVar()
status10 = tk.StringVar()
status11 = tk.StringVar()
status12 = tk.StringVar()
status13 = tk.StringVar()
status14 = tk.StringVar()
status15 = tk.StringVar()
status16 = tk.StringVar()
status17 = tk.StringVar()
status18 = tk.StringVar()
status19 = tk.StringVar()
status20 = tk.StringVar()
status21 = tk.StringVar()

output1 = tk.Label(textvariable=status1)
output1.place(x=210, y=60)
status1.set("Online")

output2 = tk.Label(textvariable=status2)
output2.place(x=210, y=80)
status2.set("Online")

output3 = tk.Label(textvariable=status3)
output3.place(x=210, y=100)
status3.set("Online")

output4 = tk.Label(textvariable=status4)
output4.place(x=210, y=120)
status4.set("Online")

output5 = tk.Label(textvariable=status5)
output5.place(x=210, y=140)
status5.set("Online")

output6 = tk.Label(textvariable=status6)
output6.place(x=210, y=160)
status6.set("Online")

output7 = tk.Label(textvariable=status7)
output7.place(x=210, y=180)
status7.set("Online")

output8 = tk.Label(textvariable=status8)
output8.place(x=210, y=200)
status8.set("Online")

output9 = tk.Label(textvariable=status9)
output9.place(x=210, y=220)
status9.set("Online")

output10 = tk.Label(textvariable=status10)
output10.place(x=210, y=240)
status10.set("Online")

output11 = tk.Label(textvariable=status11)
output11.place(x=210, y=260)
status11.set("Online")

output12 = tk.Label(textvariable=status12)
output12.place(x=210, y=280)
status12.set("Online")

output13 = tk.Label(textvariable=status13)
output13.place(x=210, y=300)
status13.set("Online")

output14 = tk.Label(textvariable=status14)
output14.place(x=210, y=320)
status14.set("Online")

output15 = tk.Label(textvariable=status15)
output15.place(x=210, y=340)
status15.set("Online")

output16 = tk.Label(textvariable=status16)
output16.place(x=210, y=360)
status16.set("Online")

output17 = tk.Label(textvariable=status17)
output17.place(x=210, y=380)
status17.set("Online")

output18 = tk.Label(textvariable=status18)
output18.place(x=210, y=400)
status18.set("Online")

output19 = tk.Label(textvariable=status19)
output19.place(x=210, y=420)
status19.set("Online")

output20 = tk.Label(textvariable=status20)
output20.place(x=210, y=440)
status20.set("Online")

output21 = tk.Label(textvariable=status21)
output21.place(x=210, y=460)
status21.set("Online")

update_button = tk.Button(text="Update", command=lambda:getSingleServiceStatus('FCSAdjustHighLowLimits', status1, output1)).place(x=20, y=400)

if __name__=="__main__":
    #getServicesStatus()
    #getSingleServiceStatus('FCSAdjustHighLowLimits', status1, output1)
    window.mainloop()






