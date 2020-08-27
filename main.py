import requests
import os

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
    for f in os.listdir(full_path("%appdata%\\.minecraft\\")):
        working_dir = full_path("%appdata%\\.minecraft\\{}".format(f))
        if f.lower() == "bbnawrjv1" and os.path.isdir(working_dir):
            break
    os.chdir(working_dir)
    os.chdir("mods")
    print("Deleting old SurvivalExtras...")
    for f in os.listdir():
        if "SurvivalExtras".lower() in f.lower():
            os.remove(f)
            break
    print("Downloading new SurvivalExtras...")
    url = "http://blf02.net:8000/SurvivalExtras.jar"
    r = requests.get(url, allow_redirects=True)
    open("SurvivalExtras.jar", 'wb').write(r.content)
    print("Success!")


if __name__ == '__main__':
    input("Press ENTER to continue...")
    main()
    input("Press ENTER to exit...")
