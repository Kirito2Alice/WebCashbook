'''
根据文件夹路径和后缀名获得文件和sha1码列表
'''
import os

def get_files_info(path: str, typename: list):
    '''
    序列化模块
    '''
    temp_list = []
    for i in typename:
        temp = path + r'\*.' + i
        temp_list.append(temp)
    pattern = 'and'.join(temp_list)
    dir_cmd = '''dir "{pattern}" /b/s/-d'''.format(pattern=pattern)
    f = os.popen(dir_cmd)
    files_list = f.readlines()

    print(len(files_list))
    count_sum = len(files_list)
    files_info_list = []
    count = 0
    for i in files_list:
        sha1_cmd = '''certutil -hashfile "{file_name}" SHA1'''.format(file_name=i.strip('\n'))
        file_sha1 = os.popen(sha1_cmd)
        files_info_list.append([i.strip('\n'), file_sha1.readlines()[1].strip()])
        # print(file_SHA1.readlines()[1].strip())
        count += 1
        if count % 10 == 0:
            print('已完成 >>>> %.2f%%'% (count/count_sum*100))