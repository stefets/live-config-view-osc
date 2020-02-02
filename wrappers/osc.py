"""
/mididings/switch_scene ,i: switch to the given scene number.
/mididings/switch_subscene ,i: switch to the given subscene number.
/mididings/prev_scene: switch to the previous scene.
/mididings/next_scene: switch to the next scene.
/mididings/prev_subscene: switch to the previous subscene.
/mididings/next_subscene: switch to the next subscene.
/mididings/panic: send all-notes-off on all channels and on all output ports.
/mididings/quit: terminate mididings.
"""
from pythonosc import udp_client

class MididingsOsc:

    def __init__(self, _ip='127.0.0.1', _port=56418):
        self.path = '/mididings'
        self.client = udp_client.SimpleUDPClient(_ip, _port)

    def send_message(self, address, value=None):
        self.client.send_message(self.path + address, value if value is not None else None)
