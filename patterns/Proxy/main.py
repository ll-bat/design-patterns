

class YoutubeLibInterface: 
  def get_video(self, id):
    pass 

  def list_videos(self):
    pass 

  def delete_video(self, id):
    pass  

class YoutubeLib(YoutubeLibInterface):
  def get_video(self, id):
    print("getting a video with id: " + id)

  def list_videos(self):
    print("getting videos")

  def delete_video(self, id):
    print("deleting video with id: " + id)

class CachedYoutubeLib(YoutubeLibInterface):
  service: YoutubeLibInterface = None
  cached_videos = dict()
  listed_videos = None
  deleted_videos = dict()
  
  def __init__(self, service: YoutubeLibInterface):
    self.service = service 
    
  def get_video(self, id):
    if self.cached_videos.get(id, None) is None:
      self.cached_videos[id] = self.service.get_video(id)
    return self.cached_videos[id]

  def list_videos(self):
    if self.listed_videos is None:
      self.listed_videos = self.service.list_videos()
    return self.listed_videos
  
  def delete_video(self, id):
    if self.deleted_videos.get(id, None) is None:
      self.service.delete_video(id)
      self.deleted_videos[id] = True 

class App:
  def init(self):
    service = YoutubeLib()
    proxy = CachedYoutubeLib(service)
    video = proxy.get_video("15")
    print(video)

app = App()
app.init()
