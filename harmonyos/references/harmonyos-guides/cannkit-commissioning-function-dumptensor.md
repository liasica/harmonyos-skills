---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-commissioning-function-dumptensor
title: DumpTensor功能
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > 自定义算子开发 > 算子调试调优 > 调测功能介绍 > 更多功能 > DumpTensor功能
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:30+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:657494a285a14e469a18478db14a7d3ec8e731da73a18029f93545fdb3a3ba4b
---

## 功能介绍

使用工具进行算子调测时，支持DumpTensor功能，默认从Tensor的第0位元素开始打印指定长度的元素值。

说明

* simulator调测场景下的DumpTensor，受dump mode参数控制。
* 固定为每个核分配的打印数据的最大可使用空间为1M，目前该大小不支持修改，若打印超过1M，打印内容不再显示，请开发者控制待打印的数据量。

## 使用方法（命令行）

1. 在核函数代码中按需在目标位置调用DumpTensor接口，接口说明参见表1，样例如下。

   ```
   1. DumpTensor(srcLocal, 5, dataNum);
   ```
2. simulator调测场景执行如下命令，使能Dump开关。

   ```
   1. ascendebug kernel --backend simulator --dump-mode normal ... {其他simulator调测参数}
   ```

   --dump-mode取normal，开启通用打印Tensor模式，其他参数参考[NPU调测参数](cannkit-cli-parameters.md#npu调测参数)按需配置。
3. 查看dump结果，具体参见[产物说明](cannkit-commissioning-function-dumptensor.md#产物说明)。

## 接口说明

DumpTensor接口说明如下。

* **函数原型：**

  + void DumpTensor(const LocalTensor<T> &tensor, uint32\_t desc, uint32\_t dumpNum)
  + void DumpTensor(const GlobalTensor<T> &tensor, uint32\_t desc, uint32\_t dumpNum)
  + void DumpTensor(const LocalTensor<T> &tensor, uint32\_t desc, uint32\_t dumpNum, const ShapeInfo& shapeInfo)
  + void DumpTensor(const GlobalTensor<T> &tensor, uint32\_t desc, uint32\_t dumpNum, const ShapeInfo& shapeInfo)
* **函数功能：** 从Tensor的第0位元素开始打印指定长度的元素值。
* **参数(IN)：**

  + **tensor：** 开发者需要Dump的Tensor。多个DumpTensor调用时，不可重复。
    - 待dump的tensor位于Unified Buffer/L1 Buffer/L0C Buffer时使用LocalTensor类型的tensor参数输入。
    - 待dump的tensor位于Global Memory时使用GlobalTensor类型的tensor参数输入。
    - 当前支持的数据类型为uint8\_t/int8\_t/int16\_t/uint16\_t/int32\_t/uint32\_t/int64\_t/uint64\_t/float/half。
  + **desc：** 开发者自定义附加信息（行号或其他自定义数字）。
  + **dumpNum：** 需要Dump的元素个数。
  + **shapeInfo：** 如果有Tensor的shape信息，工具可解析shapeInfo并进行打印。
* **参数(OUT)：** NA
* **返回值：** NA
* **使用约束：**

  + 当前接口仅支持位于Unified Buffer/L1 Buffer/L0C Buffer/Global Memory的数据Dump。
  + 每次Dump的大小(dataNum\*sizeof(T))需要32B对齐。
* **调用示例：**

  + 示例1：无Tensor shape的打印

    ```
    1. DumpTensor(srcLocal,5, dataNum);      # Dump LM
    2. DumpTensor(this->gm_, 0, dataNum);    # Dump GM
    ```
  + 示例2：带Tensor shape的打印

    ```
    1. uint32_t array[] = {static_cast<uint32_t>(8),static_cast<uint32_t>(8)};
    2. ShapeInfo shapeInfo(2, array);       # dim为2， shape为(8,8)
    3. DumpTensor(x, 2, 64, shapeInfo);     # dump x的64个元素，且解析按照shapeInfo的(8,8)排列
    ```

    打印结果如下。

    ```
    1. [[150.000000,83.000000,109.000000,166.000000,129.000000,50.000000,150.000000,74.000000],
    2. [135.000000,79.000000,98.000000,134.000000,146.000000,166.000000,112.000000,70.000000],
    3. [122.000000,51.000000,116.000000,68.000000,172.000000,72.000000,102.000000,69.000000],
    4. [136.000000,83.000000,88.000000,88.000000,112.000000,148.000000,79.000000,136.000000],
    5. [133.000000,104.000000,83.000000,71.000000,83.000000,99.000000,103.000000,151.000000],
    6. [98.000000,118.000000,128.000000,83.000000,25.000000,105.000000,179.000000,34.000000],
    7. [104.000000,169.000000,115.000000,113.000000,134.000000,121.000000,88.000000,96.000000],
    8. [29.000000,139.000000,70.000000,40.000000,158.000000,138.000000,72.000000,171.000000]]
    ```

## 产物说明

Dump的Tensor数据存放在${root}/${work\_dir}/simulator路径下，其中${root}表示当前操作路径，${work\_dir}表示调测工作空间，默认为/debug\_workspace/${op\_type}目录，${op\_type}为算子名。目录结构示例如下。

```
1. ├ ${op_type}     // 算子名
2. ├── simulator
3. │   ├── dump
4. │       ├── PARSER_${timestamp}
5. │           ├── dump_data
6. │               ├──0                     // core number
7. │                   ├──index_5           // index是dump接口的desc唯一标识值
8. │                       ├──core_0_index_5_loop_0.bin
9. │                       ├──core_0_index_5_loop_0.txt
10. │                       ├──core_0_index_5_loop_1.bin
11. │                       ├──core_0_index_5_loop_1.txt
12. │               ├──index_dtype.json       // 存放每个dump Tensor的数据类型
```

其中core\_${core\_id}\_index\_${index}\_loop\_${loop}.txt是工具根据bin文件自动解析的Dump结果，其命名规则为：

* ${core\_id}：计算核id。
* ${index}：是Dump接口的desc唯一标识值。
* ${loop}：若DumpTensor接口在for循环中被调用，其表示循环的索引值，否则默认为0。
