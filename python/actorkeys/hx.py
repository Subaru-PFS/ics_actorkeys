KeysDictionary("hx", (1, 0),
               Key("controllers", String(help='controllers list') * (1, 2)),
               Key("text", String(), help='Stuff for humans'),
               Key('version', String(help="HX actor version",
                                     FITS=("W_RVHX",
                                           "W_HXACTOR_VERSION"))),
               Key('version_tron_actorcore', String(help="tron_actorcore version",
                                                    FITS=("W_RVACOR",
                                                          "W_ACTORCORE_VERSION"))),
               Key('version_ics_actorkeys', String(help="ics_actorkeys version",
                                                   FITS=("W_RVAKEY",
                                                         "W_ACTORKEYS_VERSION"))),
               Key('version_hxhal', String(help="hxhal version",
                                           FITS=("W_RVHXHL",
                                                 "W_HXHAL_VERSION"))),
               Key('serial_SAM', String(help="SAM serial number",
                                        FITS=("W_SRSAM",
                                              "W_SAM_SERIAL"))),
               Key('serial_H4', String(help="H4RG serial number",
                                       FITS=("W_SRH4",
                                             "W_H4RG_SERIAL"))),
               Key("asicConfig",
                   String(name="ASIC_image",
                          help="name of the loaded ASIC firmware image",
                          FITS=("W_H4FIRM",
                                "W_ASIC_FIRMWARE_NAME")),
                   String(name="ASIC_config",
                          help="name of the loaded ASIC configuration",
                          FITS=("W_H4CONF",
                                "W_ASIC_CONFIGURATION_NAME"))),

               # ramp=1,1,1,3,0
               Key("ramp",
                   Int("nramp", help="number of ramps requested",
                       FITS=("W_H4NRMP",
                             "W_H4_NRAMPS")),
                   Int("ngroup", help="number of groups requested",
                       FITS=("W_H4NGRP",
                             "W_H4_NGROUPS")),
                   Int("nreset", help="number of resets requested",
                       FITS=("W_H4NRST",
                             "W_H4_NRESETS")),
                   Int("nramp", help="number of reads requested",
                       FITS=("W_H4NRED",
                             "W_H4_NREADS")),
                   Int("ndrop", help="number of drops requested",
                       FITS=("W_H4NDRP",
                             "W_H4_NDROPS"))),

               # hxread=/data/pfsx/2020-02-13/PFJB00469913.fits,1,1,0
               Key("hxread",
                   String(name="filename", help="path to ramp file"),
                   Int("ramp", help="the current ramp number",
                       FITS=("W_H4RAMP",
                             "W_H4_RAMP_NUMBER")),
                   Int("group", help="the current group number within the ramp",
                       FITS=("W_H4GRUP",
                             "W_H4_GROUP_NUMBER")),
                   Int("ramp", help="the current read within the ramp+group",
                       FITS=("W_H4READ",
                             "W_H4_READ_NUMBER"))),
                   
               Key("filepath",
                   String(name="rootDirectory"),
                   String(name="nightDirectory"),
                   String(name="filename"),
                   help="all the parts making up the image file path. Suitable for os.path.join()"),

               Key("exposureState",
                   Enum('idle','resetting','reading','aborted','unknown'),
                   help="the state of the readout system"),

)
