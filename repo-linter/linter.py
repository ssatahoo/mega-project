import os
import sys

ESSENTIAL_FILES = ['README.md', '.gitignore', 'LICENSE']
FORBIDDEN_EXTS = ['.exe', '.DS_Store', '.log']
MAX_FILE_SIZE_MB = 5
MAX_PATH_LENGTH = 100

def check_essentials(path):
    print("Checking essential files...")
    for file in ESSENTIAL_FILES:
        exists = os.path.exists(os.path.join(path, file))
        status = "✅" if exists else "❌"
        print(f"  {status} {file}")

def check_forbidden_files(path):
    print("\nChecking for forbidden files...")
    flagged = False
    for root, _, files in os.walk(path):
        for f in files:
            if any(f.endswith(ext) for ext in FORBIDDEN_EXTS):
                print(f"  ❌ Forbidden file found: {os.path.join(root, f)}")
                flagged = True
    if not flagged:
        print("  ✅ No forbidden files")

def check_large_files(path):
    print("\nChecking for large files...")
    flagged = False
    for root, _, files in os.walk(path):
        for f in files:
            full_path = os.path.join(root, f)
            try:
                size_mb = os.path.getsize(full_path) / (1024 * 1024)
                if size_mb > MAX_FILE_SIZE_MB:
                    print(f"  ❌ Large file: {full_path} ({size_mb:.2f} MB)")
                    flagged = True
            except:
                continue
    if not flagged:
        print("  ✅ No large files")

def check_path_length(path):
    print("\nChecking for long paths...")
    flagged = False
    for root, _, files in os.walk(path):
        for f in files:
            full_path = os.path.join(root, f)
            if len(full_path) > MAX_PATH_LENGTH:
                print(f"  ❌ Path too long: {full_path}")
                flagged = True
    if not flagged:
        print("  ✅ All paths reasonable")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    print(f"Running repo-linter on: {target}")
    check_essentials(target)
    check_forbidden_files(target)
    check_large_files(target)
    check_path_length(target)

# commit 0 - feat: add missing file checker
# commit 1 - feat: show total issues found
# commit 2 - fix: ignore hidden files
# commit 3 - feat: add long path detection
# commit 5 - feat: add missing file checker
# commit 6 - fix: ignore hidden files
# commit 7 - feat: show total issues found
# commit 8 - fix: unicode path bug
# commit 9 - refactor: break out functions
# commit 10 - feat: add forbidden file check
# commit 13 - chore: clean print statements
# commit 15 - refactor: break out functions
# commit 16 - feat: add missing file checker
# commit 18 - feat: add missing file checker
# commit 19 - feat: add long path detection
