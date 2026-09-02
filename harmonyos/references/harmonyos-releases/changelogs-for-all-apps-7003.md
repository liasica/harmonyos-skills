---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/changelogs-for-all-apps-7003
title: 针对所有应用的变更
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > OS平台行为变更说明 > 26.0.0 Release引入的行为变更 > 针对所有应用的变更
category: harmonyos-releases
scraped_at: 2026-09-02T14:58:27+08:00
doc_updated_at: 2026-08-31
content_hash: sha256:0f35e281def55b666e31c85c3e6edfba994b6c6fff14fa768cf265cdc48de40b
---

## Ability Kit

### 新增默认浏览器权限

**变更原因**

为避免非专业或低安全性应用引发的安全风险与体验割裂，系统引入默认浏览器权限管控机制。该机制围绕安全、隐私、用户体验三大维度设立严格准入标准，全面保障并提升网络浏览体验。

**变更影响**

此变更不涉及应用适配。

变更前：

仅声明支持打开HTTP协议，应用即可展示在默认浏览器备选列表并且可以被设置为默认浏览器。

变更后：

1. 应用需要申请默认浏览器权限（ohos.permission.DEFAULT\_WEB\_BROWSER）才可以被展示在默认浏览器备选列表。
2. 具备默认浏览器权限的应用才可以被设置为默认浏览器。

**说明** 

默认浏览器权限管控将于HarmonyOS下一个正式发布版本生效。请有需要的开发者尽快申请该权限，以免影响功能。

**起始 API Level**

不涉及

**变更的接口/组件**

不涉及

**适配指导**

若设置默认浏览器，需要按照[受限权限申请指导](../harmonyos-guides/declare-permissions-in-acl.md)申请默认浏览器权限（ohos.permission.DEFAULT\_WEB\_BROWSER）。权限授权后，在配置文件中[声明权限](../harmonyos-guides/declare-permissions.md)。

可申请默认浏览器权限的特殊场景和功能：

* 默认浏览器权限面向浏览器类应用，用于将应用设置为系统默认浏览器，接管系统及第三方应用发出的网页链接打开请求，统一管理网页内容的跳转与展示。
* 仅满足浏览器品类标准，并通过安全、隐私、用户体验三项审核的应用方可申请此权限。

## Agent Framework Kit

### OnDataCallback接口变更

**变更原因**

[OnDataCallback](../harmonyos-references/hmaf-a2a-protocol.md#ondatacallback)接口的method参数类型由枚举[AgentOperation](../harmonyos-references/hmaf-a2a-protocol.md#agentoperation)变更为string，简化了接口定义，提升了扩展性。开发者可直接使用字符串进行方法判断，无需依赖枚举类型。未知method字段值改为直接透传给Agent处理。

RequestContext参数类型中，[RequestContext.getClientSessionId()](../harmonyos-references/hmaf-a2a-protocol.md#getclientsessionid)方法仅在ClearContext请求中会返回非空值。ClearContext请求不再单独处理，改为按未知method流程处理。此方法将与ClearContext的处理流程一同删除。

**变更影响**

此变更涉及应用适配。

**说明** 

此变更涉及的接口为26.0.0 Beta版本新增接口，因此变更仅在应用的targetSdkVersion设置为大于等于26.0.0时生效。

* 变更前：[OnDataCallback](../harmonyos-references/hmaf-a2a-protocol.md#ondatacallback)的method参数类型为[AgentOperation](../harmonyos-references/hmaf-a2a-protocol.md#agentoperation)枚举；[RequestContext.getClientSessionId()](../harmonyos-references/hmaf-a2a-protocol.md#getclientsessionid)方法可用。
* 变更后：[OnDataCallback](../harmonyos-references/hmaf-a2a-protocol.md#ondatacallback)的method参数类型为string；[RequestContext.getClientSessionId()](../harmonyos-references/hmaf-a2a-protocol.md#getclientsessionid)方法已删除。

**起始 API Level**

26.0.0

**变更的接口/组件**

@kit.AgentFrameworkKit：

* [OnDataCallback](../harmonyos-references/hmaf-a2a-protocol.md#ondatacallback)，method参数类型改为string。
* [AgentOperation](../harmonyos-references/hmaf-a2a-protocol.md#agentoperation)枚举类已删除。
* [RequestContext.getClientSessionId()](../harmonyos-references/hmaf-a2a-protocol.md#getclientsessionid)方法已删除。

**适配指导**

开发者需要修改[OnDataCallback](../harmonyos-references/hmaf-a2a-protocol.md#ondatacallback)接口的实现：

1. 从@kit.AgentFrameworkKit的import中删除[AgentOperation](../harmonyos-references/hmaf-a2a-protocol.md#agentoperation)。
2. 将method参数类型由[AgentOperation](../harmonyos-references/hmaf-a2a-protocol.md#agentoperation)改为string。
3. 将switch语句中的枚举值替换为字符串。

   | 变更前（枚举值） | 变更后（string） |
   | --- | --- |
   | [AgentOperation.EXECUTE](../harmonyos-references/hmaf-a2a-protocol.md#agentoperation) | 'Execute' |
   | [AgentOperation.CANCEL](../harmonyos-references/hmaf-a2a-protocol.md#agentoperation) | 'Cancel' |
   | [AgentOperation.CLEAR\_CONTEXT](../harmonyos-references/hmaf-a2a-protocol.md#agentoperation) | ClearContext请求不再单独提供处理流程，建议删除此分支或移动到默认分支处理 |
   | [AgentOperation.PERCEPTION\_SUGGEST](../harmonyos-references/hmaf-a2a-protocol.md#agentoperation) | 'PerceptionSuggest' |
4. 删除[RequestContext.getClientSessionId()](../harmonyos-references/hmaf-a2a-protocol.md#getclientsessionid)的调用。

适配示例，变更前：

```ts
import { RequestContext, AgentOperation } from '@kit.AgentFrameworkKit';
const TAG = 'A2A-Server';
let agentOnData = (method: AgentOperation, context: RequestContext) => {
  const taskId: string = context.getTaskId() ?? '';
  switch (method) {
    case AgentOperation.EXECUTE:
      // 执行A2A服务端的请求处理流程
      hilog.info(0x0000, TAG, 'Execute called');
      break;
    case AgentOperation.CANCEL:
      hilog.info(0x0000, TAG, 'Cancel called');
      break;
    case AgentOperation.CLEAR_CONTEXT:
      const clientSessionId: string = context.getClientSessionId() ?? "";
      hilog.info(0x0000, TAG, `Clear context called, session id: ${clientSessionId}`);
      break;
    case AgentOperation.PERCEPTION_SUGGEST:
      hilog.info(0x0000, TAG, 'Perception suggest called');
      break;
    default:
      break;
  }
};
```

变更后：

```ts
import { RequestContext } from '@kit.AgentFrameworkKit';
const TAG = 'A2A-Server';
let agentOnData = (method: string, context: RequestContext) => {
  const taskId: string = context.getTaskId() ?? '';
  switch (method) {
    case 'Execute':
      // 执行A2A服务端的请求处理流程
      hilog.info(0x0000, TAG, 'Execute called');
      break;
    case 'Cancel':
      hilog.info(0x0000, TAG, 'Cancel called');
      break;
    case 'PerceptionSuggest':
      hilog.info(0x0000, TAG, 'Perception suggest called');
      break;
    default:
      break;
  }
};
```

## ArkUI

### Image组件autoResize属性默认行为变更

**变更原因**

图片解码后的宽×高像素乘积超过5000万时，按原图尺寸解码会占用大量内存，内存压力大甚至存在稳定性问题。为控制内存占用，该场景下[autoResize](../harmonyos-references/ts-basic-components-image.md#autoresize)属性默认值变更为true，即图片解码过程中开启降采样解码。该判断仅与图片像素尺寸相关，与图片文件大小及图片格式无关。

**变更影响**

此变更涉及应用适配。

* 变更前：未设置[autoResize](../harmonyos-references/ts-basic-components-image.md#autoresize)时，Image组件的autoResize属性默认为false，即图片解码过程中不自动缩放，按原图尺寸解码。
* 变更后：未设置autoResize时，如果图片解码后的宽×高像素乘积超过5000万，Image组件的autoResize默认设置为true，此时图片解码过程中会自动缩放，根据显示区域尺寸降采样解码。

**起始 API Level**

7

**变更的接口/组件**

Image的autoResize属性。

**适配指导**

默认行为变更。如果应用加载宽×高像素乘积大于5000万的图片且需要保留原图显示质量（例如需要对大图进行放大查看细节），可设置autoResize为false，按原图尺寸解码。

```ts
Image($r('app.media.large_image'))
  .autoResize(false)
```

## Core File Kit

### 沙箱路径/storage/Users/currentUser/appdata下无权限目录的stat和access行为变更

**变更原因**

为强化沙箱路径下的安全机制，应用对/storage/Users/currentUser/appdata下的目录进行stat和access时，需严格遵循权限管控设计，确保仅可访问有权限的目录及文件。

**变更影响**

此变更不涉及应用适配。

**说明** 

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于26.0.0时生效。

* 变更前：应用对沙箱路径/storage/Users/currentUser/appdata下没有权限的目录执行stat和access时，可以成功。
* 变更后：应用对沙箱路径/storage/Users/currentUser/appdata下没有权限的目录执行stat和access时，无法成功。

**起始 API Level**

9

**变更的接口/组件**

musl/sys/stat.h中stat、fstat、fstat64、fstatat等接口。

musl/unistd.h中access、faccessat等接口。

**适配指导**

排查及适配步骤如下：

1. 检查是否有硬编码访问：/storage/Users/currentUser/appdata/el2/{本应用包名}/files/路径。

   适配建议：删除硬编码逻辑，访问本应用路径可以转化为沙箱路径/data/storage/el2/base/files/。
2. 检查是否有硬编码访问：/storage/Users/currentUser/appdata/el2/{其他应用包名}/files/路径。

   适配建议：

   * 如果其他应用未对本应用授权，先获取授权再进行访问。
   * 如果其他应用已对本应用授权，无需整改。

## Localization Kit

### 国际化-I18n模块部分新增接口错误码的类型从string变更为number

**变更原因**

系统错误码类型默认为number类型，Localization Kit接口的实现一直使用string类型。从API版本26.0.0开始，Localization Kit新增接口的错误码类型变更为number类型。

**变更影响**

此变更涉及应用适配。

**说明** 

此变更涉及的接口为26.0.0 Beta版本新增接口，因此变更仅在应用的targetSdkVersion设置为大于等于26.0.0时生效。

从API版本26.0.0开始，新增接口的错误码类型为number类型，此前版本接口的错误码类型仍为string类型。

**起始API Level**

26.0.0

**变更的接口/组件**

* i18n.ChineseCalendar.setChineseCalendarTime
* i18n.ChineseCalendar.checkLeapMonth
* i18n.TimeZone.setAppDefaultTimeZoneById
* i18n.Unicode.detectEncoding
* i18n.I18NUtil.setUnicodeWrappedBidiDirection
* i18n.I18NUtil.convertCanonicalLocaleIdentifier
* i18n.SymbolDateTimeFormat.constructor
* i18n.SymbolDateTimeFormat.format
* i18n.SymbolDateTimeFormat.formatToParts
* i18n.SymbolDateTimeFormat.formatRange
* i18n.SymbolDateTimeFormat.formatRangeToParts
* i18n.SymbolDateTimeFormat.parse
* i18n.SymbolNumberFormat.constructor
* i18n.SymbolNumberFormat.format
* i18n.SymbolNumberFormat.formatToParts
* i18n.SymbolNumberFormat.formatRange
* i18n.SymbolNumberFormat.formatRangeToParts
* i18n.SymbolNumberFormat.parse

**适配指导**

接口默认行为变更。请开发者确认此变更是否影响业务逻辑（如错误码类型判断），如有影响需进行适配。

## MDM Kit

### 企业设备管理服务部分接口错误码的类型从string变更为number

**变更原因**

系统错误码类型应为number类型，而企业设备管理服务接口的实现一直使用string类型。为规范数据类型，从API版本26.0.0开始，企业设备管理服务新增接口的错误码类型变更为number类型。

**变更影响**

此变更涉及应用适配。

**说明** 

此变更涉及的接口为26.0.0 Beta版本新增接口，因此变更仅在应用的targetSdkVersion设置为大于等于26.0.0时生效。

* 变更前：企业设备管理服务接口错误码类型为string类型。
* 变更后：企业设备管理服务接口错误码类型为number类型。

```ts
import { applicationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
 
let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
 
let bundleNames: Array<string> = ['com.example.notificationapp'];
 
try {
  applicationManager.addAllowedNotificationBundles(wantTemp, bundleNames, 100);
  console.info('Succeeded in adding allowed notification bundles.');
} catch (err) {
  console.error(`Code type is ${typeof(err.code)}`);
  // 变更前打印：Code type is string
  // 变更后打印：Code type is number
}
```

**起始API Level**

26.0.0

**变更的接口/组件**

* adminManager.enableSelfDeviceAdmin
* applicationManager.addAllowedNotificationBundles
* applicationManager.removeAllowedNotificationBundles
* applicationManager.getAllowedNotificationBundles
* applicationManager.queryBundleStatsInfos
* applicationManager.queryTrafficStats
* bundleManager.installForResult
* bundleManager.getInstalledBundleStorageStats
* deviceControl.operateDevice
* deviceSettings.setSwitchStatus
* securityManager.setScreenLockDisabledForAccount
* securityManager.isScreenLockDisabledForAccount
* securityManager.setScreenWatermarkImage
* securityManager.cancelScreenWatermarkImage
* telephonyManager.activeSim
* telephonyManager.deactiveSim
* telephonyManager.setDefaultData
* telephonyManager.getDefaultData

**适配指导**

接口默认行为变更。使用上述接口的开发者，如果业务代码使用了错误码类型判断，则需要适配。

以 applicationManager.addAllowedNotificationBundles为例，适配方法如下：

```ts
import { applicationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
 
let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
 
let bundleNames: Array<string> = ['com.example.notificationapp'];
 
try {
  applicationManager.addAllowedNotificationBundles(wantTemp, bundleNames, 100);
  console.info('Succeeded in adding allowed notification bundles.');
} catch (err) {
  // 必须使用 number 类型进行判断
  if (err.code === 9200001) {
    // 相关业务操作
  }
}
```
