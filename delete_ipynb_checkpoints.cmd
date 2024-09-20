@echo off
setlocal

set "startDir=%cd%"

call :deleteCheckpoints "%startDir%"

goto :eof

:deleteCheckpoints
setlocal
set "currentDir=%~1"

for /d %%d in ("%currentDir%\*") do (
    if /i "%%~nxd"==".ipynb_checkpoints" (
        @REM rmdir /s /q "%%d"
        echo "%%d"
    ) else (
        call :deleteCheckpoints "%%d"
    )
)

endlocal
goto :eof