KeysDictionary("charis", (1, 4),
               # All ion gauge keywords
               Key("pressures",
                   Float(invalid="NaN", units="Torr", name="dewar"),
                   Float(invalid="NaN", units="Torr", name="rough"),
                   Float(invalid="NaN", units="Torr", name="full"),
                   help="Ion gauge pressures."),

               Key("filterSlot",
                   Int(name="filterSlot", help="index of current filter slot"),
                   String(name="filterName", help="name of currnet filter")),
               Key("shutter",
                   Hex(name="statusWord"),
                   String(name="position")),

               Key('laserState',
                   Int(name="enabled", help="virtual keyVarDict state"),
                   Int(name="mode", help="notifications sure, actually"),
                   Int(name="power" ,help="power level in percent"),
                   Int(name="alarms", help="alarm mask")),
               
               # All ion pump keywords:
               # Need to add:
               #    The error bit masks and descriptions, current spat out as text
               # ionpump1=1,5100,2.4e-05,23,6.5e-08
               Key("ionpump1",
                   Int(name='enabled'),
                   Float(name='Voltage', invalid="NaN", units="V"),
                   Float(name='Current', invalid="NaN", units="A"),
                   Float(name='Power', invalid="NaN", units="W"),
                   Float(name='Temperature', invalid="NaN", units="K"),
                   Float(name='Pressure', invalid="NaN", units="Torr"),
                   help="Ion pump status."),

               # Temp & heater keywords
               Key("temps", Float(invalid="NaN", units="K")*10,
                   help="Temperatures from the Lakeshores"),
               Key("tempNames", String(invalid="N/C")*10,
                   help="Names of the temperature probes."),
)
