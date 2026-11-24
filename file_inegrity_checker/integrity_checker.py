import os
import json
import hashlib
import argparse


def calculate_hash(file_path):
    """Calculate the SHA-256 hash of a file."""
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        while True:
            chunk = file.read(4096)
            if not chunk:
                break
            sha256.update(chunk)

    return sha256.hexdigest()


def create_snapshot(folder):
    """Create a dictionary of file paths and their hashes."""
    snapshot = {}

    for root, dirs, files in os.walk(folder):
        # Ignore symbolic links to avoid following them.
        dirs[:] = [
            d for d in dirs
            if not os.path.islink(os.path.join(root, d))
        ]

        for filename in files:
            path = os.path.join(root, filename)

            if os.path.islink(path):
                continue

            relative_path = os.path.relpath(path, folder)

            try:
                snapshot[relative_path] = calculate_hash(path)
            except (OSError, PermissionError) as error:
                print(f"Could not read {relative_path}: {error}")

    return snapshot


def save_baseline(folder, baseline_file):
    snapshot = create_snapshot(folder)

    with open(baseline_file, "w", encoding="utf-8") as file:
        json.dump(snapshot, file, indent=4)

    print(f"Baseline saved: {len(snapshot)} files recorded.")


def check_integrity(folder, baseline_file):
    if not os.path.isfile(baseline_file):
        print("Baseline not found. Create it first.")
        return

    with open(baseline_file, "r", encoding="utf-8") as file:
        baseline = json.load(file)

    current = create_snapshot(folder)

    old_files = set(baseline)
    new_files = set(current)

    added = sorted(new_files - old_files)
    deleted = sorted(old_files - new_files)
    common = old_files & new_files

    modified = sorted(
        name for name in common
        if baseline[name] != current[name]
    )

    unchanged = sorted(
        name for name in common
        if baseline[name] == current[name]
    )

    print("\n--- FILE INTEGRITY REPORT ---")

    for name in unchanged:
        print(f"[OK]        {name}")

    for name in modified:
        print(f"[MODIFIED]  {name}")

    for name in added:
        print(f"[ADDED]     {name}")

    for name in deleted:
        print(f"[DELETED]   {name}")

    if not (modified or added or deleted):
        print("No changes detected.")

    print("\nSummary:")
    print("Unchanged:", len(unchanged))
    print("Modified: ", len(modified))
    print("Added:    ", len(added))
    print("Deleted:  ", len(deleted))


def main():
    parser = argparse.ArgumentParser(
        description="Python File Integrity Checker"
    )

    parser.add_argument(
        "action",
        choices=["baseline", "check"],
        help="Create a baseline or check file integrity"
    )

    parser.add_argument(
        "folder",
        help="Folder to monitor"
    )

    parser.add_argument(
        "--baseline",
        default="integrity_baseline.json",
        help="Path to the saved baseline JSON file"
    )

    args = parser.parse_args()

    if not os.path.isdir(args.folder):
        print("Error: Folder does not exist.")
        return

    if os.path.abspath(args.folder) == os.path.abspath(
        args.baseline
    ):
        print("Error: Baseline must be a file, not the folder.")
        return

    if args.action == "baseline":
        save_baseline(args.folder, args.baseline)
    else:
        check_integrity(args.folder, args.baseline)


if __name__ == "__main__":
    main()
