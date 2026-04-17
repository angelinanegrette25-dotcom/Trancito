import tkinter as tk
from tkinter import messagebox

from modelos.usuario import Usuario
from modelos.vehiculo import Vehiculo
from modelos.ubicacion import Ubicacion
from modelos.zona_control import ZonaControl

from servicios.sistema_transito import SistemaTransito
from servicios.gestor_zonas import GestorZonas


class VentanaPrincipal:

    def __init__(self):

        self.sistema = SistemaTransito()
        self.gestor_zonas = GestorZonas()

        self.ventana = tk.Tk()

        self.ventana.title(
            "Sistema Inteligente de Transito"
        )

        self.ventana.geometry("500x500")

        self.crear_interfaz()

    def crear_interfaz(self):

        titulo = tk.Label(
            self.ventana,
            text="Sistema Inteligente para Evitar Comparendos",
            font=("Arial", 14)
        )

        titulo.pack(pady=10)

        boton_usuario = tk.Button(
            self.ventana,
            text="Registrar usuario",
            width=30,
            command=self.registrar_usuario
        )

        boton_usuario.pack(pady=5)

        boton_vehiculo = tk.Button(
            self.ventana,
            text="Registrar vehiculo",
            width=30,
            command=self.registrar_vehiculo
        )

        boton_vehiculo.pack(pady=5)

        boton_zona = tk.Button(
            self.ventana,
            text="Registrar zona",
            width=30,
            command=self.registrar_zona
        )

        boton_zona.pack(pady=5)

        boton_ver_usuarios = tk.Button(
            self.ventana,
            text="Ver usuarios",
            width=30,
            command=self.ver_usuarios
        )

        boton_ver_usuarios.pack(pady=5)

        boton_ver_zonas = tk.Button(
            self.ventana,
            text="Ver zonas",
            width=30,
            command=self.ver_zonas
        )

        boton_ver_zonas.pack(pady=5)

        self.resultado = tk.Text(
            self.ventana,
            width=50,
            height=12
        )

        self.resultado.pack(pady=10)

    def registrar_usuario(self):

        ventana = tk.Toplevel()

        ventana.title("Registrar usuario")

        tk.Label(
            ventana,
            text="Id"
        ).grid(row=0, column=0)

        tk.Label(
            ventana,
            text="Nombre"
        ).grid(row=1, column=0)

        tk.Label(
            ventana,
            text="Correo"
        ).grid(row=2, column=0)

        tk.Label(
            ventana,
            text="Contraseña"
        ).grid(row=3, column=0)

        entrada_id = tk.Entry(ventana)
        entrada_nombre = tk.Entry(ventana)
        entrada_correo = tk.Entry(ventana)
        entrada_contraseña = tk.Entry(ventana)

        entrada_id.grid(row=0, column=1)
        entrada_nombre.grid(row=1, column=1)
        entrada_correo.grid(row=2, column=1)
        entrada_contraseña.grid(row=3, column=1)

        def guardar():

            usuario = Usuario(
                int(entrada_id.get()),
                entrada_nombre.get(),
                entrada_correo.get(),
                entrada_contraseña.get()
            )

            self.sistema.registrar_usuario(usuario)

            messagebox.showinfo(
                "Correcto",
                "Usuario registrado"
            )

            ventana.destroy()

        boton_guardar = tk.Button(
            ventana,
            text="Guardar",
            command=guardar
        )

        boton_guardar.grid(row=4, column=1)

    def registrar_vehiculo(self):

        ventana = tk.Toplevel()

        ventana.title("Registrar vehiculo")

        campos = [
            "Id usuario",
            "Placa",
            "Tipo",
            "Marca",
            "Modelo",
            "Color"
        ]

        entradas = []

        for i, campo in enumerate(campos):

            tk.Label(
                ventana,
                text=campo
            ).grid(row=i, column=0)

            entrada = tk.Entry(ventana)

            entrada.grid(row=i, column=1)

            entradas.append(entrada)

        def guardar():

            vehiculo = Vehiculo(
                entradas[1].get(),
                entradas[2].get(),
                entradas[3].get(),
                entradas[4].get(),
                entradas[5].get()
            )

            resultado = self.sistema.registrar_vehiculo(
                int(entradas[0].get()),
                vehiculo
            )

            if resultado:

                messagebox.showinfo(
                    "Correcto",
                    "Vehiculo registrado"
                )

                ventana.destroy()

            else:

                messagebox.showerror(
                    "Error",
                    "Usuario no encontrado"
                )

        boton_guardar = tk.Button(
            ventana,
            text="Guardar",
            command=guardar
        )

        boton_guardar.grid(row=6, column=1)

    def registrar_zona(self):

        ventana = tk.Toplevel()

        ventana.title("Registrar zona")

        campos = [
            "Id zona",
            "Tipo control",
            "Direccion",
            "Latitud",
            "Longitud",
            "Limite velocidad"
        ]

        entradas = []

        for i, campo in enumerate(campos):

            tk.Label(
                ventana,
                text=campo
            ).grid(row=i, column=0)

            entrada = tk.Entry(ventana)

            entrada.grid(row=i, column=1)

            entradas.append(entrada)

        def guardar():

            ubicacion = Ubicacion(
                float(entradas[3].get()),
                float(entradas[4].get()),
                entradas[2].get()
            )

            zona = ZonaControl(
                int(entradas[0].get()),
                entradas[1].get(),
                ubicacion,
                int(entradas[5].get())
            )

            self.gestor_zonas.agregar_zona(zona)

            messagebox.showinfo(
                "Correcto",
                "Zona registrada"
            )

            ventana.destroy()

        boton_guardar = tk.Button(
            ventana,
            text="Guardar",
            command=guardar
        )

        boton_guardar.grid(row=6, column=1)

    def ver_usuarios(self):

        self.resultado.delete(
            "1.0",
            tk.END
        )

        self.resultado.insert(
            tk.END,
            self.sistema.mostrar_usuarios()
        )

    def ver_zonas(self):

        self.resultado.delete(
            "1.0",
            tk.END
        )

        self.resultado.insert(
            tk.END,
            self.gestor_zonas.mostrar_zonas()
        )

    def ejecutar(self):

        self.ventana.mainloop()