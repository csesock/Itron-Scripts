::Copies ItronMobile.sqlite file to the necessary folder and renames to be imported by FCS
@echo off
echo Copying file...
::xcopy /Y "C:\Users\christophers.UNITED-SYSTEMS\Desktop\ItronMobile.sqlite" "C:\Program Files\Itron\Field Collection System\comm\fcs\work\ima"
xcopy /Y "C:\Users\%USERNAME%\Desktop\ItronMobile.sqlite" "C:\Program Files\Itron\Field Collection System\comm\fcs\work\ima"
::xcopy /Y "%CD% and \ItronMobile.sqlite" "C:\Program Files\Itron\Field Collection System\comm\fcs\work\ima"
rename "C:\Program Files\Itron\Field Collection System\comm\fcs\work\ima\ItronMobile.sqlite" "ItronMobile.req"
echo ...
ping 127.0.0.1 -n 2 > nul
echo Readings Imported into FCS
ping 127.0.0.1 -n 2 > nul
pause