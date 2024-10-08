KeysDictionary('peb', (1, 6),
               Key("controllers", String(help='controllers list') * (1, None)),
               Key("text", String(help="text for humans")),
               Key("version", String(help="EUPS/git version")),
               Key("pfi_status", String(help="PFI router status")),
               Key('temps',
                      Float(name='AGC_4', units='degC', STS=7, help='AGC-4 Temperature'),
                      Float(name='AGC_3', units='degC', STS=8, help='AGC-3 Temperature'),
                      Float(name='AGC_2', units='degC', STS=9, help='AGC-2 Temperature'),
                      Float(name='AGC_1', units='degC', STS=10, help='AGC-1 Temperature'),
                      Float(name='AGC_6', units='degC', STS=11, help='AGC-6 Temperature'),
                      Float(name='AGC_5', units='degC', STS=12, help='AGC-5 Temperature'),
                      Float(name='UL_link_1', units='degC', STS=13, help='UL link 1 Temperature'),
                      Float(name='UL_link_2', units='degC', STS=14, help='UL link 2 Temperature'),
                      Float(name='UL_link_3', units='degC', STS=15, help='UL link 3 Temperature'),
                      Float(name='Positioner_frame', units='degC', STS=16, help='positioner frame'),
                      Float(name='COB_1', units='degC', STS=17, help='COB1 Temperature'),
                      Float(name='COB_2', units='degC', STS=18, help='COB2 Temperature'),
                      Float(name='COB_3', units='degC', STS=19, help='COB3 Temperature'),
                      Float(name='COB_4', units='degC', STS=20, help='COB4 Temperature'),
                      Float(name='COB_5', units='degC', STS=21, help='COB5 Temperature'),
                      Float(name='COB_6', units='degC', STS=22, help='COB6 Temperature'),
                      Float(name='Ebox_1', units='degC', STS=23, help='EBOX1 Temperature'),
                      Float(name='Ebox_2', units='degC', STS=24, help='EBOX2 Temperature'),
                      Float(name='Ebox_3', units='degC', STS=25, help='EBOX3 Temperature'),
                      Float(name='Flow_in', units='degC', STS=26, help='Input coolant Temperature'),
                      Float(name='Flow_out', units='degC', STS=27, help='Output coolant Temperature'),
                   help='PFI Ebox temperatures'),
               Key('humidity',
                      Float(name='Humidity', units='%', STS=0, help='E-box Humidity'),
                      Float(name='Temperature', units='degC', STS=1, help='E-box Coolant temperature'),
                      Float(name='Dew_point', units='degC', STS=2, help='E-box Dew point'),
                   help='PFI Ebox humidity sensor SHT75'),
               Key('flow',
                      Float(name='Flow_meter', units='Gal/min', STS=3, help='Coolant Flow rate'),
                      Float(name='Flow_rotor', units='Hz', STS=4, help='Flowmeter rotor speed'),
                   help='PFI Ebox flow meter'),
               Key('leakage',
                      Int(name='Leakage', units='bool', STS=5, help='Leak Sensor'),
                      Int(name='Disconnect', units='bool', STS=6, help='Leakage Sensor Disconnected'),
                   help='PFI Ebox leakage sensor'),
               Key('valve_status', 
                      Int(name='Valve_status', units='bool', STS=28, help='Coolant valve status')),
               Key('ledperiod',
                      Int(name='Now', units='uS'),
                      Int(name='On', units='uS'),
                      Int(name='Flash', units='uS'),
                   help='PFI Ebox LED peroid'),
               Key('dutycycle',
                      Float(name='Now', units='%'),
                      Float(name='On', units='%'),
                      Float(name='Flash', units='%'),
                   help='PFI Ebox LED dutycycle'),
               Key('power',
                      Int(name='AGC_1', units='V'),
                      Int(name='AGC_2', units='V'),
                      Int(name='AGC_3', units='V'),
                      Int(name='AGC_4', units='V'),
                      Int(name='AGC_5', units='V'),
                      Int(name='AGC_6', units='V'),
                      Int(name='Leakage', units='V'),
                      Int(name='Adam6015', units='V'),
                      Int(name='USB_1', units='V'),
                      Int(name='USB_2', units='V'),
                      Int(name='Flow_board', units='V'),
                      Int(name='LED_board', units='V'),
                      Int(name='Switch', units='V'),
                   help='PFI Ebox power status'),
)
