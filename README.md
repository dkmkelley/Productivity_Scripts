# Productivity Scripts

A growing collection of scripts for cleaning, organizing, and maintaining my
homelab, and a way to build fluency in Python outside of larger projects.

## Scripts

**organize_downloads** — Sorts the contents of a Downloads folder by file
type to keep it manageable. Takes a target directory as a command-line
argument and walks it recursively, moving files into folders like
`Documents`, `Images`, `Archives`, and `3D Print Files` based on extension.

**remove_zips** — Recursively deletes `.zip` files in a target directory and
its subdirectories. Built to clean up a 3D printing folder where downloaded
model archives kept piling up after extraction. Opens a folder picker,
shows every `.zip` file it found (capped at 25, with a count of any
remaining), and requires explicit confirmation before deleting anything.

## Usage

**organize_downloads** takes a target directory as a command-line argument:

    python organize_downloads.py <target_directory>

**remove_zips** launches a folder picker dialog instead of taking an
argument. Run it with no arguments, select a folder when prompted, and
confirm deletion in the dialog that lists every .zip file found before
anything is removed:

    python remove_zips.py

## Requirements

Python 3.x, standard library only (tkinter is used for remove_zips'
folder picker and confirmation dialog)