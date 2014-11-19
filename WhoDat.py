from ipwhois import IPWhois


__author__ = 'crazybmanp'


def getAllInfo(ip):
    info = IPWhois(ip).lookup()
    return info

ToPrint = ['name', 'cidr', 'country', 'address', 'postal_code',  'city', 'created',
           'abuse_emails', 'tech_emails', 'misc_emails', 'description']


def writeListHeader(file):
    for el in ToPrint:
        file.write(el + "\t")
    file.write("\n")

def writeListSegment(file, domain):
    for prop in ToPrint:
        file.write(str(domain[prop]).replace('\n', ' ') + "\t")
    file.write("\n")

file = open("ips.txt")
output = open("info.txt", "w")

writeListHeader(output)

for line in file:
    k = getAllInfo(line.rstrip())

    writeListSegment(output, k["nets"][0])
    print(k["nets"][0])
    print("---------------------------------------------")

file.close()
output.close()