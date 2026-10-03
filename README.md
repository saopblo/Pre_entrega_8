# Blog Project — Base Inicial de Django (Preentrega 7)

Este repositorio contiene la estructura base y la configuración inicial de una aplicación web de blog desarrollada con **Django** y **Python**.

---

## 📝 Descripción del Proyecto

Incluye:

- La arquitectura inicial del proyecto Django (`blog_project`)
- La creación y registro de una aplicación principal (`posts`)
- La configuración regional en español
- La preparación del entorno con control de versiones mediante Git y GitHub

---

## 📁 Estructura del Repositorio

/
├── blog_project/       # Configuración principal del proyecto Django (settings.py, urls.py, wsgi.py)
├── posts/              # Aplicación inicial
├── .gitignore          # Archivo para excluir archivos locales y temporales de Git
├── db.sqlite3          # Base de datos SQLite (generada automáticamente)
├── manage.py           # Script principal para la administración de Django
├── README.md           # Documentación técnica e instrucciones del repositorio
└── requirements.txt    # Lista de dependencias del proyecto
```

---

## ⚙️ Requisitos

- Python 3.14.6
- Django 6.1.1

Dependencias completas en `requirements.txt`:

```
asgiref==3.12.1
Django==6.1.1
sqlparse==0.6.0
tzdata==2026.4
```

---

## Instalación

1. **Clonar el repositorio**
   ```
   git clone <url-del-repositorio>
   cd blog_django
   ```

2. **Crear y activar el entorno virtual**
   ```
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS / Linux
   source venv/bin/activate
   ```

3. **Instalar dependencias**
   ```
   pip install -r requirements.txt
   ```

4. **Aplicar migraciones**
   ```
   python manage.py migrate
   ```

5. **Correr el servidor de desarrollo**
   ```
   python manage.py runserver
   ```

   El proyecto estará disponible en: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---