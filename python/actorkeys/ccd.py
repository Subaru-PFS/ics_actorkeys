KeysDictionary('ccd', (2,4),
               Key("controllers", String(help='controllers list') * (1, None)),
               Key("Text", String(), help='Stuff for humans'),
               Key('version', String(help="CCD actor version",
                                     FITS=("W_RVCCD",
                                           "W_CCDACTOR_VERSION"))),
               Key('version_tron_actorcore', String(help="tron_actorcore version",
                                                    FITS=("W_RVACOR",
                                                          "W_ACTORCORE_VERSION"))),
               Key('version_ics_xcu_fpga', String(help="ics_xcu_fpga version",
                                                    FITS=("W_RVXFPG",
                                                          "W_XCU_FPGA_VERSION"))),
               Key('version_ics_actorkeys', String(help="ics_actorkeys version",
                                                   FITS=("W_RVAKEY",
                                                         "W_ACTORKEYS_VERSION"))),
               Key('version_fpga', String(help="FPGA firmware version",
                                          FITS=("W_RVFPGA",
                                                "W_FPGA_VERSION"))),
               Key('version_fee', String(help="FEE firmware version",
                                         FITS=("W_RVFEE",
                                               "W_FEE_VERSION"))),
               Key("ccdTemps",
                   Float(invalid="NaN", units="K", name='preamp', help='preamp temperature',
                         FITS=('W_CPAMPT', 'CCD_PREAMP_TEMP')), 
                   Float(invalid="NaN", units="K", name='ccd0', help='CCD0 temperature',
                         FITS=('W_CCD0T', 'CCD0_TEMP')), 
                   Float(invalid="NaN", units="K", name='ccd1', help='CCD1 temperature',
                         FITS=('W_CCD1T', 'CCD1_TEMP')), 
                   help='detector assembly temperatures'),

               Key('beamConfigDate'
                   Int(name='visit', help='this visit'),
                   Float(name='mjd', help='the date of the last move affecting the beam')),
               
               Key("readRows",
                   Int(name='rowsDone'),
                   Int(name='rowsTotal'),
                   help="the number of rows read out and the image height."),

               Key("exposureState",
                   Enum('idle','wiping','integrating','reading','aborted','unknown'),
                   help="the state of the readout system"),

               Key("filepath",
                   String(name="rootDirectory"),
                   String(name="nightDirectory"),
                   String(name="filename"),
                   help="all the parts making up the image file path. Suitable for os.path.join()"),

               Key("spsFileIds",
                   String(name="cam", help="the camera name (e.g. b3)"),
                   String(name="pfsDay", help="the date used for the night data (e.g. 2020-05-14)"),
                   Int(name="visit", help="the PFS visit"),
                   Int(name="spectrograph", help="the spectrograph module number"),
                   Int(name="arm", help="the arm number")),

               Key("geometry",
                   Int(name="namps", help="number of CCD amps",
                       FITS=("W_CNAMPS", "CCD_NAMPS")),
                   Int(name="rows", help="total number of rows in image",
                       FITS=("W_CIMROW", "CCD_ROWS")),
                   Int(name="amp_cols", help="total number of columns in amp",
                       FITS=("W_CAMPRW", "CCD_AMP_ROWS")),
                   Int(name="leadin_rows", help="(dropped) leadin rows",
                       FITS=("W_CRWLDN", "CCD_LEADIN_ROWS")),
                   Int(name="active_rows", help="active rows",
                       FITS=("W_CRWACT", "CCD_ACTIVE_ROWS")),
                   Int(name="overscan_rows", help="overscan rows",
                       FITS=("W_CRWOVR", "CCD_OVERSCAN_ROWS")),
                   Int(name="leadin_cols", help="(dropped) leadin columns",
                       FITS=("W_CCLLDN", "CCD_LEADIN_COLS")),
                   Int(name="active_cols", help="active cols",
                       FITS=("W_CCLACT", "CCD_ACTIVE_COLS")),
                   Int(name="overscan_cols", help="overscan cols",
                       FITS=("W_CCLOVR", "CCD_OVERSCAN_COLS"))),

               Key("serials",
                   String(name="FEE", help="FEE serial ID",
                          FITS=("W_SRFEE", "CCD_FEE_SERIAL")),
                   String(name="ADC", help="ADC serial ID",
                          FITS=("W_SRADC", "CCD_ADC_SERIAL")),
                   String(name="preamp", help="Preamp serial ID",
                          FITS=("W_SRPAMP", "CCD_PREAMP_SERIAL")),
                   String(name="CCD0", help="CCD0 serial ID",
                          FITS=("W_SRCCD0", "CCD0_SERIAL")),
                   String(name="CCD1", help="CCD1 serial ID",
                          FITS=("W_SRCCD1", "CCD1_SERIAL")),
                   help="DAQ component serial numbers"),

               Key("feeVoltages",
                   Float(invalid="NaN", units="V", name='v3V3M', help='3.3V at FEE',
                         FITS=('W_F3V3M', 'FEE_3.3VM')), 
                   Float(invalid="NaN", units="V", name='v3V3', help='3.3V at FEE',
                         FITS=('W_F3V3', 'FEE_3.3V')), 
                   Float(invalid="NaN", units="V", name='v5VP', help='+5V at FEE',
                         FITS=('W_F5VP', 'FEE_+5V')), 
                   Float(invalid="NaN", units="V", name='v5VM', help='-5V at FEE',
                         FITS=('W_F5VM', 'FEE_-5V')), 
                   Float(invalid="NaN", units="V", name='v5VPpa', help='+5V for preamp at FEE',
                         FITS=('W_F5VPPA', 'FEE_+5V_PREAMP')), 
                   Float(invalid="NaN", units="V", name='v5VMpa', help='-5V for preamp at FEE',
                         FITS=('W_F5VMPA', 'FEE_-5V_PREAMP')), 
                   Float(invalid="NaN", units="V", name='v12VP', help='+12V at FEE',
                         FITS=('W_F12VP', 'FEE_+12V')), 
                   Float(invalid="NaN", units="V", name='v12VM', help='-12V at FEE',
                         FITS=('W_F12VM', 'FEE_-12V')), 
                   Float(invalid="NaN", units="V", name='v23VP', help='+24V at FEE',
                         FITS=('W_F24VP', 'FEE_+24V')), 
                   Float(invalid="NaN", units="V", name='v54VP', help='+54V at FEE',
                         FITS=('W_F54VP', 'FEE_+54V')), 
                   help='voltages at the FEE'),

               Key("integrationVoltages0",
                   Float(invalid="NaN", units="V", name='OG', help='ccd0 integration OG voltage, measured',
                         FITS=('W_FI0OG', 'FEE_CCD0_INTEGRATION_OG')), 
                   Float(invalid="NaN", units="V", name='RD', help='ccd0 integration RD voltage, measured',
                         FITS=('W_FI0RD', 'FEE_CCD0_INTEGRATION_RD')), 
                   Float(invalid="NaN", units="V", name='OD', help='ccd0 integration OD voltage, measured',
                         FITS=('W_FI0OD', 'FEE_CCD0_INTEGRATION_OD')), 
                   Float(invalid="NaN", units="V", name='BB', help='ccd0 integration BB voltage, measured',
                         FITS=('W_FI0BB', 'FEE_CCD_0BB'))), 

               Key("integrationVoltages1",
                   Float(invalid="NaN", units="V", name='OG', help='ccd1 integration OG voltage, measured',
                         FITS=('W_FI1OG', 'FEE_CCD1_INTEGRATION_OG')), 
                   Float(invalid="NaN", units="V", name='RD', help='ccd1 integration RD voltage, measured',
                         FITS=('W_FI1RD', 'FEE_CCD1_INTEGRATION_RD')), 
                   Float(invalid="NaN", units="V", name='OD', help='ccd1 integration OD voltage, measured',
                         FITS=('W_FI1OD', 'FEE_CCD1_INTEGRATION_OD')), 
                   Float(invalid="NaN", units="V", name='BB', help='ccd1 integration BB voltage, measured',
                         FITS=('W_FI1BB', 'FEE_CCD_1BB'))), 

               Key("readoutVoltages0",
                   Float(invalid="NaN", units="V", name='P_on', help='ccd0 Parallel clock on, measured',
                         FITS=('W_FR0PON', 'FEE_CCD0_READ_P_ON')), 
                   Float(invalid="NaN", units="V", name='P_off', help='ccd0 Parallel clock off, measured',
                         FITS=('W_FR0POF', 'FEE_CCD0_READ_P_OFF')), 

                   Float(invalid="NaN", units="V", name='DG_on', help='ccd0 Drain Gate clock on, measured',
                         FITS=('W_FR0DGN', 'FEE_CCD0_READ_DG_ON')), 
                   Float(invalid="NaN", units="V", name='DG_off', help='ccd0 Drain Gate clock off, measured',
                         FITS=('W_FR0DGF', 'FEE_CCD0_READ_DG_OFF')), 

                   Float(invalid="NaN", units="V", name='S_on', help='ccd0 Serial clock on, measured',
                         FITS=('W_FR0SON', 'FEE_CCD0_READ_SERIAL_ON')), 
                   Float(invalid="NaN", units="V", name='S_off', help='ccd0 Serial clock off, measured',
                         FITS=('W_FR0SOF', 'FEE_CCD0_READ_SERIAL_OFF')), 

                   Float(invalid="NaN", units="V", name='SW_on', help='ccd0 Summing Well clock on, measured',
                         FITS=('W_FR0SWN', 'FEE_CCD0_READ_SUMMING_WELL_ON')), 
                   Float(invalid="NaN", units="V", name='SW_off', help='ccd0 Summing Well clock off, measured',
                         FITS=('W_FR0SWF', 'FEE_CCD0_READ_SUMMING_WELL_OFF')), 
                
                   Float(invalid="NaN", units="V", name='RG_on', help='ccd0 Reset Gate clock on, measured',
                         FITS=('W_FR0RGN', 'FEE_CCD0_READ_RESET_GATE_ON')), 
                   Float(invalid="NaN", units="V", name='RG_off', help='ccd0 Reset Gate clock off, measured',
                         FITS=('W_FR0RGF', 'FEE_CCD0_READ_RESET_GATE_OFF')), 
                
                   Float(invalid="NaN", units="V", name='OG', help='ccd0 readout OG voltage, measured',
                         FITS=('W_FR0OG', 'FEE_CCD0_READ_OG')), 
                   Float(invalid="NaN", units="V", name='RD', help='ccd0 readout RD voltage, measured',
                         FITS=('W_FR0RD', 'FEE_CCD0_READ_RD')), 
                   Float(invalid="NaN", units="V", name='OD', help='ccd0 readout OD voltage, measured',
                         FITS=('W_FR0OD', 'FEE_CCD0_READ_OD')), 
                   Float(invalid="NaN", units="V", name='BB', help='ccd0 readout BB voltage, measured',
                         FITS=('W_FR0BB', 'FEE_CCD0_READ_BB'))), 

               Key("readoutVoltages1",
                   Float(invalid="NaN", units="V", name='P_on', help='ccd1 Parallel clock on, measured',
                         FITS=('W_FR1PON', 'FEE_CCD1_READ_P_ON')), 
                   Float(invalid="NaN", units="V", name='P_off', help='ccd1 Parallel clock off, measured',
                         FITS=('W_FR1POF', 'FEE_CCD1_READ_P_OFF')), 

                   Float(invalid="NaN", units="V", name='DG_on', help='ccd1 Drain Gate clock on, measured',
                         FITS=('W_FR1DGN', 'FEE_CCD1_READ_DG_ON')), 
                   Float(invalid="NaN", units="V", name='DG_off', help='ccd1 Drain Gate clock off, measured',
                         FITS=('W_FR1DGF', 'FEE_CCD1_READ_DG_OFF')), 

                   Float(invalid="NaN", units="V", name='S_on', help='ccd1 Serial clock on, measured',
                         FITS=('W_FR1SON', 'FEE_CCD1_READ_SERIAL_ON')), 
                   Float(invalid="NaN", units="V", name='S_off', help='ccd1 Serial clock off, measured',
                         FITS=('W_FR1SOF', 'FEE_CCD1_READ_SERIAL_OFF')), 

                   Float(invalid="NaN", units="V", name='SW_on', help='ccd1 Summing Well clock on, measured',
                         FITS=('W_FR1SWN', 'FEE_CCD1_READ_SUMMING_WELL_ON')), 
                   Float(invalid="NaN", units="V", name='SW_off', help='ccd1 Summing Well clock off, measured',
                         FITS=('W_FR1SWF', 'FEE_CCD1_READ_SUMMING_WELL_OFF')), 
                
                   Float(invalid="NaN", units="V", name='RG_on', help='ccd1 Reset Gate clock on, measured',
                         FITS=('W_FR1RGN', 'FEE_CCD1_READ_RESET_GATE_ON')), 
                   Float(invalid="NaN", units="V", name='RG_off', help='ccd1 Reset Gate clock off, measured',
                         FITS=('W_FR1RGF', 'FEE_CCD1_READ_RESET_GATE_OFF')), 
                
                   Float(invalid="NaN", units="V", name='OG', help='ccd1 readout OG voltage, measured',
                         FITS=('W_FR1OG', 'FEE_CCD1_READ_OG')), 
                   Float(invalid="NaN", units="V", name='RD', help='ccd1 readout RD voltage, measured',
                         FITS=('W_FR1RD', 'FEE_CCD1_READ_RD')), 
                   Float(invalid="NaN", units="V", name='OD', help='ccd1 readout OD voltage, measured',
                         FITS=('W_FR1OD', 'FEE_CCD1_READ_OD')), 
                   Float(invalid="NaN", units="V", name='BB', help='ccd1 readout BB voltage, measured',
                         FITS=('W_FR1BB', 'FEE_CCD1_READ_BB'))), 

               Key("offsets_master",
                   Float(invalid="NaN", units="mV", name='amp0_0', help='CCD0 amp0 master offset',
                         FITS=('W_COFM00', 'ADC_MASTER_OFFSET_AMP00')), 
                   Float(invalid="NaN", units="mV", name='amp0_1', help='CCD0 amp1 master offset',
                         FITS=('W_COFM01', 'ADC_MASTER_OFFSET_AMP01')), 
                   Float(invalid="NaN", units="mV", name='amp0_2', help='CCD0 amp2 master offset',
                         FITS=('W_COFM02', 'ADC_MASTER_OFFSET_AMP02')), 
                   Float(invalid="NaN", units="mV", name='amp0_3', help='CCD0 amp3 master offset',
                         FITS=('W_COFM03', 'ADC_MASTER_OFFSET_AMP03')), 
                   Float(invalid="NaN", units="mV", name='amp1_0', help='CCD1 amp0 master offset',
                         FITS=('W_COFM10', 'ADC_MASTER_OFFSET_AMP10')), 
                   Float(invalid="NaN", units="mV", name='amp1_1', help='CCD1 amp1 master offset',
                         FITS=('W_COFM11', 'ADC_MASTER_OFFSET_AMP11')), 
                   Float(invalid="NaN", units="mV", name='amp1_2', help='CCD1 amp2 master offset',
                         FITS=('W_COFM12', 'ADC_MASTER_OFFSET_AMP12')), 
                   Float(invalid="NaN", units="mV", name='amp1_3', help='CCD1 amp3 master offset',
                         FITS=('W_COFM13', 'ADC_MASTER_OFFSET_AMP13'))), 
               Key("offsets_reference",
                   Float(invalid="NaN", units="mV", name='amp0_0', help='CCD0 amp0 reference offset',
                         FITS=('W_COFR00', 'ADC_REFERENCE_OFFSET_AMP00')), 
                   Float(invalid="NaN", units="mV", name='amp0_1', help='CCD0 amp1 reference offset',
                         FITS=('W_COFR01', 'ADC_REFERENCE_OFFSET_AMP01')), 
                   Float(invalid="NaN", units="mV", name='amp0_2', help='CCD0 amp2 reference offset',
                         FITS=('W_COFR02', 'ADC_REFERENCE_OFFSET_AMP02')), 
                   Float(invalid="NaN", units="mV", name='amp0_3', help='CCD0 amp3 reference offset',
                         FITS=('W_COFR03', 'ADC_REFERENCE_OFFSET_AMP03')), 
                   Float(invalid="NaN", units="mV", name='amp1_0', help='CCD1 amp0 reference offset',
                         FITS=('W_COFR10', 'ADC_REFERENCE_OFFSET_AMP10')), 
                   Float(invalid="NaN", units="mV", name='amp1_1', help='CCD1 amp1 reference offset',
                         FITS=('W_COFR11', 'ADC_REFERENCE_OFFSET_AMP11')), 
                   Float(invalid="NaN", units="mV", name='amp1_2', help='CCD1 amp2 reference offset',
                         FITS=('W_COFR12', 'ADC_REFERENCE_OFFSET_AMP12')), 
                   Float(invalid="NaN", units="mV", name='amp1_3', help='CCD1 amp3 reference offset',
                         FITS=('W_COFR13', 'ADC_REFERENCE_OFFSET_AMP13'))), 
)
               
