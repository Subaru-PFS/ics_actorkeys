KeysDictionary('ccd', (1,1),
               Key("Text", String(), help='Stuff for humans'),
                   
               Key("ccdTemps",
                   Float(invalid="NaN", units="K", name='preamp'), 
                   Float(invalid="NaN", units="K", name='ccd0'), 
                   Float(invalid="NaN", units="K", name='ccd1'),
                   help='detector assembly temperatures'),

               Key("readRows",
                   Int(name='rowsDone'),
                   Int(name='rowsTotal'),
                   help="the number of rows read out and the image height."),

               Key("exposureState",
                   Enum('idle','wiping','integrating','reading','aborted','unknown'),
                   help="the state of the readout system"),

               Key("filepath",
                    String(name="rootDirectory"),
                    String(name="nightDirectory"),
                    String(name="filename"),
                    help="all the parts making up the image file path. Suitable for os.path.join()"),
)

