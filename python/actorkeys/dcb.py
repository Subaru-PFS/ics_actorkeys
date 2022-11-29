KeysDictionary('dcb', (3, 11),
               Key('text', String(help='text for humans')),
               Key('controllers', String() * (1, None)),
               Key('version', String(help='DCB actor version',
                                     FITS=('W_RVDCB', 'W_DCBACTOR_VERSION'))),
               Key('version_tron_actorcore', String()),
               Key('version_pfs_utils', String()),
               Key('version_ics_actorkeys', String()),
               Key('version_ics_enuActor', String()),

               Key("designId",
                   Long(name="mask", reprFmt="0x%016x")),
               Key("fiberConfig", String(help='fiber bundle configuration')),
               Key("dcbConfigDate",
                   Float(name="mjd", help="MJD seconds when dcb config actually changed.")),
               Key("dcbMasks",
                   String(name="mask1", FITS=('W_DMSK01', 'DCB_MASK01')),
                   String(name="mask2", FITS=('W_DMSK02', 'DCB_MASK02')),
                   String(name="mask3", FITS=('W_DMSK03', 'DCB_MASK03')),
                   String(name="mask4", FITS=('W_DMSK04', 'DCB_MASK04')),
                   String(name="mask5", FITS=('W_DMSK05', 'DCB_MASK05')),
                   String(name="mask6", FITS=('W_DMSK06', 'DCB_MASK06')),
                   String(name="mask7", FITS=('W_DMSK07', 'DCB_MASK07')),
                   String(name="mask8", FITS=('W_DMSK08', 'DCB_MASK08')),
                   String(name="mask9", FITS=('W_DMSK09', 'DCB_MASK09')),
                   String(name="mask10", FITS=('W_DMSK10', 'DCB_MASK10')),
                   String(name="mask11", FITS=('W_DMSK11', 'DCB_MASK11')),
                   String(name="mask12", FITS=('W_DMSK12', 'DCB_MASK12'))),
               Key("dcbBundles",
                   String(name="bundle1", FITS=('W_DBNL01', 'DCB_BUNDLE01')),
                   String(name="bundle2", FITS=('W_DBNL02', 'DCB_BUNDLE02')),
                   String(name="bundle3", FITS=('W_DBNL03', 'DCB_BUNDLE03')),
                   String(name="bundle4", FITS=('W_DBNL04', 'DCB_BUNDLE04')),
                   String(name="bundle5", FITS=('W_DBNL05', 'DCB_BUNDLE05')),
                   String(name="bundle6", FITS=('W_DBNL06', 'DCB_BUNDLE06')),
                   String(name="bundle7", FITS=('W_DBNL07', 'DCB_BUNDLE07')),
                   String(name="bundle8", FITS=('W_DBNL08', 'DCB_BUNDLE08')),
                   String(name="bundle9", FITS=('W_DBNL09', 'DCB_BUNDLE09')),
                   String(name="bundle10", FITS=('W_DBNL10', 'DCB_BUNDLE10')),
                   String(name="bundle11", FITS=('W_DBNL11', 'DCB_BUNDLE11')),
                   String(name="bundle12", FITS=('W_DBNL12', 'DCB_BUNDLE12'))),
               Key("collSet1Masks", String() * 5, help="collimator set1 masks config"),
               Key("collSet1Bundles", String() * 5, help="collimator set1 bundles config"),
               Key("collSet2Masks", String() * 5, help="collimator set2 masks config"),
               Key("collSet2Bundles", String() * 5, help="collimator set2 bundles config"),
               Key("collSet3Masks", String() * 5, help="collimator set3 masks config"),
               Key("collSet3Bundles", String() * 5, help="collimator set3 bundles config"),
               Key("collSet4Masks", String() * 5, help="collimator set4 masks config"),
               Key("collSet4Bundles", String() * 5, help="collimator set4 bundles config"),
               Key("collSet5Masks", String() * 1, help="single collimator mask config"),
               Key("collSet5Bundles", String() * 1, help="single collimator bundle config"),

               Key('lampNames', String() * (1, None)),
               Key('metaFSM',
                   Enum('none', 'OFF', 'LOADED', 'ONLINE', name='state'),
                   Enum('none', 'IDLE', 'LOADING', 'INITIALISING', 'BUSY', 'MOVING', 'WARMING', 'TURNING_OFF',
                        'SWITCHING', 'TRIGGERING', 'FAILED', name='substate'), help='meta state machine'),
               Key('lampsFSM',
                   Enum('none', 'OFF', 'LOADED', 'ONLINE', name='state'),
                   Enum('none', 'IDLE', 'LOADING', 'INITIALISING', 'WARMING', 'TRIGGERING', 'FAILED', name='substate')),
               Key('lampsMode',
                   Enum('operation', 'simulation', help='sources operation mode')),

               Key('halogen',
                   Bool('off', 'on', name='state', help='Halogen lamp state'),
                   String(name='offTime', help='timestamp when lamp turned off - ISO formatted'),
                   String(name='onTime', help='timestamp when lamp turned on - ISO formatted')),
               Key('neon',
                   Bool('off', 'on', name='state', help='Neon lamp state'),
                   String(name='offTime', help='timestamp when lamp turned off - ISO formatted'),
                   String(name='onTime', help='timestamp when lamp turned on - ISO formatted')),
               Key('hgar',
                   Bool('off', 'on', name='state', help='HgAr lamp state'),
                   String(name='offTime', help='timestamp when lamp turned off - ISO formatted'),
                   String(name='onTime', help='timestamp when lamp turned on - ISO formatted')),
               Key('krypton',
                   Bool('off', 'on', name='state', help='Krypton lamp state'),
                   String(name='offTime', help='timestamp when lamp turned off - ISO formatted'),
                   String(name='onTime', help='timestamp when lamp turned on - ISO formatted')),
               Key('argon',
                   Bool('off', 'on', name='state', help='Argon lamp state'),
                   String(name='offTime', help='timestamp when lamp turned off - ISO formatted'),
                   String(name='onTime', help='timestamp when lamp turned on - ISO formatted')),
               Key('xenon',
                   Bool('off', 'on', name='state', help='Xenon lamp state'),
                   String(name='offTime', help='timestamp when lamp turned off - ISO formatted'),
                   String(name='onTime', help='timestamp when lamp turned on - ISO formatted')),

               Key('filterwheelFSM',
                   Enum('none', 'OFF', 'LOADED', 'ONLINE', name='state'),
                   Enum('none', 'IDLE', 'LOADING', 'INITIALISING', 'WARMING', 'FAILED', name='substate')),
               Key('filterwheelMode',
                   Enum('operation', 'simulation', help='sources operation mode')),
               Key('filterwheel',
                   Bool('off', 'on', name='state', help='power supply state for filterwheel')),
               Key('linewheel',
                   Int(name='position', help='line wheel position (1-5)'),
                   String(name='hole', help='line wheel hole size', FITS=('W_AITLWH', 'AIT_DCB_LINEWHEEL'))),
               Key('qthwheel',
                   Int(name='position', help='qth wheel position (1-5)'),
                   String(name='hole', help='qth wheel hole size', FITS=('W_AITQWH', 'AIT_DCB_QTHWHEEL'))),
               Key('adc',
                   Float(name='channel1', help='calibrated channel 1 adc value'),
                   Float(name='channel2', help='calibrated channel 2 adc value')),

               # PURE LAM KEYWORDS STARTING FROM HERE #

               Key('sourcesFSM',
                   Enum('none', 'OFF', 'LOADED', 'ONLINE', name='state'),
                   Enum('none', 'IDLE', 'LOADING', 'INITIALISING', 'WARMING', 'TRIGGERING', 'FAILED', name='substate')),
               Key('sourcesMode',
                   Enum('operation', 'simulation', help='sources operation mode')),

               Key('pduFSM',
                   Enum('none', 'OFF', 'LOADED', 'ONLINE', name='state'),
                   Enum('none', 'IDLE', 'LOADING', 'INITIALISING', 'SWITCHING', 'FAILED', name='substate'),
                   help='pdu state machine'),
               Key('pduMode',
                   Enum('operation', 'simulation', help='pdu operation mode')),
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

               Key('monoFSM',
                   Enum('OFF', 'LOADED', 'ONLINE', name='state'),
                   Enum('IDLE', 'LOADING', 'INITIALISING', 'MOVING', 'OPENING', 'CLOSING', 'FAILED', name='substate'),
                   help='monochromator state machine'),
               Key('monoMode', Enum('operation', 'simulation', help='monochromator mode')),
               Key('monograting',
                   Int(help='grating Number', name='nb'),
                   Float(invalid='nan', help='lines per mm'),
                   Float(invalid='nan', help='')),
               Key('monochromator',
                   Enum('open', 'closed', name='shutter', help='shutter state'),
                   Int(help='outport number', name='outport'),
                   Float(invalid='nan', name='wavelength', help='wavelength (nm)',
                         FITS=('W_AITWAV', 'AIT_MONO_WAVELENGTH'))),
               Key('monoerror', String(help='text for humans')),

               Key('monoqthFSM',
                   Enum('OFF', 'LOADED', 'ONLINE', name='state'),
                   Enum('IDLE', 'LOADING', 'INITIALISING', 'WARMING', 'TURNING_OFF', 'FAILED', name='substate'),
                   help='monoqth state machine'),
               Key('monoqthMode', Enum('operation', 'simulation', help='monoqth mode')),
               Key('monoqthVAW',
                   Float(name='voltage', help='Voltage'),
                   Float(name='current', help='Current'),
                   Float(name='power', help='Power'), help='aten current Volt, Amp, Power'),
               Key('monoqth',
                   Bool('off', 'on', name='state', help='power'),
                   UInt(name="stb", help='status byte'),
                   UInt(name="esr", help='error registry'), help='monoqth status'),
               )
