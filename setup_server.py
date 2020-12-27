import os

root = os.getcwd()

print("Remember that an empty to_delete_mods dir means all the mods go bye bye!")
input("Slap that ENTER key if you're 200% sure, because the old setup is gonna go awaaaaayyyyyy...")

print("Creating mods to delete list...")
os.chdir("to_delete_mods")
to_del = os.listdir()
to_del_str = "\n".join(to_del)
if to_del_str.strip() == "":
    x = input("Delete all mods or no mods? [a/n]")
    if x == "a":
        to_del_str = "all"
    elif x == "n":
        to_del_str = "none"
    else:
        print("That isn't either or!")
        exit(1)

print("Creating mods to send list...")
os.chdir(root)
os.chdir("new_mods")
to_send = os.listdir()
to_send_str = "\n".join(to_send)

print("Writing lists to file...")
os.chdir(root)
open("to_delete_mods.txt", 'w').write(to_del_str)
open("new_mods.txt", "w").write(to_send_str)

input("ENTER to exit lol...")