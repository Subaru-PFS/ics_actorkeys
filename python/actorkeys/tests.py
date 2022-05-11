KeysDictionary('tests', (1, 1),
               Key("text", String(help="text for humans")),
               Key('version', String(help="test actor version")),
               Key("keytest1", Float(invalid="NaN") * (1, 2)),
               Key("keytest2", Float(invalid="NaN")),
               Key("keytest3",
                   Enum("Open", "Closed", name="test"),
                   String(name="errors", help="human-oriented error string")),

               Key("convergenceId", Int()),
               )
