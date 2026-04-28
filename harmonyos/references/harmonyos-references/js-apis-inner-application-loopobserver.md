---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-loopobserver
title: LoopObserver
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 接口依赖的元素及定义 > application > LoopObserver
category: harmonyos-references
scraped_at: 2026-04-28T07:58:41+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:006cef54801f0a4b08dd0fb972a9377ee13d2fd9c62cee0c23a9a4cedf430b76
---

定义异常监听，可以作为[ErrorManager.on](js-apis-app-ability-errormanager.md#errormanageronloopobserver12)的入参监听当前应用主线程事件处理事件。

说明

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { errorManager } from '@kit.AbilityKit';
```

## LoopObserver.onLoopTimeOut

PhonePC/2in1TabletTVWearable

onLoopTimeOut?(timeout: number): void

将在js运行时应用主线程处理事件超时的回调。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| timeout | number | 是 | 返回应用主线程消息实际执行时间。 |

**示例：**

```
1. import { errorManager } from '@kit.AbilityKit';

3. let observer: errorManager.LoopObserver = {
4. onLoopTimeOut(timeout: number) {
5. console.info('Duration timeout: ' + timeout);
6. }
7. };

9. errorManager.on("loopObserver", 1, observer);
```
