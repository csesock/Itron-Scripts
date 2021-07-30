::Copies ItronMobile.sqlite file to the necessary folder and renames to be imported by FCS
@echo off
echo Current working directory... %cd% 
echo Copying file...
xcopy /Y "%cd%\ItronMobile.sqlite" "C:\Program Files\Itron\Field Collection System\comm\fcs\work\ima"
rename "C:\Program Files\Itron\Field Collection System\comm\fcs\work\ima\ItronMobile.sqlite" "ItronMobile.req"
echo ...
ping 127.0.0.1 -n 2 > nul
echo Readings will be automatically imported into FCS shortly
ping 127.0.0.1 -n 2 > nul
pause