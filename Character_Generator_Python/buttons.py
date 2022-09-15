class Button:
    def __init__(self,
                 width,
                 height,
                 x1,
                 x2,
                 y1,
                 y2,
                 img1,
                 img2):
        self.img1 = img1
        self.img2 = img2
        self.displayed_img = self.img1
        self.width = width
        self.height = height
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.mouse_over = False


    def update(self, mouse):
        # Check if mouse curser is over the image.
        # If so, change displayed image to alternate,
        # which is brighter.
        if (mouse[0] > self.x1 and mouse[0] < self.x2 and
            mouse[1] > self.y1 and mouse[1] < self.y2):
            self.mouse_over = True
            self.displayed_img = self.img2
        else:
            self.mouse_over = False
            self.displayed_img = self.img1
