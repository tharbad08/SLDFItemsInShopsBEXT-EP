#!/usr/bin/env python3
import json
from pathlib import Path

ADD_TAG = "component_type_lostech"
REMOVE_TAGS = {"BUILT-IN", "BLACKLISTED"}

def make_mod_id(old_id: str) -> str:
    if old_id.startswith("Gear_Mod_"):
        return old_id
    if old_id.startswith("Gear_"):
        return "Gear_Mod_" + old_id[len("Gear_"):]
    return "Gear_Mod_" + old_id

def process_file(path: Path) -> bool:
    try:
        data = json.loads(path.read_text(encoding="utf-8-sig"))
    except Exception as e:
        print(f"[SKIP] {path.name}: cannot read JSON: {e}")
        return False

    desc = data.get("Description")
    if not isinstance(desc, dict) or not desc.get("Id"):
        print(f"[SKIP] {path.name}: missing Description.Id")
        return False

    new_id = make_mod_id(str(desc["Id"]))

    desc["Id"] = new_id
    desc["Purchasable"] = True

    tags = data.setdefault("ComponentTags", {})
    items = tags.setdefault("items", [])

    if not isinstance(items, list):
        items = []
        tags["items"] = items

    cleaned = []
    seen = set()

    for tag in items:
        if tag in REMOVE_TAGS:
            continue
        if tag not in seen:
            cleaned.append(tag)
            seen.add(tag)

    if ADD_TAG not in seen:
        cleaned.append(ADD_TAG)

    tags["items"] = cleaned
    tags.setdefault("tagSetSourceFile", "")

    new_path = path.with_name(new_id + ".json")

    path.write_text(
        json.dumps(data, indent=4, ensure_ascii=False) + "\n",
        encoding="utf-8"
    )

    if path.name != new_path.name:
        if new_path.exists():
            print(f"[WARN] target exists, not renaming: {path.name} -> {new_path.name}")
        else:
            path.rename(new_path)
            print(f"[OK] {path.name} -> {new_path.name}")
            return True

    print(f"[OK] {path.name}")
    return True

def main():
    count = 0
    for path in sorted(Path(".").glob("*.json")):
        if process_file(path):
            count += 1

    print(f"\nDone. Processed {count} JSON files.")

if __name__ == "__main__":
    main()
