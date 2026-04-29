---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-selectfraudmessage
title: 获取诈骗消息
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 反诈选择器 > 获取诈骗消息
category: harmonyos-guides
scraped_at: 2026-04-29T13:31:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ef76738f3e4ff0fdd9bd5a658361f3040d0946caf49d9a9c4dd0bb498080c14c
---

## 场景介绍

应用通过调用Device Security Kit的接口获取诈骗消息信息，用于反诈业务，比如对诈骗消息进行举报。

## 约束与限制

当前能力仅支持手机、平板设备。仅提供给反诈类应用使用。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/NsloJY9CQ0uOd0b6nBpdZg/zh-cn_image_0000002589324769.png?HW-CC-KV=V1&HW-CC-Date=20260429T053139Z&HW-CC-Expire=86400&HW-CC-Sign=5C8BEA57AF0999A4F6E63AE08EFFACCC5D2318ED0CDA9C919DB4BC2636B33073)

**流程说明：**

1. 用户在开发者应用上选择举报诈骗消息功能。
2. 开发者应用调用Device Security Kit的接口拉起诈骗消息选择器。
3. 用户在诈骗消息选择器中选择诈骗消息。
4. Device Security Kit调用回调函数通知开发者应用，开发者应用根据诈骗消息进行业务处理。

## 接口说明

以下是获取诈骗消息相关接口，更多接口及使用方法请参见[API参考](../harmonyos-references/devicesecurity-antifraudpicker-api.md)。

| 接口名 | 描述 |
| --- | --- |
| selectFraudMessage(context: common.Context, options?: AntifraudMessageOptions): Promise<AntifraudMessageResult> | 获取诈骗消息信息。 |

## 开发步骤

说明

* 在开发准备过程中，需要申请权限：ohos.permission.USE\_FRAUD\_MESSAGES\_PICKER。
* 只允许清单内的应用申请该权限，申请方式请参考：[申请使用受限权限](declare-permissions-in-acl.md)
* 开发者需向用户说明数据使用的目的、方式和范围。

1. 导入Device Security Kit模块及相关公共模块。

   ```
   1. import { antifraudPicker} from '@kit.DeviceSecurityKit';
   2. import { BusinessError} from '@kit.BasicServicesKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';
   4. import { common} from '@kit.AbilityKit';
   ```
2. 调用selectFraudMessage接口获取诈骗消息信息。

   ```
   1. const TAG = "AntifraudPickerJsTest";

   3. // 请求获取诈骗消息信息，并进行业务处理
   4. let options: antifraudPicker.AntifraudMessageOptions = {
   5. maxSelectNumber: 5
   6. };
   7. try {
   8. hilog.info(0x0000, TAG, 'SelectFraudMessage begin.');
   9. let context = this.getUIContext().getHostContext();
   10. const result: antifraudPicker.AntifraudMessageResult = await antifraudPicker.selectFraudMessage(context, options);
   11. } catch (err) {
   12. let e: BusinessError = err as BusinessError;
   13. hilog.error(0x0000, TAG, 'SelectFraudMessage failed: %{public}d %{public}s', e.code, e.message);
   14. }
   ```
