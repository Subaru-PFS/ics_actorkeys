KeysDictionary(
    'qa',
    (1, 1),
    Key('text', String(), help='Human oriented message string', ),
    Key('version', String(), help='Actor version string', ),
    Key(
        'reduceExposureStatus',
        Int(name="visit", help="the PFS visit"),
        Int(name="returnCode", help="command return code"),
        String(name="statusStr", help="command status string"),
        Float(name='timing', units="s", help='command timing in seconds')
        ),
)
