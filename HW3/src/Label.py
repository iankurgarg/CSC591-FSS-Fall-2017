import sys
sys.path.append('../HW1/src/')
sys.path.append('../HW2/src/')


"""
Class to store a label information for a discretized bin
"""
class Label(object):
    def __init__(self, most, i):
        self.most = most
        self.label = str(i)

    def __str__(self):
        return "{ 'most'=" + str(self.most) + ", 'label'=" + str(self.label) + "}"