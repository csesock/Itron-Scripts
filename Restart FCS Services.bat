::Stops all FCS services, waits 5 seconds, and then starts the services 
echo off
echo Stopping all Itron services...
echo...
sc stop adTempus$default
sc stop FCSAdjustHighLowLimits
sc stop FCSAdministrator
sc stop FCSAdvancedAMRExport
sc stop FCSApplyOutOfRouteReads
sc stop FCSBackupRoute
sc stop FDCommunicationService
sc stop FCSDailyAssignments
sc stop FCSDeleteRoute
sc stop FCSExport
sc stop FCSForceComplete
sc stop FCSGenerateAdvAMRRequests
sc stop FCSGenerateStatistics
sc stop FCSImport
sc stop FCSImportCommonReading
sc stop FCSImportPreprocessor
sc stop FCSIntervalDataExport
sc stop FCSLeakSensorExport
sc stop FCSOutOfRouteReadsExport
sc stop FCSRestoreRoute
sc stop FCSRouteSmartService
sc stop FCSSKMS
sc stop FCSTemporaryRouting
sc stop Itron.Mobile.FCS.MobileServices
echo All Itron services stopped
echo ...
ping 127.0.0.1 -n 6 > nul
echo Starting all Itron services...
sc start adTempus$default
sc start FCSAdjustHighLowLimits
sc start FCSAdministrator
sc start FCSAdvancedAMRExport
sc start FCSApplyOutOfRouteReads
sc start FCSBackupRoute
sc start FDCommunicationService
sc start FCSDailyAssignments
sc start FCSDeleteRoute
sc start FCSExport
sc start FCSForceComplete
sc start FCSGenerateAdvAMRRequests
sc start FCSGenerateStatistics
sc start FCSImport
sc start FCSImportCommonReading
sc start FCSImportPreprocessor
sc start FCSIntervalDataExport
sc start FCSLeakSensorExport
sc start FCSOutOfRouteReadsExport
sc start FCSRestoreRoute
sc start FCSRouteSmartService
sc start FCSSKMS
sc start FCSTemporaryRouting
sc start Itron.Mobile.FCS.MobileServices
echo Done 
PAUSE