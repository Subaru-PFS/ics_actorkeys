KeysDictionary('drp', (1, 2),
               Key('text', String(help='text for humans')),
               Key('ingest', String(name='filepath', help='ingested exposure filepath')),
               Key('detrend', String(name='filepath', help='detrended exposure filepath')),

               Key('ingestStatus',
                   Int(name="visit", help="the PFS visit"),
                   Int(name="returnCode", help="command return code"),
                   String(name="statusStr", help="command status string"),
                   Float(name='timing', units="s", help='command timing in seconds')),
               Key('detrendStatus',
                   Int(name="visit", help="the PFS visit"),
                   Int(name="returnCode", help="command return code"),
                   String(name="statusStr", help="command status string"),
                   Float(name='timing', units="s", help='command timing in seconds')),
               Key('reduceExposureStatus',
                   Int(name="visit", help="the PFS visit"),
                   Int(name="returnCode", help="command return code"),
                   String(name="statusStr", help="command status string"),
                   Float(name='timing', units="s", help='command timing in seconds')),

               )
