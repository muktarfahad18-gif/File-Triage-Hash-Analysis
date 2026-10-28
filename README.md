 Project Overview

The aim of this project is to develop a Python program that analyses files using SHA-256 hashing.
The program helps identify known files, unknown files and duplicate files.

 Project Features

The Python program can:
Read files from a selected folder.

Display filenames, extensions and file sizes.

Display when each file was last modified.

Calculate SHA-256 hashes.

Compare hashes against a reference CSV file.

Identify known and unknown files.

Detect duplicate files.

Display a duplicate-file summary.

Handle common errors.

Save results to a CSV report.

 Software Requirements

The project uses:



Python 3

Thonny Python IDE



Python libraries used:



pathlib

hashlib

csv

datetime



All libraries are included with Python, so no additional installations are required.

 Project Files

The main Python program is located at:



File_Triage_Ready_To_Run/File_Triage_Project/hash.py



The project also contains:



samples/ — Contains the five sample files.

hashes_reference.csv — Contains known SHA-256 hashes.

report.csv — Contains the generated analysis results.

README.txt — Contains information about the supplied dataset.

 How to Run the Program

Download the GitHub repository.

Extract the downloaded ZIP file.

Open the File_Triage_Project folder.

Open hash.py using Thonny.

Press F5 to run the program.

Press Enter to analyse the default samples folder, or enter another folder path.

View the results in the Thonny Shell.

Open report.csv to view the saved results.

 Results

The program analysed five sample files.



The results were:



Three files were classified as KNOWN.

Two files were classified as UNKNOWN.

One duplicate-file group was identified.



The duplicate files were:



sample_a.txt

sample_b.txt



These files produced identical SHA-256 hashes.
Cybersecurity Importance

SHA-256 hashing is useful in cybersecurity because it allows analysts to compare file contents.



Matching hashes provide strong evidence that files contain identical data.



A KNOWN file matches a hash in the supplied reference list.



An UNKNOWN file does not match the reference list. However, this does not automatically mean that the file is malicious.



Hash analysis alone cannot determine whether a file is safe or dangerous.

 Error Handling

The program includes basic error handling.



For example, if the samples folder is missing, the program displays:



Error: Samples folder not found!



The program also handles problems when reading the reference CSV file or sample files.

 Conclusion

This project demonstrates how Python can be used to automate basic cybersecurity file investigations.



It combines file handling, functions, dictionaries, loops, conditional statements, SHA-256 hashing and CSV reporting.



The tool provides a simple way to investigate files and identify matching or unknown content.
