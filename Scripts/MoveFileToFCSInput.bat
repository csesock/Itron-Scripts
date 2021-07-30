::Copies file named download.dat from current folder to FCS input folder
@echo off
echo Copying file...
xcopy /Y "%cd%\download.dat" "C:\Itron\FCS\Import\Input\"
ping 127.0.0.1 -n 2 > nul
pause