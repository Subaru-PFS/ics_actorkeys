KeysDictionary('fps', (1, 6),
               Key("text", String(help="text for humans")),
               Key('version', String(help="FPS actor version",
                                     FITS=("W_RVFPS",
                                           "W_FPSACTOR_VERSION"))),
               Key('version_tron_actorcore', String()),
               Key('version_pfs_utils', String()),
               Key('mcsBoresight', Float(name='x'), Float(name='y')),
               Key('pfsDesignId', Long(help="the loaded pfsDesignId",
                                       FITS=('W_PFDSGN', 'W_PFS_DESIGN_ID'))),
               Key('pfsConfig',
                   Long(name='pfsDesignId', FITS=('W_PFSCFG', 'W_PFS_CONFIG_ID'),
                        help='identifier for the pfsDesign/pfsConfig file'),
                   Int(name='visit0', help='the visit0 for the convergence'),
                   Enum('Unknown', 'Preparing', 'inProgress', 'Done', name='ConvergenceStatus', help='convergence status')),
               Key('fpsDesignId', Long(help="fps generated pfsDesignId")),
               )
