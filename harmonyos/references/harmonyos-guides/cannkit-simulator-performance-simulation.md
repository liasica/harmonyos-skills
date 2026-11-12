---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-simulator-performance-simulation
title: Simulator仿真功能
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 自定义算子开发 > AscendC算子开发 > AscendC算子调试调优 > AscendC调测调优功能 > Simulator仿真功能
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:42+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:ca842baf6489b2ca8fead19fe964766d1d0fbb6009358b6543ae90639dadee1c
---

## CAModel性能仿真

### 功能介绍

算子可以在仿真器上进行性能仿真，目前主要支持CAModel仿真器。

CAModel仿真器基于一系列host侧的so（动态共享库）实现算子运行过程的仿真，可以通过**算子直调工程**和**mskl调测工具**两种方式，使算子的程序依赖仿真器的动态共享库，接入仿真器，输出算子执行结果。

### 准备工作

请参考[鸿蒙社区cannkit开发准备](cannkit-preparations.md)

### 使用方法-算子直调工程

完整的样例工程请下载[鸿蒙CANN社区recipe仓算子直调样例工程](https://gitcode.com/cann/cann-recipes-harmony-infer/tree/master/ops/ascendc/AddKernelInvocation)

算子直调工程通过CMake编译生成可执行程序，在仿真模式下链接CAModel仿真器的动态共享库，从而在Host侧完成算子的功能验证与性能仿真。下面以Add算子样例为例，介绍工程的结构与运行步骤。

说明：

准备工作仍参考本篇文档“准备工作”一节的CANN包，请忽略上述样例工程中的README.md，仅下载工程代码。

**目录结构**

样例工程的目录结构如下：

```text
├── AddKernelInvocation
│   ├── cmake                   // 编译工程文件
│   ├── input                   // 存放脚本生成的输入数据目录
│   ├── output                  // 存放算子运行输出数据和真值数据的目录
│   ├── scripts
│   │   ├── acl.json            // acl配置文件
│   │   ├── gen_data.py         // 生成输入数据与真值数据的脚本
│   │   ├── verify_result.py    // 真值对比文件
│   ├── add_custom.cpp          // 算子kernel实现，暴露给main.cpp调用
│   ├── CMakeLists.txt          // 编译工程文件
│   ├── data_utils.h            // 数据读入写出函数
│   ├── main.cpp                // 主函数，调用算子的应用程序，含CPU域及NPU域调用
│   ├── run.sh                  // 编译运行算子的脚本
```

**操作步骤**

1. 进入样例工程目录。

   ```bash
   cd AddKernelInvocation
   ```
2. 执行如下命令编译并运行样例算子。

   ```bash
   bash run.sh -r [RUN_MODE] -v [SOC_VERSION]
   ```

   参数说明：

   * RUN\_MODE：编译运行方式。仿真场景请填写sim（NPU仿真）。
   * SOC\_VERSION：芯片型号，当前支持KirinX90或Kirin9030。

   以 KirinX90 仿真为例：

   ```bash
   bash run.sh -r sim -v KirinX90
   ```
3. run.sh 脚本会自动完成以下操作：

   * 生成输入数据与真值数据（scripts/gen\_data.py）。
   * 通过 CMake 编译生成仿真可执行文件（如add\_sim）。
   * 运行可执行文件，输出结果保存到output/目录。
   * 根据输入的[SOC\_VERSION]字段，自动链接对应SoC的仿真器so
   * 调用scripts/verify\_result.py将输出结果与真值进行比对。
4. 若终端输出 test pass，说明算子仿真运行结果与真值一致，功能验证通过。

**仿真模式下的动态库依赖说明**

在仿真模式（RUN\_MODE=sim）下，run.sh脚本会自动设置LD\_LIBRARY\_PATH，将仿真器的动态共享库路径加入搜索路径，无需用户手动配置。相关代码片段如下：

```bash
export LD_LIBRARY_PATH=$_ASCEND_INSTALL_PATH/x86_64-linux/simulator/${_SOC_VERSION}/lib:$LD_LIBRARY_PATH
```

其中$\_ASCEND\_INSTALL\_PATH为CANN安装路径（优先取自ASCEND\_TOOLKIT\_HOME或ASCEND\_HOME\_PATH环境变量，若未设置则默认使用$HOME/Ascend/ascend-toolkit/latest或/usr/local/Ascend/ascend-toolkit/latest）。仿真模式下CAModel仿真器所依赖的libascendcl等动态库已包含在该路径下。

如需保留仿真器中间态的dump log，可在运行前手动设置CAMODEL\_LOG\_PATH环境变量指定输出路径（目录需提前创建），否则脚本默认使用./sim\_log并在每次运行前清空。

**替换为自定义算子**

如需将该样例工程替换为自己的算子实现，需要修改以下内容：

1. **add\_custom.cpp**：整个文件替换为新算子的kernel实现。
2. **run.sh**：根据实际算子名修改FILE\_NAME属性（控制编译获得的二进制名）。
3. **scripts/gen\_data.py**：自定义生成输入数据的内容（Shape、数据类型、算子输入参数数量）。
4. **main.cpp**：修改调用add\_custom.cpp中暴露的符号、读数据的逻辑，使其与新算子保持一致。

### 使用方法-mskl调测工具

mskl调测工具提供了一组Python接口，开发者无需依赖ACLNN框架，即可在Python脚本中快速实现Kernel的下发、编译与运行，适用于算子的Tiling逻辑验证与功能验证。

说明：

* 当前Kirin芯片仅支持 simulator（仿真）模式。
* 使用mskl前需先完成算子工程准备并执行 build\_and\_install.sh 将算子部署到CANN环境。

**前提条件**

已拷贝[样例单算子工程](https://gitcode.com/cann/cann-recipes-harmony-infer/tree/master/ops/ascendc/src/add_custom)完成算子工程准备，并执行build\_and\_install.sh完成算子部署。

**操作步骤**

1. 进入算子工程目录。

   ```bash
   cd ~/add_custom
   ```
2. 创建启动脚本run\_mskl.sh，内容如下：

   ```shell
   soc_version=KirinX90
   export LD_PRELOAD=${ASCEND_HOME_PATH}/tools/msopt/bin/lib64/libstdc++.so.6
   export LD_LIBRARY_PATH=${ASCEND_TOOLKIT_HOME}/lib64:${ASCEND_TOOLKIT_HOME}/tools/msopt/bin/lib64/:${ASCEND_TOOLKIT_HOME}/x86_64-linux/simulator/${soc_version}/lib/:${LD_LIBRARY_PATH}
   python3 mskl_demo.py
   ```

   该脚本会设置LD\_LIBRARY\_PATH，将CANN动态库、msopt动态库与仿真器动态库路径加入搜索路径，确保mskl能正确加载仿真器与算子依赖。
3. 创建Python调用脚本mskl\_demo.py，内容如下：

   ```python
   import os
   import numpy as np
   import mskl

   CANN_ROOT = os.environ.get('ASCEND_HOME_PATH', '/usr/local/Ascend/cann')
   KERNEL_BINARY_PATH = os.path.join(CANN_ROOT, 'opp/vendors/customize/op_impl/ai_core/tbe/kernel/kirinx90/add_custom/AddCustom_99ac61bdd243ff8d84b87c4ff0c51889.o')
   TILING_LIB_PATH = os.path.join(CANN_ROOT, 'opp/vendors/customize/op_impl/ai_core/tbe/op_tiling/liboptiling.so')

   a = np.random.randint(1, 5, (8, 4096)).astype(np.float16)
   b = np.random.randint(1, 5, (8, 4096)).astype(np.float16)
   c = np.zeros((8, 4096), dtype=np.float16)
   golden = (a + b).astype(np.float16)

   out = mskl.tiling_func(op_type='AddCustom', inputs=[a,b], outputs=[c], lib_path=TILING_LIB_PATH, attr={'bias':0}, soc_version='KirinX90')
   kernel = mskl.get_kernel_from_binary(KERNEL_BINARY_PATH)
   kernel(a, b, c, out.workspace, out.tiling_data, device_id=0)
   result = 'success' if np.array_equal(c, golden) else 'failed'
   print(f'compare {result}.')
   ```
4. 根据实际部署路径，修改mskl\_demo.py中的两个路径变量。

   查询Kernel二进制文件（.o 文件）的绝对路径，填入KERNEL\_BINARY\_PATH：

   ```shell
   find $ASCEND_HOME_PATH -name *AddCustom*o
   ```

   查询Tiling动态库（liboptiling.so）的绝对路径，填入TILING\_LIB\_PATH：

   ```shell
   find $ASCEND_HOME_PATH -path */customize/* -name liboptiling.so
   ```
5. 执行脚本，调用算子。

   注意：

   请在成功部署算子到CANN后再调用，否则会报错。

   ```shell
   sh run_mskl.sh
   ```

   执行成功后，输出如下：

   ```text
   $ sh run_mskl.sh
   ...
   compare success.
   [DIGITAL_NPU] [rtDevBinaryUnRegister:634] enter Function>>>
   [DIGITAL_NPU] [rtFree:56] enter Function>>>
   ```

   若输出compare success.，说明算子仿真运行结果与真值一致，功能验证通过。

**常见问题**

运行过程中如遇到如下日志报错：

```text
init_logger Failed to init log:
```

该日志不影响mskl的执行结果，仅表示仿真器不会保存中间态dump log。如需保存仿真器中间态dump log，可手动设置环境变量指定dump路径（目录需提前创建）：

```shell
export CAMODEL_LOG_PATH=XXX
```
