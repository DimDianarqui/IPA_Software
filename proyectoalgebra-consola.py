"""
Este código implementa una versión SIMPLIFICADA del método IPA original,
enfocada en los conceptos de Álgebra Lineal que sustentan el algoritmo:

  1. Matriz de decisión D (n filas = FR, m columnas = NFR)
  2. Vector de pesos W de los NFR -> normalización -> NW
  3. Media geométrica ponderada por fila (combinación lineal en espacio
     logarítmico) -> vector R
  4. Normalización de R -> NR (vector de prioridad final)
  5. Ordenamiento descendente según NR
"""

from typing import List
import math


# ---------------------------------------------------------------------------
# 1. NORMALIZACIÓN DE VECTORES
# ---------------------------------------------------------------------------
def normalizar_vector(v: List[float]) -> List[float]:
    total = sum(v)
    if total == 0:
        raise ValueError("La suma del vector no puede ser 0 (no se puede normalizar).")
    return [x / total for x in v]


# ---------------------------------------------------------------------------
# 2. MEDIA GEOMÉTRICA PONDERADA (combinación lineal en espacio logarítmico)
# ---------------------------------------------------------------------------
def media_geometrica_ponderada(fila: List[float], pesos: List[float]) -> float:

    if len(fila) != len(pesos):
        raise ValueError("La fila y el vector de pesos deben tener la misma longitud.")

    ln_R = sum(w * math.log(d) for d, w in zip(fila, pesos) if d > 0)
    return math.exp(ln_R)


# ---------------------------------------------------------------------------
# 3. CÁLCULO COMPLETO DE PRIORIDADES (núcleo del método IPA simplificado)
# ---------------------------------------------------------------------------
def calcular_prioridades(
    matriz_D: List[List[float]],
    pesos_NFR: List[float],
    nombres_FR: List[str] = None,
    nombres_NFR: List[str] = None,
):

    n = len(matriz_D)          # número de requisitos funcionales (FR)
    m = len(matriz_D[0])       # número de requisitos no funcionales (NFR)

    if nombres_FR is None:
        nombres_FR = [f"FR{i+1}" for i in range(n)]
    if nombres_NFR is None:
        nombres_NFR = [f"NFR{j+1}" for j in range(m)]

    if len(pesos_NFR) != m:
        raise ValueError("El vector de pesos debe tener el mismo tamaño que las columnas de D.")

    # Paso 1: normalizar el vector de pesos de los NFR
    NW = normalizar_vector(pesos_NFR)

    # Paso 2: calcular R_i para cada requisito funcional (fila de D)
    R = [media_geometrica_ponderada(fila, NW) for fila in matriz_D]

    # Paso 3: normalizar R para obtener NR (vector de prioridad final)
    NR = normalizar_vector(R)

    # Paso 4: generar ranking (orden descendente por NR)
    ranking = sorted(
        zip(nombres_FR, NR),
        key=lambda par: par[1],
        reverse=True,
    )

    return {
        "NW": dict(zip(nombres_NFR, NW)),
        "R": dict(zip(nombres_FR, R)),
        "NR": dict(zip(nombres_FR, NR)),
        "ranking": ranking,
    }


# ---------------------------------------------------------------------------
# 4. IMPRESIÓN DE RESULTADOS EN FORMATO TABLA
# ---------------------------------------------------------------------------
def imprimir_resultados(resultado: dict) -> None:
    print("\n--- Vector de prioridad normalizado de los NFR (NW) ---")
    for nfr, valor in resultado["NW"].items():
        print(f"  {nfr:<10} NW = {valor:.4f}")

    print("\n--- Vector de prioridad final de los FR (NR) ---")
    for fr, valor in resultado["NR"].items():
        print(f"  {fr:<10} NR = {valor:.4f}")

    print("\n--- Ranking de prioridad (mayor a menor) ---")
    for posicion, (fr, valor) in enumerate(resultado["ranking"], start=1):
        print(f"  {posicion}. {fr:<10} (NR = {valor:.4f})")


# ---------------------------------------------------------------------------
# 5. EJEMPLO DE USO
# ---------------------------------------------------------------------------
if __name__ == "__main__":

    nombres_NFR = ["Seguridad", "Usabilidad", "Rendimiento"]
    nombres_FR = ["Login", "Reportes", "Pagos", "Notificaciones"]

    # Matriz de decisión D (filas = FR, columnas = NFR).
    # d_ij = grado de importancia del NFR j para lograr el FR i.
    # Escala sugerida: 1 (muy bajo) a 9 (muy alto), estilo Saaty/AHP.
    matriz_D = [
        # Seguridad, Usabilidad, Rendimiento
        [9, 4, 3],   # Login
        [3, 6, 5],   # Reportes
        [9, 5, 7],   # Pagos
        [2, 7, 4],   # Notificaciones
    ]

    # Vector de pesos iniciales W de los NFR (importancia relativa entre ellos,
    # definida por el equipo/cliente). Se normalizará automáticamente.
    pesos_NFR = [5, 3, 2]

    resultado = calcular_prioridades(
        matriz_D=matriz_D,
        pesos_NFR=pesos_NFR,
        nombres_FR=nombres_FR,
        nombres_NFR=nombres_NFR,
    )

    imprimir_resultados(resultado)