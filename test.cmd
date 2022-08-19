@echo off
setlocal enabledelayedexpansion

cd restest
for /f %%i in ('"dir /s /b | find "results.txt""') do set var=%%i

echo.%var%
set var=%var:\=\\%
echo.%var%

cd ..
copy %var% .\\