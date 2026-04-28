---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-selectfraudcalllog
title: 获取诈骗通话记录
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 反诈选择器 > 获取诈骗通话记录
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:01+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1f4d993de873fc9dfadb0d2f19cf53d10d078fd072ee52fdd702597d7ecb8a1a
---

## 场景介绍

应用通过调用Device Security Kit的接口获取诈骗通话记录，用于反诈业务，比如对诈骗通话记录进行举报。

## 约束与限制

当前能力仅支持手机、平板设备。仅提供给反诈类应用使用。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/zOeczbVfR3ez-BfU3-jumA/zh-cn_image_0000002583478403.png?HW-CC-KV=V1&HW-CC-Date=20260427T234301Z&HW-CC-Expire=86400&HW-CC-Sign=BD01D4348BEAFDE60F8EFF77F251C6DA9311D72BEAB8A229191FF6C1F4F37607)

**流程说明：**

1. 用户在开发者应用上选择举报诈骗通话记录功能。
2. 开发者应用调用Device Security Kit的接口拉起诈骗通话记录选择器。
3. 用户在诈骗通话记录选择器中选择诈骗通话记录。
4. Device Security Kit调用回调函数通知开发者应用，开发者应用根据诈骗通话记录信息进行业务处理。

## 接口说明

以下是获取诈骗通话记录相关接口，更多接口及使用方法请参见[API参考](../harmonyos-references/devicesecurity-antifraudpicker-api.md)。

| 接口名 | 描述 |
| --- | --- |
| selectFraudCallLog(context: common.Context, options?: AntifraudCallLogOptions): Promise<AntifraudCallLogResult> | 获取诈骗通话记录信息。 |

## 开发步骤

说明

* 在开发准备过程中，需要申请权限：ohos.permission.USE\_FRAUD\_CALL\_LOG\_PICKER。
* 只允许清单内的应用申请该权限，申请方式请参考：[申请使用受限权限](declare-permissions-in-acl.md)
* 开发者需向用户说明数据使用的目的、方式和范围。

1. 导入Device Security Kit模块及相关公共模块。

   ```
   1. import { securityAudit } from '@kit.DeviceSecurityKit';
   2. import { BusinessError} from '@kit.BasicServicesKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';
   4. import { common} from '@kit.AbilityKit';
   ```
2. 调用selectFraudCallLog接口获取诈骗通话记录信息。

   ```
   1. const TAG = "AntifraudPickerJsTest";

   3. // 请求获取诈骗通话记录信息，并进行业务处理
   4. let options: antifraudPicker.AntifraudCallLogOptions = {
   5. maxSelectNumber: 5
   6. };
   7. try {
   8. hilog.info(0x0000, TAG, 'SelectFraudCallLog begin.');
   9. let context = this.getUIContext().getHostContext();
   10. const result: antifraudPicker.AntifraudCallLogResult = await antifraudPicker.selectFraudCallLog(context, options);
   11. } catch (err) {
   12. let e: BusinessError = err as BusinessError;
   13. hilog.error(0x0000, TAG, 'SelectFraudCallLog failed: %{public}d %{public}s', e.code, e.message);
   14. }
   ```
