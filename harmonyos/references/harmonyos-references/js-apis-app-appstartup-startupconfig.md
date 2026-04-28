---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-appstartup-startupconfig
title: @ohos.app.appstartup.StartupConfig (启动框架配置信息)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > Stage模型能力的接口 > @ohos.app.appstartup.StartupConfig (启动框架配置信息)
category: harmonyos-references
scraped_at: 2026-04-28T07:58:23+08:00
doc_updated_at: 2026-04-13
content_hash: sha256:1e12459a9414d9233ebf942aa4fe2c79b5828f517d4b2c0ef5dd21a50c50dd4e
---

本模块提供[应用启动框架](../harmonyos-guides/app-startup.md)配置信息的定义。

说明

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { StartupConfig } from '@kit.AbilityKit';
```

## StartupConfig

PhonePC/2in1TabletTVWearable

用于配置任务超时时间和启动框架的监听器。详细使用方法可参考[设置启动参数](../harmonyos-guides/app-startup.md#设置启动参数)章节。

**系统能力**：SystemCapability.Ability.AppStartup

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| timeoutMs | number | 否 | 是 | 执行所有启动任务的超时时间（单位：ms），默认值为10000ms。 |
| startupListener | [StartupListener](js-apis-app-appstartup-startuplistener.md) | 否 | 是 | 表示启动框架的监听器，该监听器将在所有启动任务完成时调用。 |

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
