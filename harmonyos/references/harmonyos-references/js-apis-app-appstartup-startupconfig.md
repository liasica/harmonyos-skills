---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-appstartup-startupconfig
title: "@ohos.app.appstartup.StartupConfig (启动框架配置信息)"
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > Stage模型能力的接口 > @ohos.app.appstartup.StartupConfig (启动框架配置信息)
category: harmonyos-references
scraped_at: 2026-09-02T15:00:33+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a3bf7dc7c0792443db7def649b774927e9a9581b6bdbf30af011b555972c684c
---

本模块提供[应用启动框架](../harmonyos-guides/app-startup.md)配置信息的定义。

**说明** 

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

## 导入模块

```js
import { StartupConfig } from '@kit.AbilityKit';
```

## StartupConfig

用于配置任务超时时间和启动框架的监听器。详细使用方法可参考[设置启动参数](../harmonyos-guides/app-startup.md#设置启动参数)章节。

**系统能力**：SystemCapability.Ability.AppStartup

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| timeoutMs | number | 否 | 是 | 执行所有启动任务的超时时间（单位：ms），默认值为10000ms。超时后启动框架会停止等待，并通过startupListener.onCompleted回调返回超时错误。超时不会中断正在执行的启动任务，但会影响后续任务的执行。 |
| startupListener | [StartupListener](js-apis-app-appstartup-startuplistener.md) | 否 | 是 | 启动框架的监听器，该监听器将在所有启动任务完成时调用。未设置该参数时，不进行回调通知。 |

**示例：**

```ts
import { StartupConfig, StartupConfigEntry, StartupListener } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class MyStartupConfigEntry extends StartupConfigEntry {
  onConfig() {
    hilog.info(0x0000, 'testTag', `onConfig`);
    let onCompletedCallback = (error: BusinessError<void>) => {
      hilog.info(0x0000, 'testTag', `onCompletedCallback`);
      if (error) {
        hilog.error(0x0000, 'testTag', 'onCompletedCallback: %{public}d, message: %{public}s', error.code,
          error.message);
      } else {
        hilog.info(0x0000, 'testTag', `onCompletedCallback: success.`);
      }
    };
    let startupListener: StartupListener = {
      'onCompleted': onCompletedCallback
    };
    let config: StartupConfig = {
      'timeoutMs': 10000,
      'startupListener': startupListener
    };
    return config;
  }
}
```
