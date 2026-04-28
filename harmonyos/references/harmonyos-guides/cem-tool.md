---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cem-tool
title: cem工具
breadcrumb: 指南 > 系统 > 调测调优 > 调试命令 > cem工具
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:26+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:c5e2c51953e210e135386bd50f1937f24fabfa9921c72cef7c141455877c41f5
---

Common Event Manager（公共事件管理工具， 简称cem）是实现公共事件信息打印、发布公共事件等功能的工具，为开发者提供基本的公共事件调试和测试能力，例如打印所有公共事件订阅者、已发送公共事件和接收者、模拟发布公共事件等。

## 环境要求

在使用本工具前，开发者需要先获取[hdc工具](hdc.md#环境准备)，执行hdc shell。

## cem工具命令列表

| 命令 | 描述 |
| --- | --- |
| help | 帮助命令，用于显示cem相关的帮助信息。 |
| publish | 发布命令，用于发布公共事件。 |
| dump | 打印命令，用于打印公共事件相关信息。 |

## 帮助命令（help）

```
1. # 显示cem相关的帮助信息
2. cem help
```

## 发布命令（publish）

```
1. # 发布公共事件
2. cem publish [<options>]
```

**发布命令参数列表**

| 参数 | 参数说明 |
| --- | --- |
| -e/--event | 必选参数，发布事件名称。 |
| -o/--ordered | 可选参数，发布有序事件，默认发布无序事件。 |
| -c/--code | 可选参数，公共事件结果码。 |
| -d/--data | 可选参数，公共事件携带数据。 |
| -h/--help | 帮助信息。 |

**示例**：

```
1. # 发布名称为testevent的公共事件
2. cem publish --event "testevent"
```

```
1. # 发布名称为testevent的有序公共事件，该事件的结果码为100，携带数据内容为“this is data”
2. cem publish -e "testevent" -o -c 100 -d "this is data"
```

## 打印命令（dump）

说明

当前工具区分eng与user版本。dump命令仅支持在eng版本中使用，在user版本中使用会出现报错error: user version cannot use dump。

```
1. # 打印公共事件相关信息
2. cem dump [<options>]
```

**打印命令参数列表**

| 参数 | 参数说明 |
| --- | --- |
| -a/--all | 打印开机以来所有已发送的公共事件及其具体信息。 |
| -e/--event | 查询特定名称事件的具体信息。 |
| -h/--help | 帮助信息。 |

**示例**：

```
1. # 打印公共事件名称为testevent的具体信息
2. cem dump -e "testevent"
```
