import sys
import requests
import ipaddress

# Function to check if IP is in the CIDR ranges
def is_ip_in_cidr(ip, cidr_list):
    for cidr in cidr_list:
        if ipaddress.ip_address(ip) in ipaddress.ip_network(cidr):
            return True 
    return False

# Main function
def main():
    if len(sys.argv) != 2:
        print("Usage: python cidr_check.py <IP_ADDRESS>")
        sys.exit(1)
    
    ip = sys.argv[1]
    
    try:
        # Validate IP address
        ipaddress.ip_address(ip)
    except ValueError:
        print(f"Invalid IP address: {ip}")
        sys.exit(1)
    
    # Fetch RIPE NCC JSON data
    url = "https://stat.ripe.net/data/country-resource-list/data.json?resource=US&v4_format=prefix"
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Failed to fetch data from RIPE NCC")
        sys.exit(1)
    
    data = response.json()
    
    # Extract the ipv4 CIDR blocks
    cidr_blocks = data['data']['resources']['ipv4']
    
    # Check if IP is in the CIDR ranges
    if is_ip_in_cidr(ip, cidr_blocks):
        print("Pass: IP is in one of the CIDR ranges.")
    else:
        print("Fail: IP is not in any of the CIDR ranges.")

if __name__ == "__main__":
    main()



