---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/dataguard-introduction
title: Enterprise Data Guard Kit简介
breadcrumb: 指南 > 系统 > 安全 > Enterprise Data Guard Kit（企业数据保护服务） > Enterprise Data Guard Kit简介
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:31+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:c6feb64359d7be3c9460fb6870ed9f62cac36dc7f8d0a7fb35f723d33eefc84e
---

Enterprise Data Guard Kit（企业数据保护服务）为企业安全管控类[MDM](mdm-kit.md)应用提供关键信息资产（KIA）文件的识别、外发管控以及企业恢复密钥的管理能力，支撑企业构建完整的数据防泄漏解决方案，实现企业数据资产可知、可控、可追溯。

目前Enterprise Data Guard Kit提供了两种能力，包括文件分级管控和恢复密钥。

## 场景介绍

* 提供文件扫描和分级标识功能。企业应用获取当前扫描的文件内容，并且自主解析识别文件内容后，对文件进行安全等级标识，构建企业级资产地图。
* 提供管控策略配置能力，支持企业下发分级管控策略、灵活管控敏感文件的外发权限。
* 基于已配置的策略和敏感文件清单，对文件外发等非法行为进行管控，打开时进行水印保护。
* 提供企业恢复密钥的管理能力。

## 约束与限制

### 访问限制

当前文件分级管控仅支持对用户数据进行文件扫描和分级标识。文件扫描仅限于默认路径范围内的子目录，且[获取文件URI](fileguard-get-file-url.md)、[删除指定路径下的文件](fileguard-delete-file.md)以及以只写模式[打开文件](fileguard-openfile.md)的功能仅适用于用户个人数据目录下的绝对路径。

| 文件路径 | 说明 |
| --- | --- |
| /data/service/el2/  /data/app/el1/bundle/public/  /mnt/hmdfs/  /data/app/el1/  /data/app/el2/  /data/app/el3/  /data/app/el4/  /data/app/el5/ | 默认路径范围内的子目录。文件路径与物理路径对应的关系及不同加密分区的差异，请参考[应用沙箱路径和真实物理路径的对应关系](app-sandbox-directory.md#应用沙箱路径和真实物理路径的对应关系)和[获取和修改加密分区](application-context-stage.md#获取和修改加密分区)。 |
| /data/service/el2/{account\_id}/hmdfs/account/files/ | 对应用户的个人数据目录。 |

### 支持的国家和地区

当前仅支持在中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）提供服务。

### 支持的设备

当前设备类型仅支持PC/2in1，支持的设备详见下表。

| 设备类型 | 设备型号 |
| --- | --- |
| PC/2in1 | 华为擎云系列 |

**说明** 

* 文件分级管控能力：

  从API版本26.0.0开始，支持使用[fileGuard.isFileGuardSupported](../harmonyos-references/dataguard-fileguard.md#isfileguardsupported)接口查询当前设备是否支持文件分级管控。
* 企业恢复密钥能力：
  1. 从API版本26.0.0开始，支持使用[recoveryKey.isRecoveryKeySupported](../harmonyos-references/dataguard-recoverykey.md#recoverykeyisrecoverykeysupported)接口查询当前设备是否支持解密数据恢复密钥。
  2. 从API版本26.0.0开始，支持使用[recoveryKey.isRecoveryKeyForResettingPinSupported](../harmonyos-references/dataguard-recoverykey.md#recoverykeyisrecoverykeyforresettingpinsupported)接口查询当前设备是否支持重置锁屏密码恢复密钥。
  3. 从API版本26.0.0开始，支持使用[recoveryKey.isDataVolumeRecoveryKeySupported](../harmonyos-references/dataguard-recoverykey.md#recoverykeyisdatavolumerecoverykeysupported)接口查询当前设备是否支持数据盘恢复密钥。

## 模拟器支持情况

本Kit暂不支持模拟器。
