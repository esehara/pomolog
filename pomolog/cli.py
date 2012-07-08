# -*- coding: utf-8 -*-
if __name__ == "__main__":
    import lib
else:
    import pomolog.lib as lib
import argparse
import re
import time
import commands

def begin():
    parser = argparse.ArgumentParser(description='''!!! POMOLOG !!!
Pomodolo Toolkid for CUI''')
    subparsers = parser.add_subparsers(
            help='sub-commands')
    param_start = subparsers.add_parser(
            'start'
            ,help='Pomolog Start')
    param_start.add_argument('config'
            ,help='Pomolog Setting File(YAML)')
    param_start.set_defaults(func=start)
    cmd = parser.parse_args()
    print('Hello :) POMOLOG !!\n')
    conf = lib.load_configure(cmd.config)
    cmd.func(conf)

def start(conf):
    print("-" * 6)
    taskname = ""
    while taskname == "":
        print("""Input Task Name""")
        taskname = raw_input(">>>")
    print("-" * 6)
    set_timer = what_time(conf['default']['min'])
    print("=" * 24)
    print("set time -> %i min" % set_timer)
    timer = lib.pomotimer(time.time(),set_timer,conf['log'])
    timer.set_taskname(taskname)
    timer.write_log(lib.log_string(lib.date_for_log(),"[START]" + taskname))
    
    if conf['pre_command'] is not None and 'start' in conf['pre_command']:
        commands.getoutput(conf['pre_command']['start'])

    timer.start("""=== POMOLOG START!! ===""")
    
    if conf['pre_command'] is not None and 'done' in conf['pre_command']:
        commands.getoutput(conf['pre_command']['done'])
    
    print("Rest Time. :)")
    set_timer = what_time(conf['default']['rest'])
    timer = lib.pomotimer(time.time(),set_timer,conf['log'])
    timer.set_taskname("Rest")
    timer.start("""=== REST START ===""")
    
    print("One More Time ?")
    yes_or_not = raw_input("[Y,n] >>>")
    if yes_or_not != "n" and yes_or_not != "N":
        start(conf)
    else:
        print("see you ;)")
        exit()

def what_time(def_time):
    print("""What min?""")
    print("Default time is %i" %(def_time))
    print("")
    inp = raw_input("Input [D(efault) or Time(0..30 or more)]>>>")
    if re.match("^[0-9]+$",inp):
        return int(inp)
    elif inp == "D" or inp == "":
        return def_time
    else:
        return what_time(def_time)

if __name__ == "__main__":
    class test_data:
        def __init__(self,filepath):
            self.config = lib.load_configure(filepath)
    cmd = test_data('../sample/config.yaml')
    start(cmd.config)
