import os

root = os.getcwd()

print("Remember that an empty to_delete_mods dir means all the mods go bye bye!")
input("Slap that ENTER key if you're 200% sure, because the old setup is gonna go awaaaaayyyyyy...")

print("Creating mods to delete list...")
os.chdir("to_delete_mods")
to_del = os.listdir()
to_del_str = "\n".join(to_del)
if to_del_str.strip() == "":
    x = input("Delete all mods or no mods? [a/n] ")
    if x == "a":
        to_del_str = "all"
    elif x == "n":
        to_del_str = "none"
    else:
        print("That isn't either or!")
        exit(1)

os.chdir(os.path.expandvars(".."))
if os.path.isfile("version.txt"):
    with open("version.txt", 'r') as ver:
        c_ver = ver.read().strip()
else:
    c_ver = -1

new_ver = input("Input modpack version (ENTER to use previous version of {}) ".format(c_ver))
if new_ver == "":
    new_ver = c_ver
else:
    try:
        new_ver = int(new_ver)
    except TypeError:
        print("Didn't specify a valid number!")
        exit(1)

print("Writing version to version file...")
open("version.txt", 'w').write(str(new_ver))

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