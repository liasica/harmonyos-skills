---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-faqs-operator-development
title: 算子开发常见问题
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > 自定义算子开发 > 算子开发常见问题
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:37+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:937ccc69b423d6cb71d1cf0fd6055190fd2cd15117ab659113192c0e4f9aa750
---

## 核函数运行验证时算子存在精度问题

### 现象描述

在进行算子NPU域的运行验证时，通过md5sum等方式进行算子精度比对，实际数据和真值数据不一致，算子存在精度问题。本示例中通过md5sum来进行精度比对，打印出的真值数据和实际输出数据的md5值不一致，具体打印信息如下。

```
1. md5sum:
2. 45e17ee4c068a655be2af4d8c3a1f191  output/golden.bin
3. 6a99e41a84b14dd04f32730ceb9a3988  output/output_y.bin
```

### 问题根因

算子出现精度问题，一般是由于算子的实现逻辑有误。

### 定位步骤

AscendC提供孪生调试的功能，通过CPU域的功能验证、gdb单步调试、printf数值打印来定位算子的实现逻辑问题。本样例仅展示了可能会出现的场景，便于演示定位步骤。实际使用过程中，请根据代码情况进行调试。

1. 进行CPU域的功能验证，观察是否有日志报错。

   参考[工程化算子开发](cannkit-overview-of-engineering-operator.md)章节，编写CPU侧的运行验证代码，并进行运行验证。得到CPU域的精度比对结果如下。

   ```
   1. md5sum:
   2. 45e17ee4c068a655be2af4d8c3a1f191  output/golden.bin
   3. 5d6e1aec686b28bd3839dbcd5caaa8b2  output/output_y.bin
   ```

   可以看出CPU域的精度比对也存在不一致的问题，然后观察是否有打屏日志报错，可搜索关键词"failed"。比如，下图的报错示例指示，错误出现在代码中调用LeakyRelu接口的地方。

   ```
   1. leakyrelu_custom_cpu: /home/workdir/AscendC/ddk/tikcpp/tikcfw/interface/kernel_operator_vec_binary_scalar_intf.h:447: void AscendC::LeakyRelu(const AscendC::LocalTensor<T>&, const AscendC::LocalTensor<T>&, const T&, const int32_t&) [with T = float16::Fp16T; int32_t = int]: Assertion `false && "check vlrelu instr failed"' failed
   ```

   通过上述报错日志，一般只能定位到报错的代码行，无法明确具体错误，接下来需要通过gdb调试的方式或者printf打印的方式进一步精确定位。
2. gdb调试。下面的样例展示了拉起leakyrelu算子CPU侧运行程序的样例，该样例程序会直接抛出异常，直接gdb运行，查看调用栈信息分析定位即可。其他场景下开发者可以使用gdb打断点等基本操作进行调试。使用gdb调试AscendC程序的详细内容请参考[gdb调试](cannkit-gdb.md)。

   1. 使用gdb拉起待调试程序，进入gdb界面进行debug。

      ```
      1. gdb leakyrelu_custom_cpu
      ```
   2. 单独调试一个子进程。

      ```
      1. (gdb) set follow-fork-mode child
      ```
   3. 运行程序。

      ```
      1. (gdb) r
      ```
   4. 通过bt查看程序调用栈。

      ```
      1. (gdb) bt
      ```
   5. 查看具体层的堆栈信息，打印具体变量的值。本示例中，打印了tileLength为1024，该程序中表示需要处理1024个half类型的数，大小为1024\*sizeof(half)=2048字节；输入Tensor xLocal的值，其中dataLen表示LocalTensor的size大小为1024字节，只能计算1024字节的数据。可以看出两者的长度不匹配，由此可以定位问题。

      ```
      1. (gdb) f 5
      2. #5  0x000055555555d364 in KernelLeakyRelu::Compute (this=0x7fffffffd7d0, progress=0) at /root/AscendC_DemoCode-master/precision-error/vector/leakyrelu_custom.cpp:59
      3. 59              LeakyRelu(yLocal, xLocal, scalar, tileLength);
      4. (gdb) p tileLength
      5. $1 = 1024
      6. (gdb) p xLocal
      7. $1 = {<AscendC::BaseTensor<float16::Fp16T>> = {<No data fields>}, address_ = {logicPos = 9 '\t', bufferHandle = 0x7fffffffd930 "\003\005\377\377", dataLen = 1024,bufferAddr = 0,absAddr = ...}
      ```
3. printf打印。在合适的位置增加变量打印。样例代码如下。

   ```
   1. printf("xLocal size: %d\n", xLocal.GetSize());
   2. printf("tileLength: %d\n", tileLength);
   ```

   可以看到有如下打屏日志输出，打印了tileLength为1024，该程序中表示需要处理1024个half类型的数；输入Tensor xLocal的size大小，为512，表示只能计算512个half类型的数。可以看出两者的长度不匹配，由此可以定位问题。

   ```
   1. xLocal size: 512
   2. tileLength: 1024
   ```

## kernel侧获取Tiling信息不正确

### 现象描述

通过算子在kernel侧实现代码中添加PRINTF打印发现kernel侧获取的Tiling信息不正确。

比如下文样例，增加的打印代码如下。

```
1. PRINTF("tiling_data.totalLength: %d tiling_data.tileNum: %d.\n", tiling_data.totalLength, tiling_data.tileNum);
```

打印的Tiling数据如下，全为0：

```
1. tiling_data.totalLength: 0 tiling_data.tileNum: 0.
```

### 问题根因

kernel侧获取Tiling信息不正确的原因一般有以下两种：

* host侧计算Tiling的逻辑不正确
* kernel侧核函数的参数未按照正确顺序填写

### 处理步骤

1. 参考如下示例，打印TilingData的数据，确认host侧序列化保存的TilingData是否正确。如果此时打印值有误，说明Tiling的计算逻辑可能不正确，需要进一步检查host侧Tiling实现代码，排查计算逻辑是否有误。

   ```
   1. // 按照实际数据类型打印TilingData第一个参数值，如需确认其他值，取值指针向后偏移即可
   2. std::out<<*reinterpret_cast<uint32_t *>(context->GetRawTilingData()->GetData())<<std::endl;
   ```
2. 如果上一步骤中打印的TilingData正确，需要排查kernel侧核函数的参数是否按照正确顺序填写。

   使用msOpGen工具创建算子工程，并基于工程进行kernel侧算子开发时，核函数的定义模板已通过msOpGen工具自动生成，样例如下所示 **。** 参数按照 “输入、输出、workspace、tiling”的顺序排布。请检查是否调整过参数顺序导致和正确顺序不一致。

   ```
   1. #include "kernel_operator.h"
   2. extern "C" __global__ __aicore__ void add_custom(GM_ADDR x, GM_ADDR y, GM_ADDR z, GM_ADDR workspace, GM_ADDR tiling) {
   3. GET_TILING_DATA(tiling_data, tiling);// 获取Tiling参数
   4. // TODO: user kernel impl
   5. }
   ```

## Kernel编译时报错“error: out of jump/jumpc imm range”

### 现象描述

使用工程化算子开发方式，基于自定义算子工程进行算子开发。编译算子时失败，报如下错误：

```
1. [ERROR] [ascendxxxx] PowerCustom_88a695f03edfbc0af76b9eaae9e4556c error: out of jump/jumpc imm range
```

### 问题根因

该编译错误的原因是算子kernel代码过大，导致在编译时跳转指令跳转的偏移值超过了限定的大小（int16\_t的数据范围），可通过添加编译选项“-mllvm -cce-aicore-jump-expand=true”通过间接跳转的方式来避免该问题，让编译器能够正常编译。

### 处理步骤

1. 在kernel侧的CMakeLists中通过add\_ops\_compile\_options针对报错算子添加编译选项“-mllvm -cce-aicore-jump-expand=true”，示例如下。

   ```
   1. add_ops_compile_options(PowerCustom OPTIONS -mllvm -cce-aicore-jump-expand=true)
   ```

   add\_ops\_compile\_options的具体使用方法请参考[支持自定义编译选项](cannkit-operator-project-compilation.md#支持自定义编译选项)。
2. 重新编译该算子。正常编译无报错。

## 有可选输入的情况下，算子编译失败，报找不到DTYPE\_XX

### 现象描述

使用tilingkey设置代码分支时，无法生成对应omc文件。例如onnx模型为2个输入，算子有4个输入x、y、m、n，2个为required和2个optional，tiling key设置为2。

```
1. class KernelAddCustom_omc2 {
2. // ... ...
3. };

5. class KernelAddCustom_omc3 {
6. // ... ...
7. };

9. class KernelAddCustom_omc4 {
10. public:
11. __aicore__ inline KernelAddCustom_omc4() {}
12. __aicore__ inline void Init4(GM_ADDR x, GM_ADDR y, GM_ADDR m, GM_ADDR n, GM_ADDR z, uint32_t totalLength, uint32_t tileNum)
13. {
14. ASSERT(GetBlockNum() != 0 && "block dim can not be zero!");
15. this->blockLength = totalLength / GetBlockNum();
16. this->tileNum = tileNum;
17. ASSERT(tileNum != 0 && "tile num can not be zero!");
18. this->tileLength = this->blockLength / tileNum / BUFFER_NUM;

20. xGm.SetGlobalBuffer((__gm__ DTYPE_X*)x + this->blockLength * GetBlockIdx(), this->blockLength);
21. yGm.SetGlobalBuffer((__gm__ DTYPE_Y*)y + this->blockLength * GetBlockIdx(), this->blockLength);
22. mGm.SetGlobalBuffer((__gm__ DTYPE_M*)m + this->blockLength * GetBlockIdx(), this->blockLength);
23. nGm.SetGlobalBuffer((__gm__ DTYPE_N*)n + this->blockLength * GetBlockIdx(), this->blockLength);
24. zGm.SetGlobalBuffer((__gm__ DTYPE_Z*)z + this->blockLength * GetBlockIdx(), this->blockLength);
25. pipe.InitBuffer(inQueueX, BUFFER_NUM, this->tileLength * sizeof(DTYPE_X));
26. pipe.InitBuffer(inQueueY, BUFFER_NUM, this->tileLength * sizeof(DTYPE_Y));
27. pipe.InitBuffer(inQueueM, BUFFER_NUM, this->tileLength * sizeof(DTYPE_M));
28. pipe.InitBuffer(inQueueN, BUFFER_NUM, this->tileLength * sizeof(DTYPE_N));
29. pipe.InitBuffer(outQueueZ, BUFFER_NUM, this->tileLength * sizeof(DTYPE_Z));
30. }
31. // ... ...
32. private:
33. TPipe pipe;
34. TQue<QuePosition::VECIN, BUFFER_NUM> inQueueX, inQueueY, inQueueM, inQueueN;
35. TQue<QuePosition::VECOUT, BUFFER_NUM> outQueueZ;
36. GlobalTensor<DTYPE_X> xGm;
37. GlobalTensor<DTYPE_Y> yGm;
38. GlobalTensor<DTYPE_M> mGm;
39. GlobalTensor<DTYPE_N> nGm;
40. GlobalTensor<DTYPE_Z> zGm;
41. uint32_t blockLength;
42. uint32_t tileNum;
43. uint32_t tileLength;
44. };

48. extern "C" __global__ __aicore__ void add_custom_omc(GM_ADDR x, GM_ADDR y, GM_ADDR m, GM_ADDR n, GM_ADDR z, GM_ADDR workspace, GM_ADDR tiling) {
49. GET_TILING_DATA(tiling_data, tiling);
50. if (TILING_KEY_IS(2)){
51. KernelAddCustom_omc2 op;
52. op.Init2(x, y, z, tiling_data.size, 4);
53. op.Process2();
54. } else if (TILING_KEY_IS(3)){
55. KernelAddCustom_omc3 op;
56. op.Init3(x, y, m, z, tiling_data.size, 4);
57. op.Process3();
58. }else if (TILING_KEY_IS(4)){
59. KernelAddCustom_omc4 op;
60. op.Init4(x, y, m, n, z, tiling_data.size, 4);
61. op.Process4();
62. }
63. }
```

omg模型转换失败，报错如下。

```
1. ddk/ascendc/ops/impl/custom/add_custom_omc.cpp:165:37: error: unknown type name 'DTYPE_N'
2. nGm.SetGlobalBuffer((__gm__ DTYPE_N*)n + this->blockLength * GetBlockIdx(), this->blockLength);
3. ^
4. ddk/ascendc/ops/impl/custom/add_custom_omc.cpp:169:73: error: use of undeclared identifier 'DTYPE_M'
5. pipe.InitBuffer(inQueueM, BUFFER_NUM, this->tileLength * sizeof(DTYPE_M));
6. ^
```

### 问题根因

模型仅有2个输入x、y的情况下，仅会生成对应的宏DTYPE\_X、DTYPE\_Y，不会生成DTYPE\_M，DTYPE\_N。

### 处理步骤

通过编译宏隔离：

```
1. #if defined (DTYPE_M) && defined (DTYPE_N)
2. class KernelAddCustom_omc4 {
3. // ... ...
4. };
5. #endif
```

## 如何通过gdb启动算子调测工具脚本

### 问题描述

在Linux环境下，开发者需要通过gdb方式开启对算子调测（ascendebug）工具的调试。

### 可能的原因

无

### 处理方案

1. 执行如下命令，获取工具安装路径。

   ```
   1. which ascendebug
   ```

   说明

   一般情况下，ascendebug工具路径缺省为“{INSTALL\_DIR}/tools/tools\_ascendc/package/ascendebug”，其中${INSTALL\_DIR}请替换为DDK软件安装后文件存储路径。
2. 打开ascendebug工具启动脚本（以缺省路径为例）。

   ```
   1. vim ${INSTALL_DIR}/tools/tools_ascendc/package/ascendebug
   ```
3. 在启动脚本中添加gdb调试命令。

   样例如下。

   ```
   1. main() {
   2. check_env $LD_LIBRARY_PATH
   3. ret1=$?
   4. check_env $PATH
   5. ret2=$?
   6. check_env $TOOLCHAIN_HOME
   7. ret3=$?
   8. if [ $ret1 -eq 1 ] || [ $ret2 -eq 1 ] || [ $ret3 -eq 1 ]; then
   9. echo "Please make sure source the correct cann package setenv.bash only. you can open a new window,and restart"
   10. exit 0
   11. fi
   12. export _ASCENDC_DEBUG_TOOL_INSTALL_PATH=${DIR%%latest*}
   13. gdb --ex r --args python3 -m ascendebug.cmd $@
   14. }
   ```

## 环境变量报错提示there are multiple xxx env variable

### 问题描述

使用本工具进行算子功能调测时失败，提示的报错信息如下。

```
1. error: User specified two different cann Installation package path: {PATH_A} and {PATH_B}
2. error: User specified two different cann Installation package path: {PATH_A} and {PATH_B}
3. error: User specified two different cann Installation package path: {PATH_A} and {PATH_B}
4. Please make sure source the correct cann package setenv.bash only. you can open a new window,and restart
```

### 可能的原因

重复设置了环境变量。

### 处理方案

1. 检查当前运行环境中的环境变量（缺省路径为${INSTALL\_DIR}/ddk/tools/tools\_ascendc/set\_ascendc\_env.sh）是否有重复设置。
2. 如果有重复，重新打开一个终端窗口，按照[环境准备](cannkit-environment-preparation.md)章节设置环境变量。

## NPU编译失败提示RuntimeError: Cannot find compile result file

### 问题描述

opc编译方式下，kernel编译报错，如图1所示。

**图1** 报错样例

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/EcUd82UEQF6RHZT9sH7X_A/zh-cn_image_0000002552799606.png?HW-CC-KV=V1&HW-CC-Date=20260427T235135Z&HW-CC-Expire=86400&HW-CC-Sign=F07C095D396BC28409D8A9486E8CAF7EDB37FF98CDBA8946B784C4CCE29148F6)

### 可能的原因

Kernel代码实现有误，导致编译失败。

### 处理方案

1. 设置环境变量。

   在任意终端窗口打开ascendc环境变量文件，缺省路径为“${INSTALL\_DIR}/tools/tools\_ascendc/set\_ascendc\_env.sh”，设置如下变量，放开日志打印等级：

   ```
   1. export ASCEND_GLOBAL_LOG_LEVEL=3         # 设置日志级别为ERROR
   2. export ASCEND_SLOG_PRINT_TO_STDOUT=1     # 开启日志打屏，日志将不会保存在log文件中
   ```
2. 获取日志文件。

   通过命令行方式，日志落盘地址由[Simulator仿真参数](cannkit-cli-parameters.md#simulator仿真参数)接口指定，缺省为当前操作路径的debug\_op.log。请根据实际路径打开日志文件。
3. 截取调测命令，重新执行后再分析。

   1. 在debug\_op.log中找到“opc npu compile start”关键字。
   2. 手动拷贝opc npu compile start后的命令，如图2所示，并在终端窗口执行，通过打屏或者落盘的日志文件进一步分析问题。

      **图2** NPU编译命令

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/9S6cuQn0TPuyi9P4SVhrSQ/zh-cn_image_0000002583439301.png?HW-CC-KV=V1&HW-CC-Date=20260427T235135Z&HW-CC-Expire=86400&HW-CC-Sign=8AEA6100280BD775E758B13A9B88F624E28E686207B8678455B46886045E531F)

## NPU编译失败提示RuntimeError: Cannot get compiling bash file! Maybe template json does not match

### 问题描述

opc编译方式下，kernel编译报错，如图3所示。

**图3** 报错样例

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/H1ZfPXj5SsGSnay5eXALkA/zh-cn_image_0000002552959256.png?HW-CC-KV=V1&HW-CC-Date=20260427T235135Z&HW-CC-Expire=86400&HW-CC-Sign=8C7E81C3742FA750888D98E456D680BFEADE857EF899A999C22DAC74F4A7E36B)

### 可能的原因

开发者输入的算子json配置文件与自定义算子工程的算子json模板配置不一致（如输入/输出的dtype不一样）。

### 处理方案

若调试的算子json模板可变更：

修改开发者输入的算子json配置文件，使其与自定义算子工程的算子json模板配置保持一致。

例如图3 报错样例中，将json中的padding\_mask改为模板对应的pse\_shift。

## 调测失败提示RuntimeError: run output data xxx not found

### 问题描述

执行Kernel显示结束，但最后报错提示没有找到output输出文件。

### 可能的原因

CPU/Simulator的Kernel执行失败，导致输出路径下无输出文件生成。

### 处理方案

1. 设置环境变量。

   在任意终端窗口打开ascendc环境变量文件，缺省路径为“${INSTALL\_DIR}/tools/tools\_ascendc/set\_ascendc\_env.sh”，设置如下变量，放开日志打印等级：

   ```
   1. export ASCEND_GLOBAL_LOG_LEVEL=3         # 设置日志级别为ERROR
   2. export ASCEND_SLOG_PRINT_TO_STDOUT=1     # 开启日志打屏，日志将不会保存在log文件中
   ```
2. 获取日志文件。

   通过命令行方式，日志落盘地址由[NPU调测参数](cannkit-cli-parameters.md#npu调测参数)接口指定，缺省为当前操作路径的debug\_op.log。请根据实际路径打开日志文件。
3. 截取CPU/Simulator调测命令，重新执行后再分析。

   1. 在debug\_op.log中找到“cpu kernel run start”或“npu kernel run start”关键字。
   2. 手动拷贝关键字后的所有命令，在终端窗口分别执行，通过打屏或者落盘的日志文件信息进一步分析问题。

   ```
   1. [CONSOLE] ascendc_debug_tool [3626213] 2024-05-21 19:15:35,513 ==================== cpu kernel run start ====================
   2. [CONSOLE] ascendc_debug_tool [3626213] 2024-05-21 19:15:35,513 execute_cmd: bash -c "cd /home/ascendebug_smoking_test/op_contrib/api_opcontrib_case/ForeachSigmoid/cpu/build && ./foreach_sigmoid_cpu | tee -a /home/ascendebug_smoking_test/op_contrib/api_opcontrib_case.log && cd -"
   3. cpu run start
   ```

   ```
   1. [CONSOLE] ascendc_debug_tool [3626213] 2024-05-21 19:15:36,046 ==================== npu kernel run start ====================
   2. [CONSOLE] ascendc_debug_tool [3626213] 2024-05-21 19:15:36,046 /home/run_pkg/latest/toolkit/tools/ascendc_tools/npu_kernel_launch/npu_kernel_launch --kernel /home/ascendebug_smoking_test/op_contrib/data/op-contrib/build_out/binary/${chip_version}/bin/foreach_sigmoid/ForeachSigmoid_0885a6586f8e7f8dc8d03c4dabc73ef4_high_performance.o --name ForeachSigmoid --json_file /home/ascendebug_smoking_test/op_contrib/api_opcontrib_case/ForeachSigmoid/data/ForeachSigmoid.json --input_path /home/ascendebug_smoking_test/op_contrib/api_opcontrib_case/ForeachSigmoid/data --output_path /home/ascendebug_smoking_test/op_contrib/api_opcontrib_case/ForeachSigmoid/npu/output --tiling_data /home/ascendebug_smoking_test/op_contrib/api_opcontrib_case/ForeachSigmoid/tiling/tiling_data_tiling_key_1_block_dim_1_workspace_33554432.bin --tiling_key 1 --workspace 33554432 --block_dim 1 --timeout 600 --device 0 --core_type VectorCore --arg_lib /home/ascendebug_smoking_test/op_contrib/api_opcontrib_case/ForeachSigmoid/npu/build/launch_args.so
   3. kernel name: ForeachSigmoid
   4. kernel file: /home/ascendebug_smoking_test/op_contrib/data/op-contrib/build_out/binary/${chip_version}/bin/foreach_sigmoid/ForeachSigmoid_0885a6586f8e7f8dc8d03c4dabc73ef4_high_performance.o
   5. json file: /home/ascendebug_smoking_test/op_contrib/api_opcontrib_case/ForeachSigmoid/data/ForeachSigmoid.json
   6. // ...
   ```

## 使能打印功能后提示block info is not valid, skip this block

### 问题描述

开启printf/PRINTF/DumpTensor/DumpAccChkPoint/assert打印功能后，代码执行出现block info is not valid, skip this block，无打印信息。

### 可能的原因

打印DumpTensor的代码未在报错核中执行 （以CPU调测为例，如图4所示，block32~70 的核没有执行Dump和Print操作），后续解析对应.bin时无法获取该核对应的数据，因此该block的数据无效，打印跳过。

**图4** 报错样例

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/PFJd4KvgTxeW_6TDCFLSZQ/zh-cn_image_0000002583479257.png?HW-CC-KV=V1&HW-CC-Date=20260427T235135Z&HW-CC-Expire=86400&HW-CC-Sign=EA30648744D3354B55178A856538B932998531C34EA3365CB8757ED43A440B2C)

### 处理方案

请自行检查算子实现代码，确保printf/PRINTF/DumpTensor/DumpAccChkPoint/assert已执行到该核中。

## 调试Kernel代码时打印错误或者无打印信息

### 问题描述

调试Kernel代码时虽开启了打印功能，但无论如何修改代码，总是打印错误甚至无打印。

### 可能的原因

* 算子Kernel代码执行过程中异常退出，无打印信息。
* 上一次执行日志未清理，真值比对和Dump解析模块按照其路径读取了残留文件，输出了错误的值。

### 处理方案

1. 先清理系统中残留的日志文。

   请根据实际情况清理上一次生成的调测结果目录（由--work-dir参数指定），包括落盘的日志文件（缺省为当前操作路径的debug\_op.log）。
2. 重新进行CPU/Simulator调测。
3. 查看最新生成的日志文件，根据提示的warning、error日志进一步分析问题。

## CPU/Simulator调测的精度比对结果部分为0

### 问题描述

CPU/Simulator调测生成的精度比对结果文件出现“Failed”，部分输出为0，结果如图5所示。

**图5** 精度比对结果文件

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/IfutSjcYTeevbxyNT2LutQ/zh-cn_image_0000002552799608.png?HW-CC-KV=V1&HW-CC-Date=20260427T235135Z&HW-CC-Expire=86400&HW-CC-Sign=88B099765F8192C17CD4A978682CDCD6706D92B9ADCCC1BD1756F7F6B7B3D9E0)

### 可能的原因

算子指定的block num没有跑满，导致部分输出为0。

### 处理方案

检查Tiling文件中设置的block num或者检查--block-num参数配置是否合理，请保证该值满足算子计算业务的需求。

## 如何通过查看Tiling日志定位问题

### 问题描述

Tiling调测过程中提示报错，需要通过日志进一步定位问题。

### 可能的原因

Tiling函数代码实现有误或者输入配置有误（如数据、算子json配置文件等）。

### 处理方案

1. 获取日志文件。

   通过命令行方式，日志落盘地址由[NPU调测参数](cannkit-cli-parameters.md#npu调测参数)接口指定，缺省为当前操作路径的debug\_op.log。请根据实际路径打开日志文件。
2. 截取Tiling调测命令，重新执行，根据提示进一步定位Tiling代码问题。

   1. 在debug\_op.log中找到“gen\_tiling\_data\_cmd”关键字。
   2. 手动拷贝gen\_tiling\_data\_cmd后的所有命令，在终端窗口执行，通过打屏或者落盘的日志文件进一步分析问题。

   说明

   执行命令之前，请确保当前终端[环境准备](cannkit-environment-preparation.md)设置并生效。

   ```
   1. [CONSOLE] ascendc_debug_tool [4149480] 2024-06-03 15:57:42,364 ==================== generate tiling data start ====================
   2. [CONSOLE] ascendc_debug_tool [4149480] 2024-06-03 15:57:42,364 gen_tiling_data_cmd:
   3. /home/install_daily/latest/toolkit/tools/ascendc_tools/ascendc_tiling_tool /home/install_daily/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64/liboptiling.so FlashAttentionScore ${chip_version} /home/ascendebug_smoking_test/ops_adv/adt_biprof/FlashAttentionScore/tiling/tiling_data.bin /home/ascendebug_smoking_test/ops_adv/adt_biprof/FlashAttentionScore/tiling/tiling_run_info.bin /home/ascendebug_smoking_test/ops_adv/adt_biprof/FlashAttentionScore/tiling/inputs.json /home/ascendebug_smoking_test/ops_adv/adt_biprof/FlashAttentionScore/tiling/outputs.json /home/ascendebug_smoking_test/ops_adv/adt_biprof/FlashAttentionScore/tiling/attrs.json
   4. [CONSOLE] ascendc_debug_tool [4149480] 2024-06-03 15:57:42,917 ==================== generate tiling data end, takes 552974.0(us) ====================
   ```

## CAModel仿真过慢导致运行失败

### 问题描述

使用CAModel进行算子性能仿真时，发现运行时间较长，直至调测失败。

### 可能的原因

* 硬件资源有限，多任务抢占资源，导致CAModel运行缓慢。
* 硬件性能不足以支撑算子仿真计算。
* 算子的输入/输出Shape过大，导致CAModel仿真耗时激增。
* CAModel仿真参数设置不合理，如block num取值过大。

### 处理方案

* 建议1：尽可能避免多个任务同时抢占硬件资源，保障CAModel主任务运行效果。
* 建议2：提高硬件性能，尽量满足如下要求：

  + 服务器：X86物理服务器或者计算云（暂支持x86）
  + CPU核数：建议大于16核
  + 内存：建议大于64GB
  + 硬盘：建议大于2T
* 建议3：适当调小算子的输入/输出Shape，降低仿真数据量。
* 建议4：请参考[Simulator仿真参数](cannkit-cli-parameters.md#simulator仿真参数)设置CAModel仿真参数，如block num建议设置为1。
