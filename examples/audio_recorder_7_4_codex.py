import pyaudio
import time
import queue
import threading as th
import speech_recognition as sr  # pip install SpeechRecognition
import google.cloud.speech as speech  # pip install google-cloud-speech
import io
import argparse



class AudioProducer:
    def __init__(self, chunk_size=1024, format=pyaudio.paInt16, channels=1, rate=16000, queue_size=10, callback=None):
        self.chunk_size = chunk_size  # number of frames per buffer
        self.format = format  # audio format
        self.channels = channels  # number of channels
        self.rate = rate  # sampling rate

        self.p = pyaudio.PyAudio()  # pyaudio object
        self.stream = self.p.open(format=self.format, channels=self.channels, rate=self.rate, input=True, frames_per_buffer=self.chunk_size)  # stream object
        self.callbacks = []
        self.q = queue.Queue(maxsize=queue_size)  # queue to store audio data
        self.lock = th.Lock()  # lock to control access to the queue
        self.stop_event = th.Event()  # event to signal the thread to stop
        self.thread = th.Thread(target=self.run, args=())  # thread to read audio data
        self.thread.daemon = True  # daemonize thread

    def start(self):
        self.thread.start()

    def add_callback(self, callback):
        self.callbacks.append(callback)

    def remove_callback(self, callback):
        self.callbacks.remove(callback)

    def run(self):
        while not self.stop_event.is_set():
            data = self.stream.read(self.chunk_size,False)
            for callback in self.callbacks:
                callback(data)
            with self.lock:
                self.q.put(data)

    def __iter__(self):
        return self

    def read(self):
        with self.lock:  # lock the queue
            if self.q.qsize() > 0:  # if there is data in the queue
                data = self.q.get()  # get the data
                return data
            else:
                return None

                return None

    def __next__(self):
        data = self.read()
        if data is None:
            raise StopIteration
        return data

    def close(self):  # stop the thread
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()
        self.stop_event.set()

    @classmethod
    def parser(cls):

        parser = argparse.ArgumentParser()
        parser.add_argument('--chunk_size', type=int, default=1024)
        parser.add_argument('--format', type=int, default=pyaudio.paInt16)
        parser.add_argument('--channels', type=int, default=1)
        parser.add_argument('--rate', type=int, default=16000)
        parser.add_argument('--queue_size', type=int, default=10)
        return parser

def main(args):
    # try:
        # client = speech.SpeechClient.from_service_account_json('/Users/jianinglu/Downloads/My First Project-d8f9b8f8b8f3.json')
        # config = speech.RecognitionConfig(
        # encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        # sample_rate_hertz=16000,
        # language_code='en-US')
        # streaming_config = speech.StreamingRecognitionConfig(
        # config=config,
        # interim_results=True)

        audio_generator = AudioProducer(chunk_size=args.chunk_size, format=args.format, channels=args.channels, rate=args.rate, queue_size=args.queue_size)
        audio_generator.add_callback(callback)
        audio_generator.start()

        with io.open('output.raw', 'wb') as f:
            for data in audio_generator:
                f.write(data)
    # except Exception as e:
    #     print(e)
    # finally:
    #     audio_generator.close()
    # with io.open('/Users/jianinglu/Downloads/output.raw', 'rb') as audio_file:
    #     content = audio_file.read()
    # audio = speech.types.RecognitionAudio(content=content)
    # response = client.recognize(config, audio)
    # for result in response.results:
    #     print('Finished: {}'.format(result.is_final))
    #     print('Stability: {}'.format(result.stability))
    #     alternatives = result.alternatives
    #     #The alternatives are ordered from most likely to least.
        # for alternative in alternatives:
        #     print('Confidence: {}'.format(alternative.confidence))
        #     print(u'Transcript: {}'.format(alternative.transcript))
#

# def main(args):
#     try:
#         client = speech.SpeechClient.from_service_account_json('/Users/jianinglu/Downloads/My First Project-d8f9b8f8b8f3.json')
#         config = speech.RecognitionConfig(
#         encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
#         sample_rate_hertz=16000,
#         language_code='en-US')
#         streaming_config = speech.StreamingRecognitionConfig(
#         config=config,
#         interim_results=True)
#
#         audio_generator = AudioProducer(chunk_size=args.chunk_size, format=args.format, channels=args.channels, rate=args.rate, queue_size=args.queue_size)
#         audio_generator.start()
#
#         with io.open('/Users/jianinglu/Downloads/output.raw', 'wb') as f:
#             for data in audio_generator:
#                 f.write(data)
#     except Exception as e:
#         print(e)
#     finally:
#         audio_generator.close()
#     with io.open('/Users/jianinglu/Downloads/output.raw', 'rb') as audio_file:
#         content = audio_file.read()
#     audio = speech.types.RecognitionAudio(content=content)
#     response = client.recognize(config, audio)
#     for result in response.results:
#         print('Finished: {}'.format(result.is_final))
#         print('Stability: {}'.format(result.stability))
#         alternatives = result.alternatives
#         # The alternatives are ordered from most likely to least.
#         for alternative in alternatives:
#             print('Confidence: {}'.format(alternative.confidence))
#             print(u'Transcript: {}'.format(alternative.transcript))

def callback(data):
    print(data)



if __name__ == "__main__":
    parser = AudioProducer.parser()
    args = parser.parse_args()
    main(args)


# import pyaudio
# import time
# import queue
# import threading as th
# import speech_recognition as sr  # pip install SpeechRecognition
# import google.cloud.speech as speech  # pip install google-cloud-speech
# # import google.cloud.speech
# # import google.cloud.speech.types as types
# # import google.cloud.speech.enums as enums
# # import google.cloud.storage as storage
# import io
# import argparse
#
#
#
# class AudioProducer:
#     def __init__(self, chunk_size=1024, format=pyaudio.paInt16, channels=1, rate=16000, queue_size=10, callback=None):
#         self.chunk_size = chunk_size  # number of frames per buffer
#         self.format = format  # audio format
#         self.channels = channels  # number of channels
#         self.rate = rate  # sampling rate
#
#         self.p = pyaudio.PyAudio()  # pyaudio object
#         self.stream = self.p.open(format=self.format, channels=self.channels, rate=self.rate, input=True, frames_per_buffer=self.chunk_size)  # stream object
#         self.callbacks = []
#         self.q = queue.Queue(maxsize=queue_size)  # queue to store audio data
#         self.lock = th.Lock()  # lock to control access to the queue
#         self.stop_event = th.Event()  # event to signal the thread to stop
#         self.thread = th.Thread(target=self.run, args=())  # thread to read audio data
#         self.thread.daemon = True  # daemonize thread
#
#     def start(self):
#         self.thread.start()
#         # if callback is not None:
#         #     self.add_callback(callback)
#
#     def add_callback(self, callback):
#         self.callbacks.append(callback)
#
#     def remove_callback(self, callback):
#         self.callbacks.remove(callback)
#
#     def run(self):
#         while not self.stop_event.is_set():
#             data = self.stream.read(self.chunk_size,False)
#             for callback in self.callbacks:
#                 callback(data)
#             with self.lock:
#                 self.q.put(data)
#
#     def __iter__(self):
#         return self
#
#     def read(self):
#         with self.lock:  # lock the queue
#             if self.q.qsize() > 0:  # if there is data in the queue
#                 data = self.q.get()  # get the data
#                 return data
#             else:
#                 return None
#
#                 return None
#
#     def __next__(self):
#         data = self.read()
#         if data is None:
#             raise StopIteration
#         return data
#
#     def close(self):  # stop the thread
#         self.stream.stop_stream()
#         self.stream.close()
#         self.p.terminate()
#         self.stop_event.set()
#
#     @classmethod
#     def parser(cls):
#
#         parser = argparse.ArgumentParser()
#         parser.add_argument('--chunk_size', type=int, default=1024)
#         parser.add_argument('--format', type=int, default=pyaudio.paInt16)
#         parser.add_argument('--channels', type=int, default=1)
#         parser.add_argument('--rate', type=int, default=16000)
#         parser.add_argument('--queue_size', type=int, default=10)
#         return parser
#
#
# def main(args):
#     client = speech.SpeechClient()
#     config = speech.RecognitionConfig(
#         encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
#         sample_rate_hertz=16000,
#         language_code='en-US')
#     streaming_config = speech.StreamingRecognitionConfig(
#         config=config,
#         interim_results=True)
#
#     # audio_generator.add_callback(callback)
#     audio_generator = AudioProducer(chunk_size=args.chunk_size, format=args.format, channels=args.channels, rate=args.rate, queue_size=args.queue_size)
#     audio_generator.start()
#     requests = (speech.StreamingRecognizeRequest(audio_content=content)
#                 for content in audio_generator)
#
#     responses = client.streaming_recognize(streaming_config, requests)
#
#     # Now, put the transcription responses to use.
#     try:
#         for response in responses:
#             # Once the transcription has settled, the first result will contain the
#             # is_final result. The other results will be for subsequent portions of
#             # the audio.
#             for result in response.results:
#                 print('Finished: {}'.format(result.is_final))
#                 print('Stability: {}'.format(result.stability))
#                 alternatives = result.alternatives
#                 # The alternatives are ordered from most likely to least.
#                 for alternative in alternatives:
#                     print('Confidence: {}'.format(alternative.confidence))
#                     print(u'Transcript: {}'.format(alternative.transcript))
#     except Exception as e:
#         print(e)
#     finally:
#         audio_generator.close()
# def callback(data):
#     print(data)
#
#
#
# if __name__ == "__main__":
#     parser = AudioProducer.parser()
#     args = parser.parse_args()
#     main(args)
