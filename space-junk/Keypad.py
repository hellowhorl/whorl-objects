import os
import sys
import narrator

from narrator import Checkpoint
from inventory.specs import ItemSpec

class Keypad(ItemSpec):

    consumable = False

    def __init__(self):
        super().__init__(__name__)

    def decode(self, code):
        #
        # TODO: Fix the keypad according to the
        #       instructions left behind!
        #
        return decoded

    def use(self):
        code_entered = int(input("Enter code: "))
        if self.decode(code.entered) == 2.0:
            Checkpoint.set_flag('keycode', True)
            for dir in os.listdir():
                if os.path.isdir(dir) and dir.startswith("."):
                    os.rename(
                        dir,
                        "".join(dir.split(".")[1:])
                    )

if __name__ == "__main__":
    keypad = Keypad()
    keypad.use()
