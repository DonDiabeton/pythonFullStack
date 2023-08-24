# pythonFullStack
Bootcamp iniciado el año 2023 en AML.

## Crear entorno virtual con "virtualenv"

crear entorno virtual.
```bash
virtualenv env
```

activamos el entorno virtual
```bash
env\Scripts\activate.bat  
```

instalamos requirements.txt en el entorno virtual
```bash
python -m pip install -r requirements.txt
```

## Commit desde bash

Para ver las modificaciones. 
```bash
git status
```
Para confirmar los cambios.
```bash
git add .
```
Para hacer el commit con comentario.
```bash
git commit -m "commit desde bash"
```
Para subir la actualizacion.
```bash
git push origin main
```

## Para trabajar con VIRTUALENV

1. debemos instalar virtualenv `pip install virtualenv`
2. creamos el entorno virtual `virtualenv env`

3. activar entorno `env\Scripts\activate.bat`
4. desactivar entorno `deactivate`


python -m pip freeze > requirements.txt

python -m pip install -r requirements.txt