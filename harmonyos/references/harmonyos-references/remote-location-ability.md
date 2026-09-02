---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-location-ability
title: RemoteLocationExtensionAbility（定位扩展Ability）
breadcrumb: API参考 > 应用服务 > Push Kit（推送服务） > ArkTS API > RemoteLocationExtensionAbility（定位扩展Ability）
category: harmonyos-references
scraped_at: 2026-09-02T15:03:07+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:5d98e1f3fc7785960d4b2c2b33c221a2222e6ab578ad11781bc9cc306a771510
---

**说明** 

定位扩展Ability目前为预留能力，暂未开放使用。

位置共享消息用于提供与地理位置紧密相关的即时服务和个性化体验，此功能需要用户预先授权应用[ohos.permission.LOCATION\_IN\_BACKGROUND](../harmonyos-guides/permissions-for-all-user.md#ohospermissionlocation_in_background)权限。当用户终端收到开发者发送的位置共享消息后，Push Kit将拉起应用子进程，开发者可在该进程中执行获取位置、处理数据等操作。

RemoteLocationExtensionAbility为定位扩展Ability，提供获取消息数据和生命周期销毁的回调。有如下约束：

* RemoteLocationExtensionAbility为独立子进程，轻量级，不允许唤醒主进程。
* 不允许调用通知API、卡片API。
* 生命周期根据场景受控，默认小于10秒，超过10秒子进程生命周期结束。

执行ExtensionAbility失败可能会返回错误，请按具体报错信息排查，详见[ArkTS API错误码](push-error-code.md)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Push.PushService

**起始版本：** 4.1.0(11)

## 约束限制

为保障系统安全性和稳定性，防止RemoteLocationExtensionAbility滥用系统资源，系统对其能力进行管控， 不支持部分模块的引用，详情请参考[附录](remote-location-ability.md#附录)。

## 导入模块

```typescript
import { RemoteLocationExtensionAbility } from '@kit.PushKit';
```

## 属性

**模型约束：** 属性仅可在Stage模型下使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 该属性在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | [RemoteLocationExtensionContext](remote-location-context.md) | 否 | 否 | RemoteLocationExtensionAbility的上下文环境，继承自[ExtensionContext](js-apis-inner-application-extensioncontext.md)。 |

## onReceiveMessage

onReceiveMessage(payload: pushCommon.PushPayload): Promise<void>

应用继承RemoteLocationExtensionAbility后接收位置共享消息数据的接口，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 该接口在Phone、Tablet、PC/2in1中可正常调用，在其他设备类型中无效果。

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| payload | pushCommon.[PushPayload](push-pushcommon.md#pushpayload) | 是 | 位置共享消息数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```typescript
import { RemoteLocationExtensionAbility, pushCommon } from '@kit.PushKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { geoLocationManager } from '@kit.LocationKit';
import { BusinessError } from '@kit.BasicServicesKit';

const LOG_DOMAIN = 0x0000;
const LOG_TAG = 'RemoteLocationExtAbility';

// 此处以RemoteLocationExtAbility继承RemoteLocationExtensionAbility为例
export default class RemoteLocationExtAbility extends RemoteLocationExtensionAbility {
  async onReceiveMessage(payload: pushCommon.PushPayload): Promise<void> {
    hilog.info(LOG_DOMAIN, LOG_TAG, 'onReceiveMessage, payload: %{public}s', JSON.stringify(payload));

    try {
      // 获取实时位置
      await this.handleLocationRequest();
    } catch (err) {
      const e: BusinessError = err as BusinessError;
      hilog.error(LOG_DOMAIN, LOG_TAG, 'handleLocationRequest failed: code=%{public}d, message=%{public}s', e.code, e.message);
    }
  }
  /**
   * 获取实时位置
   */
  private async handleLocationRequest(): Promise<void> {
    const locationEnabled = geoLocationManager.isLocationEnabled();
    if (!locationEnabled) {
      hilog.error(LOG_DOMAIN, LOG_TAG, 'LocationEnabled is close');
      return;
    }

    const request: geoLocationManager.SingleLocationRequest = {
      'locatingPriority': geoLocationManager.LocatingPriority.PRIORITY_LOCATING_SPEED,
      'locatingTimeoutMs': 10000
    };
    const position = await geoLocationManager.getCurrentLocation(request);
    // 您可对position进行自行处理
  }
}
```

## onDestroy

onDestroy(): void

当RemoteLocationExtensionAbility被销毁时，会执行该回调，建议在该方法中执行资源清理等操作。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 该接口在Phone、Tablet、PC/2in1中可正常调用，在其他设备类型中无效果。

**起始版本：** 4.1.0(11)

**示例：**

```typescript
import { RemoteLocationExtensionAbility } from '@kit.PushKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

const LOG_DOMAIN = 0x0000;
const LOG_TAG = 'RemoteLocationExtAbility';
 
// 此处以RemoteLocationExtAbility继承RemoteLocationExtensionAbility为例
export default class RemoteLocationExtAbility extends RemoteLocationExtensionAbility {
  onDestroy(): void {
    hilog.info(LOG_DOMAIN, LOG_TAG, 'RemoteLocationExtAbility onDestroy');

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

RemoteLocationExtensionAbility不支持以下模块的引用。

| Kit | 模块 |
| --- | --- |
| Notification Kit | [@ohos.notification (Notification模块)](js-apis-notification.md)  [@ohos.notificationManager (NotificationManager模块)](js-apis-notificationmanager.md) |
| Form Kit | [@ohos.app.form.formProvider (formProvider)](js-apis-app-form-formprovider.md)  [@ohos.app.form.formInfo (formInfo)](js-apis-app-form-forminfo.md)  [@ohos.app.form.formBindingData (卡片数据绑定类)](js-apis-app-form-formbindingdata.md)  [@ohos.app.form.FormExtensionAbility (FormExtensionAbility)](js-apis-app-form-formextensionability.md)  [@ohos.application.formBindingData (卡片数据绑定类)](js-apis-application-formbindingdata.md)  [@ohos.application.formInfo (formInfo)](js-apis-application-forminfo.md)  [@ohos.application.formProvider (formProvider)](js-apis-application-formprovider.md) |
| Call Service Kit | [telephony.voipCall](call-voipcall.md) |
