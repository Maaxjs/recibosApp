import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import re
import PyPDF2
import pandas as pd
from pathlib import Path
import threading

class AplicacionRecibos:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Extractor de Recibos de Sueldo")
        self.ventana.geometry("600x400")
        self.ventana.resizable(False, False)
        
        # Variables
        self.carpeta_seleccionada = None
        self.procesando = False
        
        # Crear interfaz
        self.crear_interfaz()
    
    def crear_interfaz(self):
        # Título
        titulo = tk.Label(
            self.ventana, 
            text="📄 Extractor de Recibos de Sueldo",
            font=("Arial", 18, "bold"),
            pady=20
        )
        titulo.pack()
        
        # Instrucciones
        instrucciones = tk.Label(
            self.ventana,
            text="1. Seleccione la carpeta con los recibos PDF\n2. Presione 'Procesar Recibos'\n3. Se generará un archivo Excel con los datos",
            font=("Arial", 11),
            justify="left",
            pady=10
        )
        instrucciones.pack()
        
        # Frame para selección de carpeta
        frame_carpeta = tk.Frame(self.ventana, pady=20)
        frame_carpeta.pack()
        
        self.btn_seleccionar = tk.Button(
            frame_carpeta,
            text="📁 Seleccionar Carpeta con PDFs",
            font=("Arial", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            padx=20,
            pady=10,
            command=self.seleccionar_carpeta,
            cursor="hand2"
        )
        self.btn_seleccionar.pack()
        
        # Label para mostrar carpeta seleccionada
        self.label_carpeta = tk.Label(
            self.ventana,
            text="Ninguna carpeta seleccionada",
            font=("Arial", 10),
            fg="gray"
        )
        self.label_carpeta.pack(pady=5)
        
        # Botón procesar
        self.btn_procesar = tk.Button(
            self.ventana,
            text="▶️ Procesar Recibos",
            font=("Arial", 12, "bold"),
            bg="#2196F3",
            fg="white",
            padx=30,
            pady=10,
            command=self.procesar_recibos,
            cursor="hand2",
            state="disabled"
        )
        self.btn_procesar.pack(pady=20)
        
        # Barra de progreso
        self.progreso = ttk.Progressbar(
            self.ventana,
            length=400,
            mode='indeterminate'
        )
        self.progreso.pack(pady=10)
        
        # Label de estado
        self.label_estado = tk.Label(
            self.ventana,
            text="",
            font=("Arial", 10),
            fg="blue"
        )
        self.label_estado.pack()
    
    def seleccionar_carpeta(self):
        carpeta = filedialog.askdirectory(title="Seleccione la carpeta con los recibos PDF")
        if carpeta:
            self.carpeta_seleccionada = carpeta
            nombre_carpeta = Path(carpeta).name
            self.label_carpeta.config(
                text=f"Carpeta: {nombre_carpeta}",
                fg="green"
            )
            self.btn_procesar.config(state="normal")
    
    def extraer_datos_recibo(self, texto_pdf):
        """Extrae nombre y sueldo del texto del PDF"""
        nombre = None
        sueldo = None
        
        # Buscar nombre (patrón flexible)
        patrones_nombre = [
            r'Apellido\s+y\s+Nombres.*?\n.*?([A-ZÁÉÍÓÚÑ]+\s+[A-ZÁÉÍÓÚÑ]+(?:\s+[A-ZÁÉÍÓÚÑ]+)?)',
            r'([A-ZÁÉÍÓÚÑ]+\s+[A-ZÁÉÍÓÚÑ]+\s+[A-ZÁÉÍÓÚÑ]+)\s+C\.U\.I\.L\.',
        ]
        
        for patron in patrones_nombre:
            match = re.search(patron, texto_pdf, re.IGNORECASE)
            if match:
                nombre = match.group(1).strip()
                break
        
        # Buscar sueldo
        patron_sueldo = r'SUELDO\s+MENSUAL\s+[\d,\.]+\s+([\d,.]+)'
        match_sueldo = re.search(patron_sueldo, texto_pdf, re.IGNORECASE)
        
        if match_sueldo:
            sueldo_str = match_sueldo.group(1).replace('.', '').replace(',', '.')
            try:
                sueldo = float(sueldo_str)
            except ValueError:
                pass
        
        return nombre, sueldo
    
    def procesar_pdf(self, ruta_pdf):
        """Procesa un archivo PDF individual"""
        try:
            with open(ruta_pdf, 'rb') as archivo:
                lector = PyPDF2.PdfReader(archivo)
                texto_completo = ''
                
                for pagina in lector.pages:
                    texto_completo += pagina.extract_text()
                
                nombre, sueldo = self.extraer_datos_recibo(texto_completo)
                
                return {
                    'Archivo': Path(ruta_pdf).name,
                    'Nombre Empleado': nombre if nombre else 'No encontrado',
                    'Sueldo': sueldo if sueldo else 0
                }
        except Exception as e:
            return {
                'Archivo': Path(ruta_pdf).name,
                'Nombre Empleado': f'Error: {str(e)}',
                'Sueldo': 0
            }
    
    def ejecutar_procesamiento(self):
        """Ejecuta el procesamiento en un hilo separado"""
        carpeta = Path(self.carpeta_seleccionada)
        archivos_pdf = list(carpeta.glob('*.pdf'))
        
        if not archivos_pdf:
            self.ventana.after(0, lambda: messagebox.showwarning(
                "Sin archivos",
                "No se encontraron archivos PDF en la carpeta seleccionada"
            ))
            self.ventana.after(0, self.finalizar_procesamiento)
            return
        
        datos_extraidos = []
        
        for pdf in archivos_pdf:
            datos = self.procesar_pdf(pdf)
            if datos:
                datos_extraidos.append(datos)
        
        # Crear Excel
        if datos_extraidos:
            archivo_salida = carpeta / 'recibos_procesados.xlsx'
            df = pd.DataFrame(datos_extraidos)
            df.to_excel(archivo_salida, index=False, engine='openpyxl')
            
            mensaje = f"✓ Procesamiento completado!\n\n"
            mensaje += f"Recibos procesados: {len(datos_extraidos)}\n"
            mensaje += f"Archivo generado: recibos_procesados.xlsx\n"
            mensaje += f"Ubicación: {carpeta}"
            
            self.ventana.after(0, lambda: messagebox.showinfo("Éxito", mensaje))
        else:
            self.ventana.after(0, lambda: messagebox.showerror(
                "Error",
                "No se pudo extraer datos de ningún archivo"
            ))
        
        self.ventana.after(0, self.finalizar_procesamiento)
    
    def procesar_recibos(self):
        """Inicia el procesamiento de recibos"""
        if not self.carpeta_seleccionada:
            messagebox.showwarning("Advertencia", "Debe seleccionar una carpeta primero")
            return
        
        self.procesando = True
        self.btn_procesar.config(state="disabled")
        self.btn_seleccionar.config(state="disabled")
        self.label_estado.config(text="Procesando recibos...", fg="blue")
        self.progreso.start(10)
        
        # Ejecutar en hilo separado para no bloquear la interfaz
        hilo = threading.Thread(target=self.ejecutar_procesamiento)
        hilo.daemon = True
        hilo.start()
    
    def finalizar_procesamiento(self):
        """Finaliza el procesamiento y restaura la interfaz"""
        self.progreso.stop()
        self.btn_procesar.config(state="normal")
        self.btn_seleccionar.config(state="normal")
        self.label_estado.config(text="", fg="blue")
        self.procesando = False

if __name__ == "__main__":
    ventana = tk.Tk()
    app = AplicacionRecibos(ventana)
    ventana.mainloop()
