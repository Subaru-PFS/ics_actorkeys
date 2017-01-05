KeysDictionary("breva", (1, 2),

               Key("REP_OBJ", Float(invalid="NaN", units="K")*6,
                   help="repere objet par rapport nacelle "),
               Key("REP_UTIL", Float(invalid="NaN", units="K")*6,
                   help="repere utilisateur par rapport a machine"),              
               Key("position",
                   Float(name='X', help='x_coordinate'),
                   Float(name='Y', help='y_coordinate'),
                   Float(name='Z', help='z_coordinate'),
                   Float(name='U', help='u_coordinate'),
                   Float(name='V', help='v_coordinate'),
                   Float(name='W', help='w_coordinate'), help='breva current position'),

               )


