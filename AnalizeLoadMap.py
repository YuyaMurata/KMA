import os
import shutil

#ファイルが格納される親フォルダ
path_fd = 'C:/UiPath/LoadMap/output/'
outpath_fd = 'loadmap/'

#ファイルを変換するシェル
shell_cnt = 'parser/py_c87_count.bat'
shell_hour = 'parser/py_c87_hour.bat'


root = os.listdir(path_fd)

for file in root:
    if '.' in file:
        continue

    print(file)

    try:
        print('Trans_CNT>')
        os.system(shell_cnt.replace('/', '\\')+' '+path_fd.replace('/', '\\')+file)
        #os.rename(path_fd+file+"_output_count.csv", path_fd+file.replace(".txt", "")+"_output_count.csv")
        outfile1 = path_fd+file+"_output_count.csv"
        shutil.move(outfile1, outpath_fd)

        print('Trans_HOUR>')
        os.system(shell_hour.replace('/', '\\')+' '+path_fd.replace('/', '\\')+file)
        #os.rename(path_fd + file + "_output_hour.csv", path_fd + file.replace(".txt", "") + "_output_hour.csv")
        outfile2 = path_fd + file + "_output_hour.csv"
        shutil.move(outfile2, outpath_fd)
    except:
        print('no create!')

