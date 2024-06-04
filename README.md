<!-- Author: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/DanielPerezMoralesDev13 -->
<!-- Email: danielperezdev@proton.me  -->
# ***CPY - Python Implementation of the cp Command***

*This script implements a basic version of the `cp` command in Python, allowing to copy files and directories recursively if needed. This implementation is useful when the `cp` command is not available or custom functionality is required.*

## ***Usage***

*To run the script, simply call `cpy.py` with the following arguments:*

```bash
python3 cpy.py [-h] [-o] [-i] [-r] [-v] source destination
```

### ***Arguments***

- *`source`: Source directory or file to be copied.*

- *`destination`: Destination directory or file where `source` will be copied to.*

#### ***Options***

- *`-h`, `--help`: Display help message and exit.*

- *`-o`, `--override`: Override destination files if they already exist.*

- *`-i`, `--interactive`: Ask whether to overwrite the file if it already exists in the destination.*

- *`-r`, `--recursive`: Copy directories recursively.*

- *`-v`, `--verbose`: Provide details about actions being performed.*

## ***Examples***

1. *Copy a file:*

    ```bash
    python3 cpy.py file.txt new_directory/
    ```

2. *Copy a directory recursively:*

    ```bash
    python3 cpy.py -r directory/ new_directory/
    ```

3. *Copy a file overwriting the destination if it already exists:*

    ```bash
    python3 cpy.py -o file.txt existing_directory/
    ```

4. *Copy a file interactively:*

```bash
python3 cpy.py -i file.txt existing_directory/
```

## ***Binary Generation***

*To generate the CP binary, follow these steps:*

### ***Python, Pip, Pyinstaller Installation on Apt-based Systems (Ubuntu, Debian):***

- *Download and install Python from [Python3](https://www.python.org/downloads/).*

- **Python:**

    ```bash
    sudo apt-get update
    sudo apt-get -y upgrade 
    sudo apt-get install -y python3
    ```

- **Install pip:**

- *If you're using a recent version of Python (from version 3.4 onwards), pip should already be installed. Otherwise, follow the instructions at [pip3](https://pip.pypa.io/en/stable/installation/) to install pip.*

- **pip:**

    ```bash
    sudo apt-get update
    sudo apt-get install python3-pip
    ```

**Install PyInstaller:**

- *Run the following command in your terminal to install PyInstaller:*

    ```bash
    pip install pyinstaller
    ```

- **PyInstaller:**

    ```bash
    sudo apt-get update
    sudo apt-get install pyinstaller
    ```

### ***Python, Pip, Pyinstaller Installation on Arch Linux***

- **Python**

```bash
sudo pacman -Syu python
```

- **pip**

```bash
sudo pacman -Syu python-pip
```

- **PyInstaller**

```bash
sudo pacman -Syu pyinstaller
```

- *These commands will install Python, pip, and PyInstaller on the corresponding systems. Remember that you may need superuser privileges (sudo) to execute these commands. Once installed, you can use these tools as needed, as described in the README.*

**Generate the binary:**

- *Clone the repository from the URL: [repository](https://github.com/DanielPerezMoralesDev13/cpy-cli.git "https://github.com/DanielPerezMoralesDev13/cpy-cli").*

  - *Navigate to the **cpy-cli/src** directory in your terminal.*

    ```bash
    cd ./src
    ```

  - *Run the following command to generate the binary:*

    ```bash
    pyinstaller --onefile ./cpy.py
    ```

  - *This will create an executable file named cp in the cpy-cli/src/dist directory. Now you can run the CP binary on your Linux system.*
  
  ```bash
  user@user-host:~/Desktop/cpy-cli/src/$ tree -C
  .
  ├── build
  │   └── cp
  │       ├── Analysis-00.toc
  │       ├── base_library.zip
  │       ├── cp.pkg
  │       ├── EXE-00.toc
  │       ├── localpycs
  │       │   ├── pyimod01_archive.pyc
  │       │   ├── pyimod02_importers.pyc
  │       │   ├── pyimod03_ctypes.pyc
  │       │   └── struct.pyc
  │       ├── PKG-00.toc
  │       ├── PYZ-00.pyz
  │       ├── PYZ-00.toc
  │       ├── warn-cp.txt
  │       └── xref-cp.html
  ├── cpy.py
  ├── cp.spec
  └── dist
      └── cp

  4 directories, 16 files
  ```

  ```bash
  user@user-host:~/Desktop/cpy-cli/src/$ cd ./dist/
  ```

  ```bash
  user@user-host:~/Desktop/cpy-cli/src/dist$ ./cpy --help
  usage: cpy [-h] [-o | -i] [-r] [-v] source  destination

  cp command implementation in Python

  positional arguments:
  source             Source directory or file
  destination        Destination directory or  file

  options:
  -h, --help         show this help message and  exit
  -o, --override     Override destination files  if they already exist
  -i, --interactive  Asks if you want to  overwrite the file
  -r, --recursive    Copy directories  recursively
  -v, --verbose      Give details about actions  being performed
  ```

## **Contributions**

> Contributions are welcome! If you have suggestions, corrections, or wish to add additional content to this project, feel free to open an issue or submit a pull request. Your help is essential in making this project a comprehensive and up-to-date reference for the development community.

## **License**

> This repository is published under the MIT License. Feel free to use, modify, and distribute the content according to the terms of this license.

## ***Author***

- ***Author:** Daniel Benjamin Perez Morales*

- ***GitHub:** [DanielPerezMoralesDev13](https://github.com/DanielPerezMoralesDev13 "https://github.com/DanielPerezMoralesDev13")*

- ***Email:** <danielperezdev@proton.me>*
