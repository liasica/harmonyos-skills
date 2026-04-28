---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-cli-parameters
title: ascendebug调测工具参数说明
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > 自定义算子开发 > 附录 > 调测工具样例与参数说明 > ascendebug调测工具参数说明
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:37+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:eae43339ec80de48f45e32744ddf255cfc948dbd1203c80b02ef58f25c9c4055
---

## 整体说明

可通过**ascendebug -h**或**ascendebug --help**查看工具支持的所有调测模式，具体参见表1。

**表1** 支持的命令行调测模式

| 参数 | 模式说明 | 备注 |
| --- | --- | --- |
| tiling | 主要对算子Tiling代码进行调测，具体参见[Tiling调测功能](cannkit-tiling-tuning.md)。 | 通过**ascendebug tiling -h**或**ascendebug tiling --help**查看Tiling调测涉及的所有参数。 |
| kernel | 主要对Device侧算子Kernel代码进行精度和性能调测，包含CPU、NPU、Simulator调测功能，具体参见[CPU孪生调试功能](cannkit-cpu-twin-debugging.md)、[Simulator性能仿真功能](cannkit-simulator-performance-simulation.md)等章节。 | 通过**ascendebug kernel -h**或**ascendebug kernel --help**查看CPU、NPU、Simulator调测涉及的所有参数。  **说明：** 参数NPU暂不支持。 |
| json | 主要提供数据准备阶段如何生成算子json配置模板，具体参见[算子json配置模板获取](cannkit-obtaining-the-json-configuration.md)。  **说明：** 当前仅适用于标准自定义算子工程场景、built-in工程场景。 | 通过**ascendebug json convert -h**或**ascendebug json convert --help**查看涉及的所有参数。 |
| mc2parse | 预留参数项，开发者无需关注。 | - |
| op\_compiler | 预留参数项，开发者无需关注。 | - |

## Tiling调测参数

| 参数（区分大小写） | 说明 | 是否必选 | 默认值 | 备注 |
| --- | --- | --- | --- | --- |
| tiling | 开启Tiling调测的固定参数。 | 是 | 无 | 无。 |
| --chip-version | Kirin AI处理器的版本。 | 是 | 无。 | 在运行环境上通过命令行获取：  hdc -t {target} shell param get ohos.boot.chiptype  target：设备的SN码，可以通过hdc list targets获取当前环境上所有设备的SN码。 |
| -i，--install-path | CANN软件安装后文件存储路径。 | 否 | 工具自动获取。 | 不支持，开发者无需关注。 |
| -w，--work-dir | 调测结果的存放路径。 | 否 | 缺省为当前执行路径下/debug\_workspace/${op\_type}文件夹（若无则会自动新建）。 | 调测工作目录，可用于存放调测中各种临时文件、结果文件。例如/home/debug\_workspace/AddCustom/tiling。 |
| -j，--json-file | 算子信息json配置文件，配置算子输入/输出/属性信息。 | 是 | 无 | json配置文件必须是绝对路径，其配置项说明详见[输入数据和标杆数据准备](cannkit-preparing-input-data-and-benchmark.md)。 |
| --log-level | 日志级别。 | 否 | info | 支持debug 、info、warning、error级别。 |
| --log-file | 日志文件路径。 | 否 | 缺省值为当前目录下的debug\_op.log文件（若无则会新建）。 | 根据设置的--log-level存放程序执行过程中的日志信息。 |
| --repo-type | 算子开发场景类型。 | 否 | customize | 根据实际情况设置。  - minimalist：核函数直调工程场景。  - customize：标准自定义算子工程。 |
| --customize-path | 自定义算子包的安装目录。 | 否 | 无 | 开发者无需关注，当前固定为${install\_path}/ddk/ tools/tools\_ascendc/custom\_op/${chip-version}。  **说明：** 仅当--repo-type为customize，该参数生效。 |
| --tiling-json | Tiling json文件路径（绝对路径），用于生成自定义Tiling data。 | 否 | 无 | **说明：** 预留参数项，开发者无需关注。 |
| --repo-path | 算子源码仓所在路径（绝对路径）。 | 否 | 无 | **说明：** 预留参数项，开发者无需关注。 |
| --recompile-tiling | 是否重新编译算子Tiling so，无需配置值。 | 否 | 无 | **说明：** 预留参数项，开发者无需关注。 |

## CPU调测参数

| 参数（区分大小写） | 说明 | 是否必选 | 默认值 | 备注 |
| --- | --- | --- | --- | --- |
| kernel | 开启CPU调测功能的固定参数。 | 是 | 无 | 无 |
| -b，--backend | 算子调试类型。 | 否 | npu | CPU调测场景设为cpu。  - cpu：CPU调测场景。  - npu：NPU调测场景。  - simulator：仿真器调测场景。  **说明：** 参数npu暂不支持。 |
| --chip-version | Kirin AI处理器SoCNPU IP加速器的版本。 | 否 | 工具自动获取对应版本。 | 在运行环境上通过命令行获取：  hdc -t {target} shell param get ohos.boot.chiptype  target：设备的SN码，可以通过hdc list targets获取当前环境上所有设备的SN码。 |
| -i，--install-path | ddk安装后文件存储路径。 | 否 | 工具自动获取对应路径 | 不支持，开发者无需关注。 |
| -w，--work-dir | 调测结果的存放路径。 | 否 | 缺省为当前执行路径下/debug\_workspace/${op\_type}文件夹（若无则会自动新建）。 | 调测工作目录，可用于存放调测中各种临时文件、结果文件。例如/home/debug\_workspace/AddCustom/cpu。 |
| -j，--json-file | 算子信息json配置文件，配置算子输入/输出/属性信息。 | 是 | 无 | json配置文件必须是绝对路径，其配置项说明详见[输入数据和标杆数据准备](cannkit-preparing-input-data-and-benchmark.md)。 |
| --log-level | 日志级别。 | 否 | info | 支持debug 、info、warning、error级别。 |
| --log-file | 日志文件路径。 | 否 | 缺省值为当前目录下的debug\_op.log文件（若无则会新建）。 | 根据设置的--log-level存放程序执行过程中的日志信息。 |
| --repo-type | 算子开发场景类型。 | 否 | customize | 根据实际情况设置。  - minimalist：核函数直调工程场景。  - customize：标准自定义算子工程。 |
| --customize-path | 自定义算子包的安装目录。 | 否 | 无 | 开发者无需关注，当前固定为${install\_path}/ddk/ tools/tools\_ascendc/custom\_op/${chip-version}。  **说明：** 仅当--repo-type为customize，该参数生效。 |
| --dump-mode | PRINTF/DumpTensor/DumpAccChkPoint/assert打印功能的模式。 | 否 | 无 | 若不设置表示关闭打印功能，若开启支持如下取值：  normal： 使能通用的打印功能。  更多打印功能说明参见[更多功能](cannkit-commissioning-function-printf.md)。  **说明：** CPU调测场景中printf采用C++自身打印功能，不受**dump-mode**参数控制。 |
| --core-type | 算子类型。 | 否 | AiCore | 根据实际算子情况填写，可选值为AiCore、CubeCore、VectorCore  Kirin9020/KirinX90系列处理器中的算子，一般使用了AI Cube计算单元，其算子类型为AiCore。 |
| --rel-err-thd | 精度比对的相对误差阈值。 | 否 | 0.005 | 无 |
| --abs-err-thd | 精度比对的绝对误差阈值。 | 否 | 0.005 | 无 |
| --block-num | 设置运行的核个数。 | 否 | 无 | 如果有tiling bin文件，则使用其对应的block\_num值，否则根据实际情况自行配置。 |
| --npucheck | npucheck功能开关，提供CPU侧内存校验、异常检测功能。 | 否 | true | - true: 开启内存校验功能。  - false:关闭内存校验功能。  **说明：** 该参数与--dump-mode打印功能冲突，因为打印会对内存做特殊处理。 |
| --tiling-bin | 使用开发者传入的tiling.bin进行编译。 | 否 | 无 | 传入的Tiling bin是带绝对路径的文件名，文件命名规则为tiling\_data\_tiling\_key\_${tiling\_key}block\_dim${block\_num}workspace${workspace}.bin，确保tiling\_key、block\_num、workspace与Tiling bin文件匹配。  **说明：** 该参数与--tiling-so、--tiling-json、--recompile-tiling冲突，不支持同时设置。 |
| --tiling-so | 使用开发者传入的liboptiling.so进行编译。 | 否 | 无 | 该参数与--tiling-bin、--tiling-json、--recompile-tiling冲突，不支持同时设置。 |
| --tiling-json | Tiling json文件路径（绝对路径），用于生成自定义Tiling data。 | 否 | 无 | **说明：** 预留参数项，开发者无需关注。 |
| --repo-path | 算子源码仓所在路径（绝对路径）。 | 否 | 无 | **说明：** 预留参数项，开发者无需关注。 |
| --recompile-tiling | 是否重新编译算子Tiling so，无需配置值。 | 否 | 无 | **说明：** 预留参数项，开发者无需关注。 |

## NPU调测参数

| 参数（区分大小写） | 说明 | 是否必选 | 默认值 | 备注 |
| --- | --- | --- | --- | --- |
| kernel | 开启NPU调测功能的固定参数。 | 是 | 无 | 无 |
| -b，--backend | 算子调试类型。 | 否 | npu | NPU调测场景设为npu。  - cpu：CPU调测场景。  - npu：NPU调测场景。  - simulator：仿真器调测场景。 |
| --chip-version | Kirin AI处理器SoCNPU IP加速器的版本。 | 否 | 工具自动获取对应版本。 | 在运行环境上通过命令行获取：  hdc -t {target} shell param get ohos.boot.chiptype  target：设备的SN码，可以通过hdc list targets获取当前环境上所有设备的SN码。 |
| -i，--install-path | ascendc软件安装后文件存储路径。 | 否 | 工具自动获取。 | 不支持，开发者无需关注。 |
| -w，--work-dir | 调测结果的存放路径。 | 否 | 缺省为当前执行路径下/debug\_workspace/${op\_type}文件夹（若无则会自动新建）。 | 调测工作目录，可用于存放调测中各种临时文件、结果文件。例如/home/debug\_workspace/AddCustom/npu。 |
| -j，--json-file | 算子信息json配置文件，配置算子输入/输出/属性信息。 | 是 | 无 | json配置文件必须是绝对路径，其配置项说明详见[输入数据和标杆数据准备](cannkit-preparing-input-data-and-benchmark.md)。 |
| --log-level | 日志级别。 | 否 | info | 支持debug 、info、warning、error级别。 |
| --log-file | 日志文件路径。 | 否 | 缺省值为当前目录下的debug\_op.log文件（若无则会新建）。 | 根据设置的--log-level存放程序执行过程中的日志信息。 |
| --repo-type | 算子开发场景类型。 | 否 | customize | 根据实际情况设置。  - minimalist：核函数直调工程场景。  - customize：标准自定义算子工程。 |
| --customize-path | 自定义算子包的安装目录。 | 否 | 无 | 开发者无需关注，当前固定为${install\_path}/ddk/ tools/tools\_ascendc/custom\_op/${chip-version}。  **说明：** 仅当--repo-type为customize，该参数生效。 |
| --dump-mode | printf/PRINTF/DumpTensor/DumpAccChkPoint/assert/时间戳打印功能的模式。 | 否 | 无 | 若不设置表示关闭打印功能，若开启支持如下取值：  normal： 使能通用的打印功能。  **说明：** 当取值为normal时，不支持与--profiling同时开启。  更多打印功能说明参见[更多功能](cannkit-commissioning-function-printf.md)。 |
| --core-type | 算子类型。 | 否 | AiCore | 根据实际算子情况填写，可选值为AiCore、CubeCore、VectorCore为预留参数，开发者无需关注。 |
| --rel-err-thd | 精度比对的相对误差阈值。 | 否 | 0.005 | 无 |
| --abs-err-thd | 精度比对的绝对误差阈值。 | 否 | 0.005 | 无 |
| -d，--device-id | 设置运行的device id。 | 否 | 0 | 无 |
| -t，--timeout | 设置运行超时时间，单位秒。 | 否 | 600 | 无 |
| --block-num | 设置运行的核个数。 | 否 | 无 | 如果有Tiling bin文件，则使用其对应的block\_num值，否则根据实际情况自行配置。 |
| --profiling | Profiling功能开关，无需配置值。 | 否 | 无 | - 基础采集：无配置值，默认采集PipeUtilization数据（pmu数据）。  - 高级采集：支持采集多种运行性能数据，可通过--profiling ${profiling\_metrics}设置，${profiling\_metrics}取值如下。  **说明：** 预留参数项，开发者无需关注。 |
| --loop | 当使能Profiling时，设置上板执行次数。 | 否 | 10 | **说明：** 预留参数项，开发者无需关注。 |
| --kernel-bin | 指定已编译好的Kernel bin文件。 | 否 | 无 | 当该参数生效时，会跳过编译流程，直接用指定的kernel bin文件执行。  **说明：** 预留参数项，开发者无需关注。 |
| --tiling-bin | 使用开发者传入的Tiling.bin进行编译。 | 否 | 无 | 传入的Tiling bin是带绝对路径的文件名，文件命名规则为tiling\_data\_tiling\_key\_${tiling\_key}block\_dim${block\_num}workspace${workspace}.bin，确保tiling\_key、block\_num、workspace与Tiling bin文件匹配。  **说明：**  - 该参数与--tiling-so、--tiling-json、--recompile-tiling冲突，不支持同时设置。  - 预留参数项，开发者无需关注。 |
| --tiling-so | 使用开发者传入的liboptiling.so进行编译。 | 否 | 无 | 该参数与--tiling-bin、--tiling-json、--recompile-tiling冲突，不支持同时设置。  **说明：** 预留参数项，开发者无需关注。 |
| --tiling-json | Tiling json文件路径（绝对路径），用于生成自定义Tiling data。 | 否 | 无 | **说明：** 预留参数项，开发者无需关注。 |
| --repo-path | 算子源码仓所在路径（绝对路径）。 | 否 | 无 | **说明：** 预留参数项，开发者无需关注。 |
| --recompile-tiling | 是否重新编译算子Tiling so，无需配置值。 | 否 | 无 | **说明：** 预留参数项，开发者无需关注。 |
| --npu-compile-type | 设置调测场景下Kernel.o文件编译方式。 | 否 | opc | 当--repo-type为cann\_dev、ops\_adv时支持CCEC和opc两种编译方式，minimalist默认使用CCEC，customize、op\_contrib默认使用opc。  - opc：AscendC框架自带的编译方式。  - CCEC：本工具基于毕昇编译器自动拼接编译选项得到的编译方式，毕昇编译器介绍参见《[毕昇编译器使用指南](https://www.hiascend.com/document/detail/zh/canncommercial/82RC1/index/index.html)》。  **说明：** 预留参数项，开发者无需关注。 |
| --compile-option | 设置opc编译场景下的自定义参数。 | 否 | 无 | **说明：** 预留参数项，开发者无需关注。 |
| --syncall | 硬同步功能的使能开关，无需配置值。 | 否 | 无 | **说明：** 预留参数项，开发者无需关注。 |
| --task-ration | 设置核函数运行时的block数分配方式比例，例如“--task-ration 1:1”。 | 否 | 无 | 当--repo-type为ops\_adv、cann\_dev且--npu-compile-type为CCEC时，该参数才生效。  **说明：** 预留参数项，开发者无需关注。 |
| --memory-check | 是否开启内存检测功能。 | 否 | 无 | 未设置：默认关闭。  - oom：开启内存异常检测，主要检测内存泄漏、非法释放、非法读写、越界访问。  - oob：开启内存异常检测，主要检测越界访问。  **说明：**  - 与--dump-mode参数冲突，不支持同时开启。  - 仅当--repo-type为cann\_dev、customize、ops\_adv，且--npu-compile-type为opc时，该参数生效。  - 当--repo-type为minimalist、op\_contrib，不支持设置该参数。  - 预留参数项，开发者无需关注。 |

## Simulator仿真参数

| 参数（区分大小写） | 说明 | 是否必选 | 默认值 | 备注 |
| --- | --- | --- | --- | --- |
| kernel | 开启仿真功能的固定参数。 | 是 | 无 | 无 |
| -b，--backend | 算子调试类型。 | 否 | npu | 性能仿真场景设为simulator。  - cpu：CPU调测场景。  - npu：NPU调测场景。  - simulator：仿真器调测场景。  **说明：** 参数npu暂不支持。 |
| --chip-version | Kirin AI处理器SoCNPU IP加速器的版本。 | 否 | 工具自动获取对应版本。 | 在运行环境上通过命令行获取：  hdc -t {target} shell param get ohos.boot.chiptype  target：设备的SN码，可以通过hdc list targets获取当前环境上所有设备的SN码。 |
| -i，--install-path | ascendc软件安装后文件存储路径。 | 否 | 工具自动获取。 | 不支持，开发者无需关注。 |
| -w，--work-dir | 调测结果的存放路径。 | 否 | 缺省为当前执行路径下/debug\_workspace/${op\_type}文件夹（若无则会自动新建）。 | 调测工作目录，可用于存放调测中各种临时文件、结果文件。例如/home/debug\_workspace/AddCustom/simulator。 |
| -j，--json-file | 算子信息json配置文件，配置算子输入/输出/属性信息。 | 是 | 无 | json配置文件必须是绝对路径，其配置项说明详见[输入数据和标杆数据准备](cannkit-preparing-input-data-and-benchmark.md)。 |
| --log-level | 日志级别。 | 否 | info | 支持debug 、info、warning、error级别。 |
| --log-file | 日志文件路径。 | 否 | 缺省值为当前目录下的debug\_op.log文件（若无则会新建）。 | 根据设置的--log-level存放程序执行过程中的日志信息。 |
| --repo-type | 算子开发场景类型。 | 否 | customize | 根据实际情况设置。  - minimalist：核函数直调工程场景。  - customize：标准自定义算子工程。 |
| --customize-path | 自定义算子包的安装目录。 | 否 | 无 | 开发者无需关注，当前固定为${install\_path}/ddk/ tools/tools\_ascendc/custom\_op/${chip-version}。  **说明：** 仅当--repo-type为customize，该参数生效。 |
| --dump-mode | printf/PRINTF/DumpTensor/DumpAccChkPoint/assert打印功能的模式。 | 否 | 无 | 若不设置表示关闭打印功能，若开启支持如下取值：  - normal： 使能通用的打印功能。  - acc\_chk：使能偏移位置打印Tensor（DumpAccChkPoint功能）。使能分阶段打印功能。  更多打印功能说明参见[更多功能](cannkit-commissioning-function-printf.md)。 |
| --core-type | 算子类型。 | 否 | AiCore | 根据实际算子情况填写，可选值为AiCore、CubeCore、VectorCore。 |
| -t，--timeout | 设置运行超时时间，单位秒。 | 否 | 600 | CAModel运行时间比较长，一般设为1200s， 开发者可根据实际情况修改。 |
| --block-num | 设置运行的核个数。 | 否 | 无 | CAModel场景一般单核运行，设置为1。 |
| --kernel-bin | 指定已编译好的kernel bin文件。 | 否 | 无 | 当该参数生效时，会跳过编译流程，直接用指定的kernel bin文件执行。 |
| --simulator-mode | 仿真器模式设置。 | 否 | camodel | 支持camodel、esl、biprof模式，目前仅支持camodel模式。  **说明：** 当--simulator-mode为biprof时，会使能biprof分析插件帮助开发者生成结果流水图，并不影响Camodel/Esl的模拟仿真流程。 |
| --simu-pkg-path | 设置仿真器安装包路径。 | 否 | 无 | 当--simulator-mode为camodel时，不需要设置该参数，跑Esl仿真时需要设置该参数指定Esl包路径。  **说明：** 预留参数项，开发者无需关注。 |
| --tiling-bin | 使用开发者传入的tiling.bin进行编译。 | 否 | 无 | 传入的Tiling bin是带绝对路径的文件名，文件命名规则为tiling\_data\_tiling\_key\_${tiling\_key}block\_dim${block\_num}workspace${workspace}.bin，确保tiling\_key、block\_num、workspace与Tiling bin文件匹配。  **说明：**  - 该参数与--tiling-so、--tiling-json、--recompile-tiling冲突，不支持同时设置。  - 预留参数项，开发者无需关注。 |
| --tiling-so | 使用开发者传入的liboptiling.so进行编译。 | 否 | 无 | 该参数与--tiling-bin、--tiling-json、--recompile-tiling冲突，不支持同时设置。  **说明：** 预留参数项，开发者无需关注。 |
| --tiling-json | Tiling json文件路径（绝对路径），用于生成自定义Tiling data。 | 否 | 无 | 仅当--repo-type为ops\_adv、cann\_dev，该参数生效。  **说明：**  - 该参数与--tiling-so、--tiling-bin、--recompile-tiling冲突，不支持同时设置。  - 预留参数项，开发者无需关注。 |
| --repo-path | 算子源码仓所在路径（绝对路径）。 | 否 | 无 | 仅当--repo-type为ops\_adv、cann\_dev、op\_contrib，该参数生效。  **说明：** 预留参数项，开发者无需关注。 |
| --recompile-tiling | 是否重新编译算子Tiling so，无需配置值。 | 否 | 无 | - 若设置了，默认根据算子源码仓重新编译Tiling so。  - 若未设置，工具自动查找DDK包下的so文件，开发者无需关注。  **说明：**  - 仅当--repo-type为ops\_adv、cann\_dev、op\_contrib，该参数才生效。  - 该参数与--tiling-so、--tiling-bin、--tiling-json冲突，不支持同时设置。  - 预留参数项，开发者无需关注。 |
| --npu-compile-type | 设置调测场景下Kernel.o文件编译方式。 | 否 | opc | 当--repo-type为cann\_dev、ops\_adv时支持CCEC和opc两种编译方式，minimalist默认使用CCEC，customize、op\_contrib默认使用opc。  - opc：AscendC框架自带的编译方式。  - CCEC：本工具基于毕昇编译器自动拼接编译选项得到的编译方式，毕昇编译器介绍参见《[毕昇编译器使用指南](https://www.hiascend.com/document/detail/zh/canncommercial/82RC1/index/index.html)》。  **说明：** 预留参数项，开发者无需关注。 |
| --compile-option | opc编译时是否开启个性化单算子编译调试能力。 | 否 | xx | **说明：** 预留参数项，开发者无需关注。 |
| --syncall | 硬同步功能的使能开关，无需配置值。 | 否 | 无 | **说明：** 预留参数项，开发者无需关注。 |
| --task-ration | 设置核函数运行时的block数分配方式比例，例如“--task-ration 1:1”。 | 否 | 无 | 当--repo-type为ops\_adv、cann\_dev且--npu-compile-type为CCEC时，该参数才生效。  **说明：** 预留参数项，开发者无需关注。 |
