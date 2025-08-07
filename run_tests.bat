@echo off
call venv\Scripts\activate.bat
pytest test_app.py

if %ERRORLEVEL%==0 (
    echo ✅ All tests passed!
    exit /b 0
) else (
    echo ❌ Some tests failed!
    exit /b 1
)
