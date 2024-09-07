import flet as ft
import subprocess
import threading
import time
import webbrowser
from config import config

cheat_process = None

def to_bool(value):
    if isinstance(value, str):
        return value == 'YES'
    return 'YES' if value else 'NO'

def main(page):
    page.title = "Launcher"  # 设置窗口标题
    page.window.width = 800
    page.window.height = 700
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.font_family = "Microsoft YaHei"
    page.window.maximizable = False  # 禁止窗口最大化
    page.theme_mode = ft.ThemeMode.LIGHT  # 设置窗口颜色为明亮模式
    config_set = config()

    def reg_clicked(e):
        webbrowser.open("https://apex.hhhhhi.com")

    def install_clicked(e):
        process = subprocess.Popen(
            ['DriverLoader.exe'],  # 要执行的命令和参数
            stdout=subprocess.PIPE,        # 捕获标准输出
            stderr=subprocess.PIPE,         # 捕获标准错误
            shell=True
        )

        # 等待进程完成并获取返回值
        stdout, stderr = process.communicate()
        cmd_info.value = stdout.decode('gbk') + stderr.decode('gbk')
        page.update()

    def start_clicked(e):
        global cheat_process
        cheat_process = subprocess.Popen(
            ['ApexFreeCheat.exe', j8_input.value],  # 要执行的命令和参数
            stdout=subprocess.PIPE,        # 捕获标准输出
            stderr=subprocess.PIPE,        # 捕获标准错误
            stdin=subprocess.PIPE,          # 提供标准输入
            shell=True
        )
        threading.Thread(target=update_output).start()

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
        aimbot.value = to_bool(config_set['FEATURE_AIMBOT_ON'])
        page.update()

    def save_clicked(e):
        config_set['FEATURE_AIMBOT_ON'] = to_bool(aimbot.value)
        config_set.save()
        page.update()

    def update_output():
        lines = []
        cmd_info.value = ""
        while True:
            lines.append(cheat_process.stdout.readline().decode('gbk'))
            if len(lines) > 20:
                lines = lines[-20:]
            cmd_info.value = "".join(lines)
            cmd_info.update()
            if cheat_process.poll() is not None:
                break
            time.sleep(0.01)

        # 进程结束后的最终更新
        lines.extend(cheat_process.stdout.read().decode('gbk').splitlines())
        lines.extend(cheat_process.stderr.read().decode('gbk').splitlines())
        if len(lines) > 20:
            lines = lines[-20:]
        cmd_info.value = "".join(lines)
        page.update()

    cmd_info = ft.Text(value="Apex Free Cheat", color="green")
    j8_input = ft.TextField(hint_text="输入你的J8码", width=300, text_align=ft.TextAlign.CENTER)
    page.add(j8_input)
    page.add(ft.Row([
        ft.ElevatedButton("注册", on_click=reg_clicked),
        ft.ElevatedButton("日志", on_click=log_clicked),
        ft.ElevatedButton("配置", on_click=config_clicked),
        ft.ElevatedButton("安装驱动", on_click=install_clicked),
        ft.ElevatedButton("启动", on_click=start_clicked),
        ft.ElevatedButton("关闭", on_click=kill_clicked)
    ], alignment=ft.MainAxisAlignment.CENTER))
    page.add(cmd_info)
    aimbot = ft.Checkbox(label="aimbot", value=False)
    sense = ft.Checkbox(label="sense", value=False)
    item_glow = ft.Checkbox(label="item_glow", value=False)
    no_recoil = ft.Checkbox(label="no_recoil", value=False)
    trigger_bot = ft.Checkbox(label="trigger_bot", value=False)
    quick_turn = ft.Checkbox(label="quick_turn", value=False)
    quick_turn_text = ft.Text(value="quick_turn")
    quick_turn_button = ft.TextField(value='F')
    quick_turn_set = ft.Row([quick_turn_text, quick_turn_button])
    sepectator = ft.Checkbox(label="sepectator", value=False)
    skinchanger = ft.Checkbox(label="skinchanger", value=False)
    print_level = ft.Checkbox(label="print_level", value=False)
    print_level_text = ft.Text(value="print_level")
    print_level_button = ft.TextField(value='P')
    print_level_set = ft.Row([print_level_text, print_level_button])
    super_glide = ft.Checkbox(label="super_glide", value=False)
    map_rader = ft.Checkbox(label="map_rader", value=False)
    map_rade_text = ft.Text(value="map_rader")
    map_rade_button = ft.TextField(value='M')
    map_rader_set = ft.Row([map_rade_text, map_rade_button])
    no_recoil_pitch_text = ft.Text(value="no_recoil_pitch")
    no_recoil_pitch_val = ft.TextField(value='19')
    no_recoil_pitch_set = ft.Row([no_recoil_pitch_text, no_recoil_pitch_val])
    no_recoil_yaw_text = ft.Text(value="no_recoil_yaw")
    no_recoil_yaw_val = ft.TextField(value='19')
    no_recoil_yaw_set = ft.Row([no_recoil_yaw_text, no_recoil_yaw_val])
    config_pan = ft.Column([
        ft.Row([ft.Column([aimbot, sense, item_glow, no_recoil, trigger_bot, quick_turn, quick_turn_set, sepectator, skinchanger, print_level, print_level_set]),
               ft.Column([super_glide, map_rader, map_rader_set, no_recoil_pitch_set, no_recoil_yaw_set])]),
        ft.Row([ft.ElevatedButton("load", on_click=load_clicked), ft.ElevatedButton("save", on_click=save_clicked)])
               ])
    config_pan.visible = False
    page.add(config_pan)

ft.app(target=main)
