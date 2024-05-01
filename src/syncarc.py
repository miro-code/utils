#!/usr/bin/env python

# This script is used to sync your local directory with the ARC server.
from subprocess import run
from argparse import ArgumentParser
import os

parser = ArgumentParser()
parser.add_argument("-n", "--dry-run", action="store_true", help="perform a dry run")
parser.add_argument("--target-path", type=str, help="path to sync", default="MEGalodon")
parser.add_argument("--source-path", type=str, help="path to sync", default="MEGalodon")
args = parser.parse_args()

HOME = os.environ["HOME"]

PROJECT = "coml-oxmedis"  # your ARC project name
USER = "trin4076"  # your ARC username
DATA = f"/data/{PROJECT}/{USER}"  # the path to the data directory on the ARC server
HOST = "arc"  # the hostname of the ARC server
TARGET_PATH = args.target_path  # the path to the directory on the ARC server
SOURCE_PATH = args.source_path  # the path to the directory on your local machine
RSYNC_OPTIONS = '--delete --exclude=".git" --exclude="wandb/" --exclude="*.zip" --exclude="__pycache__" --exclude=".idea/" --exclude=".pytest_cache" --exclude="cache" --exclude=".vscode/"'

if args.dry_run:
    RSYNC_OPTIONS += " -n"

print(f"Pushing changes to {HOST}")
run(f"rsync -aP $HOME/{SOURCE_PATH}/ {HOST}:{DATA}/{TARGET_PATH} {RSYNC_OPTIONS} --exclude=results", shell=True)

if os.path.isdir(f"{HOME}/{SOURCE_PATH}/results"):
    print(f"Pulling results from {HOST}")
    run(f"rsync -aP {HOST}:{DATA}/{TARGET_PATH}/results/ $HOME/{SOURCE_PATH}/results {'-n' if args.dry_run else ''}", shell=True)
