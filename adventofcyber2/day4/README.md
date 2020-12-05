- Fuzzing command:
	`wfuzz -c -z file,$(pwd)/wordlist.txt 'http://$IP/api/site-log.php?date=FUZZ'
