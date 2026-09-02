---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-get-aaid
title: 获取AAID
breadcrumb: 指南 > 应用服务 > Push Kit（推送服务） > 获取AAID
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:31+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:f8cdbffb5de3f55dc340a949c98e81142c348caf405d1b58c3fea85c99759ddd
---

AAID（Anonymous Application Identifier）：应用匿名标识符，标识运行在移动智能终端设备上的应用实例，只有该应用实例才能访问该标识符，AAID只存在于应用的安装期，总长度36个字符。与无法重置的设备级硬件ID相比，AAID具有更好的隐私属性。

AAID具有以下特性：

* 匿名化、无隐私风险：AAID和已有的任何标识符都不关联，并且每个应用只能访问应用本身的AAID。
* 同一个设备上，同一个开发者的多个应用，AAID取值不同。
* 同一个设备上，不同开发者的应用，AAID取值不同。
* 不同设备上，同一个开发者的应用，AAID取值不同。
* 不同设备上，不同开发者的应用，AAID取值不同。

## 场景介绍

AAID会在包括但不限于下述场景中发生变化：

* 应用卸载重装。
* 应用调用删除AAID接口。
* 用户恢复出厂设置。
* 用户清除应用数据。

## 约束与限制

获取AAID能力支持Phone、Tablet、PC/2in1设备。并且从5.1.0(18)版本开始，新增支持Wearable设备；从5.1.1(19)版本开始，新增支持TV设备。

## 接口说明

接口返回值有两种返回形式：Callback和Promise回调。下表中仅展示Promise回调形式的接口，Promise和Callback只是返回值方式不一样，功能相同。

| 接口名 | 描述 |
| --- | --- |
| [getAAID](../harmonyos-references/push-aaid-api.md#aaidgetaaid-1)(): Promise<string> | 获取AAID，使用Promise异步返回结果。 |
| [deleteAAID](../harmonyos-references/push-aaid-api.md#aaiddeleteaaid-1)(): Promise<void> | 删除AAID，使用Promise异步返回结果。 |

## 获取AAID

1. 导入AAID模块及相关公共模块。

   ```typescript
   import { AAID } from '@kit.PushKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   const DOMAIN = 0x0000;
   ```
2. 调用AAID.[getAAID](../harmonyos-references/push-aaid-api.md#aaidgetaaid-1)()方法获取AAID信息。

   ```typescript
   try {
     // data为获取的应用匿名标识符
     AAID.getAAID((err: BusinessError, data: string) => {
       if (err) {
         hilog.error(DOMAIN, 'testTag', 'Failed to get AAID: %{public}d %{public}s', err.code, err.message);
       } else {
         hilog.info(DOMAIN, 'testTag', 'Succeeded in getting AAID');
       }
     });
   } catch (err) {
     let e: BusinessError = err as BusinessError;
     hilog.error(DOMAIN, 'testTag', 'Failed to get AAID: %{public}d %{public}s', e.code, e.message);
   }
   ```
