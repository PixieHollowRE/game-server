from pathlib import Path

ROOT = Path(__file__).resolve().parent   # this file's own folder = game root
XML = ROOT / "assets"
WEB = ROOT.parent / "web"
MEADOWS = WEB / "meadows"