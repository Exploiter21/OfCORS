# OfCORS
This tool is specially designed to test for CORS misconfigurations. In bug bounties, we typically deal with hundreds or thousands of domains to test, and this tool is well-suited for that task. It can test a single domain as well as multiple domains for CORS-based misconfigurations.

## Help
Using this tool is very straight forward. There are only two options:
+ `--domain` or `-d` : This option will take a single domain name as an input.
+ `--dfile` or `-df` : This option if for giving a file of multiple domain names.

## Usage
To test for a single domain
```sh
$ python3 main.py --domain nestle.com
```
or
```sh
$ python3 main.py -d nestle.com
```
Testing multiple domains
```sh
$ python3 main.py --dfile domains.txt #Here domains.txt is the file having multiple domain names
```
or
```sh
$ python3 main.py -df domains.txt
```

## Screen Shots
![git1](https://github.com/user-attachments/assets/bc2ba073-ab93-40dc-b6b6-968e4b0aa32d)
