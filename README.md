# Proyecto Efex: Preguntas 1, 2 y 3

Este repositorio contiene tres subproyectos que resuelven problemas distintos, organizados en las carpetas `pregunta_1`, `pregunta_2`, y `pregunta_3`.

---

## Requisitos

- Python 3.x
- Las dependencias están listadas en el archivo `requirements.txt`.

## Instalación

1. Clona este repositorio:
   ```bash
   git clone [URL del repositorio]
   ```
2. Navega a la carpeta principal del proyecto:
   ```bash
   cd project_efex
   ```
3. Crea un entorno virtual (opcional pero recomendado):
   - En macOS/Linux:
     ```bash
     python3 -m venv env
     source env/bin/activate
     ```
   - En Windows:
     ```bash
     python -m venv env
     .envScriptsactivate
     ```
4. Instala las dependencias desde el archivo `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

---

## Pregunta 1

### Descripción

Este subproyecto resuelve el problema planteado en `pregunta_1`.

### Uso

Para ejecutar el subproyecto de la carpeta `pregunta_1`, utiliza el siguiente comando:

```bash
cd pregunta_1
python main.py
```

### Pruebas

Para ejecutar las pruebas unitarias del subproyecto `pregunta_1`, usa el siguiente comando:

```bash
python -m unittest test_main.py
```

---

## Pregunta 2

### Descripción

Este subproyecto resuelve el problema planteado en `pregunta_2`.

### Uso

Para ejecutar el subproyecto de la carpeta `pregunta_2`, utiliza el siguiente comando:

```bash
cd pregunta_2
python main.py
```

### Pruebas

Para ejecutar las pruebas unitarias del subproyecto `pregunta_2`, usa el siguiente comando:

```bash
python -m unittest test_main.py
```

---

## Pregunta 3 (Django)

### Descripción

Este subproyecto es una aplicación Django que resuelve el problema planteado en `pregunta_3`.

### Uso

1. Navega a la carpeta del subproyecto `pregunta_3`:
   ```bash
   cd pregunta_3
   ```
2. Realiza las migraciones de la base de datos:
   ```bash
   python manage.py migrate
   ```
3. Inicia el servidor Django localmente:
   ```bash
   python manage.py runserver
   ```

### Pruebas

Para ejecutar las pruebas del subproyecto `pregunta_3`, usa el siguiente comando:

```bash
python manage.py test
```

---

## Licencia

Este repositorio está bajo la licencia MIT. Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para mejoras.
