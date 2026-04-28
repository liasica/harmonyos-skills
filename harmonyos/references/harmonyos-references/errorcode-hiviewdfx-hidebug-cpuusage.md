---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-hiviewdfx-hidebug-cpuusage
title: HiDebug CpuUsage错误码
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 错误码 > HiDebug CpuUsage错误码
category: harmonyos-references
scraped_at: 2026-04-28T08:11:30+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:01a79021b68adb09d23226f2d5d2e947711395a9b39a807c198b3b887cbf77ae
---

说明

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 11400104 CpuUsage统计异常

PhonePC/2in1TabletTVWearable

**错误信息**

The status of the system CPU usage is abnormal.

**错误描述**

当前CPU使用率状态异常。

**可能原因**

hiview服务进程未正常启动。

**处理步骤**

检查hiview进程的运行状态，重启hiview服务或系统。
