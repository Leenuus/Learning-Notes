# Run Tests in Python

## dep

1. pytest
2. pytest watch

### shortcut scripts

```bash

pytest ./*.py

```

```bash

pywatch() {
    local config="./.test_runner.sh"
    [ -f $config ] || echo "pytest ./*.py" > $config
    ptw --runner "sh $config"
}

```
