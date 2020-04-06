# def change_words_starting_with_a(list_to_check):
def change_words_starting_with_a(words):
    appended_string = "hello"
    return [appended_string + i for i in words if i.startswith("a")]

Names = ["annabele", "ben", "avril", "Desmond" , "ant", "steve"]
print(change_words_starting_with_a(Names))
