## ujudge

提取自uoj_judge

 - 使用平台:`ubuntu 16.04`
 - 支持`python3.5`,`c`,`c++`,`free pascal`


## 安装

```
mkdir build
cd build && cmake .. && make && sudo make install
```

## 使用方法

python3 调用
```python
import judge

judge.run_program(
        tl=1,   # time_limit 单位s 
        ml=128, # memory_limit 单位 mb
        ol=128, # output_limit 单位 mb
        sl=1024, # stack limit 单位 mb
        _in="stdin",  # 输入文件
        out="stdout", # 输出文件
        err="stderr", # 错误输出
        work_path="/", # 工作目录
        _type="default", # type default or python3.5
        show_trace_details=False, # 显示详细的信息
        allow_proc=False,         #  允许 fork exec
        unsafe=False,             #  不安全模式
        argv=[],                  # 运行的程序名
        add_readable_raw=""
)
```

返回值如下:

```
{
    "result":0,  # 运行结果
    "time":123,  # 运行时间 单位 ms
    "memory":    # 内存     单位 kb
    "exit_code": # 退出码
}
```

`result`值的含义
```
RS_AC=0     成功
RS_WA= 1    不会返回这个值
RS_RE= 2    运行时错误
RS_MLE= 3   超内存
RS_TLE= 4   超时
RS_OLE= 5   超输出大小
RS_DGS= 6   包含危险行为
RS_JGF= 7   ?
```

### 通过shell参数调用

```bash
/jduge/ujudge --tl=3 \
--ml=128 \
--ol=128 \
--sl=128 \
--in=1.in \
--out=1.out \
--err=err \
--work-path=path \
--type=default \
--unsafe \
--show-trace-details
```


## 评测python3 文件

看demo下的`demo_judge_py3.py`

## 测试

```bash
cd tests/Python_and_core
python3 -B test.py
```

