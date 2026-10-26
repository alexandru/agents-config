# Bootstrap installation from shell

Each harness is installed by streaming `bin/utils/install.sh`, published by a GitHub Actions workflow at the repository's Pages root as `install.sh`, to Bash, so the installer must run before Git or a sufficient Python exists. That entry point is therefore a Bash script, an exception to single-file Python for `bin/` scripts with logic. It stays minimal: it only installs Git, Python, and Make from the platform's official package manager and obtains the repository; deployment stays in Python (`bin/utils/deploy.py`), and remaining prerequisites stay in the harness `Makefile`.

Shared helpers like these live in `bin/utils/`, which is not placed on `PATH`, so they keep generic names and identical content across harnesses rather than taking the harness prefix that `bin/` entry points carry.
