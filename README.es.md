<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/DanielPerezMoralesDev13 -->
<!-- Correo electrónico: danielperezdev@proton.me  -->
# ***CP - Implementación del comando cp en Python***

*Este script implementa una versión basica del comando `cp` en Python, que permite copiar ficheros y directorios de manera recursiva si es necesario. Esta implementación es útil cuando el comando `cp` no está disponible o se necesita una funcionalidad personalizada.*

## ***Uso***

*Para ejecutar el script, simplemente llama a `cp.py` con los siguientes argumentos:*

```bash
python3 cp.py [-h] [-o] [-i] [-r] [-v] source destination
```

### ***Argumentos***

- *`source`: Directorio o archivo de origen que se copiará.*

- *`destination`: Directorio o archivo de destino donde se copiará `source`.*

#### ***Opciones***

- *`-h`, `--help`: Muestra un mensaje de ayuda y sale.*

- *`-o`, `--override`: Sobrescribe los ficheros de destino si ya existen.*

- *`-i`, `--interactive`: Pregunta si se desea sobrescribir el archivo si ya existe en el destino.*

- *`-r`, `--recursive`: Copia los directorios de forma recursiva.*

- *`-v`, `--verbose`: Proporciona detalles sobre las acciones que se están realizando.*

## ***Ejemplos de Uso***

1. *Copiar un archivo:*

    ```bash
    python3 cp.py file.txt new_directory/
    ```

2. *Copiar un directorio recursivamente:*

    ```bash
    python3 cp.py -r directory/ new_directory/
    ```

3. *Copiar un archivo sobrescribiendo el destino si ya existe:*

    ```bash
    python3 cp.py -o file.txt existing_directory/
    ```

4. *Copiar un archivo interactivo:*

```bash
python3 cp.py -i file.txt existing_directory/
```

## ***Autor***

- ***Autor:** Daniel Benjamin Perez Morales*

- ***GitHub:** [DanielPerezMoralesDev13](https://github.com/DanielPerezMoralesDev13)*

- ***Correo electrónico:** <danielperezdev@proton.me>*
