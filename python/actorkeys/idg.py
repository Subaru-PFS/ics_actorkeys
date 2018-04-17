KeysDictionary("idg", (1, 1),
               Key('Text', String(), help='Stuff for humans'),

               Key("testRanges",
                   String(name='camera name'),
                   Int(invalid="NaN", units="steps", name='range of axis A'), 
                   Int(invalid="NaN", units="steps", name='range of axis B'), 
                   Int(invalid="NaN", units="steps", name='range of axis C'), 
                   help="End-to-end range of the FPA motors."),

               Key("testOffsets",
                   String(name='camera name'),
                   Int(name='test loop count'), 
                   Int(invalid="NaN", units="steps", name='error of axis A'), 
                   Int(invalid="NaN", units="steps", name='error of axis B'), 
                   Int(invalid="NaN", units="steps", name='error of axis C'), 
                   help="Post-cycle error of the FPA motors."),
               )