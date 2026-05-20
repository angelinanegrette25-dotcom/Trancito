# Requisitos funcionales y no funcionales

## Requisitos funcionales

| Código | Requisito funcional | Descripción | Prioridad |
|---|---|---|---|
| RF01 | Registrar usuario | El sistema permitirá registrar un usuario con id, nombre y correo electrónico. | Alta |
| RF02 | Buscar usuario | El sistema permitirá buscar un usuario por su identificador. | Alta |
| RF03 | Registrar vehículo | El sistema permitirá asociar uno o varios vehículos a un usuario registrado. | Alta |
| RF04 | Crear ruta | El sistema permitirá crear una ruta con origen, destino, distancia y puntos geográficos. | Alta |
| RF05 | Iniciar trayecto | El sistema permitirá iniciar un trayecto asociando usuario, vehículo y ruta. | Alta |
| RF06 | Generar alerta inteligente | El sistema generará alertas de tránsito con nivel de riesgo y simulación predictiva. | Alta |
| RF07 | Consultar historial | El sistema permitirá consultar los trayectos registrados y sus alertas. | Media |
| RF08 | Calcular distancia entre ubicaciones | El sistema usará la librería externa geopy para calcular distancias entre puntos geográficos. | Alta |

## Requisitos no funcionales

| Código | Requisito no funcional | Descripción |
|---|---|---|
| RNF01 | Usabilidad | La aplicación debe ser fácil de usar mediante un menú por consola. |
| RNF02 | Modularidad | El código debe estar organizado en carpetas de modelos, servicios, excepciones y pruebas. |
| RNF03 | Mantenibilidad | Las clases deben tener responsabilidades claras y nombres entendibles. |
| RNF04 | Escalabilidad | El sistema debe permitir agregar nuevas funcionalidades como interfaz gráfica en futuras entregas. |
| RNF05 | Confiabilidad | El sistema debe manejar errores comunes mediante excepciones. |
| RNF06 | Sustentabilidad académica | El código debe ser entendible y explicable por todos los integrantes del equipo. |
| RNF07 | Uso de librerías externas | La aplicación debe usar al menos una librería externa diferente a la interfaz de usuario. |
