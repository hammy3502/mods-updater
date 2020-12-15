import requests
import os
import sys

def full_path(path):
    """Expands a File Path.

    Args:
        path (str): Path to expand

    Returns:
        str: Expanded path

    """
    return os.path.expandvars(os.path.expanduser(path))


def main():
    print("Preparing to download...")
    i = 9999
    while i > 0:
        working_dir = full_path("%appdata%\\.minecraft\\BBNAWRJv" + str(i))
        if os.path.isdir(working_dir):
            break
        else:
            i -= 1
    print("Using BBNAWRJv" + str(i))
    os.chdir(os.path.join(working_dir, "mods"))
    print("Deleting old SurvivalExtras...")
    for f in os.listdir():
        if "SurvivalExtras".lower() in f.lower():
            os.remove(f)
            break
    print("Downloading new SurvivalExtras...")
    url = "http://blf02.net:8000/SurvivalExtras.jar"
    try:
        r = requests.get(url, allow_redirects=True, timeout=30)
    except Exception:
        print("Failed to download the updated SurvivalExtras!!!!!")
        sys.exit(1)
    open("SurvivalExtras.jar", 'wb').write(r.content)
    print("Success!")
    sys.exit(0)


if __name__ == '__main__':
    input("Press ENTER to continue...")
    main()
    input("Press ENTER to exit...")
