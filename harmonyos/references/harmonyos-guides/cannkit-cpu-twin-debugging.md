---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-cpu-twin-debugging
title: CPU孪生调试功能
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > 自定义算子开发 > 算子调试调优 > 调测功能介绍 > CPU孪生调试功能
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:30+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:05065bed7de810e1b220febcfcac6047841f56a0fb4bd7fd368556f244b35d77
---

## 功能介绍

说明

* 当开发者需要快速进行代码逻辑调试，可优先选择算子CPU调测。使用通用的打印、gdb调测手段，快速定位代码问题。
* 在NPU板端上板运行之前，可优先选择算子CPU调测初步定位算子精度问题，提高算子NPU上板成功率。

CPU孪生调试主要基于开发者输入生成编译所需的二进制bin文件，然后自动执行算子编译和运行，该阶段支持的调测项如表1所示。

**表1** CPU调测功能列表

| 功能名称 | 功能说明 |
| --- | --- |
| 自动精度比对 | 若开发者配置了标杆数据（golden数据），工具会自动将实际调测运行结果与标杆数据进行精度比对。 |
| printf/PRINTF功能 | 支持屏显打印Scalar数据，如常量、字符串等信息，具体参考[printf/PRINTF功能](cannkit-commissioning-function-printf.md)。 |
| DumpTensor功能 | 支持dump Tensor数据，功能和产物与NPU上板dump功能类似，具体参考[DumpTensor功能](cannkit-commissioning-function-dumptensor.md)。 |
| DumpAccChkPoint功能 | 支持dump偏移位置的Tensor数据，具体参考[DumpAccChkPoint功能](cannkit-commissioning-function-dumpaccchkpoint.md)。 |
| assert功能 | 支持屏显打印断言，具体参考[assert功能](cannkit-commissioning-function-assert.md)。 |
| CCE指令流打印 | 默认开启，CCE指令流文件参见[产物说明](cannkit-cpu-twin-debugging.md#产物说明)。 |
| gdb调试 | 可使用gdb单步调试算子计算精度。具体参考[gdb调试](cannkit-gdb.md)。 |

## 使用方法（命令行）

通过命令行进行CPU调测的关键步骤如下。

1. 完成环境搭建，并准备好输入/标杆数据文件。
2. 执行如下命令进行CPU调测，这里仅提供关键参数项示例，其他参数请参考[CPU调测参数](cannkit-cli-parameters.md#cpu调测参数)按需设置。

   ```
   1. ascendebug kernel --backend cpu --chip-version ${chip_version} --repo-type customize --json-file ${op_config_json_file} --core-type ${core_type} --work-dir ${work_dir} ... {其他参数}
   ```

   CPU调测涉及的所有参数可通过**ascendebug kernel -h**或**ascendebug kernel --help**查看。
3. 查看结果文件，详细说明参见[产物说明](cannkit-cpu-twin-debugging.md#产物说明)。

## 产物说明

CPU调测结果存放在${root}/${work\_dir}/cpu路径下，其中${root}表示当前操作路径，${work\_dir}表示调测工作空间，默认为/debug\_workspace/${op\_type}目录，${op\_type}为算子名。目录结构示例如下。

```
1. ├ ${op_type}                    // 算子名
2. ├── cpu
3. │   ├── build               // 存放CPU编译生成的中间文件
4. │   │   ├── cceprint      // 存放cce 指令流输出文件的目录
5. │   │   │   └── auto_gen_add_custom_kernel_0_0_mix.cce // cce指令流文件
6. │       ├── xxx_cpu         // CPU编译生成的算子可执行程序
7. │   ├── output              // 存放CPU编译运行的输出文件及精度比对结果
8. │       ├── y.bin           // 运行输出原始数据
9. │       ├── y.txt           // 精度比对结果文件
10. │   ├── src                 // 存放CPU编译生成的临时代码文件
11. │       ├── CMakeLists.txt
12. │       ├── data_definition.txt
13. │       ├── add_custom_main.cpp
14. │       ├── add_custom_tiling.h
15. │       ├── _gen_kernel_${op_type}.cpp
16. │   ├── dump               // dump文件落盘目录
17. │       ├── PARSER_${timestamp}
18. │           ├── dump_data
19. │               ├──0                     // core number
20. │                   ├──index_1           // index是dump接口的desc唯一标识值
21. │                       ├──core_0_index_1_loop_0.bin
22. │                       ├──core_0_index_1_loop_0.txt
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

     **表2** 精度比对结果说明

     | 信息项 | 说明 |
     | --- | --- |
     | data\_cmp mean | 运行输出数据的均值信息。 |
     | data\_gd mean | 标杆数据的均值信息。 |
     | split\_count | 统计输出数据的个数。 |
     | max\_diff\_hd | 输出数据和golden数据的最大误差值阈值。 |
     | 详细对比数据展示（部分） | Loop（数据位置）、ExpectOut（期望输出值）、RealOut（实际输出值）、FpDiff （绝对误差值）、RateDiff（相对误差值）。 |
     | 整体对比结果展示 | DiffThd（相对误差值阈值）、PctThd （精度达标数据占比阈值）、PctRlt（实际精度达标数据占比）、Result（对比结果）。 |
     | Error Line展示项 | 若精度比对结果为Failed，会追加展示部分误差较大的数据的详细信息，信息格式与精度比对结果一致。 |
* **（可选）查看dump结果**

  若开启[DumpTensor功能](cannkit-commissioning-function-dumptensor.md)或[DumpAccChkPoint功能](cannkit-commissioning-function-dumpaccchkpoint.md)，结果文件存放在dump目录下，结果目录具体介绍参见[产物说明](cannkit-commissioning-function-dumptensor.md#产物说明)。
