@echo off
echo Deleting all .DS_Store files recursively...
for /r %%i in (.DS_Store) do (
    del "%%i"
)
echo Done.
pause