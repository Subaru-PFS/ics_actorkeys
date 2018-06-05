KeysDictionary('mcs', (1, 4),
               Key("text", String(help="text for humans")),
               Key("version", String(help="EUPS/git version")),
               Key("cameraName", String()),
               Key("readNoise", Float(help="nominal readnoise for camera", units="e-")),
               Key("ccdTemp", Float(help="measured temperature at CCD mount", units="degC",
                                    FITS=('W_MCCCDT', 'MCP_CCD_TEMP')),
               Key("centroidsChunk", String(help="base64 encoded centroids")),
               Key('exposureState',
                   Enum('IDLE','FLUSHING','INTEGRATING','READING','ABORTED','DONE', name="state"),
                   help='The current state of the exposure'),
               Key('filename', String(help='name of just finished exposure')),
)
