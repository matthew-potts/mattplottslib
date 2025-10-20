# bump_version.py
import sys
import tomli
import tomli_w

with open("pyproject.toml", "rb") as f:
    data = tomli.load(f)

# Navigate to the correct section
try:
    version = data["project"]["version"]
except KeyError:
    print("Version not found in [project] section.")
    sys.exit(1)

major, minor, patch = map(int, version.split("."))
new_version = f"{major}.{minor}.{patch + 1}"
data["project"]["version"] = new_version

with open("pyproject.toml", "wb") as f:
    f.write(tomli_w.dumps(data).encode("utf-8"))

print(f"Bumped version to {new_version}")