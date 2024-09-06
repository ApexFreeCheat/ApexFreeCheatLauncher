class config:
    def __init__(self, config_name="ApexFreeCheat.ini"):
        self.config_name = config_name
        self.config_dict = {
            'FEATURE_AIMBOT_ON': 'YES',
            'FEATURE_SENSE_ON': 'YES',
            'FEATURE_ITEM_GLOW_ON': 'YES',
            'FEATURE_NORECOIL_ON': 'YES',
            'FEATURE_TRIGGERBOT_ON': 'YES',
            'FEATURE_QUICKTURN_ON': 'YES',
            'FEATURE_QUICKTURN_BUTTON': 'XK_F',
            'FEATURE_SPECTATOR_ON': 'YES',
            'FEATURE_SKINCHANGER_ON': 'YES',
            'FEATURE_PRINT_LEVELS_ON': 'YES',
            'FEATURE_PRINT_LEVELS_BUTTON': 'XK_P',
            'FEATURE_SUPER_GLIDE_ON': 'YES',
            'FEATURE_MAP_RADAR_ON': 'YES',
            'FEATURE_MAP_RADAR_BUTTON': 'XK_M',
            'NORECOIL_PITCH_REDUCTION': '19',
            'NORECOIL_YAW_REDUCTION': '20',
            'TRIGGERBOT_ZOOMED_RANGE': '180',
            'TRIGGERBOT_HIPFIRE_RANGE': '25',
            'TRIGGERBOT_PAUSE_BUTTON': 'XK_Z',
            'SENSE_MAXRANGE': '250',
            'AIMBOT_ACTIVATED_BY_ATTACK': 'YES',
            'AIMBOT_ACTIVATED_BY_ADS': 'YES',
            'AIMBOT_ACTIVATED_BY_KEY': 'YES',
            'AIMBOT_ACTIVATION_KEY': 'XK_X',
            'AIMBOT_SMOOTH': '11.314159',
            'AIMBOT_SPEED': '81.3141',
            'AIMBOT_SMOOTH_EXTRA_BY_DISTANCE': '1500',
            'AIMBOT_FOV': '5.3141',
            'AIMBOT_PREDICT_BULLETDROP': 'YES',
            'AIMBOT_PREDICT_MOVEMENT': 'YES',
            'AIMBOT_ALLOW_TARGET_SWITCH': 'NO',
            'AIMBOT_MAX_DISTANCE': '69',
            'AIMBOT_MIN_DISTANCE': '5'
        }

    def load(self):
        with open(self.config_name, "r") as f:
            for line in f:
                line_split = line.split()
                if not line_split:
                    continue
                if line_split[0][0] == '#':
                    continue
                self.config_dict[line_split[0]] = line_split[1]
    
    def save(self):
        with open(self.config_name, "w") as f:
            for key, value in self.config_dict.items():
                f.write(key + " " + value + "\n")

    def __getitem__(self, index):
        return self.config_dict[index]

    def __repr__(self):
        return repr(self.config_dict)