Poetry is a Python dependency management tool that replaces pip, requirements.txt, and setup.py with a single pyproject.toml file. It automatically creates virtual environments, uses advanced dependency resolution to prevent conflicts, and generates poetry.lock files for reproducible builds. Unlike venv which only creates isolated environments, Poetry handles the entire workflow—dependency management, conflict detection, building, and publishing to PyPI—all with built-in commands

// create a pyproject.toml for your project
poetry init

// install poetry venv and install dependecies in pyproject.toml
poetry install

// lists all virtual envs created and their info
poetry env info

// creates venv in project folder instead of random cache memory
poetry config virtualenvs.in-project true

// open shell within the virtual environment (in which you can run programs)
poetry shell

// install packages in poetry
(poetry shell) poetry add <dependency>

// remove packages in poetry 
(poetry shell) poetry remove <dependency>

// close poetry shell
(poetry shell) poetry exit

// close and deactivate poetry shell
(poetry shell) poetry deactivate

// list active environments
poetry env list

// remove environment
rm -rf venv