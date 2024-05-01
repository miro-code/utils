#!/usr/bin/env python

# This script is used to sync your local directory with the ARC server.
from subprocess import run
from argparse import ArgumentParser
import os

parser = ArgumentParser()
parser.add_argument("-n", "--dry-run", action="store_true", help="perform a dry run")
parser.add_argument("-p", "--path", type=str, help="path to sync", default="MEGalodon")
parser.add_argument("-tp", "--target-path", type=str, help="path to sync")
parser.add_argument("-sp", "--source-path", type=str, help="path to sync")
args = parser.parse_args()

if args.target_path is None:
    TARGET_PATH = args.path
else:
    TARGET_PATH = args.target_path
if args.source_path is None:
    SOURCE_PATH = args.path
else:
    SOURCE_PATH = args.source_path


HOME = os.environ["HOME"]
PROJECT = "coml-oxmedis"  # your ARC project name
USER = "trin4076"  # your ARC username
DATA = f"/data/{PROJECT}/{USER}"  # the path to the data directory on the ARC server
HOST = "arc"  # the hostname of the ARC server

excluded = [
    ".git",
    "wandb",
    "*.zip",
    "__pycache__",
    ".pytest_cache",
    ".vscode",
    "data",
    "lightning_logs",
]
excluded_str = " ".join([f'--exclude="{x}"' for x in excluded])
RSYNC_OPTIONS = "--delete " + excluded_str

if args.dry_run:
    RSYNC_OPTIONS += " -n"

print(f"Pushing changes to {HOST}")
run(f"rsync -aP $HOME/{SOURCE_PATH}/ {HOST}:{DATA}/{TARGET_PATH} {RSYNC_OPTIONS} --exclude=results", shell=True)

if os.path.isdir(f"{HOME}/{SOURCE_PATH}/results"):
    print(f"Pulling results from {HOST}")
    run(f"rsync -aP {HOST}:{DATA}/{TARGET_PATH}/results/ $HOME/{SOURCE_PATH}/results {'-n' if args.dry_run else ''}", shell=True)
