---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-remote-notification-extension-ability
title: RemoteNotificationExtensionAbility（通知扩展Ability）
breadcrumb: API参考 > 应用服务 > Push Kit（推送服务） > ArkTS API > RemoteNotificationExtensionAbility（通知扩展Ability）
category: harmonyos-references
scraped_at: 2026-09-02T14:53:30+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:166a79d7f76ef02d4f8514925351d54e43356e2374b49dc154ed8dbb4aeef6c8
---

用户收到应用发送的语音播报消息（如订单、物流类语音提醒）时，若应用进程不在前台，Push Kit将拉起应用子进程并将消息内容传递到该进程。开发者可在该进程中完成业务处理（如语音播报），并返回自定义消息内容，Push Kit将根据该内容展示通知。开发者需在10秒内返回自定义消息内容，否则将默认展示发送消息时携带的原始内容。

RemoteNotificationExtensionAbility为通知扩展Ability，提供获取消息数据和生命周期销毁的回调。有如下约束：

* RemoteNotificationExtensionAbility为独立子进程，轻量级，不允许唤醒主进程。
* 不允许调用通知API、卡片API、窗口API、弹窗API、实况窗API。
* 生命周期根据场景受控，默认小于10秒，超过10秒子进程生命周期结束。

执行ExtensionAbility失败可能会返回错误，请按具体报错信息排查，详见[ArkTS API错误码](push-error-code.md)。

若应用进程在前台，Push Kit将不会弹出通知提醒，开发者可以在应用进程中调用[pushService.receiveMessage](push-pushservice.md#pushservicereceivemessage)接收消息内容并自行完成业务处理。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Push.PushService

**起始版本：** 4.1.0(11)

## 约束限制

为保障系统安全性和稳定性，防止RemoteNotificationExtensionAbility滥用系统资源，系统对其能力进行管控， 不支持部分模块的引用，详情请参考[附录](push-remote-notification-extension-ability.md#附录)。

## 导入模块

```typescript
import { RemoteNotificationExtensionAbility } from '@kit.PushKit';
```

## 属性

**模型约束：** 属性仅可在Stage模型下使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 对于5.1.0(18)以前版本，该属性在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。对于5.1.0(18)~6.0.2(22)版本，该属性在Phone、Tablet、PC/2in1、Wearable中可正常使用，在其他设备类型中无效果。对于6.1.0(23)及之后版本，该属性在Phone、Tablet、PC/2in1、Wearable、TV中均可正常使用。

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | [RemoteNotificationExtensionContext](push-remote-notification-extension-context.md) | 否 | 否 | RemoteNotificationExtensionAbility的上下文环境，继承自[ExtensionContext](js-apis-inner-application-extensioncontext.md)。 |

## onReceiveMessage

onReceiveMessage(remoteNotificationInfo: pushCommon.RemoteNotificationInfo): Promise<pushCommon.RemoteNotificationContent>

应用继承RemoteNotificationExtensionAbility后接收语音播报消息数据的接口，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 对于5.1.0(18)以前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。对于5.1.0(18)~6.0.2(22)版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用，在其他设备类型中无效果。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中均可正常使用。

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| remoteNotificationInfo | pushCommon.[RemoteNotificationInfo](push-pushcommon.md#remotenotificationinfo) | 是 | 语音播报消息数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<pushCommon.[RemoteNotificationContent](push-pushcommon.md#remotenotificationcontent)> | Promise对象，返回替换后的通知内容。 |

**示例：**

```typescript
import { RemoteNotificationExtensionAbility, pushCommon } from '@kit.PushKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

const LOG_DOMAIN = 0x0000;
const LOG_TAG = 'RemoteNotificationExtAbility';

// 此处以RemoteNotificationExtAbility继承RemoteNotificationExtensionAbility为例
export default class RemoteNotificationExtAbility extends RemoteNotificationExtensionAbility {
  async onReceiveMessage(remoteNotificationInfo: pushCommon.RemoteNotificationInfo): Promise<pushCommon.RemoteNotificationContent> {
    hilog.info(LOG_DOMAIN, LOG_TAG, 'onReceiveMessage notifyId: %{public}d', remoteNotificationInfo.id);
    try {
      // 执行语音播报
      await this.playVoice(remoteNotificationInfo);
    } catch (err) {
      const e: BusinessError = err as BusinessError;
      hilog.error(LOG_DOMAIN, LOG_TAG, 'playVoice failed, code=%{public}d, message=%{public}s', e.code, e.message);
    }

    // 构造替换后的通知内容
    const remoteNotificationContent: pushCommon.RemoteNotificationContent = {
      title: 'Default replace title.',
      text: 'Default replace text.',
      badgeNumber: 1,
      wantAgent: {
        abilityName: 'DemoAbility',
        parameters: {
          key: 'Default value'
        }
      }
    };

    return remoteNotificationContent;
  }

  /**
   * 语音播报
   * 开发者可根据通知内容自定义实现播报逻辑
   * @param remoteNotificationInfo 通知内容
   */
  private async playVoice(remoteNotificationInfo: pushCommon.RemoteNotificationInfo): Promise<void> {
    // 开发者自行实现语音播报逻辑
  }
}
```

## onDestroy

onDestroy(): void

当RemoteNotificationExtensionAbility被销毁时，会执行该回调，建议在该方法中执行资源清理等操作。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 对于5.1.0(18)以前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。对于5.1.0(18)~6.0.2(22)版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用，在其他设备类型中无效果。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中均可正常使用。

**起始版本：** 4.1.0(11)

**示例：**

```typescript
import { RemoteNotificationExtensionAbility } from '@kit.PushKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

const LOG_DOMAIN = 0x0000;
const LOG_TAG = 'RemoteNotificationExtAbility';

// 此处以RemoteNotificationExtAbility继承RemoteNotificationExtensionAbility为例
export default class RemoteNotificationExtAbility extends RemoteNotificationExtensionAbility {
  onDestroy(): void {
    hilog.info(LOG_DOMAIN, LOG_TAG, 'RemoteNotificationExtAbility onDestroy');

    try {
      this.releaseResources();
    } catch (err) {
      const e: BusinessError = err as BusinessError;
      hilog.error(LOG_DOMAIN, LOG_TAG, 'releaseResources failed, code=%{public}d, message=%{public}s', e.code, e.message);
    }
  }
  /**
   * 释放资源
   * 开发者根据实际业务自行实现
   */
  private releaseResources(): void {
    // 资源释放逻辑
  }
}
```

## 附录

RemoteNotificationExtensionAbility不支持以下模块的引用。

| Kit | 模块 |
| --- | --- |
| Notification Kit | [@ohos.notification (Notification模块)](js-apis-notification.md)  [@ohos.notificationManager (NotificationManager模块)](js-apis-notificationmanager.md) |
| Form Kit | [@ohos.app.form.formProvider (formProvider)](js-apis-app-form-formprovider.md)  [@ohos.app.form.formInfo (formInfo)](js-apis-app-form-forminfo.md)  [@ohos.app.form.formBindingData (卡片数据绑定类)](js-apis-app-form-formbindingdata.md)  [@ohos.app.form.FormExtensionAbility (FormExtensionAbility)](js-apis-app-form-formextensionability.md)  [@ohos.application.formBindingData (卡片数据绑定类)](js-apis-application-formbindingdata.md)  [@ohos.application.formInfo (formInfo)](js-apis-application-forminfo.md)  [@ohos.application.formProvider (formProvider)](js-apis-application-formprovider.md) |
| ArkUI | [@ohos.prompt (弹窗)](js-apis-prompt.md)  [@ohos.promptAction (弹窗)](js-apis-promptaction.md)  [@ohos.window (窗口)](js-apis-window.md) |
| Live View Kit | [core.liveview.liveViewManager](liveview-liveviewmanager.md) |
| Call Service Kit | [telephony.voipCall](call-voipcall.md) |
