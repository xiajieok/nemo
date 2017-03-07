from django.test import TestCase
import paramiko

hostname = '192.168.1.31'
port = 22
username = 'root'

key = paramiko.RSAKey.from_private_key_file('/Users/jack/.ssh/id_rsa')
#创建SSH对象
s = paramiko.SSHClient()
#允许连接不在know_hosts文件中的主机
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#连接服务器
s.connect(hostname,port,username,pkey=key)

#执行命令
stdin,stdout,stderr=s.exec_command('fdisk -l')
#获取结果
res = stdout.read()

print(res.decode())
#关闭连接
s.close()