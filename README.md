# exfat-directory-entry-checksum
Tool for calculating exFAT DirectoryEntry checksum

https://docs.microsoft.com/en-us/windows/win32/fileio/exfat-specification#figure-2-entrysetchecksum-computation

# Usage
./exfat_directory_entry_checksum.py test_entry.bin 
checksum in decimal: 26241
checksum in hex: 0x6681
checksum in hex (swapped): 0x8166
Values from the given data (offset 0x02 and 0x03): 0x81 0x66
Checksum OK

./exfat_directory_entry_checksum.py test_entry2_modded.bin 
checksum in decimal: 4481
checksum in hex: 0x1181
checksum in hex (swapped): 0x8111
Values from the given data (offset 0x02 and 0x03): 0x81 0x66
Checksum NOT OK

