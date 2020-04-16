from main import dp
from aiogram.types import Message
from config import _google_cloud_key_json_name, _sTT_google_sp_kit_lang, _path_to_ffmpeg
import os
import io
from google.cloud import speech_v1
from google.cloud.speech_v1 import enums
import subprocess
import tempfile


# command
# Распознования речи в текст
@dp.message_handler(commands=['stt', 's'])
async def speech_to_text1(message: Message):
    voice_msg_id = message.reply_to_message.voice.file_id
    data_bytes = await dp.bot.get_file(voice_msg_id)
    await data_bytes.download()
    # https://cloud.google.com/speech-to-text/docs/sync-recognize
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = _google_cloud_key_json_name
    client = speech_v1.SpeechClient()
    # The language of the supplied audio
    language_code = _sTT_google_sp_kit_lang
    # Sample rate in Hertz of the audio data sent
    sample_rate_hertz = 16000
    # https://googleapis.dev/nodejs/speech/latest/google.cloud.speech.v1p1beta1.html
    encoding = enums.RecognitionConfig.AudioEncoding.LINEAR16
    config = {
        "language_code": language_code,
        "sample_rate_hertz": sample_rate_hertz,
        "encoding": encoding,
    }
    name_voice = data_bytes.file_path
    with io.open(name_voice, "rb") as f:
        content = f.read()
        content = convert_to_pcm16b16000r(in_bytes=content)
    audio = {"content": content}

    # synchronous mode
    response = client.recognize(config, audio)

    # # asynchronous mode
    # operation = client.long_running_recognize(config, audio)
    # # print("Waiting for operation to complete...")
    # response = operation.result()

    os.remove(name_voice)
    answer = "Не удалось распознать сообщение"
    for result in response.results:
        alternative = result.alternatives[0]
        answer = alternative.transcript
    await message.reply(f'{answer}')


def convert_to_pcm16b16000r(in_filename=None, in_bytes=None):
    """
    Converter from OGG to PCM16. Use in_bytes= as an argument for bytes object
    It works better with PCM16 than OGG if you use it to send voice to google speech kit.
    :param in_filename:
    :param in_bytes:
    :return:
    """
    with tempfile.TemporaryFile() as temp_out_file:
        temp_in_file = None
        if in_bytes:
            temp_in_file = tempfile.NamedTemporaryFile(delete=False)
            temp_in_file.write(in_bytes)
            in_filename = temp_in_file.name
            temp_in_file.close()
        if not in_filename:
            raise Exception('Neither input file name nor input bytes is specified.')

        # Запрос в командную строку для обращения к FFmpeg
        command = [
            f'{_path_to_ffmpeg}',  # путь до ffmpeg.exe
            '-i', in_filename,
            '-f', 's16le',
            '-acodec', 'pcm_s16le',
            '-ar', '16000',
            '-'
        ]

        proc = subprocess.Popen(command, stdout=temp_out_file, stderr=subprocess.DEVNULL)
        proc.wait()

        if temp_in_file:
            os.remove(in_filename)

        temp_out_file.seek(0)
        return temp_out_file.read()


# The same as previous, but not using ffmpeg. Only opus type
# # command
# # Распознования речи в текст
# @dp.message_handler(commands=['stt'])
# async def speech_to_text(message: Message):
#     reply_msg_id = message.reply_to_message.message_id
#     voice_msg_id = message.reply_to_message.voice.file_id
#     data_bytes = await dp.bot.get_file(voice_msg_id)
#     await data_bytes.download()
#     # https://cloud.google.com/speech-to-text/docs/sync-recognize
#     os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = _google_cloud_key_json_name
#     client = speech_v1.SpeechClient()
#     # The language of the supplied audio
#     language_code = "ru-RU"
#     # Sample rate in Hertz of the audio data sent
#     sample_rate_hertz = 48000
#     # https://googleapis.dev/nodejs/speech/latest/google.cloud.speech.v1p1beta1.html
#     encoding = enums.RecognitionConfig.AudioEncoding.OGG_OPUS
#     config = {
#         "language_code": language_code,
#         "sample_rate_hertz": sample_rate_hertz,
#         "encoding": encoding,
#     }
#     name_mp3 = data_bytes.file_path
#     with io.open(name_mp3, "rb") as f:
#         content = f.read()
#     audio = {"content": content}
#
#     response = client.recognize(config, audio)
#     print(message.reply_to_message.voice)
#
#     # operation = client.long_running_recognize(config, audio)
#     # print(operation)
#     # print(u"Waiting for operation to complete...")
#     # response = operation.result()
#     # print('this is response  ')
#     answer = "Не удалось распознать сообщение"
#     os.remove(name_mp3)
#     for result in response.results:
#         # print(result)
#         # First alternative is the most probable result
#         alternative = result.alternatives[0]
#         answer = alternative.transcript
#         # print(u"Transcript: {}".format(alternative.transcript))
#     await message.reply(f'{answer}')

