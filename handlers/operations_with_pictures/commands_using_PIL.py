# import io
# import aiohttp
# import PIL
# from PIL import Image
# from PIL import ImageDraw
# from main import dp
# from aiogram.types import Message
# # pip install Image
#
# # Imported PIL Library from PIL import Image
#
#
# # Open an Image
# def open_image(path):
#     newImage = Image.open(path)
#     return newImage
#
#
# # Save Image
# def save_image(image, path):
#     image.save(path, 'png')
#
#
# # Create a new image with the given size
# def create_image(i, j):
#     image = Image.new("RGB", (i, j), "white")
#     return image
#
#
# # Get the pixel from the given image
# def get_pixel(image, i, j):
#     # Inside image bounds?
#     width, height = image.size
#     if i > width or j > height:
#         return None
#     # Get Pixel
#     pixel = image.getpixel((i, j))
#     return pixel
#
#
# def convert_grayscale(image):
#     # Get size
#     width, height = image.size
#
#     # Create new Image and a Pixel Map
#     new = create_image(width, height)
#     pixels = new.load()
#
#     # Transform to grayscale
#     for i in range(width):
#         for j in range(height):
#             # Get Pixel
#             pixel = get_pixel(image, i, j)
#
#             # Get R, G, B values (This are int from 0 to 255)
#             red = pixel[0]
#             green = pixel[1]
#             blue = pixel[2]
#
#             # Transform to grayscale
#             gray = (red * 0.299) + (green * 0.587) + (blue * 0.114)
#
#             # Set Pixel in new image
#             pixels[i, j] = (int(gray), int(gray), int(gray))
#
#     # Return new image
#     return new
#
#
# # Create a Half-tone version of the image
# def convert_halftoning(image):
#     # Get size
#     width, height = image.size
#
#     # Create new Image and a Pixel Map
#     new = create_image(width, height)
#     pixels = new.load()
#
#     # Transform to half tones
#     for i in range(0, width, 2):
#         for j in range(0, height, 2):
#             # Get Pixels
#             p1 = get_pixel(image, i, j)
#             p2 = get_pixel(image, i, j + 1)
#             p3 = get_pixel(image, i + 1, j)
#             p4 = get_pixel(image, i + 1, j + 1)
#
#             # Transform to grayscale
#             gray1 = (p1[0] * 0.299) + (p1[1] * 0.587) + (p1[2] * 0.114)
#             gray2 = (p2[0] * 0.299) + (p2[1] * 0.587) + (p2[2] * 0.114)
#             gray3 = (p3[0] * 0.299) + (p3[1] * 0.587) + (p3[2] * 0.114)
#             gray4 = (p4[0] * 0.299) + (p4[1] * 0.587) + (p4[2] * 0.114)
#
#             # Saturation Percentage
#             sat = (gray1 + gray2 + gray3 + gray4) / 4
#
#             # Draw white/black depending on saturation
#             if sat > 223:
#                 pixels[i, j]         = (255, 255, 255) # White
#                 pixels[i, j + 1]     = (255, 255, 255) # White
#                 pixels[i + 1, j]     = (255, 255, 255) # White
#                 pixels[i + 1, j + 1] = (255, 255, 255) # White
#             elif sat > 159:
#                 pixels[i, j]         = (255, 255, 255) # White
#                 pixels[i, j + 1]     = (0, 0, 0)       # Black
#                 pixels[i + 1, j]     = (255, 255, 255) # White
#                 pixels[i + 1, j + 1] = (255, 255, 255) # White
#             elif sat > 95:
#                 pixels[i, j]         = (255, 255, 255) # White
#                 pixels[i, j + 1]     = (0, 0, 0)       # Black
#                 pixels[i + 1, j]     = (0, 0, 0)       # Black
#                 pixels[i + 1, j + 1] = (255, 255, 255) # White
#             elif sat > 32:
#                 pixels[i, j]         = (0, 0, 0)       # Black
#                 pixels[i, j + 1]     = (255, 255, 255) # White
#                 pixels[i + 1, j]     = (0, 0, 0)       # Black
#                 pixels[i + 1, j + 1] = (0, 0, 0)       # Black
#             else:
#                 pixels[i, j]         = (0, 0, 0)       # Black
#                 pixels[i, j + 1]     = (0, 0, 0)       # Black
#                 pixels[i + 1, j]     = (0, 0, 0)       # Black
#                 pixels[i + 1, j + 1] = (0, 0, 0)       # Black
#     # Return new image
#     return new
#
#
# # Return color value depending on quadrant and saturation
# def get_saturation(value, quadrant):
#     if value > 223:
#         return 255
#     elif value > 159:
#         if quadrant != 1:
#             return 255
#         return 0
#
#     elif value > 95:
#         if quadrant == 0 or quadrant == 3:
#             return 255
#         return 0
#
#     elif value > 32:
#         if quadrant == 1:
#             return 255
#         return 0
#
#     else:
#         return 0
#
#
# # Create a dithered version of the image
# def convert_dithering(image):
#     # Get size
#     width, height = image.size
#
#     # Create new Image and a Pixel Map
#     new = create_image(width, height)
#     pixels = new.load()
#
#     # Transform to half tones
#     for i in range(0, width, 2):
#         for j in range(0, height, 2):
#             # Get Pixels
#             p1 = get_pixel(image, i, j)
#             p2 = get_pixel(image, i, j + 1)
#             p3 = get_pixel(image, i + 1, j)
#             p4 = get_pixel(image, i + 1, j + 1)
#             # Color Saturation by RGB channel
#             red   = (p1[0] + p2[0] + p3[0] + p4[0]) / 4
#             green = (p1[1] + p2[1] + p3[1] + p4[1]) / 4
#             blue  = (p1[2] + p2[2] + p3[2] + p4[2]) / 4
#             # Results by channel
#             r = [0, 0, 0, 0]
#             g = [0, 0, 0, 0]
#             b = [0, 0, 0, 0]
#             # Get Quadrant Color
#             for x in range(0, 4):
#                 r[x] = get_saturation(red, x)
#                 g[x] = get_saturation(green, x)
#                 b[x] = get_saturation(blue, x)
#
#             # Set Dithered Colors
#             pixels[i, j]         = (r[0], g[0], b[0])
#             pixels[i, j + 1]     = (r[1], g[1], b[1])
#             pixels[i + 1, j]     = (r[2], g[2], b[2])
#             pixels[i + 1, j + 1] = (r[3], g[3], b[3])
#     # Return new image
#     return new
#
#
# # Create a Primary Colors version of the image
# def convert_primary(image):
#     # Get size
#     width, height = image.size
#
#     # Create new Image and a Pixel Map
#     new = create_image(width, height)
#     pixels = new.load()
#
#     # Transform to primary
#     for i in range(width):
#         for j in range(height):
#             # Get Pixel
#             pixel = get_pixel(image, i, j)
#
#             # Get R, G, B values (This are int from 0 to 255)
#             red =   pixel[0]
#             green = pixel[1]
#             blue =  pixel[2]
#
#             # Transform to primary
#             if red > 127:
#                 red = 255
#             else:
#                 red = 0
#             if green > 127:
#                 green = 255
#             else:
#                 green = 0
#             if blue > 127:
#                 blue = 255
#             else:
#                 blue = 0
#
#             # Set Pixel in new image
#             pixels[i, j] = (int(red), int(green), int(blue))
#
#     # Return new image
#     return new
#
#
# # command
# # тест еще одной команды
# @dp.message_handler(commands=['mirror'])
# async def get_site_screenshot(message: Message):
#     photo = False
#     print(message)
#     await message.answer(message.reply_to_message.photo[0])
#     if message.text == '/mirror':
#         await message.reply('Вы не прислали сайт')
#     else:
#         user_msg = ''.join(message.text.split('/mirror ')[1])
#
# # @plugin.on_command('отзеркаль', 'Отзеркаль')
# # async def mirror(msg, args):
# #     photo = False
# #     for k, v in msg.brief_attaches.items():
# #         if '_type' in k and v == "photo":
# #             photo = True
# #             break
# #
# #     if not photo:
# #         return await msg.answer('Вы не прислали фото!')
# #
# #     attach = (await msg.full_attaches)[0]
# #
# #     if not attach.link:
# #         return await msg.answer('Вы не прислали фото!')
# #
# #     async with aiohttp.ClientSession() as sess:
# #         async with sess.get(attach.link) as response:
# #             img = Image.open(io.BytesIO(await response.read()))
# #
# #     if not img:
# #         return await msg.answer('К сожалению, ваше фото исчезло!')
# #
# #     w, h = img.size
# #
# #     part = img.crop((0, 0, w / 2, h))
# #     part1 = part.transpose(Image.FLIP_LEFT_RIGHT)
# #     img.paste(part1, (round(w / 2), 0))
# #
# #     buffer = io.BytesIO()
# #     img.save(buffer, format='png')
# #     buffer.seek(0)
# #
# #     result = await msg.vk.upload_photo(buffer)
# #
# #     return await msg.answer('Держи', attachment=str(result))
# #
# #
# #
# #
# # @plugin.on_command('Зеркало верх', 'зеркало верх')
# # async def anti_mirror(msg, args):
# #     photo = False
# #     for k, v in msg.brief_attaches.items():
# #         if '_type' in k and v == "photo":
# #             photo = True
# #             break
# #
# #     if not photo:
# #         return await msg.answer('Вы не прислали фото!')
# #
# #     attach = (await msg.full_attaches)[0]
# #
# #     if not attach.link:
# #         return await msg.answer('Вы не прислали фото!')
# #
# #     async with aiohttp.ClientSession() as sess:
# #         async with sess.get(attach.link) as response:
# #             img = Image.open(io.BytesIO(await response.read()))
# #
# #     if not img:
# #         return await msg.answer('К сожалению, ваше фото исчезло!')
# #
# #     w, h = img.size
# #
# #     part = img.crop((0, 0, w, h / 2))
# #     part1 = part.transpose(Image.FLIP_TOP_BOTTOM)
# #     img.paste(part1, (0, round(h / 2)))
# #
# #     buffer = io.BytesIO()
# #     img.save(buffer, format='png')
# #     buffer.seek(0)
# #
# #     result = await msg.vk.upload_photo(buffer)
# #
# #     return await msg.answer('Держи', attachment=str(result))
# #
# # @plugin.on_command('слей', 'Слей')
# # async def anti_mirror1(msg, args):
# #     photo = False
# #     for k, v in msg.brief_attaches.items():
# #         if '_type' in k and v == "photo":
# #             photo = True
# #             break
# #
# #     if not photo:
# #         return await msg.answer('Вы не прислали фото!')
# #
# #     attach = (await msg.full_attaches)[0]
# #     attach1 = (await msg.full_attaches)[1]
# #
# #     if not attach.link and attach1.link:
# #         return await msg.answer('Вы не прислали фото!')
# #
# #     async with aiohttp.ClientSession() as sess:
# #         async with sess.get(attach.link) as response:
# #             img = Image.open(io.BytesIO(await response.read()))
# #             async with sess.get(attach1.link) as response:
# #                 img1 = Image.open(io.BytesIO(await response.read()))
# #
# #     if not img:
# #         return await msg.answer('К сожалению, ваше фото исчезло!')
# #
# #     w, h = img.size
# #     # print(f' ARGS = {args[0]} + {type(args)}')
# #     if not args:
# #         alpha = 0.5
# #     else:
# #         alpha = float(args[0])
# #         if alpha > 1:
# #             return await msg.answer('Вы ввели коэффициент alpha больше 1. Коэффициент должен находиться в пределе от 0.1'
# #                                     ' до 1')
# #     w1, h1 = img1.size
# #     check_size_1_is_bigger_H = h > h1
# #     check_size_1_is_bigger_W = w > w1
# #     if check_size_1_is_bigger_H is True:
# #         check_size_1_is_bigger_H = h1
# #     else:
# #         check_size_1_is_bigger_H = h
# #
# #     if check_size_1_is_bigger_W is True:
# #         check_size_1_is_bigger_W = w1
# #     else:
# #         check_size_1_is_bigger_W = w
# #
# #     img = img.resize((check_size_1_is_bigger_W, check_size_1_is_bigger_H), Image.BILINEAR)
# #     img1 = img1.resize((check_size_1_is_bigger_W, check_size_1_is_bigger_H), Image.BILINEAR)
# #     out = Image.blend(img, img1, alpha)
# #     # out = img * (1.0 - alpha) + img2 * alpha
# #     # part = img.crop((0, 0, w, h / 2))
# #     # # part1 = part.transpose(Image.)
# #     # img.paste(part1, (0, round(h / 2)))
# #     img.paste(out)
# #     buffer = io.BytesIO()
# #     img.save(buffer, format='png')
# #     buffer.seek(0)
# #
# #     result = await msg.vk.upload_photo(buffer)
# #
# #     return await msg.answer('Держи', attachment=str(result))
# #
# #
# # @plugin.on_command('чб', 'Чб')
# # async def convert_grayscale_ph(msg, args):
# #     photo = False
# #     for k, v in msg.brief_attaches.items():
# #         if '_type' in k and v == "photo":
# #             photo = True
# #             break
# #
# #     if not photo:
# #         return await msg.answer('Вы не прислали фото!')
# #
# #     attach = (await msg.full_attaches)[0]
# #
# #     if not attach.link:
# #         return await msg.answer('Вы не прислали фото!')
# #
# #     async with aiohttp.ClientSession() as sess:
# #         async with sess.get(attach.link) as response:
# #             img = Image.open(io.BytesIO(await response.read()))
# #
# #     if not img:
# #         return await msg.answer('К сожалению, ваше фото исчезло!')
# #
# #     part1 = convert_grayscale(img)
# #     img.paste(part1)
# #
# #     buffer = io.BytesIO()
# #     img.save(buffer, format='png')
# #     buffer.seek(0)
# #
# #     result = await msg.vk.upload_photo(buffer)
# #
# #     return await msg.answer('Держи', attachment=str(result))
# #
# #
# # @plugin.on_command('полутон', 'Полутон')
# # async def convert_halftoning_ph(msg, args):
# #     photo = False
# #     for k, v in msg.brief_attaches.items():
# #         if '_type' in k and v == "photo":
# #             photo = True
# #             break
# #
# #     if not photo:
# #         return await msg.answer('Вы не прислали фото!')
# #
# #     attach = (await msg.full_attaches)[0]
# #
# #     if not attach.link:
# #         return await msg.answer('Вы не прислали фото!')
# #
# #     async with aiohttp.ClientSession() as sess:
# #         async with sess.get(attach.link) as response:
# #             img = Image.open(io.BytesIO(await response.read()))
# #
# #     if not img:
# #         return await msg.answer('К сожалению, ваше фото исчезло!')
# #
# #
# #     part1 = convert_halftoning(img)
# #     img.paste(part1)
# #
# #     buffer = io.BytesIO()
# #     img.save(buffer, format='png')
# #     buffer.seek(0)
# #
# #     result = await msg.vk.upload_photo(buffer)
# #
# #     return await msg.answer('Держи', attachment=str(result))
# #
# #
# #
# # @plugin.on_command('сгладь', 'Сгладь')
# # async def convert_dithering_ph(msg, args):
# #     photo = False
# #     for k, v in msg.brief_attaches.items():
# #         if '_type' in k and v == "photo":
# #             photo = True
# #             break
# #
# #     if not photo:
# #         return await msg.answer('Вы не прислали фото!')
# #
# #     attach = (await msg.full_attaches)[0]
# #
# #     if not attach.link:
# #         return await msg.answer('Вы не прислали фото!')
# #
# #     async with aiohttp.ClientSession() as sess:
# #         async with sess.get(attach.link) as response:
# #             img = Image.open(io.BytesIO(await response.read()))
# #
# #     if not img:
# #         return await msg.answer('К сожалению, ваше фото исчезло!')
# #
# #
# #     part1 = convert_dithering(img)
# #     img.paste(part1)
# #
# #     buffer = io.BytesIO()
# #     img.save(buffer, format='png')
# #     buffer.seek(0)
# #
# #     result = await msg.vk.upload_photo(buffer)
# #
# #     return await msg.answer('Держи', attachment=str(result))
# #
# #
# #
# #
# # @plugin.on_command('засвети', 'Засвети')
# # async def convert_primary_ph(msg, args):
# #     photo = False
# #     for k, v in msg.brief_attaches.items():
# #         if '_type' in k and v == "photo":
# #             photo = True
# #             break
# #
# #     if not photo:
# #         return await msg.answer('Вы не прислали фото!')
# #
# #     attach = (await msg.full_attaches)[0]
# #
# #     if not attach.link:
# #         return await msg.answer('Вы не прислали фото!')
# #
# #     async with aiohttp.ClientSession() as sess:
# #         async with sess.get(attach.link) as response:
# #             img = Image.open(io.BytesIO(await response.read()))
# #
# #     if not img:
# #         return await msg.answer('К сожалению, ваше фото исчезло!')
# #
# #
# #     part1 = convert_primary(img)
# #     img.paste(part1)
# #
# #     buffer = io.BytesIO()
# #     img.save(buffer, format='png')
# #     buffer.seek(0)
# #
# #     result = await msg.vk.upload_photo(buffer)
# #
# #     return await msg.answer('Держи', attachment=str(result))
# #
# #
# # @plugin.on_command('разверни', 'Разверни')
# # async def anti_mirror99(msg, args):
# #     photo = False
# #     for k, v in msg.brief_attaches.items():
# #         if '_type' in k and v == "photo":
# #             photo = True
# #             break
# #
# #     if not photo:
# #         return await msg.answer('Вы не прислали фото!')
# #
# #     attach = (await msg.full_attaches)[0]
# #
# #     if not attach.link:
# #         return await msg.answer('Вы не прислали фото!')
# #
# #     async with aiohttp.ClientSession() as sess:
# #         async with sess.get(attach.link) as response:
# #             img = Image.open(io.BytesIO(await response.read()))
# #
# #     if not img:
# #         return await msg.answer('К сожалению, ваше фото исчезло!')
# #
# #     w, h = img.size
# #
# #     # part = img.crop((0, 0, w, h / 2))
# #     # part1 = img.transpose(Image.RLE)
# #     part1 = img.transpose(Image.FLIP_LEFT_RIGHT)
# #     img.paste(part1)
# #
# #     buffer = io.BytesIO()
# #     img.save(buffer, format='png')
# #     buffer.seek(0)
# #
# #     result = await msg.vk.upload_photo(buffer)
# #
# #     return await msg.answer('Держи', attachment=str(result))
# #
# #
# # @plugin.on_command('перекрут', 'Перекрут')
# # async def anti_mirror999(msg, args):
# #     photo = False
# #     for k, v in msg.brief_attaches.items():
# #         if '_type' in k and v == "photo":
# #             photo = True
# #             break
# #
# #     if not photo:
# #         return await msg.answer('Вы не прислали фото!')
# #
# #     attach = (await msg.full_attaches)[0]
# #
# #     if not attach.link:
# #         return await msg.answer('Вы не прислали фото!')
# #
# #     async with aiohttp.ClientSession() as sess:
# #         async with sess.get(attach.link) as response:
# #             img = Image.open(io.BytesIO(await response.read()))
# #
# #     if not img:
# #         return await msg.answer('К сожалению, ваше фото исчезло!')
# #
# #     w, h = img.size
# #
# #     # part = img.crop((0, 0, w, h / 2))
# #     # part1 = img.transpose(Image.RLE)
# #     part1 = img.transpose(Image.FLIP_TOP_BOTTOM)
# #     img.paste(part1)
# #
# #     buffer = io.BytesIO()
# #     img.save(buffer, format='png')
# #     buffer.seek(0)
# #
# #     result = await msg.vk.upload_photo(buffer)
# #
# #     return await msg.answer('Держи', attachment=str(result))