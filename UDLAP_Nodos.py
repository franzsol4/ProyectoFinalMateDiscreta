import networkx as nx
import tkinter as tk
from tkinter import ttk


# Crear un grafo simple
udlap = nx.Graph()

# Nodos UDLAP
#Areas Deportivas
udlap.add_node("GC")    #Gimnasio "Luison"
udlap.add_node("A")     #Alberca
udlap.add_node("GA")    #Gimnasio "Moe"
udlap.add_node("BQ")    #Canchas Basquetbol
udlap.add_node("GB")    #Gimnasio Pesas
udlap.add_node("CT")    #Canchas Tenis
udlap.add_node("CFR")   #Canchas Futbol Rapido
udlap.add_node("CL")    #Campo de lanzamiento
udlap.add_node("ATL")   #Pista Atletismo
udlap.add_node("TD")    #Templo del Dolor
udlap.add_node("CIR")   #Rehabilitación
#CamposDeportivos
udlap.add_node("C1")
udlap.add_node("C2")
udlap.add_node("C3")
udlap.add_node("C4")
udlap.add_node("C5")
udlap.add_node("C6")
udlap.add_node("C7")
#Colegios Residenciales
udlap.add_node("CC")    #Colegio Cain-Murray
udlap.add_node("CRL")    #Colegio Ray Lindley
udlap.add_node("CB")    #Colegio Bernal
udlap.add_node("CG")    #Colegio Gaos
#Jardines y Plazas
udlap.add_node("J1")    #Plaza de las Banderas
udlap.add_node("J2")    #Jardín de la Fogata
udlap.add_node("J3")    #Jardín de la Meditación
udlap.add_node("J4")    #Jardín de la Pareja
udlap.add_node("J5")    #Lago
udlap.add_node("J6")    #Jardín Central
#Áreas Académicas
udlap.add_node("AG")    #Ágora
udlap.add_node("HU")    #Humanidades
udlap.add_node("LB")    #Laboratorios B
udlap.add_node("LA")    #Laboratorios A
udlap.add_node("CI")    #Ciencias/Laboratorios
udlap.add_node("IA")    #Ingenierias
udlap.add_node("CN")    #Ciencias
udlap.add_node("TI")    #Tecnologías de la Información
udlap.add_node("HA")    #Rectoria
udlap.add_node("AU")    #Auditorio
udlap.add_node("BI")    #Biblioteca
udlap.add_node("CS")    #Ciencias Sociales
udlap.add_node("NE")    #Negocios
udlap.add_node("CE")    #Centro Estudiantil
udlap.add_node("iOS")   #iOS Development Lab
udlap.add_node("SL")    #Ciencias de la Salud
udlap.add_node("1")     #Crédito y Cobranza
udlap.add_node("RH")    #Recursos Humanos
udlap.add_node("PU")    #Comunicación
udlap.add_node("PF")    #Planta Física
#Accesos
udlap.add_node("AP")    #Acceso Periférico
udlap.add_node("A14")   #Acceso 14
udlap.add_node("A14CT") #Acceso 14 Canchas Tenis
udlap.add_node("AR")    #Acceso Recta

# Aristas UDLAP
udlap.add_edge("CB", "HU")
udlap.add_edge("HU", "AG")
udlap.add_edge("AG", "LA")
udlap.add_edge("AG", "HA")
udlap.add_edge("LA", "CI")
udlap.add_edge("LA", "IA")
udlap.add_edge("LA", "CN")
udlap.add_edge("LA", "HA")
udlap.add_edge("CI", "LB")
udlap.add_edge("CI", "IA")
udlap.add_edge("IA", "TI")
udlap.add_edge("IA", "CN")
udlap.add_edge("TI", "CN")
udlap.add_edge("TI", "1")
udlap.add_edge("TI", "J1")
udlap.add_edge("1", "RH")
udlap.add_edge("1", "C4")
udlap.add_edge("1", "J1")
udlap.add_edge("1", "BI")
udlap.add_edge("RH", "PU")
udlap.add_edge("RH", "PF")
udlap.add_edge("RH", "C4")
udlap.add_edge("RH", "J4")
udlap.add_edge("PU", "PF")
udlap.add_edge("PU", "C4")
udlap.add_edge("C4", "CFR")
udlap.add_edge("CN", "HA")
udlap.add_edge("CN", "AU")
udlap.add_edge("CN", "J1")
udlap.add_edge("CN", "BI")
udlap.add_edge("HA", "AU")
udlap.add_edge("HA", "J2")
udlap.add_edge("AU", "CS")
udlap.add_edge("AU", "J6")
udlap.add_edge("AU", "BI")
udlap.add_edge("BI", "J1")
udlap.add_edge("BI", "J4")
udlap.add_edge("BI", "J6")
udlap.add_edge("BI", "iOS")
udlap.add_edge("J6", "CS")
udlap.add_edge("J6", "CE")
udlap.add_edge("J6", "iOS")
udlap.add_edge("CS", "CE")
udlap.add_edge("CS", "NE")
udlap.add_edge("NE", "J2")
udlap.add_edge("J2", "J3")
udlap.add_edge("NE", "J3")
udlap.add_edge("NE", "CG")
udlap.add_edge("CE", "iOS")
udlap.add_edge("CE", "CG")
udlap.add_edge("CE", "CRL")
udlap.add_edge("CE", "J5")
udlap.add_edge("iOS", "J4")
udlap.add_edge("iOS", "CC")
udlap.add_edge("J4", "CC")
udlap.add_edge("J5", "CC")
udlap.add_edge("J5", "CRL")
udlap.add_edge("J5", "SL")
udlap.add_edge("J5", "TD")
udlap.add_edge("J5", "CL")
udlap.add_edge("CRL", "CG")
udlap.add_edge("CRL", "SL")
udlap.add_edge("SL", "C3")
udlap.add_edge("SL", "C2")
udlap.add_edge("SL", "TD")
udlap.add_edge("SL", "GA")
udlap.add_edge("TD", "CL")
udlap.add_edge("TD", "C1")
udlap.add_edge("C1", "GA")
udlap.add_edge("C1", "ATL")
udlap.add_edge("C1", "C6")
udlap.add_edge("C6", "C5")
udlap.add_edge("C5", "ATL")
udlap.add_edge("C5", "C7")
udlap.add_edge("C7", "GC")
udlap.add_edge("GC", "CIR")
udlap.add_edge("CIR", "ATL")
udlap.add_edge("CIR", "GA")
udlap.add_edge("GA", "A")
udlap.add_edge("GA", "C2")
udlap.add_edge("C2", "C3")
udlap.add_edge("C2", "BQ")
udlap.add_edge("C2", "A")
udlap.add_edge("A", "BQ")
udlap.add_edge("A", "GC")
udlap.add_edge("A", "GB")
udlap.add_edge("GB", "BQ")
udlap.add_edge("GB", "GC")
udlap.add_edge("GB", "CT")
udlap.add_edge("CT", "BQ")
udlap.add_edge("CT", "GC")
udlap.add_edge("CT", "CG")
udlap.add_edge("AP", "CB")
udlap.add_edge("AP", "HU")
udlap.add_edge("A14", "J3")
udlap.add_edge("A14CT", "CT")
udlap.add_edge("A14CT", "BQ")
udlap.add_edge("AR", "PF")
udlap.add_edge("AR", "CL")
udlap.add_edge("AR", "CC")
udlap.add_edge("AR", "C1")
udlap.add_edge("AR", "C6")

#Distancias (Ponderación Aristas) (Calculo en metros)
distances = {
    ("AP", "CB"): 193,
    ("AP", "HU"): 260,
    ("CB", "HU"): 150,
    ("HU", "AG"): 70,
    ("AG", "LA"): 110,
    ("AG", "HA"): 135,
    ("LA", "HA"): 110,
    ("LA", "CN"): 90,
    ("LA", "IA"): 60,
    ("LA", "CI"): 55,
    ("CI", "LB"): 70,
    ("CI", "IA"): 70,
    ("IA", "TI"): 70,
    ("IA", "CN"): 55,
    ("CN", "TI"): 60,
    ("CN", "HA"): 95,
    ("CN", "AU"): 70,
    ("CN", "J1"): 75,
    ("CN", "BI"): 125,
    ("TI", "1"): 65,
    ("TI", "J1"): 50,
    ("1", "J1"): 70,
    ("1", "BI"): 130,
    ("1", "RH"): 170,
    ("1", "C4"): 195,
    ("RH", "PF"): 60,
    ("RH", "PU"): 60,
    ("RH", "C4"): 145,
    ("RH", "J4"): 240,
    ("PU", "C4"): 90,
    ("PU", "PF"): 100,
    ("C4", "CFR"): 185,
    ("PF", "AR"): 75,
    ("AR", "CL"): 170,
    ("AR", "C1"): 285,
    ("AR", "C6"): 300,
    ("AR", "CC"): 265,
    ("BI", "J1"): 55,
    ("BI", "AU"): 88,
    ("BI", "J6"): 75,
    ("BI", "J4"): 55,
    ("BI", "iOS"): 60,
    ("J4", "iOS"): 45,
    ("J4", "CC"): 30,
    ("J6", "AU"): 55,
    ("J6", "iOS"): 100,
    ("J6", "CE"): 65,
    ("J6", "CS"): 55,
    ("CS", "NE"): 50,
    ("NE", "J2"): 115,
    ("J2", "HA"): 120,
    ("J2", "J3"): 60,
    ("NE", "J3"): 105,
    ("NE", "CG"): 190,
    ("CE", "CS"): 90,
    ("CE", "iOS"): 50,
    ("CE", "CG"): 265,
    ("CE", "CRL"): 100,
    ("CE", "J5"): 95,
    ("CC", "iOS"): 50,
    ("CC", "J5"): 95,
    ("CRL", "CG"): 220,
    ("CRL", "SL"): 100,
    ("CRL", "J5"): 50,
    ("J5", "TD"): 80,
    ("J5", "CL"): 230,
    ("J5", "SL"): 100,
    ("CL", "TD"): 170,
    ("SL", "C3"): 105,
    ("SL", "C2"): 80,
    ("SL", "TD"): 90,
    ("SL", "GA"): 140,
    ("TD", "C1"): 195,
    ("C1", "GA"): 160,
    ("C1", "ATL"): 100,
    ("C1", "C6"): 200,
    ("C6", "C5"): 250,
    ("C5", "ATL"): 10,
    ("C5", "C7"): 190,
    ("C7", "GC"): 60,
    ("GC", "GB"): 60,
    ("GC", "CT"): 75,
    ("GC", "CIR"): 90,
    ("CIR", "ATL"): 60,
    ("GA", "CIR"): 65,
    ("GA", "A"): 50,
    ("GA", "C2"): 85,
    ("A", "C2"): 100,
    ("A", "GC"): 65,
    ("A", "BQ"): 50,
    ("A", "GB"): 55,
    ("BQ", "C2"): 90,
    ("BQ", "GB"): 25,
    ("BQ", "A14CT"): 100,
    ("BQ", "CT"): 40,
    ("CT", "GB"): 25,
    ("CT", "BQ"): 35,
    ("CT", "A14CT"):90
}

# Agregar las ponderaciones (distancias) al grafo
for edge, weight in distances.items():
    if udlap.has_edge(*edge):
        udlap[edge[0]][edge[1]]['weight'] = weight

# Función para encontrar la ruta más corta usando Dijkstra
def shortest_path(graph, start, end):
    try:
        path = nx.dijkstra_path(graph, start, end, weight='weight')
        distance = nx.dijkstra_path_length(graph, start, end, weight='weight')
        return path, distance
    except nx.NetworkXNoPath:
        return None, float('inf')


# Función para manejar el botón de calcular
def calculate_route():
    start = start_node.get()
    end = end_node.get()
    if start and end:
        path, distance = shortest_path(udlap, start, end)
        if path:
            result.set(f"Ruta más corta: {' -> '.join(path)}\nDistancia: {distance} metros")
        else:
            result.set("No hay ruta disponible.")
    else:
        result.set("Por favor, selecciona los nodos.")


# Crear la ventana principal
window = tk.Tk()
window.title("Sistema de Navegación UDLAP")

# Etiqueta de instrucciones
tk.Label(window, text="Seleccione los nodos de inicio y destino:").pack(pady=10)

# Dropdown para el nodo de inicio
start_node = ttk.Combobox(window, values=list(udlap.nodes))
start_node.set("Nodo de Inicio")
start_node.pack(pady=5)

# Dropdown para el nodo de destino
end_node = ttk.Combobox(window, values=list(udlap.nodes))
end_node.set("Nodo de Destino")
end_node.pack(pady=5)

# Botón para calcular la ruta más corta
calculate_button = tk.Button(window, text="Calcular Ruta", command=calculate_route)
calculate_button.pack(pady=10)

# Etiqueta para mostrar los resultados
result = tk.StringVar()
result_label = tk.Label(window, textvariable=result, wraplength=400, justify="left")
result_label.pack(pady=10)

# Ejecutar la interfaz gráfica
window.mainloop()
