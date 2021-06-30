KeysDictionary('aten', (1, 1),
               Key('text', String(help='text for humans')),
               Key('controllers', String() * (1, None)),
               Key('version', String(help='ATEN actor version')),
               Key('version_tron_actorcore', String()),
               Key('version_pfs_utils', String()),
               Key('version_ics_actorkeys', String()),
               Key('version_ics_enuActor', String()),
               Key('metaFSM',
                   Enum('none', 'OFF', 'LOADED', 'ONLINE', name='state'),
                   Enum('none', 'IDLE', 'LOADING', 'INITIALISING', 'BUSY', 'MOVING', 'WARMING', 'TURNING_OFF',
                        'SWITCHING', 'TRIGGERING', 'FAILED', name='substate'), help='meta state machine'),

               Key('pduFSM',
                   Enum('none', 'OFF', 'LOADED', 'ONLINE', name='state'),
                   Enum('none', 'IDLE', 'LOADING', 'INITIALISING', 'SWITCHING', 'FAILED', name='substate'),
                   help='pdu state machine'),
               Key('pduMode',
                   Enum('operation', 'simulation', help='pdu operation mode')),
               Key('atenVAW',
                   Float(name='voltage', help='Voltage'),
                   Float(name='current', help='Current'),
                   Float(name='power', help='Power'), help='aten current Volt, Amp, Power'),
               Key('neon',
                   Bool('off', 'on', name='state', help='neon switch'),
                   Int(name='elapsedTime', help='number of seconds since outlet is on')),
               Key('xenon',
                   Bool('off', 'on', name='state', help='xenon switch'),
                   Int(name='elapsedTime', help='number of seconds since outlet is on')),
               Key('hgar',
                   Bool('off', 'on', name='state', help='hgar switch'),
                   Int(name='elapsedTime', help='number of seconds since outlet is on')),
               Key('krypton',
                   Bool('off', 'on', name='state', help='krypton switch'),
                   Int(name='elapsedTime', help='number of seconds since outlet is on')),
               Key('breva',
                   Bool('off', 'on', name='state', help='breva switch'),
                   Int(name='elapsedTime', help='number of seconds since outlet is on')),
               Key('deuterium',
                   Bool('off', 'on', name='state', help='deuterium switch'),
                   Int(name='elapsedTime', help='number of seconds since outlet is on')),
               Key('argon',
                   Bool('off', 'on', name='state', help='argon switch'),
                   Int(name='elapsedTime', help='number of seconds since outlet is on')),
               Key('roughpump',
                   Bool('off', 'on', name='state', help='roughpump switch'),
                   Int(name='elapsedTime', help='number of seconds since outlet is on')),
               Key('roughpump2',
                   Bool('off', 'on', name='state', help='roughpump2 switch'),
                   Int(name='elapsedTime', help='number of seconds since outlet is on')),
               Key('regenheater',
                   Bool('off', 'on', name='state', help='regen heater switch'),
                   Int(name='elapsedTime', help='number of seconds since outlet is on')),
               Key('moxa',
                   Bool('off', 'on', name='state', help='moxa switch'),
                   Int(name='elapsedTime', help='number of seconds since outlet is on')),
               Key('matlamp',
                   Bool('off', 'on', name='state', help='matlamp switch'),
                   Int(name='elapsedTime', help='number of seconds since outlet is on')),
               Key('sac',
                   Bool('off', 'on', name='state', help='sac switch'),
                   Int(name='elapsedTime', help='number of seconds since outlet is on')),
               Key('mono',
                   Bool('off', 'on', name='state', help='mono switch'),
                   Int(name='elapsedTime', help='number of seconds since outlet is on')),
               Key('labsphere',
                   Bool('off', 'on', name='state', help='xenon switch'),
                   Int(name='elapsedTime', help='number of seconds since outlet is on')),

               Key('labsphereFSM',
                   Enum('OFF', 'LOADED', 'ONLINE', name='state'),
                   Enum('IDLE', 'LOADING', 'INITIALISING', 'MOVING', 'WARMING', 'FAILED', name='substate'),
                   help='labsphere state machine'),
               Key('labsphereMode', Enum('operation', 'simulation', help='labsphere mode')),
               Key('photodiode',
                   Float(invalid='nan', help='cd/m^2 at photodiode')),
               Key('flux',
                   Float(invalid='nan', name='median', help='photodiode flux median'),
                   Float(invalid='nan', name='std', help='photodiode flux standard deviation')),
               Key('attenuator',
                   Int(help='attenuator opening value (open=0)'),),
               Key('halogen',
                   Bool('off', 'on', name='state', help='Halogen switch'),
                   Int(name='elapsedTime', help='number of seconds since lamp is on')),

               )
