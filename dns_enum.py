import dns.resolver
import sys
import argparse
from time import sleep

RECORD_TYPES = ["A","AAAA","NS","CNAME","MX","PTR","SOA","TXT"]

def get_args():
	parser = argparse.ArgumentParser()
	parser.add_argument("-d","--domain-name",dest="domain",help="Domain name to look up")
	parser.add_argument("-f","--file",dest="file",help="List of domain names to look up")

	options = parser.parse_args()
	return options

def process_file(domain_file):
	domain_list = []
	with open(domain_file,'r') as f:
		lines = f.readlines()
		for line in lines:
			domain_list.append(line.strip())
		for domain in domain_list:
			print("="*12 +domain+ "="*12)
			resolve_domain(domain)
			
def resolve_domain(domain):
	for records in RECORD_TYPES:
		try:
		    answer = dns.resolver.resolve(domain, records)
		    print(f"{records} Records")
		    for server in answer:
		        print("\t- "+ server.to_text())
		    print()
		except dns.resolver.NoAnswer:
		    pass
		except dns.resolver.NXDOMAIN:
		    print(f"{domain} does not exist.\n")
		    quit()
		except KeyboardInterrupt:
		    print("Quitting.")
		    quit()

def main():
	options = get_args()
	if options.domain:
		resolve_domain(options.domain)
	elif options.file:
		process_file(options.file)

main()

