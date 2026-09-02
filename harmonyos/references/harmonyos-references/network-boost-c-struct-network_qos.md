---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-struct-network_qos
title: NetworkBoost_NetworkQos
breadcrumb: API参考 > 系统 > 网络 > Network Boost Kit（网络加速服务） > C API > 结构体 > NetworkBoost_NetworkQos
category: harmonyos-references
scraped_at: 2026-09-02T15:01:57+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f9b1e990f9c2584bdee1dbd151df1cc4dca1aedeee92240ea0be001f5330646d
---

## 概述

网络质量回调信息。

**起始版本：** 5.1.0(18)

**相关模块：** [NetworkBoost](network-boost-c-overview.md)

**所在头文件：** [network\_boost\_quality.h](network-boost-c-files-quality.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [NetworkBoost\_PathType](network-boost-c-overview.md#networkboost_pathtype-1) [pathType](network-boost-c-struct-network_qos.md#pathtype) | 相应的数据路径上的网络质量信息。 |
| uint64\_t [linkUpBandwidth](network-boost-c-struct-network_qos.md#linkupbandwidth) | 上行带宽信息，单位为bps。 |
| uint64\_t [linkDownBandwidth](network-boost-c-struct-network_qos.md#linkdownbandwidth) | 下行带宽信息，单位为bps。 |
| uint64\_t [linkUpRate](network-boost-c-struct-network_qos.md#linkuprate) | 上行速率，单位为bps。 |
| uint64\_t [linkDownRate](network-boost-c-struct-network_qos.md#linkdownrate) | 下行速率，单位为bps。 |
| uint32\_t [rttMs](network-boost-c-struct-network_qos.md#rttms) | RTT时延，表示统计时间间隔内，pathType对应数据路径上，所有的TCP上下行数据包的平均往返时延。取值范围为0或任意正数，单位：ms。  如果在统计时间间隔内没有收到某次TCP请求的回复，则该次的RTT时延不会被计入该统计时间间隔内。因此，在完全不可上网的场景下，由于无法收到TCP的回复，回调中的RTT时延值会比较小，与实际状态不一致。针对完全不可上网的场景，建议结合[on('netCapabilitiesChange')](js-apis-net-connection.md#onnetcapabilitieschange)方法进行综合判断。 |
| uint32\_t [linkUpBufferDelayMs](network-boost-c-struct-network_qos.md#linkupbufferdelayms) | 上行发送空口缓冲时延，单位为ms，取值范围是任意正数。 |
| uint32\_t [linkUpBufferCongestionPercent](network-boost-c-struct-network_qos.md#linkupbuffercongestionpercent) | 上行发送空口缓冲时延占总缓冲时间的比例，取值范围[0, 100]。 |

## 结构体成员变量说明

### linkDownBandwidth

```c
uint64_t NetworkBoost_NetworkQos::linkDownBandwidth
```

**描述**

下行带宽信息，单位为bps。

### linkDownRate

```c
uint64_t NetworkBoost_NetworkQos::linkDownRate
```

**描述**

下行速率，单位为bps。

### linkUpBandwidth

```c
uint64_t NetworkBoost_NetworkQos::linkUpBandwidth
```

**描述**

上行带宽信息，单位为bps。

### linkUpBufferCongestionPercent

```c
uint32_t NetworkBoost_NetworkQos::linkUpBufferCongestionPercent
```

**描述**

上行发送空口缓冲时延占总缓冲时间的比例，取值范围[0, 100]。

### linkUpBufferDelayMs

```c
uint32_t NetworkBoost_NetworkQos::linkUpBufferDelayMs
```

**描述**

上行发送空口缓冲时延（单位ms），取值范围是任意正数。

### linkUpRate

```c
uint64_t NetworkBoost_NetworkQos::linkUpRate
```

**描述**

上行速率，单位为bps。

### pathType

```c
NetworkBoost_PathType NetworkBoost_NetworkQos::pathType
```

**描述**

相应的数据路径上的网络质量信息。

### rttMs

```c
uint32_t NetworkBoost_NetworkQos::rttMs
```

**描述**

RTT时延（单位ms），取值范围是任意正数。
