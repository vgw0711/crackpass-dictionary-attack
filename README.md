Setup Instructions : 

1. Tested on Python2.7 (Recommended Python2.7)
2. Execution Command - python cracker.py <wordlist_location> <unshadowed_password_file>

Wordlists attached : words, linuxwords
Unshadowed Password file : lin_passwd_lab3.txt

Note: This script will work with the wordlist format that matches with /usr/share/dict/words.
Also, this script is specifically designed for unshadowed linux password files.

Additional Features:
This tool utilizes the spare CPU cores to quicken the dictionary attack. Basically, it supports multiprocessing. Along with that, I have compared the performance with running it as a single process, the difference is drastic. 

In cases where you might just require one of the users password from the list, this tool can be your best bet. But, in general too, if we exempt the position of the correct password from consideration, this tool reduces the execution time by 'x' fraction, where x is the number of processes the attack is divided into.


(This code can be modified to perform a brute-force attack. Also, the choice of what a process does depends on number of users in the unshadowed linux password list. If number of users is really huge, creating password pools to be tested against all the users in process is more efficient than testing all the passwords against one user in a process.)
