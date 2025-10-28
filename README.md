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


* que mejoraria? integraria ia para una busqueda y clasificacion eficiente de tareas, agregaria la carga de archivos PDF, CSV o XLS, crearia un resumen de la tarea en si, con crearia el resumen de un archivo cargado.

* Si tuviste que hacer trade-offs, ¿cuáles y por qué? preferi la simplicidad para lograr el tiempo estimado, ocupe el cdn de Tailwind para simplificar el css y la api la desarrolle con DRF por que es lo que mas manejo y por su simplicidad, priorize la confianza que tengo en DRF.

