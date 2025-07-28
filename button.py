import cv2

class Button:
    def __init__(self, pos, width, height, value):
        self.pos = pos
        self.width = width
        self.height = height
        self.value = value

    def draw(self, frame, hover=False):
        x, y = self.pos
        color = (0, 255, 0) if hover else (255, 0, 255)
        cv2.rectangle(frame, self.pos, (x + self.width, y + self.height), color, cv2.FILLED)
        cv2.putText(frame, self.value, (x + 20, y + 50), cv2.FONT_HERSHEY_SIMPLEX, 1.4, (255, 255, 255), 3)

    def is_hover(self, x, y):
        bx, by = self.pos
        return bx < x < bx + self.width and by < y < by + self.height
