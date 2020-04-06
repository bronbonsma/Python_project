list_of_names = ["Amy Suzor", "Gabby", "Christopher Stewart", "Sarah", "Lea Craig", "Tom"]

def name_checker(list_of_names):
    for i in list_of_names:
        yield i

for name in name_checker(list_of_names):
    if " " not in name:
        print(name)