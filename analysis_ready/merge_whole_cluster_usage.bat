@echo off
setlocal

set SCRIPT_DIR=%~dp0
python "%SCRIPT_DIR%merge_whole_cluster_usage.py" %*

if errorlevel 1 (
  exit /b %errorlevel%
)

endlocal

