---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-ukeyauthextensioncontext
title: "@ohos.security.UkeyAuthExtensionContext (UKey认证扩展能力上下文)"
breadcrumb: API参考 > 系统 > 安全 > Device Certificate Kit（设备证书服务） > ArkTS API > @ohos.security.UkeyAuthExtensionContext (UKey认证扩展能力上下文)
category: harmonyos-references
scraped_at: 2026-11-12T09:55:26+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:03aab13e95f6a847c01313b5712a7344d62607d2b60903ea029645634fc000e2
---

UkeyAuthExtensionContext是[UkeyAuthExtensionAbility](js-apis-ukeyauthextensionability.md)的上下文，继承自[ExtensionContext](js-apis-inner-application-extensioncontext.md)，仅提供终止能力。

**起始版本：** 26.0.1

## 导入模块

```ts
import { UkeyAuthExtensionContext } from '@kit.DeviceCertificateKit';
```

## UkeyAuthExtensionContext

表示UkeyAuthExtensionAbility的上下文，提供终止UkeyAuthExtensionAbility等能力。

**起始版本：** 26.0.1

**系统能力：** SystemCapability.Security.CertificateManagerDialog

### terminateSelf

terminateSelf(): Promise<void>

销毁调用当前接口的UkeyAuthExtensionAbility并关闭相应窗口。使用Promise异步回调。

**起始版本：** 26.0.1

**系统能力：** SystemCapability.Security.CertificateManagerDialog

**模型约束：** 此接口仅可在Stage模型下使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**示例：**

```ts
import { UkeyAuthExtensionAbility } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class UkeyAuthExtension extends UkeyAuthExtensionAbility {
  onSessionCreate() {
    this.context.terminateSelf().then(() => {
      console.info('Succeeded in terminating UkeyAuthExtension.');
    }).catch((error: Error) => {
      let err = error as BusinessError;
      console.error(`Failed to terminate UkeyAuthExtension. Code: ${err.code}, message: ${err.message}`);
    });
  }
}
```

### terminateSelfWithResult

terminateSelfWithResult(parameter: AbilityResult): Promise<void>

销毁调用当前接口的UkeyAuthExtensionAbility，关闭相应窗口，并将结果返回给UkeyAuthExtensionAbility的调用方（通常为系统服务）。使用Promise异步回调。

**起始版本：** 26.0.1

**系统能力：** SystemCapability.Security.CertificateManagerDialog

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| parameter | [AbilityResult](js-apis-inner-ability-abilityresult.md) | 是 | 返回给UkeyAuthExtensionAbility调用方的信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**示例：**

```ts
import { common } from '@kit.AbilityKit';
import { UkeyAuthExtensionAbility } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class UkeyAuthExtension extends UkeyAuthExtensionAbility {
  onSessionCreate() {
    // 返回给调用方的AbilityResult信息，此处仅为示例
    let abilityResult: common.AbilityResult = {
      resultCode: 0,
      want: undefined
    };
    this.context.terminateSelfWithResult(abilityResult).then(() => {
      console.info('Succeeded in terminating UkeyAuthExtension.');
    }).catch((error: Error) => {
      let err = error as BusinessError;
      console.error(`Failed to terminate UkeyAuthExtension. Code: ${err.code}, message: ${err.message}`);
    });
  }
}
```
