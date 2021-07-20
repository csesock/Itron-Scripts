echo off
ECHO Shutting down services...
echo.
sc stop adTempus$default >NUL
sc stop FCSAdjustHighLowLimits >NUL
sc stop FCSAdministrator >NUL
sc stop FCSAdvancedAMRExport >NUL
sc stop FCSApplyOutOfRouteReads >NUL
sc stop FCSBackupRoute >NUL
sc stop FDCommunicationService >NUL
sc stop FCSDailyAssignments >NUL
sc stop FCSDeleteRoute >NUL
sc stop FCSExport >NUL
sc stop FCSForceComplete >NUL
sc stop FCSGenerateAdvAMRRequests >NUL
sc stop FCSGenerateStatistics >NUL
sc stop FCSImport >NUL
sc stop FCSImportCommonReading >NUL
sc stop FCSImportPreprocessor >NUL
sc stop FCSIntervalDataExport >NUL
sc stop FCSLeakSensorExport >NUL
sc stop FCSOutOfRouteReadsExport >NUL
sc stop FCSRestoreRoute >NUL
sc stop FCSRouteSmartService >NUL
sc stop FCSSKMS >NUL
sc stop FCSTemporaryRouting >NUL
sc stop Itron.Mobile.FCS.MobileServices >NUL
echo Done
echo.
ECHO Enter username to run services 
echo.
set user=
set /p user= Type in username in the following format ^<domain\user^>:
if "%user%" == "" GOTO USERERROR
if not "%user%" == "" GOTO PASSWORD

:PASSWORD
set pass=
set /p pass=Enter the password for that user:
if "%pass%" == "" GOTO PASSERROR
if not "%pass%" == "" GOTO START

:START
sc config adTempus$default obj= %user% password= %pass%
sc config FCSAdjustHighLowLimits obj= %user% password= %pass%
sc config FCSAdministrator obj= %user% password= %pass%
sc config FCSAdvancedAMRExport obj= %user% password= %pass%
sc config FCSApplyOutOfRouteReads obj= %user% password= %pass%
sc config FCSBackupRoute obj= %user% password= %pass%
sc config FDCommunicationService obj= %user% password= %pass%
sc config FCSDailyAssignments obj= %user% password= %pass%
sc config FCSDeleteRoute obj= %user% password= %pass%
sc config FCSExport obj= %user% password= %pass%
sc config FCSForceComplete obj= %user% password= %pass%
sc config FCSGenerateAdvAMRRequests obj= %user% password= %pass%
sc config FCSGenerateStatistics obj= %user% password= %pass%
sc config FCSImport obj= %user% password= %pass%
sc config FCSImportCommonReading obj= %user% password= %pass%
sc config FCSImportPreprocessor obj= %user% password= %pass%
sc config FCSIntervalDataExport obj= %user% password= %pass%
sc config FCSLeakSensorExport obj= %user% password= %pass%
sc config FCSOutOfRouteReadsExport obj= %user% password= %pass%
sc config FCSRestoreRoute obj= %user% password= %pass%
sc config FCSRouteSmartService obj= %user% password= %pass%
sc config FCSSKMS obj= %user% password= %pass%
sc config FCSTemporaryRouting obj= %user% password= %pass%
sc config Itron.Mobile.FCS.MobileServices obj= %user% password= %pass%
pause
GOTO DONE

:USERERROR
echo.
echo Username not specified
echo Type in username in the following format ^<domain\user^>
echo.
pause
GOTO QUIT

:PASSERROR
echo.
echo Password not specified
echo Run batch file again making sure you type in a password for the user specified.
echo.
pause
GOTO QUIT

:DONE
ECHO Starting up services...
echo.
sc start adTempus$default >NUL
sc start FCSAdjustHighLowLimits >NUL
sc start FCSAdministrator >NUL
sc start FCSAdvancedAMRExport >NUL
sc start FCSApplyOutOfRouteReads >NUL
sc start FCSBackupRoute >NUL
sc start FDCommunicationService >NUL
sc start FCSDailyAssignments >NUL
sc start FCSDeleteRoute >NUL
sc start FCSExport >NUL
sc start FCSForceComplete >NUL
sc start FCSGenerateAdvAMRRequests >NUL
sc start FCSGenerateStatistics >NUL
sc start FCSImport >NUL
sc start FCSImportCommonReading >NUL
sc start FCSImportPreprocessor >NUL
sc start FCSIntervalDataExport >NUL
sc start FCSLeakSensorExport >NUL
sc start FCSOutOfRouteReadsExport >NUL
sc start FCSRestoreRoute >NUL
sc start FCSRouteSmartService >NUL
sc start FCSSKMS >NUL
sc start FCSTemporaryRouting >NUL
sc start Itron.Mobile.FCS.MobileServices >NUL
echo Done
echo.
pause
exit

:QUIT
exit