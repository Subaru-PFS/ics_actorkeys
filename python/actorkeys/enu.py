KeysDictionary('enu', (2, 5),
               Key('text', String(help='text for humans')),
               Key('version', String(help='EUPS/git version')),
               Key('metaFSM',
                   Enum('OFF', 'LOADED', 'ONLINE', name='state'),
                   Enum('IDLE', 'LOADING', 'INITIALISING', 'MOVING', 'EXPOSING', 'FAILED', name='substate'),
                   help='meta state machine'),

               Key('slitFSM',
                   Enum('OFF', 'LOADED', 'ONLINE', name='state',
                        FITS=('W_ENFCAS', 'ENU_FCA_STATE')),
                   Enum('IDLE', 'LOADING', 'INITIALISING', 'MOVING', 'FAILED', name='substate',
                        FITS=('W_ENFCAT', 'ENU_FCA_SUBSTATE')),
                   help='slit state machine'),
               Key('slitMode', Enum('operation', 'simulation',
                                    help='fca operation mode',
                                    FITS=('W_ENFCAM', 'ENU_FCA_MODE'))),
               Key('slit',
                   Float(name='X', help='FCA X coordinate', FITS=('W_ENFCAX', 'ENU_FCA_FOCUS')),
                   Float(name='Y', help='FCA Y coordinate', FITS=('W_ENFCAY', 'ENU_FCA_SHIFT')),
                   Float(name='Z', help='FCA Z coordinate', FITS=('W_ENFCAZ', 'ENU_FCA_DITHER')),
                   Float(name='U', help='FCA U coordinate', FITS=('W_ENFCAU', 'ENU_FCA_ROLL')),
                   Float(name='V', help='FCA V coordinate', FITS=('W_ENFCAV', 'ENU_FCA_PITCH')),
                   Float(name='W', help='FCA W coordinate', FITS=('W_ENFCAW', 'ENU_FCA_YAW')),
                   help='slit current position'),
               Key('slitWork',
                   Float(name='X', help='x_coordinate'),
                   Float(name='Y', help='y_coordinate'),
                   Float(name='Z', help='z_coordinate'),
                   Float(name='U', help='u_coordinate'),
                   Float(name='V', help='v_coordinate'),
                   Float(name='W', help='W_coordinate'), help='slit home coordinate system'),
               Key('slitTool',
                   Float(name='X', help='x_coordinate'),
                   Float(name='Y', help='y_coordinate'),
                   Float(name='Z', help='z_coordinate'),
                   Float(name='U', help='u_coordinate'),
                   Float(name='V', help='v_coordinate'),
                   Float(name='W', help='W_coordinate'), help='slit tool coordinate system'),
               Key('slitInfo', String(help='Hexapod controller status')),
               Key('slitLocation', Enum('home', 'undef', name='location',
                                        help='FCA location', FITS=('W_ENFCAL', 'ENU_FCA_LOCATION'))),
               Key('bshFSM',
                   Enum('OFF', 'LOADED', 'ONLINE', name='state',
                        FITS=('W_ENBSHS', 'ENU_BSH_STATE')),
                   Enum('IDLE', 'LOADING', 'INITIALISING', 'EXPOSING', 'FAILED', name='substate',
                        FITS=('W_ENBSHT', 'ENU_BSH_SUBSTATE')),
                   help='bsh state machine'),
               Key('bshMode', Enum('operation', 'simulation',
                                   help='bsh operation mode',
                                   FITS=('W_ENBSHM', 'ENU_BSH_MODE'))),
               Key('shutters', Enum('close', 'open', 'openred', 'openblue', 'undef', name='position',
                                    help='shutters current position',
                                    FITS=('W_ENSHUT', 'ENU_SHUTTERS_POSITION'))),
               Key('shb',
                   Bool('0', '1', name='open', help='blue shutter open bit'),
                   Bool('0', '1', name='close', help='blue shutter close bit'),
                   Bool('0', '1', name='error', help='blue shutter error bit')),
               Key('shr',
                   Bool('0', '1', name='open', help='blue shutter open bit'),
                   Bool('0', '1', name='close', help='blue shutter close bit'),
                   Bool('0', '1', name='error', help='blue shutter error bit')),

               Key('exptime', Float(help='exposure time in seconds')),
               Key('transientTime', Float(help='shutters transition time in seconds')),
               Key('integratingTime', Float(help='Shutter opening duration')),
               Key('elapsedTime', Float(help='Seconds since shutters opening')),
               Key('dateobs', String(help='absolute exposure start UTC time ISO formatted')),
               Key('bia', Enum('off', 'on', 'undef', name='state',
                               help='bia current state',
                               FITS=('W_ENBIAS', 'ENU_BIA_STATE'))),
               Key('biaConfig',
                   Int(name='period', help='bia illumination period'),
                   Int(name='duty', help='duty cycle')),
               Key('biaStrobe',
                   Bool('off', 'on', name='state', help='strobe mode')),

               Key('rexmFSM',
                   Enum('OFF', 'LOADED', 'ONLINE', name='state',
                        FITS=('W_ENRDAS', 'ENU_RDA_STATE')),
                   Enum('IDLE', 'LOADING', 'INITIALISING', 'MOVING', 'FAILED', name='substate',
                        FITS=('W_ENRDAT', 'ENU_RDA_SUBSTATE')),
                   help='bsh state machine'),
               Key('rexmMode', Enum('operation', 'simulation',
                                    help='rda operation mode',
                                    FITS=('W_ENRDAM', 'ENU_RDA_MODE'))),
               Key('rexm',
                   Enum('low', 'mid', 'undef', name='position',
                        help='rexm current position',
                        FITS=('W_ENRDAP', 'ENU_RDA_POSITION'))),
               Key('rexmInfo',
                   UInt(name='switchA', help='switch A state'),
                   UInt(name='switchB', help='switch B state'),
                   Int(name='speed', help='motor speed ustep/sec'),
                   Int(name='steps', help='number of ustep from origin')),

               Key('tempsFSM',
                   Enum('OFF', 'LOADED', 'ONLINE', name='state'),
                   Enum('IDLE', 'LOADING', 'INITIALISING', 'FAILED', name='substate'),
                   help='temps state machine'),
               Key('tempsMode',  Enum('operation', 'simulation', help='temps mode')),
               Key('temps', Float(invalid='NaN', units='C') * 8, ),

               Key('pduFSM',
                   Enum('OFF', 'LOADED', 'ONLINE', name='state'),
                   Enum('IDLE', 'LOADING', 'INITIALISING', 'FAILED', name='substate'),
                   help='pdu state machine'),
               Key('pduMode',  Enum('operation', 'simulation', help='pdu mode')),

               Key('iisFSM',
                   Enum('OFF', 'LOADED', 'ONLINE', name='state'),
                   Enum('IDLE', 'LOADING', 'INITIALISING', 'FAILED', name='substate'),
                   help='iis state machine'),
               Key('iisMode',  Enum('operation', 'simulation', help='iis mode')),

               )
