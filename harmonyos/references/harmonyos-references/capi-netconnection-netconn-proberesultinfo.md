---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection-netconn-proberesultinfo
title: NetConn_ProbeResultInfo
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > NetConn_ProbeResultInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:01:56+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e7c70c5ef1f519e952f0d8445bc6917fc6888eed20d52dbced34b451b89a3329
---

```c
typedef struct NetConn_ProbeResultInfo {...} NetConn_ProbeResultInfo
```

## 概述

定义探测结果信息。

**起始版本：** 20

**相关模块：** [NetConnection](capi-netconnection.md)

**所在头文件：** [net\_connection\_type.h](capi-net-connection-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint8\_t lossRate | 丢包率，百分制，值100表示100%丢包；50表示50%丢包。 |
| uint32\_t rtt[NETCONN\_MAX\_RTT\_NUM](capi-net-connection-type-h.md#宏定义) | 时延结果（单位：ms），包含最小、最大、平均、标准差。 |
