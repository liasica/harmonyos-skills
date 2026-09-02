---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getbaseaddr
title: GetBaseAddr
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 基础API > 内存管理与同步控制 > TPipe > GetBaseAddr
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:37+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:066a41c820cfa3f4afae4d613c2ab529dc145958b597631c0603812abef11fe7
---

## 功能说明

根据传入的logicPos（逻辑抽象位置），获取该位置的基础地址，只在CPU调试场景下此接口生效，在CPU调试中通常用于将Tensor地址由CPU地址转换为NPU地址。

## 函数原型

```cpp
inline uint8_t* GetBaseAddr(int8_t logicPos)
```

## 参数说明

| 参数名称 | 输入/输出 | 含义 |
| --- | --- | --- |
| logicPos | 输入 | 逻辑位置类型。该类型具体说明请参考[TPosition](cannkit-tposition.md)。 |

## 支持的型号

Kirin9020系列处理器

Kirin9030系列处理器

KirinX90系列处理器

## 注意事项

无

## 返回值

逻辑位置对应的基地址。

## 调用示例

```cpp
auto absAddr = GetTPipePtr()->GetBaseAddr(static_cast<int8_t>(pos));
```
