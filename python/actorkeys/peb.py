KeysDictionary('peb', (1, 4),
               Key("text", String(help="text for humans")),
               Key("version", String(help="EUPS/git version")),
               Key('temps',
                      Float(name='AGC_4', units='degC', STS=7, help='Temperature of AGC-4'),
                      Float(name='AGC_3', units='degC', STS=8, help='Temperature of AGC-3'),
                      Float(name='AGC_2', units='degC', STS=9, help='Temperature of AGC-2'),
                      Float(name='AGC_1', units='degC', STS=10, help='Temperature of AGC-1'),
                      Float(name='AGC_6', units='degC', STS=11, help='Temperature of AGC-6'),
                      Float(name='AGC_5', units='degC', STS=12, help='Temperature of AGC-5'),
                      Float(name='UL_link_1', units='degC', STS=13, help='Temperature of UL link 1'),
                      Float(name='UL_link_2', units='degC', STS=14, help='Temperature of UL link 2'),
                      Float(name='UL_link_3', units='degC', STS=15, help='Temperature of UL link 3'),
                      Float(name='Positioner_frame', units='degC', STS=16, help='Temperature of positioner frame'),
                      Float(name='COB_1', units='degC', STS=17, help='Temperature of COB1'),
                      Float(name='COB_2', units='degC', STS=18, help='Temperature of COB2'),
                      Float(name='COB_3', units='degC', STS=19, help='Temperature of COB3'),
                      Float(name='COB_4', units='degC', STS=20, help='Temperature of COB4'),
                      Float(name='COB_5', units='degC', STS=21, help='Temperature of COB5'),
                      Float(name='COB_6', units='degC', STS=22, help='Temperature of COB6'),
                      Float(name='Ebox_1', units='degC', STS=23, help='Temperature of EBOX1'),
                      Float(name='Ebox_2', units='degC', STS=24, help='Temperature of EBOX2'),
                      Float(name='Ebox_3', units='degC', STS=25, help='Temperature of EBOX3'),
                      Float(name='Flow_in', units='degC', STS=26, help='Temperature of input coolant'),
                      Float(name='Flow_out', units='degC', STS=27, help='Temperature of output coolant'),
                   help='PFI Ebox temperatures'),
               Key('humidity',
                      Float(name='Humidity', units='%', STS=0, help='Current humidity of PFI E-box'),
                      Float(name='Temperature', units='degC', STS=1, help='Coolant temerature'),
                      Float(name='Dew_point', units='degC', STS=2, help='Dew point temerature'),
                   help='PFI Ebox humidity sensor SHT75'),
               Key('flow',
                      Float(name='Flow_meter', units='Gal/min', STS=3, help='Flow rate of PFI coolant'),
                      Float(name='Flow_rotor', units='Hz', STS=4, help='Flowmeter rotor speed'),
                   help='PFI Ebox flow meter'),
               Key('leakage',
                      Int(name='Leakage', units='bool', STS=5, help='Leakage indicator, 0 = leak!'),
                      Int(name='Disconnect', units='bool', STS=6, help='Leakage sensor healthy indicator, 0 = disconnected!'),
                   help='PFI Ebox leakage sensor'),
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
