---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-ukeyauthextensionability
title: "@ohos.security.UkeyAuthExtensionAbility (UKey认证扩展能力)"
breadcrumb: API参考 > 系统 > 安全 > Device Certificate Kit（设备证书服务） > ArkTS API > @ohos.security.UkeyAuthExtensionAbility (UKey认证扩展能力)
category: harmonyos-references
scraped_at: 2026-11-12T09:55:26+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:5f47f8491e277c4e89922af3c6b956384033fc0cb5aa85d8c636fbb8309a5223
---

UkeyAuthExtensionAbility是用于UKey认证UI显示的ExtensionAbility组件，继承自[ExtensionAbility](js-apis-app-ability-extensionability.md)。驱动厂商可以通过继承UkeyAuthExtensionAbility并实现相关生命周期回调，提供自定义的UKey认证界面，该界面通过宿主应用启动的[UIExtensionContentSession](js-apis-app-ability-uiextensioncontentsession.md)进行显示。

与[UIExtensionAbility](js-apis-app-ability-uiextensionability.md)不同，UkeyAuthExtensionAbility不提供onForeground和onBackground生命周期回调。仅被授予ohos.permission.START\_SYSTEM\_DIALOG权限的应用可以启动UkeyAuthExtensionAbility。

**起始版本：** 26.0.1

## 导入模块

```ts
import { UkeyAuthExtensionAbility } from '@kit.DeviceCertificateKit';
```

## UkeyAuthExtensionAbility

表示UKey认证UI扩展组件，提供组件创建、会话创建、会话销毁、组件销毁等生命周期回调。

**起始版本：** 26.0.1

**系统能力：** SystemCapability.Security.CertificateManagerDialog

### 属性

**起始版本：** 26.0.1

**系统能力：** SystemCapability.Security.CertificateManagerDialog

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | [UkeyAuthExtensionContext](js-apis-ukeyauthextensioncontext.md) | 否 | 否 | UkeyAuthExtensionAbility的上下文。 |

### onCreate

onCreate(launchParam: AbilityConstant.LaunchParam): void

当UkeyAuthExtensionAbility组件实例完成创建时，系统会触发该回调。开发者可在该回调中执行初始化逻辑（如定义变量、加载资源等）。

**起始版本：** 26.0.1

**系统能力：** SystemCapability.Security.CertificateManagerDialog

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| launchParam | [AbilityConstant.LaunchParam](js-apis-app-ability-abilityconstant.md#launchparam) | 是 | 应用启动参数，包括应用启动原因和上次应用退出原因。 |

**示例：**

```ts
import { AbilityConstant } from '@kit.AbilityKit';
import { UkeyAuthExtensionAbility } from '@kit.DeviceCertificateKit';

export default class UkeyAuthExtension extends UkeyAuthExtensionAbility {
  onCreate(launchParam: AbilityConstant.LaunchParam): void {
    console.info('UkeyAuthExtension onCreate');
  }
}
```

### onSessionCreate

onSessionCreate(want: Want, session: UIExtensionContentSession): void

当[UIExtensionContentSession](js-apis-app-ability-uiextensioncontentsession.md)实例创建完成后，系统会触发该回调。开发者可在该回调中通过UIExtensionContentSession实例加载页面。

**起始版本：** 26.0.1

**系统能力：** SystemCapability.Security.CertificateManagerDialog

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | 启动UkeyAuthExtensionAbility时调用方传递的数据。 |
| session | [UIExtensionContentSession](js-apis-app-ability-uiextensioncontentsession.md) | 是 | UIExtensionContentSession实例。 |

**示例：**

```ts
import { UIExtensionContentSession, Want } from '@kit.AbilityKit';
import { UkeyAuthExtensionAbility } from '@kit.DeviceCertificateKit';

export default class UkeyAuthExtension extends UkeyAuthExtensionAbility {
  onSessionCreate(want: Want, session: UIExtensionContentSession): void {
    console.info('UkeyAuthExtension onSessionCreate');
    session.loadContent('pages/AuthPage');
  }
}
```

### onSessionDestroy

onSessionDestroy(session: UIExtensionContentSession): void

当[UIExtensionContentSession](js-apis-app-ability-uiextensioncontentsession.md)实例销毁后，系统触发该回调。该回调用于通知开发者UIExtensionContentSession实例已被销毁，不能再继续使用。

**起始版本：** 26.0.1

**系统能力：** SystemCapability.Security.CertificateManagerDialog

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| session | [UIExtensionContentSession](js-apis-app-ability-uiextensioncontentsession.md) | 是 | UIExtensionContentSession实例。 |

**示例：**

```ts
import { UIExtensionContentSession } from '@kit.AbilityKit';
import { UkeyAuthExtensionAbility } from '@kit.DeviceCertificateKit';

export default class UkeyAuthExtension extends UkeyAuthExtensionAbility {
  onSessionDestroy(session: UIExtensionContentSession): void {
    console.info('UkeyAuthExtension onSessionDestroy');
  }
}
```

### onDestroy

onDestroy(): void | Promise<void>

当UkeyAuthExtensionAbility组件被销毁时，系统触发该回调。开发者可以在该生命周期中执行资源清理、数据保存等相关操作。使用同步回调或Promise异步回调。

在执行完onDestroy生命周期回调后，应用可能会退出，从而可能导致onDestroy中的异步函数未能正确执行，比如异步写入数据库。推荐使用Promise异步回调，避免因应用退出导致onDestroy中的异步函数（比如异步写入数据库）未能正确执行。

**起始版本：** 26.0.1

**系统能力：** SystemCapability.Security.CertificateManagerDialog

**模型约束：** 此接口仅可在Stage模型下使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| void | Promise<void> | Promise对象，无返回结果。 |

**示例：**

```ts
import { UkeyAuthExtensionAbility } from '@kit.DeviceCertificateKit';

export default class UkeyAuthExtension extends UkeyAuthExtensionAbility {
  onDestroy(): void | Promise<void> {
    console.info('UkeyAuthExtension onDestroy');
    return new Promise<void>((resolve) => {
      resolve(undefined);
    });
  }
}
```
