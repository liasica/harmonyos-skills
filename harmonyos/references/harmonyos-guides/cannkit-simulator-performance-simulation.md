---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-simulator-performance-simulation
title: Simulator性能仿真功能
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > 自定义算子开发 > 算子调试调优 > 调测功能介绍 > Simulator性能仿真功能
category: harmonyos-guides
scraped_at: 2026-04-29T13:41:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:129c405a10906c37604229e718cab1553d6c2bff64ba3c2508eac25274d780f4
---

## CAModel性能仿真

### 功能介绍

算子可以在仿真器上进行性能仿真，目前主要支持CAModel仿真器。

说明

* 由于model本身存在准确性问题，CAModel建议只跑单核，仿真性能会比较准，多核一块跑比较慢，误差也大很多。

### 使用方法（命令行）

通过命令行进行性能仿真的关键步骤如下。

1. 完成环境搭建，并准备好输入/标杆数据文件。
2. 执行如下命令进行CAModel性能仿真，仅提供关键参数项示例，其他参数请参考[Simulator仿真参数](cannkit-cli-parameters.md#simulator仿真参数)按需设置。

   ```
   1. ascendebug kernel --backend simulator --repo-type customize --json-file ${op_config_json_file} --core-type ${core_type} –chip-version ${chip_version} --work-dir ${work_dir} --block-num 1 --timeout 1200 ... {其他参数}
   ```

   一般情况下，CAModel仿真时运行比较慢，--timeout一般设置为1200秒，--block-num一般设置为1，开发者需按实际情况设置。
3. 查看性能仿真结果，详细说明参见[产物说明](cannkit-simulator-performance-simulation.md#产物说明)。

### 产物说明

CAModel仿真结果存放在${root}/${work\_dir}/simulator路径下，其中${root}表示当前操作路径，${work\_dir}表示调测工作空间，默认为/debug\_workspace/${op\_type}目录，${op\_type}为算子名。目录结构示例如下。

```
1. ├ ${op_type}                           // 算子名
2. ├── simulator
3. │   ├── build                          // 存放NPU编译生成的中间文件
4. │   │   ├── launch_args.so
5. │   │   └── run_Makefile_0.sh
6. │   ├── dump
7. │   │   ├── camodel
8. │   │   │   ├── log                   // model执行日志
9. │   │   └── dump_data
10. │   │       ├── 0                     // core number
11. │   │       │   └── index_0           // index是dump接口的desc唯一标识值
12. │   │       └── index_dtype.json
13. │   ├── output                        // 存放NPU编译运行的输出文件
14. │   │   ├── z.bin                     // 运行输出原始数据
15. │   │   └── z.txt                     // 精度比对结果文件
16. │   └── src                           // 存放NPU编译生成的临时代码文件
17. │       └── _gen_args_${op_type}.cpp
```

* **查看性能仿真数据**

  1. 在执行ascendebug命令的目录下，会生成执行日志debug\_op.log。
  2. 查看该日志，搜索"block finish"，可以看到类似如下日志，其中block\_idx为芯片的核心序号，total tick为核函数执行的circle数，该值越大代表耗时越长。

     ```
     1. block finish -> block_idx: 0 total tick: 4153
     ```
* **查看精度比对结果**

  1. 在output目录下，查看是否生成输出文件(bin)和精度比对文件(txt)。
  2. 根据精度比对文件(txt)，确认算子精度比对结果。

     精度比对结果输出样例如下，主要展示两份数据的均值、部分误差对比以及成功/失败的最终比对结论。若结果是失败，会将最大误差的部分数据展示出来。

     ```
     1. data_cmp mean is -1.41e-05 data_gd mean is -1.41e-05
     2. split_count:2359296.0; max_diff_hd:0.1;
     3. ---------------------------------------------------------------------------------------
     4. Loop           ExpectOut        RealOut         FpDiff         RateDiff
     5. ---------------------------------------------------------------------------------------
     6. 00000001         0.0395813       0.0395813       0.0000000       0.0000000
     7. 00000002         0.0160980       0.0160980       0.0000000       0.0000000
     8. 00000003         -0.0443420      -0.0443420      0.0000000       0.0000000
     9. 00000004         -0.0847778      -0.0847778      0.0000000       0.0000000
     10. 00000005         -0.0066605      -0.0066605      0.0000000       0.0000000
     11. 00000006         0.0880737       0.0880737       0.0000000       0.0000000
     12. 00000007         0.0848389       0.0848389       0.0000000       0.0000000
     13. 00000008         0.1083374       0.1083374       0.0000000       0.0000000
     14. 00000009         0.0838623       0.0838623       0.0000000       0.0000000
     15. 00000010         0.0887451       0.0887451       0.0000000       0.0000000
     16. 00000011         0.0572205       0.0572205       0.0000000       0.0000000
     17. 00000012         0.0741577       0.0741577       0.0000000       0.0000000
     18. 00000013         -0.0762329      -0.0762329      0.0000000       0.0000000
     19. 00000014         -0.0957642      -0.0957642      0.0000000       0.0000000
     20. 00000015         0.0102234       0.0102234       0.0000000       0.0000000
     21. ...               ...             ...             ...             ...
     22. ---------------------------------------------------------------------------------------
     23. DiffThd           PctThd          PctRlt          Result
     24. ---------------------------------------------------------------------------------------
     25. 0.0050            99.50%          100.000000%     Pass
     26. Success Success Success Success Success
     ```

  **表1** 精度比对结果说明

  | 信息项 | 说明 |
  | --- | --- |
  | data\_cmp mean | 运行输出数据的均值信息。 |
  | data\_gd mean | 标杆数据的均值信息。 |
  | split\_count | 统计输出数据的个数。 |
  | max\_diff\_hd | 输出数据和golden数据的最大误差值阈值。 |
  | 详细对比数据展示（部分） | Loop（数据位置）、ExpectOut（期望输出值）、RealOut（实际输出值）、FpDiff （绝对误差值）、RateDiff（相对误差值）。 |
  | 整体对比结果展示 | DiffThd（相对误差值阈值）、PctThd （精度达标数据占比阈值）、PctRlt（实际精度达标数据占比）、Result（对比结果）。 |
  | Error Line展示项 | 若精度比对结果为Failed，会追加展示部分误差较大的数据的详细信息。 |
* **（可选）查看dump结果**

  若开启[DumpTensor功能](cannkit-commissioning-function-dumptensor.md)或[DumpAccChkPoint功能](cannkit-commissioning-function-dumpaccchkpoint.md)，结果文件存放在dump目录下，详细结果介绍参见[产物说明](cannkit-commissioning-function-dumptensor.md#产物说明)。

## Model仿真打点

### 功能介绍

算子进行CAModel仿真时，可对算子任意运行阶段进行打点，从而分析不同指令的流水图，以便进一步性能调优。

说明

Kirin9020/KirinX90暂不支持使用该方法进行调优。

### 使用方法

1. 先在Kernel代码中的目标指令位置分别打上TRACE\_START/TRACE\_STOP，示例如下，起始/终止接口的说明详见[Trace接口说明](cannkit-simulator-performance-simulation.md#trace接口说明)。

   ```
   1. TRACE_START(0x1);
   2. DataCopy(zGm, zLocal, this->totalLength);
   3. TRACE_STOP(0x1);
   ```
2. 参考[使用方法（命令行）](cannkit-simulator-performance-simulation.md#使用方法命令行)中的命令行方式，执行算子仿真流程。
3. 在CAModel仿真结果trace图上查看打点结果。

   如下图所示，其中USER\_DEFINE\_1\_DELAY表示DataCopy指令下发到指令开始执行的时间，USER\_DEFINE\_1表示指令执行的时间。

   **图1** 仿真打点示意图

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/JC2iuUXkTXqO2nLseKdbXQ/zh-cn_image_0000002589325621.png?HW-CC-KV=V1&HW-CC-Date=20260429T054112Z&HW-CC-Expire=86400&HW-CC-Sign=782CF51ED0A29CB332E63C93C6CA0505D449379BABACC6F4E154F88BD59E60B4)

### Trace接口说明

TRACE\_START接口说明如下。

* **函数原型：** #define TRACE\_START(apid)
* **函数功能：** 起始位置打点。
* **参数(IN)：** apid，当前预留了十个开发者自定义的类型：

  + 0x0：USER\_DEFINE\_0
  + 0x1：USER\_DEFINE\_1
  + 0x2：USER\_DEFINE\_2
  + 0x3：USER\_DEFINE\_3
  + 0x4：USER\_DEFINE\_4
  + 0x5：USER\_DEFINE\_5
  + 0x6：USER\_DEFINE\_6
  + 0x7：USER\_DEFINE\_7
  + 0x8：USER\_DEFINE\_8
  + 0x9：USER\_DEFINE\_9
* **参数(OUT)：** NA
* **返回值：** NA
* **使用约束：**

  + TRACE\_START/TRACE\_STOP需配套使用，若Trace图上未显示打点，则说明两者没有配对。
  + 不支持跨核使用，例如TRACE\_START在AI Cube打点，则TRACE\_STOP打点也需要在AI Cube上，不能在AI Vector上。
* **调用示例：**

  ```
  1. TRACE_START(0x2);
  2. Add(zLocal, xLocal, yLocal, dataSize);
  3. TRACE_STOP(0x2);
  ```

TRACE\_STOP接口说明如下。

* **函数原型：** #define TRACE\_STOP(apid)
* **函数功能：** 终止位置打点
* **参数(IN)：** apid，取值需与TRACE\_START接口参数取值保持一致，否则影响打点结果。
* **参数(OUT)：** None
* **返回值：** NA
* **使用约束：**

  + TRACE\_START/TRACE\_STOP需配套使用，若Trace图上未显示打点，则说明两者没有配对。
  + 不支持跨核使用，例如TRACE\_START在AI Cube打点，则TRACE\_STOP打点也需要在AI Cube上，不能在AI Vector上。
* **调用示例：**

  ```
  1. TRACE_START(0x2);
  2. Add(zLocal, xLocal, yLocal, dataSize);
  3. TRACE_STOP(0x2);
  ```
