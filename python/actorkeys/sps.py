KeysDictionary('sps', (1, 2),
               Key('text', String(help='text for humans')),
               Key('version', String(help='SPS actor version')),
               Key('version_tron_actorcore', String()),
               Key('version_pfs_utils', String()),
               Key('version_ics_actorkeys', String()),
               Key('visit', Int(help='assigned PFS visit')),
               Key('exposable', String(help='camera list to expose') * (1, None)),
               )
