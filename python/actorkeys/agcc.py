KeysDictionary('agcc', (1, 6),
               Key("text", String(help="text for humans")),
               Key("version", String(help="EUPS/git version")),
               Key('agc1_stat',
                   Enum('READY', 'BUSY', 'ABSENT'),
                   help='AG camera #1 status'),
               Key('agc2_stat',
                   Enum('READY', 'BUSY', 'ABSENT'),
                   help='AG camera #2 status'),
               Key('agc3_stat',
                   Enum('READY', 'BUSY', 'ABSENT'),
                   help='AG camera #3 status'),
               Key('agc4_stat',
                   Enum('READY', 'BUSY', 'ABSENT'),
                   help='AG camera #4 status'),
               Key('agc5_stat',
                   Enum('READY', 'BUSY', 'ABSENT'),
                   help='AG camera #5 status'),
               Key('agc6_stat',
                   Enum('READY', 'BUSY', 'ABSENT'),
                   help='AG camera #6 status'),
               Key('agc_exposing', Int(help='total number of exposing AG cameras')),
               Key('agc_frameid', Int(help='AG camera frame ID')),
               Key('agc_fitsfile',
                   String(name='filename', help='Filename for combined AG camera images'),
                   Float(name='timestamp', help='seconds since 1970')),
               Key('agc1_fitsfile',
                   String(name='filename', help='Filename for last AG camera #1 exposure'),
                   Float(name='timestamp', help='seconds since 1970')),
               Key('agc2_fitsfile',
                   String(name='filename', help='Filename for last AG camera #2 exposure'),
                   Float(name='timestamp', help='seconds since 1970')),
               Key('agc3_fitsfile',
                   String(name='filename', help='Filename for last AG camera #3 exposure'),
                   Float(name='timestamp', help='seconds since 1970')),
               Key('agc4_fitsfile',
                   String(name='filename', help='Filename for last AG camera #4 exposure'),
                   Float(name='timestamp', help='seconds since 1970')),
               Key('agc5_fitsfile',
                   String(name='filename', help='Filename for last AG camera #5 exposure'),
                   Float(name='timestamp', help='seconds since 1970')),
               Key('agc6_fitsfile',
                   String(name='filename', help='Filename for last AG camera #6 exposure'),
                   Float(name='timestamp', help='seconds since 1970')),
               Key('agccFileIds',
                   String(name='pfsDay', help='directory date of just finished exposure'),
                   Int(name='visit', help='visit of just finished exposure'),
                   Int(name='frame', help='AGCC subframe of just finished exposure'),
               ),
)
