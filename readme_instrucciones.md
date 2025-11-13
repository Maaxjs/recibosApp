# 📄 Extractor de Recibos de Sueldo

Aplicación simple con interfaz gráfica para extraer datos de recibos de sueldo en PDF y generar un archivo Excel.

## 🚀 Instalación desde cero (para Windows)

### Paso 1: Instalar Python

1. Ve a [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Descarga la última versión de Python (botón amarillo grande)
3. **MUY IMPORTANTE:** Durante la instalación, marca la casilla "Add Python to PATH"
4. Haz clic en "Install Now"
5. Espera a que termine la instalación

### Paso 2: Descargar este proyecto

**Opción A: Con Git (recomendado)**
```bash
git clone [URL-DEL-REPOSITORIO]
cd extractor-recibos
```

**Opción B: Sin Git**
1. Haz clic en el botón verde "Code" en GitHub
2. Selecciona "Download ZIP"
3. Descomprime el archivo en tu computadora
4. Abre la carpeta descomprimida

### Paso 3: Instalar las dependencias

1. Abre una terminal en la carpeta del proyecto:
   - En Windows: Haz clic derecho en la carpeta → "Abrir en Terminal" o "Abrir ventana de comandos aquí"
   - O busca "cmd" en el menú inicio, y navega a la carpeta con `cd ruta\a\la\carpeta`

2. Ejecuta este comando:
```bash
pip install -r requirements.txt
```

3. Espera a que se instalen todas las librerías (tomará un par de minutos)

### Paso 4: ¡Ejecutar la aplicación!

```bash
python app.py
```

Se abrirá una ventana con la interfaz gráfica.

## 📖 Cómo usar la aplicación

1. **Haz clic en "📁 Seleccionar Carpeta con PDFs"**
   - Busca y selecciona la carpeta donde están tus recibos PDF

2. **Haz clic en "▶️ Procesar Recibos"**
   - La aplicación leerá todos los PDFs de la carpeta
   - Extraerá el nombre del empleado y el sueldo de cada uno

3. **Encuentra tu archivo Excel**
   - Se generará un archivo llamado `recibos_procesados.xlsx`
   - Estará en la misma carpeta donde están tus PDFs
   - Abre el archivo con Excel o LibreOffice

## 📁 Estructura del proyecto

```
extractor-recibos/
│
├── app.py              # Aplicación principal con interfaz gráfica
├── requirements.txt    # Lista de dependencias
├── README.md          # Este archivo
└── recibos/           # (Opcional) Carpeta de ejemplo para PDFs
```

## ❓ Preguntas frecuentes

**P: ¿Funciona en Mac o Linux?**
R: Sí, los pasos son similares. En Mac/Linux usa `python3` en lugar de `python` y `pip3` en lugar de `pip`.

**P: ¿Puedo procesar recibos de otros formatos?**
R: Esta aplicación está diseñada para recibos del formato de Crisal Inversiones. Para otros formatos, contacta al desarrollador.

**P: ¿Los datos se suben a internet?**
R: No, todo se procesa localmente en tu computadora. Ningún dato sale de tu PC.

**P: ¿Qué hago si me da error?**
R: Verifica que:
- Instalaste Python correctamente (con "Add to PATH")
- Ejecutaste `pip install -r requirements.txt`
- Los archivos PDF no están corruptos
- Tienes permisos para leer los archivos

## 🛠️ Solución de problemas comunes

### Error: "python no se reconoce como comando"
- No instalaste Python con "Add to PATH"
- Solución: Reinstala Python y marca la casilla "Add Python to PATH"

### Error: "pip no se reconoce como comando"
- Mismo problema que arriba
- Solución: Reinstala Python correctamente

### Error al procesar un PDF específico
- El PDF puede estar corrupto o tener un formato diferente
- La aplicación seguirá procesando los demás archivos

## 📧 Soporte

Si tienes problemas, abre un "Issue" en GitHub con:
- Descripción del problema
- Mensaje de error completo (captura de pantalla)
- Sistema operativo que usas

## 📄 Licencia

MIT License - Puedes usar, modificar y distribuir este código libremente.
