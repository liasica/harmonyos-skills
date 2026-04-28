---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-web-webnativemessagingextensionability
title: @ohos.web.WebNativeMessagingExtensionAbility (Web Native Messaging Extension Ability)
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS API > @ohos.web.WebNativeMessagingExtensionAbility (Web Native Messaging Extension Ability)
category: harmonyos-references
scraped_at: 2026-04-28T08:05:12+08:00
doc_updated_at: 2026-04-10
content_hash: sha256:4aad6e1eb9ca52f31dd34e9d5ac8ceb6a1372c04ae81a222fbe2f97e4807241b
---

WebNativeMessagingExtensionAbility为开发者提供Web原生消息通信的能力，继承自ExtensionAbility。

说明

本模块首批接口从API version 21开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { WebNativeMessagingExtensionAbility } from '@kit.ArkWeb';
```

## WebNativeMessagingExtensionAbility

PhonePC/2in1TabletTVWearable

为开发者提供Web原生消息通信能力，继承自ExtensionAbility。

### 属性

PhonePC/2in1TabletTVWearable

**系统能力:** SystemCapability.Web.Webview.Core

**模型约束:** 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | [WebNativeMessagingExtensionContext](arkts-apis-web-webnativemessagingextensioncontext.md) | 否 | 否 | Web原生消息通信上下文。 |

### onConnectNative

PhonePC/2in1TabletTVWearable

onConnectNative(info: ConnectionInfo): void

Web原生消息连接建立时回调此方法。

**系统能力:** SystemCapability.Web.Webview.Core

**模型约束:** 此接口仅可在Stage模型下使用。

**参数:**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| info | [ConnectionInfo](arkts-apis-web-webnativemessagingextensionability.md#connectioninfo) | 是 | 连接信息对象。 |

**示例:**

```
1. import { WebNativeMessagingExtensionAbility, ConnectionInfo } from '@kit.ArkWeb';

3. export class MyWebNativeMessagingExtension extends WebNativeMessagingExtensionAbility {
4. onConnectNative(info: ConnectionInfo): void {
5. console.info('Web Native connection established!');
6. console.info(`Connection ID: ${info.connectionId}`);
7. console.info(`Caller bundle: ${info.bundleName}`);
8. // 在此处处理连接建立后的业务逻辑
9. }
10. }
```

### onDisconnectNative

PhonePC/2in1TabletTVWearable

onDisconnectNative(info: ConnectionInfo): void

Web原生消息连接断开时回调此方法。

**系统能力:** SystemCapability.Web.Webview.Core

**模型约束:** 此接口仅可在Stage模型下使用。

**参数:**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| info | [ConnectionInfo](arkts-apis-web-webnativemessagingextensionability.md#connectioninfo) | 是 | 连接信息对象。 |

**示例:**

```
1. import { WebNativeMessagingExtensionAbility, ConnectionInfo } from '@kit.ArkWeb';

3. export class MyWebNativeMessagingExtension extends WebNativeMessagingExtensionAbility {
4. onDisconnectNative(info: ConnectionInfo): void {
5. console.info('Web Native connection closed!');
6. console.info(`Connection ID: ${info.connectionId}`);
7. // 在此处处理连接断开后的清理工作
8. }
9. }
```

### onDestroy

PhonePC/2in1TabletTVWearable

onDestroy(): void

WebNativeMessagingExtensionAbility销毁时回调。

**系统能力:** SystemCapability.Web.Webview.Core

**模型约束:** 此接口仅可在Stage模型下使用。

**示例:**

```
1. import { WebNativeMessagingExtensionAbility } from '@kit.ArkWeb';

3. export class MyWebNativeMessagingExtension extends WebNativeMessagingExtensionAbility {
4. onDestroy(): void {
5. console.info('WebNativeMessagingExtensionAbility is about to be destroyed!');
6. // 在此处释放资源或者执行清理操作
7. }
8. }
```

## ConnectionInfo

PhonePC/2in1TabletTVWearable

Web原生消息连接的信息对象。

**系统能力:** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| connectionId | number | 否 | 否 | 连接的唯一标识符。 |
| bundleName | string | 否 | 否 | 调用方的应用包名。 |
| extensionOrigin | string | 否 | 否 | 调用方扩展的原始URL。 |
| fdRead | number | 否 | 否 | 用于读取数据的管道文件描述符。 |
| fdWrite | number | 否 | 否 | 用于写入数据的管道文件描述符。 |
