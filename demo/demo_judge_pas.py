import judge
import os

basedir = os.path.split(os.path.realpath(__file__))[0]

rundir = basedir+'/demo_judge_pas'
exe_path = rundir+'/main.pas'

if os.path.exists(rundir) == False:
    os.mkdir(rundir)

os.system("cp in ./demo_judge_pas")
os.system("cp aplusb.pas ./demo_judge_pas/main.pas")

res = judge.run_program(
        tl=10,   # time_limit 单位s 
        ml=512, # memory_limit 单位 mb
        ol=128, # output_limit 单位 mb
        sl=1024, # stack limit 单位 mb
        _in="/dev/null",  # 输入文件
        out="compile_out", # 输出文件
        err="compile_err", # 错误输出
        work_path=rundir, # 工作目录
        _type="default", # type default or python3.5
        show_trace_details=False, # 显示详细的信息
        allow_proc=False,         #  允许 fork exec
        unsafe=True,             #  不安全模式
        argv=["/usr/bin/fpc","main.pas"],                  # 运行的程序名
        add_readable_raw=""
        )
print(res)




# res = judge.run_program(
        # tl=1,   # time_limit 单位s 
        # ml=128, # memory_limit 单位 mb
        # ol=128, # output_limit 单位 mb
        # sl=1024, # stack limit 单位 mb
        # _in="in",  # 输入文件
        # out="out", # 输出文件
        # err="stderr", # 错误输出
        # work_path=rundir, # 工作目录
        # _type="python3.5", # type default or python3.5
        # show_trace_details=False, # 显示详细的信息
        # allow_proc=False,         #  允许 fork exec
        # unsafe=False,             #  不安全模式
        # argv=["main.py"],                  # 运行的程序名
        # add_readable_raw=""
        # )
# print(res)
