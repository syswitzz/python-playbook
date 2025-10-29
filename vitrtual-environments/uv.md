uv is an all-in-one Python package manager written in Rust that replaces pip, venv, poetry, and pyenv. It's 10-100x faster than pip and poetry, automatically downloads Python versions in seconds, and handles virtual environments, dependencies, and lockfiles in one tool. Unlike venv (basic environments only) or poetry (requires separate pyenv), uv manages everything while using a global cache to save disk space
The uv.lock file is uv's lockfile that records the exact versions of all dependencies and their sub-dependencies in your project

// FOR MODULES / PROJECTS

// creates a new project with default files like pyproject.toml, main.py etc
uv init <project-name> or uv init   // run uv init if youre already in project directory

// creates virtual environment by itself and runs main.py
uv run main.py

// install package
uv add <dependency>

// remove package
uv remove <dependency>

// manually updates your project's lockfile although uv automatically does this when "uv run"
uv lock

// builds distribution source 
uv build

// FOR SCRIPTS

// creates a virtual environment and runs the script
uv run --with 'flask' --with 'requests' script.py

// adds some comments on top of your script like pyproject.toml file 
uv add --script script.py 'flask' 'requests'
