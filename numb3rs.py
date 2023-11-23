import re
import sys

def main():
    ipv4="255.21.34.54.65"
    print(validate(ipv4))

def validate(ip):
    matches= re.search(r"^(.+)\.(.+)\.(.+)\.(.+)$", ip)
    for i in range(4):
        m=matches.group(i+1)
        try:
            n=int(m)
        except ValueError:
            print('not a number')
            return False
        else: 
            if n<0 or n>255: 
                print('not between 0 and 255')
                return False
    return True

if __name__ == "__main__":
    main()
