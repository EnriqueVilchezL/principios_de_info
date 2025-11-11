# ===================================================================
# Sistema de Calificación Modular y Configurable
# ===================================================================
from typing import Callable


class GrupoCalificacion:
    """Representa un grupo de pruebas con un valor total configurable.

    Este diseño modular permite tener múltiples grupos de pruebas
    (básicas, extras, bonificaciones) cada uno con su propio valor.
    """

    def __init__(self, nombre: str, valor_maximo: float):
        """Inicializa un grupo de calificación.

        Args:
            nombre: Nombre descriptivo del grupo (ej: "Funciones Básicas")
            valor_maximo: Valor máximo en % que vale este grupo (ej: 5.0 para 5%)
        """
        self.nombre = nombre
        self.valor_maximo = valor_maximo
        self.pruebas_pasadas: list[tuple[str, float]] = []
        self.pruebas_fallidas: list[tuple[str, float]] = []
        self.pruebas_no_implementadas: list[tuple[str, float]] = []
        self.num_pruebas_registradas = 0

    def registrar_prueba(self, nombre_prueba: str, funcion_prueba: Callable) -> bool:
        """Registra y ejecuta una prueba, calculando su valor automáticamente.

        Args:
            nombre_prueba: Nombre descriptivo de la prueba
            funcion_prueba: Función que ejecuta la prueba

        Returns:
            bool: True si la prueba pasó, False en caso contrario
        """
        self.num_pruebas_registradas += 1
        try:
            funcion_prueba()
            self.pruebas_pasadas.append((nombre_prueba, 0.0))
            print(f"✓ {nombre_prueba}: PASÓ")
            return True
        except NotImplementedError:
            self.pruebas_no_implementadas.append((nombre_prueba, 0.0))
            print(f"✗ {nombre_prueba}: FALTA IMPLEMENTACIÓN")
            return False
        except AssertionError as e:
            self.pruebas_fallidas.append((nombre_prueba, 0.0))
            print(f"✗ {nombre_prueba}: FALLÓ - {str(e)}")
            return False
        except Exception as e:
            self.pruebas_fallidas.append((nombre_prueba, 0.0))
            print(f"✗ {nombre_prueba}: ERROR - {type(e).__name__}: {str(e)}")
            return False

    def _recalcular_puntos(self):
        """Recalcula los puntos de todas las pruebas de forma equitativa."""
        if self.num_pruebas_registradas == 0:
            return

        valor_por_prueba = self.valor_maximo / self.num_pruebas_registradas

        # Actualizar todos los valores
        self.pruebas_pasadas = [(n, valor_por_prueba) for n, _ in self.pruebas_pasadas]
        self.pruebas_fallidas = [
            (n, valor_por_prueba) for n, _ in self.pruebas_fallidas
        ]
        self.pruebas_no_implementadas = [
            (n, valor_por_prueba) for n, _ in self.pruebas_no_implementadas
        ]

    def calcular_nota(self) -> tuple[float, float]:
        """Calcula la nota obtenida y el máximo posible.

        Returns:
            tuple[float, float]: (nota_obtenida, valor_maximo)
        """
        nota_obtenida = sum(puntos for _, puntos in self.pruebas_pasadas)
        return nota_obtenida, self.valor_maximo

    def obtener_estadisticas(self) -> dict:
        """Obtiene estadísticas detalladas del grupo.

        Returns:
            dict: Diccionario con estadísticas
        """
        nota_obtenida, _ = self.calcular_nota()
        total_pruebas = (
            len(self.pruebas_pasadas)
            + len(self.pruebas_fallidas)
            + len(self.pruebas_no_implementadas)
        )

        return {
            "nombre": self.nombre,
            "nota_obtenida": nota_obtenida,
            "valor_maximo": self.valor_maximo,
            "total_pruebas": total_pruebas,
            "pasadas": len(self.pruebas_pasadas),
            "fallidas": len(self.pruebas_fallidas),
            "no_implementadas": len(self.pruebas_no_implementadas),
            "porcentaje": (nota_obtenida / self.valor_maximo * 100)
            if self.valor_maximo > 0
            else 0,
        }

    def mostrar_resumen(self, verbose: bool = True):
        """Muestra el resumen de este grupo.

        Args:
            verbose: Si False, solo muestra estadísticas sin detalles de cada prueba
        """
        self._recalcular_puntos()

        stats = self.obtener_estadisticas()

        print(f"\n{'─' * 70}")
        print(f"📦 {self.nombre}")
        print(f"{'─' * 70}")
        print(f"Valor: {stats['nota_obtenida']:.2f}% / {stats['valor_maximo']:.2f}%")
        print(
            f"Pruebas: {stats['pasadas']}/{stats['total_pruebas']} pasadas "
            f"({stats['porcentaje']:.1f}%)"
        )

        # Solo mostrar detalles si verbose=True
        if not verbose:
            return

        if self.pruebas_pasadas:
            print(f"\n  ✓ Pasadas ({len(self.pruebas_pasadas)}):")
            for nombre, puntos in self.pruebas_pasadas:
                print(f"    • {nombre}: +{puntos:.3f}%")

        if self.pruebas_fallidas:
            print(f"\n  ✗ Fallidas ({len(self.pruebas_fallidas)}):")
            for nombre, puntos in self.pruebas_fallidas:
                print(f"    • {nombre}: 0/{puntos:.3f}%")

        if self.pruebas_no_implementadas:
            print(f"\n  ⚠ Sin Implementar ({len(self.pruebas_no_implementadas)}):")
            for nombre, puntos in self.pruebas_no_implementadas:
                print(f"    • {nombre}: 0/{puntos:.3f}%")


class SistemaCalificacion:
    """Sistema de calificación que maneja múltiples grupos de pruebas."""

    def __init__(self):
        """Inicializa el sistema de calificación."""
        self.grupos: list[GrupoCalificacion] = []
        self._grupos_por_nombre: dict[str, GrupoCalificacion] = {}

    def crear_grupo(self, nombre: str, valor_maximo: float) -> GrupoCalificacion:
        """Crea y registra un nuevo grupo de calificación.

        Si ya existe un grupo con ese nombre, lo retorna sin crear duplicado.

        Args:
            nombre: Nombre del grupo
            valor_maximo: Valor máximo en % que vale este grupo

        Returns:
            GrupoCalificacion: El grupo creado o existente
        """
        # Evitar duplicados - retornar el existente si ya existe
        if nombre in self._grupos_por_nombre:
            return self._grupos_por_nombre[nombre]

        grupo = GrupoCalificacion(nombre, valor_maximo)
        self.grupos.append(grupo)
        self._grupos_por_nombre[nombre] = grupo
        return grupo

    def limpiar(self):
        """Limpia todos los grupos registrados. Útil para reiniciar el sistema."""
        self.grupos.clear()
        self._grupos_por_nombre.clear()

    def calcular_nota_total(self) -> tuple[float, float]:
        """Calcula la nota total de todos los grupos.

        Returns:
            tuple[float, float]: (nota_obtenida_total, valor_maximo_total)
        """
        nota_total = sum(grupo.calcular_nota()[0] for grupo in self.grupos)
        valor_total = sum(grupo.calcular_nota()[1] for grupo in self.grupos)
        return nota_total, valor_total

    def mostrar_resumen_completo(self, verbose: bool = False):
        """Muestra el resumen completo de todos los grupos.

        Args:
            verbose: Si True, muestra el detalle de todas las pruebas.
                    Si False (default), solo muestra estadísticas resumidas.
        """
        print("\n" + "=" * 70)
        print("📊 RESUMEN DE CALIFICACIÓN COMPLETO")
        print("=" * 70)

        for grupo in self.grupos:
            grupo.mostrar_resumen(verbose=verbose)

        nota_total, valor_total = self.calcular_nota_total()

        print("\n" + "=" * 70)
        print(f"🎓 NOTA FINAL: {nota_total:.2f}% / {valor_total:.2f}%")

        if valor_total > 0:
            porcentaje_global = (nota_total / valor_total) * 100
            print(f"📈 Porcentaje de Completitud Global: {porcentaje_global:.1f}%")

            # Mensaje motivacional
            if porcentaje_global == 100:
                print("🌟 ¡PERFECTO! Todas las funciones implementadas correctamente.")
            elif porcentaje_global >= 90:
                print("🎉 ¡EXCELENTE! Casi perfecto.")
            elif porcentaje_global >= 75:
                print("👏 ¡MUY BIEN! Buen trabajo.")
            elif porcentaje_global >= 50:
                print("👍 Buen progreso. Sigue adelante.")
            else:
                print("💪 Continúa trabajando. ¡Tú puedes!")

        print("=" * 70)

    def mostrar_resumen_por_seccion(self):
        """Muestra un resumen compacto agrupado por secciones (Parte 1, Parte 2, etc.)"""
        print("\n" + "=" * 70)
        print("📊 RESUMEN POR SECCIÓN")
        print("=" * 70)

        # Primero recalcular puntos de TODOS los grupos
        for grupo in self.grupos:
            grupo._recalcular_puntos()

        # Agrupar por "Parte"
        parte1 = [g for g in self.grupos if not g.nombre.startswith("Parte 2")]
        parte2 = [g for g in self.grupos if g.nombre.startswith("Parte 2")]

        def mostrar_seccion(nombre: str, grupos: list[GrupoCalificacion]):
            if not grupos:
                return

            nota_seccion = sum(g.calcular_nota()[0] for g in grupos)
            valor_seccion = sum(g.calcular_nota()[1] for g in grupos)
            total_pruebas = sum(
                g.obtener_estadisticas()["total_pruebas"] for g in grupos
            )
            pruebas_pasadas = sum(g.obtener_estadisticas()["pasadas"] for g in grupos)

            porcentaje = (
                (nota_seccion / valor_seccion * 100) if valor_seccion > 0 else 0
            )

            # Determinar símbolo según progreso
            if porcentaje == 100:
                simbolo = "✅"
            elif porcentaje >= 50:
                simbolo = "🔄"
            else:
                simbolo = "❌"

            print(f"\n{simbolo} {nombre}")
            print(f"   Nota: {nota_seccion:.2f}% / {valor_seccion:.2f}%")
            print(f"   Pruebas: {pruebas_pasadas}/{total_pruebas} ({porcentaje:.1f}%)")

            for grupo in grupos:
                stats = grupo.obtener_estadisticas()
                print(
                    f"      • {grupo.nombre}: {stats['nota_obtenida']:.2f}% / {stats['valor_maximo']:.2f}%"
                )

        mostrar_seccion("PARTE 1: Implementación NumpyLess", parte1)
        mostrar_seccion("PARTE 2: Benchmarking y Análisis", parte2)

        # Total
        nota_total, valor_total = self.calcular_nota_total()
        porcentaje_global = (nota_total / valor_total * 100) if valor_total > 0 else 0

        print("\n" + "─" * 70)
        print(
            f"🎓 CALIFICACIÓN TOTAL: {nota_total:.2f}% / {valor_total:.2f}% ({porcentaje_global:.1f}%)"
        )
        print("=" * 70)
