# windows启动项

### vbs脚本
- 打开windows启动项文件夹：win+R, shell:startup
- windows启动脚本：C:\Users\umas\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\startup.vbs

- startup.vbs中启动wsl / 调用python
  - 参数0表示后台运行
  ```vb
  Set ws=WScript.CreateObject("WScript.Shell") 
  ' ws.Run "wsl -d Ubuntu-20.04 -u root /bin/bash",0
  ws.Run "wsl -u root /bin/bash",0
  ws.Run "python.exe D:\s-linux\project\onebox\run_backend.py",0
  ```