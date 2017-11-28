#!/usr/bin/env python

class ProgressBar(object):

    def __init__(self, fill=unichr(0x2605), empty_fill=unichr(0x2606), percent=0):
        super(ProgressBar, self).__init__()

        self.fill = fill
        self.empty_fill = empty_fill
		self.percent = percent
        self.reset()

    def __str__(self):
        bar10 = self.percent/10
		bar_left = 10 - bar10
		out = ''
		out = str(self.percent)+'% '
		out = out + unichr(0x2AF7)
		for i in range(bar10):
			out = out+self.fill
		for i in range(bar_left):
			out = out+self.empty_fill
		out = out + unichr(0x2Af8)
        return out

    __repr__ = __str__

    def reset(self):
        """Resets the current progress to the start point"""
        self.progress = float(self.start)
        return self

