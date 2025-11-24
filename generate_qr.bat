@echo off
echo Installing Python dependencies...
pip install -r requirements.txt

echo.
echo Running QR Code Generator...
python qr_generator.py

echo.
echo Press any key to exit...
pause > nul