KeysDictionary("xcu", (10, 2),
               Key("controllers", String(help='controllers list') * (1, None)),
               Key('Text', String(), help='Stuff for humans'),
               Key('version', String(help="XCU actor version",
                                     FITS=("W_RVXCU",
                                           "W_XCUACTOR_VERSION"))),
               Key('version_tron_actorcore', String()),
               Key('version_pfs_utils', String()),
               Key('version_ics_xcu_rtdadio', String()),

               # State of cooling/pumping systems.
               Key("cryoMode",
                   Enum("unknown",'offline', 'standby', 'pumpdown', 'cooldown', 'operation', 'warmup', 'bakeout',
                        help="the state of the pumping/cooling system")),

                # All cooler keys:
               Key("coolerLoop",
                   Enum("ON","OFF","POWER",
                        FITS=('W_XCOOL1', 'XCU_COOLER1_STATE'),
                        STS=0, help="Cooler1 control loop state"),
                   Float(invalid="NaN", name='P'),
                   Float(invalid="NaN", name='I'),
                   Float(invalid="NaN", name='D')),

               Key("cooler2Loop",
                   Enum("ON","OFF","POWER",
                        FITS=('W_XCOOL2', 'XCU_COOLER2_STATE'),
                        STS=1, help="Cooler2 control loop state"),
                   Float(invalid="NaN", name='P'),
                   Float(invalid="NaN", name='I'),
                   Float(invalid="NaN", name='D')),

               Key("coolerStatus",
                   Enum("ON","OFF","POWER",
                        name="state",
                        help="the state of the control loop"),
                   UInt(name="errorMask", reprFmt="0x%02x"),
                   String(name="errors",
                          STS=2, help="Cooler1 error string"),
                   Float(invalid="NaN", units="W", name='minPower'),
                   Float(invalid="NaN", units="W", name='maxPower'),
                   Float(invalid="NaN", units="W", name='power')),

               Key("cooler2Status",
                   Enum("ON","OFF","POWER",
                        name="state",
                        help="the state of the control loop"),
                   UInt(name="errorMask", reprFmt="0x%02x"),
                   String(name="errors",
                          STS=3, help="Cooler2 error string"),
                   Float(invalid="NaN", units="W", name='minPower'),
                   Float(invalid="NaN", units="W", name='maxPower'),
                   Float(invalid="NaN", units="W", name='power')),

               Key("coolerTemps",
                   Float(invalid="NaN", units="K", name='setpoint',
                         FITS=('W_XCL1ST', 'XCU_COOLER1_SETPOINT'),
                         STS=4, help="Cooler1 setpoint"),
                   Float(invalid="NaN", units="degC", name='reject',
                         FITS=('W_XCL1RJ', 'XCU_COOLER1_REJECT_TEMP'),
                         STS=5, help="Cooler1 reject temperature", ),
                   Float(invalid="NaN", units="K", name='tip',
                         FITS=('W_XCL1TP', 'XCU_COOLER1_TIP_TEMP'),
                         STS=6, help="Cooler1 tip temperature"),
                   Float(invalid="NaN", units="W", name='power',
                         FITS=('W_XCL1PW', 'XCU_COOLER1_POWER'),
                         STS=7, help="Cooler1 load"),
                   help="Cryocooler state. Setpoint, Reject, Tip."),

               Key("cooler2Temps",
                   Float(invalid="NaN", units="K", name='setpoint',
                         FITS=('W_XCL2ST', 'XCU_COOLER2_SETPOINT'),
                         STS=8, help="Cooler2 setpoint"),
                   Float(invalid="NaN", units="C", name='reject',
                         FITS=('W_XCL2RJ', 'XCU_COOLER2_REJECT_TEMP'),
                         STS=9, help="Cooler2 reject temperature"),
                   Float(invalid="NaN", units="K", name='tip',
                         FITS=('W_XCL2TP', 'XCU_COOLER2_TIP_TEMP'),
                         STS=10, help="Cooler2 tip temperature"),
                   Float(invalid="NaN", units="W", name='power',
                         FITS=('W_XCL2PW', 'XCU_COOLER2_POWER'),
                         STS=11, help="Cooler2 load"),
                   help="NIR shield cryocooler state. Setpoint, Reject, Tip."),

               # All ion gauge keywords
               Key("pressure",
                   Float(invalid="NaN", units="Torr",
                         FITS=('W_XPRESS', 'XCU_PRESSURE'),
                         STS=12,  help="Ion gauge pressure")),

               # All ion pump keywords:
               # Need to add:
               #    The error bit masks and descriptions, current spat out as text
               Key("ionpump1",
                   Bool('0', '1', name='enabled',
                        FITS=('W_XIP1EN', 'XCU_IONPUMP1_ENABLED'),
                        STS=13, help='ionpump1 enabled'),
                   Float(name='Voltage', invalid="NaN", units="V"),
                   Float(name='Current', invalid="NaN", units="A"),
                   Float(name='Temperature', invalid="NaN", units="K"),
                   Float(name='Pressure', invalid="NaN", units="Torr",
                         FITS=('W_XIP1PR', 'XCU_IONPUMP1_PRESSURE'),
                         STS=14, help='ionpump1 pressure'),
                   help="Ion pump status. Pump #1 for this dewar"),
               Key("ionpump2",
                   Bool('0', '1', name='enabled',
                        FITS=('W_XIP2EN', 'XCU_IONPUMP2_ENABLED'),
                        STS=15, help='ionpump2 enabled'),
                   Float(name='Voltage', invalid="NaN", units="V"),
                   Float(name='Current', invalid="NaN", units="A"),
                   Float(name='Temperature', invalid="NaN", units="K"),
                   Float(name='Pressure', invalid="NaN", units="Torr",
                         FITS=('W_XIP2PR', 'XCU_IONPUMP2_PRESSURE'),
                         STS=16, help='ionpump2 pressure'),
                   help="Ion pump status. Pump #2 for this dewar"),

               Key("ionpump1Errors",
                   UInt(name="errorMask", reprFmt="0x%05x"),
                   Enum("OK", "ERROR", name="errorState"),
                   String(name="errors",
                          STS=17, help="ionpump1 error string")),
               Key("ionpump2Errors",
                   UInt(name="errorMask", reprFmt="0x%05x"),
                   Enum("OK", "ERROR", name="errorState"),
                   String(name="errors",
                          STS=18, help="ionpump2 error string")),

               # PCM keywords
               Key("powerNames", String()*8,
                   help="names of the PCM power port devices."),
               Key("powerMask", Int(),
                   help="mask of the powered PCM ports. 1=on",
                   FITS=('W_XPWMSK', 'XCU_POWER_MASK')),
               Key("poweredUp", String()*(1,8),
                   help="convenience string naming the powered PCM ports"),
               Key("pcmPower1",
                   String(name="name"),
                   String(name="state", help="PCM input power state"),
                   Float(name="volts", units='V',
                         FITS=('W_XSUP1V', 'XCU_PCM_POWER_SUPPLY1'),
                         STS=19, help='PCM bus 1 input voltage'),
                   Float(name="amps"),
                   Float(name="watts")),
               Key("pcmPower2",
                   String(name="name"),
                   String(name="state", help="PCM input power state"),
                   Float(name="volts", units='V',
                         FITS=('W_XSUP2V', 'XCU_PCM_POWER_SUPPLY2'),
                         STS=20, help='PCM bus 2 input voltage'),
                   Float(name="amps"),
                   Float(name="watts")),
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
                   Float(name='val1_0', invalid="NaN", units="K", help="temp probe #1", FITS=('W_XTMP1', 'XCU_TEMP_1'), STS=21),
                   Float(name='val1_1', invalid="NaN", units="K", help="temp probe #2", FITS=('W_XTMP2', 'XCU_TEMP_2'), STS=22),
                   Float(name='val1_2', invalid="NaN", units="K", help="temp probe #3", FITS=('W_XTMP3', 'XCU_TEMP_3'), STS=23),
                   Float(name='val1_3', invalid="NaN", units="K", help="temp probe #4", FITS=('W_XTMP4', 'XCU_TEMP_4'), STS=24),
                   Float(name='val1_4', invalid="NaN", units="K", help="temp probe #5", FITS=('W_XTMP5', 'XCU_TEMP_5'), STS=25),
                   Float(name='val1_5', invalid="NaN", units="K", help="temp probe #6", FITS=('W_XTMP6', 'XCU_TEMP_6'), STS=26),
                   Float(name='val1_6', invalid="NaN", units="K", help="temp probe #7", FITS=('W_XTMP7', 'XCU_TEMP_7'), STS=27),
                   Float(name='val1_7', invalid="NaN", units="K", help="temp probe #8", FITS=('W_XTMP8', 'XCU_TEMP_8'), STS=28),
                   Float(name='val1_8', invalid="NaN", units="K", help="temp probe #9", FITS=('W_XTMP9', 'XCU_TEMP_9'), STS=29),
                   Float(name='val1_9', invalid="NaN", units="K", help="temp probe #10", FITS=('W_XTMP10', 'XCU_TEMP_10'), STS=30),
                   Float(name='val1_10', invalid="NaN", units="K", help="temp probe #11", FITS=('W_XTMP11', 'XCU_TEMP_11'), STS=31),
                   Float(name='val1_11', invalid="NaN", units="K", help="temp probe #12", FITS=('W_XTMP12', 'XCU_TEMP_12'), STS=32),
                   help="Temperatures from the IDG board"),

               Key("tempNames", String(invalid="N/C")*12,
                   help="Names of the temperature probes on the IDG board"),

               Key("heaters",
                   Int(name='H1enabled',
                       FITS=('W_XH1ENA', 'XCU_ASIC_HEATER_ENABLED'),
                       STS=33, help='asic heater enabled'),
                   Int(name='HP1enabled',
                       FITS=('W_XHP1EN', 'XCU_SHIELD_HEATER_ENABLED'),
                       STS=34, help='shield heater enabled'),
                   Float(name='H1fraction',
                         FITS=('W_XH1FRA', 'XCU_ASIC_HEATER_FRACTION'),
                         STS=35,  help='frac power to asic heater: 0..1'),
                   Float(name='HP1fraction',
                         FITS=('W_XHP2FR', 'XCU_SHIELD_HEATER_FRACTION'),
                         STS=36, help='frac power to shield heater: 0 or 1'),
                   Int(name='H2enabled',
                       FITS=('W_XH2ENA', 'XCU_CCD_HEATER_ENABLED'),
                       STS=37,  help='ccd heater enabled'),
                   Int(name='HP2enabled',
                       FITS=('W_XHP2EN', 'XCU_SPREADER_HEATER_ENABLED'),
                       STS=38,  help='spreader heater enabled'),
                   Float(name='H2fraction',
                         FITS=('W_XH2FRA', 'XCU_CCD_HEATER_FRACTION'),
                         STS=39, help='frac power to ccd heater: 0..1'),
                   Float(name='HP2fraction',
                         FITS=('W_XHP2FR', 'XCU_SPREADER_HEATER_FRACTION'),
                         STS=40,  help='frac power to spreader: 0 or 1'),
                   help='status of the heaters.'),

               Key("gatevalve",
                   UInt(),
                   Enum('Open', 'Closed', 'Unknown', 'Invalid',
                        name='position',
                        FITS=('W_XGATPS', 'XCU_GATEVALVE_POSITION'),
                        STS=41, help='actual gatevalve position'),
                   Enum('Open', 'Closed', 'Blocked', 'Invalid', 'TimedOut',
                        name='controlState',
                        FITS=('W_XGATRQ', 'XCU_GATEVALVE_REQUESTED_POS'),
                        STS=42, help='gatevalve request status'),
                   help='status of the gate valve'),

               Key("sampower", Bool('0', '1', name='enabled'),
                   FITS=('W_XSAMPW', 'XCU_SAM_POWER'),
                   STS=43, help='SAM power state'),

               Key("turboSpeed",
                   Int(units="rpm",
                       FITS=('W_XTBOSP', 'XCU_TURBO_SPEED'),
                       STS=44,  help='turbo pump speed')),
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
                        help="ccd motor2 steps",
                        FITS=('W_XM2STP', 'XCU_CCDMOT2_STEPS')),
                    Float(invalid="NaN", units="um", name='position',
                          help='arm 2 vertex offset from home',
                          FITS=('W_XM2POS', 'XCU_CCDARM2_POSITION')),
                    help="Motor 2: 4:00 facing visible dewar"),
                Key("ccdMotor3",
                    Enum('OK', 'Unknown', name='status'),
                    Int(invalid=-1, name='homeSwitch'),
                    Int(invalid=-1, name='farLimitSwitch'),
                    Int(invalid=0, units="steps", name='steps',
                        help="ccd motor3 steps",
                        FITS=('W_XM3STP', 'XCU_CCDMOT3_STEPS')),
                    Float(invalid="NaN", units="um", name='position',
                          help='arm 3 vertex offset from home',
                          FITS=('W_XM3POS', 'XCU_CCDARM3_POSITION')),
                    help="Motor 3: 8:00 facing visible dewar"),

               Key("interlock",
                   UInt(name="flags", reprFmt="0x%02x"),
                   String(name="description")),
               Key("interlockPressures",
                   Float(units="mbar", name='cryostatPressure'),
                   Float(units="mbar", name='roughingPressure')),
)
