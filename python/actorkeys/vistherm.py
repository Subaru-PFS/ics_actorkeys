KeysDictionary("vistherm", (1, 7),

               Key("lamtemps1", Float(invalid="NaN", units="K")*9,
                   help="Temperatures1 from the LAM Acq system"),
               Key("lamtemps2", Float(invalid="NaN", units="K")*9,
                   help="Temperatures2 from the LAM Acq system"),
               Key("gauge",
                   Float(invalid="NaN", units="Torr", name="secondary"),
                   Float(invalid="NaN", units="Torr", name="primar"),
                   help="Pressure from the LAM Acq system"),


)
