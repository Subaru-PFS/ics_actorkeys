KeysDictionary(
    'scr',
    (1, 6),
    Key('text', String(), help='Human oriented message string'),
    Key('version', String(), help='Actor version string'),
    Key('spsCooler',
        Float(name='facFlow', units='LPM', help='Facility coolant flow rate'),
        Float(name='facTemp', units='C', help='Facility coolant temperature'),
        Float(name='supFlow', units='LPM', help='Supply coolant flow rate'),
        Float(name='supTemp', units='C', help='Supply coolant temperature'),
        help='Coolant state at the Lytron cooler for the spectrograph cryocoolers'
    ),
    Key('scrCooler',
        Float(name='facFlow', units='LPM', help='Facility coolant flow rate'),
        Float(name='facTemp', units='C', help='Facility coolant temperature'),
        Float(name='supFlow', units='LPM', help='Supply coolant flow rate'),
        Float(name='supTemp', units='C', help='Supply coolant temperature'),
        help='Coolant state at the Lytron cooler for the clearn room heat exchangers'
    ),
    Key('spsChiller',
        Float(name='supTemp', units='C', help='Supply coolant temperature'),
        Float(name='supFlow', units='LPM', help='Supply coolant flow rate'),
        Float(name='supPress', units='MPa', help='Supply coolant pressure'),
        Enum('off', 'on', 'warning', 'fault', 'unknown', name='state', help='Operational state'),
        help='State of the SMC thermo chiller for the spectrograph cryocoolers'
    ),
    Key('scrChiller',
        Float(name='supTemp', units='C', help='Supply coolant temperature'),
        Float(name='supFlow', units='LPM', help='Supply coolant flow rate'),
        Float(name='supPress', units='MPa', help='Supply coolant pressure'),
        Enum('off', 'on', 'warning', 'fault', 'unknown', name='state', help='Operational state'),
        help='State of the SMC thermo chiller for the clearn room heat exchangers'
    ),
    Key('spsManifold',
        Float(name='inPress', units='MPa', help='Intake coolant pressure'),
        Float(name='supFlow', units='LPM', help='Supply coolant flow rate'), # computed (sum of four branches)
        Float(name='supTemp', units='C', help='Supply coolant temperature'), # computed (max of four branches)
        help='Coolant state at the supply manifold for the spectrograph cryocoolers'
    ),
    Key('scrManifold',
        Float(name='inPress', units='MPa', help='Intake coolant pressure'),
        Float(name='inFlow', units='LPM', help='Intake coolant flow rate'),
        Float(name='inTemp', units='C', help='Intake coolant temperature'),
        help='Coolant state at the supply manifold for the clean room heat exchangers'
    ),
    Key('rackManifold',
        Float(name='inFlow', units='LPM', help='Intake coolant flow rate'),
        Float(name='inTemp', units='C', help='Intake coolant temperature'),
        help='Coolant state at the supply manifold for the electronics racks'
    ),
    Key('scrHumidity',
        Float(name='dewPoint', units='C', help='Dew point inside clean room'),
        Float(name='relHum', units='%', help='Relative humidity inside clean room'),
        help='Dew point and relative humidity inside the clean room'
    ),
    Key('scrTemps',
        Float(name='bench1', units='C', help='Bench 1'),
        Float(name='bench2', units='C', help='Bench 2'),
        Float(name='bench3', units='C', help='Bench 3'),
        Float(name='bench4', units='C', help='Bench 4'),
        Float(name='hex1In', units='C', help='Heat exchanger 1 intake'),
        Float(name='hex2In', units='C', help='Heat exchanger 2 intake'),
        Float(name='hex3In', units='C', help='Heat exchanger 3 intake'), # reordered
        Float(name='hex4In', units='C', help='Heat exchanger 4 intake'), # reordered
        Float(name='hex1Exh', units='C', help='Heat exchanger 1 exhaust'), # reordered
        Float(name='hex2Exh', units='C', help='Heat exchanger 2 exhaust'), # reordered
        Float(name='hex3Exh', units='C', help='Heat exchanger 3 exhaust'), # reordered
        Float(name='hex4Exh', units='C', help='Heat exchanger 4 exhaust'), # reordered
        Float(name='ceiling1', units='C', help='Ceiling 1'),
        Float(name='ceiling2', units='C', help='Ceiling 2'),
        Float(name='ceiling3', units='C', help='Ceiling 3'),
        Float(name='ceiling4', units='C', help='Ceiling 4'),
        Float(name='bottom', units='C', help='Outside, bottom of the clean room'),
        Float(name='topRack', units='C', help='Outside, rack-side, top of the clean room'),
        Float(name='topEnt', units='C', help='Outside, entrance-side, top of the clean room'),
        help='Air temperatures inside and outside the clean room'
    ),
    Key('scrLoop',
        Float(name='airTemp', units='C', help='Air temperature'),
        Float(name='setTemp', units='C', help='Setpoint temperature'),
        Enum('unknown', 'off', 'on', name='state', help='Operational state'),
        help='State of the air temperature controller'
    ),
)
