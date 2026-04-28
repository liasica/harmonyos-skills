---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_open_g_t_x___network_info
title: OpenGTX_NetworkInfo
breadcrumb: API参考 > 图形 > Graphics Accelerate Kit（图形加速服务） > C API > 头文件和结构体 > 结构体 > OpenGTX_NetworkInfo
category: harmonyos-references
scraped_at: 2026-04-28T08:15:48+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d4d0676a335f3b638c36726c00921f03a859afbb63876ec4ade68ad81cc49f6b
---

## 概述

PhoneTabletTV

此结构体描述当前设备网络信息，游戏应用获取到网络信息后传递此参数。

**起始版本：** 5.0.0(12)

**相关模块：** [GraphicsAccelerate](_graphics_accelerate.md)

**所在头文件：** [opengtx\_base.h](opengtx__base_8h.md)

## 汇总

PhoneTabletTV

### 成员变量

PhoneTabletTV

| 名称 | 描述 |
| --- | --- |
| [OpenGTX\_NetworkLatency](_open_g_t_x___network_latency.md) [networkLatency](_open_g_t_x___network_info.md#networklatency) | 游戏中的网络延迟。 如果没有上下行时延，则设置为total（总时延）的值。将游戏总时延以0ms、50ms、100ms、150ms、200ms分为5个档位，当档位发生变化时，游戏应用通知OpenGTX。 |
| char\* [networkServerIP](_open_g_t_x___network_info.md#networkserverip) | 游戏服务器的IP地址，字节长度范围[1,256]。示例："10.10.10.10"。 |

## 结构体成员变量说明

PhoneTabletTV

### networkLatency

PhoneTabletTV

```
1. OpenGTX_NetworkLatency OpenGTX_NetworkInfo::networkLatency
```

**描述**

游戏中的网络延迟。 如果没有上下行时延，则设置为total（总时延）的值。将游戏总时延以0ms、50ms、100ms、150ms、200ms分为5个档位，当档位发生变化时，游戏应用通知OpenGTX。

### networkServerIP

PhoneTabletTV

```
1. char* OpenGTX_NetworkInfo::networkServerIP
```

**描述**

游戏服务器的IP地址，字节长度范围[1,256]。
