---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-enterprise-threat-protection
title: ArkTS API 错误码
breadcrumb: API参考 > 系统 > 安全 > Enterprise Threat Protection Kit（企业威胁防护服务） > ArkTS API > ArkTS API 错误码
category: harmonyos-references
scraped_at: 2026-09-02T15:01:44+08:00
doc_updated_at: 2026-06-12
content_hash: sha256:e510ff5bc9b492698b37a7f58fb842f46cfce6d23ab4e261a7adbc7af1c43ff6
---

**说明** 

以下仅介绍本模块特有错误码，详情请参见[通用错误码说明文档](errorcode-universal.md)。若您的问题仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1023801001 系统内部错误

**错误信息**

System service exception.

**错误描述**

系统内部错误

**可能原因**

系统处于非安全状态（如设备未解锁），或者硬件故障。

**处理步骤**

1. 确认系统状态正常后重试。
2. 如问题仍存在，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1023802001 目标文件不存在

**错误信息**

File not found.

**错误描述**

目标路径的文件不存在。

**可能原因**

目标路径配置错误或文件已被删除。

**处理步骤**

请确认目标路径及文件状态。

## 1023802002 该路径不允许访问/处置

**错误信息**

Access and disposal denied for this path.

**错误描述**

目标路径不允许访问或处置。

**可能原因**

目标路径超出允许[文件访问限制](../harmonyos-guides/enterprisethreatprotection-introduction.md#文件访问限制)或[文件处置限制](../harmonyos-guides/enterprisethreatprotection-introduction.md#文件处置限制)，如权限级别、应用沙箱等限制。

**处理步骤**

请确认路径是否超出允许访问限制和处置限制。

## 1023802003 文件名冲突

**错误信息**

A file with the same name already exists in the restored path.

**错误描述**

恢复路径中有重名文件。

**可能原因**

新旧文件同名导致恢复失败。

**处理步骤**

请检查恢复路径中是否有重名文件，可通过改名、删除旧文件等方式解决错误。

## 1023803001 尝试访问其他用户文件

**错误信息**

Access to other users' files is restricted.

**错误描述**

目标路径是其他用户的文件。

**可能原因**

非本用户账户下的文件资源。

**处理步骤**

确认当前操作用户身份并变更路径至有效目录。

## 1023804001 文件类型无效

**错误信息**

Invalid file type.

**错误描述**

目标路径的文件类型无效。

**可能原因**

当前处置仅支持单文件处置，不支持目录。

**处理步骤**

请检查路径是否为单文件，否则将目标改为单一文件并重新发起操作。

## 1023804002 不支持处置，推荐自行处置

**错误信息**

Disposal is not supported. Please handle it manually.

**错误描述**

目标路径不支持处置。

**可能原因**

目标路径为应用包体路径，推荐采用以下方式处置：

1. 禁止应用运行。
2. 卸载应用。

**处理步骤**

请检查路径是否为应用包体路径，并选择合适的处置方式。具体处置方式请参见[文件访问限制](../harmonyos-guides/enterprisethreatprotection-introduction.md#文件访问限制)和[文件处置限制](../harmonyos-guides/enterprisethreatprotection-introduction.md#文件处置限制)。

## 1023804003 操作无效

**错误信息**

Invalid operation.

**错误描述**

请求的隔离ID无效。

**可能原因**

请求ID格式错误或已无效。

**处理步骤**

请检查隔离ID是否与应用中存储一致，且该隔离ID对应的文件是否为被隔离状态（即存在且未被释放的隔离记录）。

## 1023805001 隔离区空间不足

**错误信息**

Quarantine storage space is full.

**错误描述**

隔离区空间不足。

**可能原因**

隔离区磁盘满载或达到容量上限。

**处理步骤**

1. 查询当前隔离区占用空间及状态。
2. 使用隔离删除接口[removeIsolatedFile](../harmonyos-guides/enterprisethreatprotection-virusremediation-remove.md)对隔离区进行空间清理。

## 1023806001 数据库损坏

**错误信息**

Database corruption detected.

**错误描述**

数据库损坏。

**可能原因**

表结构异常或连接失败。

**处理步骤**

1. 执行初步自检命令或查看日志获取详细错误信息。
2. 如问题仍存在，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1023807001 进程不存在

**错误信息**

Process not found.

**错误描述**

要求处置的进程不存在，或已结束运行。

**可能原因**

进程ID输入错误或进程已自行退出。

**处理步骤**

确认传入的进程ID正确，建议通过任务管理器或其他工具核实目标进程的实际PID。

## 1023807002 系统进程不允许处置

**错误信息**

Access and disposal are denied for this process.

**错误描述**

目标进程为系统关键进程，不允许处置。

**可能原因**

进程为系统进程，不允许处置。

**处理步骤**

若目标进程不属于系统进程，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1023807003 其他用户进程不允许处置

**错误信息**

Access to other users' processes is not allowed.

**错误描述**

目标进程归属于其他用户，当前用户无权限对该进程执行处置操作。

**可能原因**

目标进程由其他用户启动。

**处理步骤**

检查目标进程ID是否属于当前用户。
