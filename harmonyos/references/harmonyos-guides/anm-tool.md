---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/anm-tool
title: anm工具
breadcrumb: 指南 > 系统 > 调测调优 > 调试命令 > anm工具
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:27+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:13b5e954e12ac4813b7291998f46642e12555f51559c62f86d6471fa00467afa
---

Advanced Notification Manager（通知管理工具，简称anm）是实现通知打印、设置通知参数等功能的工具，为开发者提供基本的通知调试和测试能力，例如打印已发布通知详细信息、设置通知缓存个数、使能通知等。

## 环境要求

在使用本工具前，开发者需要先获取hdc工具，执行hdc shell。

当前工具仅支持在eng版本中使用，在user版本中使用会出现报错/bin/sh: anm: inaccessible or not found.。

## anm工具命令列表

| 命令 | 描述 |
| --- | --- |
| help | 帮助命令，用于显示anm相关的帮助信息。 |
| dump | 打印命令，用于打印通知相关信息。 |
| setting | 设置命令，用于设置通知参数。 |

## 帮助命令（help）

```
1. # 显示anm相关的帮助信息
2. anm help
```

## 打印命令（dump）

```
1. # 打印通知相关信息
2. anm dump [<options>]
```

**打印命令参数列表**

| 参数 | 参数说明 |
| --- | --- |
| -A/--active | 打印所有活跃的通知信息。 |
| -R/--recent | 打印最近的通知信息。 |
| -D/--distributed | 打印来自其他设备的分布式通知信息。 |
| -b/--bundle | 可选参数，设置指定的Bundle名称打印。 |
| -u/--user-id | 可选参数，设置指定的用户ID打印。 |
| -h/--help | 帮助信息。 |

**示例**：

```
1. # 打印活跃的通知信息
2. anm dump -A
```

## 设置命令（setting）

```
1. # 设置通知参数
2. anm setting [<options>]
```

**设置命令参数列表**

| 参数 | 参数说明 |
| --- | --- |
| -c/--recent-count | 设置保存在内存中的最近通知的最大个数。 |
| -e/--enable-notification | 设置通知使能开关。 |
| -k/--collaboration-switch | 设置通知是否支持跨设备协同至指定类型设备。  anm setting -k <deviceType>:<status>  **说明：** 从API version 18开始，新增支持该命令参数。  deviceType表示需要指定的设备类型。取值范围包括：wearable（智能穿戴设备）、litewearable（轻量级智能穿戴设备）、headset（可穿戴式音频设备）。  status表示需要指定的跨设备协同开关状态。取值为0表示开关为关闭状态，取值为1表示开关为打开状态。 |
| -b/--collaboration-switch-bundle | 设置指定应用的通知是否支持跨设备协同至指定类型设备。  anm setting -b <deviceType>:<bundleName>:<uid>:<status>  **说明：** 从API version 18开始，新增支持该命令参数。  deviceType表示需要指定的设备类型。取值范围包括：wearable（智能穿戴设备）、litewearable（轻量级智能穿戴设备）、headset（可穿戴式音频设备）。  status表示需要指定的跨设备协同开关状态。取值为0表示开关为关闭状态，取值为1表示开关为打开状态。 |
| -o/--collaboration-switch-slot | 设置指定渠道的通知是否支持通知跨设备协同至指定类型设备。  anm setting -o <deviceType>:<slotType>:<status>  **说明：** 从API version 18开始，新增支持该命令参数。  deviceType表示需要指定的设备类型。取值范围包括：wearable（智能穿戴设备）、litewearable（轻量级智能穿戴设备）、headset（可穿戴式音频设备）。  slotType表示需要指定的通知渠道类型。 取值范围参考[SlotType](../harmonyos-references/js-apis-notificationmanager.md#slottype)。  status表示需要指定的跨设备协同开关状态。取值为0表示开关为关闭状态，取值为1表示开关为打开状态。 |
| -h/--help | 帮助信息。 |

**示例**：

```
1. # 设置保存在内存中的最近通知的最大数量为100个
2. anm setting -c 100

4. # 设置通知跨设备协同至wearable类型设备的开关为打开状态
5. anm setting -k wearable:1

7. # 设置包名为example，uid为10100的应用通知跨设备协同至litewearable类型设备的开关为关闭状态
8. anm setting -b litewearable:example:10100:0

10. # 设置渠道类型为0的通知跨设备协同至headset类型设备的开关为打开状态
11. anm setting -o headset:0:1
```
