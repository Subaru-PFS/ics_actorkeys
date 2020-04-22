KeysDictionary('dcb', (3, 1),
               Key('text', String(help='text for humans')),
               Key('controllers', String() * (1, None)),
               Key('version', String(help='EUPS/git version')),
               Key('version_tron_actorcore', String()),
               Key('version_pfs_utils', String()),
               Key('version_ics_actorkeys', String()),
               Key('version_ics_enuActor', String()),
               Key("designId",
                   Long(name="mask", reprFmt="0x%016x", FITS=('W_PFDSGN', 'PFS_DESIGN_ID'))),
               Key("fiberConfig", String(help='fiber bundle configuration')),
               Key('metaFSM',
                   Enum('none', 'OFF', 'LOADED', 'ONLINE', name='state'),
                   Enum('none', 'IDLE', 'LOADING', 'INITIALISING', 'BUSY', 'MOVING', 'WARMING', 'TURNING_OFF',
                        'SWITCHING', 'FAILED', name='substate'), help='meta state machine'),
               Key('sourcesFSM',
                   Enum('none', 'OFF', 'LOADED', 'ONLINE', name='state'),
                   Enum('none', 'IDLE', 'LOADING', 'INITIALISING', 'WARMING', 'FAILED', name='substate')),
               Key('sourcesMode',
                   Enum('operation', 'simulation', help='sources operation mode')),
               Key('halogen',
                   Bool('off', 'on', name='state', help='Halogen switch', FITS=('W_AITQTH', 'AIT_DCB_HALOGEN')),
                   Int(name='elapsedTime', help='number of seconds since lamp is on')),
               Key('neon',
                   Bool('off', 'on', name='state', help='neon lamp switch', FITS=('W_AITNEO', 'AIT_DCB_NEON')),
                   Int(name='elapsedTime', help='number of seconds since lamp is on')),
               Key('hgar',
                   Bool('off', 'on', name='state', help='Hg-Ar switch', FITS=('W_AITHGA', 'AIT_DCB_HGAR')),
                   Int(name='elapsedTime', help='number of seconds since lamp is on')),
               Key('krypton',
                   Bool('off', 'on', name='state', help='Krypton switch', FITS=('W_AITKRY', 'AIT_DCB_KRYPTON')),
                   Int(name='elapsedTime', help='number of seconds since lamp is on')),
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
               ### PURE LAM KEYWORDS STARTING FROM HERE ###
               Key('atenFSM',
                   Enum('none', 'OFF', 'LOADED', 'ONLINE', name='state'),
                   Enum('none', 'IDLE', 'LOADING', 'INITIALISING', 'SWITCHING', 'FAILED', name='substate'),
                   help='pdu state machine'),
               Key('xenon',
                   Bool('off', 'on', name='state', help='xenon lamp switch', FITS=('W_AITXEN', 'AIT_DCB_XENON')),
                   Int(name='elapsedTime', help='number of seconds since lamp is on')),
               Key('deuterium',
                   Bool('off', 'on', name='state', help='deuterium switch', FITS=('W_AITDEU', 'AIT_DCB_DEUTERIUM')),
                   Int(name='elapsedTime', help='number of seconds since lamp is on')),
               Key('argon',
                   Bool('off', 'on', name='state', help='argon lamp switch', FITS=('W_AITARG', 'AIT_DCB_ARGON')),
                   Int(name='elapsedTime', help='number of seconds since lamp is on')),
               Key('bakeout', Bool('off', 'on', name='state', help='bakeout cover')),
               Key('roughpump', Bool('off', 'on', name='state', help='roughpump')),
               Key('sac', Bool('off', 'on', name='state', help='sac')),
               Key('breva', Bool('off', 'on', name='state', help='breva')),
               Key('mono', Bool('off', 'on', name='state', help='power monochromator')),
               Key('labsphere', Bool('off', 'on', name='state', help='labsphere power switch')),
               Key('atenVAW',
                   Float(name='voltage', help='Voltage'),
                   Float(name='current', help='Current'),
                   Float(name='power', help='Power'), help='aten current Volt, Amp, Power'),

               Key('labsphereFSM',
                   Enum('OFF', 'LOADED', 'ONLINE', name='state'),
                   Enum('IDLE', 'LOADING', 'INITIALISING', 'MOVING', 'WARMING', 'FAILED', name='substate'),
                   help='labsphere state machine'),
               Key('labsphereMode', Enum('operation', 'simulation', help='labsphere mode')),
               Key('photodiode',
                   Float(invalid='nan', help='cd/m^2 at photodiode',
                         FITS=('W_AITPHO', 'AIT_DCB_DIODEFLUX'))),
               Key('flux',
                   Float(invalid='nan', name='median', help='photodiode flux median'),
                   Float(invalid='nan', name='std', help='photodiode flux standard deviation')),
               Key('attenuator',
                   Int(help='attenuator opening value (open=0)',
                       FITS=('W_AITATT', 'AIT_DCB_ATTENUATOR'))),
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
