KeysDictionary('sac', (1, 1),
               Key("text", String(help="text for humans")),
               Key("version", String(help="EUPS/git version")),
               Key("position", 
                   Float(name='penta', help='pentaprism position'),
                   Float(name='detect', help='detector position'),help='sac stage position'),
               Key("status", 
                   Bool("False","True", name='detect', help='detector online'),
                   Bool("False","True", name='stage', help='stage online'),help='devices on/off status'),
               Key("origin", 
                   Bool("False","True", name='penta', help='penta origin search done'),
                   Bool("False","True", name='detect', help='detector origin search done'),help='stage origin search done'),
               

               )
