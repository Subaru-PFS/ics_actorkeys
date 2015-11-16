KeysDictionary("ccd", (1,0),
               Key('Text', String(), help='Stuff for humans'),
                   
               Key("ccdTemps",
                   Float(invalid="NaN", units="K", name='preamp'), 
                   Float(invalid="NaN", units="K", name='ccd0'), 
                   Float(invalid="NaN", units="K", name='ccd1'),
                   help='detector assembly temperatures')
)

