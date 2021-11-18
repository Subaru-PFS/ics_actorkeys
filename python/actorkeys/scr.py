KeysDictionary(
    'scr',
    (1, 6),
    Key('text', String(), help='Human oriented message string'),
    Key('version', String(help='SCR Actor version',
                          FITS=('W_RVSCR', 'W_SCRACTOR_VERSION'))),
    Key('spsCooler',
        Float(name='facFlow', units='LPM', help='Facility coolant flow rate'),
        Float(name='facTemp', units='degC', help='Facility coolant temperature'),
        Float(name='supFlow', units='LPM', help='Supply coolant flow rate'),
        Float(name='supTemp', units='degC', help='Supply coolant temperature'),
        help='Coolant state at the Lytron cooler for the spectrograph cryocoolers'
    ),
    Key('scrCooler',
        Float(name='facFlow', units='LPM', help='Facility coolant flow rate'),
        Float(name='facTemp', units='degC', help='Facility coolant temperature'),
        Float(name='supFlow', units='LPM', help='Supply coolant flow rate'),
        Float(name='supTemp', units='degC', help='Supply coolant temperature'),
        help='Coolant state at the Lytron cooler for the clean room heat exchangers'
    ),
    Key('spsChiller',
        Float(name='supTemp', units='degC', help='Supply coolant temperature'),
        Float(name='supFlow', units='LPM', help='Supply coolant flow rate'),
        Float(name='supPress', units='MPa', help='Supply coolant pressure'),
        Enum('off', 'on', 'warning', 'fault', 'unknown', name='state', help='Operational state'),
        help='State of the SMC thermo chiller for the spectrograph cryocoolers'
    ),
    Key('scrChiller',
        Float(name='supTemp', units='degC', help='Supply coolant temperature'),
        Float(name='supFlow', units='LPM', help='Supply coolant flow rate'),
        Float(name='supPress', units='MPa', help='Supply coolant pressure'),
        Enum('off', 'on', 'warning', 'fault', 'unknown', name='state', help='Operational state'),
        help='State of the SMC thermo chiller for the clean room heat exchangers'
    ),
    Key('spsManifold',
        Float(name='inPress', units='MPa', help='Intake coolant pressure'),
        Float(name='supFlow', units='LPM', help='Supply coolant flow rate'), # computed (sum of four branches)
        Float(name='supTemp', units='degC', help='Supply coolant temperature'), # computed (max of four branches)
        help='Coolant state at the supply manifold for the spectrograph cryocoolers'
    ),
    Key('scrManifold',
        Float(name='inPress', units='MPa', help='Intake coolant pressure'),
        Float(name='inFlow', units='LPM', help='Intake coolant flow rate'),
        Float(name='inTemp', units='degC', help='Intake coolant temperature'),
        help='Coolant state at the supply manifold for the clean room heat exchangers'
    ),
    Key('rackManifold',
        Float(name='inFlow', units='LPM', help='Intake coolant flow rate'),
        Float(name='inTemp', units='degC', help='Intake coolant temperature'),
        help='Coolant state at the supply manifold for the electronics racks'
    ),
    Key('scrHumidity',
        Float(name='dewPoint', units='degC', help='Dew point inside clean room'),
        Float(name='relHum', units='%', help='Relative humidity inside clean room',
              FITS=('W_CRRHUM', 'W_SCR_RELATIVE_HUMIDITY')),
        help='Dew point and relative humidity inside the clean room'
    ),
    Key('scrTemps',
        Float(name='bench1', units='degC', help='Bench 1'),
        Float(name='bench2', units='degC', help='Bench 2'),
        Float(name='bench3', units='degC', help='Bench 3'),
        Float(name='bench4', units='degC', help='Bench 4'),
        Float(name='hex1In', units='degC', help='Heat exchanger 1 intake'),
        Float(name='hex2In', units='degC', help='Heat exchanger 2 intake'),
        Float(name='hex3In', units='degC', help='Heat exchanger 3 intake'), # reordered
        Float(name='hex4In', units='degC', help='Heat exchanger 4 intake'), # reordered
        Float(name='hex1Exh', units='degC', help='Heat exchanger 1 exhaust'), # reordered
        Float(name='hex2Exh', units='degC', help='Heat exchanger 2 exhaust'), # reordered
        Float(name='hex3Exh', units='degC', help='Heat exchanger 3 exhaust'), # reordered
        Float(name='hex4Exh', units='degC', help='Heat exchanger 4 exhaust'), # reordered
        Float(name='ceiling1', units='degC', help='Ceiling 1'),
        Float(name='ceiling2', units='degC', help='Ceiling 2'),
        Float(name='ceiling3', units='degC', help='Ceiling 3'),
        Float(name='ceiling4', units='degC', help='Ceiling 4'),
        Float(name='bottom', units='degC', help='Outside, bottom of the clean room'),
        Float(name='topRack', units='degC', help='Outside, rack-side, top of the clean room'),
        Float(name='topEnt', units='degC', help='Outside, entrance-side, top of the clean room'),
        help='Air temperatures inside and outside the clean room'
    ),
    Key('scrLoop',
        Float(name='airTemp', units='degC', help='Clean room air temperature',
              FITS=('W_CRTEMP', 'W_SCR_CONTROL_TEMP')),              
        Float(name='setTemp', units='degC', help='Clean room setpoint temperature',
              FITS=('W_CRSETP', 'W_SCR_CONTROL_SETPOINT')),
        Enum('unknown', 'off', 'on', name='state', help='Clean room operational state',
              FITS=('W_CRLOOP', 'W_SCR_CONTROL_LOOP_STATE')),
        help='State of the air temperature controller'
    ),
    Key('scrLights',
        Enum('unknown', 'off', 'on', name='state', help='State of ceiling lights',
             FITS=('W_CRLGHT', 'W_SCR_ROOMLIGHTS')),
    ),
)
