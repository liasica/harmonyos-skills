---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-operator-json-configuration
title: params归一格式的算子json配置
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > 自定义算子开发 > 算子调试调优 > 数据准备和配置说明 > params归一格式的算子json配置
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:31+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f46315e88971f9c20866ca83d6ba04263b42df1a9a22690add3a7d48dc3594b9
---

## json配置说明

为了支持输入/输出参数交叉配置的场景，params归一配置格式应运而生，所有输入/输出参数均放在“params”配置项中。该算子json配置文件中参数可以按**输入/输出规则排布**，也可以按**输入/输出交叉排布**，只要保证参数顺序与Kernel入口函数的参数顺序保持一致即可。

说明

* **调试工具暂不支持该配置**。
* **输入/输出规则排布**（所有输出参数排布在输入参数之后）：例如Kernel入口函数的参数排布为extern "C" \_\_global\_\_ \_\_aicore\_\_ void add\_custom(GM\_ADDR input1, GM\_ADDR input2, GM\_ADDR input3,**GM\_ADDR output**)。
* **输入/输出交叉排布**（输入/输出参数排布顺序有交叉）：例如Kernel入口函数的参数排布为extern "C" \_\_global\_\_ \_\_aicore\_\_ void add\_custom(GM\_ADDR input1, GM\_ADDR input2, **GM\_ADDR output**, GM\_ADDR input3)，output参数排在input3之前。
* **核函数直调工程场景**的开发人员一般按此方式配置。

以AddCustom算子为例，对应的json配置示例如下，参数说明参见表1。

```
1. {
2. "op_type": "add_custom",
3. "data_script": "",
4. "gen_data": false,
5. "params": [{
6. "name": "x",
7. "dtype": "float16",
8. "param_type": "input",
9. "shape": [1,16384],
10. "data_file": "x.bin"
11. },
12. {
13. "name": "z",
14. "dtype": "float16",
15. "param_type": "output",
16. "shape": [1,16384],
17. "data_file": "golden_z.bin"
18. },
19. {
20. "name": "y",
21. "dtype": "float16",
22. "param_type": "input",
23. "shape": [1,16384],
24. "data_file": "y.bin"
25. },
26. ],
27. "kernel_info": {
28. "kernel_source": "add_custom.cpp",
29. "kernel_name": "add_custom",
30. "kernel_includes": []
31. }
32. }
```

**表1** params归一格式的算子json全量参数说明

| 参数名 | 参数名 | 数据类型 | 参数说明 | 取值说明 | 是否必选 |
| --- | --- | --- | --- | --- | --- |
| op\_type | - | string | 算子名。 | 与待调测算子严格匹配。 | 是 |
| data\_script | - | string | 数据生成脚本(python)，用于生成输入和标杆数据。 | 根据实际情况设置，如"/home/flash\_attention\_golden.py"。  **说明：** 若无数据生成脚本，填写空字符或null。 | 否 |
| gen\_data | - | bool | 是否根据data\_script生成输入和标杆数据。 | - true：采用脚本生成数据。  - false：不采用脚本生成数据，默认false。 | 是 |
| params | name | string | 核函数输入/输出的参数名。 | 根据实际情况设置。 | 是 |
| params | dtype | string | 输入/输出的数据类型。 | 目前支持bool、int、int8、int16、int32、int64、uint8、uint16、uint32、uint64、float16、float32、float64、bfloat16。  **说明：** 算子json配置时dtype仅允许输入一种数据类型，不支持多种数据类型。 | 是 |
| params | param\_type | string | 标识该节点是输入或输出。 | - input：表示为输入节点。  - output：表示为输出节点。 | 是 |
| params | shape | list | 输入/输出的shape。 | 根据算子实际shape填写，例如[24, 20, 144, 8]。  **说明：** 当输入为Scalar时，shape填null。 | 是 |
| params | data\_file | string | - 当param\_type为input：指定输入数据bin文件。  - 当param\_type为output：指定标杆数据bin文件。 | 根据实际情况设置数据bin文件路径，必须为绝对路径，例如"/home/data.bin"。  **说明：**  - 当data\_file设为空字符或null，表示不对运行输出作精度比对。  - 当输入为Scalar时，data\_file字段删除，只需配置data\_value。 | 否 |
| params | data\_value | 由dtype确定 | 输入的Scalar值。 | 根据实际情况填写。  **说明：**  - 仅当param\_type为input才可以配置该参数。  - data\_value与data\_file互斥。若配置data\_value则data\_file必须删除，且shape必须为null，表示本节点是Scalar输入。 | 否 |
| kernel\_info  **说明：** 仅**核函数直调工程场景**需要设置kernel文件相关的配置。 | kernel\_source | string | Kernel入口源文件绝对路径，注意格式是“绝对路径+文件名”。 | 根据开发的核函数信息填写。 | 是 |
| kernel\_info | kernel\_name | string | Kernel入口函数名。 | 根据开发的核函数信息填写。 | 是 |
| kernel\_info | kernel\_includes | list | Kernel文件依赖的头文件所在的路径。 | 可为[]，也可填入多个路径。 | 是 |

## 特殊格式输入

* **场景1：支持Scalar格式的输入。**

  当输入为Scalar格式，json中“params”配置项中删除data\_file，param\_type配为“input”，shape配为null，data\_value配为指定的标量值。

  ```
  1. {
  2. "op_type": "xxxx",
  3. "data_script": "",
  4. "gen_data": false,
  5. "params": [{
  6. "name": "input_1",
  7. "dtype": "float16",
  8. "param_type": "input",
  9. "shape": null,
  10. "data_value": 8
  11. }
  12. ]
  13. }
  ```
* **场景2：支持TensorList格式的输入。**

  当输入为TensorList格式，该参数需要用[ ]表示，List中的每一项表示一个Tensor，示例如下。

  ```
  1. {
  2. "op_type": "xxxx",
  3. "data_script": "",
  4. "gen_data": false,
  5. "params": [
  6. [{
  7. "name": "input_1",
  8. "dtype": "float16",
  9. "param_type": "input",
  10. "shape": [1,16384],
  11. "data_file": "input_1.bin"
  12. },
  13. {
  14. "name": "input_2",
  15. "dtype": "float16",
  16. "param_type": "input",
  17. "shape": [1,16384],
  18. "data_file": "input_2.bin"
  19. }],
  20. {
  21. "name": "output",
  22. "dtype": "float16",
  23. "param_type": "output",
  24. "shape": [1,16384],
  25. "data_file": "golden.bin"
  26. },
  27. ],
  28. "kernel_info": {
  29. "kernel_source": "add_custom.cpp",
  30. "kernel_name": "add_custom",
  31. "kernel_includes": []
  32. }
  33. }
  ```
* **场景3：支持原地算子格式的输入。**

  当算子为[原地算子(in-place op)](cannkit-commissioning-tools.md#基本概念)时，输入和输出地址一样，配置算子json时除了“param\_type”和“data\_file”不同，其他配置项均保持一致。配置示例如下。

  + param\_type：分别配为input、output。
  + data\_file：输入数据为x.bin，输出数据为标杆数据golden\_x.bin。

  ```
  1. {
  2. "op_type": "add_custom",
  3. "data_script": "",
  4. "gen_data": false,
  5. "params": [{
  6. "name": "x",
  7. "dtype": "float16",
  8. "param_type": "input",
  9. "shape": [1,16384],
  10. "data_file": "x.bin"
  11. },
  12. {
  13. "name": "x",
  14. "dtype": "float16",
  15. "param_type": "output",
  16. "shape": [1,16384],
  17. "data_file": "golden_x.bin"
  18. },
  19. {
  20. "name": "y",
  21. "dtype": "float16",
  22. "param_type": "input",
  23. "shape": [1,16384],
  24. "data_file": "y.bin"
  25. },
  26. ],
  27. "kernel_info": {
  28. "kernel_source": "add_custom.cpp",
  29. "kernel_name": "add_custom",
  30. "kernel_includes": []
  31. }
  32. }
  ```
