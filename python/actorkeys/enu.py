KeysDictionary('enu', (3, 3),
               Key("controllers", String(help='controllers list') * (1, None)),
               Key('text', String(help='text for humans')),

               Key('metaFSM',
                   Enum('OFF', 'LOADED', 'ONLINE', name='state'),
                   Enum('IDLE', 'LOADING', 'INITIALISING', 'MOVING', 'EXPOSING', 'OPENRED', 'OPENBLUE', 'BIA', 'BUSY',
                        'SWITCHING', 'WARMING', 'SAFESTOP', 'FAILED', name='substate'), help='meta state machine'),

               Key('slitFSM',
                   Enum('OFF', 'LOADED', 'ONLINE', name='state',
                        FITS=('W_ENFCAS', 'ENU_FCA_STATE')),
                   Enum('IDLE', 'LOADING', 'INITIALISING', 'MOVING', 'FAILED', name='substate',
                        FITS=('W_ENFCAT', 'ENU_FCA_SUBSTATE')), help='slit state machine'),
               Key('slitMode',
                   Enum('operation', 'simulation', help='fca operation mode',
                        FITS=('W_ENFCAM', 'ENU_FCA_MODE'))),
               Key('slit',
                   Float(name='X', invalid="NaN", units="mm", help='ENU_FCA_FOCUS',
                         FITS=('W_ENFCAX', 'ENU_FCA_FOCUS')),
                   Float(name='Y', invalid="NaN", units="mm", help='ENU_FCA_SHIFT',
                         FITS=('W_ENFCAY', 'ENU_FCA_SHIFT')),
                   Float(name='Z', invalid="NaN", units="mm", help='ENU_FCA_DITHER',
                         FITS=('W_ENFCAZ', 'ENU_FCA_DITHER')),
                   Float(name='U', invalid="NaN", units="deg", help='ENU_FCA_ROLL',
                         FITS=('W_ENFCAU', 'ENU_FCA_ROLL')),
                   Float(name='V', invalid="NaN", units="deg", help='ENU_FCA_PITCH',
                         FITS=('W_ENFCAV', 'ENU_FCA_PITCH')),
                   Float(name='W', invalid="NaN", units="deg", help='ENU_FCA_YAW',
                         FITS=('W_ENFCAW', 'ENU_FCA_YAW')), help='slit current position'),
               Key('slitWork',
                   Float(name='X', help='x_coordinate', units="mm"),
                   Float(name='Y', help='y_coordinate', units="mm"),
                   Float(name='Z', help='z_coordinate', units="mm"),
                   Float(name='U', help='u_coordinate', units="deg"),
                   Float(name='V', help='v_coordinate', units="deg"),
                   Float(name='W', help='W_coordinate', units="deg"), help='slit work coordinate system'),
               Key('slitTool',
                   Float(name='X', help='x_coordinate', units="mm"),
                   Float(name='Y', help='y_coordinate', units="mm"),
                   Float(name='Z', help='z_coordinate', units="mm"),
                   Float(name='U', help='u_coordinate', units="deg"),
                   Float(name='V', help='v_coordinate', units="deg"),
                   Float(name='W', help='W_coordinate', units="deg"), help='slit tool coordinate system'),
               Key('hxpStatus',
                   Int(name='code', help='status code'),
                   String(name='msg', help='Hexapod controller status')),
               Key('slitPosition',
                   String(help='FCA position',
                          FITS=('W_ENFCAP', 'ENU_FCA_POSITION'))),

               Key('biashaFSM',
                   Enum('OFF', 'LOADED', 'ONLINE', name='state',
                        FITS=('W_ENBSHS', 'ENU_BIASHA_STATE')),
                   Enum('IDLE', 'LOADING', 'INITIALISING', 'FAILED', 'BUSY', 'EXPOSING', 'OPENRED', 'OPENBLUE', 'BIA',
                        name='substate',
                        FITS=('W_ENBSHT', 'ENU_BIASHA_SUBSTATE')), help='biasha state machine'),
               Key('biashaMode',
                   Enum('operation', 'simulation', help='biasha operation mode',
                        FITS=('W_ENBSHM', 'ENU_BIASHA_MODE'))),
               Key('shutters',
                   Enum('close', 'open', 'openred', 'openblue', 'undef', help='shutters current position',
                        FITS=('W_ENSHUT', 'ENU_SHUTTERS_POSITION'))),
               Key('shb',
                   Bool('0', '1', name='open', help='blue shutter open bit'),
                   Bool('0', '1', name='close', help='blue shutter close bit'),
                   Bool('0', '1', name='error', help='blue shutter error bit')),
               Key('shr',
                   Bool('0', '1', name='open', help='blue shutter open bit'),
                   Bool('0', '1', name='close', help='blue shutter close bit'),
                   Bool('0', '1', name='error', help='blue shutter error bit')),

               Key('exptime', Float(units="s", help='exposure time')),
               Key('transientTime', Float(units="s", help='shutters transition time')),
               Key('integratingTime', Float(units="s", help='Shutter opening duration')),
               Key('elapsedTime', Float(units="s", help='Seconds since shutters opening')),
               Key('dateobs', String(help='absolute exposure start UTC time ISO formatted')),
               Key('bia',
                   Enum('off', 'on', 'undef', name='state', help='bia current state',
                        FITS=('W_ENBIAS', 'ENU_BIA_STATE'))),
               Key('biaConfig',
                   Bool('0', '1', name='state', help='strobe enabled'),
                   Int(name='period', units='ms', help='bia strobe period'),
                   Int(name='duty', help='duty cycle(0-255)')),
               Key('photores',
                   Int(help='bia photo resistance 1'),
                   Int(help='bia photo resistance 2')),

               Key('rexmFSM',
                   Enum('OFF', 'LOADED', 'ONLINE', name='state',
                        FITS=('W_ENRDAS', 'ENU_RDA_STATE')),
                   Enum('IDLE', 'LOADING', 'INITIALISING', 'MOVING', 'SAFESTOP', 'FAILED', name='substate',
                        FITS=('W_ENRDAT', 'ENU_RDA_SUBSTATE')), help='rexm state machine'),
               Key('rexmMode',
                   Enum('operation', 'simulation', help='rda operation mode',
                        FITS=('W_ENRDAM', 'ENU_RDA_MODE'))),
               Key('rexm',
                   Enum('low', 'med', 'undef', name='position', help='rexm current position',
                        FITS=('W_ENRDAP', 'ENU_RDA_POSITION'))),
               Key('rexmInfo',
                   Int(name='switchA', help='switch A state'),
                   Int(name='switchB', help='switch B state'),
                   Int(name='speed', units='steps/s', help='motor speed step/sec'),
                   Int(name='steps', units='steps', help='step count from origin')),
               Key('rexmStop',
                   Int(name='stopButton', help='emergency stop button state'),
                   Int(name='stopFlag', help='emergency flag state')),
               Key('rexmConfig',
                   Int(name='maxSpeed', help=' max. positioning speed'),
                   Int(name='maxAcceleration', help='max. acceleration'),
                   Int(name='maxCurrent', help='max. current'),
                   Int(name='standbyCurrent', help='standby current'),
                   Int(name='rightLimitSwitchDisable', help='right limit switch disable'),
                   Int(name='leftLimitSwitchDisable', help='left limit switch disable'),
                   Int(name='minSpeed', help='minimum speed [int]'),
                   Int(name='ustepResolution', help='microstep resolution'),
                   Int(name='softStopFlag', help='soft stop flag'),
                   Int(name='rampDivisor', help='ramp divisor'),
                   Int(name='pulseDivisor', help='pulse divisor'),
                   Int(name='stepInterpolationEnable', help='step interpolation enable'),
                   Int(name='doubleStepEnable', help='double step enable'),
                   Int(name='chopperBlankTime', help='chopper blank time'),
                   Int(name='chopperMode', help='chopper mode'),
                   Int(name='chopperHystDecrement', help='chopper hysteresis decrement'),
                   Int(name='chopperHystEnd', help='chopper hysteresis end'),
                   Int(name='chopperHystStart', help='chopper hysteresis start'),
                   Int(name='chopperOffTime', help='chopper off time'),
                   Int(name='smEnergyMinCurrent', help='smartEnergy current minimum'),
                   Int(name='smEnergyCurrentDownStep', help='smartEnergy current down step'),
                   Int(name='smEnergyHyst', help='smartEnergy hysteresis'),
                   Int(name='smEnergyCurrentUpStep', help='smartEnergy current up step'),
                   Int(name='smEnergyHystStart', help='smartEnergy hysteresis start'),
                   Int(name='stallGuardFilterEnable', help='stallGuard filter enable'),
                   Int(name='stallGuardThresh', help='stallGuard threshold'),
                   Int(name='slopeControlHighSide', help='slope control high side'),
                   Int(name='slopeControlLowSide', help='slope control low side'),
                   Int(name='shortProtectionDisable', help='short protection disable'),
                   Int(name='shortDetectionTimer', help='short detection timer'),
                   Int(name='stopOnStall', help='stop on stall [int]'),
                   Int(name='smEnergyThresh', help='smartEnergy threshold speed [int]'),
                   Int(name='smEnergySlowRunCurrent', help='smartEnergy slow run current'),
                   Int(name='randomChopperOffTime', help='random chopper off time'),
                   Int(name='refSearchMode', help='reference search mode'),
                   Int(name='refSearchSpeed', help='reference search speed'),
                   Int(name='refSwitchSpeed', help='reference switch speed'),
                   Int(name='boostCurrent', help='boost current'),
                   Int(name='freeWheelingDelay', help='freewheeling delay'),
                   Int(name='encoderPrescaler', help='encoder prescaler'),
                   Int(name='maxEncoderDev', help='max. encoder deviation'),
                   Int(name='powerDownDelay', help='power down delay'),
                   Int(name='stepDirMode', help='step/direction mode')),

               Key('tempsFSM',
                   Enum('OFF', 'LOADED', 'ONLINE', name='state',
                        FITS=('W_ENTMPS', 'ENU_TEMP_STATE')),
                   Enum('IDLE', 'LOADING', 'INITIALISING', 'FAILED', name='substate',
                        FITS=('W_ENTMPT', 'ENU_TEMP_SUBSTATE')), help='rexm state machine'),
               Key('tempsMode',
                   Enum('operation', 'simulation', help='temps operation mode',
                        FITS=('W_ENTMPM', 'ENU_TEMP_MODE'))),
               Key("temps1",
                   Float(name='val1_0', invalid="NaN", units="C", FITS=('W_ETMP1', 'MOTOR_RDA')),
                   Float(name='val1_1', invalid="NaN", units="C", FITS=('W_ETMP2', 'MOTOR_SHUTTER_B')),
                   Float(name='val1_2', invalid="NaN", units="C", FITS=('W_ETMP3', 'MOTOR_SHUTTER_R')),
                   Float(name='val1_3', invalid="NaN", units="C", FITS=('W_ETMP4', 'BIA_BOX_UPPER')),
                   Float(name='val1_4', invalid="NaN", units="C", FITS=('W_ETMP5', 'BIA_BOX_LOWER')),
                   Float(name='val1_5', invalid="NaN", units="C", FITS=('W_ETMP6', 'FIBER_UNIT_BENCH_LEVEL')),
                   Float(name='val1_6', invalid="NaN", units="C", FITS=('W_ETMP7', 'FIBER_UNIT_HEXAPOD_TOP')),
                   Float(name='val1_7', invalid="NaN", units="C", FITS=('W_ETMP8', 'FIBER_UNIT_FIBER_FRAME_TOP')),
                   Float(name='val1_8', invalid="NaN", units="C", FITS=('W_ETMP9', 'COLLIMATOR_FRAME_BENCH_LEVEL')),
                   Float(name='val1_9', invalid="NaN", units="C", FITS=('W_ETMP10', 'COLLIMATOR_FRAME_TOP')),
                   help="Bench Temperatures stage1"),
               Key("temps2",
                   Float(name='val1_0', invalid="NaN", units="C", FITS=('W_ETMP11', 'BENCH_LEFT_TOP')),
                   Float(name='val1_1', invalid="NaN", units="C", FITS=('W_ETMP12', 'BENCH_LEFT_BOTTOM')),
                   Float(name='val1_2', invalid="NaN", units="C", FITS=('W_ETMP13', 'BENCH_RIGHT_TOP')),
                   Float(name='val1_3', invalid="NaN", units="C", FITS=('W_ETMP14', 'BENCH_RIGHT_BOTTOM')),
                   Float(name='val1_4', invalid="NaN", units="C", FITS=('W_ETMP15', 'BENCH_FAR_TOP')),
                   Float(name='val1_5', invalid="NaN", units="C", FITS=('W_ETMP16', 'BENCH_FAR_BOTTOM')),
                   Float(name='val1_6', invalid="NaN", units="C", FITS=('W_ETMP17', 'BENCH_NEAR_TOP')),
                   Float(name='val1_7', invalid="NaN", units="C", FITS=('W_ETMP18', 'BENCH_NEAR_BOTTOM')),
                   Float(name='val1_8', invalid="NaN", units="C", FITS=('W_ETMP19', 'BENCH_CENTRAL_BOTTOM')),
                   Float(name='val1_9', invalid="NaN", units="C", FITS=('W_ETMP20', 'ENU_TEMP_20')),
                   help="Bench Temperatures stage2"),
               Key('res1', Float(invalid='NaN', units='ohm') * 10, ),
               Key('res2', Float(invalid='NaN', units='ohm') * 10, ),
               Key('tempsVersion',
                   String(help='software version of the SCPI (Standard Commands for Programmable Instruments)')),
               Key('tempsSlot1',
                   String(name='company', help='Company name'),
                   String(name='modelNumber', help='Card model number'),
                   Int(name='serialNumber', help='Serial Number'),
                   Float(name='firmware', help='Firmware rev'), help='temperature plug-in module slot 1'),
               Key('tempsSlot2',
                   String(name='company', help='Company name'),
                   String(name='modelNumber', help='Card model number'),
                   Int(name='serialNumber', help='Serial Number'),
                   Float(name='firmware', help='Firmware rev'), help='temperature plug-in module slot 2'),
               Key('tempsStatus',
                   Int(name='code', help='status code'),
                   String(name='msg', help='Keysight controller status')),

               Key('pduFSM',
                   Enum('OFF', 'LOADED', 'ONLINE', name='state',
                        FITS=('W_ENPDUS', 'ENU_PDU_STATE')),
                   Enum('IDLE', 'LOADING', 'INITIALISING', 'SWITCHING', 'FAILED', name='substate',
                        FITS=('W_ENPDUT', 'ENU_PDU_SUBSTATE')), help='pdu state machine'),
               Key('pduMode',
                   Enum('operation', 'simulation', help='pdu operation mode',
                        FITS=('W_ENPDUM', 'ENU_PDU_MODE'))),
               Key("pduPort1",
                   String(name="name"),
                   String(name="state"),
                   Float(name="volts", units="V"),
                   Float(name="amps", units="A"),
                   Float(name="watts", units="W")),
               Key("pduPort2",
                   String(name="name"),
                   String(name="state"),
                   Float(name="volts", units="V"),
                   Float(name="amps", units="A"),
                   Float(name="watts", units="W")),
               Key("pduPort3",
                   String(name="name"),
                   String(name="state"),
                   Float(name="volts", units="V"),
                   Float(name="amps", units="A"),
                   Float(name="watts", units="W")),
               Key("pduPort4",
                   String(name="name"),
                   String(name="state"),
                   Float(name="volts", units="V"),
                   Float(name="amps", units="A"),
                   Float(name="watts", units="W")),
               Key("pduPort5",
                   String(name="name"),
                   String(name="state"),
                   Float(name="volts", units="V"),
                   Float(name="amps", units="A"),
                   Float(name="watts", units="W")),
               Key("pduPort6",
                   String(name="name"),
                   String(name="state"),
                   Float(name="volts", units="V"),
                   Float(name="amps", units="A"),
                   Float(name="watts", units="W")),
               Key("pduPort7",
                   String(name="name"),
                   String(name="state"),
                   Float(name="volts", units="V"),
                   Float(name="amps", units="A"),
                   Float(name="watts", units="W")),
               Key("pduPort8",
                   String(name="name"),
                   String(name="state"),
                   Float(name="volts", units="V"),
                   Float(name="amps", units="A"),
                   Float(name="watts", units="W")),

               Key('iisFSM',
                   Enum('OFF', 'LOADED', 'ONLINE', name='state',
                        FITS=('W_ENIISS', 'ENU_IIS_STATE')),
                   Enum('IDLE', 'LOADING', 'INITIALISING', 'WARMING', 'FAILED', name='substate',
                        FITS=('W_ENIIST', 'ENU_IIS_SUBSTATE')), help='iis state machine'),
               Key('iisMode',
                   Enum('operation', 'simulation', help='iis operation mode',
                        FITS=('W_ENIISM', 'ENU_IIS_MODE'))),
               Key('hgar',
                   Bool('off', 'on', name='state', help='Internal Illumination Sources mercury-argon lamp state',
                        FITS=('W_ENIISH', 'ENU_IIS_HGAR'))),

               )
