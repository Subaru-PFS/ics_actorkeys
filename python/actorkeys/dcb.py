KeysDictionary('dcb', (1, 4),
               Key("text", String(help="text for humans")),
               Key("version", String(help="EUPS/git version")),
               Key("ne", Bool("off", "on", name='neon', help='neon lamp switch')),
               Key("xenon", Bool("off", "on", name='xenon', help='xenon lamp switch')),
               Key("hgar", Bool("off", "on", name='hgar', help='Hg-Ar switch')),
               Key("krypton", Bool("off", "on", name='hgar', help='Krypton switch')),
               Key("deuterium", Bool("off", "on", name='deuterium', help='deuterium lamp switch')),
               Key("bakeout", Bool("off", "on", name='bakeout', help='bakeout cover')),
               Key("roughpump", Bool("off", "on", name='roughpump', help='roughpump')),
               Key("pow_attenuator", Bool("off", "on", name='pow_attenuator', help='power attenuator switch')),
               Key("pow_sphere", Bool("off", "on", name='pow_sphere', help='power int sphere switch')),
               Key("pow_halogen", Bool("off", "on", name='pow_halogen', help='power halogen switch')),

               Key("photodiode", Float(invalid="Nan", help='photo diode flux (foot-lambert)')),
               Key("fluxmedian", Float(invalid="Nan", help='photodiode flux median')),
               Key("attenuator", UInt(help='attenuator opening value (open=0)')),
               Key("halogen", Bool("off", "on", name='halogen', help='halogen switch')),
               Key("aten_vaw",
                   Float(name='V', help='Voltage'),
                   Float(name='A', help='Current'),
                   Float(name='W', help='Power'), help='aten current Volt, Amp, Power')

               )

