# -*- coding:utf-8 -*-
import time

def log_string(tp,st):
    return "[%i/%i/%i %i:%i:%i]%s" %(tp[0],tp[1],tp[2],tp[3],tp[4],tp[5],st)

def load_configure(filepath):
    import yaml
    conf = yaml.load(open(filepath))
    if conf['default'] is None:
        conf['default'] = {}
    if 'min' not in conf['default']:
        conf['default']['min'] = 30
    if 'rest' not in conf['default']:
        conf['default']['rest'] = 5
    return conf

def date_for_log():
    tt = time.localtime()
    return (tt.tm_year,tt.tm_mon,tt.tm_mday,tt.tm_hour,tt.tm_min,tt.tm_sec)

class pomotimer:
    def __init__(self,set_time,limit_min,filepath):
        self.set_time = set_time
        self.limit_min = limit_min * 60
        self.filepath = filepath

    def set_taskname(self,taskname):
        self.taskname = taskname

    def is_done_time(self,assert_time):
        return self.set_time + self.limit_min < assert_time

    def what_done_time(self,assert_time):
        return (((self.set_time + self.limit_min) - assert_time) / (60)) + 1

    def print_message(self):
        return "[%s] Done Time ... %i min" %(self.taskname,self.what_done_time(time.time()))

    def start(self,message):
        is_done = False
        print(message)
        while not is_done:
            is_done = self.time_done()
            if is_done:
                print("\nTimer is Done. :) ")
                self.write_log(log_string(date_for_log(),"[Done]" + self.taskname))
            else:
                print("\nTimer is not Done. :(")
                restart_or_end = raw_input("Input [(r)estart,(e)nd] >>>")
                if restart_or_end == "e":
                    self.write_log(log_string(date_for_log(),"[Not done]" + self.taskname))
                    is_done = True
    
    def time_done(self):
        try:
            while not self.is_done_time(time.time()):
                print(self.print_message())
                time.sleep(60)
            return True
        except KeyboardInterrupt:
            return False

    def write_log(self,write_log):
        log_file = open(self.filepath,"a") 
        log_file.write("\n" + write_log)
        log_file.close() 
