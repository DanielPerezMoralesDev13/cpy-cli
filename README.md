<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/DanielPerezMoralesDev13 -->
<!-- Correo electrónico: danielperezdev@proton.me  -->
# ***CP - Implementation of the cp command in Python***

*This script implements a basic version of the `cp` command in Python, which allows copying files and directories recursively if necessary. This implementation is useful when the `cp` command is not available or custom functionality is needed.*

## ***Usage***

*To execute the script, simply call `cp.py` with the following arguments:*

```bash
python3 cp.py [-h] [-o] [-i] [-r] [-v] source destination
```

### ***Arguments***

- *`source`: Source directory or file to be copied.*

- *`destination`: Destination directory or file where `source` will be copied.*

#### ***Options***

- *`-h`, `--help`: Show a help message and exit.*

- *`-o`, `--override`: Override destination files if they already exist.*

- *`-i`, `--interactive`: Ask if you want to overwrite the file if it already exists in the destination.*

- *`-r`, `--recursive`: Copy directories recursively.*

- *`-v`, `--verbose`: Provide details about the actions being performed.*

## ***Usage Examples***

1. *Copy a file:*

    ```bash
    python3 cp.py file.txt new_directory/
    ```

2. *Copy a directory recursively:*

    ```bash
    python3 cp.py -r directory/ new_directory/
    ```

3. *Copy a file overwriting the destination if it already exists:*

    ```bash
    python3 cp.py -o file.txt existing_directory/
    ```

4. *Copy an interactive file:*

```bash
python3 cp.py -i file.txt existing_directory/
```

## ***Author***

- ***Author:** Daniel Benjamin Perez Morales*

- ***GitHub:** [DanielPerezMoralesDev13](https://github.com/DanielPerezMoralesDev13)*

- ***Email:** <danielperezdev@proton.me>*
