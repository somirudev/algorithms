class Gap_buffer:
    def __init__(self, size=10):
        self.default = "_"
        self.increment = size
        self.buffer = [self.default] * self.increment
        self.gap_start = 0
        self.gap_end = self.increment - 1

    # moves the gap by index_change amount by shifting elements over the gap one by one
    def move_cursor(self, index_change):
        # move gap left one at a time
        if index_change > 0:
            shift_amount = min(index_change, len(self.buffer) - self.gap_end - 1)
            for i in range(shift_amount):
                self.buffer[self.gap_start] = self.buffer[self.gap_end + 1]
                self.buffer[self.gap_end + 1] = self.default
                self.gap_start += 1
                self.gap_end += 1
        # move gap right one at a time
        elif index_change < 0:
            shift_amount = min(abs(index_change), self.gap_start)
            for i in range(shift_amount):
                self.buffer[self.gap_end] = self.buffer[self.gap_start - 1]
                self.buffer[self.gap_start - 1] = self.default
                self.gap_start -= 1
                self.gap_end -= 1

    # handles inserting a text string by breaking it up per character
    def insert(self, text):
        for char in str(text):
            self._insert_char(char)

    # inserts char at gap start and enlarges buffer if there is no gap
    def _insert_char(self, char):
        if self.gap_start == self.gap_end:
            self._enlarge_buffer()
        self.buffer[self.gap_start] = char
        self.gap_start += 1

    # increases buffer size by increment
    def _enlarge_buffer(self):
        self.buffer = (
            self.buffer[: self.gap_start]
            + [self.default] * self.increment
            + self.buffer[self.gap_end + 1 :]
        )
        self.gap_end = self.gap_start + self.increment - 1

    # deletes amount of characters before the gap by moving gap start amount spaces back (doesn't actually overwrite the values)
    def delete(self, amount):
        if self.gap_start - amount >= 0:
            self.gap_start -= amount
        else:
            self.gap_start = 0

    def __iter__(self):
        index = 0
        while index < len(self.buffer):
            if self.gap_start <= index <= self.gap_end:
                index += 1
                continue
            yield self.buffer[index]
            index += 1

    def __repr__(self):
        return f"{self.buffer}"

    def __str__(self):
        return "".join(self)


if __name__ == "__main__":
    gb = Gap_buffer()
    text = "Hello World"
    print(f"inserting '{text}'")
    gb.insert(text)
    print(gb)
    print(repr(gb))
    movement = -4
    print(f"Moving cursor by {movement}")
    gb.move_cursor(movement)
    print(gb)
    print(repr(gb))
    count = 3
    print(f"deleting {count} elements")
    gb.delete(count)
    print(gb)
    print(repr(gb))
    text = "inserting this many letters should expand the buffersize"
    print(f"inserting '{text}'")
    gb.insert(text)
    print(gb)
    print(repr(gb))
