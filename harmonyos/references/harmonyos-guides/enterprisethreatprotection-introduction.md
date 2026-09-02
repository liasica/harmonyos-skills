---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisethreatprotection-introduction
title: Enterprise Threat Protection Kit简介
breadcrumb: 指南 > 系统 > 安全 > Enterprise Threat Protection Kit（企业威胁防护服务） > Enterprise Threat Protection Kit简介
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:31+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:67983aeb4aff7c89a69a044838d5ae298bdc47acbbbcbe6268f22e9966cbc7b7
---

Enterprise Threat Protection Kit（企业威胁防护服务）为企业开发者提供了一套构建安全防护类应用的核心能力，旨在助力上层应用快速构建完整的终端安全防护解决方案，其核心在于**文件访问与处置**和**进程处置**功能。文件访问与处置功能通过对文件进行安全、高效地扫描以识别潜在威胁，并对已识别的威胁文件执行隔离、恢复或删除等操作，从而有效保护企业设备上的数据安全。进程处置功能提供了对运行中进程进行安全管控的核心能力，当检测到恶意或可疑进程时，该功能可帮助安全应用在规格范围内，对威胁进程执行精准的终止操作，切断恶意代码的执行路径，阻止其进一步破坏系统或窃取数据。

## 场景介绍

在文件访问与处置场景下，开发者应支持安全防护类应用对文件进行扫描与威胁识别、威胁文件隔离、误报文件恢复、威胁文件清除以及隔离文件查询等功能，以实现从检测到处置的全流程防护。具体包括：

* 文件扫描与威胁识别：支持打开文件并对文件进行安全扫描，识别潜在威胁文件。
* 威胁文件隔离：可将检测到的威胁文件安全转移至隔离区。
* 误报文件恢复：支持将误判文件从隔离区还原至原位置。
* 威胁文件清除：可永久删除隔离区中的威胁文件。
* 隔离文件查询：提供已隔离文件信息的查询功能。

在进程处置场景下，支持三方杀软对规格范围内的进程进行终止操作。

## 约束与限制

### 支持的国家/地区

当前仅支持在中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）提供服务。

### 支持的设备

本Kit仅适用于PC/2in1。

### 文件访问限制

**注意** 

访问和处置操作受限于应用类型，请确保应用为调试类型或企业应用。

当前文件访问能力仅支持对用户数据和必要应用包体进行扫描，默认路径范围包含以下目录：

| 目录 | 说明 |
| --- | --- |
| 用户公共目录 | N/A |
| 云盘目录 | 建议只访问本地文件，可通过[Stat](../harmonyos-references/js-apis-file-fs.md#stat)查询文件具体信息。 |
| 外部存储目录 | N/A |
| 应用el2级别加密数据目录 | 目录详述见[应用沙箱目录](app-sandbox-directory.md)。 |
| 应用安装包目录 | 仅支持调试类型的应用及企业应用。 |
| 网络邻居目录 | N/A |
| 兼容应用数据目录 | N/A |

### 文件处置限制

| 目录 | 说明 |
| --- | --- |
| 用户公共目录 | N/A |
| 云盘目录 | 仅支持处置本地文件。 |
| 外部存储目录 | 本服务不支持处置外部存储目录文件，建议调用方自行处置。 |
| 应用el2级别加密数据目录 | 目录详述见[应用沙箱目录](app-sandbox-directory.md)。 |
| 应用安装包目录 | 不支持处置，建议以应用维度处置，可通过[addDisallowedRunningBundlesSync](../harmonyos-references/js-apis-enterprise-applicationmanager.md#applicationmanageradddisallowedrunningbundlessync)添加应用至应用运行禁止名单，添加至禁止名单的应用不允许在当前/指定用户下运行。或通过[bundleManager.uninstall](../harmonyos-references/js-apis-enterprise-bundlemanager.md#bundlemanageruninstall)卸载应用。 |
| 网络邻居目录 | 不支持处置，建议企业开发者自行处置。 |
| 兼容应用数据目录 | N/A |

### 进程处置限制

进程处置功能不支持处置系统进程。

## 模拟器支持情况

本Kit暂不支持模拟器。
