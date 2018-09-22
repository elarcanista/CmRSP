class Solution:
    def __init__(self, w, y, z):
        self.w = w
        self.y = y
        self.z = z

    def __str__(self):
        return "{w = " + str(self.w) + \
               ", y = " + str(self.y) + \
               ", z = " + str(self.z) + "}"
