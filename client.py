#!/usr/bin/python3

import requests
import os
import sys

######### CONFIGURE HOST ###########



host = "http://blf02.net:8000"
modpack_folder = "BBKAWRJv"



######### CONFIGURE HOST ###########

url = host + "/{}"


def status(msg):
    if len(msg) > 120:
        pound_size = 120
    else:
        pound_size = len(msg)
    print("#"*pound_size)
    print(msg)
    print("#"*pound_size)


def progress(val, msg="    "):
    """Update Progress of Operation.
    Updates a progress bar (if we have a GUI) as tarstall processes run
    Args:
        val (int/float): Value to update the progress bar to.
        msg (str): Message to display on right side of progress bar. Defaults to "    ".
    Stole this from tarstall (my own program) lol

    """
    try:
        columns = os.get_terminal_size()[0]
    except Exception:
        columns = 140
    start_chars = "Progress ({}%): ".format(str(int(val)))
    end_chars = msg
    end_buffer = 80
    full_squares = int(val * 0.01 * (columns - len(start_chars) - end_buffer))
    empty_squares = columns - len(start_chars) - end_buffer - full_squares
    print(start_chars + "■"*full_squares + "□"*empty_squares + end_chars, end="\r")


def full_path(path):
    """Expands a File Path.

    Args:
        path (str): Path to expand

    Returns:
        str: Expanded path

    """
    return os.path.expandvars(os.path.expanduser(path))


def download(down_url, safe=False):
    try:
        r = requests.get(down_url, allow_redirects=True, timeout=30)
        if r.status_code != 200:
            raise Exception
        return r.content
    except Exception:
        if safe:
            return None
        print("\nError " + str(r.status_code) + ".")
        print("\n"*5)
        print("Failed to download file!")
        input("Press ENTER to exit...")
        sys.exit(1)


def main():
    print("Initiating...")
    # Set terminal size to 140, while keeping original height
    try:
        os.system("mode con: cols=140 lines={}".format(os.get_terminal_size()[1]))
    except OSError:
        pass
    i = download(url.format("version.txt"))
    i = i.strip()
    try:
        i = int(i)
    except TypeError:
        print("Error determining version. Please yell at hammy3502!")
        exit(1)
    working_dir = full_path("%appdata%\\.minecraft\\{}".format(modpack_folder) + str(i))
    print("Using {}".format(modpack_folder) + str(i))
    if not os.path.isdir(working_dir):
        os.mkdir(working_dir)
        os.chdir(working_dir)
        os.mkdir("mods")
    os.chdir(os.path.join(working_dir, "mods"))
    print("Getting list of mods to delete...")
    to_del = download(url.format("to_delete_mods.txt")).decode("utf-8")
    to_del = to_del.split("\n")
    for i in range(len(to_del)):
        to_del[i] = to_del[i].strip()
    print("Deleting old mods...")
    if to_del[0].lower() == "all":
        to_del = os.listdir()
    elif to_del[0].lower() == "none":
        to_del = []
    for f in os.listdir():
        if f in to_del:
            try:
                os.remove(f)
            except (IsADirectoryError, FileNotFoundError):
                continue
    if not to_del:
        print("No mods needed to be deleted!")
    else:
        print("Old mods deleted!")
    print("Getting list of mods to download")
    to_get = download(url.format("new_mods.txt")).decode("utf-8")
    to_get = to_get.split("\n")
    for i in range(len(to_get)):
        to_get[i] = to_get[i].strip()
    print("\n\n\nDownloading Mods...")
    for n in to_get:
        try:
            this_progress = (to_get.index(n) / (len(to_get) - 1))*100
        except Exception:
            this_progress = 0
        progress(this_progress, "    Downloading {}...".format(n))
        content = download(url.format("new_mods/" + n))
        progress(this_progress, "    Writing     {}...".format(n))
        open(n, 'wb').write(content)
        print(" "*139, end="\r")
    print("Checking for new Forge version...")
    forge_content = download(url.format("forge.jar"), True)
    if forge_content is not None:
        print("Running Forge installer. Please click install client, then click ok!")
        os.chdir(os.path.expandvars("%temp%"))
        with open("forge.jar", 'wb') as f:
            f.write(forge_content)
        os.system('"C:\\Program Files (x86)\\Minecraft Launcher\\runtime\\jre-x64\\bin\\javaw.exe" -jar forge.jar')

    print("\nSuccessfully downloaded all mods!")


if __name__ == '__main__':
    print("Welcome to the Mods Updater/Downloader/Whatever-er!")
    print("Made by hammy3502")
    status("Please keep this window open and do not use other applications while this is running! " 
    + "If you do, and the installation freezes, press ENTER on this window to continue installation!")
    input("Press ENTER to continue...")
    main()
    input("Press ENTER to exit...")
