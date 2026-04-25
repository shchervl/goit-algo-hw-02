# goit-algo-hw-02

## Setup

### Install uv

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Create virtual environment

```bash
uv venv
```

### Activate virtual environment

```bash
# macOS/Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

### Install dependencies

```bash
uv sync
```

## Running

### Task 01 — Service center queue simulation

```bash
uv run task_01/task_01.py
```

### Task 02 — Palindrome checker

```bash
uv run python task_02/task_02.py
```

## Testing

### Run all tests

```bash
uv run pytest
```

### Run tests for a specific task

```bash
uv run pytest task_02/
```

### Run tests with verbose output

```bash
uv run pytest task_02/ -v
```

## Managing Dependencies

### Add a package

```bash
uv add <package>
```

### Remove a package

```bash
uv remove <package>
```

### Update all packages

```bash
uv lock --upgrade
uv sync
```

### Show installed packages

```bash
uv pip list
```

## Development

### Run with a specific Python version

```bash
uv run --python 3.12 task_01/task_01.py
```

### Run a one-off command without activating venv

```bash
uv run python -c "import sys; print(sys.version)"
```
