# Calculadora-de-Rentabilidad

Descripción

Esta aplicación permite calcular el punto de equilibrio de un negocio, mostrando gráficamente la relación entre costos, ingresos y rentabilidad. Además, incluye sliders interactivos para simular cambios en costos variables y precios de venta en tiempo real, ayudando a los emprendedores a tomar mejores decisiones financieras.

Asegúrate de tener Python 3.x instalado. Luego, instala las dependencias necesarias:

pip install matplotlib numpy
Si Tkinter no está instalado en tu sistema, instálalo con:
  Windows: Tkinter ya viene incluido con Python.
  macOS: brew install python-tk

Funcionamiento:
El programa sigue estos pasos:

Captura de datos: Obtiene los costos fijos, variables y precio de venta ingresados.
Cálculo del punto de equilibrio: Se usa la fórmula:
Punto de Equilibrio (unidades) = Costos Fijos / (Precio de Venta - Costos Variables)
Visualización gráfica: Muestra un gráfico con ingresos y costos en función de las unidades vendidas.
Simulación dinámica: Los sliders permiten modificar los valores y actualizar la gráfica en tiempo real.

Ejemplo de Uso

Si tienes:
Costos Fijos: $5000
Costos Variables: $10 por unidad
Precio de Venta: $25 por unidad
El programa calculará el punto de equilibrio y mostrará una gráfica con los datos
