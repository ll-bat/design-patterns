class Player:
    state = None

    def __init__(self):
        self.state = ReadyState(self)

    def change_state(self, state):
        self.state = state

    def click_play(self):
        self.state.click_play()

    def click_lock(self):
        self.state.click_lock()

    def start_playback(self):
        print('started playback')

    def stop_playback(self):
        print('stopped playback')

    @property
    def is_playing(self):
        return False


class State:
    player = None

    def __init__(self, player):
        self.player = player

    def click_play(self):
        pass

    def click_lock(self):
        pass


class ReadyState(State):
    def click_play(self):
        self.player.start_playback()
        self.player.change_state(PlayingState(self.player))

    def click_lock(self):
        self.player.change_state(LockedState(self.player))


class PlayingState(State):
    def click_play(self):
        self.player.stop_playback()
        self.player.change_state(ReadyState(self.player))

    def click_lock(self):
        self.player.change_state(LockedState(self.player))


class LockedState(State):
    def click_play(self):
        pass

    def click_lock(self):
        if not self.player.is_playing:
            self.player.change_state(ReadyState(self.player))


class App:
    def init(self):
        player = Player()
        player.click_play()
        player.click_lock()
        player.click_lock()
        player.click_play()
        player.click_play()


app = App()
app.init()
