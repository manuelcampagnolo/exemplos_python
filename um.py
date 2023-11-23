import re
import sys


def main():
    text="um hello, um, yummy um world um"
    text="um"
    text="Um, thanks for the album."
    text="Um, thanks, um..."
    text="um?"
    print(count(text))


def count(s):
    count=0
    s=str(s).lower()
    words=re.findall(".?um.?", s)
    print(words)
    for word in words:
        if len(word)==2 and re.search("um",word): # \W not a word character
            count +=1
        if len(word)==3 and re.search("\Wum|um\W",word):
            count +=1
        if len(word)==4 and re.search("\Wum\W",word):
            count +=1
    return count


if __name__ == "__main__":
    main()
