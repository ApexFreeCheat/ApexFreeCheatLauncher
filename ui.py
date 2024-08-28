import flet as ft
import subprocess
import threading
import time

cheat_process = None

def main(page):
    def install_clicked(e):
        process = subprocess.Popen(
            ['DriverLoader.exe'],  # 要执行的命令和参数
            stdout=subprocess.PIPE,        # 捕获标准输出
            stderr=subprocess.PIPE,         # 捕获标准错误
            shell=True
        )

        # 等待进程完成并获取返回值
        stdout, stderr = process.communicate()
        t.value = stdout.decode('gbk') + stderr.decode('gbk')
        t.update()

    def start_clicked(e):
        global cheat_process
        cheat_process = subprocess.Popen(
            ['ApexFreeCheat.exe', new_task.value],  # 要执行的命令和参数
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
        t.value = ""
        while True:
            lines.append(cheat_process.stdout.readline().decode('gbk'))
            if len(lines) > 20:
                lines = lines[-20:]
            t.value = "".join(lines)
            t.update()
            if cheat_process.poll() is not None:
                break
            time.sleep(0.01)

        # 进程结束后的最终更新
        lines.extend(cheat_process.stdout.read().decode('gbk').splitlines())
        lines.extend(cheat_process.stderr.read().decode('gbk').splitlines())
        if len(lines) > 20:
            lines = lines[-20:]
        t.value = "".join(lines)
        t.update()

    t = ft.Text(value="Hello, world!", color="green")
    page.add(ft.ElevatedButton("安装驱动", on_click=install_clicked))
    new_task = ft.TextField(hint_text="输入你的J8码", width=300)
    page.add(ft.Row([new_task, ft.ElevatedButton("启动", on_click=start_clicked)]))
    page.add(ft.ElevatedButton("关闭", on_click=kill_clicked))
    page.add(t)

ft.app(target=main)
