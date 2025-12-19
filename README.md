# Kadir Kevin Castillo Ancco
# AdoptaApp - Examen Final

Implementación del módulo **Galería de Momentos** para cada mascota.

## Funcionalidades agregadas
- Modelo `PostMascota` con relación ForeignKey a Mascota
- Campo foto obligatorio (ImageField)
- Formulario con validaciones:
  - Descripción mínima 20 caracteres
  - Fecha no futura
- Vista `posts_mascota` con manejo GET/POST
- Plantilla responsive con Bootstrap mostrando galería en cards
- Botón en detalle de mascota para acceder a la galería
- Subida de imágenes funcional

## Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Git

## Instalación y Configuración

### 1. Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd miRedSocial
```

### 2. Crear entorno virtual

**En Windows:**
```bash
python -m venv venv
```

**En Linux/Mac:**
```bash
python3 -m venv venv
```

### 3. Activar el entorno virtual

**En Windows:**
```bash
venv\Scripts\activate
```

**En Linux/Mac:**
```bash
source venv/bin/activate
```

### 4. Actualizar pip (recomendado)

```bash
python -m pip install --upgrade pip
```

### 5. Instalar dependencias

Si existe `requirements.txt`:
```bash
pip install -r requirements.txt
```

Si no existe, instalar las dependencias manualmente:
```bash
pip3 install django
pip3 install djangorestframework
pip3 install djangorestframework-simplejwt
pip3 install pillow
pip3 install django-cors-headers
pip3 install channels
pip3 install channels-redis
```

### 6. Configurar la base de datos

Aplicar las migraciones:
```bash
python manage.py migrate
```

### 7. Crear un superusuario (opcional)

Para acceder al panel de administración:
```bash
python manage.py createsuperuser
```

Sigue las instrucciones en pantalla para crear tu usuario administrador.

### 8. Ejecutar el servidor de desarrollo

```bash
python manage.py runserver
```

El servidor estará disponible en: `http://127.0.0.1:8000/`

## Acceso a la Aplicación

- **Aplicación principal:** http://127.0.0.1:8000/
- **Panel de administración:** http://127.0.0.1:8000/admin/


## Comandos Útiles

### Crear migraciones después de cambios en modelos
```bash
python manage.py makemigrations
```

### Aplicar migraciones
```bash
python manage.py migrate
```

### Crear un nuevo superusuario
```bash
python manage.py createsuperuser
```

## Desactivar el Entorno Virtual

Cuando termines de trabajar:
```bash
deactivate
```

```

### El servidor no inicia

1. Verifica que el entorno virtual esté activado
2. Asegúrate de estar en la carpeta raíz del proyecto
3. Verifica que todas las dependencias estén instaladas

## Tecnologías Utilizadas

- **Django** - Framework web de Python
- **Django REST Framework** - API REST
- **Django REST Framework SimpleJWT** - Autenticación JWT
- **Pillow** - Procesamiento de imágenes
- **Channels** - WebSockets para chat en tiempo real
- **SQLite** - Base de datos (desarrollo)

## Contribuir

1. Haz fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Agrega nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crea un Pull Request

## Licencia

Este proyecto es parte de un curso educativo de PUCP.

## Contacto

Para preguntas o sugerencias sobre el proyecto, contacta al equipo de desarrollo.