KeysDictionary("aitroom", (2, 0),

               Key("flowduino",
                   Float(invalid="NaN", units="C", name="temp"),
                   Float(invalid="Nan", units="L/m", name="flow"),
                   help="temperature, flow from LAM water system"),
               Key("weatherduino",
                   Float(invalid="NaN", units="percent", name="humidity"),
                   Float(invalid="Nan", units="C", name="temp"),
                   Float(invalid="NaN", units="C", name="dewpoint"),
                   help="humidity, temperature from LAM clean room"),
               Key("weatherduino2",
                   Float(invalid="NaN", units="percent", name="humidity"),
                   Float(invalid="Nan", units="C", name="temp"),
                   Float(invalid="NaN", units="C", name="dewpoint"),
                   help="humidity2, temperature2 from LAM clean room"),
               Key("weatherduino3",
                   Float(invalid="NaN", units="percent", name="humidity"),
                   Float(invalid="Nan", units="C", name="temp"),
                   Float(invalid="NaN", units="C", name="dewpoint"),
                   help="humidity3, temperature3 from LAM clean room"),
               Key("tetraduino",
                   Float(invalid="Nan", units="C", name="temp1"),
                   Float(invalid="Nan", units="C", name="temp2"),
                   Float(invalid="Nan", units="C", name="temp3"),
                   Float(invalid="Nan", units="C", name="temp4"),
                   help="temperature from LAM clean room"),
               Key("chiller",
                   Float(name='flow', invalid="NaN", units="L/min", help='Coolant flow rate', STS=0),
                   Float(name='temp', invalid="NaN", units="C"),
                   Float(name='pressure', invalid="NaN", units="Bar"),
                   help="monitoring values from cooling system"),
               Key("lake1",
                   Float(invalid="NaN", units="C", name="temp1"),
                   help="temperature from lakeshore controller"),
               Key("roughPressure", Float(invalid="NaN", units="Torr"),
                   help="Roughing station ait gauge pressure."),
               Key("lauda",
                   Float(invalid="NaN", units="C", name="setpoint"),
                   Float(invalid="Nan", units="C", name="temp"),
                   help="temperature setpoint, current temperature from LAUDA bath"),

)
