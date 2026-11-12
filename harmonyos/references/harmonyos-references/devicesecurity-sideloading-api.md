---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-sideloading-api
title: Sideloading（侧载安全管控）
breadcrumb: API参考 > 系统 > 安全 > Device Security Kit（设备安全服务） > ArkTS API > Sideloading（侧载安全管控）
category: harmonyos-references
scraped_at: 2026-11-12T09:55:22+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:df973d229ea3011bcca5d5ff1d50b6fd7f3ad66cc945111b724fe3739449e77a
---

本模块提供侧载场景的安全控制能力，应用可以判断外部二进制文件是否允许加载，以支撑侧载安全管控业务。

**起始版本：** 26.0.1

## 导入模块

```typescript
import { sideloading } from '@kit.DeviceSecurityKit';
```

## sideloading.isExternalBinaryLoadingEnabled

isExternalBinaryLoadingEnabled(): Promise<boolean>

查询设备是否允许加载外部二进制文件。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.SecurityPrivacyServer

**起始版本：** 26.0.1

**设备行为差异：**

本接口实际支持的设备类型范围（PC/2in1）小于其所属系统能力支持的设备类型范围（Phone、Tablet、TV）。因硬件能力限制，该接口在Phone、Car、Wearable、Tv设备中调用将返回[1006205002](errorcode-devicesecurity-sideloading.md#section1006205002-侧载安全管控不支持)错误码。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示允许加载外部二进制文件；返回false表示不允许加载外部二进制文件。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-devicesecurity-sideloading.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1006205000 | Internal error. Possible causes: 1.System is busy or resources are insufficient; 2.Abnormal system environment. Please try again later, you can check the logs for more information. |
| 1006205002 | Sideloading is not supported. |

**示例：**

```typescript
import { sideloading } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "SideloadingTest";

try {
  hilog.info(0x0000, TAG, 'isExternalBinaryLoadingEnabled begin.');
  const result: boolean = await sideloading.isExternalBinaryLoadingEnabled();
  hilog.info(0x0000, TAG, 'isExternalBinaryLoadingEnabled result: %{public}s', result.toString());
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'isExternalBinaryLoadingEnabled failed: %{public}d %{public}s', e.code, e.message);
}
```

## sideloading.enableExternalBinaryLoadingOnSetting

enableExternalBinaryLoadingOnSetting(context: common.Context): Promise<ExternalBinaryLoadingStatus>

用于[UIAbility](js-apis-app-ability-uiability.md#uiability)或[UIExtensionAbility](js-apis-app-ability-uiextensionability.md#uiextensionability)弹窗请求用户设置二进制加载管控开关状态，返回本次请求的用户选择开关的结果。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.SecurityPrivacyServer

**起始版本：** 26.0.1

**设备行为差异：**

本接口实际支持的设备类型范围（PC/2in1）小于其所属系统能力支持的设备类型范围（Phone、Tablet、TV）。因硬件能力限制，该接口在Phone、Car、Wearable、Tv设备中调用将返回[1006205002](errorcode-devicesecurity-sideloading.md#section1006205002-侧载安全管控不支持)错误码。

**参数：**

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 加载外部二进制文件的UIAbility或UIExtensionAbility的上下文。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ExternalBinaryLoadingStatus](devicesecurity-sideloading-api.md#externalbinaryloadingstatus)> | Promise对象。返回外部二进制文件加载状态。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-devicesecurity-sideloading.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1006205000 | Internal error. Possible causes: 1.System is busy or resources are insufficient; 2.Abnormal system environment. Please try again later, you can check the logs for more information. |
| 1006205001 | Invalid parameter. Possible causes: 1. The context is invalid because it does not belong to the application itself. |
| 1006205002 | Sideloading is not supported. |

**示例：**

```typescript
import { sideloading } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "SideloadingTest";

try {
  hilog.info(0x0000, TAG, 'enableExternalBinaryLoadingOnSetting begin.');
  let context = getContext();
  const result: sideloading.ExternalBinaryLoadingStatus = await sideloading.enableExternalBinaryLoadingOnSetting(context);
  hilog.info(0x0000, TAG, 'enableExternalBinaryLoadingOnSetting result: %{public}d', result);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'enableExternalBinaryLoadingOnSetting failed: %{public}d %{public}s', e.code, e.message);
}
```

## ExternalBinaryLoadingStatus

外部二进制文件加载状态枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.SecurityPrivacyServer

**起始版本：** 26.0.1

| 状态值 | 说明 |
| --- | --- |
| DENY | 禁止加载外部二进制文件。 |
| ALLOW | 允许加载外部二进制文件。 |
