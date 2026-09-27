# IPA Simplificado — Priorización de Requisitos con Álgebra Lineal

Aplicación interactiva construida con **Python + Gradio** que implementa una versión simplificada del método **IPA (Integrated Prioritization Approach)**, usado para priorizar requisitos funcionales (FR) frente a requisitos no funcionales (NFR) en el desarrollo de software mediante conceptos de álgebra lineal: matrices, vectores, normalización y combinación lineal (media geométrica ponderada).

Proyecto de aula — **Álgebra Lineal (16133), Grupo 6**
Universidad de Santander (UDES) — Bucaramanga, noviembre 2026
Profesora: Andrea Fernanda Muñoz Potosi

**Autores:**
- Ardila Quintero Diego Andrés — Ing. Software
- Keyner Steven García Anaya — Ing. Software
- Sebastián Soto Mora — Ing. Software

---

## 📖 Contexto

Al desarrollar software es necesario decidir **en qué orden** atender los requisitos: no todos los requisitos funcionales aportan lo mismo al cumplimiento de los requisitos no funcionales (seguridad, usabilidad, rendimiento, etc.). El artículo de Dabbagh & Lee (2014) propone el método IPA para resolver esto con una sola matriz de requisitos.

Este proyecto toma el núcleo algebraico de ese método —dejando fuera la parte de lógica difusa (números difusos triangulares y Alpha-Cut), que no pertenece al álgebra lineal— y lo implementa en una interfaz que se puede ajustar en vivo durante la sustentación.

## 🧮 Fundamento matemático

1. **Matriz de decisión D** (n × m): las filas son los FR, las columnas los NFR. Cada celda `d_ij` indica qué tan importante es el NFR `j` para lograr el FR `i` (escala sugerida 1–9).
2. **Vector de pesos W**: importancia relativa entre los NFR, definida por el equipo/cliente.
3. **Normalización** (`NW = W / Σ W`): garantiza que los pesos sumen 1.
4. **Media geométrica ponderada** por fila:

   ```
   R_i = ∏ (d_ij ^ NW_j)         para j = 1..m
   ```

   equivalente, en espacio logarítmico, a la combinación lineal:

   ```
   Ln(R_i) = Σ NW_j · Ln(d_ij)
   ```

5. **Normalización final** (`NR = R / Σ R`): da el vector de prioridad de los FR, con valores en `[0, 1]` que suman 1.
6. **Ranking**: orden descendente de `NR`.

## ✨ Funcionalidades de la app

- Define cuántos FR y NFR quieres comparar (sliders).
- Nombra cada requisito.
- Edita la matriz de decisión D y los pesos de los NFR directamente en una tabla interactiva.
- Calcula el ranking en tiempo real con un gráfico de barras y una tabla de resultados.

## 🚀 Instalación y ejecución

```bash
# Clonar el repositorio
git clone <URL-de-este-repositorio>
cd <nombre-del-repositorio>

# Instalar dependencias
pip install gradio pandas matplotlib

# Ejecutar la aplicación
python app.py
```

Se abrirá automáticamente en el navegador en `http://127.0.0.1:7860`.

> Si quieres generar un enlace público temporal para compartir la demo (por ejemplo, durante la sustentación), cambia la última línea del archivo por:
> ```python
> demo.launch(share=True)
> ```

## 📂 Estructura del repositorio

```
.
├── proyectoalgebra-interfaz-AnexoA.py       # Aplicación de Gradio (Interfaz + Lógica del método IPA)
├── proyectoalgebra-consola-AnexoB.py         # Aplicación en consola (lógica del método IPA) para comprobar los resultados obtenidos
└── README.md        # Este archivo
```

## 🖥️ Cómo usar la interfaz

1. Ajusta el número de FR y NFR con los sliders.
2. Escribe los nombres de cada uno (separados por coma).
3. Pulsa **"Generar tabla"**.
4. En la tabla, edita los valores de la matriz D (1–9) para cada FR frente a cada NFR.
5. En la **última fila** de la tabla, ingresa los pesos de importancia de cada NFR (no es un requisito funcional, es el vector `W`).
6. Pulsa **"Calcular prioridades"** para ver el ranking, el gráfico y el detalle de resultados.

## 📚 Referencia principal

Dabbagh, M., & Lee, S. P. (2014). An approach for integrating the prioritization of functional and nonfunctional requirements. *The Scientific World Journal*, 2014, 1–18. https://doi.org/10.1155/2014/737626

## 📝 Licencia

Proyecto académico con fines educativos — Universidad de Santander (UDES).
