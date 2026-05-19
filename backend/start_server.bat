@echo off
set "PROJECT_ROOT=%~dp0.."
set "BACKEND_DIR=%~dp0"
set "BACKEND_PATH=%BACKEND_DIR:~0,-1%"
set "PYTHON_EXE=C:\Users\ah\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
set "DEPS_DIR=C:\tmp\chatbot_backend_deps"
set "PYTHONPATH=%DEPS_DIR%;%BACKEND_DIR%"
cd /d "%BACKEND_DIR%"
"%PYTHON_EXE%" -c "import sys; sys.path.insert(0, r'%DEPS_DIR%'); sys.path.insert(0, r'%BACKEND_PATH%'); from uvicorn.main import main; main()" main:app --host 0.0.0.0 --port 8000 1> "%BACKEND_PATH%\server.log" 2> "%BACKEND_PATH%\server.err"
