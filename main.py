def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(f'___ Begin report of books/frankenstein.txt')
    count = word_count(text)
    print(f"{count} words found in the document")
    print()
    dic = num_char(text)
    sorted_dic_to_sorted_list = sorted_dic(dic)
    
    for item in sorted_dic_to_sorted_list:
        if not item["name"].isalpha():
            continue
        print(f"The '{item['name']}' character was found {item['num']} times")
    print("--- End report ---")

#step 1
def get_book_text(path):
    with open(path) as f:
        return f.read()
    
#step 2
def word_count(text):
    counts = 0
    words = text.split()
    for word in words:
        counts += 1
    return counts

#step 3: create a dictionary that has each letter in the text with its corresponding count
def num_char(text):
    num_char_dic = {}
    for char in text:
        char = char.lower()
        if char in num_char_dic:   
            num_char_dic[char] += 1
        else:
            num_char_dic[char] = 1
    return num_char_dic

# Step 4: Create a list from the dictionary and make it such that it prints in descending order the characters in the text and their counts. Return it as a list

#4a
def sorted_dic(dic):
    sorted_dic = []
    sorted_dic = [{"name": key, "num": value} for key, value in dic.items()]
    sorted_dic.sort(reverse=True, key=sort_on)
    return sorted_dic

#4b: Tell the sort what to look for
def sort_on(dict):
    return dict["num"]



  

main()