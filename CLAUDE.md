# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

Course materials for **CI-0202 Principios de Informática** at UCR (Universidad de Costa Rica). Content consists of Jupyter notebooks (lab exercises), Python exam practice problems (with solution files and automated test scripts), and supporting documents in Spanish.

## Course Knowledge

When you need to understand the course content to assist with code, refer to the [course syllabus](CI0202_Principios_I_2026.md) and the [repository structure](#repository-structure) sections below. The syllabus provides an overview of the course objectives, topics, and methodology, while the repository structure shows how materials are organized.

The topics are covered sequentially, starting with basic programming concepts and progressing to more advanced topics like data manipulation and visualization. Each lab exercise builds on previous ones, so understanding the progression is important for providing accurate exercises.

## Repository structure

```
material_practico/
├── labs/
│   ├── 1_fundamentos_de_la_programacion/    # Lab 1: Fundamentos de la programación
|   |   └── 1_fundamentos_de_la_programacion.ipynb
│   ├── 2_variables_y_valores/                # Lab 2: Variables y valores
|   |   └── 2_variables_y_valores.ipynb
│   ├── 3_operadores_y_expresiones/          # Lab 3: Operadores y expresiones
|   |   └── 3_operadores_y_expresiones.ipynb
│   ├── 5_entrada_y_salida_de_datos/          # Lab 5: Entrada y salida de datos, junto a manejo de errores
|   |   └── 5_entrada_y_salida_de_datos.ipynb
│   ├── 6_control_de_flujo_de_ejecucion/    # Lab 6: Control de flujo de ejecución
|   |   └── 6_control_de_flujo_de_ejecucion.ipynb
│   ├── 7_subrutinas/                        # Lab 7: Subrutinas
|   |   └── 7_subrutinas.ipynb
│   ├── 8_estructuras_de_datos_fundamentales/    # Lab 8: Estructuras de datos fundamentales
|   |   └── 8_estructuras_de_datos_fundamentales_parte_1.ipynb
│   ├── 9_introduccion_al_uso_de_bibliotecas/    # Lab 9: Introducción al uso de bibliotecas
|   |   └── 9_introduccion_al_uso_de_bibliotecas.ipynb
│   ├── 10_computacion_numerica/              # Lab 10: Computación numérica
|   |   └── 10_computacion_numerica.ipynb
│   ├── 11_manipulacion_de_archivos/          # Lab 11: Manipulación de archivos
|   |   └── 11_manipulacion_de_archivos.ipynb
│   └── 12_visualizacion_de_datos/              # Lab 12: Visualización de datos
|       └── 12_visualizacion_de_datos.ipynb
├── examenes/                            # Exam practice problems and solutions
|   ├── resources/                    # Logos
|   ├── examen_1/                    # Exam 1 practice problems
|   |   ├── enunciados
|   |   └── soluciones
|   ├── examen_2/                    # Exam 2 practice problems
|   |   ├── enunciados
|   |   └── soluciones
└── otros/                          # Style guides, methodology docs
```

## Doing Tests

To do automatic tests for the lab exercises, see the [doing-tests skill](.claude/skills/doing-tests/SKILL.md).
