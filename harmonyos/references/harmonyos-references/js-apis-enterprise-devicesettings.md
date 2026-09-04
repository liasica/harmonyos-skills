---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-devicesettings
title: "@ohos.enterprise.deviceSettings（设备设置管理）"
breadcrumb: API参考 > 系统 > 基础功能 > MDM Kit（企业设备管理服务） > ArkTS API > @ohos.enterprise.deviceSettings（设备设置管理）
category: harmonyos-references
scraped_at: 2026-09-05T06:19:29+08:00
doc_updated_at: 2026-09-04
content_hash: sha256:858102bdb114e061512a6ea8a0e57c787e6262498eef16721ff08a7f7a21f5e2
---

本模块提供企业设备设置能力，支持设置和获取设备息屏时间、系统时间、电源策略、护眼模式、默认输入法、壁纸、隐藏设置项等。

**说明** 

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

本模块接口仅对设备管理应用开放，且调用接口前需激活设备管理应用，具体请参考[MDM Kit开发指南](../harmonyos-guides/mdm-kit-guide.md)。

## 导入模块

```ts
import { deviceSettings } from '@kit.MDMKit';
```

## deviceSettings.setValue

setValue(admin: Want, item: string, value: string): void

设置设备策略。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SETTINGS

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [配置](../harmonyos-guides/mdm-kit-multi-mdm.md#规则3配置)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| item | string | 是 | 设备设置策略类型。  - screenOff：设备息屏策略。对于PC/2in1设备，支持设置电池和电源供电下的设备息屏策略。  - dateTime：设置系统时间。  - powerPolicy：设备电源策略。该能力仅支持PC/2in1设备，策略设置之后不刷新设置—电源和电池页面，在手机平板设备设置后不生效。  对于PC/2in1设备，仅支持设置电池供电下的设备电源策略。设置设备超时灭屏时睡眠延迟策略，睡眠动作需要在设置—电源和电池页面显示的睡眠时间之后等待设置的delayTime才会生效。  - eyeComfort：从API version 23开始支持，设置护眼模式开关状态，仅支持全天开启和关闭护眼模式。  - defaultInputMethod：从API version 23开始支持，设置默认输入法。 |
| value | string | 是 | 策略类型值。  当item为screenOff时，value为设备息屏时间（单位：毫秒）。建议value值和设置页面手动操作下拉框中的可选项保持一致。仅在PC/2in1设备上支持传-1设置永不息屏，其他设备无效。  当item为dateTime时，value为要设置的系统时间（单位：毫秒）。  当item为powerPolicy时，value为JSON字符串，格式：{"powerScene":xx,"powerPolicy":{"powerPolicyAction":xx,"delayTime":xx}}。  powerScene为电源策略场景，可设置参数如下：  - 0：超时灭屏场景。  powerPolicyAction为休眠动作策略场景，可设置参数如下：  - 0：不执行动作。  - 1：自动进入睡眠。  - 2：强制进入睡眠。  - 3：进入休眠，该策略暂不生效。  - 4：关机。  delayTime为延迟时间（单位：毫秒），不支持设置为30000毫秒，其余数值均在允许范围内。  当item为eyeComfort时，value为护眼模式开关状态的字符串。  - on：全天开启护眼模式。  - off：关闭护眼模式。  当item为defaultInputMethod时，value为输入法应用包名字符串。  - 可以通过[getCurrentInputMethod](js-apis-inputmethod.md#inputmethodgetcurrentinputmethod9)获取当前输入法应用包名。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
import { deviceSettings } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
import { inputMethod } from '@kit.IMEKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

// 设置设备息屏时间为3秒
try {
  // 需根据实际情况进行替换
  deviceSettings.setValue(wantTemp, 'screenOff', '3000');
  console.info(`Succeeded in setting screen off time.`);
} catch (err) {
  console.error(`Failed to set screen off time. Code: ${err.code}, message: ${err.message}`);
}

// 设置系统时间，value为要设置的系统时间（单位：毫秒）
try {
  // 需根据实际情况进行替换
  deviceSettings.setValue(wantTemp, 'dateTime', '1698768000000');
  console.info(`Succeeded in setting date time.`);
} catch (err) {
  console.error(`Failed to set date time. Code: ${err.code}, message: ${err.message}`);
}

// 设置设备电源策略，超时灭屏后自动进入睡眠，延迟时间为60000毫秒（该能力仅支持PC/2in1设备）
try {
  // 需根据实际情况进行替换
  let powerPolicyString: string = JSON.stringify({
    powerPolicyAction: 1,
    delayTime: 60000
  });
  let value: string = JSON.stringify({
    powerScene: 0,
    powerPolicy: powerPolicyString
  });
  deviceSettings.setValue(wantTemp, 'powerPolicy', value);
  console.info(`Succeeded in setting power policy.`);
} catch (err) {
  console.error(`Failed to set power policy. Code: ${err.code}, message: ${err.message}`);
}

// 设置护眼模式为全天开启，value可设置为on或off
try {
  // 需根据实际情况进行替换
  deviceSettings.setValue(wantTemp, 'eyeComfort', 'on');
  console.info(`Succeeded in setting eye comfort.`);
} catch (err) {
  console.error(`Failed to set eye comfort. Code: ${err.code}, message: ${err.message}`);
}

// 设置默认输入法，value为输入法应用包名
try {
  // 需根据实际情况进行替换
  let currentInputMethod: inputMethod.InputMethodProperty = inputMethod.getCurrentInputMethod();
  deviceSettings.setValue(wantTemp, 'defaultInputMethod', currentInputMethod.name);
  console.info(`Succeeded in setting default input method.`);
} catch (err) {
  console.error(`Failed to set default input method. Code: ${err.code}, message: ${err.message}`);
}
```

## deviceSettings.getValue

getValue(admin: Want, item: string): string

获取设备设置策略。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SETTINGS

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| item | string | 是 | 设备设置策略类型。  - screenOff：设备息屏策略，对于PC/2in1设备，支持查询电池供电下的设备息屏策略。  - powerPolicy：设备电源策略，仅对PC/2in1设备生效，仅支持查询电池供电下的设备电源策略。  - eyeComfort：从API version 23开始支持，护眼模式开关状态。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 策略类型值。  当item为screenOff时，返回设备息屏时间（单位：毫秒），对于PC/2in1设备，返回设备电池供电下的息屏时间（单位：毫秒）。  当item为powerPolicy时，返回电源策略，对于PC/2in1设备，返回设备电池供电下的电源策略，格式为JSON字符串：{"powerScene":xx,"powerPolicy":{"powerPolicyAction":xx,"delayTime":xx}}。powerScene为电源策略场景；delayTime为延迟时间（单位：毫秒）；powerPolicyAction为休眠策略。  电源策略场景：  - 0：超时场景。  休眠策略：  - 0：不执行动作。  - 1：自动进入睡眠。  - 2：强制进入睡眠。  - 3：进入休眠，该策略暂不生效。  - 4：关机。  当item为eyeComfort时，返回的value为护眼模式开关状态的字符串。  - on：全天开启护眼模式。  - off：关闭护眼模式。  - unknown：其他模式。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
import { deviceSettings } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

// 获取设备息屏时间，返回设备息屏时间（单位：毫秒）
try {
  // 参数需根据实际情况进行替换
  let result: string = deviceSettings.getValue(wantTemp, 'screenOff');
  console.info(`Succeeded in getting screen off time, result : ${result}`);
} catch (err) {
  console.error(`Failed to get screen off time. Code: ${err.code}, message: ${err.message}`);
}

// 获取设备电源策略（仅支持PC/2in1设备），返回JSON字符串{"powerScene":xx,"powerPolicy":{"powerPolicyAction":xx,"delayTime":xx}}
try {
  // 参数需根据实际情况进行替换
  let result: string = deviceSettings.getValue(wantTemp, 'powerPolicy');
  console.info(`Succeeded in getting power policy, result : ${result}`);
} catch (err) {
  console.error(`Failed to get power policy. Code: ${err.code}, message: ${err.message}`);
}

// 获取护眼模式开关状态，返回值为on、off或unknown
try {
  // 参数需根据实际情况进行替换
  let result: string = deviceSettings.getValue(wantTemp, 'eyeComfort');
  console.info(`Succeeded in getting eye comfort, result : ${result}`);
} catch (err) {
  console.error(`Failed to get eye comfort. Code: ${err.code}, message: ${err.message}`);
}
```

## deviceSettings.setHomeWallpaper20+

setHomeWallpaper(admin: Want, fd: number): Promise<void>

设置桌面壁纸，使用Promise异步回调。

**需要权限：** ohos.permission.ENTERPRISE\_SET\_WALLPAPER

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [配置](../harmonyos-guides/mdm-kit-multi-mdm.md#规则3配置)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| fd | number | 是 | 需要设置为桌面壁纸图片的文件描述符，可以通过file.fs的[openSync](js-apis-file-fs.md#fileioopensync)接口获取应用沙箱目录下的图片文件描述符。壁纸图片大小不能超过100MB。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。当设置桌面壁纸失败后会抛出错误对象。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```ts
import { deviceSettings } from '@kit.MDMKit';
import { common, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';

let wantTemp: Want = {
  // 请根据实际情况修改
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
const context = this.getUIContext().getHostContext() as common.UIAbilityContext;
// 参数根据实际情况进行替换
let filename: string = "homewallpaper.jpg";
let filePath: string = context.filesDir + '/' + filename;
let fd: number = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE).fd;
deviceSettings.setHomeWallpaper(wantTemp, fd).then(() => {
  console.info('Succeeded in setting home wallpaper');
}).catch((err: BusinessError) => {
  console.error(`Failed to set home wallpaper. Code: ${err.code}, message: ${err.message}`);
}).finally(() => {
  fileIo.closeSync(fd);
});
```

## deviceSettings.setUnlockWallpaper20+

setUnlockWallpaper(admin: Want, fd: number): Promise<void>

设置锁屏壁纸，使用Promise异步回调。企业设备管理应用可通过此接口统一设置企业设备的锁屏壁纸，用于企业形象展示或安全管控等场景。

**需要权限：** ohos.permission.ENTERPRISE\_SET\_WALLPAPER

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [配置](../harmonyos-guides/mdm-kit-multi-mdm.md#规则3配置)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| fd | number | 是 | 需要设置为锁屏壁纸图片的文件描述符，可以通过file.fs的[openSync](js-apis-file-fs.md#fileioopensync)接口获取应用沙箱目录下的图片文件描述符。壁纸图片大小不能超过100MB。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。当设置锁屏壁纸失败后会抛出错误对象。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```ts
import { deviceSettings } from '@kit.MDMKit';
import { common, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
const context = this.getUIContext().getHostContext() as common.UIAbilityContext;
// 参数根据实际情况进行替换
let filename: string = "lockwallpaper.jpg";
let filePath: string = context.filesDir + '/' + filename;
let fd: number = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE).fd;
deviceSettings.setUnlockWallpaper(wantTemp, fd).then(() => {
  console.info('Succeeded in setting lock wallpaper');
}).catch((err: BusinessError) => {
  console.error(`Failed to set lock wallpaper. Code: ${err.code}, message: ${err.message}`);
}).finally(() => {
  fileIo.closeSync(fd);
});
```

## deviceSettings.setValueForAccount24+

setValueForAccount(admin: Want, item: SettingsItem, accountId: number, value: string): void

设置指定用户的设备设置策略。该接口可以设置指定用户在设置应用中的某个参数，比如设置用户100的设备名称等。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SETTINGS

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| item | [SettingsItem](js-apis-enterprise-devicesettings.md#settingsitem24) | 是 | 设备设置策略类型。 |
| accountId | number | 是 | 用户ID，取值范围：大于等于0。  accountId可以通过[getOsAccountLocalId](js-apis-osaccount.md#getosaccountlocalid9-1)等接口来获取。 |
| value | string | 是 | 策略类型值。  当item为[SettingsItem.DEVICE\_NAME](js-apis-enterprise-devicesettings.md#settingsitem24)时，value为设备名称的字符串。 字符串长度范围：大于等于1，小于等于100。只允许设置当前用户的设备名称，设置其他用户的设备名称返回9200012错误码。  当item为[SettingsItem.FLOATING\_NAVIGATION](js-apis-enterprise-devicesettings.md#settingsitem24)时，在Phone和Tablet设备中可正常调用，在其他设备中返回801错误码。只允许设置当前用户的三键导航，设置其他用户的三键导航不会生效，value为三键导航的开关状态。  - '0'：表示开启三键导航（通过接口[enterKioskMode](js-apis-app-ability-kioskmanager.md#kioskmanagerenterkioskmode)进入Kiosk模式下，三键导航显示依赖底部手势开启；即三键导航开关和底部手势开关同时开启时，三键导航才会显示。底部手势可通过接口[applicationManager.setKioskFeatures](js-apis-enterprise-applicationmanager.md#applicationmanagersetkioskfeatures20)设置开启或关闭）。  - '1'：表示关闭三键导航。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```ts
import { deviceSettings } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // 需根据实际情况进行替换
  let accountId = 100;
  let deviceName: string = "deviceName";
  deviceSettings.setValueForAccount(wantTemp, deviceSettings.SettingsItem.DEVICE_NAME, accountId, deviceName);
  console.info('Succeeded in setting device name.');
} catch (err) {
  console.error(`Failed to set device name. Code: ${err.code}, message: ${err.message}`);
}
```

## deviceSettings.getValueForAccount24+

getValueForAccount(admin: Want, item: SettingsItem, accountId: number): string

获取指定用户的设备设置策略。该接口可以获取指定用户在设置应用中的某个参数，比如获取用户100的设备名称等。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SETTINGS

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| item | [SettingsItem](js-apis-enterprise-devicesettings.md#settingsitem24) | 是 | 设备设置策略类型。支持的策略类型包括：DEVICE\_NAME（设备名称）、FLOATING\_NAVIGATION（三键导航）。 |
| accountId | number | 是 | 用户ID，取值范围：大于等于0。  accountId可以通过[getOsAccountLocalId](js-apis-osaccount.md#getosaccountlocalid9-1)等接口来获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 策略类型值。  当item为[SettingsItem.DEVICE\_NAME](js-apis-enterprise-devicesettings.md#settingsitem24)时，返回当前用户的设备名称，查询非当前用户的设备名称返回9200012错误码。  当item为[SettingsItem.FLOATING\_NAVIGATION](js-apis-enterprise-devicesettings.md#settingsitem24)时，返回指定用户的三键导航的开关状态。  当item为[SettingsItem.FLOATING\_NAVIGATION](js-apis-enterprise-devicesettings.md#settingsitem24)时，该接口在Phone和Tablet设备中可正常调用，在其他设备中返回801错误码。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```ts
import { deviceSettings } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // 需根据实际情况进行替换
  let accountId = 100;
  let result: string = deviceSettings.getValueForAccount(wantTemp, deviceSettings.SettingsItem.DEVICE_NAME, accountId);
  console.info(`Succeeded in getting device name, result : ${result}`);
} catch (err) {
  console.error(`Failed to get device name. Code: ${err.code}, message: ${err.message}`);
}
```

## deviceSettings.addHiddenSettingsMenu24+

addHiddenSettingsMenu(admin: Want, menusToHidden: Array<SettingsMenu>): void

添加设置项至当前用户下的隐藏设置项列表。添加至隐藏设置项列表的设置项在当前用户的设置菜单中会被隐藏，隐藏后不可以在设置的搜索中搜索到。如果通过某种方式搜索到该设置项，点击后也无法打开。调用接口后即刻生效，无需重启设置应用。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SETTINGS

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 该接口在Phone和Tablet设备中可正常调用，在其他设备中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| menusToHidden | Array<[SettingsMenu](js-apis-enterprise-devicesettings.md#settingsmenu24)> | 是 | 隐藏的设置项列表。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 9200016 | Service timeout. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```ts
import { deviceSettings } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

let menusToHidden: Array<deviceSettings.SettingsMenu> = [
  // 需根据实际情况进行替换或增加
  deviceSettings.SettingsMenu.ACCOUNT_ID,
  deviceSettings.SettingsMenu.WIFI
];

try {
  deviceSettings.addHiddenSettingsMenu(wantTemp, menusToHidden);
  console.info('Succeeded in adding hidden settings menu.');
} catch (err) {
  console.error(`Failed to add hidden settings menu. Code: ${err.code}, message: ${err.message}`);
}
```

## deviceSettings.removeHiddenSettingsMenu24+

removeHiddenSettingsMenu(admin: Want, menusToHidden: Array<SettingsMenu>): void

将设置项从当前用户下的隐藏设置项列表中移除。隐藏设置项列表中的设置项在当前用户的设置菜单中会被隐藏，隐藏后不可以在设置的搜索中搜索到，如果通过某种方式搜索到该设置项，点击后也无法打开。若移除后剩余的隐藏设置项列表为空，则设置项会全部显示。调用接口后即刻生效，无需重启设置应用。

从API版本26.0.0开始，调用[setDisallowedPolicyForAccount](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicyforaccount)接口禁用[SUPER\_HUB](js-apis-enterprise-restrictions.md#featureforaccount)后，再调用该接口将中转站从隐藏设置项列表中移除时，会发生策略冲突，抛出9200010错误码。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SETTINGS

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 该接口在Phone和Tablet设备中可正常调用，在其他设备中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| menusToHidden | Array<[SettingsMenu](js-apis-enterprise-devicesettings.md#settingsmenu24)> | 是 | 隐藏的设置项列表。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200010 | A conflict policy has been configured.  适用版本：26.0.0+ |
| 9200012 | Parameter verification failed. |
| 9200016 | Service timeout. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```ts
import { deviceSettings } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

let menusToHidden: Array<deviceSettings.SettingsMenu> = [
  // 需根据实际情况进行替换或增加
  deviceSettings.SettingsMenu.ACCOUNT_ID,
  deviceSettings.SettingsMenu.WIFI
];

try {
  deviceSettings.removeHiddenSettingsMenu(wantTemp, menusToHidden);
  console.info('Succeeded in removing hidden settings menu.');
} catch (err) {
  console.error(`Failed to remove hidden settings menu. Code: ${err.code}, message: ${err.message}`);
}
```

## deviceSettings.getHiddenSettingsMenu24+

getHiddenSettingsMenu(admin: Want): Array<SettingsMenu>

获取配置在当前用户下被隐藏的设置项列表。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SETTINGS

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 该接口在Phone和Tablet设备中可正常调用，在其他设备中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[SettingsMenu](js-apis-enterprise-devicesettings.md#settingsmenu24)> | 隐藏的设置项列表。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```ts
import { deviceSettings } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  const rawList: Array<number> = deviceSettings.getHiddenSettingsMenu(wantTemp) as Array<number>;
  for (const item of rawList) {
    const menu: deviceSettings.SettingsMenu = item as deviceSettings.SettingsMenu;
    console.info(`Valid SettingsMenu item: ${item} -> ${menu}`);
  }
  console.info('Succeeded in getting hidden settings menu.');
} catch (err) {
  console.error(`Failed to get hidden settings menu. Code: ${err.code}, message: ${err.message}`);
}
```

## deviceSettings.setSwitchStatus

setSwitchStatus(admin: Want, key: SwitchKey, status: SwitchStatus): void

设置开关的状态。支持设置星闪、蓝牙、Wi-Fi、NFC的状态为开启或关闭，设置完毕后，用户可以手动开关。支持设置蓝牙、NFC的状态为强制开启，设置完毕后，用户不可以手动开关。若已经通过[setDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicydeprecated) 接口禁用了某个开关，则通过本接口设置这个开关的状态会抛出错误码203，需通过[setDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicydeprecated) 接口解除该开关禁用策略。当设备有多个MDM应用时，各MDM应用设置开关状态不存在冲突，最后设置的策略生效。开启（用户可手动开启、关闭）、关闭（用户可手动开启、关闭）、强制开启（用户不可手动关闭）三个状态可以随意切换，也不存在冲突。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SETTINGS 或 ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [配置](../harmonyos-guides/mdm-kit-multi-mdm.md#规则3配置)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| key | [SwitchKey](js-apis-enterprise-devicesettings.md#switchkey) | 是 | 开关的名称，应用申请权限 ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS 并通过接口[startAdminProvision](js-apis-enterprise-adminmanager.md#adminmanagerstartadminprovision15)激活为自带设备管理应用，可以使用此接口设置以下开关：星闪、蓝牙、Wi-Fi。设置NFC开关时会报错误码9200002。 |
| status | [SwitchStatus](js-apis-enterprise-devicesettings.md#switchstatus) | 是 | 开关的状态，应用申请权限 ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS 并通过接口[startAdminProvision](js-apis-enterprise-adminmanager.md#adminmanagerstartadminprovision15)激活为自带设备管理应用，可以使用此接口设置以下状态：ON、OFF。设置为FORCE\_ON状态时会报错误码9200002。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 9201042 | Failed to toggle the switch state. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 203 | This function is prohibited by enterprise management policies. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```ts
import { deviceSettings } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // 需根据实际情况进行替换
  let key: deviceSettings.SwitchKey = deviceSettings.SwitchKey.BLUETOOTH;
  let status: deviceSettings.SwitchStatus  = deviceSettings.SwitchStatus.ON;
  deviceSettings.setSwitchStatus(wantTemp, key, status);
  console.info(`Succeeded in setting switch status.`);
} catch (err) {
  console.error(`Failed to set switch status. Code: ${err.code}, message: ${err.message}`);
}
```

## SettingsItem24+

设置的策略类型。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEVICE\_NAME | 0 | 设备名称。 |
| FLOATING\_NAVIGATION24+ | 1 | 三键导航。 |

## SettingsMenu24+

设置项列表。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ACCOUNT\_ID | 0 | 账号。 |
| WIFI | 1 | WLAN。 |
| WIFI\_PROXY\_SETTINGS | 2 | WLAN 代理。 |
| WIFI\_IP\_SETTINGS | 3 | WLAN IP 。 |
| BLUETOOTH | 4 | 星闪和蓝牙/蓝牙。 |
| NETWORK | 5 | 网络。 |
| MOBILE\_NETWORK | 6 | 移动网络。 |
| SUPER\_DEVICE | 7 | 多设备协同-超级终端。 |
| MORE\_CONNECTIVITY\_OPTIONS | 8 | 多设备协同。 |
| HOME\_SCREEN\_STYLE | 9 | 桌面和个性化。 |
| DISPLAY\_BRIGHTNESS | 10 | 显示和亮度。 |
| SOUND\_VIBRATION | 11 | 声音和振动。 |
| NOTIFICATIONS | 12 | 通知和状态栏。 |
| BIOMETRICS\_PASSWORD | 13 | 生物识别和密码。 |
| APPS\_AND\_SERVICES | 14 | 应用和元服务。 |
| BATTERY | 15 | 电池。 |
| STORAGE | 16 | 存储。 |
| PRIVACY\_AND\_SECURITY | 17 | 隐私和安全。 |
| DIGITAL\_BALANCE | 18 | 健康使用设备。 |
| SMART\_ASSISTANT | 19 | 智能助手。 |
| ACCESSIBILITY | 20 | 关怀和无障碍。 |
| SYSTEM | 21 | 系统。 |
| ABOUT\_DEVICE | 22 | 关于本机。 |
| SYSTEM\_NAVIGATION | 23 | 系统-系统导航。 |
| LANGUAGE\_REGION | 24 | 系统-语言和地区。 |
| INPUT\_METHODS | 25 | 系统-输入法。 |
| DATE\_TIME | 26 | 系统-日期和时间。 |
| DATA\_CLONE | 27 | 系统-数据克隆。 |
| BACKUP\_SETTINGS | 28 | 系统-备份和恢复。 |
| RESET | 29 | 系统-重置。 |
| SUPERHUB | 30 | 系统-中转站。 |
| USER\_EXPERIENCE | 31 | 系统-用户体验改进计划。 |
| SCREEN\_CAST | 32 | 多设备协同-无线投屏。 |
| PRINTERS\_SCANNERS | 33 | 打印机和扫描仪。 |
| MOBILE\_DATA | 34 | 移动网络-移动数据。 |
| PERSONAL\_HOTSPOT | 35 | 移动网络-个人热点。 |
| SIM\_MANAGEMENT | 36 | 移动网络-SIM卡管理。 |
| AIRPLANE\_MODE | 37 | 移动网络-飞行模式。 |
| MANAGE\_DATA\_USAGE | 38 | 移动网络-流量管理。 |
| VPN\_SETTINGS | 39 | 移动网络-VPN。 |
| TEXT\_DISPLAY\_SIZE | 40 | 显示和亮度-字体大小和界面缩放。 |
| APP\_DUPLICATOR | 41 | 系统-应用分身。 |
| SEARCH | 42 | 搜索。 |

## SwitchKey

开关名称的枚举。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 值 | 说明 | 需要权限 |
| --- | --- | --- | --- |
| NEARLINK | 0 | 星闪开关。 | ohos.permission.ENTERPRISE\_MANAGE\_SETTINGS 或 ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS |
| BLUETOOTH | 1 | 蓝牙开关。 | ohos.permission.ENTERPRISE\_MANAGE\_SETTINGS 或 ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS |
| WIFI | 2 | Wi-Fi开关。 | ohos.permission.ENTERPRISE\_MANAGE\_SETTINGS 或 ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS |
| NFC | 3 | NFC开关。 | ohos.permission.ENTERPRISE\_MANAGE\_SETTINGS |

## SwitchStatus

开关状态的枚举。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 值 | 说明 | 需要权限 |
| --- | --- | --- | --- |
| ON | 0 | 开启状态。 | ohos.permission.ENTERPRISE\_MANAGE\_SETTINGS 或 ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS |
| OFF | 1 | 关闭状态。 | ohos.permission.ENTERPRISE\_MANAGE\_SETTINGS 或 ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS |
| FORCE\_ON | 2 | 强制开启状态。 | ohos.permission.ENTERPRISE\_MANAGE\_SETTINGS |
