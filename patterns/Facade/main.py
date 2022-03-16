
class VideoFile:
  def __init__(self, video_file):
    pass 

class OggCompressionCodec:
  pass  

class MPEG4CompressionCodec:
  pass  

class CodecFactory:
  def __init__(self, file):
    pass 

class BitrateReader:
  def __init__(self, filename, source_codec):
    pass 

  @staticmethod
  def convert(buffer, codec):
    pass 

class File:
  def __init__(self, converted_video):
    pass 

  def save(self):
    pass 

class AudioMixer:
  def fix(self, result):
    pass 

class VideoConverter:
  def convert(self, filename, format):
    file = VideoFile(filename)
    sourceCodec = CodecFactory(file)
    if (format == "mp4"):
      destinationCodec = MPEG4CompressionCodec()
    else:
      destinationCodec = OggCompressionCodec()
    buffer = BitrateReader(filename, sourceCodec)
    result = BitrateReader.convert(buffer, destinationCodec)
    result = AudioMixer().fix(result)
    print(f"converted video to format: {format}")
    return File(result)

class Application:
  def start(self):
    convertor = VideoConverter()
    mp4 = convertor.convert("funny-cats-video.ogg", "mp4")
    mp4.save()

app = Application()
app.start()