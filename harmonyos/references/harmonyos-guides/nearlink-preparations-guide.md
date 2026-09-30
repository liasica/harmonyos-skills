---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/nearlink-preparations-guide
title: 开发准备
breadcrumb: 指南 > 系统 > 网络 > Connectivity Kit（短距通信服务） > 星闪 > 开发准备
category: harmonyos-guides
scraped_at: 2026-10-01T07:34:31+08:00
doc_updated_at: 2026-09-30
content_hash: sha256:2dddc42882026b2680a302db9619cae2c2d4a7055708818183c5cd1262b3b345
---

开发星闪应用前，需完成设备确认、环境准备与权限申请等准备工作，并可通过查询接口确认设备支持星闪且星闪开关已开启。开发前建议先阅读[星闪常见问题](nearlink-faq-guide.md)中关于服务UUID、事件订阅、SSAP属性描述符与设备地址的说明。

## 开发前检查

1. 请先确认设备支持星闪功能。确认方法：进入“设置 > 星闪和蓝牙”界面（不同产品或系统版本可能为“设置 > 多设备协同”），确认“星闪”选项存在。若选项不存在，则设备不支持星闪功能。
2. 请参考[“应用开发准备”](https://developer.huawei.com/consumer/cn/develop-novice-guide/)完成开发者注册、创建应用、安装开发环境、配置签名信息等基本准备工作，再继续进行以下开发活动。

## 申请星闪权限

开发者需要在应用中动态申请星闪权限ohos.permission.ACCESS\_NEARLINK，包括在应用配置文件中声明此权限，并向用户申请授权。该权限为user\_grant授权方式，申请步骤如下：

1. 在配置文件module.json5中声明权限，声明方式参见[声明权限](declare-permissions.md)。
2. 应用启动时向用户申请授权，申请方式参见[向用户申请授权](request-user-authorization.md)。

**说明** 

* 权限申请建议在Ability创建时一次性完成，并检查授权结果（authResults）；用户拒绝后，调用需要ohos.permission.ACCESS\_NEARLINK权限的星闪接口将返回[201 权限校验失败](../harmonyos-references/errorcode-universal.md#section201-权限校验失败)错误。
* 事件订阅类接口的权限行为参见[星闪常见问题 > 事件订阅类接口的权限要求问题](nearlink-faq-guide.md#事件订阅类接口的权限要求问题)：无权限订阅不会报错，但收不到事件上报。

## 查询是否支持星闪

由于并非所有设备都支持星闪，使用星闪相关功能前可以主动查询当前设备是否支持星闪。

### 接口说明

查询设备是否支持星闪，完整的API说明以及示例代码请参考：[@ohos.nearlink.manager (星闪基础管理能力)](../harmonyos-references/js-apis-nearlink-manager.md)。

| 接口名 | 描述 |
| --- | --- |
| isNearLinkSupported(): boolean | 主动查询当前设备是否支持星闪。 |

### 开发步骤

1. 导入相关模块。

   ```ts
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { manager } from '@kit.ConnectivityKit';
   ```
2. 发起当前设备是否支持星闪的状态查询。

   ```typescript
   try {
     let supported: boolean = manager.isNearLinkSupported();
     // ...
   } catch (err) {
     hilog.error(0x0000, 'testTag',
       `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
   }
   ```

## 查询星闪开关状态

使用星闪前需要在设置应用里手动打开星闪。可以通过主动查询或订阅通知的方式获取星闪开关状态，星闪开关状态变化为STATE\_ON时可以进行相应的业务流程。

### 接口说明

提供主动查询和订阅通知两种获取星闪开关状态的方式，完整的API说明以及示例代码请参考：[@ohos.nearlink.manager (星闪基础管理能力)](../harmonyos-references/js-apis-nearlink-manager.md)。

| 接口名 | 描述 |
| --- | --- |
| getState(): NearlinkState | 主动查询星闪开关状态。 |
| onStateChange(callback: Callback<NearlinkState>): void | 订阅星闪开关状态变化事件。使用callback异步回调。 |
| offStateChange(callback?: Callback<NearlinkState>): void | 取消订阅星闪开关状态变化事件。使用callback异步回调。 |

### 开发步骤

1. 导入相关模块。

   ```typescript
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { manager } from '@kit.ConnectivityKit';
   ```
2. 发起星闪开关状态查询。

   ```typescript
   try {
     let state: manager.NearlinkState = manager.getState();
     // ...
   } catch (err) {
     hilog.error(0x0000, 'testTag',
       `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
   }
   ```
3. 订阅星闪开关状态变化。

   ```typescript
   try {
     manager.onStateChange((state: manager.NearlinkState) => {
       hilog.info(0x0000, 'testTag', `NearLink state changed: ${state}`);
       // ...
     });
   } catch (err) {
     hilog.error(0x0000, 'testTag',
       `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
   }
   ```
4. 取消订阅星闪开关状态变化。

   ```typescript
   try {
     manager.offStateChange();
   } catch (err) {
     hilog.error(0x0000, 'testTag',
       `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
   }
   ```
