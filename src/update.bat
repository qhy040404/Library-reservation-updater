@echo off
echo Waiting Updater to exit
timeout 3 >nul
xcopy update\*.* .\ /y /e
rd update /S /Q
del temp.zip /Q
exit