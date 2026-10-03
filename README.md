# 🚀 Mi Blog con Django — Preentrega 8

---

## 💡 ¿De qué trata este proyecto?

El objetivo principal es construir una plataforma web limpia, modular y fácil de navegar. En esta entrega en particular, trabajé sobre el patrón MVT (Modelo - Vista - Template) de Django implementando:

- 🧩 **Herencia de plantillas (`base.html`)**: Diseñé una plantilla madre que contiene el encabezado, el menú de navegación y el pie de página comunes. De esta forma, cada página hija solo define su contenido específico sin repetir código innecesario.
- ⚙️ **Vistas dinámicas (`views.py`)**: Funciones que reciben las peticiones del usuario y devuelven las páginas renderizadas junto con su contexto.
- 🧭 **Rutas organizadas (`urls.py`)**: Mapeo limpio y modular, separando las URLs generales del proyecto de las rutas específicas de la aplicación `posts`.
- 🎨 **Diseño visual (`estilos.css`)**: Integración de archivos estáticos para lograr una interfaz moderna, prolija y agradable tanto en computadoras como en dispositivos móviles.

---

---

## 📁 ¿Cómo está organizado el proyecto?

Así está estructurado el código dentro del repositorio:


blog_django/
├── blog_project/           # Configuración central del proyecto Django
│   ├── settings.py         # Configuración general y de archivos estáticos
│   ├── urls.py             # Enrutador principal (incluye a posts.urls)
│   ├── wsgi.py
│   └── asgi.py
├── posts/                  # Aplicación principal del blog
│   ├── static/             # Archivos estáticos de diseño
│   │   └── posts/
│   │       └── css/
│   │           └── estilos.css   # Estilos visuales del sitio
│   ├── templates/          # Plantillas HTML
│   │   └── posts/
│   │       ├── base.html         # Plantilla madre (estructura y navegación común)
│   │       ├── inicio.html       # Página de inicio y bienvenida
│   │       └── acerca.html       # Página sobre el autor y el proyecto
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py             # Rutas propias de la app posts
│   └── views.py            # Lógica y renderizado de las vistas
├── .gitignore              # Archivos y carpetas ignorados por Git
├── db.sqlite3              # Base de datos SQLite local
├── manage.py               # Comando de administración de Django
├── README.md               # Esta documentación
└── requirements.txt        # Librerías y dependencias necesarias


## 💻 ¿Cómo correr este proyecto en tu máquina?

Si querés probar el blog en tu entorno local, podés seguir estos pasos:

### 1. Clonar el repositorio

git clone <url-de-tu-repositorio>
cd blog_django


### 2. Crear y activar tu entorno virtual

# En Windows:
python -m venv venv
venv\Scripts\activate

# En Linux o MAC
python3 -m venv venv
source venv/bin/activate


### 3. Instalar las dependencias

pip install -r requirements.txt
```

### 4. Aplicar las migraciones iniciales

python manage.py migrate
```

### 5. Encender el servidor

python manage.py runserver


Una vez iniciado, abrí tu navegador y visitá:  
👉 **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

---