---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/screentimeguard-app-picker
title: "@hms.utilityApplication.screenTimeGuard.appPicker（应用选择）"
breadcrumb: API参考 > 应用服务 > Screen Time Guard Kit（屏幕时间守护服务） > ArkTS API > @hms.utilityApplication.screenTimeGuard.appPicker（应用选择）
category: harmonyos-references
scraped_at: 2026-09-02T14:53:31+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:3a1ce33b2080452944fbd70b950c0b9cea9c4dcd4403bb0f4876d8d43b43dc6d
---

## 模块概述

已安装应用列表属于用户隐私，若管控应用获取到相关数据，则可能通过其来构造用户画像，造成隐私泄漏问题。针对上述问题，Screen Time Guard Kit为管控应用提供匿名化的应用token来代替具体应用。

应用选择模块在保护用户隐私的前提下，为管控应用提供将token与具体应用信息相互转换的能力。该模块通过半模态页面展示具体的应用信息，而管控应用只能通过token与页面交互。

应用选择模块目前支持拉起两种页面：

* 应用选择页：用于将具体应用转换为token。页面展示系统中已安装的应用并提供选择功能，完成相应的操作后返回将已选择应用对应的token。
* 许可应用跳转页：用于将token转换为具体应用，并提供跳转功能。页面将输入的token转换为对应的应用图标和名称并进行展示，点击页面中相应的图标后可以启动并跳转到该应用。

**起始版本：** 6.0.0(20)

## 导入模块

```typescript
import { appPicker } from '@kit.ScreenTimeGuardKit';
```

## startAppPicker

startAppPicker(context: common.Context, appSelection: guardService.AppInfo): Promise<string[]>

拉起应用选择页，展示设备上已安装的应用列表，用户可在该半模态页面中勾选或取消勾选应用。在用户完成操作后，该接口返回已选择应用的token数组。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.MANAGE\_SCREEN\_TIME\_GUARD

**系统能力：** SystemCapability.ScreenTimeGuard.GuardService

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md) | 是 | 应用上下文（仅支持[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)）。 |
| appSelection | [guardService.AppInfo](screentimeguard-guardservice.md#appinfo) | 是 | 已被选择的应用。  调用此接口后，系统将根据该参数中指定的token列表，在拉起的应用选择页面中预勾选对应应用。  **说明**：  若Token数组包含无效token（同一管控应用在同一设备上通过[startAppPicker](screentimeguard-app-picker.md#startapppicker)接口获取的token为有效token，其它情况均为无效token），系统将自动过滤并仅对有效token生效。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string[]> | Promise对象，返回用户已勾选应用的token数组。当用户未选择任何应用时返回空数组。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-screentimeguard.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 801 | Capability not supported. function startAppPicker can not work correctly due to limited device capabilities. |
| 1019000001 | Internal error. |
| 1019000002 | The user has not authorized the application to access this interface. |
| 1019000003 | The user canceled the operation. |

**示例：**

```typescript
import { common } from '@kit.AbilityKit';
import { appPicker } from '@kit.ScreenTimeGuardKit';

@Entry
@Component
struct TestPage {
  build() {
    Column() {
      Button('TestStartAppPicker')
        .onClick(() => {
            // 获取UIAbilityContext上下文
            const context = this.getUIContext().getHostContext() as common.UIAbilityContext;
            // 调用startAppPicker接口，展示应用选择页并返回用户选择的应用token数组
            // 首次拉起AppPicker，没有已勾选的应用tokens传入，则appSelection为空数组
            appPicker.startAppPicker(context, { appTokens: [] })
               .then((tokens) => {
                  // 处理调用成功后的回调，打印用户已勾选应用的tokens数组
                  console.info('startAppPicker invoke success' + tokens);
               });
        })
    }
  }
}
```

## startAppForm

startAppForm(context: common.Context, appSelection: guardService.AppInfo, appSubTitle: string, displayTrustApp: boolean): Promise<void>

拉起许可应用跳转页，该半模态页面将传入的应用token数组转换为对应的应用图标和名称并进行展示，用户点击应用图标后，系统会跳转到该应用。此功能主要用于管控生效期间，帮助用户快速访问未被限制访问的应用。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.MANAGE\_SCREEN\_TIME\_GUARD

**系统能力：** SystemCapability.ScreenTimeGuard.GuardService

**起始版本：** 6.0.2(22)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md) | 是 | 应用上下文（仅支持[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)）。 |
| appSelection | [guardService.AppInfo](screentimeguard-guardservice.md#appinfo) | 是 | 在许可应用跳转页中展示的应用，最多可展示100个应用。  **说明**：  1. 若Token数组包含无效token（同一管控应用在同一设备上通过[startAppPicker](screentimeguard-app-picker.md#startapppicker)接口获取的token为有效token，其它情况均为无效token），系统将自动过滤并仅使用有效的Token进行展示。  2. 支持空数组，即用户不设置自定义的许可应用，只显示系统默认的许可应用，是正常场景。 |
| appSubTitle | string | 是 | 许可应用跳转页的子标题。该参数支持的最大长度为200个字符，超出范围时返回1019000009错误码。若传入参数为空字符串，则子标题显示为空。 |
| displayTrustApp | boolean | 是 | 是否在拉起的跳转页中展示默认的访问不受限应用，true表示展示，false表示不展示。目前支持的默认访问不受限应用仅包括"联系人"。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-screentimeguard.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. function startAppForm can not work correctly due to limited device capabilities. |
| 1019000001 | Internal error. |
| 1019000002 | The user has not authorized the application to access this interface. |
| 1019000003 | The user canceled the operation. |
| 1019000009 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```typescript
import { common } from '@kit.AbilityKit';
import { appPicker } from '@kit.ScreenTimeGuardKit';

@Entry
@Component
struct TestPage {
  build() {
    Column() {
      Button('TestStartAppForm')
        .onClick(() => {
             // 定义已选择的应用token数组
             // 可以通过调用startAppPicker接口获取相应的应用token并填充，本次初始化为空数组，表示没有用户选择的许可应用
            let selectedTokens: string[] = [];
            // 获取UIAbilityContext上下文
            const context = this.getUIContext().getHostContext() as common.UIAbilityContext;
            // 调用startAppForm接口，展示许可应用跳转页
            // 传入的selectedTokens为空数组，则许可应用跳转页只展示系统默认的许可应用
            appPicker.startAppForm(context, { appTokens: selectedTokens }, 'TestStartAppForm', false)
               .then(() => {
                  // 处理调用成功后的回调
                  console.info('startAppForm invoke success');
               });
        })
    }
  }
}
```
