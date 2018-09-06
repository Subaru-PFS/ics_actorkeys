KeysDictionary("xcu", (6, 1),
               Key('Text', String(), help='Stuff for humans'),
               # All cooler keys:
               Key("coolerLoop",
                   Enum("ON","OFF","POWER",
                        FITS=('W_XCOOL1', 'XCU_COOLER1_STATE'),
                        help="the state of the control loop"),
                   Float(invalid="NaN", name='P'), 
                   Float(invalid="NaN", name='I'), 
                   Float(invalid="NaN", name='D')),

               Key("cooler2Loop",
                   Enum("ON","OFF","POWER",
                        FITS=('W_XCOOL2', 'XCU_COOLER2_STATE'),
                        help="the state of the control loop"),
                   Float(invalid="NaN", name='P'), 
                   Float(invalid="NaN", name='I'), 
                   Float(invalid="NaN", name='D')),

               Key("coolerStatus",
                   Enum("ON","OFF","POWER",
                        name="state",
                        help="the state of the control loop"),
                   UInt(name="errorMask", reprFmt="0x%02x"),
                   String(name="errors", help="human-oriented error string"),
                   Float(invalid="NaN", units="W", name='minPower'), 
                   Float(invalid="NaN", units="W", name='maxPower'), 
                   Float(invalid="NaN", units="W", name='power')),

               Key("cooler2Status",
                   Enum("ON","OFF","POWER",
                        name="state",
                        help="the state of the control loop"),
                   UInt(name="errorMask", reprFmt="0x%02x"),
                   String(name="errors", help="human-oriented error string"),
                   Float(invalid="NaN", units="W", name='minPower'), 
                   Float(invalid="NaN", units="W", name='maxPower'), 
                   Float(invalid="NaN", units="W", name='power')),

               Key("coolerTemps",
                   Float(invalid="NaN", units="K", name='setpoint',
                         FITS=('W_XCL1ST', 'XCU_COOLER1_SETPOINT'),
                         help="Cooler1 setpoint"),
                   Float(invalid="NaN", units="degC", name='reject',
                         FITS=('W_XCL1RJ', 'XCU_COOLER1_REJECT_TEMP'),
                         help="Cooler1 reject temperature"),
                   Float(invalid="NaN", units="K", name='tip',
                         FITS=('W_XCL1TP', 'XCU_COOLER1_TIP_TEMP'),
                         help="Cooler1 tip temperature"),
                   Float(invalid="NaN", units="W", name='power',
                         FITS=('W_XCL1PW', 'XCU_COOLER1_POWER'),
                         help="Cooler1 load"),
                   help="Cryocooler state. Setpoint, Reject, Tip."),

               Key("cooler2Temps",
                   Float(invalid="NaN", units="K", name='setpoint',
                         FITS=('W_XCL2ST', 'XCU_COOLER2_SETPOINT'),
                         help="Cooler2 setpoint"),
                   Float(invalid="NaN", units="C", name='reject',
                         FITS=('W_XCL2RJ', 'XCU_COOLER2_REJECT_TEMP'),
                         help="Cooler2 reject temperature"),
                   Float(invalid="NaN", units="K", name='tip',
                         FITS=('W_XCL2TP', 'XCU_COOLER2_TIP_TEMP'),
                         help="Cooler2 tip temperature"),
                   Float(invalid="NaN", units="W", name='power',
                         FITS=('W_XCL2PW', 'XCU_COOLER2_POWER'),
                         help="Cooler2 load"),
                   help="NIR shield cryocooler state. Setpoint, Reject, Tip."),

               # All ion gauge keywords
               Key("pressure", Float(invalid="NaN", units="Torr"),
                   help="Ion gauge pressure",
                   FITS=('W_XPRESS', 'XCU_PRESSURE')),

               # All ion pump keywords:
               # Need to add:
               #    The error bit masks and descriptions, current spat out as text
               Key("ionpump1",
                   Bool('0', '1', name='enabled', help='is ionpump1 enabled'),
                   Float(name='Voltage', invalid="NaN", units="V"),
                   Float(name='Current', invalid="NaN", units="A"),
                   Float(name='Temperature', invalid="NaN", units="K"),
                   Float(name='Pressure', invalid="NaN", units="Torr",
                         help='ionpump 1 pressure',
                         FITS=('W_XIONP1', 'XCU_IONPUMP1_PRESSURE')),
                   help="Ion pump status. Pump #1 for this dewar"),
               Key("ionpump2",
                   Bool('0', '1', name='enabled'),
                   Float(name='Voltage', invalid="NaN", units="V"),
                   Float(name='Current', invalid="NaN", units="A"),
                   Float(name='Temperature', invalid="NaN", units="K"),
                   Float(name='Pressure', invalid="NaN", units="Torr",
                         help='ionpump 2 pressure',
                         FITS=('W_XIONP2', 'XCU_IONPUMP2_PRESSURE')),
                   help="Ion pump status. Pump #2 for this dewar"),

               Key("ionpump1Errors",
                   UInt(name="errorMask", reprFmt="0x%02x"),
                   Enum("OK", "ERROR", name="errorState")),
               Key("ionpump2Errors",
                   UInt(name="errorMask", reprFmt="0x%02x"),
                   Enum("OK", "ERROR", name="errorState")),

               # PCM keywords
               Key("powerNames", String()*8,
                   help="names of the PCM power port devices."),
               Key("powerMask", Int(),
                   help="mask of the powered PCM ports. 1=on",
                   FITS=('W_XPWMSK', 'XCU_POWER_MASK')),
               Key("poweredUp", String()*(1,8),
                   help="convenience string naming the powered PCM ports"),
               Key("pcmPower",
                   Float("bus1", units='V',
                         help='PCM bus 1 input voltage',
                         FITS=('W_XSUP1V', 'XCU_PCM_POWER_SUPPLY1')),
                   Float("bus2", units='V',
                         help='PCM bus 2 input voltage',
                         FITS=('W_XSUP2V', 'XCU_PCM_POWER_SUPPLY2')),
                   help="input voltages for the two power busses"),
               Key("pcmPort1",
                   String(name="name"),
                   String(name="state"),
                   Float(name="volts"),
                   Float(name="amps"),
                   Float(name="watts")),
               Key("pcmPort2",
                   String(name="name"),
                   String(name="state"),
                   Float(name="volts"),
                   Float(name="amps"),
                   Float(name="watts")),
               Key("pcmPort3",
                   String(name="name"),
                   String(name="state"),
                   Float(name="volts"),
                   Float(name="amps"),
                   Float(name="watts")),
               Key("pcmPort4",
                   String(name="name"),
                   String(name="state"),
                   Float(name="volts"),
                   Float(name="amps"),
                   Float(name="watts")),
               Key("pcmPort5",
                   String(name="name"),
                   String(name="state"),
                   Float(name="volts"),
                   Float(name="amps"),
                   Float(name="watts")),
               Key("pcmPort6",
                   String(name="name"),
                   String(name="state"),
                   Float(name="volts"),
                   Float(name="amps"),
                   Float(name="watts")),
               Key("pcmPort7",
                   String(name="name"),
                   String(name="state"),
                   Float(name="volts"),
                   Float(name="amps"),
                   Float(name="watts")),
               Key("pcmPort8",
                   String(name="name"),
                   String(name="state"),
                   Float(name="volts"),
                   Float(name="amps"),
                   Float(name="watts")),

               # Temp & heater keywords
               #    Still need heater names, description of high power heaters.
               Key("temps",
                   Float(invalid="NaN", units="K", help="temp probe #1", FITS=('W_XTMP1', 'XCU_TEMP_1'),
                   Float(invalid="NaN", units="K", help="temp probe #2", FITS=('W_XTMP2', 'XCU_TEMP_2'),
                   Float(invalid="NaN", units="K", help="temp probe #3", FITS=('W_XTMP3', 'XCU_TEMP_3'),
                   Float(invalid="NaN", units="K", help="temp probe #4", FITS=('W_XTMP4', 'XCU_TEMP_4'),
                   Float(invalid="NaN", units="K", help="temp probe #5", FITS=('W_XTMP5', 'XCU_TEMP_5'),
                   Float(invalid="NaN", units="K", help="temp probe #6", FITS=('W_XTMP6', 'XCU_TEMP_6'),
                   Float(invalid="NaN", units="K", help="temp probe #7", FITS=('W_XTMP7', 'XCU_TEMP_7'),
                   Float(invalid="NaN", units="K", help="temp probe #8", FITS=('W_XTMP8', 'XCU_TEMP_8'),
                   Float(invalid="NaN", units="K", help="temp probe #9", FITS=('W_XTMP9', 'XCU_TEMP_9'),
                   Float(invalid="NaN", units="K", help="temp probe #10", FITS=('W_XTMP10', 'XCU_TEMP_10'),
                   Float(invalid="NaN", units="K", help="temp probe #11", FITS=('W_XTMP11', 'XCU_TEMP_11'),
                   Float(invalid="NaN", units="K", help="temp probe #12", FITS=('W_XTMP12', 'XCU_TEMP_12'),
                   help="Temperatures from the IDG board"),
               Key("tempNames", String(invalid="N/C")*12,
                   help="Names of the temperature probes on the IDG board"),

               Key("heaters",
                   Int(name='H1enabled', help='ccd heater enabled',
                       FITS=('W_XH1ENA', 'XCU_CCD_HEATER_ENABLED')),
                   Int(name='HP1enabled', help='spreader heater enabled',
                       FITS=('W_XHP1EN', 'XCU_SPREADER_HEATER_ENABLED')),
                   Float(name='H1fraction', help='frac power to ccd heater: 0..1',
                         FITS=('W_XH1FRA', 'XCU_CCD_HEATER_FRACTION')),
                   Float(name='HP1fraction', help='frac power to spreader heater: 0 or 1',
                         FITS=('W_XHP2FR', 'XCU_SPREADER_HEATER_FRACTION')),
                   Int(name='H2enabled', help='asic heater enabled',
                       FITS=('W_XH2ENA', 'XCU_ASIC_HEATER_ENABLED')),
                   Int(name='HP2enabled', help='shield heater enabled',
                       FITS=('W_XHP2EN', 'XCU_SHIELD_HEATER_ENABLED')),
                   Float(name='H2fraction', help='frac power to asic heater: 0..1',
                         FITS=('W_XH2FRA', 'XCU_ASIC_HEATER_FRACTION')),
                   Float(name='HP2fraction', help='frac power to shield: 0 or 1',
                         FITS=('W_XHP2FR', 'XCU_SHIELD_HEATER_FRACTION')),
                   help='status of the heaters.'),

               Key("gatevalve",
                   UInt(),
                   Enum('Open', 'Closed', 'Unknown', 'Invalid',
                        name='position', help='requested gatevalve position',
                        FITS=('W_XGATRQ', 'XCU_GATEVALVE_REQUESTED_POS')),
                   Enum('Open', 'Closed', 'Blocked', 'Invalid',
                        name='controlState', help='actual gatevalve state',
                        FITS=('W_XGATPS', 'XCU_GATEVALVE_POSITION')),
                   help='status of the gate valve'),

               Key("sampower", Bool('0', '1', name='enabled'),
                   help='SAM power state',
                   FITS=('W_XSAMPW', 'XCU_SAM_POWER')),


               Key("turboSpeed",
                   Int(units="rpm")),
               Key("turboStatus",
                   UInt(name="flags", reprFmt="0x%08x"),
                   String(name="description")),
               Key("turboVAW",
                   Float(invalid="NaN", units="V", name='voltage'), 
                   Float(invalid="NaN", units="A", name='current'), 
                   Float(invalid="NaN", units="W", name='power'), 
                   help="Turbo pump draw. Use W, as A has useless resolution."),
               Key('turboTemps',
                   Float(invalid="NaN", units="degC", name='bodyTemp'), 
                   Float(invalid="NaN", units="degC", name='controllerTemp')), 

                # Motors:
                Key("ccdMotor1",
                    Enum('OK', 'Unknown', name='status'),
                    Int(invalid=-1, name='homeSwitch'),
                    Int(invalid=-1, name='farLimitSwitch'),
                    Int(invalid=0, units="steps", name='steps',
                        help="ccd motor1 steps",
                        FITS=('W_XM1STP', 'XCU_CCDMOT1_STEPS')),
                    Float(invalid="NaN", units="um", name='position',
                          help='arm 1 vertex offset from home',
                          FITS=('W_XM1POS', 'XCU_CCDARM1_POSITION')),
                    help="Motor 1: 12:00 facing visible dewar"),
                Key("ccdMotor2",
                    Enum('OK', 'Unknown', name='status'),
                    Int(invalid=-1, name='homeSwitch'),
                    Int(invalid=-1, name='farLimitSwitch'),
                    Int(invalid=0, units="steps", name='steps',
                        help="ccd motor1 steps",
                        FITS=('W_XM1STP', 'XCU_CCDMOT1_STEPS')),
                    Float(invalid="NaN", units="um", name='position',
                          help='arm 2 vertex offset from home',
                          FITS=('W_XM2POS', 'XCU_CCDARM2_POSITION')),
                    help="Motor 2: 4:00 facing visible dewar"),
                Key("ccdMotor3",
                    Enum('OK', 'Unknown', name='status'),
                    Int(invalid=-1, name='homeSwitch'),
                    Int(invalid=-1, name='farLimitSwitch'),
                    Int(invalid=0, units="steps", name='steps',
                        help="ccd motor1 steps",
                        FITS=('W_XM1STP', 'XCU_CCDMOT1_STEPS')),
                    Float(invalid="NaN", units="um", name='position',
                          help='arm 3 vertex offset from home',
                          FITS=('W_XM3POS', 'XCU_CCDARM3_POSITION')),
                    help="Motor 3: 8:00 facing visible dewar"),
)
