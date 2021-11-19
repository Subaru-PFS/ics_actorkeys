#!/usr/bin/env python3

import argparse
import pkgutil

import actorkeys
from opscore.protocols import keys


def gatherAllDictionaries():
    """ Load all existing actorkeys dictionaries"""
    allDict = [modname for __, modname, __ in pkgutil.iter_modules(actorkeys.__path__)]
    return allDict


def main(argv=None):
    """Command-line interface to load actorkeys dictionary. """
    parser = argparse.ArgumentParser(description="load actorkeys dictionary")
    parser.add_argument('-l', '--actors', nargs='+', default=None, help='actorkeys dictionary(ies) to load')

    args = parser.parse_args(argv)

    allDict = gatherAllDictionaries() if args.actors is None else args.actors

    for dictname in allDict:
        keys.KeysDictionary.load(dictname, forceReload=True)


if __name__ == '__main__':
    main()
