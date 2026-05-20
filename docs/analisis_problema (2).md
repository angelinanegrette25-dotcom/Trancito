# Análisis del problema

## 1. Descripción del problema

Los conductores pueden recibir comparendos o multas de tránsito por no conocer previamente las zonas de control, cámaras de velocidad, fotomultas o puntos de alto riesgo en sus rutas. Muchas veces el conductor inicia un recorrido sin información suficiente sobre los controles presentes en el trayecto, lo cual puede ocasionar infracciones por exceso de velocidad o desconocimiento de las normas específicas de una zona.

El proyecto propone un sistema inteligente de alertas de tránsito que permite registrar usuarios, vehículos, rutas y trayectos. Además, el sistema genera alertas preventivas cuando identifica posibles riesgos asociados a una ruta o trayecto. La solución busca ayudar al conductor a manejar de forma más consciente y responsable.

## 2. Objetivo general

Desarrollar una aplicación en Python basada en programación orientada a objetos que permita registrar usuarios, vehículos, rutas y trayectos, generando alertas inteligentes para prevenir posibles comparendos o multas de tránsito.

## 3. Alcance de la primera entrega

Para esta primera entrega se implementará una aplicación por consola que permita:

- Registrar usuarios.
- Registrar vehículos.
- Crear rutas.
- Iniciar trayectos.
- Generar alertas inteligentes.
- Consultar usuarios y trayectos.
- Usar una librería externa para cálculo de distancias.

## 4. Funcionalidad innovadora

La funcionalidad innovadora del proyecto consiste en simular un análisis inteligente de riesgo. Cada alerta tiene un nivel de riesgo y el sistema calcula una probabilidad aproximada de peligro mediante un método de análisis predictivo básico. Además, se utiliza la librería externa geopy para calcular distancias reales entre ubicaciones geográficas.

## 5. Modelo del mundo del problema

El sistema se compone de las siguientes clases principales:

- Usuario: representa al conductor.
- Vehículo: representa el vehículo registrado por el usuario.
- Ubicación: representa un punto geográfico con latitud, longitud y dirección.
- Ruta: representa el recorrido entre un origen y un destino.
- Trayecto: representa un viaje realizado por un usuario con un vehículo y una ruta.
- Alerta: representa una advertencia generada durante un trayecto.
- SistemaTransitoInteligente: coordina las operaciones principales de la aplicación.

## 6. Asignación de responsabilidades

| Clase | Responsabilidad |
|---|---|
| Usuario | Guardar la información del conductor, sus vehículos y su historial de trayectos. |
| Vehículo | Guardar la información del vehículo registrado. |
| Ubicación | Representar puntos geográficos y calcular distancia entre ubicaciones. |
| Ruta | Guardar origen, destino, distancia y puntos de la ruta. |
| Trayecto | Asociar usuario, vehículo, ruta y alertas generadas. |
| Alerta | Representar una alerta y calcular una probabilidad de riesgo. |
| SistemaTransitoInteligente | Gestionar usuarios, vehículos, trayectos y alertas. |

## 7. Prototipo de interfaz por consola

```text
=== SISTEMA INTELIGENTE DE ALERTAS DE TRÁNSITO ===
1. Registrar usuario
2. Buscar usuario
3. Registrar vehículo
4. Crear ruta
5. Iniciar trayecto
6. Generar alerta inteligente
7. Ver usuarios
8. Ver trayectos
9. Salir
```

## 8. Librerías externas

- geopy: para calcular distancias entre ubicaciones.
- colorama: para mejorar la visualización de mensajes en consola.
- pytest: para pruebas unitarias.
