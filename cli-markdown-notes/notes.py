import os
import sys
from datetime import datetime

NOTES_DIR = "notes"

def ensure_dir():
    if not os.path.exists(NOTES_DIR):
        os.makedirs(NOTES_DIR)

def create_note(title):
    filename = f"{datetime.now().strftime('%Y-%m-%d')}-{title.replace(' ', '_')}.md"
    filepath = os.path.join(NOTES_DIR, filename)
    with open(filepath, 'w') as f:
        f.write(f"# {title}\n\n")
    print(f"📝 Created note: {filepath}")

def list_notes():
    notes = os.listdir(NOTES_DIR)
    for note in sorted(notes):
        print(note)

def view_note(name):
    filepath = os.path.join(NOTES_DIR, name)
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            print(f.read())
    else:
        print("Note not found.")

def main():
    ensure_dir()
    args = sys.argv[1:]
    if not args:
        print("Usage: create <title>, list, view <filename>")
        return
    cmd = args[0]
    if cmd == "create":
        create_note(" ".join(args[1:]))
    elif cmd == "list":
        list_notes()
    elif cmd == "view":
        view_note(args[1])
    else:
        print("Unknown command")

if __name__ == "__main__":
    main()

# update 4 - refactor: improve command structure
# update 5 - docs: update usage guide
# update 8 - test: add basic tests for create
# update 11 - feat: add note search
# update 27 - refactor: improve command structure
# update 28 - feat: auto-timestamp notes
# update 32 - style: format CLI output
# update 42 - style: format CLI output
# update 49 - docs: update usage guide
# update 54 - style: format CLI output
