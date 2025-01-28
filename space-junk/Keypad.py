#!/usr/bin/env python

import os
import sys
import narrator

from narrator import Checkpoint
from inventory.specs import ItemSpec

class Keypad(ItemSpec):

    consumable = False

    def __init__(self):
        super().__init__(__name__)
        self.entered = None

    def __str__(self):
        prev_code = Checkpoint.check_flag("last_code")
        return f"The last code entered reads: {prev_code}"

    def decode(self, code):
        # TODO: Fix broken keypad
        return decoded

    def use(self):
        self.entered = int(input("Enter code: "))
        Checkpoint.set_flag('last_code', self.entered)
        if self.decode(self.entered) == 2.0:
            for dir in os.listdir():
                if os.path.isdir(dir) and dir.startswith("."):
                    os.rename(
                        dir,
                        "".join(dir.split(".")[1:])
                    )

if __name__ == "__main__":
    keypad = Keypad()
    keypad.use()
