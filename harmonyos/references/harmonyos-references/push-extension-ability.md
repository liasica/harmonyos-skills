---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-extension-ability
title: PushExtensionAbility（推送扩展Ability）
breadcrumb: API参考 > 应用服务 > Push Kit（推送服务） > ArkTS API > PushExtensionAbility（推送扩展Ability）
category: harmonyos-references
scraped_at: 2026-09-02T15:03:06+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0982c89ec1ff52e6b1009afa8ef74865503571404f57d2750869de661afbdd0a
---

**说明** 

仅对系统应用开放，暂不对外开放申请。

应用退至后台后，系统通常会限制其CPU等资源的使用，导致应用无法与服务器完成数据同步。Push Kit提供了应用在后台时仍能更新数据的能力。当用户终端收到开发者发送的拉起应用子进程的后台消息时，Push Kit将拉起应用子进程并将消息内容传递到该进程，开发者可在该进程中完成后台数据处理、数据更新等操作。

PushExtensionAbility为推送扩展Ability，提供获取消息数据和生命周期销毁的回调。有如下约束：

* PushExtensionAbility为独立子进程，轻量级，不允许唤醒主进程。
* 不允许调用通知API、卡片API、窗口API、弹窗API、实况窗API。
* 生命周期根据场景受控，默认小于10秒，超过10秒子进程生命周期结束。

执行ExtensionAbility失败可能会返回错误，请按具体报错信息排查，详见[ArkTS API错误码](push-error-code.md)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Push.PushService

**起始版本：** 4.0.0(10)

## 约束限制

为保障系统安全性和稳定性，防止PushExtensionAbility滥用系统资源，系统对其能力进行管控， 不支持部分模块的引用，详情请参考[附录](push-extension-ability.md#附录)。

## 导入模块

```typescript
import { PushExtensionAbility } from '@kit.PushKit';
```

## 属性

**模型约束：** 属性仅可在Stage模型下使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 对于5.1.0(18)以前版本，该属性在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。对于5.1.0(18)版本，该属性在Phone、Tablet、PC/2in1、Wearable中可正常使用，在其他设备类型中无效果。对于5.1.1(19)及之后版本，该属性在Phone、Tablet、PC/2in1、Wearable、TV中均可正常使用。

**起始版本：** 4.0.0(10)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | [PushExtensionContext](push-extension-context.md) | 否 | 否 | PushExtensionAbility的上下文环境，继承自[ExtensionContext](js-apis-inner-application-extensioncontext.md)。 |

## onReceiveMessage

onReceiveMessage(payload: pushCommon.PushPayload): void

应用继承PushExtensionAbility后接收拉起应用子进程的后台消息数据的接口。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 对于5.1.0(18)以前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。对于5.1.0(18)版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用，在其他设备类型中无效果。对于5.1.1(19)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中均可正常使用。

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| payload | pushCommon.[PushPayload](push-pushcommon.md#pushpayload) | 是 | 拉起应用子进程的后台消息数据。 |

**示例：**

```typescript
import { PushExtensionAbility, pushCommon } from '@kit.PushKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

const LOG_DOMAIN = 0x0000;
const LOG_TAG = 'PushExtAbility';

// 此处以PushExtAbility继承PushExtensionAbility为例
export default class PushExtAbility extends PushExtensionAbility {
  onReceiveMessage(payload: pushCommon.PushPayload): void {
    hilog.info(LOG_DOMAIN, LOG_TAG,'onReceiveMessage');

    try {
      this.updateData(payload.data);
    } catch (err) {
      const e: BusinessError = err as BusinessError;
      hilog.error(LOG_DOMAIN, LOG_TAG, 'updateData failed, code=%{public}d, message=%{public}s', e.code, e.message);
    }
  }

  /**
   * 数据更新
   * 开发者可根据透传数据自定义实现数据更新逻辑
   * @param data 透传数据
   */
  private updateData(data: string): void {
    // 开发者自行实现数据更新逻辑
  }
}
```

## onDestroy

onDestroy(): void

当PushExtensionAbility被销毁时，会执行该回调，建议在该方法中执行资源清理等操作。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 对于5.1.0(18)以前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。对于5.1.0(18)版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用，在其他设备类型中无效果。对于5.1.1(19)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中均可正常使用。

**起始版本：** 4.0.0(10)

**示例：**

```typescript
import { PushExtensionAbility } from '@kit.PushKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

const LOG_DOMAIN = 0x0000;
const LOG_TAG = 'PushExtAbility';

// 此处以PushExtAbility继承PushExtensionAbility为例
export default class PushExtAbility extends PushExtensionAbility {
  onDestroy(): void {
    hilog.info(LOG_DOMAIN, LOG_TAG,'PushExtAbility onDestroy');

    try {
      this.releaseResources();
    } catch (err) {
      const e: BusinessError = err as BusinessError;
      hilog.error(LOG_DOMAIN,LOG_TAG,'releaseResources failed, code=%{public}d, message=%{public}s', e.code, e.message);
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

PushExtensionAbility不支持以下模块的引用。

| Kit | 模块 |
| --- | --- |
| Notification Kit | [@ohos.notification (Notification模块)](js-apis-notification.md)  [@ohos.notificationManager (NotificationManager模块)](js-apis-notificationmanager.md) |
| Form Kit | [@ohos.app.form.formProvider (formProvider)](js-apis-app-form-formprovider.md)  [@ohos.app.form.formInfo (formInfo)](js-apis-app-form-forminfo.md)  [@ohos.app.form.formBindingData (卡片数据绑定类)](js-apis-app-form-formbindingdata.md)  [@ohos.app.form.FormExtensionAbility (FormExtensionAbility)](js-apis-app-form-formextensionability.md)  [@ohos.application.formBindingData (卡片数据绑定类)](js-apis-application-formbindingdata.md)  [@ohos.application.formInfo (formInfo)](js-apis-application-forminfo.md)  [@ohos.application.formProvider (formProvider)](js-apis-application-formprovider.md) |
| ArkUI | [@ohos.prompt (弹窗)](js-apis-prompt.md)  [@ohos.promptAction (弹窗)](js-apis-promptaction.md)  [@ohos.window (窗口)](js-apis-window.md) |
| Live View Kit | [core.liveview.liveViewManager](liveview-liveviewmanager.md) |
| Call Service Kit | [telephony.voipCall](call-voipcall.md) |
