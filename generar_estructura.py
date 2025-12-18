import os
from pathlib import Path

def ignorar_carpeta(nombre_carpeta: str, ruta_actual: Path) -> bool:
    carpetas_ignoradas = {'node_modules', '.git', '.next', '__pycache__', '.venv', 'venv', '.env'}
    return nombre_carpeta in carpetas_ignoradas

def es_archivo_a_mostrar(archivo: str, ruta_padre: Path) -> bool:
    extensiones_ocultas = {'.pyc', '.log', '.tmp'}
    if Path(archivo).suffix in extensiones_ocultas:
        return False
    return True

def generar_estructura(ruta: Path, prefijo: str = '', resultado: list = None) -> list:
    if resultado is None:
        resultado = []

    try:
        elementos = sorted(ruta.iterdir(), key=lambda x: (not x.is_dir(), x.name.lower()))
    except PermissionError:
        return resultado

    elementos_visibles = []
    for elemento in elementos:
        if elemento.name.startswith('.'):  # ignorar ocultos
            continue
        if elemento.is_dir() and ignorar_carpeta(elemento.name, ruta):
            continue
        if not elemento.is_dir() and not es_archivo_a_mostrar(elemento.name, ruta):
            continue
        elementos_visibles.append(elemento)

    for indice, elemento in enumerate(elementos_visibles):
        es_ultimo = indice == len(elementos_visibles) - 1
        conector = '└── ' if es_ultimo else '├── '
        nuevo_prefijo = prefijo + ('    ' if es_ultimo else '│   ')

        nombre_mostrar = elemento.name

        resultado.append(prefijo + conector + nombre_mostrar)

        if elemento.is_dir():  # Aquí usamos .is_dir() que sí existe en versiones modernas
            generar_estructura(elemento, nuevo_prefijo, resultado)

    return resultado

def main():
    raiz_proyecto = Path.cwd()
    nombre_carpeta_raiz = raiz_proyecto.name

    estructura = [f"{nombre_carpeta_raiz}/"]

    lineas = generar_estructura(raiz_proyecto)
    estructura.extend(lineas)

    archivo_salida = raiz_proyecto / 'estructura.txt'
    archivo_salida.write_text('\n'.join(estructura), encoding='utf-8')

    print(f"Estructura del proyecto generada correctamente en: {archivo_salida}")

if __name__ == '__main__':
    main()