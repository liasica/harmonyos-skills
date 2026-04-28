---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/screentimeguard-app-picker
title: AppPicker（应用选择页）
breadcrumb: API参考 > 应用服务 > Screen Time Guard Kit（屏幕时间守护服务） > ArkTS API > AppPicker（应用选择页）
category: harmonyos-references
scraped_at: 2026-04-28T08:18:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:44aaa5d4ffcca70fb0b698e2f8706c939aae051fb4128c13bf0bff6af94eb32c
---

AppPicker模块支持拉起具有不同功能的应用页，目前包括应用选择页和许可应用跳转页。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ScreenTimeGuard.GuardService

**起始版本：** 6.0.0(20)

## 导入模块

PhoneTablet

```
1. import { appPicker } from '@kit.ScreenTimeGuardKit';
```

## startAppPicker

PhoneTablet

startAppPicker(context: common.Context, appSelection: guardService.AppInfo): Promise<string[]>

拉起应用选择页，展示设备上已安装的应用列表，用户可在该半模态页面中勾选或取消勾选应用。在用户完成操作后，该接口返回已选择应用的token数组。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.MANAGE\_SCREEN\_TIME\_GUARD

**系统能力：** SystemCapability.ScreenTimeGuard.GuardService

**设备行为差异：** 该接口在Phone、Tablet设备中可正常调用，在其他设备中返回801错误码。

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md) | 是 | 应用上下文（仅支持[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)）。 |
| appSelection | [guardService.AppInfo](screentimeguard-guardservice.md#appinfo) | 是 | 已被选择的应用，在picker页呈现勾选状态。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string[]> | Promise对象，返回用户已勾选应用的token数组。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](screentimeguard-error-code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 801 | Capability not supported. function startAppPicker can not work correctly due to limited device capabilities. |
| 1019000001 | Internal error. |
| 1019000002 | The user has not authorized the application to access this interface. |
| 1019000003 | The user canceled the operation. |

**示例：**

```
1. import { common } from '@kit.AbilityKit';
2. import { appPicker } from '@kit.ScreenTimeGuardKit';

4. @Entry
5. @Component
6. struct TestPage {
7. build() {
8. Column() {
9. Button("TestStartAppPicker")
10. .onClick(() => {
11. const context = this.getUIContext().getHostContext() as common.UIAbilityContext;
12. appPicker.startAppPicker(context, { appTokens: [] })
13. .then((tokens) => {
14. console.info('startAppPicker invoke success' + tokens);
15. })
16. })
17. }
18. }
19. }
```

## startAppForm

PhoneTablet

startAppForm(context: common.Context, appSelection: guardService.AppInfo, appSubTitle: string, displayTrustApp: boolean): Promise<void>

拉起许可应用跳转页，该半模态页面将传入的应用token数组转换为对应的应用图标和名称并进行展示，用户点击应用图标后，系统会跳转到该应用。此功能主要用于管控生效期间，帮助用户快速访问未被限制访问的应用。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.MANAGE\_SCREEN\_TIME\_GUARD

**系统能力：** SystemCapability.ScreenTimeGuard.GuardService

**设备行为差异：** 该接口在Phone、Tablet设备中可正常调用，在其他设备中返回801错误码。

**起始版本：** 6.0.2(22)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | 应用上下文（仅支持[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)）。 |
| appSelection | [guardService.AppInfo](screentimeguard-guardservice.md#appinfo) | 是 | 在许可应用跳转页中展示的应用。 |
| appSubTitle | string | 是 | 许可应用跳转页的子标题。该参数支持的最大长度为200个字符，超出范围时返回1019000009错误码。 |
| displayTrustApp | boolean | 是 | 是否在拉起的跳转页中展示默认的访问不受限应用，true表示展示，false表示不展示。目前支持的默认访问不受限应用仅包括"联系人"。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](screentimeguard-error-code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. function startAppForm can not work correctly due to limited device capabilities. |
| 1019000001 | Internal error. |
| 1019000002 | The user has not authorized the application to access this interface. |
| 1019000003 | The user canceled the operation. |
| 1019000009 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```
1. import { common } from '@kit.AbilityKit';
2. import { appPicker } from '@kit.ScreenTimeGuardKit';

4. @Entry
5. @Component
6. struct TestPage {
7. build() {
8. Column() {
9. Button("TestStartAppForm")
10. .onClick(() => {
11. let selectedTokens: string[] = []; // 可以通过调用startAppPicker接口获取相应的应用token
12. const context = this.getUIContext().getHostContext() as common.UIAbilityContext;
13. appPicker.startAppForm(context, { appTokens: selectedTokens }, "TestStartAppForm", false)
14. .then(() => {
15. console.info('startAppForm invoke success');
16. })
17. })
18. }
19. }
20. }
```
