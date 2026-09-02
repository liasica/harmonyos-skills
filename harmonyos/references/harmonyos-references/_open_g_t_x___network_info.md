---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_open_g_t_x___network_info
title: OpenGTX_NetworkInfo
breadcrumb: API参考 > 图形 > Graphics Accelerate Kit（图形加速服务） > C API > 头文件和结构体 > 结构体 > OpenGTX_NetworkInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:02:48+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b26e53b62da7295554e8c98ad76d7afa7ae98df776099302f1f1bcee151fd8ae
---

## 概述

此结构体描述当前设备网络信息，游戏应用获取到网络信息后传递此参数。

**起始版本：** 5.0.0(12)

**相关模块：** [GraphicsAccelerate](_graphics_accelerate.md)

**所在头文件：** [opengtx\_base.h](opengtx__base_8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [OpenGTX\_NetworkLatency](_open_g_t_x___network_latency.md) [networkLatency](_open_g_t_x___network_info.md#networklatency) | 游戏中的网络延迟。 如果没有上下行时延，则设置为total（总时延）的值。将游戏总时延以0ms、50ms、100ms、150ms、200ms分为5个档位，当档位发生变化时，游戏应用通知OpenGTX。 |
| char\* [networkServerIP](_open_g_t_x___network_info.md#networkserverip) | 游戏服务器的IP地址，字节长度范围[1,256]。示例："10.10.10.10"。该参数支持IPv4和IPv6地址格式，长度范围为1-256字节；不支持空字符串或null值；建议在设置前进行格式校验。 |

## 结构体成员变量说明

### networkLatency

```c
OpenGTX_NetworkLatency OpenGTX_NetworkInfo::networkLatency
```

**描述**

游戏中的网络延迟。 如果没有上下行时延，则设置为total（总时延）的值。将游戏总时延以0ms、50ms、100ms、150ms、200ms分为5个档位，当档位发生变化时，游戏应用通知OpenGTX。

### networkServerIP

```c
char* OpenGTX_NetworkInfo::networkServerIP
```

**描述**

游戏服务器的IP地址，字节长度范围[1,256]。
