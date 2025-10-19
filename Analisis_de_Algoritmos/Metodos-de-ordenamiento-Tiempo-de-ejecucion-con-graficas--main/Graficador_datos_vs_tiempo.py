def iniciar_graficador():
    import tkinter as tk
    from tkinter import filedialog, messagebox
    import matplotlib.pyplot as plt
    import csv, os

    def leer_csv(nombre_archivo):
        tamanos, tiempos = [], []
        try:
            with open(nombre_archivo, "r", newline="") as archivo:
                lector = csv.reader(archivo, delimiter=",")
                next(lector)  # saltar encabezado
                for fila in lector:
                    tamanos.append(int(fila[0]))
                    tiempos.append(float(fila[1]))
            return tamanos, tiempos
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo leer {nombre_archivo}\n{e}")
            return None, None

    def graficar():
        archivos = filedialog.askopenfilenames(
            title="Selecciona uno o más archivos CSV",
            filetypes=[("Archivos CSV", "*.csv")]
        )
        if not archivos:
            return

        plt.figure(figsize=(8, 6))

        for archivo in archivos:
            tamanos, tiempos = leer_csv(archivo)
            if tamanos and tiempos:
                nombre = os.path.basename(archivo).replace(".csv", "")
                plt.plot(tamanos, tiempos, marker="o", label=nombre)

        plt.title("Comparación de algoritmos de ordenamiento")
        plt.xlabel("Número de elementos (N)")
        plt.ylabel("Tiempo (segundos)")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    ventana = tk.Tk()
    ventana.title("Graficador: Datos vs Tiempo")
    ventana.geometry("400x200")

    lbl = tk.Label(ventana, text="Selecciona archivos CSV para comparar.\n(puedes elegir varios a la vez)")
    lbl.pack(pady=20)

    btn = tk.Button(ventana, text="Seleccionar y graficar", command=graficar)
    btn.pack(pady=10)

    ventana.mainloop()
if __name__ == "__main__":
    iniciar_graficador()
