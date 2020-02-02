import sys
from osc import MididingsOsc

def main(args=None):
    osc = MididingsOsc('127.0.0.1', 56418)
    #osc.send_message('/prev_scene')
    #osc.send_message('/next_scene')
    osc.send_message('/switch_scene', 4)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]) or 0)
