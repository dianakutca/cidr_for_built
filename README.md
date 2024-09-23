## Steps: 

##### Takes an IP address as a command line argument
##### Gets json data from the RIPE network coordination center link here
##### Use the ['data']['resources']['ipv4'] block in the json above to determine whether the IP provided on the CLI is in any of the CIDRs
##### Output a Pass/Fail result based on the presence of the IP address in the CIDR ranges