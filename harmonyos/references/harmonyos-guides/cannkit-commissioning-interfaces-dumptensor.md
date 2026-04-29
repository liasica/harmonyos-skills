---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-commissioning-interfaces-dumptensor
title: DumpTensor
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 基础API > 调测接口 > DumpTensor
category: harmonyos-guides
scraped_at: 2026-04-29T13:41:26+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fe4b691922bd0042bd0dfd47d0724948ec943655e3af268d499782a9ee71bb7a
---

## 函数功能

基于算子工程开发的算子，可以使用该接口Dump指定Tensor的内容。同时支持打印自定义的附加信息（仅支持uint32\_t数据类型的信息），比如打印当前行号等。

在算子kernel侧实现代码中需要打印Tensor数据的地方调用DumpTensor接口打印相关内容。样例如下。

```
1. AscendC::DumpTensor(srcLocal,5, dataLen);
```

说明

DumpTensor接口打印功能会对算子实际运行的性能带来一定影响，通常在调测阶段使用。开发者可以按需通过如下方式关闭打印功能。

自定义算子工程：

修改算子工程op\_kernel目录下的CMakeLists.txt文件，首行增加编译选项-DASCENDC\_DUMP=0，关闭ASCENDC\_DUMP开关。

打印示例如下。

```
1. -19.046875,62.15625,-56.0625,-12.515625,-82.8125,70.5625,-57.65625,67.0625,
2. 62.8125,30.234375,48.0,-10.8984375,18.171875,-30.4375,-25.3125,-77.1875,
3. 21.21875,-70.25,-2.8125,69.375,-69.1875,-60.8125,-48.3125,51.21875,
4. 74.3125,-47.5,2.923828125,-7.05859375,63.5,-89.1875,2.236328125,-52.1875,
5. 97.75,-17.21875,-0.30322265625,31.640625,39.09375,-3.013671875,36.125,-30.015625,
6. -39.40625,26.59375,27.859375,89.0,-36.125,61.6875,70.375,74.5625,
7. -75.875,-46.0625,73.5625,51.59375,-30.09375,96.3125,77.25,42.90625,
8. -74.9375,-89.9375,30.046875,-76.1875,61.5625,-8.7578125,38.28125,-55.71875,
```

## 函数原型

* 无Tensor shape的打印

  ```
  1. void DumpTensor(const LocalTensor<T> &tensor, uint32_t desc, uint32_t dumpSize)
  2. void DumpTensor(const GlobalTensor<T>& tensor, uint32_t desc, uint32_t dumpSize)
  ```
* 带Tensor shape的打印

  ```
  1. void DumpTensor(const LocalTensor<T> &tensor, uint32_t desc, uint32_t dumpNum, const ShapeInfo& shapeInfo)
  2. void DumpTensor(const GlobalTensor<T> &tensor, uint32_t desc, uint32_t dumpNum, const ShapeInfo& shapeInfo)
  ```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| tensor | 输入 | 需要dump的Tensor。  - 待dump的tensor位于Unified Buffer/L1 Buffer/L0C Buffer时使用LocalTensor类型的tensor参数输入。  - 待dump的tensor位于Global Memory时使用GlobalTensor类型的tensor参数输入。  - 当前支持的数据类型为uint8\_t/int8\_t/int16\_t/uint16\_t/int32\_t/uint32\_t/int64\_t/uint64\_t/float/half。 |
| desc | 输入 | 开发者自定义附加信息（行号或其他自定义数字）。 |
| dumpSize | 输入 | 需要dump的元素个数。**dump的元素总长度需要32Byte对齐。** |
| shapeInfo | 输入 | 传入Tensor的shape信息，可按照shape信息进行打印。 |

## 返回值

无

## 支持的型号

Kirin9020系列处理器

KirinX90系列处理器

## 约束说明

* **该功能仅在如下场景支持：** 通过[工程化算子开发](cannkit-overview-of-engineering-operator.md)方式调用算子。
* **当前仅支持打印存储位置为Unified Buffer/L1 Buffer/L0C Buffer/Global Memory的Tensor信息。**
* 操作数地址偏移对齐要求请参见[通用约束](cannkit-general-constraints.md)。
* 程序中调用[printf](cannkit-commissioning-interfaces-printf.md)接口使用的空间+[assert](cannkit-commissioning-interfaces-assert.md)接口使用的空间+[DumpAccChkPoint](cannkit-commissioning-interfaces-dumpaccch.md)接口使用的空间+调用DumpTensor接口使用的空间+框架dump功能所使用的空间，每个核上不可超过1M。请开发者自行控制待打印的内容数据量，超出则不会打印。

## 调用示例

* 无Tensor shape的打印

  ```
  1. AscendC::DumpTensor(srcLocal,5, dataLen);
  ```
* 带Tensor shape的打印

  ```
  1. uint32_t array[] = {static_cast<uint32_t>(8),static_cast<uint32_t>(8)};
  2. AscendC::ShapeInfo shapeInfo(2, array);       // dim为2， shape为(8,8)
  3. AscendC::DumpTensor(x, 2, 64, shapeInfo);     // dump x的64个元素，且解析按照shapeInfo的(8,8)排列
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
