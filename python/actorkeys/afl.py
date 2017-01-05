KeysDictionary('afl', (1, 1),
               Key("text", String(help="text for humans")),
               Key("version", String(help="EUPS/git version")),
               Key("engDuino", 
                   Int(name='bool', help='engDuino switch state'),
                   Int(name='pwm', help='pwm value of engDuino 0-255'),
                   help='engineering fiber illumination devices status'),

               )
