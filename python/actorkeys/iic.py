KeysDictionary('iic', (1,2),
               Key("controllers", String(help='controllers list') * (1, None)),
               Key("text", String(), help='Stuff for humans'),
               Key('version', String(help="IIC actor version",
                                     FITS=("W_RVIIC",
                                           "W_IICACTOR_VERSION"))),
               Key('version_tron_actorcore', String(help="tron_actorcore version")),
               Key('version_ics_actorkeys', String(help="ics_actorkeys version")),
               Key('version_pfs_utils', String(help="pfs_utils version")),
)
