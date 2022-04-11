# NOTE: There appears to be a line length limit. Exceeding that limit appears
#       to result in silent failure.  Therefore, the key sequences are split
#       across multiple lines.

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values
from adafruit_hid.consumer_control_code import ConsumerControlCode


DELAY_AFTER_SLASH = 0.80 # required so minecraft has time to bring up command screen
DELAY_BEFORE_RETURN = 0.10 # give minecraft time to show all the keys pressed...

PURPLE = 0x800080
GREEN = 0x008000
PALE_BLUE = 0x0A75AD
RED = 0xCC0000
YELLOW = 0xdaa520
NONE = 0x000000

app = {                               # REQUIRED dict, must be named 'app'
    'name' : 'Eralpboard', # Application name
    #
    # /effect <player: target> <effect: Effect>
    #         [seconds: int] [amplifier: int] [hideParticles: Boolean]
    #
    'macros' : [                      # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (PURPLE, 'Obsut', [
            Keycode.LEFT_CONTROL,
            Keycode.SPACE,
            -Keycode.LEFT_CONTROL,
            -Keycode.SPACE,
            DELAY_BEFORE_RETURN,
            'Obsidian',
            Keycode.RETURN,
            ]),
        (GREEN, 'Supot', [
            Keycode.LEFT_CONTROL,
            Keycode.SPACE,
            -Keycode.LEFT_CONTROL,
            -Keycode.SPACE,
            DELAY_BEFORE_RETURN,
            'Spotify',
            Keycode.RETURN,
            ]),
        (PALE_BLUE, 'Telo', [
            Keycode.LEFT_CONTROL,
            Keycode.SPACE,
            -Keycode.LEFT_CONTROL,
            -Keycode.SPACE,
            DELAY_BEFORE_RETURN,
            'Telegram',
            Keycode.RETURN,
            ]),
        # 2nd row ----------
        (RED, 'Vol-', [[ConsumerControlCode.VOLUME_DECREMENT]]),
        (RED, 'Vol+', [[ConsumerControlCode.VOLUME_INCREMENT]]),
        (YELLOW, 'Mute', [[ConsumerControlCode.MUTE]]),
        # 3rd row ----------
        (0x202000, '<<', [[ConsumerControlCode.SCAN_PREVIOUS_TRACK]]),
        (0x002000, 'Play/Pause', [[ConsumerControlCode.PLAY_PAUSE]]),
        (0x202000, '>>', [[ConsumerControlCode.SCAN_NEXT_TRACK]]),
        # 4th row ---------
        (NONE, '', [
            ]),
        (NONE, '', [
            ]),
        (NONE, '', [
            ]),
        # Encoder button --- Remberove all status effects....
        (0x000000, '', [
        ]),
    ]
}
