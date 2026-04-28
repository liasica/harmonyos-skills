---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicedebug-tool
title: devicedebug工具
breadcrumb: 指南 > 系统 > 调测调优 > 调试命令 > 命令行工具 > devicedebug工具
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:28+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:30a451076a8f0dba65f2ee8acdbe21f6d6a8b8117a1f44de4c584f55bed5b9a9
---

devicedebug工具向开发者提供对调试应用发送信号的能力，目前仅支持向AMS管理的debug类型的应用进程的pid发送signal信号，达到终止对应pid进程的能力。

说明

在使用本工具前，开发者需要先获取hdc工具，执行hdc shell。

**表1** devicedebug工具命令列表

| 命令 | 描述 |
| --- | --- |
| help/-h | 帮助命令，显示devicedebug支持的命令信息。 |
| kill | 终止进程命令，用来终止对应pid进程。 |

## 帮助命令

```
1. devicedebug help
```

**表2** help命令列表

| 命令 | 描述 |
| --- | --- |
| devicedebug help | 显示devicedebug支持的命令信息。 |

示例：

```
1. # 显示帮助信息。
2. devicedebug help
```

## 终止进程命令

```
1. devicedebug kill
```

用于向debug类型的应用进程发送signal（1-64）信号，应用进程接收到信号后终止对应pid进程。

**表3** kill命令列表

| 命令 | 描述 |
| --- | --- |
| help/-h | 帮助信息。 |
| -<signal> <pid> | 必选字段，signal（1-64）为终止信号，终止pid对应的debug类型的应用进程。 |

**返回值**：

当pid对应的进程为非应用进程时，返回"devicedebug: kill: {pid}: No such app process"；当pid对应的进程为非debug类型的应用进程时，返回"devicedebug: kill: process: {pid} is not debuggable app"。

示例：

```
1. # 以终止12111进程，signal信号9为例。
2. devicedebug kill -9 12111
```
