# Enunciados

Los enunciados acá presentados son prácticas de exámen.

## Conversión a latex

Para convertir los MD a un PDF en latex, se puede ejecutar el comando:

```sh
pandoc <practica_de_examen_#.md> -o <practica_de_examen_#.pdf> --include-in-header=header.tex --pdf-engine=xelatex
```

Esto genera un PDF con la práctica de exámen en PDF.
