# Just for editors, since opscore annoyingly imports everything before
# importing this file
#
#try:
#    KeysDictionary
#except NameError:
#    from opscore.protocols.keys import KeysDictionary, Key
#    from opscore.protocols.types import String, Float, Int, Enum

KeysDictionary('gen2', (4, 8),
               Key("text", String(help="text for humans")),
               Key("version", String(help="Gen2 actor version",
                                     FITS=('W_RVGEN2',
                                           'W_GEN2ACTOR_VERSION'))),
               Key("version_gen2", String(help="Gen2 library version",
                                          FITS=('W_RVG2LB',
                                                'W_GEN2_LIBRARY_VERSION'))),
               Key('version_tron_actorcore', String()),
               Key('version_pfs_utils', String()),
               Key('gen2server',
                   String(name='name', help="Internal name of Gen2 server used by PFS",
                          FITS=("W_G2SERV",
                                "W_GEN2_SERVER_NAME")),
                   String(name='IP', help="IP address of Gen2 server used by PFS",
                          FITS=("W_G2SVIP",
                                "W_GEN2_SERVER_IP"))),
               
               Key("visit", Int(help="Gen2-assigned PFS visit")),
               
               Key("inst_ids",
                   String(name="observatory", help="Observatory",
                          FITS=("OBSERVAT", "")),
                   String(name="telescope", help="Telescope",
                          FITS=("TELESCOP", "")),
                   String(name="instrument", help="Instrument name",
                          FITS=("INSTRUME", ""))),

               Key("program",
                   String(name="proposal", help="Proposal ID",
                          FITS=("PROP-ID", "")),
                   String(name="mode", help="Observation Mode",
                          FITS=("OBS-MOD", "")),
                   String(name="allocation", help="Observation or Standby",
                          FITS=("OBS-ALOC", "")),
                   String(name="observers", help="Observers",
                          FITS=("OBSERVER", ""))),

               Key("object",
                   String(name="name",
                          FITS=("OBJECT", ""),
                          help="Object name"),
                   String(name="ra",
                          FITS=("RA", ""),
                          help="RA of telescope pointing",
                          units='HMS'),
                   String(name="dec",
                          FITS=("DEC", ""),
                          help="DEC of telescope pointing",
                          units='DMS'),
                   String(name="ra2000",
                          FITS=("RA2000", ""),
                          help="RA of telescope pointing",
                          units='HMS'),
                   String(name="dec2000",
                          FITS=("DEC2000", ""),
                          help="DEC of telescope pointing",
                          units='DMS')),

               Key("pointing",
                   String(name="ra",
                          FITS=("RA_CMD", ""),
                          help="RA of nominal telescope pointing",
                          units='HMS'),
                   String(name="dec",
                          FITS=("DEC_CMD", ""),
                          help="DEC of nominal telescope pointing",
                          units='DMS')),

               Key("offsets",
                   Float(name="ra",
                         FITS=("W_RAOFF", ""),
                         help="RA offset",
                         units='arcsec'),
                   Float(name="dec",
                         FITS=("W_DECOFF", ""),
                         help="Dec offset",
                         units='arcsec')),

               Key("telDither",
                   Float(name="ra",
                         FITS=("W_DTHRA", ""),
                         help="Cumulative RA dither offset",
                         units='arcsec'),
                   Float(name="dec",
                         FITS=("W_DTHDEC", ""),
                         help="Cumulative Dec dither offset",
                         units='arcsec'),
                   Float(name="pa",
                         FITS=("W_DTHPA", ""),
                         help="Cumulative posAngle dither offset",
                         units='arcsec')),

               Key("telGuide",
                   Float(name="ra",
                         FITS=("W_AGRA", ""),
                         help="Cumulative RA guide offset",
                         units='arcsec'),
                   Float(name="dec",
                         FITS=("W_AGDEC", ""),
                         help="Cumulative Dec guide offset",
                         units='arcsec'),
                   Float(name="insrot",
                         FITS=("W_AGINR", ""),
                         help="Cumulative rotator guide offset",
                         units='arcsec')),

               Key("conditions",
                   String(name="weather",
                          FITS=("WEATHER", ""),
                          help="Weather conditions, per observer"),
                   Float(name="seeing",
                         FITS=("SEEING", ""),
                         help="FWHM of star at telescope focus",
                         units='arcsec'),
                   Float(name="transparency",
                         FITS=("TRANSP", ""),
                         help="Sky transparency",
                         units='frac')),

               Key("coordinate_system_ids",
                   String(name="radesys", help="The equatorial coordinate system",
                          FITS=("RADESYS", "")),
                   Float(name="pole", units='deg', help="North Pole of the coordinate system",
                         FITS=("LONPOLE", "")),
                   Float(name="equinox", units='year', help="Standard FK5",
                         FITS=("EQUINOX", ""))),


               Key("tel_axes",
                   Float(name='az', units='deg', help="Azimuth position",
                         FITS=('AZIMUTH', '')),
                   Float(name='alt', units='deg', help="Altitude position",
                         FITS=('ALTITUDE', '')),
                   Float(name="zd", units="deg", help="Zenith Distance",
                         FITS=("ZD", "")),
                   Float("airmass", help="Typical airmass during exposure",
                         FITS=("AIRMASS", ""))),
               Key("tel_rot",
                   Float(name='posAngle', units='deg', help="Inst pos angle at flange",
                         FITS=('INST-PA', '')),
                   Float(name='instrot', units='deg', help="Inst rotation angle",
                         FITS=('INSROT', ''))),
               Key("tel_focus",
                   String(name='telpos', help="Focus where a beam is reachable",
                          FITS=('TELFOCUS', '')),
                   String(name="platform", help="Focus where instrument is attached.",
                          FITS=("FOC-POS", "")),
                   Float(name='val', units='mm', help="Focus encoder value",
                         FITS=('FOC-VAL', ''))),
               Key("tel_adc",
                   String(name='name', help="ADC name",
                          FITS=('ADC-TYPE', '')),
                   Float(name='angle', units='mm', help="ADC pos angle",
                         FITS=('ADC-STR', ''))),

               Key("dome_env",
                   Float(name='humidity', units='%', help="Dome humidity",
                         FITS=('DOM-HUM', '')),
                   Float(name='pressure', units='hPa', help="Dome pressure",
                         FITS=('DOM-PRS', '')),
                   Float(name='temperature', units='K', help="Dome temperature",
                         FITS=('DOM-TMP', '')),
                   Float(name='wind', units='m/s', help="Dome wind speed",
                         FITS=('DOM-WND', ''))),
               Key("outside_env",
                   Float(name='humidity', units='%', help="Outside humidity",
                         FITS=('OUT-HUM', '')),
                   Float(name='pressure', units='hPa', help="Outside pressure",
                         FITS=('OUT-PRS', '')),
                   Float(name='temperature', units='K', help="Outside temperature",
                         FITS=('OUT-TMP', '')),
                   Float(name='wind', units='m/s', help="Outside wind speed",
                         FITS=('OUT-WND', ''))),
               
               Key("m2",
                   String(name="type",
                          help="M2 type"),
                   Float(name="xpos",
                         FITS=("M2-POS1", ""),
                         help="M2 X position",
                         units='mm'),
                   Float(name="ypos",
                         FITS=("M2-POS2", ""),
                         help="M2 Y position",
                         units='mm'),
                   Float(name="zpos",
                         FITS=("M2-POS3", ""),
                         help="M2 Z position",
                         units='mm')),

               Key("m2rot",
                   Float(name="xang",
                         FITS=("M2-ANG1", ""),
                         help="M2 X angle",
                         units='deg'),
                   Float(name="yang",
                         FITS=("M2-ANG2", ""),
                         help="M2 Y angle",
                         units='deg'),
                   Float(name="zang",
                         FITS=("M2-ANG3", ""),
                         help="M2 Z angle",
                         units='deg')),

               Key("pfuOffset",
                   Float(name="xoff",
                         FITS=("W_M2OFF1", "W_GEN2_M2_XOFFSET"),
                         help="M2 X offset",
                         units='mm'),
                   Float(name="yoff",
                         FITS=("W_M2OFF2", "W_GEN2_M2_YOFFSET"),
                         help="M2 Y offset",
                         units='mm'),
                   Float(name="zoff",
                         FITS=("W_M2OFF3", "W_GEN2_M2_ZOFFSET"),
                         help="M2 Z offset",
                         units='mm')),
               
               Key("frame_ids",
                   String(name="imageId", help="Image ID"),
                   String(name="expId", help="Exposure/visit ID")),

               Key("autoguider",
                   String(name="state",
                          FITS=("AUTOGUID", ""),
                          help="State of autoguider")),
               
               Key("header", String(help="Gen2-supplied FITS header")),

               Key("moon",
                   Float(name="elevation",
                         FITS=("MOON-EL", ""),
                         help="Moon elevation at exposure start",
                         units='deg'),
                   Float(name="separation",
                         FITS=("MOON-SEP", ""),
                         help="Moon separation at exposure start",
                         units='deg'),
                   Float(name="illumination",
                         FITS=("MOON-ILL", ""),
                         help="Moon elevation at exposure start")),

               Key("statusUpdate",
                   Int(name="visit", help='assocated visit'),
                   Int(name="sequenceNum", help='status sequence number within visit'),
                   String(name="caller", help='who requested the status update')),

               Key("obsMethod",
                   String(name="method",
                          FITS=("OBS-MTHD", ""),
                          help="Observing method (classical vs. queue)")),
               Key("domeShutter",
                   Enum("open", "closed", "unknown",
                        name="state", help="position of the dome shutters",
                        FITS=("W_TSHUTR", "W_GEN2_DOME_SHUTTER_POS"))),
               Key("domeLights",
                   Int(name="mask", help="which dome lamps are on",
                       FITS=("W_TDLGHT", "W_GEN2_DOME_LIGHT_MASK"))),
               Key("topScreenPos",
                   Float(name="front", help="front edge of FF screen",
                         units='m',
                         FITS=("W_TFFSFP", "W_GEN2_FLATFIELD_SCREEN_FRONT")),
                   Float(name="rear", help="rear edge of FF screen",
                         units='m',
                         FITS=("W_TFFSRP", "W_GEN2_FLATFIELD_SCREEN_REAR")),
                   String(name="position", help="name of known position",
                          FITS=("W_TFFPOS", "W_GEN2_FLATFIELD_SCREEN_POSITION"))),
               Key("ringLampsStatus",
                   Int(name="lamp1", help="status of ring lamp #1",
                       FITS=("W_TFF1ST", "W_GEN2_RING_LAMP1_STATUS")),
                   Int(name="lamp2", help="status of ring lamp #2",
                       FITS=("W_TFF2ST", "W_GEN2_RING_LAMP2_STATUS")),
                   Int(name="lamp3", help="status of ring lamp #3",
                       FITS=("W_TFF3ST", "W_GEN2_RING_LAMP3_STATUS")),
                   Int(name="lamp4", help="status of ring lamp #4",
                       FITS=("W_TFF4ST", "W_GEN2_RING_LAMP4_STATUS"))),
               Key("ringLampsCmd",
                   Float(name="lamp1", help="Command to ring lamp #1",
                         units="V",
                         FITS=("W_TFF1VC", "W_GEN2_RING_LAMP1_CMD_V")),
                   Float(name="lamp2", help="Command to ring lamp #2",
                         units="V",
                         FITS=("W_TFF2VC", "W_GEN2_RING_LAMP2_CMD_V")),
                   Float(name="lamp3", help="Command to ring lamp #3",
                         units="V",
                         FITS=("W_TFF3VC", "W_GEN2_RING_LAMP3_CMD_V")),
                   Float(name="lamp4", help="Command to ring lamp #4",
                         units="V",
                         FITS=("W_TFF4VC", "W_GEN2_RING_LAMP4_CMD_V"))),
               Key("ringLamps",
                   Float(name="lamp1", help="Measured ring lamp #1",
                         units="V",
                         FITS=("W_TFF1VV", "W_GEN2_RING_LAMP1_MEAS_V")),
                   Float(name="lamp2", help="Measured ring lamp #2",
                         units="V",
                         FITS=("W_TFF2VV", "W_GEN2_RING_LAMP2_MEAS_V")),
                   Float(name="lamp3", help="Measured ring lamp #3",
                         units="V",
                         FITS=("W_TFF3VV", "W_GEN2_RING_LAMP3_MEAS_V")),
                   Float(name="lamp4", help="Measured ring lamp #4",
                         units="V",
                         FITS=("W_TFF4VV", "W_GEN2_RING_LAMP4_MEAS_V"))),
)
