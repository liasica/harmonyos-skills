---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resource-manager
title: @ohos.resourceManager (资源管理)
breadcrumb: API参考 > 应用框架 > Localization Kit（本地化开发服务） > ArkTS API > @ohos.resourceManager (资源管理)
category: harmonyos-references
scraped_at: 2026-04-28T08:06:30+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:40930face81ad604ddcc87fc15d20a3c5a3310f742e815b695c5ec4b059ecbac
---

本模块提供资源获取能力。根据当前的[Configuration](js-apis-resource-manager.md#configuration)配置，获取最匹配的应用资源或系统资源。具体匹配规则参考[资源匹配](../harmonyos-guides/resource-categories-and-access.md#资源匹配)。

Configuration配置包括语言、区域、横竖屏、Mcc（移动国家码）和Mnc（移动网络码）、Device capability（设备类型）、Density（分辨率）。

说明

本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { resourceManager } from '@kit.LocalizationKit';
```

## 使用说明

PhonePC/2in1TabletTVWearable

从API version 9开始，Stage模型支持通过Context获取资源管理resourceManager对象，无需再导入模块。

FA模型仍需要先导入模块，再调用[getResourceManager](js-apis-resource-manager.md#resourcemanagergetresourcemanager)接口获取资源管理对象。

Stage模型下Context的引用方法请参考[Stage模型的Context详细介绍](../harmonyos-guides/application-context-stage.md)。

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';

4. export default class EntryAbility extends UIAbility {
5. onWindowStageCreate(windowStage: window.WindowStage) {
6. let context = this.context;
7. let resourceManager = context.resourceManager;
8. }
9. }
```

## resourceManager.getResourceManager

PhonePC/2in1TabletTVWearable

getResourceManager(callback: AsyncCallback<ResourceManager>): void

获取当前应用的资源管理对象，使用callback异步回调。

**系统能力：** SystemCapability.Global.ResourceManager

**模型约束：** 此接口仅可在FA模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](js-apis-resource-manager.md#asynccallbackdeprecated)<[ResourceManager](js-apis-resource-manager.md#resourcemanager)> | 是 | 回调函数，返回资源管理ResourceManager对象。 |

**示例：**

```
1. import resourceManager from '@ohos.resourceManager';
2. // FA模型请使用上述方式导入模块

4. export default {
5. onCreate() {
6. resourceManager.getResourceManager((error, mgr) => {
7. if (error != null) {
8. console.error("error is " + error);
9. return;
10. }
11. // 'test'仅作示例，请替换为实际使用的资源名称
12. mgr.getStringByName('test', (error, value) => {
13. if (error) {
14. console.error("error is " + JSON.stringify(error));
15. } else {
16. console.info("success is " + value);
17. }

19. });
20. });
21. }
22. };
```

## resourceManager.getResourceManager

PhonePC/2in1TabletTVWearable

getResourceManager(bundleName: string, callback: AsyncCallback<ResourceManager>): void

获取指定应用的资源管理对象，使用callback异步回调。

**系统能力：** SystemCapability.Global.ResourceManager

**模型约束：** 此接口仅可在FA模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleName | string | 是 | 应用包名。 |
| callback | [AsyncCallback](js-apis-resource-manager.md#asynccallbackdeprecated)<[ResourceManager](js-apis-resource-manager.md#resourcemanager)> | 是 | 回调函数，返回应用包名对应的资源管理ResourceManager对象。 |

**示例：**

```
1. import resourceManager from '@ohos.resourceManager';
2. // FA模型请使用上述方式导入模块

4. // 'com.example.testapp'仅作示例，请替换为实际应用包名
5. const BUNDLE_NAME = 'com.example.testapp';

7. export default {
8. onCreate() {
9. resourceManager.getResourceManager(BUNDLE_NAME, (error, mgr) => {
10. if (error != null) {
11. console.error("getResourceManager error is " + error);
12. return;
13. }
14. // 'test'仅作示例，请替换为实际使用的资源名称
15. mgr.getStringByName('test', (error, value) => {
16. if (error) {
17. console.error("getResourceManager error is " + JSON.stringify(error));
18. } else {
19. console.info("getResourceManager success is " + value);
20. }
21. });
22. });
23. }
24. };
```

## resourceManager.getResourceManager

PhonePC/2in1TabletTVWearable

getResourceManager(): Promise<ResourceManager>

获取当前应用的资源管理对象，使用Promise异步回调。

**系统能力：** SystemCapability.Global.ResourceManager

**模型约束：** 此接口仅可在FA模型下使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ResourceManager](js-apis-resource-manager.md#resourcemanager)> | Promise对象，返回资源管理ResourceManager对象。 |

**示例：**

```
1. import resourceManager from '@ohos.resourceManager';
2. // FA模型请使用上述方式导入模块

4. export default {
5. onCreate() {
6. resourceManager.getResourceManager().then(resMgr => {
7. try {
8. // 'test'仅作示例，请替换为实际使用的资源名称
9. let testStr = resMgr.getStringByNameSync('test')
10. console.info("getResourceManager success is " + testStr);
11. } catch (error) {
12. console.error("getResourceManager error is " + JSON.stringify(error));
13. }
14. }).catch(error => {
15. console.error("getResourceManager error is " + error);
16. });
17. }
18. };
```

## resourceManager.getResourceManager

PhonePC/2in1TabletTVWearable

getResourceManager(bundleName: string): Promise<ResourceManager>

获取指定应用的资源管理对象，使用Promise异步回调。

**系统能力：** SystemCapability.Global.ResourceManager

**模型约束：** 此接口仅可在FA模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleName | string | 是 | 应用包名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ResourceManager](js-apis-resource-manager.md#resourcemanager)> | Promise对象，返回应用包名对应的资源管理ResourceManager对象。 |

**示例：**

```
1. import resourceManager from '@ohos.resourceManager';
2. // FA模型请使用上述方式导入模块

4. // 'com.example.testapp'仅作示例，请替换为实际应用包名
5. const BUNDLE_NAME = 'com.example.testapp';

7. export default {
8. onCreate() {
9. resourceManager.getResourceManager(BUNDLE_NAME).then(resMgr => {
10. try {
11. // 'test'仅作示例，请替换为实际使用的资源名称
12. let testStr = resMgr.getStringByNameSync('test')
13. console.info("getResourceManager success is " + testStr);
14. } catch (error) {
15. console.error("getResourceManager error is " + JSON.stringify(error));
16. }
17. }).catch(error => {
18. console.error("getResourceManager error is " + error);
19. });
20. }
21. };
```

## resourceManager.getSysResourceManager20+

PhonePC/2in1TabletTVWearable

getSysResourceManager(): ResourceManager

获取系统资源管理对象。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager](js-apis-resource-manager.md#resourcemanager) | 系统资源管理对象。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9001009 | Failed to access the system resource. which is not mapped to application sandbox, This error code will be thrown. |

**示例：**

```
1. import { resourceManager } from '@kit.LocalizationKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. let systemResourceManager = resourceManager.getSysResourceManager();
6. // 'sys.string.ohos_lab_vibrate'仅作示例，请替换为实际使用的资源
7. systemResourceManager.getStringValue($r('sys.string.ohos_lab_vibrate').id).then((value: string) => {
8. let str = value;
9. }).catch((error: BusinessError) => {
10. console.error(`systemResourceManager getStringValue promise error: ${error}`);
11. });
12. } catch (error) {
13. let code = (error as BusinessError).code;
14. let message = (error as BusinessError).message;
15. console.error(`getSysResourceManager failed, error code: ${code}, message: ${message}.`);
16. }
```

## Direction

PhonePC/2in1TabletTVWearable

用于表示设备屏幕方向。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DIRECTION\_VERTICAL | 0 | 竖屏。 |
| DIRECTION\_HORIZONTAL | 1 | 横屏。 |

## DeviceType

PhonePC/2in1TabletTVWearable

用于表示当前设备类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEVICE\_TYPE\_PHONE | 0x00 | 手机。 |
| DEVICE\_TYPE\_TABLET | 0x01 | 平板。 |
| DEVICE\_TYPE\_CAR | 0x02 | 汽车。 |
| DEVICE\_TYPE\_PC | 0x03 | 电脑。 |
| DEVICE\_TYPE\_TV | 0x04 | 电视。 |
| DEVICE\_TYPE\_WEARABLE | 0x06 | 穿戴。 |
| DEVICE\_TYPE\_2IN111+ | 0x07 | 2IN1。 |

## ScreenDensity

PhonePC/2in1TabletTVWearable

用于表示当前设备屏幕密度。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SCREEN\_SDPI | 120 | 低屏幕密度。 |
| SCREEN\_MDPI | 160 | 中屏幕密度。 |
| SCREEN\_LDPI | 240 | 高屏幕密度。 |
| SCREEN\_XLDPI | 320 | 特高屏幕密度。 |
| SCREEN\_XXLDPI | 480 | 超高屏幕密度。 |
| SCREEN\_XXXLDPI | 640 | 超特高屏幕密度。 |

## ColorMode12+

PhonePC/2in1TabletTVWearable

用于表示当前设备颜色模式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DARK | 0 | 深色模式。 |
| LIGHT | 1 | 浅色模式。 |

## Configuration

PhonePC/2in1TabletTVWearable

表示当前设备的状态。

**系统能力：** SystemCapability.Global.ResourceManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| direction | [Direction](js-apis-resource-manager.md#direction) | 否 | 否 | 屏幕方向。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| locale | string | 否 | 否 | 语言文字国家地区。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| deviceType12+ | [DeviceType](js-apis-resource-manager.md#devicetype) | 否 | 否 | 设备类型。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| screenDensity12+ | [ScreenDensity](js-apis-resource-manager.md#screendensity) | 否 | 否 | 屏幕密度。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| colorMode12+ | [ColorMode](js-apis-resource-manager.md#colormode12) | 否 | 否 | 颜色模式。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| mcc12+ | number | 否 | 否 | 移动国家码。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| mnc12+ | number | 否 | 否 | 移动网络码。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## DeviceCapability

PhonePC/2in1TabletTVWearable

表示设备支持的能力。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| screenDensity | [ScreenDensity](js-apis-resource-manager.md#screendensity) | 否 | 否 | 当前设备屏幕密度。 |
| deviceType | [DeviceType](js-apis-resource-manager.md#devicetype) | 否 | 否 | 当前设备类型。 |

## RawFileDescriptor9+

PhonePC/2in1TabletTVWearable

type RawFileDescriptor = \_RawFileDescriptor

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

| 类型 | 说明 |
| --- | --- |
| [\_RawFileDescriptor](js-apis-rawfiledescriptor.md#rawfiledescriptor-1) | 表示rawfile文件所在HAP的文件描述符（fd）。 |

## Resource9+

PhonePC/2in1TabletTVWearable

type Resource = \_Resource

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

| 类型 | 说明 |
| --- | --- |
| [\_Resource](js-apis-resource.md#resource-1) | 表示资源信息，包含资源ID值、应用包名、模块名称等信息，一般可使用$r方式获取。 |

## ResourceManager

PhonePC/2in1TabletTVWearable

提供访问应用资源和系统资源的能力。

说明

* ResourceManager涉及到的方法，仅限基于TS扩展的声明式开发范式使用。
* 资源文件在工程的resources目录中定义，通过resName、resId、Resource对象等可以获取对应的字符串、字符串数组、颜色等资源值，resName为资源名称，resId可通过$r(资源地址).id的方式获取，例如$r('app.string.test').id。
* 单HAP包获取自身资源、跨HAP/HSP包获取资源，由于入参为Resource的接口相比于入参为resName、resId的接口耗时更长，因此更推荐使用参数为resName或resId的接口。跨HAP/HSP包获取资源，**需要先使用[createModuleContext](js-apis-app-ability-application.md#applicationcreatemodulecontext)创建对应module的context**，再调用参数为resName或resId的接口。更多请参考[资源访问](../harmonyos-guides/resource-categories-and-access.md#资源访问)。
* 在API version 22及之前版本，中间码HAR、字节码HAR通过资源ID相关接口访问资源时，因ID无效会抛出异常；从API version 23开始，中间码HAR、字节码HAR通过资源ID相关接口可以正常访问资源，更多请参考[资源访问](../harmonyos-guides/resource-categories-and-access.md#资源访问)。
* 示例代码中test文件的具体内容请参考[附录](js-apis-resource-manager.md#附录)。

### getStringSync9+

PhonePC/2in1TabletTVWearable

getStringSync(resId: number): string

获取指定资源ID对应的字符串，使用同步方式返回。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resId | number | 是 | 资源ID值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 资源ID值对应的字符串。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |

**示例：**

```
1. // 资源文件路径: src/main/resources/base/element/string.json
2. {
3. "string": [
4. {
5. "name": "test",
6. "value": "I'm a test string resource."
7. }
8. ]
9. }
```

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. try {
7. // 'app.string.test'仅作示例，请替换为实际使用的资源
8. let testStr = this.context.resourceManager.getStringSync($r('app.string.test').id);
9. console.info(`getStringSync, result: ${testStr}`);
10. // 打印输出结果: getStringSync, result: I'm a test string resource.
11. } catch (error) {
12. let code = (error as BusinessError).code;
13. let message = (error as BusinessError).message;
14. console.error(`getStringSync failed, error code: ${code}, message: ${message}.`);
15. }
16. }
17. }
```

### getStringSync10+

PhonePC/2in1TabletTVWearable

getStringSync(resId: number, ...args: Array<string | number>): string

获取指定资源ID对应的字符串，并根据args参数对字符串进行格式化，使用同步方式返回。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resId | number | 是 | 资源ID值。 |
| ...args | Array<string | number> | 否 | 格式化字符串资源参数。  支持参数类型：%d、%f、%s、%%、%数字$d、%数字$f、%数字$s。  说明：%%转义为%; %数字$d中的数字表示使用args中的第几个参数。  举例：%%d格式化后为%d字符串; %1$d表示使用第一个参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 资源ID值对应的格式化字符串。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |
| 9001007 | Failed to format the resource obtained based on the resource ID. |

**示例：**

```
1. // 资源文件路径: src/main/resources/base/element/string.json
2. {
3. "string": [
4. {
5. "name": "test",
6. "value": "I'm a %1$s, format int: %2$d, format float: %3$f."
7. }
8. ]
9. }
```

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. try {
7. // 'app.string.test'仅作示例，请替换为实际使用的资源
8. let testStr = this.context.resourceManager.getStringSync($r('app.string.test').id, "format string", 10, 98.78);
9. console.info(`getStringSync, result: ${testStr}`);
10. // 打印输出结果: getStringSync, result: I'm a format string, format int: 10, format float: 98.78.
11. } catch (error) {
12. let code = (error as BusinessError).code;
13. let message = (error as BusinessError).message;
14. console.error(`getStringSync failed, error code: ${code}, message: ${message}.`);
15. }
16. }
17. }
```

### getStringByNameSync9+

PhonePC/2in1TabletTVWearable

getStringByNameSync(resName: string): string

获取指定资源名称对应的字符串，使用同步方式返回。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resName | string | 是 | 资源名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 资源名称对应的字符串。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001003 | Invalid resource name. |
| 9001004 | No matching resource is found based on the resource name. |
| 9001006 | The resource is referenced cyclically. |

**示例：**

```
1. // 资源文件路径: src/main/resources/base/element/string.json
2. {
3. "string": [
4. {
5. "name": "test",
6. "value": "I'm a test string resource."
7. }
8. ]
9. }
```

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. try {
7. // "test"仅作示例，请替换为实际使用的资源
8. let testStr = this.context.resourceManager.getStringByNameSync("test");
9. console.info(`getStringByNameSync, result: ${testStr}`);
10. // 打印输出结果: getStringByNameSync, result: I'm a test string resource.
11. } catch (error) {
12. let code = (error as BusinessError).code;
13. let message = (error as BusinessError).message;
14. console.error(`getStringByNameSync failed, error code: ${code}, message: ${message}.`);
15. }
16. }
17. }
```

### getStringByNameSync10+

PhonePC/2in1TabletTVWearable

getStringByNameSync(resName: string, ...args: Array<string | number>): string

获取指定资源名称对应的字符串，并根据args参数对字符串进行格式化，使用同步方式返回。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resName | string | 是 | 资源名称。 |
| ...args | Array<string | number> | 否 | 格式化字符串资源参数。  支持参数类型：%d、%f、%s、%%、%数字$d、%数字$f、%数字$s。  说明：%%转义为%; %数字$d中的数字表示使用args中的第几个参数。  举例：%%d格式化后为%d字符串; %1$d表示使用第一个参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 资源名称对应的格式化字符串。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001003 | Invalid resource name. |
| 9001004 | No matching resource is found based on the resource name. |
| 9001006 | The resource is referenced cyclically. |
| 9001008 | Failed to format the resource obtained based on the resource Name. |

**示例：**

```
1. // 资源文件路径: src/main/resources/base/element/string.json
2. {
3. "string": [
4. {
5. "name": "test",
6. "value": "I'm a %1$s, format int: %2$d, format float: %3$f."
7. }
8. ]
9. }
```

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. try {
7. // "test"仅作示例，请替换为实际使用的资源
8. let testStr = this.context.resourceManager.getStringByNameSync("test", "format string", 10, 98.78);
9. console.info(`getStringByNameSync, result: ${testStr}`);
10. // 打印输出结果: getStringByNameSync, result: I'm a format string, format int: 10, format float: 98.78.
11. } catch (error) {
12. let code = (error as BusinessError).code;
13. let message = (error as BusinessError).message;
14. console.error(`getStringByNameSync failed, error code: ${code}, message: ${message}.`);
15. }
16. }
17. }
```

### getStringValue9+

PhonePC/2in1TabletTVWearable

getStringValue(resId: number, callback: \_AsyncCallback<string>): void

获取指定资源ID对应的字符串，使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resId | number | 是 | 资源ID值。 |
| callback | [\_AsyncCallback](js-apis-base.md#asynccallback)<string> | 是 | 回调函数，返回获取的字符串。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |

**示例Stage：**

```
1. // 资源文件路径: src/main/resources/base/element/string.json
2. {
3. "string": [
4. {
5. "name": "test",
6. "value": "I'm a test string resource."
7. }
8. ]
9. }
```

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. // 'app.string.test'仅作示例，请替换为实际使用的资源
7. this.context.resourceManager.getStringValue($r('app.string.test').id, (error: BusinessError, value: string) => {
8. if (error != null) {
9. console.error(`callback getStringValue failed, error code: ${error.code}, message: ${error.message}.`);
10. } else {
11. console.info(`getStringValue, result: ${value}`);
12. // 打印输出结果: getStringValue, result: I'm a test string resource.
13. }
14. });
15. }
16. }
```

### getStringValue9+

PhonePC/2in1TabletTVWearable

getStringValue(resId: number): Promise<string>

获取指定资源ID对应的字符串，使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resId | number | 是 | 资源ID值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回资源ID值对应的字符串。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |

**示例：**

```
1. // 资源文件路径: src/main/resources/base/element/string.json
2. {
3. "string": [
4. {
5. "name": "test",
6. "value": "I'm a test string resource."
7. }
8. ]
9. }
```

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. // 'app.string.test'仅作示例，请替换为实际使用的资源
7. this.context.resourceManager.getStringValue($r('app.string.test').id).then((value: string) => {
8. console.info(`getStringValue, result: ${value}`);
9. // 打印输出结果: getStringValue, result: I'm a test string resource.
10. }).catch((error: BusinessError) => {
11. console.error(`promise getStringValue failed, error code: ${error.code}, message: ${error.message}.`);
12. });
13. }
14. }
```

### getStringByName9+

PhonePC/2in1TabletTVWearable

getStringByName(resName: string, callback: \_AsyncCallback<string>): void

获取指定资源名称对应的字符串，使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resName | string | 是 | 资源名称。 |
| callback | [\_AsyncCallback](js-apis-base.md#asynccallback)<string> | 是 | 返回获取的字符串。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001003 | Invalid resource name. |
| 9001004 | No matching resource is found based on the resource name. |
| 9001006 | The resource is referenced cyclically. |

**示例：**

```
1. // 资源文件路径: src/main/resources/base/element/string.json
2. {
3. "string": [
4. {
5. "name": "test",
6. "value": "I'm a test string resource."
7. }
8. ]
9. }
```

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. // "test"仅作示例，请替换为实际使用的资源
7. this.context.resourceManager.getStringByName("test", (error: BusinessError, value: string) => {
8. if (error != null) {
9. console.error(`callback getStringByName failed, error code: ${error.code}, message: ${error.message}.`);
10. } else {
11. console.info(`getStringByName, result: ${value}`);
12. // 打印输出结果: getStringByName, result: I'm a test string resource.
13. }
14. });
15. }
16. }
```

### getStringByName9+

PhonePC/2in1TabletTVWearable

getStringByName(resName: string): Promise<string>

获取指定资源名称对应的字符串，使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resName | string | 是 | 资源名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回资源名称对应的字符串。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001003 | Invalid resource name. |
| 9001004 | No matching resource is found based on the resource name. |
| 9001006 | The resource is referenced cyclically. |

**示例：**

```
1. // 资源文件路径: src/main/resources/base/element/string.json
2. {
3. "string": [
4. {
5. "name": "test",
6. "value": "I'm a test string resource."
7. }
8. ]
9. }
```

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. // "test"仅作示例，请替换为实际使用的资源
7. this.context.resourceManager.getStringByName("test").then((value: string) => {
8. console.info(`getStringByName, result: ${value}`);
9. // 打印输出结果: getStringByName, result: I'm a test string resource.
10. }).catch((error: BusinessError) => {
11. console.error(`promise getStringByName failed, error code: ${error.code}, message: ${error.message}.`);
12. });
13. }
14. }
```

### getStringArrayValueSync10+

PhonePC/2in1TabletTVWearable

getStringArrayValueSync(resId: number): Array<string>

获取指定资源ID对应的字符串数组，使用同步方式返回。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resId | number | 是 | 资源ID值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 资源ID值对应的字符串数组。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |

**示例：**

```
1. // 资源文件路径: src/main/resources/base/element/strarray.json
2. {
3. "strarray": [
4. {
5. "name": "test",
6. "value": [
7. {
8. "value": "I'm one of the array's values."
9. }
10. ]
11. }
12. ]
13. }
```

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. try {
7. // 'app.strarray.test'仅作示例，请替换为实际使用的资源
8. let strArray: Array<string> = this.context.resourceManager.getStringArrayValueSync($r('app.strarray.test').id);
9. console.info(`getStringArrayValueSync, result: ${strArray[0]}`);
10. // 打印输出结果: getStringArrayValueSync, result: I'm one of the array's values.
11. } catch (error) {
12. let code = (error as BusinessError).code;
13. let message = (error as BusinessError).message;
14. console.error(`getStringArrayValueSync failed, error code: ${code}, message: ${message}.`);
15. }
16. }
17. }
```

### getStringArrayByNameSync10+

PhonePC/2in1TabletTVWearable

getStringArrayByNameSync(resName: string): Array<string>

获取指定资源名称对应的字符串数组，使用同步方式返回。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resName | string | 是 | 资源名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 对应资源名称的字符串数组。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001003 | Invalid resource name. |
| 9001004 | No matching resource is found based on the resource name. |
| 9001006 | The resource is referenced cyclically. |

**示例：**

```
1. // 资源文件路径: src/main/resources/base/element/strarray.json
2. {
3. "strarray": [
4. {
5. "name": "test",
6. "value": [
7. {
8. "value": "I'm one of the array's values."
9. }
10. ]
11. }
12. ]
13. }
```

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. try {
7. // "test"仅作示例，请替换为实际使用的资源
8. let strArray: Array<string> = this.context.resourceManager.getStringArrayByNameSync("test");
9. console.info(`getStringArrayByNameSync, result: ${strArray[0]}`);
10. // 打印输出结果: getStringArrayByNameSync, result: I'm one of the array's values.
11. } catch (error) {
12. let code = (error as BusinessError).code;
13. let message = (error as BusinessError).message;
14. console.error(`getStringArrayByNameSync failed, error code: ${code}, message: ${message}.`);
15. }
16. }
17. }
```

### getStringArrayValue9+

PhonePC/2in1TabletTVWearable

getStringArrayValue(resId: number, callback: \_AsyncCallback<Array<string>>): void

获取指定资源ID对应的字符串数组，使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resId | number | 是 | 资源ID值。 |
| callback | [\_AsyncCallback](js-apis-base.md#asynccallback)<Array<string>> | 是 | 回调函数，返回资源ID值对应的字符串数组。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |

**示例：**

```
1. // 资源文件路径: src/main/resources/base/element/strarray.json
2. {
3. "strarray": [
4. {
5. "name": "test",
6. "value": [
7. {
8. "value": "I'm one of the array's values."
9. }
10. ]
11. }
12. ]
13. }
```

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. // 'app.strarray.test'仅作示例，请替换为实际使用的资源
7. this.context.resourceManager.getStringArrayValue($r('app.strarray.test').id,
8. (error: BusinessError, value: Array<string>) => {
9. if (error != null) {
10. console.error(`callback getStringArrayValue failed, error code: ${error.code}, message: ${error.message}.`);
11. } else {
12. console.info(`getStringArrayValue, result: ${value[0]}`);
13. // 打印输出结果: getStringArrayValue, result: I'm one of the array's values.
14. }
15. });
16. }
17. }
```

### getStringArrayValue9+

PhonePC/2in1TabletTVWearable

getStringArrayValue(resId: number): Promise<Array<string>>

获取指定资源ID对应的字符串数组，使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resId | number | 是 | 资源ID值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<string>> | Promise对象，返回资源ID值对应的字符串数组。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |

**示例：**

```
1. // 资源文件路径: src/main/resources/base/element/strarray.json
2. {
3. "strarray": [
4. {
5. "name": "test",
6. "value": [
7. {
8. "value": "I'm one of the array's values."
9. }
10. ]
11. }
12. ]
13. }
```

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. // 'app.strarray.test'仅作示例，请替换为实际使用的资源
7. this.context.resourceManager.getStringArrayValue($r('app.strarray.test').id)
8. .then((value: Array<string>) => {
9. console.info(`getStringArrayValue, result: ${value[0]}`);
10. // 打印输出结果: getStringArrayValue, result: I'm one of the array's values.
11. })
12. .catch((error: BusinessError) => {
13. console.error(`promise getStringArrayValue failed, error code: ${error.code}, message: ${error.message}.`);
14. });
15. }
16. }
```

### getStringArrayByName9+

PhonePC/2in1TabletTVWearable

getStringArrayByName(resName: string, callback: \_AsyncCallback<Array<string>>): void

获取指定资源名称对应的字符串数组，使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resName | string | 是 | 资源名称。 |
| callback | [\_AsyncCallback](js-apis-base.md#asynccallback)<Array<string>> | 是 | 回调函数，返回资源名称对应的字符串数组。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001003 | Invalid resource name. |
| 9001004 | No matching resource is found based on the resource name. |
| 9001006 | The resource is referenced cyclically. |

**示例：**

```
1. // 资源文件路径: src/main/resources/base/element/strarray.json
2. {
3. "strarray": [
4. {
5. "name": "test",
6. "value": [
7. {
8. "value": "I'm one of the array's values."
9. }
10. ]
11. }
12. ]
13. }
```

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. // "test"仅作示例，请替换为实际使用的资源
7. this.context.resourceManager.getStringArrayByName("test", (error: BusinessError, value: Array<string>) => {
8. if (error != null) {
9. console.error(`callback getStringArrayByName failed, error code: ${error.code}, message: ${error.message}.`);
10. } else {
11. let strArray = value;
12. console.info(`getStringArrayByName, result: ${value[0]}`);
13. // 打印输出结果: getStringArrayByName, result: I'm one of the array's values.
14. }
15. });
16. }
17. }
```

### getStringArrayByName9+

PhonePC/2in1TabletTVWearable

getStringArrayByName(resName: string): Promise<Array<string>>

获取指定资源名称对应的字符串数组，使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resName | string | 是 | 资源名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<string>> | Promise对象，返回资源名称对应的字符串数组。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001003 | Invalid resource name. |
| 9001004 | No matching resource is found based on the resource name. |
| 9001006 | The resource is referenced cyclically. |

**示例：**

```
1. // 资源文件路径: src/main/resources/base/element/strarray.json
2. {
3. "strarray": [
4. {
5. "name": "test",
6. "value": [
7. {
8. "value": "I'm one of the array's values."
9. }
10. ]
11. }
12. ]
13. }
```

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. // "test"仅作示例，请替换为实际使用的资源
7. this.context.resourceManager.getStringArrayByName("test")
8. .then((value: Array<string>) => {
9. console.info(`getStringArrayByName, result: ${value[0]}`);
10. // 打印输出结果: getStringArrayByName, result: I'm one of the array's values.
11. })
12. .catch((error: BusinessError) => {
13. console.error(`promise getStringArrayByName failed, error code: ${error.code}, message: ${error.message}.`);
14. });
15. }
16. }
```

### getIntPluralStringValueSync18+

PhonePC/2in1TabletTVWearable

getIntPluralStringValueSync(resId: number, num: number, ...args: Array<string | number>): string

获取指定资源ID对应的[单复数](../harmonyos-guides/l10n-singular-plural.md)字符串，并根据args参数对字符串进行格式化，使用同步方式返回。

说明

* 中文环境下，字符串不区分单复数；其他语言环境下，字符串区分单复数，具体规则参考[语言单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)。
* 在英语、德语等语言中，单复数类型包括基数词（如1、2、3）和序数词（如1st、2nd、3rd），本接口仅支持在基数词类型下使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resId | number | 是 | 资源ID值。 |
| num | number | 是 | 数量值（整数）。根据当前语言的[单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)获取该数量值对应的字符串。 |
| ...args | Array<string | number> | 否 | 格式化字符串资源参数。  支持参数类型：%d、%f、%s、%%、%数字$d、%数字$f、%数字$s。  说明：%%转义为%; %数字$d中的数字表示使用args中的第几个参数。  举例：%%d格式化后为%d字符串; %1$d表示使用第一个参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 资源ID值对应的格式化单复数字符串。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |
| 9001007 | Failed to format the resource obtained based on the resource ID. |

**示例：**

```
1. // 资源文件路径: src/main/resources/base/element/plural.json
2. {
3. "plural": [
4. {
5. "name": "format_test",
6. "value": [
7. {
8. "quantity": "one",
9. "value": "There is %d apple in the %s, the total amount is %f kg."
10. },
11. {
12. "quantity": "other",
13. "value": "There are %d apples in the %s, the total amount is %f kg."
14. }
15. ]
16. }
17. ]
18. }
```

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. try {
7. // 根据语言单复数规则，参数num取值为1，英文环境下对应单复数类别为one
8. // 在资源文件中用quantity字段表示单复数类别，因此会获取quantity为one的字符串
9. // 'app.plural.format_test'仅作示例，请替换为实际使用的资源
10. let pluralStr = this.context.resourceManager.getIntPluralStringValueSync($r('app.plural.format_test').id, 1, 1, "basket", 0.3);
11. console.info(`getIntPluralStringValueSync, result: ${pluralStr}`);
12. // 打印输出结果: getIntPluralStringValueSync, result: There is 1 apple in the basket, the total amount is 0.3 kg.
13. } catch (error) {
14. let code = (error as BusinessError).code;
15. let message = (error as BusinessError).message;
16. console.error(`getIntPluralStringValueSync failed, error code: ${code}, message: ${message}.`);
17. }
18. }
19. }
```

### getIntPluralStringByNameSync18+

PhonePC/2in1TabletTVWearable

getIntPluralStringByNameSync(resName: string, num: number, ...args: Array<string | number>): string

获取指定资源名称对应的[单复数](../harmonyos-guides/l10n-singular-plural.md)字符串，并根据args参数对字符串进行格式化，使用同步方式返回。

说明

* 中文环境下，字符串不区分单复数；其他语言环境下，字符串区分单复数，具体规则参考[语言单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)。
* 在英语、德语等语言中，单复数类型包括基数词（如1、2、3）和序数词（如1st、2nd、3rd），本接口仅支持在基数词类型下使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resName | string | 是 | 资源名称。 |
| num | number | 是 | 数量值（整数）。根据当前语言的[单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)获取该数量值对应的字符串。 |
| ...args | Array<string | number> | 否 | 格式化字符串资源参数。  支持参数类型：%d、%f、%s、%%、%数字$d、%数字$f、%数字$s。  说明：%%转义为%; %数字$d中的数字表示使用args中的第几个参数。  举例：%%d格式化后为%d字符串; %1$d表示使用第一个参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 资源名称对应的格式化单复数字符串。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9001003 | Invalid resource name. |
| 9001004 | No matching resource is found based on the resource name. |
| 9001006 | The resource is referenced cyclically. |
| 9001008 | Failed to format the resource obtained based on the resource name. |

**示例：**

```
1. // 资源文件路径: src/main/resources/base/element/plural.json
2. {
3. "plural": [
4. {
5. "name": "format_test",
6. "value": [
7. {
8. "quantity": "one",
9. "value": "There is %d apple in the %s, the total amount is %f kg."
10. },
11. {
12. "quantity": "other",
13. "value": "There are %d apples in the %s, the total amount is %f kg."
14. }
15. ]
16. }
17. ]
18. }
```

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. try {
7. // 根据语言单复数规则，参数num取值为1，英文环境下对应单复数类别为one
8. // 在资源文件中用quantity字段表示单复数类别，因此会获取quantity为one的字符串
9. // "format_test"仅作示例，请替换为实际使用的资源
10. let pluralStr = this.context.resourceManager.getIntPluralStringByNameSync("format_test", 1, 1, "basket", 0.3);
11. console.info(`getIntPluralStringByNameSync, result: ${pluralStr}`);
12. // 打印输出结果: getIntPluralStringByNameSync, result: There is 1 apple in the basket, the total amount is 0.3 kg.
13. } catch (error) {
14. let code = (error as BusinessError).code;
15. let message = (error as BusinessError).message;
16. console.error(`getIntPluralStringByNameSync failed, error code: ${code}, message: ${message}.`);
17. }
18. }
19. }
```

### getDoublePluralStringValueSync18+

PhonePC/2in1TabletTVWearable

getDoublePluralStringValueSync(resId: number, num: number, ...args: Array<string | number>): string

获取指定资源ID对应的[单复数](../harmonyos-guides/l10n-singular-plural.md)字符串，并根据args参数对字符串进行格式化，使用同步方式返回。

说明

* 中文环境下，字符串不区分单复数；其他语言环境下，字符串区分单复数，具体规则参考[语言单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)。
* 在英语、德语等语言中，单复数类型包括基数词（如1、2、3）和序数词（如1st、2nd、3rd），本接口仅支持在基数词类型下使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resId | number | 是 | 资源ID值。 |
| num | number | 是 | 数量值（浮点数）。根据当前语言的[单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)获取该数量值对应的字符串。 |
| ...args | Array<string | number> | 否 | 格式化字符串资源参数。  支持参数类型：%d、%f、%s、%%、%数字$d、%数字$f、%数字$s。  说明：%%转义为%; %数字$d中的数字表示使用args中的第几个参数。  举例：%%d格式化后为%d字符串; %1$d表示使用第一个参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 资源ID值对应的格式化单复数字符串。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |
| 9001007 | Failed to format the resource obtained based on the resource ID. |

**示例：**

```
1. // 资源文件路径: src/main/resources/base/element/plural.json
2. {
3. "plural": [
4. {
5. "name": "format_test",
6. "value": [
7. {
8. "quantity": "one",
9. "value": "There is %d apple in the %s, the total amount is %f kg."
10. },
11. {
12. "quantity": "other",
13. "value": "There are %d apples in the %s, the total amount is %f kg."
14. }
15. ]
16. }
17. ]
18. }
```

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. try {
7. // 根据语言单复数规则，参数num取值为2.1，英文环境下对应单复数类别为other
8. // 在资源文件中用quantity字段表示单复数类别，因此会获取quantity为other的字符串
9. // 'app.plural.format_test'仅作示例，请替换为实际使用的资源
10. let pluralStr = this.context.resourceManager.getDoublePluralStringValueSync($r('app.plural.format_test').id, 2.1, 2, "basket", 0.6);
11. console.info(`getDoublePluralStringValueSync, result: ${pluralStr}`);
12. // 打印输出结果: getDoublePluralStringValueSync, result: There are 2 apples in the basket, the total amount is 0.6 kg.
13. } catch (error) {
14. let code = (error as BusinessError).code;
15. let message = (error as BusinessError).message;
16. console.error(`getDoublePluralStringValueSync failed, error code: ${code}, message: ${message}.`);
17. }
18. }
19. }
```

### getDoublePluralStringByNameSync18+

PhonePC/2in1TabletTVWearable

getDoublePluralStringByNameSync(resName: string, num: number, ...args: Array<string | number>): string

获取指定资源名称对应的[单复数](../harmonyos-guides/l10n-singular-plural.md)字符串，并根据args参数对字符串进行格式化，使用同步方式返回。

说明

* 中文环境下，字符串不区分单复数；其他语言环境下，字符串区分单复数，具体规则参考[语言单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)。
* 在英语、德语等语言中，单复数类型包括基数词（如1、2、3）和序数词（如1st、2nd、3rd），本接口仅支持在基数词类型下使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resName | string | 是 | 资源名称。 |
| num | number | 是 | 数量值（浮点数）。根据当前语言的[单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)获取该数量值对应的字符串。 |
| ...args | Array<string | number> | 否 | 格式化字符串资源参数。  支持参数类型：%d、%f、%s、%%、%数字$d、%数字$f、%数字$s。  说明：%%转义为%; %数字$d中的数字表示使用args中的第几个参数。  举例：%%d格式化后为%d字符串; %1$d表示使用第一个参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 资源名称对应的格式化单复数字符串。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9001003 | Invalid resource name. |
| 9001004 | No matching resource is found based on the resource name. |
| 9001006 | The resource is referenced cyclically. |
| 9001008 | Failed to format the resource obtained based on the resource name. |

**示例：**

```
1. // 资源文件路径: src/main/resources/base/element/plural.json
2. {
3. "plural": [
4. {
5. "name": "format_test",
6. "value": [
7. {
8. "quantity": "one",
9. "value": "There is %d apple in the %s, the total amount is %f kg."
10. },
11. {
12. "quantity": "other",
13. "value": "There are %d apples in the %s, the total amount is %f kg."
14. }
15. ]
16. }
17. ]
18. }
```

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. try {
7. // 根据语言单复数规则，参数num取值为2.1，英文环境下对应单复数类别为other
8. // 在资源文件中用quantity字段表示单复数类别，因此会获取quantity为other的字符串
9. // "format_test"仅作示例，请替换为实际使用的资源
10. let pluralStr = this.context.resourceManager.getDoublePluralStringByNameSync("format_test", 2.1, 2, "basket", 0.6);
11. console.info(`getDoublePluralStringByNameSync, result: ${pluralStr}`);
12. // 打印输出结果: getDoublePluralStringByNameSync, result: There are 2 apples in the basket, the total amount is 0.6 kg.
13. } catch (error) {
14. let code = (error as BusinessError).code;
15. let message = (error as BusinessError).message;
16. console.error(`getDoublePluralStringByNameSync failed, error code: ${code}, message: ${message}.`);
17. }
18. }
19. }
```

### getMediaContentSync10+

PhonePC/2in1TabletTVWearable

getMediaContentSync(resId: number, density?: number): Uint8Array

获取指定资源ID对应的默认或指定的屏幕密度媒体文件内容，使用同步方式返回。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resId | number | 是 | 资源ID值。 |
| [density](js-apis-resource-manager.md#screendensity) | number | 否 | 资源获取需要的屏幕密度，0或缺省表示默认屏幕密度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | 资源ID对应的媒体文件内容。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |

**示例：**

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. try {
7. // 'app.media.test'仅作示例，请替换为实际使用的资源
8. this.context.resourceManager.getMediaContentSync($r('app.media.test').id); // 默认屏幕密度
9. } catch (error) {
10. let code = (error as BusinessError).code;
11. let message = (error as BusinessError).message;
12. console.error(`getMediaContentSync failed, error code: ${code}, message: ${message}.`);
13. }

15. try {
16. // 'app.media.test'仅作示例，请替换为实际使用的资源
17. this.context.resourceManager.getMediaContentSync($r('app.media.test').id, 120); // 指定屏幕密度
18. } catch (error) {
19. let code = (error as BusinessError).code;
20. let message = (error as BusinessError).message;
21. console.error(`getMediaContentSync failed, error code: ${code}, message: ${message}.`);
22. }
23. }
24. }
```

### getMediaByNameSync10+

PhonePC/2in1TabletTVWearable

getMediaByNameSync(resName: string, density?: number): Uint8Array

获取指定资源名称对应的默认或指定的屏幕密度媒体文件内容，使用同步方式返回。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resName | string | 是 | 资源名称。 |
| [density](js-apis-resource-manager.md#screendensity) | number | 否 | 资源获取需要的屏幕密度，0或缺省表示默认屏幕密度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | 资源名称对应的媒体文件内容。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |
| 9001003 | Invalid resource name. |
| 9001004 | No matching resource is found based on the resource name. |

**示例：**

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. try {
7. // "test"仅作示例，请替换为实际使用的资源
8. this.context.resourceManager.getMediaByNameSync("test"); // 默认屏幕密度
9. } catch (error) {
10. let code = (error as BusinessError).code;
11. let message = (error as BusinessError).message;
12. console.error(`getMediaByNameSync failed, error code: ${code}, message: ${message}.`);
13. }

15. try {
16. // "test"仅作示例，请替换为实际使用的资源
17. this.context.resourceManager.getMediaByNameSync("test", 120); // 指定屏幕密度
18. } catch (error) {
19. let code = (error as BusinessError).code;
20. let message = (error as BusinessError).message;
21. console.error(`getMediaByNameSync failed, error code: ${code}, message: ${message}.`);
22. }
23. }
24. }
```

### getMediaContent9+

PhonePC/2in1TabletTVWearable

getMediaContent(resId: number, callback: \_AsyncCallback<Uint8Array>): void

获取指定资源ID对应的媒体文件内容，使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resId | number | 是 | 资源ID值。 |
| callback | [\_AsyncCallback](js-apis-base.md#asynccallback)<Uint8Array> | 是 | 回调函数，返回资源ID对应的媒体文件内容。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |

**示例：**

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. try {
7. // 'app.media.test'仅作示例，请替换为实际使用的资源
8. this.context.resourceManager.getMediaContent($r('app.media.test').id,
9. (error: BusinessError, value: Uint8Array) => {
10. if (error != null) {
11. console.error("error is " + error);
12. } else {
13. let media = value;
14. }
15. });
16. } catch (error) {
17. let code = (error as BusinessError).code;
18. let message = (error as BusinessError).message;
19. console.error(`callback getMediaContent failed, error code: ${code}, message: ${message}.`);
20. }
21. }
22. }
```

### getMediaContent10+

PhonePC/2in1TabletTVWearable

getMediaContent(resId: number, density: number, callback: \_AsyncCallback<Uint8Array>): void

获取指定资源ID对应的指定屏幕密度媒体文件内容，使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resId | number | 是 | 资源ID值。 |
| [density](js-apis-resource-manager.md#screendensity) | number | 是 | 资源获取需要的屏幕密度，0表示默认屏幕密度。 |
| callback | [\_AsyncCallback](js-apis-base.md#asynccallback)<Uint8Array> | 是 | 回调函数，返回资源ID对应的媒体文件内容。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |

**示例：**

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. try {
7. // 'app.media.test'仅作示例，请替换为实际使用的资源
8. this.context.resourceManager.getMediaContent($r('app.media.test').id, 120, (error: BusinessError, value: Uint8Array) => {
9. if (error != null) {
10. console.error(`callback getMediaContent failed, error code: ${error.code}, message: ${error.message}.`);
11. } else {
12. let media = value;
13. }
14. });
15. } catch (error) {
16. let code = (error as BusinessError).code;
17. let message = (error as BusinessError).message;
18. console.error(`callback getMediaContent failed, error code: ${code}, message: ${message}.`);
19. }
20. }
21. }
```

### getMediaContent9+

PhonePC/2in1TabletTVWearable

getMediaContent(resId: number): Promise<Uint8Array>

获取指定资源ID对应的媒体文件内容，使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resId | number | 是 | 资源ID值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Uint8Array> | Promise对象，返回资源ID值对应的媒体文件内容。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |

**示例：**

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. try {
7. // 'app.media.test'仅作示例，请替换为实际使用的资源
8. this.context.resourceManager.getMediaContent($r('app.media.test').id).then((value: Uint8Array) => {
9. let media = value;
10. }).catch((error: BusinessError) => {
11. console.error("getMediaContent promise error is " + error);
12. });
13. } catch (error) {
14. let code = (error as BusinessError).code;
15. let message = (error as BusinessError).message;
16. console.error(`promise getMediaContent failed, error code: ${code}, message: ${message}.`);
17. }
18. }
19. }
```

### getMediaContent10+

PhonePC/2in1TabletTVWearable

getMediaContent(resId: number, density: number): Promise<Uint8Array>

获取指定资源ID对应的指定屏幕密度媒体文件内容，使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resId | number | 是 | 资源ID值。 |
| [density](js-apis-resource-manager.md#screendensity) | number | 是 | 资源获取需要的屏幕密度，0表示默认屏幕密度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Uint8Array> | Promise对象，返回资源ID值对应的媒体文件内容。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |

**示例：**

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. try {
7. // 'app.media.test'仅作示例，请替换为实际使用的资源
8. this.context.resourceManager.getMediaContent($r('app.media.test').id, 120).then((value: Uint8Array) => {
9. let media = value;
10. }).catch((error: BusinessError) => {
11. console.error(`promise getMediaContent failed, error code: ${error.code}, message: ${error.message}.`);
12. });
13. } catch (error) {
14. let code = (error as BusinessError).code;
15. let message = (error as BusinessError).message;
16. console.error(`promise getMediaContent failed, error code: ${code}, message: ${message}.`);
17. }
18. }
19. }
```

### getMediaByName9+

PhonePC/2in1TabletTVWearable

getMediaByName(resName: string, callback: \_AsyncCallback<Uint8Array>): void

获取指定资源名称对应的媒体文件内容，使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resName | string | 是 | 资源名称。 |
| callback | [\_AsyncCallback](js-apis-base.md#asynccallback)<Uint8Array> | 是 | 回调函数，返回资源名称对应的媒体文件内容。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001003 | Invalid resource name. |
| 9001004 | No matching resource is found based on the resource name. |

**示例：**

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. try {
7. // "test"仅作示例，请替换为实际使用的资源
8. this.context.resourceManager.getMediaByName("test", (error: BusinessError, value: Uint8Array) => {
9. if (error != null) {
10. console.error("error is " + error);
11. } else {
12. let media = value;
13. }
14. });
15. } catch (error) {
16. let code = (error as BusinessError).code;
17. let message = (error as BusinessError).message;
18. console.error(`callback getMediaByName failed, error code: ${code}, message: ${message}.`);
19. }
20. }
21. }
```

### getMediaByName10+

PhonePC/2in1TabletTVWearable

getMediaByName(resName: string, density: number, callback: \_AsyncCallback<Uint8Array>): void

获取指定资源名称对应的指定屏幕密度媒体文件内容，使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resName | string | 是 | 资源名称。 |
| [density](js-apis-resource-manager.md#screendensity) | number | 是 | 资源获取需要的屏幕密度，0表示默认屏幕密度。 |
| callback | [\_AsyncCallback](js-apis-base.md#asynccallback)<Uint8Array> | 是 | 回调函数，返回资源名称对应的媒体文件内容。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |
| 9001003 | Invalid resource name. |
| 9001004 | No matching resource is found based on the resource name. |

**示例：**

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. try {
7. // "test"仅作示例，请替换为实际使用的资源
8. this.context.resourceManager.getMediaByName("test", 120, (error: BusinessError, value: Uint8Array) => {
9. if (error != null) {
10. console.error(`callback getMediaByName failed, error code: ${error.code}, message: ${error.message}.`);
11. } else {
12. let media = value;
13. }
14. });
15. } catch (error) {
16. let code = (error as BusinessError).code;
17. let message = (error as BusinessError).message;
18. console.error(`callback getMediaByName failed, error code: ${code}, message: ${message}.`);
19. }
20. }
21. }
```

### getMediaByName9+

PhonePC/2in1TabletTVWearable

getMediaByName(resName: string): Promise<Uint8Array>

获取指定资源名称对应的媒体文件内容，使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resName | string | 是 | 资源名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Uint8Array> | Promise对象，返回资源名称对应的媒体文件内容。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001003 | Invalid resource name. |
| 9001004 | No matching resource is found based on the resource name. |

**示例：**

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. try {
7. // "test"仅作示例，请替换为实际使用的资源
8. this.context.resourceManager.getMediaByName("test").then((value: Uint8Array) => {
9. let media = value;
10. }).catch((error: BusinessError) => {
11. console.error("getMediaByName promise error is " + error);
12. });
13. } catch (error) {
14. let code = (error as BusinessError).code;
15. let message = (error as BusinessError).message;
16. console.error(`promise getMediaByName failed, error code: ${code}, message: ${message}.`);
17. }
18. }
19. }
```

### getMediaByName10+

PhonePC/2in1TabletTVWearable

getMediaByName(resName: string, density: number): Promise<Uint8Array>

获取指定资源名称对应的指定屏幕密度媒体文件内容，使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resName | string | 是 | 资源名称。 |
| [density](js-apis-resource-manager.md#screendensity) | number | 是 | 资源获取需要的屏幕密度，0表示默认屏幕密度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Uint8Array> | Promise对象，返回资源名称对应的媒体文件内容。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |
| 9001003 | Invalid resource name. |
| 9001004 | No matching resource is found based on the resource name. |

**示例：**

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. try {
7. // "test"仅作示例，请替换为实际使用的资源
8. this.context.resourceManager.getMediaByName("test", 120).then((value: Uint8Array) => {
9. let media = value;
10. }).catch((error: BusinessError) => {
11. console.error(`promise getMediaByName failed, error code: ${error.code}, message: ${error.message}.`);
12. });
13. } catch (error) {
14. let code = (error as BusinessError).code;
15. let message = (error as BusinessError).message;
16. console.error(`promise getMediaByName failed, error code: ${code}, message: ${message}.`);
17. }
18. }
19. }
```

### getMediaContentBase64Sync10+

PhonePC/2in1TabletTVWearable

getMediaContentBase64Sync(resId: number, density?: number): string

获取指定资源ID对应的默认或指定的屏幕密度图片资源Base64编码，使用同步方式返回。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resId | number | 是 | 资源ID值。 |
| [density](js-apis-resource-manager.md#screendensity) | number | 否 | 资源获取需要的屏幕密度，0或缺省表示默认屏幕密度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 资源ID对应的图片资源Base64编码。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |

**示例：**

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. try {
7. // 'app.media.test'仅作示例，请替换为实际使用的资源
8. this.context.resourceManager.getMediaContentBase64Sync($r('app.media.test').id); // 默认屏幕密度
9. } catch (error) {
10. let code = (error as BusinessError).code;
11. let message = (error as BusinessError).message;
12. console.error(`getMediaContentBase64Sync failed, error code: ${code}, message: ${message}.`);
13. }

15. try {
16. // 'app.media.test'仅作示例，请替换为实际使用的资源
17. this.context.resourceManager.getMediaContentBase64Sync($r('app.media.test').id, 120); // 指定屏幕密度
18. } catch (error) {
19. let code = (error as BusinessError).code;
20. let message = (error as BusinessError).message;
21. console.error(`getMediaContentBase64Sync failed, error code: ${code}, message: ${message}.`);
22. }
23. }
24. }
```

### getMediaBase64ByNameSync10+

PhonePC/2in1TabletTVWearable

getMediaBase64ByNameSync(resName: string, density?: number): string

获取指定资源名称对应的默认或指定的屏幕密度图片资源Base64编码，使用同步方式返回。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resName | string | 是 | 资源名称。 |
| [density](js-apis-resource-manager.md#screendensity) | number | 否 | 资源获取需要的屏幕密度，0或缺省表示默认屏幕密度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 资源名称对应的图片资源Base64编码。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |
| 9001003 | Invalid resource name. |
| 9001004 | No matching resource is found based on the resource name. |

**示例：**

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. try {
7. // "test"仅作示例，请替换为实际使用的资源
8. this.context.resourceManager.getMediaBase64ByNameSync("test"); // 默认屏幕密度
9. } catch (error) {
10. let code = (error as BusinessError).code;
11. let message = (error as BusinessError).message;
12. console.error(`getMediaBase64ByNameSync failed, error code: ${code}, message: ${message}.`);
13. }

15. try {
16. // "test"仅作示例，请替换为实际使用的资源
17. this.context.resourceManager.getMediaBase64ByNameSync("test", 120); // 指定屏幕密度
18. } catch (error) {
19. let code = (error as BusinessError).code;
20. let message = (error as BusinessError).message;
21. console.error(`getMediaBase64ByNameSync failed, error code: ${code}, message: ${message}.`);
22. }
23. }
24. }
```

### getMediaContentBase649+

PhonePC/2in1TabletTVWearable

getMediaContentBase64(resId: number, callback: \_AsyncCallback<string>): void

获取指定资源ID对应的图片资源Base64编码，使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resId | number | 是 | 资源ID值。 |
| callback | [\_AsyncCallback](js-apis-base.md#asynccallback)<string> | 是 | 回调函数，返回资源ID值对应的图片资源Base64编码。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |

**示例：**

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. try {
7. // 'app.media.test'仅作示例，请替换为实际使用的资源
8. this.context.resourceManager.getMediaContentBase64($r('app.media.test').id, (error: BusinessError, value: string) => {
9. if (error != null) {
10. console.error("error is " + error);
11. } else {
12. let media = value;
13. }
14. });
15. } catch (error) {
16. let code = (error as BusinessError).code;
17. let message = (error as BusinessError).message;
18. console.error(`callback getMediaContentBase64 failed, error code: ${code}, message: ${message}.`);
19. }
20. }
21. }
```

### getMediaContentBase6410+

PhonePC/2in1TabletTVWearable

getMediaContentBase64(resId: number, density: number, callback: \_AsyncCallback<string>): void

获取指定资源ID对应的指定屏幕密度图片资源Base64编码，使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resId | number | 是 | 资源ID值。 |
| [density](js-apis-resource-manager.md#screendensity) | number | 是 | 资源获取需要的屏幕密度，0表示默认屏幕密度。 |
| callback | [\_AsyncCallback](js-apis-base.md#asynccallback)<string> | 是 | 回调函数，返回资源ID值对应的图片资源Base64编码。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |

**示例：**

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. try {
7. // 'app.media.test'仅作示例，请替换为实际使用的资源
8. this.context.resourceManager.getMediaContentBase64($r('app.media.test').id, 120, (error: BusinessError, value: string) => {
9. if (error != null) {
10. console.error(`callback getMediaContentBase64 failed, error code: ${error.code}, message: ${error.message}.`);
11. } else {
12. let media = value;
13. }
14. });
15. } catch (error) {
16. let code = (error as BusinessError).code;
17. let message = (error as BusinessError).message;
18. console.error(`callback getMediaContentBase64 failed, error code: ${code}, message: ${message}.`);
19. }
20. }
21. }
```

### getMediaContentBase649+

PhonePC/2in1TabletTVWearable

getMediaContentBase64(resId: number): Promise<string>

获取指定资源ID对应的图片资源Base64编码，使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resId | number | 是 | 资源ID值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回资源ID值对应的图片资源Base64编码。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |

**示例：**

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. try {
7. // 'app.media.test'仅作示例，请替换为实际使用的资源
8. this.context.resourceManager.getMediaContentBase64($r('app.media.test').id).then((value: string) => {
9. let media = value;
10. }).catch((error: BusinessError) => {
11. console.error("getMediaContentBase64 promise error is " + error);
12. });
13. } catch (error) {
14. let code = (error as BusinessError).code;
15. let message = (error as BusinessError).message;
16. console.error(`promise getMediaContentBase64 failed, error code: ${code}, message: ${message}.`);
17. }
18. }
19. }
```

### getMediaContentBase6410+

PhonePC/2in1TabletTVWearable

getMediaContentBase64(resId: number, density: number): Promise<string>

获取指定资源ID对应的指定屏幕密度图片资源Base64编码，使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resId | number | 是 | 资源ID值。 |
| [density](js-apis-resource-manager.md#screendensity) | number | 是 | 资源获取需要的屏幕密度，0表示默认屏幕密度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回资源ID值对应的图片资源Base64编码。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |

**示例：**

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. try {
7. // 'app.media.test'仅作示例，请替换为实际使用的资源
8. this.context.resourceManager.getMediaContentBase64($r('app.media.test').id, 120).then((value: string) => {
9. let media = value;
10. }).catch((error: BusinessError) => {
11. console.error(`promise getMediaContentBase64 failed, error code: ${error.code}, message: ${error.message}.`);
12. });
13. } catch (error) {
14. let code = (error as BusinessError).code;
15. let message = (error as BusinessError).message;
16. console.error(`promise getMediaContentBase64 failed, error code: ${code}, message: ${message}.`);
17. }
18. }
19. }
```

### getMediaBase64ByName9+

PhonePC/2in1TabletTVWearable

getMediaBase64ByName(resName: string, callback: \_AsyncCallback<string>): void

获取指定资源名称对应的图片资源Base64编码，使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resName | string | 是 | 资源名称。 |
| callback | [\_AsyncCallback](js-apis-base.md#asynccallback)<string> | 是 | 回调函数，返回资源名称的图片资源Base64编码。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001003 | Invalid resource name. |
| 9001004 | No matching resource is found based on the resource name. |

**示例：**

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. try {
7. // "test"仅作示例，请替换为实际使用的资源
8. this.context.resourceManager.getMediaBase64ByName("test", (error: BusinessError, value: string) => {
9. if (error != null) {
10. console.error("error is " + error);
11. } else {
12. let media = value;
13. }
14. });
15. } catch (error) {
16. let code = (error as BusinessError).code;
17. let message = (error as BusinessError).message;
18. console.error(`callback getMediaBase64ByName failed, error code: ${code}, message: ${message}.`);
19. }
20. }
21. }
```

### getMediaBase64ByName10+

PhonePC/2in1TabletTVWearable

getMediaBase64ByName(resName: string, density: number, callback: \_AsyncCallback<string>): void

获取指定资源名称对应的指定屏幕密度图片资源Base64编码，使用callback异步回调。

说明

推荐使用[getMediaBase64ByName](js-apis-resource-manager.md#getmediacontentbase6410)或[getMediaContentBase64](js-apis-resource-manager.md#getmediacontentbase6410)接口，具体请参考[ResourceManager](js-apis-resource-manager.md#resourcemanager)的说明。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resName | string | 是 | 资源名称。 |
| [density](js-apis-resource-manager.md#screendensity) | number | 是 | 资源获取需要的屏幕密度，0表示默认屏幕密度。 |
| callback | [\_AsyncCallback](js-apis-base.md#asynccallback)<string> | 是 | 回调函数，返回资源名称的图片资源Base64编码。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |
| 9001003 | Invalid resource name. |
| 9001004 | No matching resource is found based on the resource name. |

**示例：**

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. try {
7. // "test"仅作示例，请替换为实际使用的资源
8. this.context.resourceManager.getMediaBase64ByName("test", 120, (error: BusinessError, value: string) => {
9. if (error != null) {
10. console.error(`callback getMediaBase64ByName failed, error code: ${error.code}, message: ${error.message}.`);
11. } else {
12. let media = value;
13. }
14. });
15. } catch (error) {
16. let code = (error as BusinessError).code;
17. let message = (error as BusinessError).message;
18. console.error(`callback getMediaBase64ByName failed, error code: ${code}, message: ${message}.`);
19. }
20. }
21. }
```

### getMediaBase64ByName9+

PhonePC/2in1TabletTVWearable

getMediaBase64ByName(resName: string): Promise<string>

获取指定资源名称对应的图片资源Base64编码，使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resName | string | 是 | 资源名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回资源名称对应的图片资源Base64编码。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001003 | Invalid resource name. |
| 9001004 | No matching resource is found based on the resource name. |

**示例：**

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. try {
7. // "test"仅作示例，请替换为实际使用的资源
8. this.context.resourceManager.getMediaBase64ByName("test").then((value: string) => {
9. let media = value;
10. }).catch((error: BusinessError) => {
11. console.error("getMediaBase64ByName promise error is " + error);
12. });
13. } catch (error) {
14. let code = (error as BusinessError).code;
15. let message = (error as BusinessError).message;
16. console.error(`promise getMediaBase64ByName failed, error code: ${code}, message: ${message}.`);
17. }
18. }
19. }
```

### getMediaBase64ByName10+

PhonePC/2in1TabletTVWearable

getMediaBase64ByName(resName: string, density: number): Promise<string>

获取指定资源名称对应的指定屏幕密度图片资源Base64编码，使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resName | string | 是 | 资源名称。 |
| [density](js-apis-resource-manager.md#screendensity) | number | 是 | 资源获取需要的屏幕密度，0表示默认屏幕密度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回资源名称对应的图片资源Base64编码。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |
| 9001003 | Invalid resource name. |
| 9001004 | No matching resource is found based on the resource name. |

**示例：**

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. try {
7. // "test"仅作示例，请替换为实际使用的资源
8. this.context.resourceManager.getMediaBase64ByName("test", 120).then((value: string) => {
9. let media = value;
10. }).catch((error: BusinessError) => {
11. console.error(`promise getMediaBase64ByName failed, error code: ${error.code}, message: ${error.message}.`);
12. });
13. } catch (error) {
14. let code = (error as BusinessError).code;
15. let message = (error as BusinessError).message;
16. console.error(`promise getMediaBase64ByName failed, error code: ${code}, message: ${message}.`);
17. }
18. }
19. }
```

### getDrawableDescriptor10+

PhonePC/2in1TabletTVWearable

getDrawableDescriptor(resId: number, density?: number, type?: number): DrawableDescriptor

获取指定资源ID对应的DrawableDescriptor对象，用于图标的显示，使用同步方式返回。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resId | number | 是 | 资源ID值。 |
| [density](js-apis-resource-manager.md#screendensity) | number | 否 | 资源获取需要的屏幕密度，0或缺省表示默认屏幕密度。 |
| type11+ | number | 否 | - 1表示获取主题资源包中应用的分层图标资源。  - 0或缺省表示获取应用自身图标资源。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DrawableDescriptor](js-apis-arkui-drawabledescriptor.md#drawabledescriptor) | 资源ID值对应的DrawableDescriptor对象。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |

**示例：**

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { DrawableDescriptor } from '@kit.ArkUI';

5. export default class EntryAbility extends UIAbility {
6. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
7. try {
8. // 'app.media.icon'仅作示例，请替换为实际使用的资源
9. let drawableDescriptor:DrawableDescriptor = this.context.resourceManager.getDrawableDescriptor($r('app.media.icon').id);
10. } catch (error) {
11. let code = (error as BusinessError).code;
12. let message = (error as BusinessError).message;
13. console.error(`getDrawableDescriptor failed, error code: ${code}, message: ${message}.`);
14. }
15. try {
16. // 'app.media.icon'仅作示例，请替换为实际使用的资源
17. let drawableDescriptor:DrawableDescriptor = this.context.resourceManager.getDrawableDescriptor($r('app.media.icon').id, 120);
18. } catch (error) {
19. let code = (error as BusinessError).code;
20. let message = (error as BusinessError).message;
21. console.error(`getDrawableDescriptor failed, error code: ${code}, message: ${message}.`);
22. }
23. try {
24. // 'app.media.icon'仅作示例，请替换为实际使用的资源
25. let drawableDescriptor:DrawableDescriptor = this.context.resourceManager.getDrawableDescriptor($r('app.media.icon').id, 0, 1);
26. } catch (error) {
27. let code = (error as BusinessError).code;
28. let message = (error as BusinessError).message;
29. console.error(`getDrawableDescriptor failed, error code: ${code}, message: ${message}.`);
30. }
31. }
32. }
```

### getDrawableDescriptorByName10+

PhonePC/2in1TabletTVWearable

getDrawableDescriptorByName(resName: string, density?: number, type?: number): DrawableDescriptor

获取指定资源名称对应的DrawableDescriptor对象，用于图标的显示，使用同步方式返回。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resName | string | 是 | 资源名称。 |
| [density](js-apis-resource-manager.md#screendensity) | number | 否 | 资源获取需要的屏幕密度，0或缺省表示默认屏幕密度。 |
| type11+ | number | 否 | - 1表示获取主题资源包中应用的分层图标资源。  - 0或缺省表示获取应用自身图标资源。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DrawableDescriptor](js-apis-arkui-drawabledescriptor.md#drawabledescriptor) | 资源名称对应的DrawableDescriptor对象。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |
| 9001003 | Invalid resource name. |
| 9001004 | No matching resource is found based on the resource name. |

**示例：**

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { DrawableDescriptor } from '@kit.ArkUI';

5. export default class EntryAbility extends UIAbility {
6. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
7. try {
8. // "icon"仅作示例，请替换为实际使用的资源
9. let drawableDescriptor:DrawableDescriptor = this.context.resourceManager.getDrawableDescriptorByName('icon');
10. } catch (error) {
11. let code = (error as BusinessError).code;
12. let message = (error as BusinessError).message;
13. console.error(`getDrawableDescriptorByName failed, error code: ${code}, message: ${message}.`);
14. }
15. try {
16. // "icon"仅作示例，请替换为实际使用的资源
17. let drawableDescriptor:DrawableDescriptor = this.context.resourceManager.getDrawableDescriptorByName('icon', 120);
18. } catch (error) {
19. let code = (error as BusinessError).code;
20. let message = (error as BusinessError).message;
21. console.error(`getDrawableDescriptorByName failed, error code: ${code}, message: ${message}.`);
22. }
23. try {
24. // "icon"仅作示例，请替换为实际使用的资源
25. let drawableDescriptor:DrawableDescriptor = this.context.resourceManager.getDrawableDescriptorByName('icon', 0, 1);
26. } catch (error) {
27. let code = (error as BusinessError).code;
28. let message = (error as BusinessError).message;
29. console.error(`getDrawableDescriptorByName failed, error code: ${code}, message: ${message}.`);
30. }
31. }
32. }
```

### getBoolean9+

PhonePC/2in1TabletTVWearable

getBoolean(resId: number): boolean

获取指定资源ID值对应的布尔值，使用同步方式返回。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resId | number | 是 | 资源ID值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 资源ID值对应的布尔值。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |

**示例：**

```
1. // 资源文件路径: src/main/resources/base/element/boolean.json
2. {
3. "boolean": [
4. {
5. "name": "boolean_test",
6. "value": true
7. }
8. ]
9. }
```

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. try {
7. // 'app.boolean.boolean_test'仅作示例，请替换为实际使用的资源
8. let boolTest = this.context.resourceManager.getBoolean($r('app.boolean.boolean_test').id);
9. console.info(`getBoolean, result: ${boolTest}`);
10. // 打印输出结果: getBoolean, result: true
11. } catch (error) {
12. let code = (error as BusinessError).code;
13. let message = (error as BusinessError).message;
14. console.error(`getBoolean failed, error code: ${code}, message: ${message}.`);
15. }
16. }
17. }
```

### getBooleanByName9+

PhonePC/2in1TabletTVWearable

getBooleanByName(resName: string): boolean

获取指定资源名称对应的布尔值，使用同步方式返回。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resName | string | 是 | 资源名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 资源名称对应的布尔值。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001003 | Invalid resource name. |
| 9001004 | No matching resource is found based on the resource name. |
| 9001006 | The resource is referenced cyclically. |

**示例：**

```
1. // 资源文件路径: src/main/resources/base/element/boolean.json
2. {
3. "boolean": [
4. {
5. "name": "boolean_test",
6. "value": true
7. }
8. ]
9. }
```

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. try {
7. // "boolean_test"仅作示例，请替换为实际使用的资源
8. let boolTest = this.context.resourceManager.getBooleanByName("boolean_test");
9. console.info(`getBooleanByName, result: ${boolTest}`);
10. // 打印输出结果: getBooleanByName, result: true
11. } catch (error) {
12. let code = (error as BusinessError).code;
13. let message = (error as BusinessError).message;
14. console.error(`getBooleanByName failed, error code: ${code}, message: ${message}.`);
15. }
16. }
17. }
```

### getNumber9+

PhonePC/2in1TabletTVWearable

getNumber(resId: number): number

获取指定资源ID对应的integer数值或者float数值，使用同步方式返回。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resId | number | 是 | 资源ID值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 资源ID值对应的数值。  integer对应的是原数值，float不带单位时对应的是原数值，带"vp","fp"单位时对应的是px值，具体参考示例代码。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |

**示例：**

```
1. // 资源文件路径: src/main/resources/base/element/integer.json
2. {
3. "integer": [
4. {
5. "name": "integer_test",
6. "value": 100
7. }
8. ]
9. }
```

```
1. // 资源文件路径: src/main/resources/base/element/float.json
2. {
3. "float": [
4. {
5. "name": "float_test",
6. "value": "30.6vp"
7. }
8. ]
9. }
```

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { display } from '@kit.ArkUI';

5. export default class EntryAbility extends UIAbility {
6. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
7. try {
8. // integer对应返回的是原数值
9. // 'app.integer.integer_test'仅作示例，请替换为实际使用的资源
10. let intValue = this.context.resourceManager.getNumber($r('app.integer.integer_test').id);
11. console.info(`getNumber, int value: ${intValue}`);
12. // 打印输出结果: getNumber, int value: 100
13. } catch (error) {
14. let code = (error as BusinessError).code;
15. let message = (error as BusinessError).message;
16. console.error(`getNumber failed, error code: ${code}, message: ${message}.`);
17. }

19. try {
20. // float对应返回的是真实像素点值，带"vp","fp"单位的像素值 = 原数值 * densityPixels
21. // 'app.float.float_test'仅作示例，请替换为实际使用的资源
22. let floatValue = this.context.resourceManager.getNumber($r('app.float.float_test').id);
23. console.info(`getNumber, densityPixels: ${display.getDefaultDisplaySync().densityPixels}, float value: ${floatValue}`);
24. // 打印输出结果: getNumber, densityPixels: 3.25, float value: 99.45000457763672
25. } catch (error) {
26. let code = (error as BusinessError).code;
27. let message = (error as BusinessError).message;
28. console.error(`getNumber failed, error code: ${code}, message: ${message}.`);
29. }
30. }
31. }
```

### getNumberByName9+

PhonePC/2in1TabletTVWearable

getNumberByName(resName: string): number

获取指定资源名称对应的integer数值或者float数值，使用同步方式返回。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resName | string | 是 | 资源名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 资源名称对应的数值。  integer对应的是原数值，float不带单位时对应的是原数值，带"vp","fp"单位时对应的是px值。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001003 | Invalid resource name. |
| 9001004 | No matching resource is found based on the resource name. |
| 9001006 | The resource is referenced cyclically. |

**示例：**

```
1. // 资源文件路径: src/main/resources/base/element/integer.json
2. {
3. "integer": [
4. {
5. "name": "integer_test",
6. "value": 100
7. }
8. ]
9. }
```

```
1. // 资源文件路径: src/main/resources/base/element/float.json
2. {
3. "float": [
4. {
5. "name": "float_test",
6. "value": "30.6vp"
7. }
8. ]
9. }
```

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { display } from '@kit.ArkUI';

5. export default class EntryAbility extends UIAbility {
6. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
7. try {
8. // integer对应返回的是原数值
9. // "integer_test"仅作示例，请替换为实际使用的资源
10. let intValue = this.context.resourceManager.getNumberByName("integer_test");
11. console.info(`getNumberByName, int value: ${intValue}`);
12. // 打印输出结果: getNumberByName, int value: 100
13. } catch (error) {
14. let code = (error as BusinessError).code;
15. let message = (error as BusinessError).message;
16. console.error(`getNumberByName failed, error code: ${code}, message: ${message}.`);
17. }

19. try {
20. // float对应返回的是真实像素点值，带"vp","fp"单位的像素值 = 原数值 * densityPixels
21. // "float_test"仅作示例，请替换为实际使用的资源
22. let floatValue = this.context.resourceManager.getNumberByName("float_test");
23. console.info(`getNumberByName, densityPixels: ${display.getDefaultDisplaySync().densityPixels}, float value: ${floatValue}`);
24. // 打印输出结果: getNumberByName, densityPixels: 3.25, float value: 99.45000457763672
25. } catch (error) {
26. let code = (error as BusinessError).code;
27. let message = (error as BusinessError).message;
28. console.error(`getNumberByName failed, error code: ${code}, message: ${message}.`);
29. }
30. }
31. }
```

### getColorSync10+

PhonePC/2in1TabletTVWearable

getColorSync(resId: number) : number

获取指定资源ID对应的颜色值，使用同步方式返回。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resId | number | 是 | 资源ID值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 资源ID值对应的颜色值（十进制）。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |

**示例：**

```
1. // 资源文件路径: src/main/resources/base/element/color.json
2. {
3. "color": [
4. {
5. "name": "test",
6. "value": "#FFFFFF"
7. }
8. ]
9. }
```

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. try {
7. // 'app.color.test'仅作示例，请替换为实际使用的资源
8. let colorValue = this.context.resourceManager.getColorSync($r('app.color.test').id);
9. console.info(`getColorSync, result: ${colorValue}`);
10. // 打印输出结果: getColorSync, result: 4294967295
11. } catch (error) {
12. let code = (error as BusinessError).code;
13. let message = (error as BusinessError).message;
14. console.error(`getColorSync failed, error code: ${code}, message: ${message}.`);
15. }
16. }
17. }
```

### getColorByNameSync10+

PhonePC/2in1TabletTVWearable

getColorByNameSync(resName: string) : number

获取指定资源名称对应的颜色值，使用同步方式返回。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resName | string | 是 | 资源名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 资源名称对应的颜色值（十进制）。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001003 | Invalid resource name. |
| 9001004 | No matching resource is found based on the resource name. |
| 9001006 | The resource is referenced cyclically. |

**示例：**

```
1. // 资源文件路径: src/main/resources/base/element/color.json
2. {
3. "color": [
4. {
5. "name": "test",
6. "value": "#FFFFFF"
7. }
8. ]
9. }
```

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. try {
7. // "test"仅作示例，请替换为实际使用的资源
8. let colorValue = this.context.resourceManager.getColorByNameSync("test");
9. console.info(`getColorByNameSync, result: ${colorValue}`);
10. // 打印输出结果: getColorByNameSync, result: 4294967295
11. } catch (error) {
12. let code = (error as BusinessError).code;
13. let message = (error as BusinessError).message;
14. console.error(`getColorByNameSync failed, error code: ${code}, message: ${message}.`);
15. }
16. }
17. }
```

### getColor10+

PhonePC/2in1TabletTVWearable

getColor(resId: number, callback: \_AsyncCallback<number>): void

获取指定资源ID对应的颜色值，使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resId | number | 是 | 资源ID值。 |
| callback | [\_AsyncCallback](js-apis-base.md#asynccallback)<number> | 是 | 回调函数，返回资源ID值对应的颜色值（十进制）。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |

**示例Stage：**

```
1. // 资源文件路径: src/main/resources/base/element/color.json
2. {
3. "color": [
4. {
5. "name": "test",
6. "value": "#FFFFFF"
7. }
8. ]
9. }
```

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. // 'app.color.test'仅作示例，请替换为实际使用的资源
7. this.context.resourceManager.getColor($r('app.color.test').id, (error: BusinessError, value: number) => {
8. if (error != null) {
9. console.error(`callback getColor failed, error code: ${error.code}, message: ${error.message}.`);
10. } else {
11. console.info(`getColor, result: ${value}`);
12. // 打印输出结果: getColor, result: 4294967295
13. }
14. });
15. }
16. }
```

### getColor10+

PhonePC/2in1TabletTVWearable

getColor(resId: number): Promise<number>

获取指定资源ID对应的颜色值，使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resId | number | 是 | 资源ID值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回资源ID值对应的颜色值（十进制）。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |

**示例：**

```
1. // 资源文件路径: src/main/resources/base/element/color.json
2. {
3. "color": [
4. {
5. "name": "test",
6. "value": "#FFFFFF"
7. }
8. ]
9. }
```

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. // 'app.color.test'仅作示例，请替换为实际使用的资源
7. this.context.resourceManager.getColor($r('app.color.test').id)
8. .then((value: number) => {
9. console.info(`getColor, result: ${value}`);
10. // 打印输出结果: getColor, result: 4294967295
11. })
12. .catch((error: BusinessError) => {
13. console.error(`promise getColor failed, error code: ${error.code}, message: ${error.message}.`);
14. });
15. }
16. }
```

### getColorByName10+

PhonePC/2in1TabletTVWearable

getColorByName(resName: string, callback: \_AsyncCallback<number>): void

获取指定资源名称对应的颜色值，使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resName | string | 是 | 资源名称。 |
| callback | [\_AsyncCallback](js-apis-base.md#asynccallback)<number> | 是 | 回调函数，返回资源名称对应的颜色值（十进制）。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001003 | Invalid resource name. |
| 9001004 | No matching resource is found based on the resource name. |
| 9001006 | The resource is referenced cyclically. |

**示例：**

```
1. // 资源文件路径: src/main/resources/base/element/color.json
2. {
3. "color": [
4. {
5. "name": "test",
6. "value": "#FFFFFF"
7. }
8. ]
9. }
```

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. // "test"仅作示例，请替换为实际使用的资源
7. this.context.resourceManager.getColorByName("test", (error: BusinessError, value: number) => {
8. if (error != null) {
9. console.error(`callback getColorByName failed, error code: ${error.code}, message: ${error.message}.`);
10. } else {
11. console.info(`getColorByName, result: ${value}`);
12. // 打印输出结果: getColorByName, result: 4294967295
13. }
14. });
15. }
16. }
```

### getColorByName10+

PhonePC/2in1TabletTVWearable

getColorByName(resName: string): Promise<number>

获取指定资源名称对应的颜色值，使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resName | string | 是 | 资源名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回资源名称对应的颜色值（十进制）。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001003 | Invalid resource name. |
| 9001004 | No matching resource is found based on the resource name. |
| 9001006 | The resource is referenced cyclically. |

**示例：**

```
1. // 资源文件路径: src/main/resources/base/element/color.json
2. {
3. "color": [
4. {
5. "name": "test",
6. "value": "#FFFFFF"
7. }
8. ]
9. }
```

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. // "test"仅作示例，请替换为实际使用的资源
7. this.context.resourceManager.getColorByName("test")
8. .then((value: number) => {
9. console.info(`getColorByName, result: ${value}`);
10. // 打印输出结果: getColorByName, result: 4294967295
11. })
12. .catch((error: BusinessError) => {
13. console.error(`promise getColorByName failed, error code: ${error.code}, message: ${error.message}.`);
14. });
15. }
16. }
```

### getRawFileContentSync10+

PhonePC/2in1TabletTVWearable

getRawFileContentSync(path: string): Uint8Array

获取resources/rawfile目录下对应的rawfile文件内容，使用同步形式返回。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | rawfile文件路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | 返回获取的rawfile文件内容。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001005 | Invalid relative path. |

**示例：**

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. try {
7. // "test.txt"仅作示例，请替换为实际使用的资源
8. this.context.resourceManager.getRawFileContentSync("test.txt");
9. } catch (error) {
10. let code = (error as BusinessError).code;
11. let message = (error as BusinessError).message;
12. console.error(`getRawFileContentSync failed, error code: ${code}, message: ${message}.`);
13. }
14. }
15. }
```

### getRawFileContent9+

PhonePC/2in1TabletTVWearable

getRawFileContent(path: string, callback: \_AsyncCallback<Uint8Array>): void

获取resources/rawfile目录下对应的rawfile文件内容，使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | rawfile文件路径。 |
| callback | [\_AsyncCallback](js-apis-base.md#asynccallback)<Uint8Array> | 是 | 回调函数，返回获取的rawfile文件内容。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001005 | Invalid relative path. |

**示例：**

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. try {
7. // "test.txt"仅作示例，请替换为实际使用的资源
8. this.context.resourceManager.getRawFileContent("test.txt", (error: BusinessError, value: Uint8Array) => {
9. if (error != null) {
10. console.error("error is " + error);
11. } else {
12. let rawFile = value;
13. }
14. });
15. } catch (error) {
16. let code = (error as BusinessError).code;
17. let message = (error as BusinessError).message;
18. console.error(`callback getRawFileContent failed, error code: ${code}, message: ${message}.`);
19. }
20. }
21. }
```

### getRawFileContent9+

PhonePC/2in1TabletTVWearable

getRawFileContent(path: string): Promise<Uint8Array>

获取resources/rawfile目录下对应的rawfile文件内容，使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | rawfile文件路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Uint8Array> | Promise对象，返回获取的rawfile文件内容。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001005 | Invalid relative path. |

**示例：**

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. try {
7. // "test.txt"仅作示例，请替换为实际使用的资源
8. this.context.resourceManager.getRawFileContent("test.txt").then((value: Uint8Array) => {
9. let rawFile = value;
10. }).catch((error: BusinessError) => {
11. console.error("getRawFileContent promise error is " + error);
12. });
13. } catch (error) {
14. let code = (error as BusinessError).code;
15. let message = (error as BusinessError).message;
16. console.error(`promise getRawFileContent failed, error code: ${code}, message: ${message}.`);
17. }
18. }
19. }
```

### getRawFileListSync10+

PhonePC/2in1TabletTVWearable

getRawFileListSync(path: string): Array<string>

获取resources/rawfile目录下文件夹及文件列表，使用同步形式返回。

说明

若文件夹中无文件，则抛出异常；若文件夹中有文件，则返回文件夹及文件列表。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | rawfile文件夹路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | rawfile文件目录下的文件夹及文件列表。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001005 | Invalid relative path. |

**示例：**

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. try {
7. // 传入""表示获取rawfile根目录下的文件列表，假设rawfile根目录下存在test.txt文件
8. // 传入""仅作示例，请替换为rawfile目录下实际的文件路径
9. let fileList: Array<string> = this.context.resourceManager.getRawFileListSync("");
10. console.info(`getRawFileListSync, result: ${JSON.stringify(fileList)}`);
11. // 打印输出结果: getRawFileListSync, result: ["test.txt"]
12. } catch (error) {
13. let code = (error as BusinessError).code;
14. let message = (error as BusinessError).message;
15. console.error(`getRawFileListSync failed, error code: ${code}, message: ${message}.`);
16. }
17. }
18. }
```

### getRawFileList10+

PhonePC/2in1TabletTVWearable

getRawFileList(path: string, callback: \_AsyncCallback<Array<string>>): void

获取resources/rawfile目录下文件夹及文件列表，使用callback异步回调。

说明

若文件夹中无文件，则抛出异常；若文件夹中有文件，则返回文件夹及文件列表。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | rawfile文件夹路径。 |
| callback | [\_AsyncCallback](js-apis-base.md#asynccallback)<Array<string>> | 是 | 回调函数，返回rawfile文件目录下的文件夹及文件列表。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001005 | Invalid relative path. |

**示例：**

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. // 传入""表示获取rawfile根目录下的文件列表，假设rawfile根目录下存在test.txt文件
7. // 传入""仅作示例，请替换为rawfile目录下实际的文件路径
8. this.context.resourceManager.getRawFileList("", (error: BusinessError, value: Array<string>) => {
9. if (error != null) {
10. console.error(`callback getRawFileList failed, error code: ${error.code}, message: ${error.message}.`);
11. } else {
12. console.info(`getRawFileList, result: ${JSON.stringify(value)}`);
13. // 打印输出结果: getRawFileList, result: ["test.txt"]
14. }
15. });
16. }
17. }
```

### getRawFileList10+

PhonePC/2in1TabletTVWearable

getRawFileList(path: string): Promise<Array<string>>

获取resources/rawfile目录下文件夹及文件列表，使用Promise异步回调。

说明

若文件夹中无文件，则抛出异常；若文件夹中有文件，则返回文件夹及文件列表。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | rawfile文件夹路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<string>> | Promise对象，返回rawfile文件目录下的文件夹及文件列表。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001005 | Invalid relative path. |

**示例：**

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. // 传入""表示获取rawfile根目录下的文件列表，假设rawfile根目录下存在test.txt文件
7. // 传入""仅作示例，请替换为rawfile目录下实际的文件路径
8. this.context.resourceManager.getRawFileList("")
9. .then((value: Array<string>) => {
10. console.info(`getRawFileList, result: ${JSON.stringify(value)}`);
11. // 打印输出结果: getRawFileList, result: ["test.txt"]
12. })
13. .catch((error: BusinessError) => {
14. console.error(`promise getRawFileList failed, error code: ${error.code}, message: ${error.message}.`);
15. });
16. }
17. }
```

### getRawFdSync10+

PhonePC/2in1TabletTVWearable

getRawFdSync(path: string): RawFileDescriptor

获取resources/rawfile目录下rawfile文件所在HAP的文件描述符（fd），使用同步方式返回。

说明

文件描述符（fd）使用完毕后需调用[closeRawFdSync](js-apis-resource-manager.md#closerawfdsync10)或[closeRawFd](js-apis-resource-manager.md#closerawfd9)关闭fd，避免资源泄露。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | rawfile文件路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RawFileDescriptor](js-apis-resource-manager.md#rawfiledescriptor9) | rawfile文件所在HAP的文件描述符（fd）。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001005 | Invalid relative path. |

**示例：**

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. try {
7. // "test.txt"仅作示例，请替换为实际使用的资源
8. this.context.resourceManager.getRawFdSync("test.txt");
9. } catch (error) {
10. let code = (error as BusinessError).code;
11. let message = (error as BusinessError).message;
12. console.error(`getRawFdSync failed, error code: ${code}, message: ${message}.`);
13. }
14. }
15. }
```

### getRawFd9+

PhonePC/2in1TabletTVWearable

getRawFd(path: string, callback: \_AsyncCallback<RawFileDescriptor>): void

获取resources/rawfile目录下对应rawfile文件所在HAP的文件描述符（fd），使用callback异步回调。

说明

文件描述符（fd）使用完毕后需调用[closeRawFdSync](js-apis-resource-manager.md#closerawfdsync10)或[closeRawFd](js-apis-resource-manager.md#closerawfd9)关闭fd，避免资源泄露。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | rawfile文件路径。 |
| callback | [\_AsyncCallback](js-apis-base.md#asynccallback)<[RawFileDescriptor](js-apis-resource-manager.md#rawfiledescriptor9)> | 是 | 回调函数，返回的rawfile文件所在HAP的文件描述符（fd）。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001005 | Invalid relative path. |

**示例：**

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { resourceManager } from '@kit.LocalizationKit';

5. export default class EntryAbility extends UIAbility {
6. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
7. try {
8. // "test.txt"仅作示例，请替换为实际使用的资源
9. this.context.resourceManager.getRawFd("test.txt", (error: BusinessError, value: resourceManager.RawFileDescriptor) => {
10. if (error != null) {
11. console.error(`callback getRawFd failed error code: ${error.code}, message: ${error.message}.`);
12. } else {
13. let fd = value.fd;
14. let offset = value.offset;
15. let length = value.length;
16. }
17. });
18. } catch (error) {
19. let code = (error as BusinessError).code;
20. let message = (error as BusinessError).message;
21. console.error(`callback getRawFd failed, error code: ${code}, message: ${message}.`);
22. }
23. }
24. }
```

### getRawFd9+

PhonePC/2in1TabletTVWearable

getRawFd(path: string): Promise<RawFileDescriptor>

获取resources/rawfile目录下rawfile文件所在HAP的文件描述符（fd），使用Promise异步回调。

说明

文件描述符（fd）使用完毕后需调用[closeRawFdSync](js-apis-resource-manager.md#closerawfdsync10)或[closeRawFd](js-apis-resource-manager.md#closerawfd9)关闭fd，避免资源泄露。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | rawfile文件路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[RawFileDescriptor](js-apis-resource-manager.md#rawfiledescriptor9)> | Promise对象，返回rawfile文件所在HAP的文件描述符（fd）。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001005 | Invalid relative path. |

**示例：**

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { resourceManager } from '@kit.LocalizationKit';

5. export default class EntryAbility extends UIAbility {
6. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
7. try {
8. // "test.txt"仅作示例，请替换为实际使用的资源
9. this.context.resourceManager.getRawFd("test.txt").then((value: resourceManager.RawFileDescriptor) => {
10. let fd = value.fd;
11. let offset = value.offset;
12. let length = value.length;
13. }).catch((error: BusinessError) => {
14. console.error(`promise getRawFd error error code: ${error.code}, message: ${error.message}.`);
15. });
16. } catch (error) {
17. let code = (error as BusinessError).code;
18. let message = (error as BusinessError).message;
19. console.error(`promise getRawFd failed, error code: ${code}, message: ${message}.`);
20. }
21. }
22. }
```

### closeRawFdSync10+

PhonePC/2in1TabletTVWearable

closeRawFdSync(path: string): void

关闭resources/rawfile目录下rawfile文件所在HAP的文件描述符（fd），使用同步方式返回。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | rawfile文件路径 。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001005 | Invalid relative path. |

**示例：**

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. try {
7. // "test.txt"仅作示例，请替换为实际使用的资源
8. let rawfile = this.context.resourceManager.getRawFdSync("test.txt");
9. // 根据实际业务场景，使用rawfile资源

11. this.context.resourceManager.closeRawFdSync("test.txt");
12. console.info(`closeRawFdSync test success.`);
13. } catch (error) {
14. let code = (error as BusinessError).code;
15. let message = (error as BusinessError).message;
16. console.error(`closeRawFdSync test failed, error code: ${code}, message: ${message}.`);
17. }
18. }
19. }
```

### closeRawFd9+

PhonePC/2in1TabletTVWearable

closeRawFd(path: string, callback: \_AsyncCallback<void>): void

关闭resources/rawfile目录下rawfile文件所在HAP的文件描述符（fd），使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | rawfile文件路径。 |
| callback | [\_AsyncCallback](js-apis-base.md#asynccallback)<void> | 是 | 回调函数。当关闭rawfile所在HAP的文件描述符（fd）成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001005 | Invalid relative path. |

**示例：**

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. try {
7. // "test.txt"仅作示例，请替换为实际使用的资源
8. let rawfile = this.context.resourceManager.getRawFdSync("test.txt");
9. // 根据实际业务场景，使用rawfile资源
10. this.context.resourceManager.closeRawFd("test.txt", (error: BusinessError) => {
11. if (error != null) {
12. console.error("error is " + error);
13. return;
14. }
15. console.info('closeRawFd success.');
16. });
17. } catch (error) {
18. let code = (error as BusinessError).code;
19. let message = (error as BusinessError).message;
20. console.error(`callback closeRawFd failed, error code: ${code}, message: ${message}.`);
21. }
22. }
23. }
```

### closeRawFd9+

PhonePC/2in1TabletTVWearable

closeRawFd(path: string): Promise<void>

关闭resources/rawfile目录下rawfile文件所在HAP的文件描述符（fd），使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | rawfile文件路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001005 | Invalid relative path. |

**示例：**

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. try {
7. // "test.txt"仅作示例，请替换为实际使用的资源
8. let rawfile = this.context.resourceManager.getRawFdSync("test.txt");
9. // 根据实际业务场景，使用rawfile资源
10. this.context.resourceManager.closeRawFd("test.txt");
11. console.info(`closeRawFd test success.`);
12. } catch (error) {
13. let code = (error as BusinessError).code;
14. let message = (error as BusinessError).message;
15. console.error(`promise closeRawFd failed, error code: ${code}, message: ${message}.`);
16. }
17. }
18. }
```

### getConfigurationSync10+

PhonePC/2in1TabletTVWearable

getConfigurationSync(): Configuration

获取设备的Configuration，使用同步形式返回。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Configuration](js-apis-resource-manager.md#configuration) | 设备的Configuration。 |

**示例：**

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

3. export default class EntryAbility extends UIAbility {
4. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
5. try {
6. let value = this.context.resourceManager.getConfigurationSync();
7. let direction = value.direction;
8. let locale = value.locale;
9. } catch (error) {
10. console.error("getConfigurationSync error is " + error);
11. }
12. }
13. }
```

### getConfiguration

PhonePC/2in1TabletTVWearable

getConfiguration(callback: \_AsyncCallback<Configuration>): void

获取设备的Configuration，使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [\_AsyncCallback](js-apis-base.md#asynccallback)<[Configuration](js-apis-resource-manager.md#configuration)> | 是 | 回调函数，返回设备的Configuration。 |

**示例：**

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { resourceManager } from '@kit.LocalizationKit';

5. export default class EntryAbility extends UIAbility {
6. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
7. try {
8. this.context.resourceManager.getConfiguration((error: BusinessError, value: resourceManager.Configuration) => {
9. if (error != null) {
10. console.error("getConfiguration callback error is " + error);
11. } else {
12. let direction = value.direction;
13. let locale = value.locale;
14. }
15. });
16. } catch (error) {
17. console.error("getConfiguration callback error is " + error);
18. }
19. }
20. }
```

### getConfiguration

PhonePC/2in1TabletTVWearable

getConfiguration(): Promise<Configuration>

获取设备的Configuration，使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Configuration](js-apis-resource-manager.md#configuration)> | Promise对象，返回设备的Configuration。 |

**示例：**

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { resourceManager } from '@kit.LocalizationKit';

5. export default class EntryAbility extends UIAbility {
6. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
7. try {
8. this.context.resourceManager.getConfiguration().then((value: resourceManager.Configuration) => {
9. let direction = value.direction;
10. let locale = value.locale;
11. }).catch((error: BusinessError) => {
12. console.error("getConfiguration promise error is " + error);
13. });
14. } catch (error) {
15. console.error("getConfiguration promise error is " + error);
16. }
17. }
18. }
```

### getDeviceCapabilitySync10+

PhonePC/2in1TabletTVWearable

getDeviceCapabilitySync(): DeviceCapability

获取设备的DeviceCapability，使用同步形式返回。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DeviceCapability](js-apis-resource-manager.md#devicecapability) | 设备的DeviceCapability。 |

**示例：**

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

3. export default class EntryAbility extends UIAbility {
4. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
5. try {
6. let value = this.context.resourceManager.getDeviceCapabilitySync();
7. let screenDensity = value.screenDensity;
8. let deviceType = value.deviceType;
9. } catch (error) {
10. console.error("getDeviceCapabilitySync error is " + error);
11. }
12. }
13. }
```

### getDeviceCapability

PhonePC/2in1TabletTVWearable

getDeviceCapability(callback: \_AsyncCallback<DeviceCapability>): void

获取设备的DeviceCapability，使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [\_AsyncCallback](js-apis-base.md#asynccallback)<[DeviceCapability](js-apis-resource-manager.md#devicecapability)> | 是 | 回调函数，返回设备的DeviceCapability。 |

**示例：**

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { resourceManager } from '@kit.LocalizationKit';

5. export default class EntryAbility extends UIAbility {
6. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
7. try {
8. this.context.resourceManager.getDeviceCapability((error: BusinessError, value: resourceManager.DeviceCapability) => {
9. if (error != null) {
10. console.error("getDeviceCapability callback error is " + error);
11. } else {
12. let screenDensity = value.screenDensity;
13. let deviceType = value.deviceType;
14. }
15. });
16. } catch (error) {
17. console.error("getDeviceCapability callback error is " + error);
18. }
19. }
20. }
```

### getDeviceCapability

PhonePC/2in1TabletTVWearable

getDeviceCapability(): Promise<DeviceCapability>

获取设备的DeviceCapability，使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[DeviceCapability](js-apis-resource-manager.md#devicecapability)> | Promise对象，返回设备的DeviceCapability。 |

**示例：**

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { resourceManager } from '@kit.LocalizationKit';

5. export default class EntryAbility extends UIAbility {
6. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
7. try {
8. this.context.resourceManager.getDeviceCapability().then((value: resourceManager.DeviceCapability) => {
9. let screenDensity = value.screenDensity;
10. let deviceType = value.deviceType;
11. }).catch((error: BusinessError) => {
12. console.error("getDeviceCapability promise error is " + error);
13. });
14. } catch (error) {
15. console.error("getDeviceCapability promise error is " + error);
16. }
17. }
18. }
```

### addResource10+

PhonePC/2in1TabletTVWearable

addResource(path: string): void

应用运行时加载指定的资源路径，实现资源覆盖。

说明

rawfile和resfile目录不支持资源覆盖。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 资源路径。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001010 | Invalid overlay path. |

**示例：**

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. // "/library1-default-signed.hsp"仅作示例，请替换为实际的文件路径
7. let path = this.context.bundleCodeDir + "/library1-default-signed.hsp";
8. try {
9. this.context.resourceManager.addResource(path);
10. } catch (error) {
11. let code = (error as BusinessError).code;
12. let message = (error as BusinessError).message;
13. console.error(`addResource failed, error code: ${code}, message: ${message}.`);
14. }
15. }
16. }
```

### removeResource10+

PhonePC/2in1TabletTVWearable

removeResource(path: string): void

应用运行时移除指定的资源路径，还原被覆盖前的资源。

说明

rawfile和resfile目录不支持资源覆盖。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 资源路径。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001010 | Invalid overlay path. |

**示例：**

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. // "/library1-default-signed.hsp"仅作示例，请替换为实际的文件路径
7. let path = this.context.bundleCodeDir + "/library1-default-signed.hsp";
8. try {
9. this.context.resourceManager.removeResource(path);
10. } catch (error) {
11. let code = (error as BusinessError).code;
12. let message = (error as BusinessError).message;
13. console.error(`removeResource failed, error code: ${code}, message: ${message}.`);
14. }
15. }
16. }
```

### getLocales11+

PhonePC/2in1TabletTVWearable

getLocales(includeSystem?: boolean): Array<string>

获取应用的语言列表。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| includeSystem | boolean | 否 | 是否包含系统资源，默认值为false。  - false：表示仅获取应用资源的语言列表。  - true：表示获取系统资源和应用资源的语言列表。  当使用系统资源管理对象获取语言列表时，includeSystem值无效，始终返回系统资源语言列表。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 返回获取的语言列表，列表中的字符串由语言、脚本（可选）、地区（可选），按照顺序使用中划线“-”连接组成。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |

**示例：**

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { resourceManager } from '@kit.LocalizationKit';

5. export default class EntryAbility extends UIAbility {
6. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
7. try {
8. this.context.resourceManager.getLocales(); // 仅获取应用资源语言列表
9. } catch (error) {
10. let code = (error as BusinessError).code;
11. let message = (error as BusinessError).message;
12. console.error(`getLocales failed, error code: ${code}, message: ${message}.`);
13. }

15. try {
16. resourceManager.getSysResourceManager().getLocales(); // 仅获取系统资源语言列表
17. } catch (error) {
18. let code = (error as BusinessError).code;
19. let message = (error as BusinessError).message;
20. console.error(`getLocales failed, error code: ${code}, message: ${message}.`);
21. }

23. try {
24. this.context.resourceManager.getLocales(true); // 获取应用资源和系统资源语言列表
25. } catch (error) {
26. let code = (error as BusinessError).code;
27. let message = (error as BusinessError).message;
28. console.error(`getLocales failed, error code: ${code}, message: ${message}.`);
29. }
30. }
31. }
```

### getSymbol11+

PhonePC/2in1TabletTVWearable

getSymbol(resId: number): number

获取指定资源ID对应的[Symbol字符](https://developer.huawei.com/consumer/cn/design/harmonyos-symbol)Unicode码，使用同步方式返回。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resId | number | 是 | 资源ID值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 资源ID值对应的Symbol字符Unicode码（十进制）。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |

**示例：**

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. try {
7. // 'sys.symbol.message'仅作示例，请替换为实际使用的资源
8. let symbolValue = this.context.resourceManager.getSymbol($r('sys.symbol.message').id);
9. console.info(`getSymbol, result: ${symbolValue}`);
10. // 打印输出结果: getSymbol, result: 983183
11. } catch (error) {
12. let code = (error as BusinessError).code;
13. let message = (error as BusinessError).message;
14. console.error(`getSymbol failed, error code: ${code}, message: ${message}.`);
15. }
16. }
17. }
```

### getSymbolByName11+

PhonePC/2in1TabletTVWearable

getSymbolByName(resName: string): number

获取指定资源名称对应的[Symbol字符](https://developer.huawei.com/consumer/cn/design/harmonyos-symbol)Unicode码，使用同步方式返回。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resName | string | 是 | 资源名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 资源名称对应的Symbol字符Unicode码（十进制）。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001003 | Invalid resource name. |
| 9001004 | No matching resource is found based on the resource name. |
| 9001006 | The resource is referenced cyclically. |

**示例：**

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. try {
7. // "message"仅作示例，请替换为实际使用的资源
8. let symbolValue = this.context.resourceManager.getSymbolByName("message");
9. console.info(`getSymbolByName, result: ${symbolValue}`);
10. // 打印输出结果: getSymbolByName, result: 983183
11. } catch (error) {
12. let code = (error as BusinessError).code;
13. let message = (error as BusinessError).message;
14. console.error(`getSymbolByName failed, error code: ${code}, message: ${message}.`);
15. }
16. }
17. }
```

### isRawDir12+

PhonePC/2in1TabletTVWearable

isRawDir(path: string): boolean

判断指定路径是否为rawfile下的目录，使用同步方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | rawfile路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否为rawfile下的目录。  - true：表示是rawfile下的目录。  - false：表示非rawfile下的目录。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001005 | Invalid relative path. |

**示例：**

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. try {
7. // 假设rawfile根目录下存在非空文件夹sub，则isRawDir返回结果为true
8. // "sub"仅作示例，请替换为实际使用的目录名称
9. let isRawDir = this.context.resourceManager.isRawDir("sub");
10. // 打印输出结果: sub isRawDir, result: true
11. console.info(`sub isRawDir, result: ${isRawDir}`);

13. // 假设rawfile根目录下存在test.txt文件，则isRawDir返回结果为false
14. // "test.txt"仅作示例，请替换为实际使用的资源
15. isRawDir = this.context.resourceManager.isRawDir("test.txt");
16. // 打印输出结果: test.txt isRawDir, result: false
17. console.info(`test.txt isRawDir, result: ${isRawDir}`);
18. } catch (error) {
19. let code = (error as BusinessError).code;
20. let message = (error as BusinessError).message;
21. console.error(`isRawDir failed, error code: ${code}, message: ${message}.`);
22. }
23. }
24. }
```

### getOverrideResourceManager12+

PhonePC/2in1TabletTVWearable

getOverrideResourceManager(configuration?: Configuration): ResourceManager

获取可以加载差异化资源的资源管理对象，使用同步方式返回。

普通的资源管理对象获取的资源的配置（语言、深浅色、分辨率、横竖屏等）是由系统决定的，而通过该接口返回的对象，应用可以获取符合指定配置的资源，即差异化资源，比如在浅色模式时可以获取深色资源。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| configuration | [Configuration](js-apis-resource-manager.md#configuration) | 否 | 指定想要获取的资源配置。  通过[getOverrideConfiguration](js-apis-resource-manager.md#getoverrideconfiguration12)获取差异化配置后，根据需求修改配置项，再作为参数传入该函数。  若缺省则表示使用当前系统的configuration。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ResourceManager | 可以加载差异化资源的资源管理对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |

**示例：**

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { resourceManager } from '@kit.LocalizationKit';

5. export default class EntryAbility extends UIAbility {
6. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
7. try {
8. let resMgr = this.context.resourceManager;
9. let overrideConfig = resMgr.getOverrideConfiguration();
10. overrideConfig.colorMode = resourceManager.ColorMode.DARK;
11. let overrideResMgr = resMgr.getOverrideResourceManager(overrideConfig);
12. } catch (error) {
13. let code = (error as BusinessError).code;
14. let message = (error as BusinessError).message;
15. console.error(`getOverrideResourceManager failed, error code: ${code}, message: ${message}.`);
16. }
17. }
18. }
```

### getOverrideConfiguration12+

PhonePC/2in1TabletTVWearable

getOverrideConfiguration(): Configuration

获取差异化资源的配置，使用同步方式返回。普通资源管理对象与通过它的[getOverrideResourceManager](js-apis-resource-manager.md#getoverrideresourcemanager12)接口获取的差异化资源管理对象调用该方法可获得相同的返回值。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Configuration](js-apis-resource-manager.md#configuration) | 差异化资源的配置。 |

**示例：**

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { resourceManager } from '@kit.LocalizationKit';

5. export default class EntryAbility extends UIAbility {
6. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
7. try {
8. let resMgr = this.context.resourceManager;
9. let overrideConfig = resMgr.getOverrideConfiguration();
10. overrideConfig.colorMode = resourceManager.ColorMode.DARK;
11. let overrideResMgr = resMgr.getOverrideResourceManager(overrideConfig);
12. } catch (error) {
13. let code = (error as BusinessError).code;
14. let message = (error as BusinessError).message;
15. console.error(`getOverrideResourceManager failed, error code: ${code}, message: ${message}.`);
16. }
17. }
18. }
```

### updateOverrideConfiguration12+

PhonePC/2in1TabletTVWearable

updateOverrideConfiguration(configuration: Configuration): void

更新差异化资源配置。普通资源管理对象与通过它的[getOverrideResourceManager](js-apis-resource-manager.md#getoverrideresourcemanager12)接口获取的差异化资源管理对象调用该方法均可更新差异化资源管理对象的配置。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| configuration | [Configuration](js-apis-resource-manager.md#configuration) | 是 | 指定差异化资源的配置。通过[getOverrideConfiguration](js-apis-resource-manager.md#getoverrideconfiguration12)获取差异化配置后，根据需求修改配置项，再作为参数传入。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |

**示例：**

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { resourceManager } from '@kit.LocalizationKit';

5. export default class EntryAbility extends UIAbility {
6. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
7. try {
8. let resMgr = this.context.resourceManager;
9. let overrideConfig = resMgr.getOverrideConfiguration();
10. overrideConfig.colorMode = resourceManager.ColorMode.DARK;
11. let overrideResMgr = resMgr.updateOverrideConfiguration(overrideConfig);
12. } catch (error) {
13. let code = (error as BusinessError).code;
14. let message = (error as BusinessError).message;
15. console.error(`updateOverrideConfiguration failed, error code: ${code}, message: ${message}.`);
16. }
17. }
18. }
```

### release(deprecated)

PhonePC/2in1TabletTVWearable

release()

释放创建的resourceManager, 此接口暂不支持。

说明

从API version 7开始支持，从API version 12开始废弃。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**示例：**

```
1. try {
2. this.context.resourceManager.release();
3. } catch (error) {
4. console.error("release error is " + error);
5. }
```

### getString(deprecated)

PhonePC/2in1TabletTVWearable

getString(resId: number, callback: AsyncCallback<string>): void

获取指定资源ID对应的字符串，使用callback异步回调。

说明

从API version 6开始支持，从API version 9开始废弃，建议使用[getStringValue](js-apis-resource-manager.md#getstringvalue9)替代。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resId | number | 是 | 资源ID值。 |
| callback | [AsyncCallback](js-apis-resource-manager.md#asynccallbackdeprecated)<string> | 是 | 回调函数，返回资源ID值对应的字符串。 |

**示例：**

```
1. resourceManager.getResourceManager((error, mgr) => {
2. mgr.getString($r('app.string.test').id, (error: Error, value: string) => {
3. if (error != null) {
4. console.error("error is " + error);
5. } else {
6. let str = value;
7. }
8. });
9. });
```

### getString(deprecated)

PhonePC/2in1TabletTVWearable

getString(resId: number): Promise<string>

获取指定资源ID对应的字符串，使用Promise异步回调。

说明

从API version 6开始支持，从API version 9开始废弃，建议使用[getStringValue](js-apis-resource-manager.md#getstringvalue9-1)替代。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resId | number | 是 | 资源ID值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回资源ID值对应的字符串。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. resourceManager.getResourceManager((error, mgr) => {
4. mgr.getString($r('app.string.test').id).then((value: string) => {
5. let str = value;
6. }).catch((error: BusinessError) => {
7. console.error("getstring promise error is " + error);
8. });
9. });
```

### getStringSync(deprecated)

PhonePC/2in1TabletTVWearable

getStringSync(resource: Resource): string

获取指定resource对象对应的字符串，使用同步方式返回。

说明

从API version 9开始支持，从API version 20开始废弃，建议使用[getStringByNameSync](js-apis-resource-manager.md#getstringbynamesync9)或[getStringSync](js-apis-resource-manager.md#getstringsync9)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resource | [Resource](js-apis-resource-manager.md#resource9) | 是 | 资源信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | resource对象对应的字符串。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |

**示例：**

```
1. // 资源文件路径: src/main/resources/base/element/string.json
2. {
3. "string": [
4. {
5. "name": "test",
6. "value": "I'm a test string resource."
7. }
8. ]
9. }
```

```
1. import { resourceManager } from '@kit.LocalizationKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let resource: resourceManager.Resource = {
5. bundleName: "com.example.myapplication",
6. moduleName: "entry",
7. id: $r('app.string.test').id
8. };
9. try {
10. let testStr = this.context.resourceManager.getStringSync(resource);
11. console.info(`getStringSync, result: ${testStr}`);
12. // 打印输出结果: getStringSync, result: I'm a test string resource.
13. } catch (error) {
14. let code = (error as BusinessError).code;
15. let message = (error as BusinessError).message;
16. console.error(`getStringSync failed, error code: ${code}, message: ${message}.`);
17. }
```

### getStringSync(deprecated)

PhonePC/2in1TabletTVWearable

getStringSync(resource: Resource, ...args: Array<string | number>): string

获取指定resource对象对应的字符串，并根据args参数对字符串进行格式化，使用同步方式返回。

说明

从API version 10开始支持，从API version 20开始废弃，建议使用[getStringByNameSync](js-apis-resource-manager.md#getstringbynamesync10)或[getStringSync](js-apis-resource-manager.md#getstringsync10)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resource | [Resource](js-apis-resource-manager.md#resource9) | 是 | 资源信息。 |
| ...args | Array<string | number> | 否 | 格式化字符串资源参数。  支持参数类型：%d、%f、%s、%%、%数字$d、%数字$f、%数字$s。  说明：%%转义为%; %数字$d中的数字表示使用args中的第几个参数。  举例：%%d格式化后为%d字符串; %1$d表示使用第一个参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | resource对象对应的格式化字符串。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |
| 9001007 | Failed to format the resource obtained based on the resource ID. |

**示例：**

```
1. // 资源文件路径: src/main/resources/base/element/string.json
2. {
3. "string": [
4. {
5. "name": "test",
6. "value": "I'm a %1$s, format int: %2$d, format float: %3$f."
7. }
8. ]
9. }
```

```
1. import { resourceManager } from '@kit.LocalizationKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let resource: resourceManager.Resource = {
5. bundleName: "com.example.myapplication",
6. moduleName: "entry",
7. id: $r('app.string.test').id
8. };
9. try {
10. let testStr = this.context.resourceManager.getStringSync(resource, "format string", 10, 98.78);
11. console.info(`getStringSync, result: ${testStr}`);
12. // 打印输出结果: getStringSync, result: I'm a format string, format int: 10, format float: 98.78.
13. } catch (error) {
14. let code = (error as BusinessError).code;
15. let message = (error as BusinessError).message;
16. console.error(`getStringSync failed, error code: ${code}, message: ${message}.`);
17. }
```

### getStringValue(deprecated)

PhonePC/2in1TabletTVWearable

getStringValue(resource: Resource, callback: \_AsyncCallback<string>): void

获取指定resource对象对应的字符串，使用callback异步回调。

说明

从API version 9开始支持，从API version 20开始废弃，建议使用[getStringByName](js-apis-resource-manager.md#getstringbyname9)或[getStringValue](js-apis-resource-manager.md#getstringvalue9)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resource | [Resource](js-apis-resource-manager.md#resource9) | 是 | 资源信息。 |
| callback | [\_AsyncCallback](js-apis-base.md#asynccallback)<string> | 是 | 回调函数，返回resource对象对应的字符串。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |

**示例：**

```
1. // 资源文件路径: src/main/resources/base/element/string.json
2. {
3. "string": [
4. {
5. "name": "test",
6. "value": "I'm a test string resource."
7. }
8. ]
9. }
```

```
1. import { resourceManager } from '@kit.LocalizationKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let resource: resourceManager.Resource = {
5. bundleName: "com.example.myapplication",
6. moduleName: "entry",
7. id: $r('app.string.test').id
8. };
9. this.context.resourceManager.getStringValue(resource, (error: BusinessError, value: string) => {
10. if (error != null) {
11. console.error(`callback getStringValue failed, error code: ${error.code}, message: ${error.message}.`);
12. } else {
13. console.info(`getStringValue, result: ${value}`);
14. // 打印输出结果: getStringValue, result: I'm a test string resource.
15. }
16. });
```

### getStringValue(deprecated)

PhonePC/2in1TabletTVWearable

getStringValue(resource: Resource): Promise<string>

获取指定resource对象对应的字符串，使用Promise异步回调。

说明

从API version 9开始支持，从API version 20开始废弃，建议使用[getStringByName](js-apis-resource-manager.md#getstringbyname9-1)或[getStringValue](js-apis-resource-manager.md#getstringvalue9-1)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resource | [Resource](js-apis-resource-manager.md#resource9) | 是 | 资源信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回resource对象对应的字符串。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |

**示例：**

```
1. import { resourceManager } from '@kit.LocalizationKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let resource: resourceManager.Resource = {
5. bundleName: "com.example.myapplication",
6. moduleName: "entry",
7. id: $r('app.string.test').id
8. };
9. this.context.resourceManager.getStringValue(resource, (error: BusinessError, value: string) => {
10. if (error != null) {
11. console.error(`callback getStringValue failed, error code: ${error.code}, message: ${error.message}.`);
12. } else {
13. console.info(`getStringValue, result: ${value}`);
14. // 打印输出结果: getStringValue, result: I'm a test string resource.
15. }
16. });
```

### getStringArray(deprecated)

PhonePC/2in1TabletTVWearable

getStringArray(resId: number, callback: AsyncCallback<Array<string>>): void

获取指定资源ID对应的字符串数组，使用callback异步回调。

说明

从API version 6开始支持，从API version 9开始废弃，建议使用[getStringArrayValue](js-apis-resource-manager.md#getstringarrayvalue9)替代。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resId | number | 是 | 资源ID值。 |
| callback | [AsyncCallback](js-apis-resource-manager.md#asynccallbackdeprecated)<Array<string>> | 是 | 回调函数，返回资源ID值对应的字符串数组。 |

**示例：**

```
1. resourceManager.getResourceManager((error, mgr) => {
2. mgr.getStringArray($r('app.strarray.test').id, (error: Error, value: Array<string>) => {
3. if (error != null) {
4. console.error("error is " + error);
5. } else {
6. let strArray = value;
7. }
8. });
9. });
```

### getStringArray(deprecated)

PhonePC/2in1TabletTVWearable

getStringArray(resId: number): Promise<Array<string>>

获取指定资源ID对应的字符串数组，使用Promise异步回调。

说明

从API version 6开始支持，从API version 9开始废弃，建议使用[getStringArrayValue](js-apis-resource-manager.md#getstringarrayvalue9-1)替代。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resId | number | 是 | 资源ID值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<string>> | Promise对象，返回资源ID值对应的字符串数组。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. resourceManager.getResourceManager((error, mgr) => {
4. mgr.getStringArray($r('app.strarray.test').id).then((value: Array<string>) => {
5. let strArray = value;
6. }).catch((error: BusinessError) => {
7. console.error("getStringArray promise error is " + error);
8. });
9. });
```

### getStringArrayValueSync(deprecated)

PhonePC/2in1TabletTVWearable

getStringArrayValueSync(resource: Resource): Array<string>

获取指定resource对象对应的字符串数组，使用同步方式返回。

说明

从API version 10开始支持，从API version 20开始废弃，建议使用[getStringArrayByNameSync](js-apis-resource-manager.md#getstringarraybynamesync10)或[getStringArrayValueSync](js-apis-resource-manager.md#getstringarrayvaluesync10)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resource | [Resource](js-apis-resource-manager.md#resource9) | 是 | 资源信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | resource对象对应的字符串数组。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |

**示例：**

```
1. // 资源文件路径: src/main/resources/base/element/strarray.json
2. {
3. "strarray": [
4. {
5. "name": "test",
6. "value": [
7. {
8. "value": "I'm one of the array's values."
9. }
10. ]
11. }
12. ]
13. }
```

```
1. import { resourceManager } from '@kit.LocalizationKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let resource: resourceManager.Resource = {
5. bundleName: "com.example.myapplication",
6. moduleName: "entry",
7. id: $r('app.strarray.test').id
8. };
9. try {
10. let strArray: Array<string> = this.context.resourceManager.getStringArrayValueSync(resource);
11. console.info(`getStringArrayValueSync, result: ${strArray[0]}`);
12. // 打印输出结果: getStringArrayValueSync, result: I'm one of the array's values.
13. } catch (error) {
14. let code = (error as BusinessError).code;
15. let message = (error as BusinessError).message;
16. console.error(`getStringArrayValueSync failed, error code: ${code}, message: ${message}.`);
17. }
```

### getStringArrayValue(deprecated)

PhonePC/2in1TabletTVWearable

getStringArrayValue(resource: Resource, callback: \_AsyncCallback<Array<string>>): void

获取指定resource对象对应的字符串数组，使用callback异步回调。

说明

从API version 9开始支持，从API version 20开始废弃，建议使用[getStringArrayByName](js-apis-resource-manager.md#getstringarraybyname9)或[getStringArrayValue](js-apis-resource-manager.md#getstringarrayvalue9)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resource | [Resource](js-apis-resource-manager.md#resource9) | 是 | 资源信息。 |
| callback | [\_AsyncCallback](js-apis-base.md#asynccallback)<Array<string>> | 是 | 回调函数，返回resource对象对应的字符串数组。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |

**示例：**

```
1. // 资源文件路径: src/main/resources/base/element/strarray.json
2. {
3. "strarray": [
4. {
5. "name": "test",
6. "value": [
7. {
8. "value": "I'm one of the array's values."
9. }
10. ]
11. }
12. ]
13. }
```

```
1. import { resourceManager } from '@kit.LocalizationKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let resource: resourceManager.Resource = {
5. bundleName: "com.example.myapplication",
6. moduleName: "entry",
7. id: $r('app.strarray.test').id
8. };
9. this.context.resourceManager.getStringArrayValue(resource, (error: BusinessError, value: Array<string>) => {
10. if (error != null) {
11. console.error(`callback getStringArrayValue failed, error code: ${error.code}, message: ${error.message}.`);
12. } else {
13. console.info(`getStringArrayValue, result: ${value[0]}`);
14. // 打印输出结果: getStringArrayValue, result: I'm one of the array's values.
15. }
16. });
```

### getStringArrayValue(deprecated)

PhonePC/2in1TabletTVWearable

getStringArrayValue(resource: Resource): Promise<Array<string>>

获取指定resource对象对应的字符串数组，使用Promise异步回调。

说明

从API version 9开始支持，从API version 20开始废弃，建议使用[getStringArrayByName](js-apis-resource-manager.md#getstringarraybyname9-1)或[getStringArrayValue](js-apis-resource-manager.md#getstringarrayvalue9-1)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resource | [Resource](js-apis-resource-manager.md#resource9) | 是 | 资源信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<string>> | Promise对象，返回resource对象对应的字符串数组。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |

**示例：**

```
1. // 资源文件路径: src/main/resources/base/element/strarray.json
2. {
3. "strarray": [
4. {
5. "name": "test",
6. "value": [
7. {
8. "value": "I'm one of the array's values."
9. }
10. ]
11. }
12. ]
13. }
```

```
1. import { resourceManager } from '@kit.LocalizationKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let resource: resourceManager.Resource = {
5. bundleName: "com.example.myapplication",
6. moduleName: "entry",
7. id: $r('app.strarray.test').id
8. };
9. this.context.resourceManager.getStringArrayValue(resource)
10. .then((value: Array<string>) => {
11. console.info(`getStringArrayValue, result: ${value[0]}`);
12. // 打印输出结果: getStringArrayValue, result: I'm one of the array's values.
13. })
14. .catch((error: BusinessError) => {
15. console.error(`promise getStringArrayValue failed, error code: ${error.code}, message: ${error.message}.`);
16. });
```

### getMedia(deprecated)

PhonePC/2in1TabletTVWearable

getMedia(resId: number, callback: AsyncCallback<Uint8Array>): void

获取指定资源ID对应的媒体文件内容，使用callback异步回调。

说明

从API version 6开始支持，从API version 9开始废弃，建议使用[getMediaContent](js-apis-resource-manager.md#getmediacontent9)替代。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resId | number | 是 | 资源ID值。 |
| callback | [AsyncCallback](js-apis-resource-manager.md#asynccallbackdeprecated)<Uint8Array> | 是 | 回调函数，返回资源ID值对应的媒体文件内容。 |

**示例：**

```
1. resourceManager.getResourceManager((error, mgr) => {
2. mgr.getMedia($r('app.media.test').id, (error: Error, value: Uint8Array) => {
3. if (error != null) {
4. console.error("error is " + error);
5. } else {
6. let media = value;
7. }
8. });
9. });
```

### getMedia(deprecated)

PhonePC/2in1TabletTVWearable

getMedia(resId: number): Promise<Uint8Array>

获取指定资源ID对应的媒体文件内容，使用Promise异步回调。

说明

从API version 6开始支持，从API version 9开始废弃，建议使用[getMediaContent](js-apis-resource-manager.md#getmediacontent9-1)替代。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resId | number | 是 | 资源ID值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Uint8Array> | Promise对象，返回资源ID值对应的媒体文件内容。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. resourceManager.getResourceManager((error, mgr) => {
4. mgr.getMedia($r('app.media.test').id).then((value: Uint8Array) => {
5. let media = value;
6. }).catch((error: BusinessError) => {
7. console.error("getMedia promise error is " + error);
8. });
9. });
```

### getMediaContentSync(deprecated)

PhonePC/2in1TabletTVWearable

getMediaContentSync(resource: Resource, density?: number): Uint8Array

获取指定resource对象对应的默认或指定的屏幕密度媒体文件内容，使用同步方式返回。

说明

从API version 10开始支持，从API version 20开始废弃，建议使用[getMediaByNameSync](js-apis-resource-manager.md#getmediabynamesync10)或[getMediaContentSync](js-apis-resource-manager.md#getmediacontentsync10)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resource | [Resource](js-apis-resource-manager.md#resource9) | 是 | 资源信息。 |
| [density](js-apis-resource-manager.md#screendensity) | number | 否 | 资源获取需要的屏幕密度，0或缺省表示默认屏幕密度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | resource对象对应的媒体文件内容。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |

**示例：**

```
1. import { resourceManager } from '@kit.LocalizationKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let resource: resourceManager.Resource = {
5. bundleName: "com.example.myapplication",
6. moduleName: "entry",
7. id: $r('app.media.test').id
8. };
9. try {
10. this.context.resourceManager.getMediaContentSync(resource); // 默认屏幕密度
11. } catch (error) {
12. let code = (error as BusinessError).code;
13. let message = (error as BusinessError).message;
14. console.error(`getMediaContentSync failed, error code: ${code}, message: ${message}.`);
15. }

17. try {
18. this.context.resourceManager.getMediaContentSync(resource, 120); // 指定屏幕密度
19. } catch (error) {
20. let code = (error as BusinessError).code;
21. let message = (error as BusinessError).message;
22. console.error(`getMediaContentSync failed, error code: ${code}, message: ${message}.`);
23. }
```

### getMediaContent(deprecated)

PhonePC/2in1TabletTVWearable

getMediaContent(resource: Resource, callback: \_AsyncCallback<Uint8Array>): void

获取指定resource对象对应的媒体文件内容，使用callback异步回调。

说明

从API version 9开始支持，从API version 20开始废弃，建议使用[getMediaByName](js-apis-resource-manager.md#getmediabyname9)或[getMediaContent](js-apis-resource-manager.md#getmediacontent9)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resource | [Resource](js-apis-resource-manager.md#resource9) | 是 | 资源信息。 |
| callback | [\_AsyncCallback](js-apis-base.md#asynccallback)<Uint8Array> | 是 | 回调函数，返回resource对象对应的媒体文件内容。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |

**示例：**

```
1. import { resourceManager } from '@kit.LocalizationKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let resource: resourceManager.Resource = {
5. bundleName: "com.example.myapplication",
6. moduleName: "entry",
7. id: $r('app.media.test').id
8. };
9. try {
10. this.context.resourceManager.getMediaContent(resource, (error: BusinessError, value: Uint8Array) => {
11. if (error != null) {
12. console.error("error is " + error);
13. } else {
14. let media = value;
15. }
16. });
17. } catch (error) {
18. let code = (error as BusinessError).code;
19. let message = (error as BusinessError).message;
20. console.error(`callback getMediaContent failed, error code: ${code}, message: ${message}.`);
21. }
```

### getMediaContent(deprecated)

PhonePC/2in1TabletTVWearable

getMediaContent(resource: Resource, density: number, callback: \_AsyncCallback<Uint8Array>): void

获取指定resource对象对应的指定屏幕密度媒体文件内容，使用callback异步回调。

说明

从API version 10开始支持，从API version 20开始废弃，建议使用[getMediaByName](js-apis-resource-manager.md#getmediabyname10)或[getMediaContent](js-apis-resource-manager.md#getmediacontent10)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resource | [Resource](js-apis-resource-manager.md#resource9) | 是 | 资源信息。 |
| [density](js-apis-resource-manager.md#screendensity) | number | 是 | 资源获取需要的屏幕密度，0表示默认屏幕密度。 |
| callback | [\_AsyncCallback](js-apis-base.md#asynccallback)<Uint8Array> | 是 | 回调函数，返回resource对象对应的媒体文件内容。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |

**示例：**

```
1. import { resourceManager } from '@kit.LocalizationKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let resource: resourceManager.Resource = {
5. bundleName: "com.example.myapplication",
6. moduleName: "entry",
7. id: $r('app.media.test').id
8. };
9. try {
10. this.context.resourceManager.getMediaContent(resource, 120, (error: BusinessError, value: Uint8Array) => {
11. if (error != null) {
12. console.error(`callback getMediaContent failed, error code: ${error.code}, message: ${error.message}.`);
13. } else {
14. let media = value;
15. }
16. });
17. } catch (error) {
18. let code = (error as BusinessError).code;
19. let message = (error as BusinessError).message;
20. console.error(`callback getMediaContent failed, error code: ${code}, message: ${message}.`);
21. }
```

### getMediaContent(deprecated)

PhonePC/2in1TabletTVWearable

getMediaContent(resource: Resource): Promise<Uint8Array>

获取指定resource对象对应的媒体文件内容，使用Promise异步回调。

说明

从API version 9开始支持，从API version 20开始废弃，建议使用[getMediaByName](js-apis-resource-manager.md#getmediabyname9-1)或[getMediaContent](js-apis-resource-manager.md#getmediacontent9-1)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resource | [Resource](js-apis-resource-manager.md#resource9) | 是 | 资源信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Uint8Array> | Promise对象，返回resource对象对应的媒体文件内容。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |

**示例：**

```
1. import { resourceManager } from '@kit.LocalizationKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let resource: resourceManager.Resource = {
5. bundleName: "com.example.myapplication",
6. moduleName: "entry",
7. id: $r('app.media.test').id
8. };
9. try {
10. this.context.resourceManager.getMediaContent(resource).then((value: Uint8Array) => {
11. let media = value;
12. }).catch((error: BusinessError) => {
13. console.error("getMediaContent promise error is " + error);
14. });
15. } catch (error) {
16. let code = (error as BusinessError).code;
17. let message = (error as BusinessError).message;
18. console.error(`promise getMediaContent failed, error code: ${code}, message: ${message}.`);
19. }
```

### getMediaContent(deprecated)

PhonePC/2in1TabletTVWearable

getMediaContent(resource: Resource, density: number): Promise<Uint8Array>

获取指定resource对象对应的指定屏幕密度媒体文件内容，使用Promise异步回调。

说明

从API version 10开始支持，从API version 20开始废弃，建议使用[getMediaByName](js-apis-resource-manager.md#getmediabyname10-1)或[getMediaContent](js-apis-resource-manager.md#getmediacontent10-1)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resource | [Resource](js-apis-resource-manager.md#resource9) | 是 | 资源信息。 |
| [density](js-apis-resource-manager.md#screendensity) | number | 是 | 资源获取需要的屏幕密度，0表示默认屏幕密度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Uint8Array> | Promise对象，返回resource对象对应的媒体文件内容。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |

**示例：**

```
1. import { resourceManager } from '@kit.LocalizationKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let resource: resourceManager.Resource = {
5. bundleName: "com.example.myapplication",
6. moduleName: "entry",
7. id: $r('app.media.test').id
8. };
9. try {
10. this.context.resourceManager.getMediaContent(resource, 120).then((value: Uint8Array) => {
11. let media = value;
12. }).catch((error: BusinessError) => {
13. console.error(`promise getMediaContent failed, error code: ${error.code}, message: ${error.message}.`);
14. });
15. } catch (error) {
16. let code = (error as BusinessError).code;
17. let message = (error as BusinessError).message;
18. console.error(`promise getMediaContent failed, error code: ${code}, message: ${message}.`);
19. }
```

### getMediaBase64(deprecated)

PhonePC/2in1TabletTVWearable

getMediaBase64(resId: number, callback: AsyncCallback<string>): void

获取指定资源ID对应的图片资源Base64编码，使用callback异步回调。

说明

从API version 6开始支持，从API version 9开始废弃，建议使用[getMediaContentBase64](js-apis-resource-manager.md#getmediacontentbase649)替代。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resId | number | 是 | 资源ID值。 |
| callback | [AsyncCallback](js-apis-resource-manager.md#asynccallbackdeprecated)<string> | 是 | 回调函数，返回资源ID值对应的图片资源Base64编码。 |

**示例：**

```
1. resourceManager.getResourceManager((error, mgr) => {
2. mgr.getMediaBase64($r('app.media.test').id, ((error: Error, value: string) => {
3. if (error != null) {
4. console.error("error is " + error);
5. } else {
6. let media = value;
7. }
8. });
9. });
```

### getMediaBase64(deprecated)

PhonePC/2in1TabletTVWearable

getMediaBase64(resId: number): Promise<string>

获取指定资源ID对应的图片资源Base64编码，使用Promise异步回调。

说明

从API version 6开始支持，从API version 9开始废弃，建议使用[getMediaContentBase64](js-apis-resource-manager.md#getmediacontentbase649-1)替代。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resId | number | 是 | 资源ID值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回资源ID值对应的图片资源Base64编码。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. resourceManager.getResourceManager((error, mgr) => {
4. mgr.getMediaBase64($r('app.media.test').id).then((value: string) => {
5. let media = value;
6. }).catch((error: BusinessError) => {
7. console.error("getMediaBase64 promise error is " + error);
8. });
9. });
```

### getMediaContentBase64Sync(deprecated)

PhonePC/2in1TabletTVWearable

getMediaContentBase64Sync(resource: Resource, density?: number): string

获取指定resource对象对应的默认或指定的屏幕密度图片资源Base64编码，使用同步方式返回。

说明

从API version 10开始支持，从API version 20开始废弃，建议使用[getMediaBase64ByNameSync](js-apis-resource-manager.md#getmediabase64bynamesync10)或[getMediaContentBase64Sync](js-apis-resource-manager.md#getmediacontentbase64sync10)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resource | [Resource](js-apis-resource-manager.md#resource9) | 是 | 资源信息。 |
| [density](js-apis-resource-manager.md#screendensity) | number | 否 | 资源获取需要的屏幕密度，0或缺省表示默认屏幕密度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | resource对象对应的图片资源Base64编码。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |

**示例：**

```
1. import { resourceManager } from '@kit.LocalizationKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let resource: resourceManager.Resource = {
5. bundleName: "com.example.myapplication",
6. moduleName: "entry",
7. id: $r('app.media.test').id
8. };
9. try {
10. this.context.resourceManager.getMediaContentBase64Sync(resource); // 默认屏幕密度
11. } catch (error) {
12. let code = (error as BusinessError).code;
13. let message = (error as BusinessError).message;
14. console.error(`getMediaContentBase64Sync failed, error code: ${code}, message: ${message}.`);
15. }

17. try {
18. this.context.resourceManager.getMediaContentBase64Sync(resource, 120); // 指定屏幕密度
19. } catch (error) {
20. let code = (error as BusinessError).code;
21. let message = (error as BusinessError).message;
22. console.error(`getMediaContentBase64Sync failed, error code: ${code}, message: ${message}.`);
23. }
```

### getMediaContentBase64(deprecated)

PhonePC/2in1TabletTVWearable

getMediaContentBase64(resource: Resource, callback: \_AsyncCallback<string>): void

获取指定resource对象对应的图片资源Base64编码，使用callback异步回调。

说明

从API version 9开始支持，从API version 20开始废弃，建议使用[getMediaBase64ByName](js-apis-resource-manager.md#getmediabase64byname9)或[getMediaContentBase64](js-apis-resource-manager.md#getmediacontentbase649)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resource | [Resource](js-apis-resource-manager.md#resource9) | 是 | 资源信息。 |
| callback | [\_AsyncCallback](js-apis-base.md#asynccallback)<string> | 是 | 回调函数，返回resource对象对应的图片资源Base64编码。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |

**示例：**

```
1. import { resourceManager } from '@kit.LocalizationKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let resource: resourceManager.Resource = {
5. bundleName: "com.example.myapplication",
6. moduleName: "entry",
7. id: $r('app.media.test').id
8. };
9. try {
10. this.context.resourceManager.getMediaContentBase64(resource, (error: BusinessError, value: string) => {
11. if (error != null) {
12. console.error("error is " + error);
13. } else {
14. let media = value;
15. }
16. });
17. } catch (error) {
18. let code = (error as BusinessError).code;
19. let message = (error as BusinessError).message;
20. console.error(`callback getMediaContentBase64 failed, error code: ${code}, message: ${message}.`);
21. }
```

### getMediaContentBase64(deprecated)

PhonePC/2in1TabletTVWearable

getMediaContentBase64(resource: Resource, density: number, callback: \_AsyncCallback<string>): void

获取指定resource对象对应的指定屏幕密度图片资源Base64编码，使用callback异步回调。

说明

从API version 10开始支持，从API version 20开始废弃，建议使用[getMediaBase64ByName](js-apis-resource-manager.md#getmediabase64byname10)或[getMediaContentBase64](js-apis-resource-manager.md#getmediacontentbase6410)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resource | [Resource](js-apis-resource-manager.md#resource9) | 是 | 资源信息。 |
| [density](js-apis-resource-manager.md#screendensity) | number | 是 | 资源获取需要的屏幕密度，0表示默认屏幕密度。 |
| callback | [\_AsyncCallback](js-apis-base.md#asynccallback)<string> | 是 | 回调函数，返回resource对象对应的图片资源Base64编码。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |

**示例：**

```
1. import { resourceManager } from '@kit.LocalizationKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let resource: resourceManager.Resource = {
5. bundleName: "com.example.myapplication",
6. moduleName: "entry",
7. id: $r('app.media.test').id
8. };
9. try {
10. this.context.resourceManager.getMediaContentBase64(resource, 120, (error: BusinessError, value: string) => {
11. if (error != null) {
12. console.error(`callback getMediaContentBase64 failed, error code: ${error.code}, message: ${error.message}.`);
13. } else {
14. let media = value;
15. }
16. });
17. } catch (error) {
18. let code = (error as BusinessError).code;
19. let message = (error as BusinessError).message;
20. console.error(`callback getMediaContentBase64 failed, error code: ${code}, message: ${message}.`);
21. }
```

### getMediaContentBase64(deprecated)

PhonePC/2in1TabletTVWearable

getMediaContentBase64(resource: Resource): Promise<string>

获取指定resource对象对应的图片资源Base64编码，使用Promise异步回调。

说明

从API version 9开始支持，从API version 20开始废弃，建议使用[getMediaBase64ByName](js-apis-resource-manager.md#getmediabase64byname9-1)或[getMediaContentBase64](js-apis-resource-manager.md#getmediacontentbase649-1)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resource | [Resource](js-apis-resource-manager.md#resource9) | 是 | 资源信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回resource对象对应的图片资源Base64编码。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |

**示例：**

```
1. import { resourceManager } from '@kit.LocalizationKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let resource: resourceManager.Resource = {
5. bundleName: "com.example.myapplication",
6. moduleName: "entry",
7. id: $r('app.media.test').id
8. };
9. try {
10. this.context.resourceManager.getMediaContentBase64(resource).then((value: string) => {
11. let media = value;
12. }).catch((error: BusinessError) => {
13. console.error("getMediaContentBase64 promise error is " + error);
14. });
15. } catch (error) {
16. let code = (error as BusinessError).code;
17. let message = (error as BusinessError).message;
18. console.error(`promise getMediaContentBase64 failed, error code: ${code}, message: ${message}.`);
19. }
```

### getMediaContentBase64(deprecated)

PhonePC/2in1TabletTVWearable

getMediaContentBase64(resource: Resource, density: number): Promise<string>

获取指定resource对象对应的指定屏幕密度图片资源Base64编码，使用Promise异步回调。

说明

从API version 10开始支持，从API version 20开始废弃，建议使用[getMediaBase64ByName](js-apis-resource-manager.md#getmediabase64byname10-1)或[getMediaContentBase64](js-apis-resource-manager.md#getmediacontentbase6410-1)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resource | [Resource](js-apis-resource-manager.md#resource9) | 是 | 资源信息。 |
| [density](js-apis-resource-manager.md#screendensity) | number | 是 | 资源获取需要的屏幕密度，0表示默认屏幕密度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回resource对象对应的图片资源Base64编码。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |

**示例：**

```
1. import { resourceManager } from '@kit.LocalizationKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let resource: resourceManager.Resource = {
5. bundleName: "com.example.myapplication",
6. moduleName: "entry",
7. id: $r('app.media.test').id
8. };
9. try {
10. this.context.resourceManager.getMediaContentBase64(resource, 120).then((value: string) => {
11. let media = value;
12. }).catch((error: BusinessError) => {
13. console.error(`promise getMediaContentBase64 failed, error code: ${error.code}, message: ${error.message}.`);
14. });
15. } catch (error) {
16. let code = (error as BusinessError).code;
17. let message = (error as BusinessError).message;
18. console.error(`promise getMediaContentBase64 failed, error code: ${code}, message: ${message}.`);
19. }
```

### getDrawableDescriptor(deprecated)

PhonePC/2in1TabletTVWearable

getDrawableDescriptor(resource: Resource, density?: number, type?: number): DrawableDescriptor

获取指定resource对应的DrawableDescriptor对象，用于图标的显示，使用同步方式返回。

说明

从API version 10开始支持，从API version 20开始废弃，建议使用[getDrawableDescriptorByName](js-apis-resource-manager.md#getdrawabledescriptorbyname10)或[getDrawableDescriptor](js-apis-resource-manager.md#getdrawabledescriptor10)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resource | [Resource](js-apis-resource-manager.md#resource9) | 是 | 资源信息。 |
| [density](js-apis-resource-manager.md#screendensity) | number | 否 | 资源获取需要的屏幕密度，0或缺省表示默认屏幕密度。 |
| type11+ | number | 否 | - 1表示获取主题资源包中应用的分层图标资源。  - 0或缺省表示获取应用自身图标资源。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DrawableDescriptor](js-apis-arkui-drawabledescriptor.md#drawabledescriptor) | 资源ID值对应的DrawableDescriptor对象。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |

**示例：**

```
1. import { resourceManager } from '@kit.LocalizationKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { DrawableDescriptor } from '@kit.ArkUI';

5. let resource: resourceManager.Resource = {
6. bundleName: "com.example.myapplication",
7. moduleName: "entry",
8. id: $r('app.media.icon').id
9. };
10. try {
11. let drawableDescriptor:DrawableDescriptor = this.context.resourceManager.getDrawableDescriptor(resource);
12. } catch (error) {
13. let code = (error as BusinessError).code;
14. let message = (error as BusinessError).message;
15. console.error(`getDrawableDescriptor failed, error code: ${code}, message: ${message}.`);
16. }
17. try {
18. let drawableDescriptor:DrawableDescriptor = this.context.resourceManager.getDrawableDescriptor(resource, 120);
19. } catch (error) {
20. let code = (error as BusinessError).code;
21. let message = (error as BusinessError).message;
22. console.error(`getDrawableDescriptor failed, error code: ${code}, message: ${message}.`);
23. }
24. try {
25. let drawableDescriptor:DrawableDescriptor = this.context.resourceManager.getDrawableDescriptor(resource, 0, 1);
26. } catch (error) {
27. let code = (error as BusinessError).code;
28. let message = (error as BusinessError).message;
29. console.error(`getDrawableDescriptor failed, error code: ${code}, message: ${message}.`);
30. }
```

### getIntPluralStringValueSync(deprecated)

PhonePC/2in1TabletTVWearable

getIntPluralStringValueSync(resource: Resource, num: number, ...args: Array<string | number>): string

获取指定resource对象对应的[单复数](../harmonyos-guides/l10n-singular-plural.md)字符串，并根据args参数对字符串进行格式化，使用同步方式返回。

说明

* 从API version 18开始支持，从API version 20开始废弃，建议使用[getIntPluralStringByNameSync](js-apis-resource-manager.md#getintpluralstringbynamesync18)或[getIntPluralStringValueSync](js-apis-resource-manager.md#getintpluralstringvaluesync18)替代。
* 中文环境下，字符串不区分单复数；其他语言环境下，字符串区分单复数，具体规则参考[语言单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resource | [Resource](js-apis-resource-manager.md#resource9) | 是 | 资源信息。 |
| num | number | 是 | 数量值（整数）。根据当前语言的[单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)获取该数量值对应的字符串。 |
| ...args | Array<string | number> | 否 | 格式化字符串资源参数。  支持参数类型：%d、%f、%s、%%、%数字$d、%数字$f、%数字$s。  说明：%%转义为%; %数字$d中的数字表示使用args中的第几个参数。  举例：%%d格式化后为%d字符串; %1$d表示使用第一个参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | resource对象对应的格式化单复数字符串。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |
| 9001007 | Failed to format the resource obtained based on the resource ID. |

**示例：**

```
1. // 资源文件路径: src/main/resources/base/element/plural.json
2. {
3. "plural": [
4. {
5. "name": "format_test",
6. "value": [
7. {
8. "quantity": "one",
9. "value": "There is %d apple in the %s, the total amount is %f kg."
10. },
11. {
12. "quantity": "other",
13. "value": "There are %d apples in the %s, the total amount is %f kg."
14. }
15. ]
16. }
17. ]
18. }
```

```
1. import { resourceManager } from '@kit.LocalizationKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let resource: resourceManager.Resource = {
5. bundleName: "com.example.myapplication",
6. moduleName: "entry",
7. id: $r('app.plural.format_test').id
8. };

10. try {
11. // 根据语言单复数规则，参数num取值为1，英文环境下对应单复数类别为one
12. // 在资源文件中用quantity字段表示单复数类别，因此会获取quantity为one的字符串
13. let pluralStr = this.context.resourceManager.getIntPluralStringValueSync(resource, 1, 1, "basket", 0.3);
14. console.info(`getIntPluralStringValueSync, result: ${pluralStr}`);
15. // 打印输出结果: getIntPluralStringValueSync, result: There is 1 apple in the basket, the total amount is 0.3 kg.
16. } catch (error) {
17. let code = (error as BusinessError).code;
18. let message = (error as BusinessError).message;
19. console.error(`getIntPluralStringValueSync failed, error code: ${code}, message: ${message}.`);
20. }
```

### getDoublePluralStringValueSync(deprecated)

PhonePC/2in1TabletTVWearable

getDoublePluralStringValueSync(resource: Resource, num: number, ...args: Array<string | number>): string

获取指定resource对象对应的[单复数](../harmonyos-guides/l10n-singular-plural.md)字符串，并根据args参数对字符串进行格式化，使用同步方式返回。

说明

* 从API version 18开始支持，从API version 20开始废弃，建议使用[getDoublePluralStringByNameSync](js-apis-resource-manager.md#getdoublepluralstringbynamesync18)或[getDoublePluralStringValueSync](js-apis-resource-manager.md#getdoublepluralstringvaluesync18)替代。
* 中文环境下，字符串不区分单复数；其他语言环境下，字符串区分单复数，具体规则参考[语言单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resource | [Resource](js-apis-resource-manager.md#resource9) | 是 | 资源信息。 |
| num | number | 是 | 数量值（浮点数）。根据当前语言的[单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)获取该数量值对应的字符串。 |
| ...args | Array<string | number> | 否 | 格式化字符串资源参数。  支持参数类型：%d、%f、%s、%%、%数字$d、%数字$f、%数字$s。  说明：%%转义为%; %数字$d中的数字表示使用args中的第几个参数。  举例：%%d格式化后为%d字符串; %1$d表示使用第一个参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | resource对象对应的格式化单复数字符串。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |
| 9001007 | Failed to format the resource obtained based on the resource ID. |

**示例：**

```
1. // 资源文件路径: src/main/resources/base/element/plural.json
2. {
3. "plural": [
4. {
5. "name": "format_test",
6. "value": [
7. {
8. "quantity": "one",
9. "value": "There is %d apple in the %s, the total amount is %f kg."
10. },
11. {
12. "quantity": "other",
13. "value": "There are %d apples in the %s, the total amount is %f kg."
14. }
15. ]
16. }
17. ]
18. }
```

```
1. import { resourceManager } from '@kit.LocalizationKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let resource: resourceManager.Resource = {
5. bundleName: "com.example.myapplication",
6. moduleName: "entry",
7. id: $r('app.plural.format_test').id
8. };

10. try {
11. // 根据语言单复数规则，参数num取值为2.1，英文环境下对应单复数类别为other
12. // 在资源文件中用quantity字段表示单复数类别，因此会获取quantity为other的字符串
13. let pluralStr = this.context.resourceManager.getDoublePluralStringValueSync(resource, 2.1, 2, "basket", 0.6);
14. console.info(`getDoublePluralStringValueSync, result: ${pluralStr}`);
15. // 打印输出结果: getIntPluralStringValueSync, result: There are 2 apples in the basket, the total amount is 0.6 kg.
16. } catch (error) {
17. let code = (error as BusinessError).code;
18. let message = (error as BusinessError).message;
19. console.error(`getDoublePluralStringValueSync failed, error code: ${code}, message: ${message}.`);
20. }
```

### getPluralStringValueSync(deprecated)

PhonePC/2in1TabletTVWearable

getPluralStringValueSync(resId: number, num: number): string

获取指定资源ID，指定资源数量的单复数字符串，使用同步方式返回。

说明

中文环境下，字符串不区分单复数；其他语言环境下，字符串区分单复数，具体规则参考[语言单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)。

从API version 10开始支持，从API version 18开始废弃，建议使用[getIntPluralStringValueSync](js-apis-resource-manager.md#getintpluralstringvaluesync18)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resId | number | 是 | 资源ID值。 |
| num | number | 是 | 数量值。根据当前语言的复数规则获取该数量值对应的字符串数字，语言的复数规则参见[语言单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 根据指定数量获取指定ID字符串表示的单复数字符串。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |

**示例：**

```
1. // 资源文件路径: src/main/resources/base/element/plural.json
2. {
3. "plural": [
4. {
5. "name": "test",
6. "value": [
7. {
8. "quantity": "one",
9. "value": "%d apple"
10. },
11. {
12. "quantity": "other",
13. "value": "%d apples"
14. }
15. ]
16. }
17. ]
18. }
```

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. // 根据语言单复数规则，参数num取值为1，英文环境下对应单复数类别为one
5. // 在资源文件中用quantity字段表示单复数类别，因此会获取quantity为one的字符串
6. let pluralValue = this.context.resourceManager.getPluralStringValueSync($r('app.plural.test').id, 1);
7. console.info(`getPluralStringValueSync, result: ${pluralValue}`);
8. // 打印输出结果: getPluralStringValueSync, result: 1 apple
9. } catch (error) {
10. let code = (error as BusinessError).code;
11. let message = (error as BusinessError).message;
12. console.error(`getPluralStringValueSync failed, error code: ${code}, message: ${message}.`);
13. }
```

### getPluralStringValueSync(deprecated)

PhonePC/2in1TabletTVWearable

getPluralStringValueSync(resource: Resource, num: number): string

获取指定资源信息，指定资源数量的单复数字符串，使用同步方式返回。

说明

中文环境下，字符串不区分单复数；其他语言环境下，字符串区分单复数，具体规则参考[语言单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)。

从API version 10开始支持，从API version 18开始废弃，建议使用[getIntPluralStringValueSync](js-apis-resource-manager.md#getintpluralstringvaluesync18)或[getIntPluralStringByNameSync](js-apis-resource-manager.md#getintpluralstringbynamesync18)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resource | [Resource](js-apis-resource-manager.md#resource9) | 是 | 资源信息。 |
| num | number | 是 | 数量值。根据当前语言的复数规则获取该数量值对应的字符串数字，语言的复数规则参见[语言单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 根据指定数量获取指定resource对象表示的单复数字符串。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |

**示例：**

```
1. // 资源文件路径: src/main/resources/base/element/plural.json
2. {
3. "plural": [
4. {
5. "name": "test",
6. "value": [
7. {
8. "quantity": "one",
9. "value": "%d apple"
10. },
11. {
12. "quantity": "other",
13. "value": "%d apples"
14. }
15. ]
16. }
17. ]
18. }
```

```
1. import { resourceManager } from '@kit.LocalizationKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let resource: resourceManager.Resource = {
5. bundleName: "com.example.myapplication",
6. moduleName: "entry",
7. id: $r('app.plural.test').id
8. };
9. try {
10. // 根据语言单复数规则，参数num取值为1，英文环境下对应单复数类别为one
11. // 在资源文件中用quantity字段表示单复数类别，因此会获取quantity为one的字符串
12. let pluralValue = this.context.resourceManager.getPluralStringValueSync(resource, 1);
13. console.info(`getPluralStringValueSync, result: ${pluralValue}`);
14. // 打印输出结果: getPluralStringValueSync, result: 1 apple
15. } catch (error) {
16. let code = (error as BusinessError).code;
17. let message = (error as BusinessError).message;
18. console.error(`getPluralStringValueSync failed, error code: ${code}, message: ${message}.`);
19. }
```

### getPluralStringByNameSync(deprecated)

PhonePC/2in1TabletTVWearable

getPluralStringByNameSync(resName: string, num: number): string

获取指定资源名称，指定资源数量的单复数字符串，使用同步方式返回。

说明

中文环境下，字符串不区分单复数；其他语言环境下，字符串区分单复数，具体规则参考[语言单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)。

从API version 10开始支持，从API version 18开始废弃，建议使用[getIntPluralStringByNameSync](js-apis-resource-manager.md#getintpluralstringbynamesync18)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resName | string | 是 | 资源名称。 |
| num | number | 是 | 数量值。根据当前语言的复数规则获取该数量值对应的字符串数字，语言的复数规则参见[语言单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 根据指定数量获取指定资源名称表示的单复数字符串。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001003 | Invalid resource name. |
| 9001004 | No matching resource is found based on the resource name. |
| 9001006 | The resource is referenced cyclically. |

**示例：**

```
1. // 资源文件路径: src/main/resources/base/element/plural.json
2. {
3. "plural": [
4. {
5. "name": "test",
6. "value": [
7. {
8. "quantity": "one",
9. "value": "%d apple"
10. },
11. {
12. "quantity": "other",
13. "value": "%d apples"
14. }
15. ]
16. }
17. ]
18. }
```

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. // 根据语言单复数规则，参数num取值为1，英文环境下对应单复数类别为one
5. // 在资源文件中用quantity字段表示单复数类别，因此会获取quantity为one的字符串
6. let pluralValue = this.context.resourceManager.getPluralStringByNameSync("test", 1);
7. console.info(`getPluralStringByNameSync, result: ${pluralValue}`);
8. // 打印输出结果: getPluralStringByNameSync, result: 1 apple
9. } catch (error) {
10. let code = (error as BusinessError).code;
11. let message = (error as BusinessError).message;
12. console.error(`getPluralStringByNameSync failed, error code: ${code}, message: ${message}.`);
13. }
```

### getPluralStringValue(deprecated)

PhonePC/2in1TabletTVWearable

getPluralStringValue(resId: number, num: number, callback: \_AsyncCallback<string>): void

获取指定资源ID，指定资源数量的单复数字符串，使用callback异步回调。

说明

中文环境下，字符串不区分单复数；其他语言环境下，字符串区分单复数，具体规则参考[语言单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)。

从API version 9开始支持，从API version 18开始废弃，建议使用[getIntPluralStringValueSync](js-apis-resource-manager.md#getintpluralstringvaluesync18)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resId | number | 是 | 资源ID值。 |
| num | number | 是 | 数量值。根据当前语言的复数规则获取该数量值对应的字符串数字，语言的复数规则参见[语言单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)。 |
| callback | [\_AsyncCallback](js-apis-base.md#asynccallback)<string> | 是 | 回调函数，返回资源ID值对应的指定数量的单复数字符串。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |

**示例：**

```
1. // 资源文件路径: src/main/resources/base/element/plural.json
2. {
3. "plural": [
4. {
5. "name": "test",
6. "value": [
7. {
8. "quantity": "one",
9. "value": "%d apple"
10. },
11. {
12. "quantity": "other",
13. "value": "%d apples"
14. }
15. ]
16. }
17. ]
18. }
```

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. // 根据语言单复数规则，参数num取值为1，英文环境下对应单复数类别为one
4. // 在资源文件中用quantity字段表示单复数类别，因此会获取quantity为one的字符串
5. this.context.resourceManager.getPluralStringValue($r("app.plural.test").id, 1,
6. (error: BusinessError, value: string) => {
7. if (error != null) {
8. console.error(`callback getPluralStringValue failed, error code: ${error.code}, message: ${error.message}.`);
9. } else {
10. console.info(`getPluralStringValue, result: ${value}`);
11. // 打印输出结果: getPluralStringValue, result: 1 apple
12. }
13. });
```

### getPluralStringValue(deprecated)

PhonePC/2in1TabletTVWearable

getPluralStringValue(resId: number, num: number): Promise<string>

获取指定资源ID，指定资源数量的单复数字符串，使用Promise异步回调。

说明

中文环境下，字符串不区分单复数；其他语言环境下，字符串区分单复数，具体规则参考[语言单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)。

从API version 9开始支持，从API version 18开始废弃，建议使用[getIntPluralStringValueSync](js-apis-resource-manager.md#getintpluralstringvaluesync18)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resId | number | 是 | 资源ID值。 |
| num | number | 是 | 数量值。根据当前语言的复数规则获取该数量值对应的字符串数字，语言的复数规则参见[语言单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回资源ID值对应的指定数量的单复数字符串。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |

**示例：**

```
1. // 资源文件路径: src/main/resources/base/element/plural.json
2. {
3. "plural": [
4. {
5. "name": "test",
6. "value": [
7. {
8. "quantity": "one",
9. "value": "%d apple"
10. },
11. {
12. "quantity": "other",
13. "value": "%d apples"
14. }
15. ]
16. }
17. ]
18. }
```

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. // 根据语言单复数规则，参数num取值为1，英文环境下对应单复数类别为one
4. // 在资源文件中用quantity字段表示单复数类别，因此会获取quantity为one的字符串
5. this.context.resourceManager.getPluralStringValue($r("app.plural.test").id, 1)
6. .then((value: string) => {
7. console.info(`getPluralStringValue, result: ${value}`);
8. // 打印输出结果: getPluralStringValue, result: 1 apple
9. })
10. .catch((error: BusinessError) => {
11. console.error(`promise getPluralStringValue failed, error code: ${error.code}, message: ${error.message}.`);
12. });
```

### getPluralStringValue(deprecated)

PhonePC/2in1TabletTVWearable

getPluralStringValue(resource: Resource, num: number, callback: \_AsyncCallback<string>): void

获取指定资源信息，指定资源数量的单复数字符串，使用callback异步回调。

说明

中文环境下，字符串不区分单复数；其他语言环境下，字符串区分单复数，具体规则参考[语言单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)。

从API version 9开始支持，从API version 18开始废弃，建议使用[getIntPluralStringValueSync](js-apis-resource-manager.md#getintpluralstringvaluesync18)或[getIntPluralStringByNameSync](js-apis-resource-manager.md#getintpluralstringbynamesync18)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resource | [Resource](js-apis-resource-manager.md#resource9) | 是 | 资源信息。 |
| num | number | 是 | 数量值。根据当前语言的复数规则获取该数量值对应的字符串数字，语言的复数规则参见[语言单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)。 |
| callback | [\_AsyncCallback](js-apis-base.md#asynccallback)<string> | 是 | 回调函数，返回resource对象对应的指定数量的单复数字符串。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |

**示例：**

```
1. // 资源文件路径: src/main/resources/base/element/plural.json
2. {
3. "plural": [
4. {
5. "name": "test",
6. "value": [
7. {
8. "quantity": "one",
9. "value": "%d apple"
10. },
11. {
12. "quantity": "other",
13. "value": "%d apples"
14. }
15. ]
16. }
17. ]
18. }
```

```
1. import { resourceManager } from '@kit.LocalizationKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let resource: resourceManager.Resource = {
5. bundleName: "com.example.myapplication",
6. moduleName: "entry",
7. id: $r('app.plural.test').id
8. };
9. // 根据语言单复数规则，参数num取值为1，英文环境下对应单复数类别为one
10. // 在资源文件中用quantity字段表示单复数类别，因此会获取quantity为one的字符串
11. this.context.resourceManager.getPluralStringValue(resource, 1,
12. (error: BusinessError, value: string) => {
13. if (error != null) {
14. console.error(`callback getPluralStringValue failed, error code: ${error.code}, message: ${error.message}.`);
15. } else {
16. console.info(`getPluralStringValue, result: ${value}`);
17. // 打印输出结果: getPluralStringValue, result: 1 apple
18. }
19. });
```

### getPluralStringValue(deprecated)

PhonePC/2in1TabletTVWearable

getPluralStringValue(resource: Resource, num: number): Promise<string>

获取指定资源信息，指定资源数量的单复数字符串，使用Promise异步回调。

说明

中文环境下，字符串不区分单复数；其他语言环境下，字符串区分单复数，具体规则参考[语言单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)。

从API version 9开始支持，从API version 18开始废弃，建议使用[getIntPluralStringValueSync](js-apis-resource-manager.md#getintpluralstringvaluesync18)或[getIntPluralStringByNameSync](js-apis-resource-manager.md#getintpluralstringbynamesync18)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resource | [Resource](js-apis-resource-manager.md#resource9) | 是 | 资源信息。 |
| num | number | 是 | 数量值。根据当前语言的复数规则获取该数量值对应的字符串数字，语言的复数规则参见[语言单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回resource对象对应的指定数量的单复数字符串。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |

**示例：**

```
1. // 资源文件路径: src/main/resources/base/element/plural.json
2. {
3. "plural": [
4. {
5. "name": "test",
6. "value": [
7. {
8. "quantity": "one",
9. "value": "%d apple"
10. },
11. {
12. "quantity": "other",
13. "value": "%d apples"
14. }
15. ]
16. }
17. ]
18. }
```

```
1. import { resourceManager } from '@kit.LocalizationKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let resource: resourceManager.Resource = {
5. bundleName: "com.example.myapplication",
6. moduleName: "entry",
7. id: $r('app.plural.test').id
8. };
9. // 根据语言单复数规则，参数num取值为1，英文环境下对应单复数类别为one
10. // 在资源文件中用quantity字段表示单复数类别，因此会获取quantity为one的字符串
11. this.context.resourceManager.getPluralStringValue(resource, 1)
12. .then((value: string) => {
13. console.info(`getPluralStringValue, result: ${value}`);
14. // 打印输出结果: getPluralStringValue, result: 1 apple
15. })
16. .catch((error: BusinessError) => {
17. console.error(`promise getPluralStringValue failed, error code: ${error.code}, message: ${error.message}.`);
18. });
```

### getPluralStringByName(deprecated)

PhonePC/2in1TabletTVWearable

getPluralStringByName(resName: string, num: number, callback: \_AsyncCallback<string>): void

获取指定资源名称，指定资源数量的单复数字符串，使用callback异步回调。

说明

中文环境下，字符串不区分单复数；其他语言环境下，字符串区分单复数，具体规则参考[语言单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)。

从API version 9开始支持，从API version 18开始废弃，建议使用[getIntPluralStringByNameSync](js-apis-resource-manager.md#getintpluralstringbynamesync18)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resName | string | 是 | 资源名称。 |
| num | number | 是 | 数量值。根据当前语言的复数规则获取该数量值对应的字符串数字，语言的复数规则参见[语言单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)。 |
| callback | [\_AsyncCallback](js-apis-base.md#asynccallback)<string> | 是 | 回调函数，返回资源名称对应的指定数量的单复数字符串。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001003 | Invalid resource name. |
| 9001004 | No matching resource is found based on the resource name. |
| 9001006 | The resource is referenced cyclically. |

**示例：**

```
1. // 资源文件路径: src/main/resources/base/element/plural.json
2. {
3. "plural": [
4. {
5. "name": "test",
6. "value": [
7. {
8. "quantity": "one",
9. "value": "%d apple"
10. },
11. {
12. "quantity": "other",
13. "value": "%d apples"
14. }
15. ]
16. }
17. ]
18. }
```

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. // 根据语言单复数规则，参数num取值为1，英文环境下对应单复数类别为one
4. // 在资源文件中用quantity字段表示单复数类别，因此会获取quantity为one的字符串
5. this.context.resourceManager.getPluralStringByName("test", 1, (error: BusinessError, value: string) => {
6. if (error != null) {
7. console.error(`callback getPluralStringByName failed, error code: ${error.code}, message: ${error.message}.`);
8. } else {
9. console.info(`getPluralStringByName, result: ${value}`);
10. // 打印输出结果: getPluralStringByName, result: 1 apple
11. }
12. });
```

### getPluralStringByName(deprecated)

PhonePC/2in1TabletTVWearable

getPluralStringByName(resName: string, num: number): Promise<string>

获取指定资源名称，指定资源数量的单复数字符串，使用Promise异步回调。

说明

中文环境下，字符串不区分单复数；其他语言环境下，字符串区分单复数，具体规则参考[语言单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)。

从API version 9开始支持，从API version 18开始废弃，建议使用[getIntPluralStringByNameSync](js-apis-resource-manager.md#getintpluralstringbynamesync18)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resName | string | 是 | 资源名称。 |
| num | number | 是 | 数量值。根据当前语言的复数规则获取该数量值对应的字符串数字，语言的复数规则参见[语言单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | 根据传入的数量值，获取资源名称对应的字符串资源。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001003 | Invalid resource name. |
| 9001004 | No matching resource is found based on the resource name. |
| 9001006 | The resource is referenced cyclically. |

**示例：**

```
1. // 资源文件路径: src/main/resources/base/element/plural.json
2. {
3. "plural": [
4. {
5. "name": "test",
6. "value": [
7. {
8. "quantity": "one",
9. "value": "%d apple"
10. },
11. {
12. "quantity": "other",
13. "value": "%d apples"
14. }
15. ]
16. }
17. ]
18. }
```

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. // 根据语言单复数规则，参数num取值为1，英文环境下对应单复数类别为one
4. // 在资源文件中用quantity字段表示单复数类别，因此会获取quantity为one的字符串
5. this.context.resourceManager.getPluralStringByName("test", 1)
6. .then((value: string) => {
7. console.info(`getPluralStringByName, result: ${value}`);
8. // 打印输出结果: getPluralStringByName, result: 1 apple
9. })
10. .catch((error: BusinessError) => {
11. console.error(`promise getPluralStringByName failed, error code: ${error.code}, message: ${error.message}.`);
12. });
```

### getPluralString(deprecated)

PhonePC/2in1TabletTVWearable

getPluralString(resId: number, num: number): Promise<string>

获取指定资源ID，指定资源数量的单复数字符串，使用Promise异步回调。

说明

中文环境下，字符串不区分单复数；其他语言环境下，字符串区分单复数，具体规则参考[语言单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)。

从API version 6开始支持，从API version 9开始废弃，建议使用[getPluralStringValue](js-apis-resource-manager.md#getpluralstringvaluedeprecated-1)替代。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resId | number | 是 | 资源ID值。 |
| num | number | 是 | 数量值。根据当前语言的复数规则获取该数量值对应的字符串数字，语言的复数规则参见[语言单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回资源ID值对应的指定数量的单复数字符串。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. resourceManager.getResourceManager((error, mgr) => {
4. mgr.getPluralString($r("app.plural.test").id, 1).then((value: string) => {
5. let str = value;
6. }).catch((error: BusinessError) => {
7. console.error("getPluralString promise error is " + error);
8. });
9. });
```

### getPluralString(deprecated)

PhonePC/2in1TabletTVWearable

getPluralString(resId: number, num: number, callback: AsyncCallback<string>): void

获取指定资源ID，指定资源数量的单复数字符串，使用callback异步回调。

说明

中文环境下，字符串不区分单复数；其他语言环境下，字符串区分单复数，具体规则参考[语言单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)。

从API version 6开始支持，从API version 9开始废弃，建议使用[getPluralStringValue](js-apis-resource-manager.md#getpluralstringvaluedeprecated)替代。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resId | number | 是 | 资源ID值。 |
| num | number | 是 | 数量值。根据当前语言的复数规则获取该数量值对应的字符串数字，语言的复数规则参见[语言单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)。 |
| callback | [AsyncCallback](js-apis-resource-manager.md#asynccallbackdeprecated)<string> | 是 | 回调函数，返回资源ID值对应的指定数量的单复数字符串。 |

**示例：**

```
1. import { resourceManager } from '@kit.LocalizationKit';

3. resourceManager.getResourceManager((error, mgr) => {
4. mgr.getPluralString($r("app.plural.test").id, 1, (error: Error, value: string) => {
5. if (error != null) {
6. console.error("error is " + error);
7. } else {
8. let str = value;
9. }
10. });
11. });
```

### getBoolean(deprecated)

PhonePC/2in1TabletTVWearable

getBoolean(resource: Resource): boolean

获取指定resource对象对应的布尔值，使用同步方式返回。

说明

从API version 9开始支持，从API version 20开始废弃，建议使用[getBooleanByName](js-apis-resource-manager.md#getbooleanbyname9)或[getBoolean](js-apis-resource-manager.md#getboolean9)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resource | [Resource](js-apis-resource-manager.md#resource9) | 是 | 资源信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | resource对象对应的布尔值。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |

**示例：**

```
1. // 资源文件路径: src/main/resources/base/element/boolean.json
2. {
3. "boolean": [
4. {
5. "name": "boolean_test",
6. "value": true
7. }
8. ]
9. }
```

```
1. import { resourceManager } from '@kit.LocalizationKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let resource: resourceManager.Resource = {
5. bundleName: "com.example.myapplication",
6. moduleName: "entry",
7. id: $r('app.boolean.boolean_test').id
8. };
9. try {
10. let boolTest = this.context.resourceManager.getBoolean(resource);
11. console.info(`getBoolean, result: ${boolTest}`);
12. // 打印输出结果: getBoolean, result: true
13. } catch (error) {
14. let code = (error as BusinessError).code;
15. let message = (error as BusinessError).message;
16. console.error(`getBoolean failed, error code: ${code}, message: ${message}.`);
17. }
```

### getNumber(deprecated)

PhonePC/2in1TabletTVWearable

getNumber(resource: Resource): number

获取指定resource对象对应的integer数值或者float数值，使用同步方式返回。

说明

从API version 9开始支持，从API version 20开始废弃，建议使用[getNumberByName](js-apis-resource-manager.md#getnumberbyname9)或[getNumber](js-apis-resource-manager.md#getnumber9)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resource | [Resource](js-apis-resource-manager.md#resource9) | 是 | 资源信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | resource对象对应的数值。  integer对应的是原数值，float不带单位时对应的是原数值，带"vp","fp"单位时对应的是px值。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |

**示例：**

```
1. // 资源文件路径: src/main/resources/base/element/integer.json
2. {
3. "integer": [
4. {
5. "name": "integer_test",
6. "value": 100
7. }
8. ]
9. }
```

```
1. import { resourceManager } from '@kit.LocalizationKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let resource: resourceManager.Resource = {
5. bundleName: "com.example.myapplication",
6. moduleName: "entry",
7. id: $r('app.integer.integer_test').id
8. };

10. try {
11. let intValue = this.context.resourceManager.getNumber(resource);
12. console.info(`getNumber, int value: ${intValue}`);
13. // 打印输出结果: getNumber, int value: 100
14. } catch (error) {
15. let code = (error as BusinessError).code;
16. let message = (error as BusinessError).message;
17. console.error(`getNumber failed, error code: ${code}, message: ${message}.`);
18. }
```

### getColorSync(deprecated)

PhonePC/2in1TabletTVWearable

getColorSync(resource: Resource): number

获取指定resource对象对应的颜色值，使用同步方式返回。

说明

从API version 10开始支持，从API version 20开始废弃，建议使用[getColorByNameSync](js-apis-resource-manager.md#getcolorbynamesync10)或[getColorSync](js-apis-resource-manager.md#getcolorsync10)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resource | [Resource](js-apis-resource-manager.md#resource9) | 是 | 资源信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | resource对象对应的颜色值（十进制）。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |

**示例：**

```
1. // 资源文件路径: src/main/resources/base/element/color.json
2. {
3. "color": [
4. {
5. "name": "test",
6. "value": "#FFFFFF"
7. }
8. ]
9. }
```

```
1. import { resourceManager } from '@kit.LocalizationKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let resource: resourceManager.Resource = {
5. bundleName: "com.example.myapplication",
6. moduleName: "entry",
7. id: $r('app.color.test').id
8. };
9. try {
10. let colorValue = this.context.resourceManager.getColorSync(resource);
11. console.info(`getColorSync, result: ${colorValue}`);
12. // 打印输出结果: getColorSync, result: 4294967295
13. } catch (error) {
14. let code = (error as BusinessError).code;
15. let message = (error as BusinessError).message;
16. console.error(`getColorSync failed, error code: ${code}, message: ${message}.`);
17. }
```

### getColor(deprecated)

PhonePC/2in1TabletTVWearable

getColor(resource: Resource, callback: \_AsyncCallback<number>): void

获取指定resource对象对应的颜色值，使用callback异步回调。

说明

从API version 10开始支持，从API version 20开始废弃，建议使用[getColorByName](js-apis-resource-manager.md#getcolorbyname10)或[getColor](js-apis-resource-manager.md#getcolor10)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resource | [Resource](js-apis-resource-manager.md#resource9) | 是 | 资源信息。 |
| callback | [\_AsyncCallback](js-apis-base.md#asynccallback)<number> | 是 | 回调函数，返回resource对象对应的颜色值（十进制）。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |

**示例：**

```
1. // 资源文件路径: src/main/resources/base/element/color.json
2. {
3. "color": [
4. {
5. "name": "test",
6. "value": "#FFFFFF"
7. }
8. ]
9. }
```

```
1. import { resourceManager } from '@kit.LocalizationKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let resource: resourceManager.Resource = {
5. bundleName: "com.example.myapplication",
6. moduleName: "entry",
7. id: $r('app.color.test').id
8. };
9. this.context.resourceManager.getColor(resource, (error: BusinessError, value: number) => {
10. if (error != null) {
11. console.error(`callback getColor failed, error code: ${error.code}, message: ${error.message}.`);
12. } else {
13. console.info(`getColor, result: ${value}`);
14. // 打印输出结果: getColor, result: 4294967295
15. }
16. });
```

### getColor(deprecated)

PhonePC/2in1TabletTVWearable

getColor(resource: Resource): Promise<number>

获取指定resource对象对应的颜色值，使用Promise异步回调。

说明

从API version 10开始支持，从API version 20开始废弃，建议使用[getColorByName](js-apis-resource-manager.md#getcolorbyname10-1)或[getColor](js-apis-resource-manager.md#getcolor10-1)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resource | [Resource](js-apis-resource-manager.md#resource9) | 是 | 资源信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回resource对象对应的颜色值（十进制）。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |

**示例：**

```
1. // 资源文件路径: src/main/resources/base/element/color.json
2. {
3. "color": [
4. {
5. "name": "test",
6. "value": "#FFFFFF"
7. }
8. ]
9. }
```

```
1. import { resourceManager } from '@kit.LocalizationKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let resource: resourceManager.Resource = {
5. bundleName: "com.example.myapplication",
6. moduleName: "entry",
7. id: $r('app.color.test').id
8. };
9. this.context.resourceManager.getColor(resource)
10. .then((value: number) => {
11. console.info(`getColor, result: ${value}`);
12. // 打印输出结果: getColor, result: 4294967295
13. })
14. .catch((error: BusinessError) => {
15. console.error(`promise getColor failed, error code: ${error.code}, message: ${error.message}.`);
16. });
```

### getSymbol(deprecated)

PhonePC/2in1TabletTVWearable

getSymbol(resource: Resource): number

获取指定resource对象对应的[Symbol字符](https://developer.huawei.com/consumer/cn/design/harmonyos-symbol)Unicode码，使用同步方式返回。

说明

从API version 11开始支持，从API version 20开始废弃，建议使用[getSymbolByName](js-apis-resource-manager.md#getsymbolbyname11)或[getSymbol](js-apis-resource-manager.md#getsymbol11)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resource | [Resource](js-apis-resource-manager.md#resource9) | 是 | 资源信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | resource对象对应的Symbol字符Unicode码（十进制）。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |

**示例：**

```
1. import { resourceManager } from '@kit.LocalizationKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let resource: resourceManager.Resource = {
5. bundleName: "com.example.myapplication",
6. moduleName: "entry",
7. id: $r('sys.symbol.message').id
8. };
9. try {
10. let symbolValue = this.context.resourceManager.getSymbol(resource);
11. console.info(`getSymbol, result: ${symbolValue}`);
12. // 打印输出结果: getSymbol, result: 983183
13. } catch (error) {
14. let code = (error as BusinessError).code;
15. let message = (error as BusinessError).message;
16. console.error(`getSymbol failed, error code: ${code}, message: ${message}.`);
17. }
```

### getRawFile(deprecated)

PhonePC/2in1TabletTVWearable

getRawFile(path: string, callback: AsyncCallback<Uint8Array>): void

获取resources/rawfile目录下对应的rawfile文件内容，使用callback异步回调。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[getRawFileContent](js-apis-resource-manager.md#getrawfilecontent9)替代。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | rawfile文件路径。 |
| callback | [AsyncCallback](js-apis-resource-manager.md#asynccallbackdeprecated)<Uint8Array> | 是 | 回调函数，返回rawfile文件内容。 |

**示例：**

```
1. import { resourceManager } from '@kit.LocalizationKit';

3. resourceManager.getResourceManager((error, mgr) => {
4. mgr.getRawFile("test.txt", (error: Error, value: Uint8Array) => {
5. if (error != null) {
6. console.error("error is " + error);
7. } else {
8. let rawFile = value;
9. }
10. });
11. });
```

### getRawFile(deprecated)

PhonePC/2in1TabletTVWearable

getRawFile(path: string): Promise<Uint8Array>

获取resources/rawfile目录下对应的rawfile文件内容，使用Promise异步回调。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[getRawFileContent](js-apis-resource-manager.md#getrawfilecontent9-1)替代。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | rawfile文件路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Uint8Array> | Promise对象，返回rawfile文件内容。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. resourceManager.getResourceManager((error, mgr) => {
4. mgr.getRawFile("test.txt").then((value: Uint8Array) => {
5. let rawFile = value;
6. }).catch((error: BusinessError) => {
7. console.error("getRawFile promise error is " + error);
8. });
9. });
```

### getRawFileDescriptor(deprecated)

PhonePC/2in1TabletTVWearable

getRawFileDescriptor(path: string, callback: AsyncCallback<RawFileDescriptor>): void

获取resources/rawfile目录下对应rawfile文件的文件描述符（fd），使用callback异步回调。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[getRawFd](js-apis-resource-manager.md#getrawfd9)替代。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | rawfile文件路径。 |
| callback | [AsyncCallback](js-apis-resource-manager.md#asynccallbackdeprecated)<[RawFileDescriptor](js-apis-resource-manager.md#rawfiledescriptor9)> | 是 | 回调函数，返回rawfile文件的文件描述符（fd）。 |

**示例：**

```
1. import { resourceManager } from '@kit.LocalizationKit';

3. resourceManager.getResourceManager((error, mgr) => {
4. mgr.getRawFileDescriptor("test.txt", (error: Error, value: resourceManager.RawFileDescriptor) => {
5. if (error != null) {
6. console.error("error is " + error);
7. } else {
8. let fd = value.fd;
9. let offset = value.offset;
10. let length = value.length;
11. }
12. });
13. });
```

### getRawFileDescriptor(deprecated)

PhonePC/2in1TabletTVWearable

getRawFileDescriptor(path: string): Promise<RawFileDescriptor>

获取resources/rawfile目录下对应rawfile文件的文件描述符（fd），使用Promise异步回调。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[getRawFd](js-apis-resource-manager.md#getrawfd9-1)替代。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | rawfile文件路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[RawFileDescriptor](js-apis-resource-manager.md#rawfiledescriptor9)> | Promise对象，返回rawfile文件的文件描述符（fd）。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. resourceManager.getResourceManager((error, mgr) => {
4. mgr.getRawFileDescriptor("test.txt").then((value: resourceManager.RawFileDescriptor) => {
5. let fd = value.fd;
6. let offset = value.offset;
7. let length = value.length;
8. }).catch((error: BusinessError) => {
9. console.error("getRawFileDescriptor promise error is " + error);
10. });
11. });
```

### closeRawFileDescriptor(deprecated)

PhonePC/2in1TabletTVWearable

closeRawFileDescriptor(path: string, callback: AsyncCallback<void>): void

关闭resources/rawfile目录下rawfile文件的文件描述符（fd），使用callback异步回调。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[closeRawFd](js-apis-resource-manager.md#closerawfd9)替代。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | rawfile文件路径。 |
| callback | [AsyncCallback](js-apis-resource-manager.md#asynccallbackdeprecated)<void> | 是 | 回调函数。当关闭rawfile文件的文件描述符（fd）成功，err为undefined，否则为错误对象。 |

**示例：**

```
1. import { resourceManager } from '@kit.LocalizationKit';

3. resourceManager.getResourceManager((error, mgr) => {
4. mgr.closeRawFileDescriptor("test.txt", (error: Error) => {
5. if (error != null) {
6. console.error("error is " + error);
7. }
8. });
9. });
```

### closeRawFileDescriptor(deprecated)

PhonePC/2in1TabletTVWearable

closeRawFileDescriptor(path: string): Promise<void>

关闭resources/rawfile目录下rawfile文件的文件描述符（fd），使用Promise异步回调。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[closeRawFd](js-apis-resource-manager.md#closerawfd9-1)替代。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | rawfile文件路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. import { resourceManager } from '@kit.LocalizationKit';

3. resourceManager.getResourceManager((error, mgr) => {
4. mgr.closeRawFileDescriptor("test.txt");
5. });
```

## resourceManager.getSystemResourceManager(deprecated)

PhonePC/2in1TabletTVWearable

getSystemResourceManager(): ResourceManager

获取系统资源管理ResourceManager对象。

说明

当前接口获取到的系统资源管理ResourceManager对象中的Configuration为默认值。默认值如下：

{"locale": "", "direction": -1, "deviceType": -1, "screenDensity": 0, "colorMode": 1, "mcc": 0, "mnc": 0}。

从API version 10开始支持，从API version 20开始废弃，建议使用[resourceManager.getSysResourceManager](js-apis-resource-manager.md#resourcemanagergetsysresourcemanager20)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ResourceManager](js-apis-resource-manager.md#resourcemanager) | 系统资源管理对象。 |

**错误码：**

以下错误码的详细介绍请参见[资源管理错误码](errorcode-resource-manager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9001009 | Failed to access the system resource. which is not mapped to application sandbox, This error code will be thrown. |

**示例：**

```
1. import { resourceManager } from '@kit.LocalizationKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. let systemResourceManager = resourceManager.getSystemResourceManager();
6. systemResourceManager.getStringValue($r('sys.string.ohos_lab_vibrate').id).then((value: string) => {
7. let str = value;
8. }).catch((error: BusinessError) => {
9. console.error("systemResourceManager getStringValue promise error is " + error);
10. });
11. } catch (error) {
12. let code = (error as BusinessError).code;
13. let message = (error as BusinessError).message;
14. console.error(`getSystemResourceManager failed, error code: ${code}, message: ${message}.`);
15. }
```

## AsyncCallback(deprecated)

PhonePC/2in1TabletTVWearable

说明

从API version 6开始支持，从API version 9开始废弃，建议使用[AsyncCallback](js-apis-base.md#asynccallback)替代。

### (err: Error, data: T)(deprecated)

PhonePC/2in1TabletTVWearable

(err: Error, data: T): void;

异步回调函数，携带错误参数和异步返回值。

说明

从API version 6开始支持，从API version 9开始废弃，建议使用[AsyncCallback](js-apis-base.md#asynccallback)替代。

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| err | Error | 是 | 接口调用失败的错误信息。 |
| data | T | 是 | 接口调用时的回调信息。 |

## 附录

PhonePC/2in1TabletTVWearable

* 示例代码中用到的'app.string.test'文件内容如下：

  ```
  1. // 资源文件路径: src/main/resources/base/element/string.json
  2. {
  3. "string": [
  4. {
  5. "name": "test",
  6. "value": "I'm a test string resource."
  7. }
  8. ]
  9. }
  ```

  ```
  1. // 资源文件路径: src/main/resources/base/element/string.json
  2. {
  3. "string": [
  4. {
  5. "name": "test",
  6. "value": "I'm a %1$s, format int: %2$d, format float: %3$f."
  7. }
  8. ]
  9. }
  ```
* 示例代码中用到的'app.strarray.test'文件内容如下：

  ```
  1. // 资源文件路径: src/main/resources/base/element/strarray.json
  2. {
  3. "strarray": [
  4. {
  5. "name": "test",
  6. "value": [
  7. {
  8. "value": "I'm one of the array's values."
  9. }
  10. ]
  11. }
  12. ]
  13. }
  ```
* 示例代码中用到的'app.plural.test'文件内容如下：

  ```
  1. // 资源文件路径: src/main/resources/base/element/plural.json
  2. {
  3. "plural": [
  4. {
  5. "name": "test",
  6. "value": [
  7. {
  8. "quantity": "one",
  9. "value": "%d apple"
  10. },
  11. {
  12. "quantity": "other",
  13. "value": "%d apples"
  14. }
  15. ]
  16. }
  17. ]
  18. }
  ```
* 示例代码中用到的'app.plural.format\_test'文件内容如下：

  ```
  1. // 资源文件路径: src/main/resources/base/element/plural.json
  2. {
  3. "plural": [
  4. {
  5. "name": "format_test",
  6. "value": [
  7. {
  8. "quantity": "one",
  9. "value": "There is %d apple in the %s, the total amount is %f kg."
  10. },
  11. {
  12. "quantity": "other",
  13. "value": "There are %d apples in the %s, the total amount is %f kg."
  14. }
  15. ]
  16. }
  17. ]
  18. }
  ```
* 示例代码中用到的'app.boolean.boolean\_test'文件内容如下：

  ```
  1. // 资源文件路径: src/main/resources/base/element/boolean.json
  2. {
  3. "boolean": [
  4. {
  5. "name": "boolean_test",
  6. "value": true
  7. }
  8. ]
  9. }
  ```
* 示例代码中用到的"integer\_test"和"float\_test"文件内容如下：

  ```
  1. // 资源文件路径: src/main/resources/base/element/integer.json
  2. {
  3. "integer": [
  4. {
  5. "name": "integer_test",
  6. "value": 100
  7. }
  8. ]
  9. }
  ```

  ```
  1. // 资源文件路径: src/main/resources/base/element/float.json
  2. {
  3. "float": [
  4. {
  5. "name": "float_test",
  6. "value": "30.6vp"
  7. }
  8. ]
  9. }
  ```
* 示例代码中用到的'app.color.test'文件内容如下：

  ```
  1. // 资源文件路径: src/main/resources/base/element/color.json
  2. {
  3. "color": [
  4. {
  5. "name": "test",
  6. "value": "#FFFFFF"
  7. }
  8. ]
  9. }
  ```
