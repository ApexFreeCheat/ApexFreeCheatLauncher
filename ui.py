import flet as ft
import subprocess
import threading
import time
import webbrowser

cheat_process = None

def main(page):
    page.title = "Launcher"  # 设置窗口标题
    page.window.width = 500
    page.window.height = 650
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.font_family = "Microsoft YaHei"
    page.window.maximizable = False  # 禁止窗口最大化
    page.theme_mode = ft.ThemeMode.LIGHT  # 设置窗口颜色为明亮模式

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
        cmd_info.update()

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
        cmd_info.update()

    cmd_info = ft.Text(value="Hello, world!", color="green")
    j8_input = ft.TextField(hint_text="输入你的J8码", width=300, text_align=ft.TextAlign.CENTER)
    page.add(j8_input)
    page.add(ft.Row([
        ft.ElevatedButton("注册", on_click=reg_clicked),
        ft.ElevatedButton("安装驱动", on_click=install_clicked),
        ft.ElevatedButton("启动", on_click=start_clicked),
        ft.ElevatedButton("关闭", on_click=kill_clicked)
    ], alignment=ft.MainAxisAlignment.CENTER))
    page.add(cmd_info)

ft.app(target=main)
