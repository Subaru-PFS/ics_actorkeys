KeysDictionary('meb', (1, 4),
               Key("text", String(help="text for humans")),
               Key("version", String(help="EUPS/git version")),
               Key('temps', Float()*7,
                   help='The MCS Ebox temperatures'),
               Key('power', Int()*4),
)
