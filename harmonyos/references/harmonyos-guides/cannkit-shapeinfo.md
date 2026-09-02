---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-shapeinfo
title: ShapeInfo
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 数据类型定义 > ShapeInfo
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:35+08:00
doc_updated_at: 2026-05-18
content_hash: sha256:867cf69a6f6544ae57007319c1fa1902e94c7764b71c9833eea52cb706553e7b
---

## 功能说明

ShapeInfo用来存放LocalTensor或GlobalTensor的shape信息。

## 定义原型

* ShapeInfo结构定义

  ```cpp
  struct ShapeInfo {
   public:
       __aicore__ inline ShapeInfo();
       __aicore__ inline ShapeInfo(const uint8_t inputShapeDim, const uint32_t inputShape[],
           const uint8_t inputOriginalShapeDim, const uint32_t inputOriginalShape[], const DataFormat inputFormat);
       __aicore__ inline ShapeInfo(const uint8_t inputShapeDim, const uint32_t inputShape[], const DataFormat inputFormat);
       __aicore__ inline ShapeInfo(const uint8_t inputShapeDim, const uint32_t inputShape[]);
       uint8_t shapeDim;
       uint8_t originalShapeDim;
       uint32_t shape[K_MAX_DIM];
       uint32_t originalShape[K_MAX_DIM];
       DataFormat dataFormat;
   };
  ```
* 获取Shape中所有dim的累乘结果

  ```cpp
  __aicore__ inline int GetShapeSize(const ShapeInfo& shapeInfo)
  ```

## 函数说明

**表1** ShapeInfo结构参数说明

| 参数名称 | 类型 | 描述 |
| --- | --- | --- |
| shapeDim | uint8\_t | 现有的shape维度。 |
| shape | uint32\_t | 现有的shape。 |
| originalShapeDim | uint8\_t | 原始的shape维度。 |
| originalShape | uint32\_t | 原始的shape。 |
| dataFormat | DataFormat | 数据排布格式。NCHW取值为0，NHWC取值为1。  - NCHW：数据按NCHW排布。  - NHWC：数据按NHWC排布。 |

**表2** GetShapeSize参数说明

| **函数名称** | **入参说明** | **含义** |
| --- | --- | --- |
| shapeInfo | Tensor的shape信息。 | 用来存放LocalTensor或GlobalTensor的shape信息。 |
