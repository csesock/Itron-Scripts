::Copies file named download.dat from Desktop to FCS input folder
@echo off
echo Copying file...
xcopy /Y C:\Users\christophers.UNITED-SYSTEMS\Desktop\download.dat C:\Itron\FCS\Import\Input\
ping 127.0.0.1 -n 2 > nul
pause