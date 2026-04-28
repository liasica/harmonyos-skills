---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-json-configuration
title: 固定输入/输出顺序的算子json配置
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > 自定义算子开发 > 算子调试调优 > 数据准备和配置说明 > 固定输入/输出顺序的算子json配置
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:28+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:26db88f22e57db55f354c7da135a92ceb21a27345bbec23fbe3e140cbd150e61
---

## json配置说明

固定输入/输出顺序的算子json配置文件中“inputs”和“outputs”参数按照“**输入/输出规则排布**”，所以要求Kernel入口函数的参数也是按照该规则排布。

**简要说明：**

* **输入/输出规则排布**（所有输出参数排布在输入参数之后）：例如Kernel入口函数的参数排布为

  ```
  1. extern "C" __global__ __aicore__ void add_custom(GM_ADDR input1, GM_ADDR input2, GM_ADDR output)
  ```
* **标准自定义算子工程场景**的开发人员一般按此方式配置算子json文件。

以AddCustom算子为例，对应的json配置示例如下，参数说明参见表1。

```
1. {
2. "op_type": "AddCustom",
3. "data_script": "./add_golden.py",
4. "gen_data": true,
5. "inputs": [
6. {
7. "name": "x",
8. "dtype": "int32",
9. "format": "ND",
10. "ignore": false,
11. "shape": [32],
12. "param_type": "required",
13. "data_file": "x.bin"
14. },
15. {
16. "name": "y",
17. "dtype": "int32",
18. "format": "ND",
19. "ignore": false,
20. "shape": [32],
21. "param_type": "required",
22. "data_file": "y.bin"
23. }
24. ],
25. "outputs": [
26. {
27. "name": "z",
28. "dtype": "int32",
29. "format": "ND",
30. "ignore": false,
31. "shape": [32],
32. "param_type": "required",
33. "data_file": "golden_z.bin"
34. }
35. ],
36. "attrs": [
37. {
38. "name": "mask",
39. "dtype": "list_int",
40. "value": [0,0]
41. },
42. {
43. "name": "repeatTimes",
44. "dtype": "int",
45. "value": 1
46. },
47. // ...
48. ]
49. }
```

**表1** 固定输入/输出顺序的算子json全量参数说明

| 配置项 | 配置项 | 数据类型 | 参数说明 | 取值说明 | 是否必选 |
| --- | --- | --- | --- | --- | --- |
| op\_type | N/A | string | 算子名。 | 与待调测算子严格匹配。 | 是 |
| data\_script | N/A | string | 数据生成脚本（python），用于生成输入和标杆数据。 | 根据实际情况设置，如"/home/flash\_attention\_golden.py"。  **说明：** 若无数据生成脚本，填写空字符或null。 | 否 |
| gen\_data | N/A | bool | 是否根据data\_script生成输入和标杆数据。 | - true：采用脚本生成数据。  - false：不采用脚本生成数据，默认false。 | 是 |
| inputs /  outputs | name | string | 核函数输入/输出的参数名。 | 根据实际情况设置（若通过算子二进制模板文件生成，不建议修改）。 | 是 |
| inputs /  outputs | dtype | string | 输入/输出的数据类型。 | 目前支持bool、int、int8、int16、int32、int64、uint8、uint16、uint32、uint64、float16、float32、float64、bfloat16。  **说明：** 算子json配置时dtype仅允许输入一种数据类型，不支持多种数据类型。 | 是 |
| inputs /  outputs | format | string | 输入/输出的存储格式。 | 支持的数据格式有ND、NZ。 | 是 |
| inputs /  outputs | shape | list | 输入/输出的shape。 | 根据算子实际shape填写，例如[24, 20, 144, 8]。  **说明：** 当输入为Scalar时，shape填null。 | 是 |
| inputs /  outputs | ignore | bool | 是否忽略该输入/输出。 | - true：表示输入/输出可忽略，不分配Global Memory内存。  - false：表示输入/输出不可忽略，默认false。 | 否 |
| inputs /  outputs | param\_type | string | 是否必选该输入/输出。 | - required：必选。  - optional：可选。  **说明：** 当param\_type为optional时  - ignore为false视为没有该输入。  - ignore为true视为存在该输入。  - 不支持中间有悬空输入。例如，存在3个输入x, y, z时，不允许ignore的情况为false, true, false。 | 是 |
| inputs /  outputs | data\_file | string | - inputs场景下，指输入数据bin文件。  - outputs场景下，指标杆数据bin文件。 | 根据实际情况设置数据bin文件路径，必须为绝对路径，例如"/home/data.bin"。  **说明：**  - 当data\_file设为空字符或null，表示不对运行输出作精度比对。  - 当输入为Scalar时，data\_file字段删除，只需配置data\_value。 | 否 |
| inputs /  outputs | data\_value | 由dtype确定 | 输入的Scalar值。 | 根据实际情况填写。  **说明：**  - 只有input节点才可以配置该参数。  - data\_value与data\_file互斥。若配置data\_value则data\_file必须删除，且shape必须为null，表示本节点是Scalar输入。 | 否 |
| inputs /  outputs | value\_depend | string | 输入是否为Const类型 | 该配置项可选，不配置该字段表示输入不为Const类型。  - true：输入为Const类型。  - false：输入不为Const类型。 | 否 |
| attrs | name | string | 算子的属性名，是区分每个算子的唯一标识，不可重复。 | 部分场景允许没有attrs，请根据实际情况填写。 | 是 |
| attrs | dtype | string | 数据类型。 | 部分场景允许没有attrs，请根据实际情况填写。 | 是 |
| attrs | value | 可变 | 属性值。 | 部分场景允许没有attrs，请根据实际情况填写。 | 是 |

## 特殊格式输入

* **场景1：支持Scalar格式的输入。**

  当输入为Scalar格式，json中“inputs”配置项中删除data\_file，shape配为null，data\_value配为指定的标量值。

  ```
  1. {
  2. "op_type": "xxxx",
  3. "data_script": "",
  4. "gen_data": false,
  5. "inputs": [{
  6. "name": "tileNumIn",
  7. "dtype": "uint32",
  8. "param_type": "required",

  10. "shape": null,
  11. "data_value": 8
  12. }]

  14. }
  ```
* **场景2：支持TensorList格式的输入。**

  当输入为TensorList格式，该参数需要用[ ]表示，List中的每一项表示一个Tensor，示例如下。

  ```
  1. {
  2. "op_type": "xxxx",
  3. "data_script": "",
  4. "gen_data": false,
  5. "inputs":
  6. [{
  7. "name": "key0",
  8. "dtype": "float16",
  9. "format": "ND",
  10. "ignore": false,
  11. "shape": [1,5,8192,128],
  12. "param_type": "required",
  13. "data_file": "/home/data/input/k_0.bin"
  14. },{
  15. "name": "key1",
  16. "dtype": "float16",
  17. "format": "ND",
  18. "ignore": false,
  19. "shape": [1,5,8192,128],
  20. "param_type": "required",
  21. "data_file": "/home/data/input/k_1.bin"
  22. }]

  24. }
  ```
* **场景3：支持原地算子格式的输入。**

  说明

  暂不支持该方式设置输入。

  当算子为[原地算子(in-place op)](cannkit-commissioning-tools.md#基本概念)时，输入和输出地址一样，配置算子json时“outputs”和“inputs”除了“data\_file”不同，其他配置项均保持一致。配置示例如下。

  + "inputs"中data\_file：输入数据为x.bin。
  + "outputs"中data\_file：输出数据为标杆数据golden\_x.bin。

  ```
  1. {
  2. "op_type": "AddCustom",
  3. "data_script": "./add_golden.py",
  4. "gen_data": true,
  5. "inputs": [
  6. {
  7. "name": "x",
  8. "dtype": "int32",
  9. "format": "ND",
  10. "ignore": false,
  11. "shape": [32],
  12. "param_type": "required",
  13. "data_file": "x.bin"
  14. },
  15. {
  16. "name": "y",
  17. "dtype": "int32",
  18. "format": "ND",
  19. "ignore": false,
  20. "shape": [32],
  21. "param_type": "required",
  22. "data_file": "y.bin"
  23. }
  24. ],
  25. "outputs": [
  26. {
  27. "name": "x",
  28. "dtype": "int32",
  29. "format": "ND",
  30. "ignore": false,
  31. "shape": [32],
  32. "param_type": "required",
  33. "data_file": "golden_x.bin"
  34. }
  35. ],
  36. "attrs": [
  37. {
  38. "name": "mask",
  39. "dtype": "list_int",
  40. "value": [0,0]
  41. },
  42. {
  43. "name": "repeatTimes",
  44. "dtype": "int",
  45. "value": 1
  46. }
  47. ]
  48. }
  ```
