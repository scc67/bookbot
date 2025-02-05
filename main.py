def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    

    def count_words(tekst):
        return len(tekst.split())

    def count_characters(tekst):
        letter_count = {}
        for char in tekst:
            if char.lower() in letter_count:
                letter_count[char.lower()] += 1
            else:
                letter_count[char.lower()] = 1
        
        return letter_count
    
    
    count_dict = count_characters(file_contents)
    count_list = []
    for letter in count_dict:
        dict = {}
        dict["name"] = letter
        dict["num"] = count_dict[letter]
        count_list.append(dict)
        
    def sort_on(dict):
        return dict["num"]
    
    count_list.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {f.name} ---")
    print(f"{count_words(file_contents)} word found in the document")
    print()
    for k in count_dict:
        if k.isalpha():
            print(f"The '{k}' character was found {count_dict[k]} times")
    print("--- End report ---")

main()