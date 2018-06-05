KeysDictionary('meb', (1, 7),
               Key("text", String(help="text for humans")),
               Key("version", String(help="EUPS/git version")),
               Key('temps',
                      Float(name='Top_plate', units='degC',
                            help="Top plate temp",
                            FITS=('W_MCTOPT', 'MCP_TOPPLATE_TEMP')),
                      Float(name='Carbon_fiber_tube', units='degC',
                            help="Carbon fiber tube temp",
                            FITS=('W_MCCFTT', 'MCP_TUBE_TEMP')),
                      Float(name='Primary_mirror', units='degC',
                            help="Primary mirror temp",
                            FITS=('W_MCM1T', 'MCP_M1_TEMP')),
                      Float(name='Cover_panel', units='degC',
                            help="Cover panel temp",
                            FITS=('W_MCTCOVT', 'MCP_COVERPLATE_TEMP')),
                      Float(name='Coolant_water_in', units='degC',
                            help="Coolant inlet temp",
                            FITS=('W_MCCINT', 'MCP_COOLANTIN_TEMP')),
                      Float(name='Coolant_water_out', units='degC',
                            help="Coolant outlet temp",
                            FITS=('W_MCCOTT', 'MCP_COOLANTOUT_TEMP')),
                      Float(name='Electronic_rack', units='degC',
                            help="Electronics rack temp",
                            FITS=('W_MCELET', 'MCP_ELECTRONICS_TEMP')),
                   help='MCS Ebox temperatures'),
               Key('power',
                      Int(name='Camera', units='V'),
                      Int(name='Shutter_and_Temp', units='V'),
                      Int(name='Cisco_switch', units='V'),
                      Int(name='MCS_computer', units='V'),
                   help='MCS power status'),
               Key('flow',
                   Float(name='Flow_meter', units='Hz',
                         help='Flow meter reading',
                         FITS=('W_MCFLOW', 'MCP__COOLANT_FLOW')),
)
