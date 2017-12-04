import judge
import os

basedir = os.path.split(os.path.realpath(__file__))[0]

rundir = basedir+'/demo_judge_py'
exe_path = rundir+'/main.py'

if os.path.exists(rundir) == False:
    os.mkdir(rundir)


if os.system(" ".join(["python3","-m","py_compile","aplusb.py"])) !=0:
    print('编译失败')
    os.exit(1)

os.system("cp in ./demo_judge_py")
os.system("cp aplusb.py ./demo_judge_py/main.py")

res = judge.run_program(
        tl=1,   # time_limit 单位s 
        ml=128, # memory_limit 单位 mb
        ol=128, # output_limit 单位 mb
        sl=1024, # stack limit 单位 mb
        _in="in",  # 输入文件
        out="out", # 输出文件
        err="stderr", # 错误输出
        work_path=rundir, # 工作目录
        _type="python3.5", # type default or python3.5
        show_trace_details=True, # 显示详细的信息
        allow_proc=False,         #  允许 fork exec
        unsafe=False,             #  不安全模式
        argv=["main.py"],                  # 运行的程序名
        add_readable_raw=""
        )
print(res)
