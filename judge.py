# coding:utf-8
import subprocess

def run_program_args(
        tl=1,  # time_limit
        ml=128, # memory_limit
        ol=128, # output_limit
        sl=1024, # stack limit
        _in="stdin",
        out="stdout",
        err="stderr",
        work_path="/",
        _type="default", # type
        show_trace_details=False,
        allow_proc=False,
        unsafe=False,
        argv=[],
        add_readable_raw=""
        ):
    cmdline = ''
    cmdline += '--tl='+str(tl)+' '
    cmdline += '--ml='+str(ml)+' '
    cmdline += '--ol='+str(ol)+' '
    cmdline += '--sl='+str(sl)+' '
    cmdline += '--in='+str(_in)+' '
    cmdline += '--out='+str(out)+' '
    cmdline += '--err='+str(err)+' '
    cmdline += '--work-path='+work_path+ ' '
    cmdline += '--type='+ _type+' '
    cmdline += "--add-readable-raw="+add_readable_raw + ' '

    if unsafe:
        cmdline += '--unsafe '

    if show_trace_details:
        cmdline += '--show-trace-details'+' '

    cmdline += ' '.join(argv)
    return cmdline

def run_program(**kwargs):
    # print(kwargs)
    _cmdline = (run_program_args(**kwargs))
    _cmdline = '/judge/ujudge ' + _cmdline
    cmd  = _cmdline.split(' ')
    # print(cmd)
    p=subprocess.Popen(cmd,stdout=subprocess.PIPE)
    out,err = p.communicate()
    _out = out.decode('ASCII').split(' ')
    return {
        "result":int(_out[0]),
        "time":int(_out[1]),
        "memory":int(_out[2]),
        "exit_code":int(_out[3].strip())
        }

RS_AC=0
RS_WA= 1
RS_RE= 2
RS_MLE= 3
RS_TLE= 4
RS_OLE= 5
RS_DGS= 6
RS_JGF= 7
      
if __name__ == '__main__':
    pass

