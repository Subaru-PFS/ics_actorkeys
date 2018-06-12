KeysDictionary('sac', (1, 4),
               Key("text", String(help="text for humans")),
               Key("lsPenta",
                   Enum('LOADED', 'ONLINE', name='state'),
                   Enum('IDLE', 'INITIALISING', 'MOVING', 'FAILED', name='substate'),
                   Float(name='position'), help='pentaprism stage status'),
               Key("lsDetector",
                   Enum('LOADED', 'ONLINE', name='state'),
                   Enum('IDLE', 'INITIALISING', 'MOVING', 'FAILED', name='substate'),
                   Float(name='position'), help='detector stage status'),
               Key("ccd",
                   Enum('LOADED', 'ONLINE', name='state'),
                   Enum('IDLE', 'INITIALISING', 'EXPOSING', 'FAILED', name='substate'), help='ccd status'),
               Key("filepath",
                   String(name="rootDirectory"),
                   String(name="nightDirectory"),
                   String(name="filename"),
                   help="all the parts making up the image file path. Suitable for os.path.join()"),
               Key("newVisits", Int() * (1,), help='new visits'),

               )
