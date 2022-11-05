
import os
import shutil


caminho_original = r'C:\Users\Almerinda Home\Desktop\pasta.teste'
caminho_novo = r'C:\Users\Almerinda Home\Desktop\pasta.teste\criadaComPython'

try:
    os.mkdir(caminho_novo)
except FileExistsError as e:
    print(f'Pasta {caminho_novo} já existe.')

for root, dirs, files in os.walk(caminho_novo):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)

        # shutil.move(old_file_path, new_file_path)  # "move" serve também para renomear
        # shutil.copy(old_file_path, new_file_path)
        # print(f'Arquivo {file} movido com sucesso!')

        print(new_file_path)
        os.remove(new_file_path)



