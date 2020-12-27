#!/usr/bin/python3

import requests
import os
import sys

######### CONFIGURE HOST ###########



host = "http://blf02.net:8000"



######### CONFIGURE HOST ###########

url = host + "/{}"

def full_path(path):
    """Expands a File Path.

    Args:
        path (str): Path to expand

    Returns:
        str: Expanded path

    """
    return os.path.expandvars(os.path.expanduser(path))


def download(down_url):
    try:
        r = requests.get(down_url, allow_redirects=True, timeout=30)
        if r.status_code != 200:
            print("Error " + r.status_code + ".")
            raise Exception
        return r.content
    except Exception:
        print("\n"*5)
        print("Failed to download file!")
        input("Press ENTER to exit...")
        sys.exit(1)


def main():
    print("Initiating...")
    i = 9999
    while i > 0:
        working_dir = full_path("%appdata%\\.minecraft\\BBNAWRJv" + str(i))
        if os.path.isdir(working_dir):
            break
        else:
            i -= 1
    print("Using BBNAWRJv" + str(i))
    os.chdir(os.path.join(working_dir, "mods"))
    print("Getting list of mods to delete...")
    to_del = download(url.format("to_delete_mods.txt")).decode("utf-8")
    to_del = to_del.split("\n")
    for i in range(len(to_del)):
        to_del[i] = to_del[i].strip()
    print("Deleting files...")
    if to_del[0].lower() == "all":
        to_del = os.listdir()
    for f in os.listdir():
        if f in to_del:
            try:
                os.remove(f)
            except (IsADirectoryError, FileNotFoundError):
                continue
    print("Getting list of mods to download")
    to_get = download(url.format("new_mods.txt")).decode("utf-8")
    to_get = to_get.split("\n")
    for i in range(len(to_get)):
        to_get[i] = to_get[i].strip()
    for n in to_get:
        print("Downloading {}...".format(n), end="\r")
        content = download(url.format("new_mods/" + n))
        print("Writing     {}...".format(n), end="\r")
        open(n, 'wb').write(content)
    print("Successfully downloaded all mods!")
    input("Press ENTER to exit...")
    sys.exit(0)


if __name__ == '__main__':
    input("Press ENTER to continue...")
    main()
    input("Press ENTER to exit...")
