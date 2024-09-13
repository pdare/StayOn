import ctypes
import time

class StayOnC:

    def runStayOn(self):
        print("running...")
        print('\n')
        time_to_sleep = 10
        count = 0

        while True:
            ctypes.windll.kernel32.SetThreadExecutionState(0x80000002)
            ctypes.windll.kernel32.SetThreadExecutionState(0x80000000)
            count = count + 1
            print("move done, sleeping {}".format(count))
            time.sleep(time_to_sleep * 60)