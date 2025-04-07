@echo off
echo ===================================
echo Examination System Quick Setup
echo ===================================

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed or not in PATH.
    echo Please install Python 3.9 or newer from https://www.python.org/downloads/
    pause
    exit /b 1
)

echo [1/3] Installing dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Error installing dependencies.
    pause
    exit /b 1
)

echo [2/3] Setting up database...
if not exist exam_system.db (
    echo - Creating new database...
    python init_db.py
    
    echo - Would you like to create sample data? [Y/N]
    set /p create_sample=
    if /i "%create_sample%"=="Y" (
        python create_sample_data.py
        echo Sample data created. 
        echo You can login with:
        echo   Teacher: teacher@example.com / password
        echo   Student: student@example.com / password
    )
) else (
    echo - Database already exists.
)

echo [3/3] Starting examination system...
echo ===================================
echo The application is running at: http://localhost:5000
echo Press Ctrl+C to stop the server
echo ===================================

python app.py
