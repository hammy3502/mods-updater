## Mods Updater

Small thing for personal use that updates a private modpack. Feel free to use if you want to figure it out. Code is also kind of a mess. Explanation below may help you in some way.

# Intentions

Using the `client.py` for others and `setup_server.py` for the server hoster, it should be super easy to setup or update a modpack. `client.py` NEEDS to be distributed to everyone playing.

Run `python -m http.server` in the root directory to host the server for `client.py` to connect with.

# Setup

0. Change the host line in `client.py` if using a different domain and port, and change instances of "BBNAWRJ" in `client.py` to the name of the pack (make sure your pack ends in "v#" where # is a version number between 1 and 9999 inclusive)

1. Distribute `client.py` to everyone (only need to do once)

2. Create 2 folders: `new_mods` and `to_delete_mods` in the directory of this repo.

3. Place the mods that need to be deleted in `to_delete_mods` and the mods to download in `new_mods`.

NOTE: If no mods are going to be deleted, or all mods should simply be deleted, leave `to_delete_mods` empty.

4. Run `setup_server.py` and follow the instructions.

5. Run `python -m http.server` in the directory of this repo, and port forward port 8000

6. Have users run `client.py` and follow instructions.