
from pathlib import Path

def get_data_path(category, name):
    data_dir = Path(__file__).parent / f"../../50_Data/{category}"
    if not data_dir.exists():
        data_dir.mkdir(parents=True, exist_ok=True)
    return data_dir / name