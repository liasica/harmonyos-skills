---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/os-account-introduction
title: 系统账号介绍
breadcrumb: 指南 > 系统 > 基础功能 > Basic Services Kit（基础服务） > 账号管理 > 系统账号介绍
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:36+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d5a6ae36e3819d03f792ea5961c41574af1844e85330a9dd89314691426d6e08
---

## 系统账号ID体系

在HarmonyOS中，每个系统账号在创建时都会被分配一个唯一的整型标识，称为**系统账号ID**，对应[OsAccountInfo](../harmonyos-references/js-apis-osaccount.md#osaccountinfo)中的localId字段。系统账号ID按用途可划分为以下类别：

| 范围 | 类别 | 用途 |
| --- | --- | --- |
| ID=0 | 系统级公共服务账号 | 系统级服务与应用安装并运行在此账号下。 |
| ID=1 | 企业级公共服务账号 | 企业级服务与应用安装并运行在此账号下。 |
| ID=2~99 | 预留的系统账号 | 系统预留，暂未定义。 |
| ID=100+ | 自然人用户账号 | 由自然人使用的账号，ID从100开始。 |

**说明** 

各类系统账号下应用的安装规格，请参考[应用安装说明文档](bm-tool.md#userid)。

## 相关文档

* [OsAccountInfo](../harmonyos-references/js-apis-osaccount.md#osaccountinfo)
