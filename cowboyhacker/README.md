# Bounty Hacker

## Tasks

- What ports are open?

  - 21 ftp
  - 22 ssh
  - 80 http

- Who wrote the task list?

  - Using anonymous ftp access, we are able to access locks.txt and tasks.txt
  - We see that `lin` is the person who wrote tasks.txt

- What service can you bruteforce with the text file found?

  - ssh

- What is the users password?

  - After downloading the locks.txt file, we'll use hydra to find the password by bruteforcing ssh
    - `hydra -v -l lin -P locks.txt ssh://$IP`

- user.txt found in `~/Desktop/user.txt`

- root.txt
  - using `sudo -l` will show us that we can use tar as root
  - GTFO bins gives us the command to escalate our privileges
    - sudo tar -cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/bash
