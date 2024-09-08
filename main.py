import flet as ft
import subprocess
import threading
import time
import webbrowser
from config import config
import os

cheat_process = None

def main(page):
    page.title = "Launcher"  # 设置窗口标题
    page.window.width = 1280
    page.window.height = 720
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window.maximizable = False  # 禁止窗口最大化
    page.theme_mode = ft.ThemeMode.LIGHT  # 设置窗口颜色为明亮模式
    config_set = config()

    def reg_clicked(e):
        webbrowser.open("https://apex.hhhhhi.com")

    def install_clicked(e):
        process = subprocess.Popen(
            ['DriverLoader.exe'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='gbk'
        )

        stdout, stderr = process.communicate()
        cmd_info.value = stdout + stderr
        page.update()

    def start_clicked(e):
        global cheat_process
        cheat_process = subprocess.Popen(
            ['ApexFreeCheat.exe', j8_input.value],
            #['ping', 'localhost', '-t'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='gbk'
        )
        threading.Thread(target=update_output).start()
        start_button.disabled = True
        page.update()

    def kill_clicked(e):
        cheat_process.kill()

    def log_clicked(e):
        cmd_info.visible = True
        config_pan.visible = False
        page.update()

    def config_clicked(e):
        cmd_info.visible = False
        config_pan.visible = True
        page.update()

    def load_clicked(e):
        config_set.load()
        aimbot_on.value = config_set['FEATURE_AIMBOT_ON']
        sense_on.value = config_set['FEATURE_SENSE_ON']
        item_glow_on.value = config_set['FEATURE_ITEM_GLOW_ON']
        norecoil_on.value = config_set['FEATURE_NORECOIL_ON']
        triggerbot_on.value = config_set['FEATURE_TRIGGERBOT_ON']
        quickturn_on.value = config_set['FEATURE_QUICKTURN_ON']
        quickturn_button.value = config_set['FEATURE_QUICKTURN_BUTTON']
        spectator_on.value = config_set['FEATURE_SPECTATOR_ON']
        skinchanger_on.value = config_set['FEATURE_SKINCHANGER_ON']
        print_levels.value = config_set['FEATURE_PRINT_LEVELS_ON']
        print_levels_button.value = config_set['FEATURE_PRINT_LEVELS_BUTTON']
        super_glide.value = config_set['FEATURE_SUPER_GLIDE_ON']
        map_radar.value = config_set['FEATURE_MAP_RADAR_ON']
        map_radar_button.value = config_set['FEATURE_MAP_RADAR_BUTTON']
        norecoil_pitch_reduction.value = config_set['NORECOIL_PITCH_REDUCTION']
        norecoil_yaw_reduction.value = config_set['NORECOIL_YAW_REDUCTION']
        triggerbot_zoomed_range.value = config_set['TRIGGERBOT_ZOOMED_RANGE']
        triggerbot_hipfire_range.value = config_set['TRIGGERBOT_HIPFIRE_RANGE']
        triggerbot_pause_button.value = config_set['TRIGGERBOT_PAUSE_BUTTON']
        sense_maxrange.value = config_set['SENSE_MAXRANGE']
        aimbot_activated_by_attack.value = config_set['AIMBOT_ACTIVATED_BY_ATTACK']
        aimbot_activated_by_ads.value = config_set['AIMBOT_ACTIVATED_BY_ADS']
        aimbot_activated_by_key.value = config_set['AIMBOT_ACTIVATED_BY_KEY']
        aimbot_activation_key.value = config_set['AIMBOT_ACTIVATION_KEY']
        aimbot_smooth.value = config_set['AIMBOT_SMOOTH']
        aimbot_smooth_extra_by_distance.value = config_set['AIMBOT_SMOOTH_EXTRA_BY_DISTANCE']
        aimbot_fov.value = config_set['AIMBOT_FOV']
        aimbot_predict_bulletdrop.value = config_set['AIMBOT_PREDICT_BULLETDROP']
        aimbot_predict_movement.value = config_set['AIMBOT_PREDICT_MOVEMENT']
        aimbot_allow_target_switch.value = config_set['AIMBOT_ALLOW_TARGET_SWITCH']
        aimbot_max_distance.value = config_set['AIMBOT_MAX_DISTANCE']
        aimbot_min_distance.value = config_set['AIMBOT_MIN_DISTANCE']
        page.update()

    def save_clicked(e):
        config_set['FEATURE_AIMBOT_ON'] = aimbot_on.value
        config_set['FEATURE_SENSE_ON'] = sense_on.value
        config_set['FEATURE_ITEM_GLOW_ON'] = item_glow_on.value
        config_set['FEATURE_NORECOIL_ON'] = norecoil_on.value
        config_set['FEATURE_TRIGGERBOT_ON'] = triggerbot_on.value
        config_set['FEATURE_QUICKTURN_ON'] = quickturn_on.value
        config_set['FEATURE_QUICKTURN_BUTTON'] = quickturn_button.value
        config_set['FEATURE_SPECTATOR_ON'] = spectator_on.value
        config_set['FEATURE_SKINCHANGER_ON'] = skinchanger_on.value
        config_set['FEATURE_PRINT_LEVELS_ON'] = print_levels.value
        config_set['FEATURE_PRINT_LEVELS_BUTTON'] = print_levels_button.value
        config_set['FEATURE_SUPER_GLIDE_ON'] = super_glide.value
        config_set['FEATURE_MAP_RADAR_ON'] = map_radar.value
        config_set['FEATURE_MAP_RADAR_BUTTON'] = map_radar_button.value
        config_set['NORECOIL_PITCH_REDUCTION'] = norecoil_pitch_reduction.value
        config_set['NORECOIL_YAW_REDUCTION'] = norecoil_yaw_reduction.value
        config_set['TRIGGERBOT_ZOOMED_RANGE'] = triggerbot_zoomed_range.value
        config_set['TRIGGERBOT_HIPFIRE_RANGE'] = triggerbot_hipfire_range.value
        config_set['TRIGGERBOT_PAUSE_BUTTON'] = triggerbot_pause_button.value
        config_set['SENSE_MAXRANGE'] = sense_maxrange.value
        config_set['AIMBOT_ACTIVATED_BY_ATTACK'] = aimbot_activated_by_attack.value
        config_set['AIMBOT_ACTIVATED_BY_ADS'] = aimbot_activated_by_ads.value
        config_set['AIMBOT_ACTIVATED_BY_KEY'] = aimbot_activated_by_key.value
        config_set['AIMBOT_ACTIVATION_KEY'] = aimbot_activation_key.value
        config_set['AIMBOT_SMOOTH'] = aimbot_smooth.value
        config_set['AIMBOT_SMOOTH_EXTRA_BY_DISTANCE'] = aimbot_smooth_extra_by_distance.value
        config_set['AIMBOT_FOV'] = aimbot_fov.value
        config_set['AIMBOT_PREDICT_BULLETDROP'] = aimbot_predict_bulletdrop.value
        config_set['AIMBOT_PREDICT_BULLETDROP'] = aimbot_predict_bulletdrop.value
        config_set['AIMBOT_PREDICT_MOVEMENT'] = aimbot_predict_movement.value
        config_set['AIMBOT_ALLOW_TARGET_SWITCH'] = aimbot_allow_target_switch.value
        config_set['AIMBOT_MAX_DISTANCE'] = aimbot_max_distance.value
        config_set['AIMBOT_MIN_DISTANCE'] = aimbot_min_distance.value
        config_set['AIMBOT_PREDICT_BULLETDROP'] = aimbot_predict_bulletdrop.value
        config_set['AIMBOT_PREDICT_MOVEMENT'] = aimbot_predict_movement.value
        config_set['AIMBOT_ALLOW_TARGET_SWITCH'] = aimbot_allow_target_switch.value
        config_set['AIMBOT_PREDICT_BULLETDROP'] = aimbot_predict_bulletdrop.value
        config_set['AIMBOT_PREDICT_MOVEMENT'] = aimbot_predict_movement.value
        config_set['AIMBOT_PREDICT_BULLETDROP'] = aimbot_predict_bulletdrop.value
        config_set['AIMBOT_PREDICT_BULLETDROP'] = aimbot_predict_bulletdrop.value
        config_set['AIMBOT_PREDICT_MOVEMENT'] = aimbot_predict_movement.value
        config_set['AIMBOT_ALLOW_TARGET_SWITCH'] = aimbot_allow_target_switch.value
        config_set['AIMBOT_MAX_DISTANCE'] = aimbot_max_distance.value
        config_set['AIMBOT_PREDICT_BULLETDROP'] = aimbot_predict_bulletdrop.value
        config_set['AIMBOT_PREDICT_MOVEMENT'] = aimbot_predict_movement.value
        config_set['AIMBOT_PREDICT_BULLETDROP'] = aimbot_predict_bulletdrop.value
        config_set['AIMBOT_PREDICT_BULLETDROP'] = aimbot_predict_bulletdrop.value
        config_set['AIMBOT_PREDICT_MOVEMENT'] = aimbot_predict_movement.value
        config_set['AIMBOT_ALLOW_TARGET_SWITCH'] = aimbot_allow_target_switch.value
        config_set['AIMBOT_MAX_DISTANCE'] = aimbot_max_distance.value
        config_set['AIMBOT_MIN_DISTANCE'] = aimbot_min_distance.value
        config_set.save()
        page.update()

    def update_output():
        cmd_info.value = "Starting ..."
        lines = []
        while True:
            for line in iter(cheat_process.stdout.readline, ''):
                lines.append(line)
                if len(lines) > 20:
                    lines = lines[-20:]
                cmd_info.value = "".join(lines)
                page.update()
            if cheat_process.poll() is not None:
                break
        stdout = cheat_process.stdout.read()
        stderr = cheat_process.stderr.read()
        cmd_info.value += stdout + stderr
        start_button.disabled = False
        page.update()

    cmd_info = ft.Text(value="Apex Free Cheat", color="green")
    j8_input = ft.TextField(hint_text="输入你的J8码", width=300, text_align=ft.TextAlign.CENTER)
    page.add(j8_input)
    start_button = ft.ElevatedButton("Start", on_click=start_clicked)
    page.add(ft.Row([
        ft.ElevatedButton("Register", on_click=reg_clicked),
        ft.ElevatedButton("Logs", on_click=log_clicked),
        ft.ElevatedButton("Config", on_click=config_clicked),
        ft.ElevatedButton("Install Driver", on_click=install_clicked),
        start_button,
        ft.ElevatedButton("Stop", on_click=kill_clicked)
    ], alignment=ft.MainAxisAlignment.CENTER))
    page.add(cmd_info)
    aimbot_on = ft.Checkbox(label="aimbot_on", value=False)
    sense_on = ft.Checkbox(label="sense_on", value=False)
    item_glow_on = ft.Checkbox(label="item_glow_on", value=False)
    norecoil_on = ft.Checkbox(label="norecoil_on", value=False)
    triggerbot_on = ft.Checkbox(label="triggerbot_on", value=False)
    quickturn_on = ft.Checkbox(label="quickturn_on", value=False)
    quickturn_button = ft.TextField(label="quickturn_button", value='XK_F')
    spectator_on = ft.Checkbox(label="spectator_on", value=False)
    skinchanger_on = ft.Checkbox(label="skinchanger_on", value=False)
    print_levels = ft.Checkbox(label="print_levels", value=False)
    print_levels_button = ft.TextField(label="print_level_button", value='XK_P')
    super_glide = ft.Checkbox(label="super_glide", value=False)
    map_radar = ft.Checkbox(label="map_radar", value=False)
    map_radar_button = ft.TextField(label="map_radar_button", value='XK_M')
    norecoil_pitch_reduction = ft.TextField(label="norecoil_pitch_reduction", value='19')
    norecoil_yaw_reduction = ft.TextField(label="norecoil_yaw_reduction", value='20')
    triggerbot_zoomed_range = ft.TextField(label="triggerbot_zoomed_range", value='180')
    triggerbot_hipfire_range = ft.TextField(label="triggerbot_zoomed_range", value='25')
    triggerbot_pause_button = ft.TextField(label="triggerbot_pause_button", value='XK_Z')
    sense_maxrange = ft.TextField(label="sense_maxrange", value='250')
    aimbot_activated_by_attack = ft.Checkbox(label="aimbot_activated_by_attack", value=False)
    aimbot_activated_by_ads = ft.Checkbox(label="aimbot_activated_by_ads", value=False)
    aimbot_activated_by_key = ft.Checkbox(label="aimbot_activated_by_key", value=False)
    aimbot_activation_key  = ft.TextField(label="aimbot_activation_key", value='XK_X')
    aimbot_smooth = ft.TextField(label="aimbot_smooth", value='11.314159')
    aimbot_speed = ft.TextField(label="aimbot_speed", value='81.3141')
    aimbot_smooth_extra_by_distance  = ft.TextField(label="aimbot_speed", value='1500')
    aimbot_fov = ft.TextField(label="aimbot_speed", value='5.3141')
    aimbot_predict_bulletdrop = ft.Checkbox(label="aimbot_predict_bulletdrop", value=False)
    aimbot_predict_movement = ft.Checkbox(label="aimbot_predict_movement", value=False)
    aimbot_allow_target_switch = ft.Checkbox(label="aimbot_allow_target_switch", value=False)
    aimbot_max_distance = ft.TextField(label="aimbot_max_distance", value='69')
    aimbot_min_distance = ft.TextField(label="aimbot_min_distance", value='5')
    config_pan = ft.Column([
        ft.Row([ft.Column([aimbot_on, sense_on, item_glow_on, norecoil_on, triggerbot_on, quickturn_on, quickturn_button,
                           spectator_on, skinchanger_on, print_levels, print_levels_button]),
                ft.Column([super_glide, map_radar, map_radar_button, norecoil_pitch_reduction, norecoil_yaw_reduction,
                          triggerbot_zoomed_range, triggerbot_hipfire_range, triggerbot_pause_button, sense_maxrange]),
                ft.Column([aimbot_activated_by_attack, aimbot_activated_by_ads, aimbot_activated_by_key, aimbot_activation_key,
                          aimbot_smooth, aimbot_speed, aimbot_smooth_extra_by_distance, aimbot_fov, aimbot_predict_bulletdrop]),
                ft.Column([aimbot_predict_movement, aimbot_allow_target_switch, aimbot_max_distance, aimbot_min_distance])]),
        ft.Row([ft.ElevatedButton("load", on_click=load_clicked), ft.ElevatedButton("save", on_click=save_clicked)])
               ])
    load_clicked(None)
    config_pan.visible = False
    page.add(config_pan)

ft.app(target=main)
