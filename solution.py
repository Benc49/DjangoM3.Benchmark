class KeyCodeDoorLock:
    def __init__(self, comb):
        self.comb = comb
        self.locked = True
        self.fail = 0
        self.h_lock = False

    def is_locked(self):
        return self.locked

    def is_hard_locked(self):
        if self.fail == 3:
            self.h_lock = True
            self.locked = True
        else:
            self.h_lock = False

        return self.h_lock

    def enter_code(self, code):
        if self.h_lock == False:
            if self.comb == code:
                self.locked = False
                self.fail = 0
            else:
                self.locked = True
                self.fail += 1

    def reset(self, new):
        if self.locked == False:
            self.comb = new
            self.locked = True

    def lock(self):
        self.locked = True


        



