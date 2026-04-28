---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-appstartup-startuplistener
title: @ohos.app.appstartup.StartupListener (启动框架任务监听器)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > Stage模型能力的接口 > @ohos.app.appstartup.StartupListener (启动框架任务监听器)
category: harmonyos-references
scraped_at: 2026-04-28T07:58:23+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:e99ced48a8ecc05701cf9150c3fbdfd337f513a3d2ffb3eab6df9e9adef9c9bd
---

本模块提供[应用启动框架](../harmonyos-guides/app-startup.md)任务监听器的定义。

说明

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { StartupListener } from '@kit.AbilityKit';
```

## StartupListener.onCompleted

PhonePC/2in1TabletTVWearable

onCompleted?(error: BusinessError<void>): void

在所有启动任务完成时调用。

**系统能力**：SystemCapability.Ability.AppStartup

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| error | [BusinessError<void>](js-apis-base.md#businesserror) | 是 | 错误信息。 |

**示例：**

```
1. import { StartupConfig, StartupConfigEntry, StartupListener } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. export default class MyStartupConfigEntry extends StartupConfigEntry {
6. onConfig() {
7. hilog.info(0x0000, 'testTag', `onConfig`);
8. let onCompletedCallback = (error: BusinessError<void>) => {
9. hilog.info(0x0000, 'testTag', `onCompletedCallback`);
10. if (error) {
11. hilog.error(0x0000, 'testTag', 'onCompletedCallback: %{public}d, message: %{public}s', error.code,
12. error.message);
13. } else {
14. hilog.info(0x0000, 'testTag', `onCompletedCallback: success.`);
15. }
16. };
17. let startupListener: StartupListener = {
18. 'onCompleted': onCompletedCallback
19. };
20. let config: StartupConfig = {
21. 'timeoutMs': 10000,
22. 'startupListener': startupListener
23. };
24. return config;
25. }
26. }
```
