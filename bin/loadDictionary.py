#!/usr/bin/env python3

import argparse
import glob
import os

from opscore.protocols import keys


def gatherAllDictionaries():
    """ Load all existing actorkeys dictionaries"""
    toCheck = []
    actorkeysDir = os.environ['ICS_ACTORKEYS_DIR']
    files = glob.glob(f'{actorkeysDir}/*/*/*.py')

    for file in files:
        __, actorkeyPy = os.path.split(file)
        actorkey, __ = os.path.splitext(actorkeyPy)
        toCheck.append(actorkey)

    return toCheck


def main(argv=None):
    """Command-line interface to load actorkey dictionary. """
    parser = argparse.ArgumentParser(description="load actorkey dictionary")
    parser.add_argument("--actor", default=None, type=str, help="actorkey dictionary to load")

    args = parser.parse_args(argv)

    toCheck = gatherAllDictionaries() if args.actor is None else [args.actor]

    for actor in toCheck:
        keys.KeysDictionary.load(actor, forceReload=True)


if __name__ == '__main__':
    main()
