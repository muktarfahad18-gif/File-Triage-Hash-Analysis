from pathlib import Path
import hashlib
import csv
from datetime import datetime

folder = Path(__file__).parent

path = input("Enter folder path (or press Enter for samples): ")

if path == "":
    samples = folder / "samples"
else:
    samples = Path(path)


def hash_file(file):
    data = file.read_bytes()
    return hashlib.sha256(data).hexdigest()



def load_hashes():
    known = {}

    try:
        with open(folder / "hashes_reference.csv") as file:
            for row in csv.DictReader(file):

                hash_value = row["sha256"]

                
                if not hash_value or len(hash_value) != 64:
                    print("Invalid hash found!")
                    return None

                if any(c not in "0123456789abcdef"
                       for c in hash_value.lower()):
                    print("Invalid hash found!")
                    return None

                known[hash_value.lower()] = row["label"]

    except (OSError, KeyError, csv.Error):
        print("Error reading reference file!")
        return None

    return known

def scan_files():
    known = load_hashes()

    if known is None:
        return

    seen = {}
    duplicates = {}
    results = []

    if not samples.is_dir():
        print("Error: Samples folder not found!")
        return

    for file in samples.iterdir():
        if file.is_file():
            try:
                file_hash = hash_file(file)

                print("Name:", file.name)
                print("Size:", file.stat().st_size, "bytes")
                print("Type:", file.suffix)

                date = datetime.fromtimestamp(file.stat().st_mtime)
                print("Last Modified:", date)

                print("SHA-256:", file_hash)

                if file_hash in known:
                    status = "KNOWN"
                else:
                    status = "UNKNOWN"

                print("Status:", status)

                
                if file_hash in seen:
                    print("Duplicate of:", seen[file_hash])

                    if file_hash not in duplicates:
                        duplicates[file_hash] = [seen[file_hash]]

                    duplicates[file_hash].append(file.name)
                else:
                    seen[file_hash] = file.name

                
                results.append([
                    file.name,
                    file.stat().st_size,
                    file.suffix,
                    str(date),
                    file_hash,
                    status
                ])

                print("--------------------")

            except OSError:
                print("Error reading:", file.name)

    
    print("===== DUPLICATE SUMMARY =====")

    if duplicates:
        for names in duplicates.values():
            print("Duplicate files:")
            for name in names:
                print(name)

        print("Total duplicate groups:", len(duplicates))
    else:
        print("No duplicates found")

    
    try:
        with open(folder / "report.csv", "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([
                "Name", "Size", "Type",
                "Last Modified", "SHA-256", "Status"
            ])

            writer.writerows(results)

        print("CSV report saved!")

    except OSError:
        print("Error saving CSV report!")


scan_files()