---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-subscribe-superprivacymode
title: 订阅超级隐私模式状态改变事件
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 超级隐私模式 > 订阅超级隐私模式状态改变事件
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:02+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:5b6f99dc9c7bc782353700a59928362bd35a44598b9615b08d711d0bd8638284
---

## 场景介绍

从6.0.2(22)开始，新增订阅超级隐私模式状态改变事件的能力。

超级隐私模式为用户提供一键关闭敏感器件的能力，管控范围包括位置、相机和麦克风，且随着版本演进，超级隐私模式管控的敏感器件范围会相应调整。应用可通过Device Security Kit提供的接口监听当前超级隐私模式开关状态。

## 约束与限制

本特性需要设备上存在超级隐私模式选项。开发者可通过在设备上选择“设置 > 隐私和安全 > 超级隐私模式”查看超级隐私模式选项。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/5CFdF_VlQmi5YejHgpR4BQ/zh-cn_image_0000002706674376.png)

**流程说明：**

1. 开发者应用调用[on](../harmonyos-references/devicesecurity-superprivacymode-api.md#onsuperprivacymodechange)接口订阅超级隐私模式状态改变事件。
2. Device Security Kit调用回调函数通知开发者应用，
3. 开发者应用根据当前超级隐私模式的状态进行业务处理。
4. 当开发者应用不需要使用超级隐私模式状态时，取消订阅超级隐私模式状态改变事件。

## 接口说明

以下是超级隐私模式状态改变订阅与取消订阅接口，更多接口及使用方法请参见[API参考](../harmonyos-references/devicesecurity-superprivacymode-api.md)。

| 接口名 | 描述 |
| --- | --- |
| [on](../harmonyos-references/devicesecurity-superprivacymode-api.md#onsuperprivacymodechange)(type: 'superPrivacyModeChange', callback: Callback<[SuperPrivacyMode](../harmonyos-references/devicesecurity-superprivacymode-api.md#superprivacymode)>): void | 订阅超级隐私模式状态改变事件 |
| [off](../harmonyos-references/devicesecurity-superprivacymode-api.md#offsuperprivacymodechange)(type: 'superPrivacyModeChange', callback?: Callback<[SuperPrivacyMode](../harmonyos-references/devicesecurity-superprivacymode-api.md#superprivacymode)>): void | 取消订阅超级隐私模式状态改变事件 |

## 开发步骤

1. 导入超级隐私模块及相关公共模块。

   ```typescript
   import { superPrivacyMode } from '@kit.DeviceSecurityKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 定义超级隐私模式状态改变时触发的回调函数。

   ```typescript
   const superPrivacyChangedCallback = (mode: superPrivacyMode.SuperPrivacyMode): void => {
     hilog.info(DOMAIN, TAG, `super privacy mode changed, mode = ${mode}`);
     // ...
   }
   ```
3. 调用[on](../harmonyos-references/devicesecurity-superprivacymode-api.md#onsuperprivacymodechange)接口订阅超级隐私模式状态改变事件。

   ```typescript
   const DOMAIN = 0x0000;
   const TAG = 'SuperPrivacyModeTest';
   ```

   ```typescript
   hilog.info(DOMAIN, TAG, 'start register super privacy mode changed listener');
   try {
     superPrivacyMode.on('superPrivacyModeChange', superPrivacyChangedCallback);
     hilog.info(DOMAIN, TAG, 'register super privacy mode change listener success');
     // ...
   } catch (err) {
     hilog.error(DOMAIN, TAG, `register super privacy changed listener failed, errCode:${err?.code}, errMessage:${err?.message}`);
     // ...
   }
   ```
4. 调用[off](../harmonyos-references/devicesecurity-superprivacymode-api.md#offsuperprivacymodechange)接口取消订阅超级隐私模式状态改变事件。

   ```typescript
   const DOMAIN = 0x0000;
   const TAG = 'SuperPrivacyModeTest';
   ```

   ```typescript
   hilog.info(DOMAIN, TAG, 'start unregister super privacy mode changed listener');
   try {
     superPrivacyMode.off('superPrivacyModeChange', superPrivacyChangedCallback);
     subscribeCallback_ = null;
     // ...
   } catch (err) {
     hilog.error(DOMAIN, TAG, `unregister super privacy changed listener failed, errCode:${err?.code}, errMessage:${err?.message}`);
     // ...
   }
   ```
