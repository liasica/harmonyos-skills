---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/store-moduleinstallmanager
title: moduleInstallManager (产品特性按需分发)
breadcrumb: API参考 > 应用服务 > AppGallery Kit（应用市场服务） > ArkTS API > moduleInstallManager (产品特性按需分发)
category: harmonyos-references
scraped_at: 2026-04-28T08:16:19+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a899fabcb5149ded02544fe0e5569c663699e6383f7e8bea9e8e1529f55dd929
---

借助该模块，您可以从应用的基本模块中分离特定功能和资源，并将其包含在子模块的包中。用户在使用应用过程中，可以动态下载子模块包。该模块包含判断模块是否安装、请求按需加载任务、监听模块下载进度、流量提醒弹窗、取消按需加载任务等功能。

说明

调用接口需捕获异常。

**起始版本：** 4.1.0(11)

## 导入模块

PhonePC/2in1TabletTV

```
1. import { moduleInstallManager } from '@kit.AppGalleryKit';
```

## InstalledModule

PhonePC/2in1TabletTV

当前模块的安装信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| moduleName | string | 是 | 否 | 模块名称。 |
| moduleType | [bundleManager.ModuleType](js-apis-bundlemanager.md#moduletype) | 是 | 是 | 模块类型。  **说明：** 当installStatus=1时，moduleType默认返回0（UNKNOWN）。 |
| installStatus | [InstallStatus](store-moduleinstallmanager.md#installstatus) | 是 | 否 | 模块安装结果。 |

## ModuleInstallSessionState

PhonePC/2in1TabletTV

请求、监听/注销监听接口，接口调用结果。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| code | [RequestErrorCode](store-moduleinstallmanager.md#requesterrorcode) | 是 | 否 | 接口调用结果码。 |
| taskStatus | [TaskStatus](store-moduleinstallmanager.md#taskstatus) | 是 | 否 | 按需下载任务状态码。 |
| taskId | string | 是 | 是 | 按需下载任务taskId，默认值为0。 |
| desc | string | 是 | 否 | 接口调用结果描述，默认值为“”。 |
| modules | string[] | 是 | 是 | 下载任务中的模块名列表，默认值为[]。 |
| totalSize | number | 是 | 是 | 下载的总模块大小（字节），默认值为0。 |
| downloadedSize | number | 是 | 是 | 已下载大小（字节），默认值为0。 |

## InstallStatus

PhonePC/2in1TabletTV

安装结果状态码类型的枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 4.1.0(11)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| INSTALLED | 0 | 模块已安装。 |
| NOT\_INSTALLED | 1 | 模块未安装。 |

## ReturnCode

PhonePC/2in1TabletTV

添加模块、取消下载、流量提醒弹窗接口，接口调用结果码类型的枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 4.1.0(11)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SUCCESS | 0 | 成功。 |
| FAILURE | 1 | 失败。 |

## RequestErrorCode

PhonePC/2in1TabletTV

请求、监听/注销监听接口，接口调用结果码类型的枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 4.1.0(11)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MODULE\_DEBUG\_FILES\_SIZE\_OVER\_LIMIT | -10 | 单次请求所有模块调试文件大小总和超过8G。  **起始版本：** 5.0.2(14) |
| MODULE\_DEBUG\_FILES\_NOT\_EXIST | -9 | 模块调试文件不存在。  **起始版本：** 5.0.2(14) |
| MODULE\_ALREADY\_EXISTS | -8 | 模块已存在。 |
| MODULE\_UNAVAILABLE | -7 | 要下载的模块不存在或者模块不适配该设备。 |
| INVALID\_REQUEST | -6 | 该请求无效，请求中包含的信息不准确。 |
| NETWORK\_ERROR | -5 | 网络异常，请求失败。 |
| INVOKER\_VERIFICATION\_FAILED | -4 | 调用者信息异常。 |
| FOREGROUND\_REQUIRED | -3 | 仅允许前台时请求按需加载。 |
| ACTIVE\_SESSION\_LIMIT\_EXCEEDED | -2 | 请求遭到拒绝，因为当前至少有一个请求正在下载。 |
| FAILURE | -1 | 失败。 |
| SUCCESS | 0 | 成功。 |
| DOWNLOAD\_WAIT\_WIFI | 1 | 当前使用的是流量，开发者需要调用[showCellularDataConfirmation](store-moduleinstallmanager.md#moduleinstallmanagershowcellulardataconfirmation)接口，提醒用户确认是否使用流量下载。 |

## TaskStatus

PhonePC/2in1TabletTV

请求、监听/注销监听接口，接口返回下载任务状态码类型的枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 4.1.0(11)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CREATE\_TASK\_FAILED | -4 | 创建下载任务失败。 |
| HIGHER\_VERSION\_INSTALLED | -3 | 本地存在相同或者更高版本。 |
| TASK\_ALREADY\_EXISTS | -2 | 下载任务已存在。 |
| TASK\_UNFOUND | -1 | 下载任务不存在。 |
| TASK\_CREATED | 0 | 创建下载任务成功。 |
| DOWNLOADING | 1 | 下载中。 |
| DOWNLOAD\_PAUSING | 2 | 暂停中。 |
| DOWNLOAD\_WAITING | 3 | 等待下载中。 |
| DOWNLOAD\_SUCCESSFUL | 4 | 下载成功完成。 |
| DOWNLOAD\_FAILED | 5 | 下载失败。 |
| DOWNLOAD\_WAIT\_WIFI | 6 | Wi-Fi预约。 |
| INSTALL\_WAITING | 20 | 等待安装。 |
| INSTALLING | 21 | 安装中。 |
| INSTALL\_SUCCESSFUL | 22 | 安装完成。 |
| INSTALL\_FAILED | 23 | 安装失败。 |

## moduleInstallManager.getInstalledModule

PhonePC/2in1TabletTV

getInstalledModule(moduleName: string): InstalledModule

查询模块安装信息接口。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| moduleName | string | 是 | 需要获取的模块名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [InstalledModule](store-moduleinstallmanager.md#installedmodule) | 当前模块的安装信息。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](store-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1006500001 | Failed to invoke the BMS. |

**示例：**

```
1. import { moduleInstallManager } from '@kit.AppGalleryKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. @Entry
5. @Component
6. struct LoadInstallService {

8. @State allInstalledModules: string = '';

10. private getModuleInstanceInfo() {
11. try {
12. // 查询模块安装信息
13. const result: moduleInstallManager.InstalledModule = moduleInstallManager.getInstalledModule('AModulelib');
14. this.allInstalledModules = JSON.stringify(result);
15. hilog.info(0, 'InstantDownload', 'getModuleInstanceInfo success=' + this.allInstalledModules);
16. } catch (error) {
17. hilog.error(0, 'InstantDownload', `getModuleInstanceInfo error.code is ${error.code}, message is ${error.message}`);
18. }
19. }

21. build() {
22. Column() {
23. }
24. .width('100%')
25. .height('100%')
26. .padding(16)
27. }
28. }
```

## InstallProvider

PhonePC/2in1TabletTV

按需加载controller父类对象。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 4.1.0(11)

## InstallRequest

PhonePC/2in1TabletTV

按需加载请求父类对象。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 4.1.0(11)

## ModuleInstallProvider

PhonePC/2in1TabletTV

实现按需加载的方法，提供创建按需加载请求对象能力，继承[InstallProvider](store-moduleinstallmanager.md#installprovider)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 4.1.0(11)

### ModuleInstallProvider.createModuleInstallRequest

PhonePC/2in1TabletTV

createModuleInstallRequest(context: common.UIAbilityContext | common.ExtensionContext): ModuleInstallRequest

创建按需加载请求对象，可通过返回值设置请求参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | [common.ExtensionContext](js-apis-inner-application-extensioncontext.md) | 是 | 调用方应用的上下文。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ModuleInstallRequest](store-moduleinstallmanager.md#moduleinstallrequest) | 按需下载请求对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md#section401-参数检查失败)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { common } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { moduleInstallManager } from '@kit.AppGalleryKit';

5. const TAG: string = 'createModuleInstallRequest';

7. @Entry
8. @Component
9. struct CreateModuleInstallRequest {

11. build() {
12. Column() {
13. Button("createModuleInstallRequest")
14. .onClick(() => {
15. try {
16. const myModuleInstallProvider: moduleInstallManager.ModuleInstallProvider =
17. new moduleInstallManager.ModuleInstallProvider();
18. const context: common.UIAbilityContext | common.ExtensionContext = this.getUIContext().getHostContext()  as common.UIAbilityContext;
19. // 创建按需加载请求对象
20. const myModuleInstallRequest: moduleInstallManager.ModuleInstallRequest =
21. myModuleInstallProvider.createModuleInstallRequest(context);
22. hilog.info(0, TAG, `myModuleInstallRequest: ${JSON.stringify(myModuleInstallRequest)}`);
23. } catch (error) {
24. hilog.error(0, TAG, `createModuleInstallRequest onError.code is ${error.code}, message is ${error.message}`);
25. }
26. })
27. .width('100%')
28. }
29. .margin(16)
30. .height('100%')
31. .justifyContent(FlexAlign.Center)
32. }
33. }
```

## ModuleInstallRequest

PhonePC/2in1TabletTV

按需下载请求对象，继承[InstallRequest](store-moduleinstallmanager.md#installrequest)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 4.1.0(11)

### ModuleInstallRequest.addModule

PhonePC/2in1TabletTV

addModule(moduleName: string): ReturnCode

添加要按需加载的模块名。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| moduleName | string | 是 | 模块名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ReturnCode](store-moduleinstallmanager.md#returncode) | 接口调用结果码。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md#section401-参数检查失败)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { common } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { moduleInstallManager } from '@kit.AppGalleryKit';

5. const TAG: string = 'addModule';

7. @Entry
8. @Component
9. struct AddModule {

11. build() {
12. Column() {
13. Button("addModule")
14. .onClick(() => {
15. try {
16. const myModuleInstallProvider: moduleInstallManager.ModuleInstallProvider =
17. new moduleInstallManager.ModuleInstallProvider();
18. const context: common.UIAbilityContext | common.ExtensionContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
19. // 创建按需加载请求对象
20. const myModuleInstallRequest: moduleInstallManager.ModuleInstallRequest =
21. myModuleInstallProvider.createModuleInstallRequest(context);
22. // 添加要按需加载的模块名
23. const aResult: moduleInstallManager.ReturnCode = myModuleInstallRequest.addModule('AModule');
24. const bResult: moduleInstallManager.ReturnCode = myModuleInstallRequest.addModule('BModule');
25. hilog.info(0, TAG, 'Succeeded in getting aResult:' + aResult + ' bResult:' + bResult);
26. } catch (error) {
27. hilog.error(0, TAG, `addModule onError.code is ${error.code}, message is ${error.message}`);
28. }
29. })
30. .width('100%')
31. }
32. .margin(16)
33. .height('100%')
34. .justifyContent(FlexAlign.Center)
35. }
36. }
```

## moduleInstallManager.fetchModules

PhonePC/2in1TabletTV

fetchModules(moduleInstallRequest: ModuleInstallRequest): Promise<ModuleInstallSessionState>

按需加载请求接口，支持调试模式，使用Promise方式异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| moduleInstallRequest | [ModuleInstallRequest](store-moduleinstallmanager.md#moduleinstallrequest) | 是 | 按需加载请求对象实例。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ModuleInstallSessionState](store-moduleinstallmanager.md#moduleinstallsessionstate)> | Promise对象，返回请求、监听/注销监听调用结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](store-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1006500004 | SA connection failed. |
| 1006500008 | Write param into container failed. |
| 1006500009 | Request to service error. |
| 1006500010 | Response from service cannot be recognized. |

**示例：**

```
1. import { common } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { moduleInstallManager } from '@kit.AppGalleryKit';

5. const TAG: string = 'fetchModules';

7. @Entry
8. @Component
9. struct FetchModules {

11. build() {
12. Column() {
13. Button("fetchModules")
14. .onClick(() => {
15. try {
16. const myModuleInstallProvider: moduleInstallManager.ModuleInstallProvider =
17. new moduleInstallManager.ModuleInstallProvider();
18. const context: common.UIAbilityContext | common.ExtensionContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
19. // 创建按需加载请求对象
20. const myModuleInstallRequest: moduleInstallManager.ModuleInstallRequest =
21. myModuleInstallProvider.createModuleInstallRequest(context);
22. // 添加要按需加载的模块名
23. myModuleInstallRequest.addModule('AModule');
24. myModuleInstallRequest.addModule('BModule');
25. // 按需加载请求接口,返回请求、监听/注销监听调用结果
26. moduleInstallManager.fetchModules(myModuleInstallRequest)
27. .then(() => {
28. hilog.info(0, TAG, 'Succeeded in fetching modules success data.' );
29. })
30. } catch (error) {
31. hilog.error(0, TAG, `fetching modules onError.code is ${error.code}, message is ${error.message}`);
32. }
33. })
34. .width('100%')
35. }
36. .margin(16)
37. .height('100%')
38. .justifyContent(FlexAlign.Center)
39. }
40. }
```

## moduleInstallManager.cancelTask

PhonePC/2in1TabletTV

cancelTask(taskId: string): ReturnCode

取消下载任务接口。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| taskId | string | 是 | 下载任务的taskId。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ReturnCode](store-moduleinstallmanager.md#returncode) | 接口调用结果码。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](store-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1006500007 | The specified service extension connect failed. |
| 1006500008 | Write param into container failed. |
| 1006500009 | Request to service error. |
| 1006500010 | Response from service cannot be recognized. |

**示例：**

```
1. import { moduleInstallManager } from '@kit.AppGalleryKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. // taskId 是fetchModules返回结果ModuleInstallSessionState中的taskId字段
6. const taskId: string = '********';
7. const rtnCode: moduleInstallManager.ReturnCode = moduleInstallManager.cancelTask(taskId);
8. hilog.info(0, 'TAG', "Succeeded in getting result:" + rtnCode);
9. } catch (error) {
10. hilog.error(0, 'TAG', `cancelTask onError.code is ${error.code}, message is ${error.message}`);
11. }
```

## moduleInstallManager.showCellularDataConfirmation

PhonePC/2in1TabletTV

showCellularDataConfirmation(context: common.UIAbilityContext | common.ExtensionContext,taskId: string): ReturnCode

流量提醒弹窗接口。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | [common.ExtensionContext](js-apis-inner-application-extensioncontext.md) | 是 | Context上下文，目前只支持UIAbilityContext和ExtensionContext，其中UIAbilityContext用于校验当前应用是否在前台。 |
| taskId | string | 是 | 下载任务的taskId。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ReturnCode](store-moduleinstallmanager.md#returncode) | 接口调用结果码。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](store-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1006500007 | The specified service extension connect failed. |
| 1006500008 | Write param into container failed. |
| 1006500009 | Request to service error. |
| 1006500010 | Response from service cannot be recognized. |

**示例：**

```
1. import { common } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { moduleInstallManager } from '@kit.AppGalleryKit';

5. const TAG: string = 'showCellularDataConfirmation';

7. @Entry
8. @Component
9. struct ShowCellularDataConfirmation {

11. build() {
12. Column() {
13. Button("showCellularDataConfirmation")
14. .onClick(() => {
15. try {
16. // taskId 是fetchModules返回结果ModuleInstallSessionState中的taskId字段
17. const taskId: string = '********';
18. const context = this.getUIContext().getHostContext()  as common.UIAbilityContext;
19. const rtnCode: moduleInstallManager.ReturnCode =
20. moduleInstallManager.showCellularDataConfirmation(context, taskId);
21. hilog.info(0, TAG, "Succeeded in getting result:" + rtnCode);
22. } catch (error) {
23. hilog.error(0, TAG, `showCellularDataConfirmation onError.code is ${error.code}, message is ${error.message}`);
24. }
25. })
26. .width('100%')
27. }
28. .margin(16)
29. .height('100%')
30. .justifyContent(FlexAlign.Center)
31. }
32. }
```

## moduleInstallManager.on('moduleInstallStatus')

PhonePC/2in1TabletTV

on(type: 'moduleInstallStatus', callback: Callback<ModuleInstallSessionState>, timeout: number): void

监听当前应用下载任务的进度，不支持多线程调用。加载模块时，通过回调函数通知调用者。安装成功且是调试模式时，会删除安装成功模块路径下的调试文件。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定值"moduleInstallStatus"。 |
| callback | Callback<[ModuleInstallSessionState](store-moduleinstallmanager.md#moduleinstallsessionstate)> | 是 | 回调函数，使用Callback的方式获取结果。 |
| timeout | number | 是 | 注册监听允许的最大监听时间，单位：s，默认30分钟（即30\*60s），且最大超过30分钟也是按30分钟算。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](store-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1006500002 | The interface is called repeatedly with the same input. |
| 1006500004 | SA connection failed. |

**示例：**

```
1. import { moduleInstallManager } from '@kit.AppGalleryKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. const timeout = 30 * 60;
6. moduleInstallManager.on('moduleInstallStatus', (data: moduleInstallManager.ModuleInstallSessionState) => {
7. // 注册监听
8. hilog.info(0, 'TAG', 'Succeeded in getting moduleInstallManager.on.' );
9. }, timeout)
10. } catch (error) {
11. hilog.error(0, 'TAG', `moduleInstallManager.on onError.code is ${error.code}, message is ${error.message}`);
12. }
```

## moduleInstallManager.off('moduleInstallStatus')

PhonePC/2in1TabletTV

off(type: 'moduleInstallStatus', callback?: Callback<ModuleInstallSessionState>): void

取消监听当前应用下载任务的进度，不支持多线程调用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定值"moduleInstallStatus"。 |
| callback | Callback<[ModuleInstallSessionState](store-moduleinstallmanager.md#moduleinstallsessionstate)> | 否 | 回调函数，使用Callback的方式获取结果。不传该参数则会取消当前应用的所有监听。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](store-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1006500004 | SA connection failed. |
| 1006500006 | The interface is not used together with "on". |

**示例：**

```
1. import { moduleInstallManager } from '@kit.AppGalleryKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. moduleInstallManager.off('moduleInstallStatus', (data: moduleInstallManager.ModuleInstallSessionState) => {
6. // 取消监听
7. hilog.info(0, 'TAG', 'Succeeded in getting moduleInstallManager.off.' );
8. })
9. } catch (error) {
10. hilog.error(0, 'TAG', `moduleInstallManager.off onError.code is ${error.code}, message is ${error.message}`);
11. }
```
