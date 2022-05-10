KeysDictionary(
    'ag',
    (1, 7),
    Key('text', String(), help='Human oriented message string',),
    Key('version', String(), help='Actor version string',),
    Key('guideOffsets',
        Int(name='exposureId', help='Exposure identifier'),
        Float(name='dRA', units='arcsec', help='Right ascension offset'),
        Float(name='dDec', units='arcsec', help='Declination offset'),
        Float(name='dInR', units='arcsec', help='Instrument rotator angle offset'),
        Float(name='dAz', units='arcsec', help='Azimuth offset'),
        Float(name='dAlt', units='arcsec', help='Altitude offset'),
        Float(name='dZ', units='mm', help='Focus offset'),
    ),
    Key('focusOffsets',
        Int(name='exposureId', help='Exposure identifier'),
        Float(name='dZ1', units='mm', help='Focus offset (AGC1)'),
        Float(name='dZ2', units='mm', help='Focus offset (AGC2)'),
        Float(name='dZ3', units='mm', help='Focus offset (AGC3)'),
        Float(name='dZ4', units='mm', help='Focus offset (AGC4)'),
        Float(name='dZ5', units='mm', help='Focus offset (AGC5)'),
        Float(name='dZ6', units='mm', help='Focus offset (AGC6)'),
    ),
)
