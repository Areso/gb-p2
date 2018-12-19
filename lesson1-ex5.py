import subprocess

args = ['ping', 'yandex.ru']
subproc_ping_ya = subprocess.Popen(args, stdout=subprocess.PIPE)
for line in subproc_ping_ya.stdout:
    print(line.decode('cp866').encode('utf-8').decode('utf-8'))

args_yt = ['ping', 'youtube.com']
subproc_ping_yt = subprocess.Popen(args_yt, stdout=subprocess.PIPE)
for line in subproc_ping_yt.stdout:
    print(line.decode('cp866').encode('utf-8').decode('utf-8'))