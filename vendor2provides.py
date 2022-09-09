#!/usr/bin/python3
 
# vendor2provides.py
# ==================
#
# Parse modules.txt files into rpm .spec file Provides for bundled dependencies.
# Written by Fabio "decathorpe" Valentini <decathorpe@fedoraproject.org> for
# the fedora syncthing package: https://src.fedoraproject.org/rpms/syncthing
# Modified by @anthr76 for talos
# SPDX-License-Identifier: CC0-1.0 OR Unlicense
 
import os
import re
import sys
 
 
def main() -> int:
    if len(sys.argv) < 2:
        print("No path to 'modules.txt' file given.")
        return 1
 
    path = sys.argv[1]
 
    with open(path) as file:
        contents = file.read()
 
    lines = contents.split("\n")
 
    # dependencies = filter lines for "# package version"
    dependencies = list(filter(lambda line: line.startswith("# "), lines))
 
    # parse vendored dependencies into (import path, version) pairs
    vendored = list()
    replace_regex = re.compile("^.+( v[0-9-\.]+)? => ")
    for dep in dependencies:
        ipath, version = replace_regex.sub("", dep[2:]).split(" ")[:2]
 
        # check for git snapshots
        if len(version) > 27:
            # return only 7 digits of git commit hash
            version = version[-12:-1][0:7]
        else:
            # strip off leading "v"
            version = version.lstrip("v")
 
        vendored.append((ipath, version))
 
    for ipath, version in vendored:
        print(f"Provides:       bundled(golang({ipath})) = {version}")
 
 
if __name__ == "__main__":
    exit(main())
