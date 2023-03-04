import sys
import os
from cx_Freeze import setup, Executable

include_files = ['app.ico']

target = Executable(
    script="main.py",
    base="Win32GUI",
    icon="app.ico"
)

setup(
    name="Eye",
    version="1.0",
    description="Bigdata with Eye",
    author="Mohsen Dehghanzadeh",
    options = {'build_exe' : {'include_files' : include_files}},
    executables=[target]
)
