---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tiling-tuning
title: Tiling调测功能
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > 自定义算子开发 > 算子调试调优 > 调测功能介绍 > Tiling调测功能
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:30+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1462692b52a4f297f8c13b2cd75ef407f06f6a0fd0c02a9aa89264f9f007185a
---

## 功能介绍

Tiling是算子开发中独立且关键的部分，描述了Kirin AI处理器SoC NPU IP加速器上算子的输入/输出数据切分、分块计算、多核并行等策略，以满足片上存储限制和计算pipeline的需求，最大化计算并行性和数据局部性(data locality OR data reuse)，从而发挥硬件的极致性能。

对单算子执行Tiling调测时，根据Tiling so文件执行Tiling运算，生成Tiling bin文件。

说明

目前仅标准自定义算子工程场景、ops\_adv算子工程场景、built-in工程场景、内源框架工程场景需要进行Tiling调测，其余场景不涉及。

## 使用方法（命令行）

通过命令行进行Tiling调测的关键步骤如下，详细样例请参考Tiling调测功能。

1. 完成环境搭建，并准备好输入/标杆数据文件。
2. 执行如下命令进行Tiling调测，这里仅提供关键参数项示例，其他参数请参考[Tiling调测参数](cannkit-cli-parameters.md#tiling调测参数)按需配置。

   标准自定义算子场景：

   ```
   1. ascendebug tiling --json-file {op_config_json_file } --chip-version ${chip_version} --work-dir ${work_dir} ... {其他参数}
   ```

   Tiling调测涉及的所有参数可通过**ascendebug tiling -h**或**ascendebug tiling --help**查看。
3. 查看结果文件，详细说明参见[产物说明](cannkit-tiling-tuning.md#产物说明)。

## 产物说明

Tiling调测结果存放在${root}/${work\_dir}/tiling路径下，其中${root}表示当前操作路径，${work\_dir}表示调测工作空间，默认为./debug\_workspace/${op\_type}目录，${op\_type}为算子名。产物一般包含Tiling data bin文件（二进制）、结构体解析文件等，目录结构示例如下，结果文件的详细说明参见表1。

```
1. ├ ${op_type}        // 算子名
2. ├── tiling
3. │   ├── attrs.json
4. │   ├── inputs.json
5. │   ├── outputs.json
6. │   ├── tiling_data_tiling_key_2_block_dim_1_workspace_106258432.bin
7. │   ├── tiling_parse_result.json
8. │   ├── tiling_run_info.bin
```

**表1** Tiling调测结果说明

| 文件名 | 说明 |
| --- | --- |
| attrs.json | 根据算子属性、输入/输出信息生成的中间文件。 |
| inputs.json | 根据算子属性、输入/输出信息生成的中间文件。 |
| outputs.json | 根据算子属性、输入/输出信息生成的中间文件。 |
| tiling\_data\_tiling\_key\_2\_block\_dim\_1\_workspace\_106258432.bin | Tiling数据bin文件，供CPU和simulator调测使用。  **说明：** 文件名中“tiling\_key\_2\_block\_dim\_1\_workspace\_106258432”表示tiling\_key=2，block\_num=1，workspace=106258432，这些信息可用于后续核函数编译和运行（比如--block-num取值为block\_dim值）。 |
| tiling\_parse\_result.json | 对生成的Tiling数据bin文件解析，生成Tiling结构体文件，该文件展现了Tiling中每个数据的数据类型dtype和数值value。 |
| tiling\_run\_info.bin | Tiling调测过程中的信息文件，包含block\_dim、workspace大小以及tiling\_key等信息。该文件关键信息已映射到Tiling数据bin文件名中。 |
