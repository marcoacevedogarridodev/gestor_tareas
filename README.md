# Gestor de Tareas 

* 2. Crear entorno virtual
python -m venv venv

* 3. Activar entorno virtual
* Linux/Mac:
source venv/bin/activate

* Windows:
venv\Scripts\activate

* 4. Instalar dependencias
pip install -r requirements.txt

* 5. Configurar base de datos
python manage.py makemigrations tareas
python manage.py migrate

* 6. Cargar datos de ejemplo
python manage.py crear_tareas_ejemplo

* 7. Ejecutar servidor
python manage.py runserver

* 8. Abrir en navegador
* http://localhost:8000/tareas/