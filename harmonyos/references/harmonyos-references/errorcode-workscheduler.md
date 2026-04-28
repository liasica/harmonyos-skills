---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-workscheduler
title: workScheduler错误码
breadcrumb: API参考 > 应用框架 > Background Tasks Kit（后台任务开发服务） > 错误码 > workScheduler错误码
category: harmonyos-references
scraped_at: 2026-04-28T08:05:40+08:00
doc_updated_at: 2026-04-10
content_hash: sha256:1b5857ce6222b362cf216efdf5b074cd8f81334817cdf9b96c958f5e67d4a9ea
---

说明

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 9700001 内存操作失败

PhonePC/2in1TabletTVWearable

**错误信息**

Memory operation failed.

**错误描述**

内存操作失败。

**可能原因**

1. 系统内存泄漏。
2. 系统内存不足。

**处理步骤**

1. 内存不足，请释放内存。
2. 请检查是否内存泄漏。

## 9700002 Parcel读写操作失败

PhonePC/2in1TabletTVWearable

**错误信息**

Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory.

**错误描述**

IPC通信读写Parcel数据失败。

**可能原因**

1. 进程间通信的时候，读取或写入数据对象失败。
2. 读写操作申请内存失败。

**处理步骤**

系统内部工作异常，请稍候重试，或者重启设备尝试。

## 9700003 系统服务失败

PhonePC/2in1TabletTVWearable

**错误信息**

System service operation failed.

**错误描述**

客户端进程请求服务进程时，请求系统服务操作失败。

**可能原因**

1. 系统服务还未启动。
2. 系统服务异常。

**处理步骤**

系统服务内部工作异常，请稍候重试，或者重启设备尝试。

## 9700004 workInfo校验失败

PhonePC/2in1TabletTVWearable

**错误信息**

Check on workInfo failed.

**错误描述**

延迟任务信息参数异常。

**可能原因**

1. workInfo中的bundleName和应用的uid不匹配。
2. 取消或查询延迟任务时，延迟任务不存在。

**处理步骤**

请检查workInfo参数。

## 9700005 StartWork失败

PhonePC/2in1TabletTVWearable

**错误信息**

Calling startWork failed.

**错误描述**

延迟任务申请失败。

**可能原因**

1. 延迟任务已存在。
2. 每个应用uid最多添加10个延迟任务。
3. 重复任务设置的重复时间应至少为20分钟。

**处理步骤**

请检查输入的参数和代码逻辑。
