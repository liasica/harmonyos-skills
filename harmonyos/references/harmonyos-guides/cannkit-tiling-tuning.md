---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tiling-tuning
title: Tiling调测功能
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 自定义算子开发 > AscendC算子开发 > AscendC算子调试调优 > AscendC调测调优功能 > Tiling调测功能
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:42+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:9bf7d4280cdae31e8d8678be0a9e11aa10ac228954e80f9d62ca7be597f3d3be
---

## 功能介绍

Tiling是算子开发中独立且关键的部分，描述了Kirin AI处理器SoC NPU IP加速器上算子的输入/输出数据切分、分块计算、多核并行等策略，以满足片上存储限制和计算pipeline的需求，最大化计算并行性和数据局部性(data locality OR data reuse)，从而发挥硬件的极致性能。

对单算子执行Tiling调测时，根据Tiling so文件执行Tiling运算，生成Tiling结果。

**说明** 

目前仅标准自定义算子工程场景、ops\_adv算子工程场景、built-in工程场景、内源框架工程场景需要进行Tiling调测，其余场景不涉及。

## 准备工作

请参考[鸿蒙社区CANN Kit开发准备](cannkit-preparations.md)

## 使用方法

当前Tiling调测通过mskl调测工具的mskl.tiling\_func接口完成。开发者可在Python脚本中轻量化调用Tiling函数，无需依赖ACLNN框架。

mskl调测工具的完整用法，请参考[Simulator仿真功能—使用方法-mskl调测工具](cannkit-simulator-performance-simulation.md#使用方法-mskl调测工具)

说明：

当前Kirin芯片仅支持simulator（仿真）模式。

### mskl.tiling\_func 接口说明

通过mskl.tiling\_func接口，开发者可指定Tiling动态库（.so文件）与算子类型（op\_type），精准调用目标Tiling函数；同时，通过传入inputs、attr等参数，可灵活构造TilingContext，实现无需依赖ACLNN框架的轻量化Tiling调用。

Tiling函数的执行结果包含：

* **blockdim**：核函数启动数量。
* **workspace**：工作空间内存。
* **tiling\_data**：序列化的tiling\_data结构体数据。

上述结果既可用于Tiling逻辑验证，也可作为后续Kernel调用的必要输入。

### 操作步骤

**说明** 

以下步骤假设您已完成 CANN 环境安装、算子工程准备与部署。若尚未完成，请先参考[Simulator仿真功能—使用方法-mskl调测工具](cannkit-simulator-performance-simulation.md#使用方法-mskl调测工具)中的"前提条件"与"操作步骤"。

1. 进入算子工程目录。

   ```bash
   cd ~/ot_demo/workspace/src/add_custom
   ```
2. 创建启动脚本run\_mskl.sh，内容如下：

   ```shell
   soc_version=KirinX90
   export LD_PRELOAD=${ASCEND_HOME_PATH}/tools/msopt/bin/lib64/libstdc++.so.6
   export LD_LIBRARY_PATH=${ASCEND_TOOLKIT_HOME}/lib64:${ASCEND_TOOLKIT_HOME}/tools/msopt/bin/lib64/:${ASCEND_TOOLKIT_HOME}/x86_64-linux/simulator/${soc_version}/lib/:${LD_LIBRARY_PATH}
   python3 mskl_tiling_demo.py
   ```

   该脚本会设置LD\_LIBRARY\_PATH，将CANN动态库、msopt动态库与仿真器动态库路径加入搜索路径，确保mskl能正确加载仿真器与算子依赖。
3. 创建Python调用脚本mskl\_tiling\_demo.py，内容如下：

   ```python
   import os
   import numpy as np
   import mskl

   CANN_ROOT = os.environ.get('ASCEND_HOME_PATH', '/usr/local/Ascend/cann')
   TILING_LIB_PATH = os.path.join(CANN_ROOT, 'opp/vendors/customize/op_impl/ai_core/tbe/op_tiling/liboptiling.so')

   # 构造输入数据
   a = np.random.randint(1, 5, (8, 4096)).astype(np.float16)
   b = np.random.randint(1, 5, (8, 4096)).astype(np.float16)
   c = np.zeros((8, 4096), dtype=np.float16)

   # 调用Tiling函数
   out = mskl.tiling_func(
       op_type='AddCustom',
       inputs=[a, b],
       outputs=[c],
       lib_path=TILING_LIB_PATH,
       attr={'bias': 0},
       soc_version='KirinX90'
   )

   # 查看Tiling结果
   print(f'blockdim: {out.blockdim}')
   print(f'workspace size: {len(out.workspace)}')
   print(f'tiling_data size: {len(out.tiling_data)}')
   ```
4. 根据实际部署路径，修改mskl\_tiling\_demo.py中的Tiling动态库路径。执行以下命令查询liboptiling.so的绝对路径，填入TILING\_LIB\_PATH。

   ```shell
   find $ASCEND_HOME_PATH -path */customize/* -name liboptiling.so
   ```
5. 执行脚本。

   注意：

   请在成功部署算子到CANN后再调用，否则会报错。

   ```shell
   sh run_mskl.sh
   ```

   执行成功后，终端会输出Tiling结果的关键信息：

   ```text
   $ sh run_mskl.sh
   ...
   blockdim: 1
   workspace size: 0
   tiling_data size: 64
   ```

   开发者可据此验证Tiling逻辑是否正确，例如blockdim是否符合预期，workspace大小是否合理等。

### Tiling 结果说明

mskl.tiling\_func的返回值是一个包含以下字段的对象：

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| blockdim | int | 核函数启动数量，即数据切分后使用的核数。 |
| workspace | bytes | 工作空间内存，供Kernel运行时使用。 |
| tiling\_data | bytes | 序列化的tiling\_data结构体数据，包含数据切分、分块计算等策略信息，是后续Kernel调用的必要输入。 |

**说明** 

该返回结果也可作为后续Kernel调用的必要输入，完整的算子仿真调用流程请参考[Simulator仿真功能—使用方法-mskl调测工具](cannkit-simulator-performance-simulation.md#使用方法-mskl调测工具)。
