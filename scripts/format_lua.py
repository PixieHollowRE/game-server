import subprocess
from pathlib import Path
import sys

TOOLS_DIR = Path(__file__).resolve().parent
CONFIG_DIR = TOOLS_DIR.parent / "config"


def format_lua_file(path: Path) -> None:
    try:
        result = subprocess.run(
            ["luafmt", str(path)],
            check=True,
            text=True,
            capture_output=True,
            shell=True,
        )
        path.write_text(result.stdout, encoding="utf-8")
        print(f"Formatted {path}")
    except FileNotFoundError:
        print("Error: 'luafmt' not found on PATH.")
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"luafmt failed on {path}:\n{e.stderr}")
        return


def main():
    lua_files = list(CONFIG_DIR.rglob("*.lua"))

    for lua_file in lua_files:
        format_lua_file(lua_file)


if __name__ == "__main__":
    main()
