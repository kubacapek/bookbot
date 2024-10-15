def wordcount(content):
    words = content.split()
    return len(words)

def countchars(content):
    lower = content.lower()
    counter = {}
    charsetm = set()
    for char in lower:
        if char in charsetm:
            counter[char] += 1
        else:
            counter[char] = 1
            charsetm.add(char)
    return counter
    
def printdict(dict):
    a = []
    for i in dict:
        a.append({"char": i, "occurence" : dict[i]})
    a.sort(reverse=True, key=sort_by_occurence)
    #print(a)
    for i in a:
        if i["char"].isalpha():
            print (f'character {i["char"]} is in the text {i["occurence"]} times')

def sort_by_occurence(dict):
    return dict["occurence"]

def print_result(dict, wc):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{wc} words found in the document")
    print()
    printdict(dict)
    print("--- End report ---")

def main():
    book = "books/frankenstein.txt"
    with open(book) as f:
        file_contents = f.read()
    #print (file_contents)
    wc = wordcount(file_contents)
    print(wc)
    charcount = countchars(file_contents)
    print_result(charcount, wc)
main ()