---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-voip-ability
title: VoIPExtensionAbility（应用内通话消息扩展Ability）（废弃）
breadcrumb: API参考 > 应用服务 > Push Kit（推送服务） > ArkTS API > VoIPExtensionAbility（应用内通话消息扩展Ability）（废弃）
category: harmonyos-references
scraped_at: 2026-09-02T14:53:30+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b0764b6f99f942202619431f6b4188a883aae71db87922c5948b62600722c034
---

VoIPExtensionAbility为应用内通话消息扩展Ability，继承自[UIExtensionAbility](js-apis-app-ability-uiextensionability.md)，增加获取场景化消息数据的回调。有如下约束：

* VoIPExtensionAbility为独立子进程，轻量级。
* 不允许调用卡片API。

执行ExtensionAbility失败可能会返回错误，请按具体报错信息排查，详见[ArkTS API错误码](push-error-code.md)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Push.PushService

**起始版本：** 4.1.0(11)

**废弃版本：** 26.0.0

## 约束限制

为保障系统安全性和稳定性，防止VoIPExtensionAbility滥用系统资源，系统对其能力进行管控， 不支持部分模块的引用，详情请参考[附录](push-voip-ability.md#附录)。

## 导入模块

```typescript
import { VoIPExtensionAbility } from '@kit.PushKit';
```

## 属性

**模型约束：** 属性仅可在Stage模型下使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 对于6.1.0(23)以前版本，该属性在Phone、Tablet中可正常使用，在其他设备类型中无效果。对于6.1.0(23)及之后版本，该属性在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。

**起始版本：** 4.1.0(11)

**废弃版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | [VoIPExtensionContext](push-voip-context.md)(deprecated) | 否 | 否 | VoIPExtensionAbility的上下文环境，继承自[UIExtensionContext](js-apis-inner-application-uiextensioncontext.md)。 |

## onReceiveMessage(deprecated)

onReceiveMessage(voipInfo: pushCommon.VoIPInfo): void

应用继承VoIPExtensionAbility后接收应用内通话消息的接口。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 对于6.1.0(23)以前版本，该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、PC/2in1中可正常调用，在其他设备类型中无效果。

**起始版本：** 4.1.0(11)

**废弃版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| voipInfo | pushCommon.[VoIPInfo](push-pushcommon.md#voipinfo) | 是 | 网络音视频通话消息数据。 |

**示例：**

```typescript
import { VoIPExtensionAbility, pushCommon } from '@kit.PushKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const LOG_DOMAIN = 0x0000;
const LOG_TAG = 'VoIPExtensionAbility';

export default class VoipExtAbility extends VoIPExtensionAbility {
  // voipInfo为场景化消息数据
  onReceiveMessage(voipInfo: pushCommon.VoIPInfo): void {
    hilog.info(LOG_DOMAIN, LOG_TAG, 'VoipExtAbility onReceiveMessage');
  }
}
```

## 附录

VoIPExtensionAbility不支持以下模块的引用。

| Kit | 模块 |
| --- | --- |
| Form Kit | [@ohos.app.form.formProvider (formProvider)](js-apis-app-form-formprovider.md)  [@ohos.app.form.formInfo (formInfo)](js-apis-app-form-forminfo.md)  [@ohos.app.form.formBindingData (卡片数据绑定类)](js-apis-app-form-formbindingdata.md)  [@ohos.app.form.FormExtensionAbility (FormExtensionAbility)](js-apis-app-form-formextensionability.md)  [@ohos.application.formBindingData (卡片数据绑定类)](js-apis-application-formbindingdata.md)  [@ohos.application.formInfo (formInfo)](js-apis-application-forminfo.md)  [@ohos.application.formProvider (formProvider)](js-apis-application-formprovider.md) |
