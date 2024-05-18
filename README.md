# DNS Enumerator #
## Overview ##
This project is a Python script designed to enumerate various DNS records for a given domain or a list of domains. It supports querying multiple types of DNS records, including A, AAAA, NS, CNAME, MX, PTR, SOA, and TXT records.

## Features ##
- Query individual domains for DNS records.
- Batch query multiple domains from a file.
- Supports a wide range of DNS record types.
- Handles errors gracefully and provides informative output.

## Prerequisites ##
- Python 3.x
- `dnspython` library
You can install the required dnspython library using pip:
```
pip install dnspython
```
## Usage ##
### Command-Line Arguments ###
The script accepts the following command-line arguments:
- -d, --domain-name: Specify a single domain name to look up.
- -f, --file: Provide a file containing a list of domain names to look up, one per line.
### Example Commands ###
#### Query a Single Domain ####
To query a single domain for all supported DNS records:
```
python dns_enum.py -d example.com
```
#### Query Multiple Domains from a File ####
To query multiple domains listed in a file:
1. Create a text file (e.g., domains.txt) with each domain name on a new line.
2. Run the script with the -f option:
```
python dns_enum.py -f domains.txt
```
### Example Output ###
For a domain with various DNS records, the output will be:
```
A Records
    - 93.184.216.34

AAAA Records

NS Records
    - ns1.example.com.
    - ns2.example.com.

CNAME Records

MX Records
    - 10 mail.example.com.

PTR Records

SOA Records
    - ns1.example.com. hostmaster.example.com. 2021040401 7200 3600 1209600 3600

TXT Records
    - "v=spf1 include:_spf.example.com ~all"
```
If a domain does not exist, the script will output:
```
example.com does not exist.
```
### Script Details ###
The script `dns_enum.py` consists of the following parts:
- RECORD_TYPES: A list of DNS record types to query.
- get_args(): Parses command-line arguments.
- process_file(domain_file): Reads domains from a file and resolves each one.
- resolve_domain(domain): Resolves and prints DNS records for a given domain.
- main(): Entry point of the script that processes command-line arguments and calls the appropriate functions.

## License ##
This project is licensed under the GNU General Public License v3.0. You are free to use, modify, and distribute this script in accordance with the terms of the license.
