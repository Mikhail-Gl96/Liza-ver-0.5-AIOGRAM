from main import dp
from aiogram.types import Message
from config import _google_cloud_key_json_name
import os
import io
from google.cloud import speech_v1
from google.cloud.speech_v1 import enums


# command
# Распознования речи в текст
@dp.message_handler(commands=['stt'])
async def speech_to_text(message: Message):
    reply_msg_id = message.reply_to_message.message_id
    voice_msg_id = message.reply_to_message.voice.file_id
    data_bytes = await dp.bot.get_file(voice_msg_id)
    await data_bytes.download()
    # https://cloud.google.com/speech-to-text/docs/sync-recognize
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = _google_cloud_key_json_name
    client = speech_v1.SpeechClient()
    # The language of the supplied audio
    language_code = "ru-RU"
    # Sample rate in Hertz of the audio data sent
    sample_rate_hertz = 48000
    # https://googleapis.dev/nodejs/speech/latest/google.cloud.speech.v1p1beta1.html
    encoding = enums.RecognitionConfig.AudioEncoding.OGG_OPUS
    config = {
        "language_code": language_code,
        "sample_rate_hertz": sample_rate_hertz,
        "encoding": encoding,
    }
    name_mp3 = data_bytes.file_path
    with io.open(name_mp3, "rb") as f:
        content = f.read()
    audio = {"content": content}

    response = client.recognize(config, audio)

    # operation = client.long_running_recognize(config, audio)
    # print(operation)
    # print(u"Waiting for operation to complete...")
    # response = operation.result()
    # print('this is response  ')
    answer = "Не удалось распознать сообщение"
    os.remove(name_mp3)
    for result in response.results:
        # print(result)
        # First alternative is the most probable result
        alternative = result.alternatives[0]
        answer = alternative.transcript
        # print(u"Transcript: {}".format(alternative.transcript))
    await message.reply(f'{answer}')
