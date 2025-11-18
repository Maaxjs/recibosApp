# RecibosApp

PASOS:

Instalar Tesseract OCR
Descargar Tesseract (versión Windows 64 bits) desde el siguiente enlace:

🔗 https://github.com/tesseract-ocr/tesseract/releases/download/5.5.0/tesseract-ocr-w64-setup-5.5.0.20241111.exe

Durante la instalación:

Elegir el idioma Español.

Marcar “Add to PATH” si lo pide.

Instalar en una carpeta vacía (importante para evitar conflictos).

Crear entorno virtual
Ejecutar en PowerShell dentro del proyecto:

python -m venv venv .\venv\Scripts\activate.bat

Instalar dependencias
pip install -r requirements.txt

Credenciales (agregar en config.py)
MAIL: ticketsaloe@gmail.com

PASS: txze yqrs ncmj gtqr

API KEY GROQ: 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

Ejecutar la aplicación
python app.py

#! Solución si Tesseract falla con el idioma Español

Si al ejecutar aparece un error indicando que falta spa.traineddata, instalarlo manualmente.

Ejecutar PowerShell como administrador:

cd "C:\Program Files\Tesseract-OCR\tessdata"
Invoke-WebRequest -Uri "https://github.com/tesseract-ocr/tessdata/raw/main/spa.traineddata" -
