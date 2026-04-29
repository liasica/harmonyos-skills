---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-getsuperprivacymode
title: 查询当前状态场景
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 超级隐私模式 > 查询当前状态场景
category: harmonyos-guides
scraped_at: 2026-04-29T13:31:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:973712a9ca263ee722c71bd95a543d673a709a5ced2ea4f262f29434f2d0b713
---

## 场景介绍

从6.0.2(22)开始，新增了查询设备当前超级隐私模式状态的功能。

超级隐私模式为用户提供一键关闭敏感器件的能力，管控范围包括位置、相机和麦克风，且随着版本演进，超级隐私模式管控的敏感器件范围会相应调整。应用可通过Device Security Kit提供的接口查询当前超级隐私模式开关状态。

## 约束与限制

本特性需要设备上存在超级隐私模式选项。开发者可通过在设备上选择“设置 > 隐私和安全 > 超级隐私模式”查看超级隐私模式选项。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/EuOK6-e0QNeohg2Qvycv9A/zh-cn_image_0000002558605248.png?HW-CC-KV=V1&HW-CC-Date=20260429T053142Z&HW-CC-Expire=86400&HW-CC-Sign=DD3D3B3F2D076458818A8BE67D25EDEAE1957700E95651751BEF06E4192BEDE4)

**流程说明：**

1. 开发者应用查询当前超级隐私模式状态。
2. Device Security Kit接口同步返回当前超级隐私模式状态给HAP应用。
3. 应用根据返回的超级隐私模式状态进行业务处理。

## 接口说明

以下是超级隐私模式状态查询接口，更多接口及使用方法请参见[API参考](../harmonyos-references/devicesecurity-superprivacymode-api.md)。

| 接口名 | 描述 |
| --- | --- |
| [getSuperPrivacyMode](../harmonyos-references/devicesecurity-superprivacymode-api.md#getsuperprivacymode)() : Promise<[SuperPrivacyMode](../harmonyos-references/devicesecurity-superprivacymode-api.md#superprivacymode)> | 查询当前超级隐私模式状态 |

## 开发步骤

1. 导入超级隐私模块及相关公共模块。

   ```
   1. import { superPrivacyMode } from '@kit.DeviceSecurityKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 查询超级隐私模式状态改变事件。

   ```
   1. const DOMAIN = 0x0000;
   2. const TAG = "SuperPrivacyModeTest";

   4. let mode: superPrivacyMode.SuperPrivacyMode = superPrivacyMode.SuperPrivacyMode.OFF;
   5. try {
   6. mode = await superPrivacyMode.getSuperPrivacyMode();
   7. hilog.info(DOMAIN, TAG, `Super privacy mode = ${mode}`);
   8. } catch (err) {
   9. hilog.error(DOMAIN, TAG, `call getSuperPrivacyMode interface failed, errCode:${err?.code}, errMessage:${err?.message}`);
   10. }
   ```
