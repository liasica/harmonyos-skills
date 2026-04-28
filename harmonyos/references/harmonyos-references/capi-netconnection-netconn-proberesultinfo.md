---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection-netconn-proberesultinfo
title: NetConn_ProbeResultInfo
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > NetConn_ProbeResultInfo
category: harmonyos-references
scraped_at: 2026-04-28T08:08:36+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:a6bc7401bf30911b154c2430af3a54c16193aa723b2e624b600df41b4dfd6b9b
---

```
1. typedef struct NetConn_ProbeResultInfo {...} NetConn_ProbeResultInfo
```

## 概述

PhonePC/2in1TabletTVWearable

定义探测结果信息。

**起始版本：** 20

**相关模块：** [NetConnection](capi-netconnection.md)

**所在头文件：** [net\_connection\_type.h](capi-net-connection-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint8\_t lossRate | 丢包率，百分制，值100表示100%丢包；50表示50%丢包。 |
| uint32\_t rtt[[NETCONN\_MAX\_RTT\_NUM]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-connection-type-h#宏定义) | 时延结果，包含最小、最大、平均、标准差。 |
