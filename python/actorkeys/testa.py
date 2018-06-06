KeysDictionary('testa', (1, 6),
               Key('Text', String(), help='Stuff for humans'),

               Key('loop',
                   Enum('ON','OFF','POWER',
                        name='loop',
                        FITS=('W_ZLUPST', 'TEST_LOOP_STAT'),
                        help='the state of some control loop')),

               Key('pump',
                   Bool('0', '1', name='enabled',
                        FITS=('W_ZPMPST', 'TEST_PUMP_STATE'),
                        help='pump enabled'),
                   Float(name='Voltage', invalid='NaN', units='V',
                         FITS=('W_ZPMPV', 'TEST_PUMP_VOLTAGE'),
                         help='pump voltage'),
                   Float(name='Current', invalid='NaN', units='A',
                         FITS=('W_ZPMPA', 'TEST_PUMP_CURRENT'),
                         help='pump current'),
                   Float(name='Temperature', invalid='NaN', units='K',
                         FITS=('W_ZPMPT', 'TEST_PUMP_TEMP'),
                         help='pump temperature'),
                   Float(name='Pressure', invalid='NaN', units='Torr',
                         FITS=('W_ZPMPP', 'TEST_PUMP_PRESSURE'),
                         help='pump pressure'),
                   help='Pump status.'),

               Key('valve',
                   UInt(reprFmt='0x%02x', name='maskBits',
                        FITS=('W_ZVVMSK', 'TEST_VALVE_MASK'),
                        help='valve status mask'),
                   Enum('Open', 'Closed', 'Unknown', 'Invalid',
                        name='position', help='reported position',
                        FITS=('W_ZVVPOS', 'TEST_VALVE_POS')),
                   help='valve status'),
)
