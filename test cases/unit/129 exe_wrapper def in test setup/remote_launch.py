#!/usr/bin/env python3

import argparse
import pathlib

parser = argparse.ArgumentParser(description="execute a cross binary by launching remotely")
parser.add_argument('elf_file', type=pathlib.Path)
args = parser.parse_args()

assert args.elf_file.exists()

stamp_path = args.elf_file.parent / "remote_launch_has_run.stamp"
with open(stamp_path, 'w') as stamp_file:
        stamp_file.write("Success")
