rem set WINPATH=C:\Python27\
rem ******* Python / Jython *******
if NOT defined PYTHONBINPATH (
    set PYTHONBINPATH=C:\Python27
)
set PATH=%PATH%;%PYTHONBINPATH%;%PYTHONBINPATH%\Scripts