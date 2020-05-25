KeysDictionary('sps', (1, 4),
               Key('text', String(help='text for humans')),
               Key('version', String(help='SPS actor version',
                                     FITS=('W_RVSPS', 'W_SPSACTOR_VERSION'))),
               Key('version_tron_actorcore', String()),
               Key('version_pfs_utils', String()),
               Key('version_ics_actorkeys', String()),
               Key('exposable', String(help='camList that can be safely exposed') * (1, None)),
               Key('fileIds',
                   Int(help='assigned PFS visit'), String('camera list'), UInt(name="camMask", reprFmt="0x%04x")),
               Key('visit', Int(help='assigned PFS visit')),
               Key('frames', String(help='camList for frames that has genuinely been created') * (1, None)),

               )
