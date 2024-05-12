#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/DanielPerezMoralesDev13
# Correo electrónico: danielperezdev@proton.me 

# from sys import argv
import argparse
from pathlib import Path, PosixPath
from sys import stderr, stdout,exit
from typing import TextIO

# bash color
# https://stackoverflow.com/questions/5947742/how-to-change-the-output-color-of-echo-in-linux

class CpError(Exception):
    pass


class Logger:
    def __init__(self:'Logger', verbosity: bool = False) -> None:
        self._verbose : bool = verbosity
        return None

    def set_verbosity(self:'Logger', verbosity: bool) -> None:
        self._verbose = verbosity
        return None


    def log(self: 'Logger', message:str, file: TextIO = stdout) -> None:
        if self._verbose: print(f"\033[1;32mMESSAGE:\033[0m {message}", file=file,end="\n")
        return None

    def warn(self: 'Logger', message:str, file: TextIO = stderr) -> None:
        print(f"\033[1;31m\nWARNING: \033[0m{message}", file=file,end="\n")
        return None

    def error(self: 'Logger', message:str, file: TextIO = stderr) -> None:
        print(f"\033[1;31mERROR: \033[0m{message}", file=file,end="\n")
        return None


logger: Logger = Logger()


def dump(src: Path, dest: Path) -> None:
    with open(file = src, mode = "rb") as s, open(file = dest ,mode = "wb") as d:
        d.write(s.read())


def copy_directory(src_dir: PosixPath, dest_dir: PosixPath, override:bool=False, interactive:bool=False) -> None:
    for src_child in src_dir.iterdir():
        dest_child: PosixPath = dest_dir / src_child.name

        if src_child.is_dir():
            logger.log(message=f"\033[1;35mCopy dir\033[0m {src_child} \033[0;96m->\033[0m {dest_child}")
            dest_child.mkdir(exist_ok=True)
            copy_directory(src_dir = src_child, dest_dir = dest_child, override = override,interactive = interactive)
        elif src_child.is_file():
            confirmed: bool = True
            if dest_child.is_file():
                if interactive:
                    confirmed = "y" in str(input(f"\033[1;35mOverride\033[0m {dest_child} ? \033[1;30m[\033[0m\033[0;31mNo\033[0m\033[1;30m/\033[0m\033[0;32mYes\033[0m\033[1;30m]:\033[0m ")).lower()
                elif not override:
                    confirmed = False
    
            if confirmed:
                logger.log(message=f"\033[1;35mCopy file\033[0m {src_child} \033[0;96m->\033[0m {dest_child}")
                dest_child.touch()
                dump(src_child, dest_child)
            else:
                logger.log(message=f"\033[1;35mSkipping\033[0m {src_child} \033[0;96m->\033[0m {dest_child}")
        else:
            logger.error(message=f"\033[1;35mSkipping\033[0m {src_child} because file type is not supported")


def copy_file(src: Path, dest: Path, override:bool=False) -> None:
    if dest.is_dir():
        dest = dest / src.name
    if dest.is_file() and not override:
        raise CpError(f"\033[1;35mCannot override\033[0m {dest}, specify \033[1;35m-o\033[0m option")
    logger.log(message=f"\033[1;35mCopy\033[0m {src} \033[0;96m->\033[0m {dest}")
    dest.touch()
    dump(src=src, dest=dest)


def copy(src: PosixPath, dest: PosixPath, override:bool=False, recursive:bool=False, interactive:bool=False) -> None:
    if src.is_file():
        copy_file(src, dest, override)
    elif src.is_dir():
        dest_is_dir:bool = dest.is_dir()
        if not dest_is_dir and dest.exists():
            raise CpError(f"\033[1;35mDestination\033[0m {dest} is not a directory")
        if not recursive:
            raise CpError(f"\033[1;35mSkipping directory\033[0m {src} because \033[1;35m-r\033[0m is not present")
        if dest_is_dir:
            dest = dest / src.name
        dest.mkdir(exist_ok=True)
        copy_directory(src_dir = src,dest_dir = dest,override = override,interactive = interactive)
    else:
        raise CpError("File type not supported")
    return None


def cli() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="cp",
        description="cp command implementation in Python",
    )
    group: argparse._MutuallyExclusiveGroup = parser.add_mutually_exclusive_group()
    
    group.add_argument(
        "-o", "--override",
        action="store_true",
        help="Override destination files if they already exist"
    )
    group.add_argument(
        "-i", "--interactive",
        action="store_true",
        help="Asks if you want to overwrite the file"
    )
    parser.add_argument(
        "-r", "--recursive",
        action="store_true",
        help="Copy directories recursively"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Give details about actions being performed"
    )
    parser.add_argument(
        "source",
        type=Path,
        help="Source directory or file"
    )
    parser.add_argument(
        "destination",
        type=Path,
        help="Destination directory or file",
    )

    return parser.parse_args()


def main() -> None:
    args:argparse.Namespace = cli()
    try:
        logger.set_verbosity(verbosity=args.verbose)
        copy(src=args.source,dest= args.destination,override= args.override,recursive= args.recursive,interactive= args.interactive)
    except CpError as e:
        logger.error(message = str(e))
        exit(1)
    except KeyboardInterrupt:
        logger.warn(message="Interrupted")
    return None


if __name__ == "__main__":
     main()
     exit(0)