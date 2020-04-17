# from main import dp
# from aiogram.types import Message
# import json
#
#
# def conv2dict(aiogram_message_class_answer):
#     obj_str = aiogram_message_class_answer.as_json()
#     str2json = json.loads(obj_str)
#     return str2json
#
#
# def search_in_list(list_value, lvl, tag_name=None):
#     for i in list_value:
#         if type(i) is dict:
#             # print(" " * lvl * 5, i)
#             tag_flag = search4tag(level=lvl + 1, dict_obj=i, tag_name=tag_name)
#             if tag_flag is not None:
#                 return i
#         elif type(i) is list:
#             from_return = search_in_list(list_value, lvl, tag_name)
#             if from_return is not None:
#                 return from_return
#     return None
#
#
# def search4tag(level=0, dict_obj=None, tag_name=None):
#     lvl = level
#     for keys in dict_obj.keys():
#         # print(f'keys= {keys}   tag_name= {tag_name}')
#         if keys == tag_name:
#             print('- '*100, dict_obj.get(keys))
#             return dict_obj.get(keys)
#         # print(f'{" "*(5*level+1)}lvl= {lvl} type(keys) = {type(keys)}  key = {keys}  data = {dict_obj.get(keys)}')
#         if type(dict_obj.get(keys)) in [dict, list]:
#             if type(dict_obj.get(keys)) is dict:
#                 # print(" "*lvl*5, keys)
#                 tag_flag = search4tag(level=lvl+1, dict_obj=dict_obj.get(keys), tag_name=tag_name)
#                 if tag_flag is not None:
#                     return dict_obj.get(keys)
#             elif type(dict_obj.get(keys)) is list:
#                 from_return = search_in_list(dict_obj.get(keys), lvl, tag_name)
#                 if from_return is not None:
#                     return from_return
#     return None
#
#
#
#
# # command
# # тест еще одной команды
# @dp.message_handler(commands=['r'], content_types=['photo', 'text'])
# async def get_site_screenshot(message: Message):
#     photo = False
#     message_dict = conv2dict(message)
#     print(search4tag(level=0, dict_obj=message_dict, tag_name='photo'))
#
#
#     # print(message)
#     await message.answer(message)
#     await message.answer(message.reply_to_message.photo[0])
#     # if message.text == '/mirror':
#     #     await message.reply('Вы не прислали сайт')
#     # else:
#     #     user_msg = ''.join(message.text.split('/mirror ')[1])