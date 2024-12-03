Sistema de Navegación en la UDLAP
Características
1.Grafo del campus UDLAP:
 - Cada edificio, plaza, jardín y área está representado como un nodo.
 - Las conexiones entre estos están representadas como aristas con pesos basados en las distancias en metros.
2. Algoritmo de Dijkstra:
 - Calcula la ruta más corta entre dos ubicaciones basándose en las distancias ponderadas.
3.Interfaz gráfica:
 - Construida con Tkinter.
 - Permite seleccionar nodos de inicio y destino desde listas desplegables.
 - Muestra la ruta más corta y la distancia total.
4.Visualización del grafo (opcional):
 - Puede integrar una visualización gráfica del grafo utilizando Matplotlib.
________________________________________
Requisitos del Sistema
• Python 3.7+

• Bibliotecas necesarias:
 - networkx
 - tkinter (incluido con Python)
 - matplotlib (opcional, si se desea dibujar el grafo)

Para instalar networkx y matplotlib:

pip install networkx matplotlib

________________________________________
Uso
1.Ejecuta el script principal:

python UDLAP_Nodos.py

2.Aparecerá una ventana que permite:
 - Seleccionar un nodo de inicio.
 - Seleccionar un nodo de destino.
 - Presionar el botón "Calcular Ruta" para obtener la ruta más corta.

3.El resultado incluye:
 - La secuencia de nodos que forman la ruta.
 - La distancia total en metros.
________________________________________
Estructura del Código
1. Creación del Grafo
El grafo se define usando networkx, con nodos que representan lugares del campus y aristas que indican las conexiones entre ellos, ponderadas por distancias en metros.

udlap = nx.Graph()
udlap.add_node("GC")    # Ejemplo: Gimnasio "Luison"
udlap.add_edge("GC", "GA", weight=60)

2. Algoritmo de Dijkstra
Se usa el algoritmo de Dijkstra para encontrar la ruta más corta:

path = nx.dijkstra_path(udlap, start, end, weight='weight')
distance = nx.dijkstra_path_length(udlap, start, end, weight='weight')

3. Interfaz Gráfica
La interfaz gráfica permite la interacción fácil del usuario:
 - Dropdowns para nodos de inicio y destino.
 - Un botón para calcular rutas.
 - Una etiqueta para mostrar resultados.

4. Visualización del Grafo (opcional)
Se puede integrar un diagrama del grafo con rutas resaltadas utilizando Matplotlib.
________________________________________
Ejemplo
Input:
• Nodo de inicio: CB (Colegio Bernal)
• Nodo de destino: CIR (Centro de Rehabilitación)

Output:
Ruta más corta: CB -> HU -> AG -> HA -> CN -> TI -> CIR
Distancia total: 580 metros
________________________________________
Mejoras Futuras
1.Visualización dinámica del grafo:
 - Implementar una visualización en la interfaz para mostrar la ruta calculada.
2. Soporte para múltiples criterios:
 - Incorporar factores adicionales como tiempo de recorrido o accesibilidad.
3. Exportar resultados:
 - Agregar opción para guardar rutas calculadas en un archivo de texto o imagen.
________________________________________
Licencia
Este proyecto es de uso educativo. Siéntete libre de modificarlo y adaptarlo a tus necesidades.

