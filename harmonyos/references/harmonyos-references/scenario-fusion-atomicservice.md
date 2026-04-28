---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/scenario-fusion-atomicservice
title: atomicService（融合场景化API）
breadcrumb: API参考 > 应用服务 > Scenario Fusion Kit（融合场景服务） > ArkTS API > atomicService（融合场景化API）
category: harmonyos-references
scraped_at: 2026-04-28T08:18:37+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:dcdf2139149e501c6a1b875c8a26f3791d7b6e45589d88d8b4f070bd425f58cb
---

本模块为开发者提供获取系统信息、系统设置、关注组件等能力。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.atomicservice

**起始版本：** 5.0.0(12)

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { atomicService } from '@kit.ScenarioFusionKit';
```

## SystemSettingInfo

PhonePC/2in1TabletTVWearable

该类提供获取系统设置属性的对象。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.atomicservice

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| bluetoothEnabled | boolean | 否 | 是 | 蓝牙系统开关。“true”表示开关已打开，“false”表示开关已关闭。 |
| locationEnabled | boolean | 否 | 是 | 地理位置的系统开关。“true”表示开关已打开，“false”表示开关已关闭。 |
| wifiEnabled | boolean | 否 | 是 | Wi-Fi 的系统开关。“true”表示开关已打开，“false”表示开关已关闭。 |
| deviceOrientation | string | 否 | 是 | 设备当前显示的方向。“portrait”表示竖屏，“landscape”表示横屏。 |

## SystemInfo

PhonePC/2in1TabletTVWearable

该类提供获取系统信息属性的对象。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.atomicservice

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| brand | string | 否 | 是 | 设备品牌名称。 |
| deviceModel | string | 否 | 是 | 设备类型。  **说明：**  返回值中如果出现特殊字符，需要进行转义。 |
| screenWidth | number | 否 | 是 | 屏幕的宽度，单位px。 |
| screenHeight | number | 否 | 是 | 屏幕的高度，单位px。 |
| statusBarHeight | number | 否 | 是 | 状态栏的高度，单位px。 |
| screenSafeArea | [window.AvoidArea](arkts-apis-window-i.md#avoidarea7) | 否 | 是 | 竖屏正方向下的安全区域。 |
| language | string | 否 | 是 | 系统语言。 |
| osFullName | string | 否 | 是 | 系统版本。 |
| fontSizeSetting | number | 否 | 是 | 显示设备逻辑像素的密度，代表物理像素与逻辑像素的缩放系数，计算方式为：  该参数为浮点数，受[densityDPI](js-apis-display.md#display)范围限制，取值范围在[0.5，4.0]。一般取值1.0、3.0等，实际取值取决于不同设备提供的[densityDPI](js-apis-display.md#display)。 |
| sdkApiVersion | number | 否 | 是 | 系统软件API版本。 |
| bluetoothEnabled | boolean | 否 | 是 | 蓝牙系统开关。“true”表示开关已打开，“false”表示开关已关闭。 |
| locationEnabled | boolean | 否 | 是 | 地理位置的系统开关。“true”表示开关已打开，“false”表示开关已关闭。 |
| wifiEnabled | boolean | 否 | 是 | Wi-Fi 的系统开关。“true”表示开关已打开，“false”表示开关已关闭。 |
| deviceOrientation | string | 否 | 是 | 设备当前显示的方向。“portrait”表示竖屏，“landscape”表示横屏。 |
| theme | [ColorMode](ts-state-management-environment-variables.md#colormode) | 否 | 是 | 深浅色模式，可选值为：  - ColorMode.LIGHT：浅色模式；  - ColorMode.DARK：深色模式。 |
| windowWidth | number | 否 | 是 | 可使用窗口宽度，单位px，该参数应为整数。 |
| windowHeight | number | 否 | 是 | 可使用窗口高度，单位px，该参数应为整数。 |

## FollowResult

PhonePC/2in1TabletTVWearable

该枚举定义了关注结果的类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.1(21)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.atomicservice

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中返回801错误码。

**起始版本：** 6.0.1(21)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SUCCESS | 0 | 关注成功。 |
| FAILED | 1 | 关注失败。 |

## FollowComponentParams

PhonePC/2in1TabletTVWearable

获取关注组件的参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.1(21)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.atomicservice

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中返回801错误码。

**起始版本：** 6.0.1(21)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| pubId | string | 否 | 否 | 服务号ID。从华为开发者联盟服务号管理页面获取，长度限制1~64位字符。 |
| channelId | string | 否 | 是 | 渠道ID。长度限制0~32位字符，只能是数字或字母。用于识别组件关注的来源渠道。 |
| offset | [Position](ts-types.md#position) | [Edges](ts-types.md#edges12) | [LocalizedEdges](ts-types.md#localizededges12) | 否 | 是 | 组件放置位置，基于屏幕中心点的位置偏移。  默认值：{ x: 0, y: 300 } |

## FollowComponentCallback

PhonePC/2in1TabletTVWearable

关注组件的回调接口。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.1(21)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.atomicservice

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中返回801错误码。

**起始版本：** 6.0.1(21)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| onFollowComplete | AsyncCallback<[FollowCompleteResult](scenario-fusion-atomicservice.md#followcompleteresult)> | 否 | 否 | 回调函数。当关注操作成功，err为undefined，data为获取到的FollowCompleteResult；否则为错误对象。 |

## FollowCompleteResult

PhonePC/2in1TabletTVWearable

该接口定义了关注组件关注结果的返回体。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.1(21)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.atomicservice

**起始版本：** 6.0.1(21)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| code | [FollowResult](scenario-fusion-atomicservice.md#followresult) | 否 | 否 | 关注组件返回结果。关注成功：FollowResult.SUCCESS，关注失败：FollowResult.FAILED。 |

## SystemInfoType

PhonePC/2in1TabletTVWearable

type SystemInfoType = 'brand' | 'deviceModel' | 'screenWidth' | 'screenHeight' | 'statusBarHeight'

| 'screenSafeArea' | 'language' | 'osFullName' | 'fontSizeSetting' | 'sdkApiVersion' | 'bluetoothEnabled'

| 'locationEnabled' | 'wifiEnabled' | 'deviceOrientation' | 'theme' | 'windowWidth' | 'windowHeight'

系统信息属性取值类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.atomicservice

**设备行为差异：** 对于5.1.0(18)之前的版本，该接口在Phone、Tablet、2in1中可正常调用，在其他设备类型中返回801错误码。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、2in1、Wearable、TV中可正常调用，在其他设备类型中返回801错误码。

**起始版本：** 5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| 'brand' | 设备品牌名称。 |
| 'deviceModel' | 设备类型。 |
| 'screenWidth' | 屏幕的宽度。 |
| 'screenHeight' | 屏幕的高度。 |
| 'statusBarHeight' | 状态栏的高度。 |
| 'screenSafeArea' | 竖屏正方向下的安全区域。 |
| 'language' | 系统语言。 |
| 'osFullName' | 系统版本。 |
| 'fontSizeSetting' | 显示设备逻辑像素的密度，代表物理像素与逻辑像素的缩放系数，计算方式为：  该参数为浮点数，受[densityDPI](js-apis-display.md#display)范围限制，取值范围在[0.5，4.0]。一般取值1.0、3.0等，实际取值取决于不同设备提供的[densityDPI](js-apis-display.md#display)。 |
| 'sdkApiVersion' | 系统软件API版本。 |
| 'bluetoothEnabled' | 蓝牙系统开关。 |
| 'locationEnabled' | 地理位置的系统开关。 |
| 'wifiEnabled' | Wi-Fi 的系统开关。 |
| 'deviceOrientation' | 设备当前显示的方向。 |
| 'theme' | 系统主题（深色、浅色模式）。 |
| 'windowWidth' | 可使用窗口宽度。 |
| 'windowHeight' | 可使用窗口高度。 |

## SystemSettingType

PhonePC/2in1TabletTVWearable

type SystemSettingType = 'bluetoothEnabled' | 'locationEnabled' | 'wifiEnabled' | 'deviceOrientation'

系统设置属性取值类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.atomicservice

**设备行为差异：** 对于5.1.0(18)之前的版本，该接口在Phone、Tablet、2in1中可正常调用，在其他设备类型中返回801错误码。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、2in1、Wearable、TV中可正常调用，在其他设备类型中返回801错误码。

**起始版本：** 5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| 'bluetoothEnabled' | 蓝牙系统开关。 |
| 'locationEnabled' | 地理位置的系统开关。 |
| 'wifiEnabled' | Wi-Fi 的系统开关。 |
| 'deviceOrientation' | 设备当前显示的方向。 |

## getSystemInfoSync

PhonePC/2in1TabletTVWearable

getSystemInfoSync(properties?: Array<SystemInfoType>): SystemInfo

调用该方法获取设备、网络状态、屏幕、语言、主题等系统信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.atomicservice

**设备行为差异：** 对于5.1.0(18)之前的版本，该接口在Phone、Tablet、2in1中可正常调用，在其他设备类型中返回801错误码。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、2in1、Wearable、TV中可正常调用，在其他设备类型中返回801错误码。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| properties | Array<[SystemInfoType](scenario-fusion-atomicservice.md#systeminfotype)> | 否 | 获取设备、网络状态、屏幕、语言、主题等系统信息的请求对象。  **说明：**  - 使用5.0.1(13)及以上版本时不需要配置Wi-Fi权限、蓝牙权限。  - 获取Wi-Fi信息需要配置权限ohos.permission.GET\_WIFI\_INFO。  - 获取蓝牙开启状态需要配置权限ohos.permission.ACCESS\_BLUETOOTH。  - 获取用户程序访问控制权限可参考[程序访问控制管理](js-apis-abilityaccessctrl.md#requestpermissionsfromuser9)。 |

说明

在多线程中调用getSystemInfoSync接口时，请勿获取theme、windowWidth、windowHeight、statusBarHeight和screenSafeArea的信息，可能会引发空指针问题导致程序异常终止。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SystemInfo](scenario-fusion-atomicservice.md#systeminfo) | 返回[SystemInfo](scenario-fusion-atomicservice.md#systeminfo)对象。  **说明：**  getSystemInfoSync接口不支持获取windowWidth、windowHeight、statusBarHeight和screenSafeArea属性，如需获取可使用[getSystemInfo](scenario-fusion-atomicservice.md#getsysteminfo)接口。 |

**示例：**

```
1. import { atomicService } from '@kit.ScenarioFusionKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. let stateArray: Array<atomicService.SystemInfoType> =
5. ['brand', 'deviceModel', 'screenWidth', 'screenHeight', 'language', 'osFullName', 'fontSizeSetting',
6. 'sdkApiVersion', 'bluetoothEnabled', 'wifiEnabled', 'locationEnabled', 'deviceOrientation', 'theme'];
7. try {
8. let data = atomicService.getSystemInfoSync(stateArray);
9. hilog.info(0x0000, 'testTag', 'succeeded in getting system info');
10. let brand: string | undefined = data.brand;
11. let deviceModel: string | undefined = data.deviceModel;
12. let screenWidth: number | undefined = data.screenWidth;
13. let screenHeight: number | undefined = data.screenHeight;
14. let language: string | undefined = data.language;
15. let osFullName: string | undefined = data.osFullName;
16. let fontSizeSetting: number | undefined = data.fontSizeSetting;
17. let sdkApiVersion: number | undefined = data.sdkApiVersion;
18. let bluetoothEnabled: boolean | undefined = data.bluetoothEnabled;
19. let wifiEnabled: boolean | undefined = data.wifiEnabled;
20. let locationEnabled: boolean | undefined = data.locationEnabled;
21. let deviceOrientation: string | undefined = data.deviceOrientation;
22. let theme: ColorMode | undefined = data.theme;
23. } catch (error) {
24. hilog.error(0x0000, 'testTag', 'failReason: %{public}d %{public}s', error.code, error.message);
25. }
```

## getSystemInfo

PhonePC/2in1TabletTVWearable

getSystemInfo(properties?: Array<SystemInfoType>): Promise<SystemInfo>

调用该方法获取设备、网络状态、屏幕、语言、主题等系统信息，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.atomicservice

**设备行为差异：** 对于5.1.0(18)之前的版本，该接口在Phone、Tablet、2in1中可正常调用，在其他设备类型中返回801错误码。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、2in1、Wearable、TV中可正常调用，在其他设备类型中返回801错误码。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| properties | Array<[SystemInfoType](scenario-fusion-atomicservice.md#systeminfotype)> | 否 | 获取设备、网络状态、屏幕、语言、主题等系统信息的请求对象。  **说明：**  - 使用5.0.1(13)及以上版本时不需要配置Wi-Fi权限、蓝牙权限。  - 获取Wi-Fi信息需要配置权限ohos.permission.GET\_WIFI\_INFO。  - 获取蓝牙开启状态需要配置权限ohos.permission.ACCESS\_BLUETOOTH。  - 获取用户程序访问控制权限可参考[程序访问控制管理](js-apis-abilityaccessctrl.md#requestpermissionsfromuser9)。 |

说明

在多线程中调用getSystemInfo接口时，请勿获取theme、windowWidth、windowHeight、statusBarHeight和screenSafeArea的信息，可能会引发空指针问题导致程序异常终止。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[SystemInfo](scenario-fusion-atomicservice.md#systeminfo)> | Promise对象，返回[SystemInfo](scenario-fusion-atomicservice.md#systeminfo)对象。 |

**示例：**

```
1. import { atomicService } from '@kit.ScenarioFusionKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { window } from '@kit.ArkUI';

6. let stateArray: Array<atomicService.SystemInfoType> =
7. ['brand', 'deviceModel', 'screenWidth', 'screenHeight', 'statusBarHeight', 'screenSafeArea', 'language', 'osFullName',
8. 'fontSizeSetting', 'sdkApiVersion', 'bluetoothEnabled', 'wifiEnabled', 'locationEnabled', 'deviceOrientation',
9. 'theme', 'windowWidth', 'windowHeight'];
10. try {
11. atomicService.getSystemInfo(stateArray).then((data: atomicService.SystemInfo) => {
12. hilog.info(0x0000, 'testTag', 'succeeded in getting system info asynchronously');
13. let brand: string | undefined = data.brand;
14. let deviceModel: string | undefined = data.deviceModel;
15. let screenWidth: number | undefined = data.screenWidth;
16. let screenHeight: number | undefined = data.screenHeight;
17. let statusBarHeight: number | undefined = data.statusBarHeight;
18. let screenSafeArea: window.AvoidArea | undefined = data.screenSafeArea;
19. let language: string | undefined = data.language;
20. let osFullName: string | undefined = data.osFullName;
21. let fontSizeSetting: number | undefined = data.fontSizeSetting;
22. let sdkApiVersion: number | undefined = data.sdkApiVersion;
23. let bluetoothEnabled: boolean | undefined = data.bluetoothEnabled;
24. let wifiEnabled: boolean | undefined = data.wifiEnabled;
25. let locationEnabled: boolean | undefined = data.locationEnabled;
26. let deviceOrientation: string | undefined = data.deviceOrientation;
27. let theme: ColorMode | undefined = data.theme;
28. let windowWidth: number | undefined = data.windowWidth;
29. let windowHeight: number | undefined = data.windowHeight;
30. }).catch((error: BusinessError) => {
31. hilog.error(0x0000, 'testTag', 'Promise error: %{public}d %{public}s', error.code, error.message);
32. })
33. } catch (error) {
34. hilog.error(0x0000, 'testTag', 'failReason: %{public}d %{public}s', error.code, error.message);
35. }
```

## getSystemSetting

PhonePC/2in1TabletTVWearable

getSystemSetting(properties?: Array<SystemSettingType>): SystemSettingInfo

调用该方法获取系统设置属性，包括蓝牙、位置、Wi-Fi状态和设备方向信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.atomicservice

**设备行为差异：** 对于5.1.0(18)之前的版本，该接口在Phone、Tablet、2in1中可正常调用，在其他设备类型中返回801错误码。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、2in1、Wearable、TV中可正常调用，在其他设备类型中返回801错误码。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| properties | Array<[SystemSettingType](scenario-fusion-atomicservice.md#systemsettingtype)> | 否 | 获取蓝牙、定位、Wi-Fi开关，以及设备方向等系统信息的请求对象。  **说明：**  - 使用5.0.1(13)及以上版本时不需要配置Wi-Fi权限、蓝牙权限。  - 获取Wi-Fi信息需要配置权限ohos.permission.GET\_WIFI\_INFO。  - 获取蓝牙开启状态需要配置权限ohos.permission.ACCESS\_BLUETOOTH。  - 获取用户程序访问控制权限可参考[程序访问控制管理](js-apis-abilityaccessctrl.md#requestpermissionsfromuser9)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SystemSettingInfo](scenario-fusion-atomicservice.md#systemsettinginfo) | 返回[SystemSettingInfo](scenario-fusion-atomicservice.md#systemsettinginfo)对象。 |

**示例：**

```
1. import { atomicService } from '@kit.ScenarioFusionKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. let stateArray: Array<atomicService.SystemSettingType> =
5. ['bluetoothEnabled', 'locationEnabled', 'deviceOrientation', 'wifiEnabled'];
6. try {
7. let data = atomicService.getSystemSetting(stateArray);
8. hilog.info(0x0000, 'testTag', 'succeeded in getting system setting info');
9. let bluetoothEnabled: boolean | undefined = data.bluetoothEnabled;
10. let locationEnabled: boolean | undefined = data.locationEnabled;
11. let deviceOrientation: string | undefined = data.deviceOrientation;
12. let wifiEnabled: boolean | undefined = data.wifiEnabled;
13. } catch (error) {
14. hilog.error(0x0001, 'testTag', 'failReason: %{public}d %{public}s', error.code, error.message);
15. }
```

## showFollowComponent

PhonePC/2in1TabletTVWearable

showFollowComponent(ctx: UIContext, params: FollowComponentParams, callback: FollowComponentCallback): Promise<void>

调用该方法展示关注组件。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.1(21)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.atomicservice

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中返回801错误码。

**起始版本：** 6.0.1(21)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ctx | [UIContext](ts-custom-component-api.md#uicontext) | 是 | UIContext实例对象。 |
| params | [FollowComponentParams](scenario-fusion-atomicservice.md#followcomponentparams) | 是 | 关注组件的参数。 |
| callback | [FollowComponentCallback](scenario-fusion-atomicservice.md#followcomponentcallback) | 是 | 回调函数。callback返回关注的结果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [801](errorcode-universal.md#section801-该设备不支持此api) | Capability not supported. |
| [1009601001](scenario-fusion-arkts-api-error-code.md#section1009601001-非法的服务号id) | Invalid service account id. |
| [1009601002](scenario-fusion-arkts-api-error-code.md#section1009601002-用户未登录华为账号) | The user has not logged in with HUAWEI ID. |
| [1009601003](scenario-fusion-arkts-api-error-code.md#section1009601003-请求服务号云失败) | Request server failed. |
| [1009601004](scenario-fusion-arkts-api-error-code.md#section1009601004-网络连接失败) | Network connection error. |
| [1009601005](scenario-fusion-arkts-api-error-code.md#section1009601005-其他异常) | Other error. |

**示例：**

```
1. import { atomicService } from '@kit.ScenarioFusionKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct Index {
8. aboutToAppear(): void {
9. // 一键关注组件。
10. // pubId: 服务号id，此处以官方小助手服务号id为例。
11. const pubId: string = '0cca1c645526449fb89d4a83e3bc25df';
12. // channelId：渠道id，长度限制32，只能是数字或字母组成；offset：设置关注组件的位置坐标。
13. const params: atomicService.FollowComponentParams =
14. { pubId: pubId, channelId: '', offset: { x: 0, y: 300 } };
15. // 点击关注按钮的关注结果回调。
16. const callbacks: atomicService.FollowComponentCallback = {
17. onFollowComplete: (err, result) => {
18. if (err) {
19. // 错误日志处理。
20. hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
21. return;
22. }
23. hilog.info(0x0000, "testTag", "follow result: %{public}d", result.code);
24. if (result.code === atomicService.FollowResult.SUCCESS) {
25. hilog.info(0x0000, "testTag", "follow succeeded handle");
26. } else {
27. hilog.info(0x0000, "testTag", "follow failed handle");
28. }
29. }
30. }
31. // 展示关注组件。
32. atomicService.showFollowComponent(this.getUIContext(), params, callbacks).catch((error: BusinessError<void>) => {
33. hilog.error(0x0000, 'testTag', 'showFollowComponent failReason: %{public}d %{public}s:', error.code,
34. error.message);
35. })
36. }

38. build() {
39. }
40. }
```
