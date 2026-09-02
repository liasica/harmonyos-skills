---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-releaseeventid
title: ReleaseEventID
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 基础API > 内存管理与同步控制 > TPipe > ReleaseEventID
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:36+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:ca3161793f146759ed17ba17d23032a99472918c7f7518c4ef7e943ae59502de
---

## 功能说明

用于释放HardEvent（硬件类型同步事件）的TEventID，通常与[AllocEventID](cannkit-alloceventid.md)搭配使用。

## 函数原型

```cpp
template <HardEvent evt> 
__aicore__ inline void ReleaseEventID(TEventID id)
```

## 参数说明

| 参数名称 | 输入/输出 | 含义 |
| --- | --- | --- |
| id | 输入 | TEventID类型，调用[AllocEventID](cannkit-alloceventid.md)申请获得的TEventID。 |

## 支持的型号

Kirin9020系列处理器

Kirin9030系列处理器

KirinX90系列处理器

## 注意事项

AllocEventID、ReleaseEventID需成对出现，ReleaseEventID传入的TEventID需由对应的AllocEventID申请而来。

## 返回值

无

## 调用示例

```cpp
AscendC::TEventID eventID = GetTPipePtr()->AllocEventID<AscendC::HardEvent::V_S>(); // 需要插入scalar与vector之间的同步，申请对应的HardEvent的ID
AscendC::SetFlag<AscendC::HardEvent::V_S>(eventID);
// ...
AscendC::WaitFlag<AscendC::HardEvent::V_S>(eventID);
GetTPipePtr()->ReleaseEventID<AscendC::HardEvent::V_S>(eventID); // 释放scalar等vector的同步HardEvent的ID
// ...
```
