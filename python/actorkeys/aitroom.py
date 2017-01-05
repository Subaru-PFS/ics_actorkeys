KeysDictionary("aitroom", (1, 6),

               Key("flowduino",
                   Float(invalid="NaN", units="C", name="temp"),
                   Float(invalid="Nan", units="L/m", name="flow"),
                   help="temperature, flow from LAM water system"),
               Key("weatherduino",
                   Float(invalid="NaN", units="percent", name="humidity"),
                   Float(invalid="Nan", units="C", name="temp"),
                   help="humidity, temperature from LAM clean room"),
               Key("weatherduino2",
                   Float(invalid="NaN", units="percent", name="humidity"),
                   Float(invalid="Nan", units="C", name="temp"),
                   help="humidity2, temperature2 from LAM clean room"),
               Key("tetraduino",
                   Float(invalid="Nan", units="C", name="temp1"),
                   Float(invalid="Nan", units="C", name="temp2"),
                   Float(invalid="Nan", units="C", name="temp3"),
                   Float(invalid="Nan", units="C", name="temp4"),
                   help="temperature from LAM clean room"),


)