---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-pushcommon
title: pushCommon（推送服务公共信息）
breadcrumb: API参考 > 应用服务 > Push Kit（推送服务） > ArkTS API > pushCommon（推送服务公共信息）
category: harmonyos-references
scraped_at: 2026-09-02T15:03:07+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6d5b8dbafde4f8c58f4b4e7c8e54386cf25cc3d45465000def11a5a699e29dcf
---

本模块定义推送服务相关公共接口与枚举，为账号绑定、消息接收、通知内容替换等核心能力提供支撑。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Push.PushService

**起始版本：** 4.0.0(10)

## 导入模块

```typescript
import { pushCommon } from '@kit.PushKit';
```

## AppProfileType

绑定账号类型，为枚举值。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 对于5.1.0(18)以前版本，该枚举值在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。对于5.1.0(18)版本，该枚举值在Phone、Tablet、PC/2in1、Wearable中可正常使用，在其他设备类型中无效果。对于5.1.1(19)及之后版本，该枚举值在Phone、Tablet、PC/2in1、Wearable、TV中均可正常使用。

**起始版本：** 4.0.0(10)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PROFILE\_TYPE\_OS\_DISTRIBUTED\_ACCOUNT | 1 | 华为账号。 |
| PROFILE\_TYPE\_APPLICATION\_ACCOUNT | 2 | 应用账号。 |

## PushPayload

PushPayload是推送服务向应用传递数据的核心接口，开发者可以通过[receiveMessage](push-pushservice.md#pushservicereceivemessage)()接收通知、语音播报等类型消息的数据。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 对于5.1.0(18)以前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。对于5.1.0(18)版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用，在其他设备类型中无效果。对于5.1.1(19)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中均可正常使用。

**起始版本：** 4.0.0(10)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | string | 否 | 否 | 传递给Ability的消息类型，取值范围：  'IM'：语音播报消息  'VoIP'：应用内通话消息  'BACKGROUND'：后台消息  'EMERGENCY'：紧急事件消息（该类型的消息仅对系统应用开放，暂不对外开放申请，开发者无需处理）  'ALERT'：通知消息 |
| data | string | 否 | 否 | 传递给Ability的数据。详见[data取值样例](push-pushcommon.md#data取值样例)（格式化后）。 |

### data取值样例

* type为'IM'时，data取值样例（格式化后）：

  ```json5
  {
      "data": "extraData", // 详情参考ExtensionPayload.extraData
      "header": {
          "token": "MA**"
      },
      "messageAction": 0,
      "notification": { // 详情参考ExtensionPayload.notification
          "bigBody": "bigBodyXX",
          "bigTitle": "bigTitleXX",
          "body": "bodyXX",

          "image": "https://**/image**.png",
          "notifyId": -1,
          "title": "titleXX"
      }
  }
  ```
* type为 'VoIP' 时，data取值样例（格式化后）：

  ```json5
  {
      "data": "extraData", // 详情参考VoIPCallPayload.extraData
      "header": {
          "token": "MA**"
      }
  }
  ```
* type为 'BACKGROUND'时，data取值样例（格式化后）：

  ```json5
  {
      "data": "extraData", // 详情参考BackgroundPayload.extraData
      "header": {
          "token": "MA**"
      }
  }
  ```
* type为 'ALERT'时，无需额外配置data字段：

  ```json5
  {
      "data": "", // data为空字符串
      "header": {
          "token": "MA**"
      },
      "messageAction": 0,
      "notification": { // 详情参考AlertPayload.notification
        "title": "通知标题",
        "body": "通知内容",
        "clickAction": {
          "actionType": 0
        },
        "image":"https://lf*******246.png"
      }
  }
  ```

## RemoteNotificationInfo

应用进程不在前台时，开发者可以通过[onReceiveMessage](push-remote-notification-extension-ability.md#onreceivemessage)()接收语音播报消息的数据，数据由该接口进行传递，继承自[PushPayload](push-pushcommon.md#pushpayload)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 对于5.1.0(18)以前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。对于5.1.0(18)~6.0.2(22)版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用，在其他设备类型中无效果。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中均可正常使用。

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | number | 否 | 否 | 通知id。 |
| type | string | 否 | 否 | 继承自[PushPayload](push-pushcommon.md#pushpayload)，表示传递给[RemoteNotificationExtensionAbility](push-remote-notification-extension-ability.md)的消息类型。 |
| data | string | 否 | 否 | 继承自[PushPayload](push-pushcommon.md#pushpayload)，表示传递给[RemoteNotificationExtensionAbility](push-remote-notification-extension-ability.md)的数据。 |

## RemoteNotificationContent

开发者接收并处理[RemoteNotificationInfo](push-pushcommon.md#remotenotificationinfo)后，通过该接口返回替换后的通知标题、通知内容等属性。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 对于5.1.0(18)以前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。对于5.1.0(18)~6.0.2(22)版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用，在其他设备类型中无效果。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中均可正常使用。

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| title | string | 否 | 是 | 扩展通知标题，将作为发布通知时NotificationRequest对象的[title](js-apis-inner-notification-notificationcontent.md#notificationbasiccontent)。  **说明：**  title从5.0.0(12)起变更为非必填字段。 |
| text | string | 否 | 是 | 扩展通知内容，将作为发布通知时NotificationRequest对象的[text](js-apis-inner-notification-notificationcontent.md#notificationbasiccontent)。  **说明：**  text从5.0.0(12)起变更为非必填字段。 |
| overlayIcon | image.[PixelMap](arkts-apis-image-pixelmap.md) | 否 | 是 | 扩展通知的叠加图标，将作为发布通知时NotificationRequest对象的[overlayIcon](js-apis-inner-notification-notificationrequest.md#notificationrequest-1)。  **说明：**  图片长\*宽建议小于128\*128像素，若超过49152像素，则图片不展示。 |
| badgeNumber | number | 否 | 是 | 增加的角标数量，取值范围为全体整数，当badgeNumber取值小于或等于0时，将忽略本次角标设定。在应用的桌面图标上呈现。该参数将作为发布通知时NotificationRequest对象的[badgeNumber](js-apis-inner-notification-notificationrequest.md)。 |
| setBadgeNumber | number | 否 | 是 | 设置的角标数量，取值范围为全体整数，当设置的角标数量小于或等于0时，清除角标。与badgeNumber同时返回时，优先于badgeNumber，将作为发布通知时NotificationRequest对象的[setBadgeNumber](js-apis-notificationmanager.md)。  **说明：**  起始版本：5.0.0(12)。 |
| wantAgent | [RemoteWantAgent](push-pushcommon.md#remotewantagent) | 否 | 是 | 点击事件时可以替换的数据，将作为发布通知时NotificationRequest对象的[wantAgent](js-apis-inner-notification-notificationrequest.md)。 |

## RemoteWantAgent

点击事件时可以替换的数据。返回[RemoteNotificationContent](push-pushcommon.md#remotenotificationcontent)时，开发者可以通过该接口实现替换后的通知点击行为，例如启动 Ability。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 对于5.1.0(18)以前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。对于5.1.0(18)~6.0.2(22)版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用，在其他设备类型中无效果。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中均可正常使用。

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| abilityName | string | 否 | 否 | 自定义页面名称。 |
| parameters | Record<string, Object> | 否 | 是 | 传递给应用的数据。 |

## VoIPInfo

应用内通话消息数据，继承自[PushPayload](push-pushcommon.md#pushpayload)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 对于6.1.0(23)以前版本，该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、PC/2in1中可正常调用，在其他设备类型中无效果。

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| callId | string | 否 | 否 | 当次呼叫的唯一标识。 |
| type | string | 否 | 否 | 继承自[PushPayload](push-pushcommon.md#pushpayload)，表示传递给[VoIPExtensionAbility](push-voip-ability.md)的消息类型。 |
| data | string | 否 | 否 | 继承自[PushPayload](push-pushcommon.md#pushpayload)，表示传递给[VoIPExtensionAbility](push-voip-ability.md)的数据。 |
