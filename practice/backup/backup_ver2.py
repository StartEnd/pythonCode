import os
import time

# 1. 需要备份的文件与目录将被
# 指定一个列表中
source = ['~/Code/python']

# 2. 备份文件必须存储在一个
# 主备份目录中

backup_dir = '/Users/song/Desktop/backup'


# 3. 备份文件将打包压缩成zip文件
# 4. zip压缩文件的文件名由当前日期与时间构成

today = backup_dir + os.sep + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')
target = today + os.sep + now + '.zip'


# 如果目录不存在,则进行创建
if not os.path.exists(today):
    os.mkdir(today)
    print('Successed create directory:',today)

# 5. 我们使用zip命令将文件打包成zip格式
zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))


# 运行备份
print('Zip command is:')
print(zip_command)
print('Runnind:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')
