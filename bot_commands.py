import os

from config import _COMMANDS_DIR, _base_root, _main_handler_filename

if __name__ == "__main__":
    _base_root = os.getcwd().split(f"{_COMMANDS_DIR}")[0]

path_handler_dir = _base_root + f"\\{_COMMANDS_DIR}"  # Path to handler dir
handler_dir = os.listdir(path_handler_dir)  # All objects from handler path

# filename of file with all functions which ought to be imported in main handler.py
filename_handler_functions_import = 'filename_handler_functions_import'


def get_files_paths(path):
    """
    Get paths to files with handler functions
    :param path:
    :return:
    """
    temp_paths = list()
    for i in os.listdir(path):
        # print(f'    inside func object= {i},  path= {path}')
        if os.path.isdir(path + f'\\{i}'):
            if os.path.isdir(path + f'\\{i}'):
                # print(f'        {i} is a dir')
                temp_paths.extend(get_files_paths(path + f'\\{i}'))

        else:
            # print(f'        {i} is a file')
            if i[-3:] == ".py":
                temp_paths.append(path + f'\\{i}')
    # print(f'temp_paths ===== {temp_paths}')
    return temp_paths.copy()


def get_commands_from_file(file_path):
    """
    Get handler functions' names
    :param file_path:
    :return:
    """
    BOT_COMMANDS = dict()
    with open(f'{file_path}', 'r', encoding='utf-8') as file_handlers:
        flag_find_command = False
        local_list = [None, None]
        for i in file_handlers:
            if i.startswith('# command'):
                flag_find_command = True
                continue
            if flag_find_command is True:
                if i.startswith('# '):
                    local_list[1] = i.split("# ")[1]
                elif i.startswith('@dp.message_handler(commands=['):
                    local_list[0] = i[i.find("[") + 1:i.find(']')]
                    local_dict = {
                        local_list[0].replace("'", ""): local_list[1].replace('\n', ''),
                    }
                    BOT_COMMANDS.update(local_dict.copy())
                    local_list = [None, None]
                    flag_find_command = False
                else:
                    flag_find_command = False
    return BOT_COMMANDS


# new_str = '\n'
# print(f'\n\n\n'
#       f'get_dirs_paths = {f"{new_str}".join(get_files_paths(path_handler_dir))}')


def get_all_commands(path=path_handler_dir):
    BOT_COMMANDS = dict()
    for file_path in get_files_paths(path):
        BOT_COMMANDS.update(get_commands_from_file(file_path))
    return BOT_COMMANDS


# BOT_COMMANDS = get_all_commands(path_handler_dir)


# commands_as_a_list = [f'Команда: /{i} - {BOT_COMMANDS.get(i)}' for i in BOT_COMMANDS.keys()]
# print('\n'.join(commands_as_a_list))

def _get_all_commands_functions_names(file_path):
    """
    Get all handler's commands names
    :param file_path:
    :return:
    """
    BOT_COMMANDS_FUNCS = list()
    with open(f'{file_path}', 'r', encoding='utf-8') as file_handlers:
        flag_find_command = False
        for i in file_handlers:
            if i.startswith('# command'):
                flag_find_command = True
                continue
            if flag_find_command is True:
                if i.startswith('# '):
                    continue
                elif i.startswith('@dp.'):
                    continue
                elif i.startswith('async def '):
                    func_name = i.split("async def ")[1]
                    BOT_COMMANDS_FUNCS.append(func_name[0:func_name.find("(")])
                    flag_find_command = False
                else:
                    flag_find_command = False
    return BOT_COMMANDS_FUNCS


def import_all_commands_functions(path=path_handler_dir):
    """
    This function create file with all handler's commands functions imports
    :param path:
    :return:
    """
    import_list = list()
    for file_path in get_files_paths(path):
        # print(f"get_files_paths ========  {file_path}   \n"
        #       f"                          {path_handler_dir}\\{_main_handler_filename}")
        if file_path != (path_handler_dir + f'\\{_main_handler_filename}'):
            funcs_from_a_file = _get_all_commands_functions_names(file_path=file_path)
            for func in funcs_from_a_file:
                # print(f'file_path= {file_path} _COMMANDS_DIR= {_COMMANDS_DIR}\n')
                file_dirs = file_path[file_path.find(f'{_COMMANDS_DIR}')+len(f'{_COMMANDS_DIR}'):].split("\\")[1:]
                file_dirs[-1] = file_dirs[-1].replace(".py", "")
                # print(f'file_dirs=  {file_dirs}')
                import_string = f'from {_COMMANDS_DIR}.{".".join(file_dirs)} import {func}'
                # import_string = f'from {".".join(file_dirs)} import {func}'
                # print(f'import string =   {import_string}')
                import_list.append(import_string)
    with open(f"{filename_handler_functions_import}.py", 'w', encoding='utf-8') as import_file:
        for i in import_list:
            import_file.write(i + '\n')
