---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-app-context
title: Context (FA模型的上下文基类)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > FA模型能力的接口 > app > Context (FA模型的上下文基类)
category: harmonyos-references
scraped_at: 2026-04-28T07:58:30+08:00
doc_updated_at: 2026-03-23
content_hash: sha256:1d9e08d647b5f2672523e48451db1af8c617dac2758115c3a493c09590a64122
---

Context模块提供了Ability或Application的上下文的基础能力，包括允许访问特定于应用程序的资源、请求和验证权限等。

说明

本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在FA模型下使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import featureAbility from '@ohos.ability.featureAbility';
```

## 使用说明

PhonePC/2in1TabletTVWearable

Context对象是在featureAbility中创建实例，并通过featureAbility的[getContext](js-apis-ability-featureability.md#featureabilitygetcontext)接口返回，因此在使用Context时，必须导入@ohos.ability.featureAbility库。示例如下：

```
1. import featureAbility from '@ohos.ability.featureAbility';

3. let context: featureAbility.Context = featureAbility.getContext();
4. context.getOrCreateLocalDir().then((data) => {
5. console.info(`getOrCreateLocalDir data: ${JSON.stringify(data)}`);
6. });
```

## Context.getOrCreateLocalDir7+

PhonePC/2in1TabletTVWearable

getOrCreateLocalDir(callback: AsyncCallback<string>): void

获取应用程序的本地根目录。使用callback异步回调。

如果是第一次调用，将创建目录。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<string> | 是 | 回调函数，返回应用程序的本地根目录。 |

**示例：**

```
1. import featureAbility from '@ohos.ability.featureAbility';

3. let context: featureAbility.Context = featureAbility.getContext();
4. context.getOrCreateLocalDir((error, data)=>{
5. if (error && error.code !== 0) {
6. console.error(`getOrCreateLocalDir fail, error: ${JSON.stringify(error)}`);
7. } else {
8. console.info(`getOrCreateLocalDir success, data: ${JSON.stringify(data)}`);
9. }
10. });
```

## Context.getOrCreateLocalDir7+

PhonePC/2in1TabletTVWearable

getOrCreateLocalDir(): Promise<string>

获取应用程序的本地根目录。使用Promise异步回调。

如果是第一次调用，将创建目录。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回应用程序的本地根目录。 |

**示例：**

```
1. import featureAbility from '@ohos.ability.featureAbility';

3. let context: featureAbility.Context = featureAbility.getContext();
4. context.getOrCreateLocalDir().then((data) => {
5. console.info(`getOrCreateLocalDir data: ${JSON.stringify(data)}`);
6. });
```

## Context.verifyPermission7+

PhonePC/2in1TabletTVWearable

verifyPermission(permission: string, options: PermissionOptions, callback: AsyncCallback<number>): void

验证系统中运行的特定pid和uid是否允许指定的权限。使用callback异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| permission | string | 是 | 指定权限的名称。 |
| options | [PermissionOptions](js-apis-inner-app-context.md#permissionoptions7) | 是 | 权限选项。 |
| callback | AsyncCallback<number> | 是 | 回调函数，返回权限验证结果，0有权限，-1无权限。 |

**示例：**

```
1. import featureAbility from '@ohos.ability.featureAbility';
2. import bundle from '@ohos.bundle.bundleManager';
3. import { BusinessError } from '@ohos.base';

5. let context: featureAbility.Context = featureAbility.getContext();
6. bundle.getBundleInfo('com.context.test', 1, (err: BusinessError, datainfo: bundle.BundleInfo) =>{
7. context.verifyPermission('com.example.permission', {uid:datainfo.appInfo.uid}, (error, data) =>{
8. if (error && error.code !== 0) {
9. console.error(`verifyPermission fail, error: ${JSON.stringify(error)}`);
10. } else {
11. console.info(`verifyPermission success, data: ${JSON.stringify(data)}`);
12. }
13. });
14. });
```

示例代码中出现的getBundleInfo相关描述可参考对应[文档](js-apis-bundlemanager.md)。

## Context.verifyPermission7+

PhonePC/2in1TabletTVWearable

verifyPermission(permission: string, callback: AsyncCallback<number>): void

验证系统中运行的当前pid和uid是否具有指定的权限。使用callback异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| permission | string | 是 | 指定权限的名称。 |
| callback | AsyncCallback<number> | 是 | 回调函数，返回权限验证结果，0有权限，-1无权限。 |

**示例：**

```
1. import featureAbility from '@ohos.ability.featureAbility';

3. let context: featureAbility.Context = featureAbility.getContext();
4. context.verifyPermission('com.example.permission', (error, data) =>{
5. if (error && error.code !== 0) {
6. console.error(`verifyPermission fail, error: ${JSON.stringify(error)}`);
7. } else {
8. console.info(`verifyPermission success, data: ${JSON.stringify(data)}`);
9. }
10. });
```

## Context.verifyPermission7+

PhonePC/2in1TabletTVWearable

verifyPermission(permission: string, options?: PermissionOptions): Promise<number>

验证系统中运行的特定pid和uid是否具有指定的权限。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| permission | string | 是 | 指定权限的名称。 |
| options | [PermissionOptions](js-apis-inner-app-context.md#permissionoptions7) | 否 | 权限选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，如果pid和uid具有权限，则使用0进行异步回调；否则使用-1回调。 |

**示例：**

```
1. import featureAbility from '@ohos.ability.featureAbility';

3. let context: featureAbility.Context = featureAbility.getContext();
4. context.verifyPermission('com.context.permission', {pid:1}).then((data) => {
5. console.info(`verifyPermission data: ${JSON.stringify(data)}`);
6. });
```

## Context.requestPermissionsFromUser7+

PhonePC/2in1TabletTVWearable

requestPermissionsFromUser(permissions: Array<string>, requestCode: number, resultCallback: AsyncCallback<PermissionRequestResult>): void

从系统请求某些权限。使用callback异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| permissions | Array<string> | 是 | 指示要请求的权限列表。此参数不能为null。 |
| requestCode | number | 是 | 指示要传递给[PermissionRequestResult](js-apis-inner-app-context.md#permissionrequestresult7)的请求代码。 |
| resultCallback | AsyncCallback<[PermissionRequestResult](js-apis-inner-app-context.md#permissionrequestresult7)> | 是 | 回调函数，返回授权结果信息。 |

**示例：**

ArkTS示例：

```
1. import featureAbility from '@ohos.ability.featureAbility';

3. let context: featureAbility.Context = featureAbility.getContext();
4. context.requestPermissionsFromUser(
5. ['com.example.permission1',
6. 'com.example.permission2',
7. 'com.example.permission3',
8. 'com.example.permission4',
9. 'com.example.permission5'],
10. 1,
11. (error, data) => {
12. if (error && error.code !== 0) {
13. console.error(`requestPermissionsFromUser fail, error: ${JSON.stringify(error)}`);
14. } else {
15. console.info(`requestPermissionsFromUser success, data: ${JSON.stringify(data)}`);
16. }
17. }
18. );
```

JS示例：

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <div>
4. <input class="perm-btn" type="button" value="申请权限" onclick="requestPermissions" />
5. </div>
6. </div>
```

```
1. /*xxx.css*/
2. .container {
3. display: flex;
4. flex-direction: column;
5. justify-content: center;
6. align-items: center;
7. left: 0px;
8. top: 0px;
9. width: 100%;
10. height: 100%;
11. }

13. .perm-btn {
14. width: 200px;
15. height: 60px;
16. background-color: #007dff;
17. color: white;
18. font-size: 20px;
19. border: none;
20. border-radius: 8px;
21. }

23. .perm-btn:active {
24. background-color: #0058b3;
25. }
```

```
1. // xxx.js
2. import featureAbility from '@ohos.ability.featureAbility';

4. export default {
5. data: {
6. },
7. onInit() {
8. },
9. requestPermissions() {
10. let context = featureAbility.getContext();
11. context.requestPermissionsFromUser(
12. ['com.example.permission1',
13. 'com.example.permission2',
14. 'com.example.permission3',
15. 'com.example.permission4',
16. 'com.example.permission5'],
17. 1,
18. (error, data) => {
19. if (error && error.code !== 0) {
20. console.error(`requestPermissionsFromUser fail, error: ${JSON.stringify(error)}`);
21. } else {
22. console.info(`requestPermissionsFromUser success, data: ${JSON.stringify(data)}`);
23. }
24. }
25. );
26. }
27. }
```

## Context.requestPermissionsFromUser7+

PhonePC/2in1TabletTVWearable

requestPermissionsFromUser(permissions: Array<string>, requestCode: number): Promise<PermissionRequestResult>

从系统请求某些权限。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| permissions | Array<string> | 是 | 指示要请求的权限列表。此参数不能为null。 |
| requestCode | number | 是 | 指示要传递给[PermissionRequestResult](js-apis-inner-app-context.md#permissionrequestresult7)的请求代码。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[PermissionRequestResult](js-apis-inner-app-context.md#permissionrequestresult7)> | Promise对象，返回授权结果信息。 |

**示例：**

ArkTS示例：

```
1. import featureAbility from '@ohos.ability.featureAbility';

3. let context: featureAbility.Context = featureAbility.getContext();
4. context.requestPermissionsFromUser(
5. ['com.example.permission1',
6. 'com.example.permission2',
7. 'com.example.permission3',
8. 'com.example.permission4',
9. 'com.example.permission5'],
10. 1).then((data)=>{
11. console.info(`requestPermissionsFromUser data: ${JSON.stringify(data)}`);
12. }
13. );
```

JS示例：

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <div>
4. <input class="perm-btn" type="button" value="申请权限" onclick="requestPermissions" />
5. </div>
6. </div>
```

```
1. /*xxx.css*/
2. .container {
3. display: flex;
4. flex-direction: column;
5. justify-content: center;
6. align-items: center;
7. left: 0px;
8. top: 0px;
9. width: 100%;
10. height: 100%;
11. }

13. .perm-btn {
14. width: 200px;
15. height: 60px;
16. background-color: #007dff;
17. color: white;
18. font-size: 20px;
19. border: none;
20. border-radius: 8px;
21. }

23. .perm-btn:active {
24. background-color: #0058b3;
25. }
```

```
1. // xxx.js
2. import featureAbility from '@ohos.ability.featureAbility';

4. export default {
5. data: {
6. },
7. onInit() {
8. },
9. requestPermissions() {
10. let context = featureAbility.getContext();
11. context.requestPermissionsFromUser(
12. ['com.example.permission1',
13. 'com.example.permission2',
14. 'com.example.permission3',
15. 'com.example.permission4',
16. 'com.example.permission5'],
17. 1).then((data)=>{
18. console.info(`requestPermissionsFromUser data: ${JSON.stringify(data)}`);
19. }
20. );
21. }
22. }
```

## Context.getApplicationInfo7+

PhonePC/2in1TabletTVWearable

getApplicationInfo(callback: AsyncCallback<ApplicationInfo>): void

获取有关当前应用程序的信息。使用callback异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[ApplicationInfo](js-apis-bundlemanager-applicationinfo.md)> | 是 | 回调函数，返回当前应用程序的信息。 |

**示例：**

```
1. import featureAbility from '@ohos.ability.featureAbility';

3. let context: featureAbility.Context = featureAbility.getContext();
4. context.getApplicationInfo((error, data) => {
5. if (error && error.code !== 0) {
6. console.error(`getApplicationInfo fail, error: ${JSON.stringify(error)}`);
7. } else {
8. console.info(`getApplicationInfo success, data: ${JSON.stringify(data)}`);
9. }
10. });
```

## Context.getApplicationInfo7+

PhonePC/2in1TabletTVWearable

getApplicationInfo(): Promise<ApplicationInfo>

获取有关当前应用程序的信息。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ApplicationInfo](js-apis-bundle-applicationinfo.md)> | Promise对象，返回当前应用程序的信息。 |

**示例：**

```
1. import featureAbility from '@ohos.ability.featureAbility';

3. let context: featureAbility.Context = featureAbility.getContext();
4. context.getApplicationInfo().then((data) => {
5. console.info(`getApplicationInfo data: ${JSON.stringify(data)}`);
6. });
```

## Context.getBundleName7+

PhonePC/2in1TabletTVWearable

getBundleName(callback: AsyncCallback<string>): void

获取当前ability的Bundle名称。使用callback异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<string> | 是 | 回调函数，返回当前ability的Bundle名称。 |

**示例：**

```
1. import featureAbility from '@ohos.ability.featureAbility';

3. let context: featureAbility.Context = featureAbility.getContext();
4. context.getBundleName((error, data) => {
5. if (error && error.code !== 0) {
6. console.error(`getBundleName fail, error: ${JSON.stringify(error)}`);
7. } else {
8. console.info(`getBundleName success, data: ${JSON.stringify(data)}`);
9. }
10. });
```

## Context.getBundleName7+

PhonePC/2in1TabletTVWearable

getBundleName(): Promise<string>

获取当前ability的Bundle名称。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回当前ability的Bundle名称。 |

**示例：**

```
1. import featureAbility from '@ohos.ability.featureAbility';

3. let context: featureAbility.Context = featureAbility.getContext();
4. context.getBundleName().then((data) => {
5. console.info(`getBundleName data: ${JSON.stringify(data)}`);
6. });
```

## Context.getDisplayOrientation7+

PhonePC/2in1TabletTVWearable

getDisplayOrientation(callback: AsyncCallback<bundle.DisplayOrientation>): void

获取当前ability的显示方向。使用callback异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[bundle.DisplayOrientation](js-apis-bundlemanager.md#displayorientation)> | 是 | 回调函数，返回屏幕显示方向。 |

**示例：**

```
1. import featureAbility from '@ohos.ability.featureAbility';

3. let context: featureAbility.Context = featureAbility.getContext();
4. context.getDisplayOrientation((error, data) => {
5. if (error && error.code !== 0) {
6. console.error(`getDisplayOrientation fail, error: ${JSON.stringify(error)}`);
7. } else {
8. console.info(`getDisplayOrientation success, data: ${JSON.stringify(data)}`);
9. }
10. });
```

## Context.getDisplayOrientation7+

PhonePC/2in1TabletTVWearable

getDisplayOrientation(): Promise<bundle.DisplayOrientation>

获取此能力的当前显示方向。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[bundle.DisplayOrientation](js-apis-bundlemanager.md#displayorientation)> | Promise对象，返回屏幕显示方向。 |

**示例：**

```
1. import featureAbility from '@ohos.ability.featureAbility';

3. let context: featureAbility.Context = featureAbility.getContext();
4. context.getDisplayOrientation().then((data) => {
5. console.info(`getDisplayOrientation data: ${JSON.stringify(data)}`);
6. });
```

## Context.getExternalCacheDir(deprecated)

PhonePC/2in1TabletTVWearable

getExternalCacheDir(callback: AsyncCallback<string>): void

获取应用程序的外部缓存目录。使用callback异步回调。

说明

从API version 7开始不再支持。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<string> | 是 | 回调函数，返回应用程序的缓存目录的绝对路径。 |

**示例：**

```
1. import featureAbility from '@ohos.ability.featureAbility';

3. let context: featureAbility.Context = featureAbility.getContext();
4. context.getExternalCacheDir((error, data) => {
5. if (error && error.code !== 0) {
6. console.error(`getExternalCacheDir fail, error: ${JSON.stringify(error)}`);
7. } else {
8. console.info(`getExternalCacheDir success, data: ${JSON.stringify(data)}`);
9. }
10. });
```

## Context.getExternalCacheDir(deprecated)

PhonePC/2in1TabletTVWearable

getExternalCacheDir(): Promise<string>

获取应用程序的外部缓存目录。使用Promise异步回调。

说明

从API version 7开始不再支持。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回应用程序的缓存目录的绝对路径。 |

**示例：**

```
1. import featureAbility from '@ohos.ability.featureAbility';

3. let context: featureAbility.Context = featureAbility.getContext();
4. context.getExternalCacheDir().then((data) => {
5. console.info(`getExternalCacheDir data: ${JSON.stringify(data)}`);
6. });
```

## Context.setDisplayOrientation7+

PhonePC/2in1TabletTVWearable

setDisplayOrientation(orientation: bundle.DisplayOrientation, callback: AsyncCallback<void>): void

设置当前Ability的显示方向。使用callback异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| orientation | [bundle.DisplayOrientation](js-apis-bundlemanager.md#displayorientation) | 是 | 指示当前能力的新方向。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当设置当前Ability的显示方向成功，err为undefined，否则为错误对象。 |

**示例：**

```
1. import featureAbility from '@ohos.ability.featureAbility';
2. import bundleManager from '@ohos.bundle';

4. let context: featureAbility.Context = featureAbility.getContext();
5. let orientation = bundleManager.DisplayOrientation.LANDSCAPE;
6. context.setDisplayOrientation(orientation, (error) => {
7. console.error(`setDisplayOrientation fail, error: ${JSON.stringify(error)}`);
8. });
```

## Context.setDisplayOrientation7+

PhonePC/2in1TabletTVWearable

setDisplayOrientation(orientation: bundle.DisplayOrientation): Promise<void>

设置当前Ability的显示方向。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| orientation | [bundle.DisplayOrientation](js-apis-bundlemanager.md#displayorientation) | 是 | 表示屏幕显示方向。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. import featureAbility from '@ohos.ability.featureAbility';
2. import bundleManager from '@ohos.bundle';

4. let context: featureAbility.Context = featureAbility.getContext();
5. let orientation = bundleManager.DisplayOrientation.UNSPECIFIED;
6. context.setDisplayOrientation(orientation).then((data) => {
7. console.info(`setDisplayOrientation data: ${JSON.stringify(data)}`);
8. });
```

## Context.setShowOnLockScreen(deprecated)

PhonePC/2in1TabletTVWearable

setShowOnLockScreen(show: boolean, callback: AsyncCallback<void>): void

设置每当显示锁屏时是否在锁屏顶部显示此功能，使该功能保持激活状态。使用callback异步回调。

说明

该接口功能仅对系统应用生效。

从API version 7开始支持，从API version 9开始废弃。建议使用window.setShowOnLockScreen替代，新接口为系统接口。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| show | boolean | 是 | 指定是否在锁屏顶部显示此功能。值true表示在锁屏上显示，值false表示不显示。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当设置每当显示锁屏时是否在锁屏顶部显示此功能并使该功能保持激活状态的操作成功，err为undefined，否则为错误对象。 |

**示例：**

```
1. import featureAbility from '@ohos.ability.featureAbility';

3. let context: featureAbility.Context = featureAbility.getContext();
4. let show = true;
5. context.setShowOnLockScreen(show, (error) => {
6. console.error(`setShowOnLockScreen fail, error: ${JSON.stringify(error)}`);
7. });
```

## Context.setShowOnLockScreen(deprecated)

PhonePC/2in1TabletTVWearable

setShowOnLockScreen(show: boolean): Promise<void>

设置每当显示锁屏时是否在锁屏顶部显示此功能，使该功能保持激活状态。使用Promise异步回调。

说明

该接口功能仅对系统应用生效。

从API version 7开始支持，从API version 9开始废弃。建议使用window.setShowOnLockScreen替代，新接口为系统接口。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| show | boolean | 是 | 指定是否在锁屏顶部显示此功能。值true表示在锁屏上显示，值false表示不显示。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. import featureAbility from '@ohos.ability.featureAbility';

3. let context: featureAbility.Context = featureAbility.getContext();
4. let show = true;
5. context.setShowOnLockScreen(show).then((data) => {
6. console.info(`setShowOnLockScreen data: ${JSON.stringify(data)}`);
7. });
```

## Context.setWakeUpScreen(deprecated)

PhonePC/2in1TabletTVWearable

setWakeUpScreen(wakeUp: boolean, callback: AsyncCallback<void>): void

设置恢复此功能时是否唤醒屏幕。使用callback异步回调。

说明

该接口功能仅对系统应用生效。

从API version 7开始支持，从API version 12开始废弃。替代接口window.setWakeUpScreen替代，新接口为系统接口。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| wakeUp | boolean | 是 | 指定是否唤醒屏幕。值true表示唤醒它，值false表示不唤醒它。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当设置恢复此功能时是否唤醒屏幕成功，err为undefined，否则为错误对象。 |

**示例：**

```
1. import featureAbility from '@ohos.ability.featureAbility';

3. let context: featureAbility.Context = featureAbility.getContext();
4. let wakeUp = true;
5. context.setWakeUpScreen(wakeUp, (error) => {
6. console.error(`setWakeUpScreen fail, error: ${JSON.stringify(error)}`);
7. });
```

## Context.setWakeUpScreen(deprecated)

PhonePC/2in1TabletTVWearable

setWakeUpScreen(wakeUp: boolean): Promise<void>

设置恢复此功能时是否唤醒屏幕。使用Promise异步回调。

说明

该接口功能仅对系统应用生效。

从API version 7开始支持，从API version 12开始废弃。替代接口window.setWakeUpScreen替代，新接口为系统接口。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| wakeUp | boolean | 是 | 指定是否唤醒屏幕。值true表示唤醒它，值false表示不唤醒它。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. import featureAbility from '@ohos.ability.featureAbility';

3. let context: featureAbility.Context = featureAbility.getContext();
4. let wakeUp = true;
5. context.setWakeUpScreen(wakeUp).then((data) => {
6. console.info(`setWakeUpScreen data: ${JSON.stringify(data)}`);
7. });
```

## Context.getProcessInfo7+

PhonePC/2in1TabletTVWearable

getProcessInfo(callback: AsyncCallback<ProcessInfo>): void

获取有关当前进程的信息，包括进程ID和名称。使用callback异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[ProcessInfo](js-apis-inner-app-processinfo.md)> | 是 | 回调函数，返回当前进程的信息。 |

**示例：**

```
1. import featureAbility from '@ohos.ability.featureAbility';

3. let context: featureAbility.Context = featureAbility.getContext();
4. context.getProcessInfo((error, data) => {
5. if (error && error.code !== 0) {
6. console.error(`getProcessInfo fail, error: ${JSON.stringify(error)}`);
7. } else {
8. console.info(`getProcessInfo success, data: ${JSON.stringify(data)}`);
9. }
10. });
```

## Context.getProcessInfo7+

PhonePC/2in1TabletTVWearable

getProcessInfo(): Promise<ProcessInfo>

获取有关当前进程的信息，包括进程id和名称。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ProcessInfo](js-apis-inner-app-processinfo.md)> | Promise对象，返回当前进程的信息。 |

**示例：**

```
1. import featureAbility from '@ohos.ability.featureAbility';

3. let context: featureAbility.Context = featureAbility.getContext();
4. context.getProcessInfo().then((data) => {
5. console.info(`getProcessInfo data: ${JSON.stringify(data)}`);
6. });
```

## Context.getElementName7+

PhonePC/2in1TabletTVWearable

getElementName(callback: AsyncCallback<ElementName>): void

获取当前ability的ohos.bundleManager.ElementName对象。使用callback异步回调。

此方法仅适用于页面功能。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[ElementName](js-apis-bundlemanager-elementname.md)> | 是 | 回调函数，返回当前ability的ohos.bundleManager.ElementName对象。 |

**示例：**

```
1. import featureAbility from '@ohos.ability.featureAbility';

3. let context: featureAbility.Context = featureAbility.getContext();
4. context.getElementName((error, data) => {
5. if (error && error.code !== 0) {
6. console.error(`getElementName fail, error: ${JSON.stringify(error)}`);
7. } else {
8. console.info(`getElementName success, data: ${JSON.stringify(data)}`);
9. }
10. });
```

## Context.getElementName7+

PhonePC/2in1TabletTVWearable

getElementName(): Promise<ElementName>

获取当前能力的ohos.bundleManager.ElementName对象。使用Promise异步回调。

此方法仅适用于页面功能。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ElementName](js-apis-bundlemanager-elementname.md)> | Promise对象，返回当前ability的ohos.bundleManager.ElementName对象。 |

**示例：**

```
1. import featureAbility from '@ohos.ability.featureAbility';

3. let context: featureAbility.Context = featureAbility.getContext();
4. context.getElementName().then((data) => {
5. console.info(`getElementName data: ${JSON.stringify(data)}`);
6. });
```

## Context.getProcessName7+

PhonePC/2in1TabletTVWearable

getProcessName(callback: AsyncCallback<string>): void

获取当前进程的名称。使用callback异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<string> | 是 | 回调函数，返回当前进程的名称。 |

**示例：**

```
1. import featureAbility from '@ohos.ability.featureAbility';

3. let context: featureAbility.Context = featureAbility.getContext();
4. context.getProcessName((error, data) => {
5. if (error && error.code !== 0) {
6. console.error(`getProcessName fail, error: ${JSON.stringify(error)}`);
7. } else {
8. console.info(`getProcessName success, data: ${JSON.stringify(data)}`);
9. }
10. });
```

## Context.getProcessName7+

PhonePC/2in1TabletTVWearable

getProcessName(): Promise<string>

获取当前进程的名称。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回当前进程的名称。 |

**示例：**

```
1. import featureAbility from '@ohos.ability.featureAbility';

3. let context: featureAbility.Context = featureAbility.getContext();
4. context.getProcessName().then((data) => {
5. console.info(`getProcessName data: ${JSON.stringify(data)}`);
6. });
```

## Context.getCallingBundle7+

PhonePC/2in1TabletTVWearable

getCallingBundle(callback: AsyncCallback<string>): void

获取ability调用方的Bundle名称。使用callback异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<string> | 是 | 回调函数，返回ability调用方的Bundle名称。 |

**示例：**

```
1. import featureAbility from '@ohos.ability.featureAbility';

3. let context: featureAbility.Context = featureAbility.getContext();
4. context.getCallingBundle((error, data) => {
5. if (error && error.code !== 0) {
6. console.error(`getCallingBundle fail, error: ${JSON.stringify(error)}`);
7. } else {
8. console.info(`getCallingBundle success, data: ${JSON.stringify(data)}`);
9. }
10. });
```

## Context.getCallingBundle7+

PhonePC/2in1TabletTVWearable

getCallingBundle(): Promise<string>

获取ability调用方的Bundle名称。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回ability调用方的Bundle名称。 |

**示例：**

```
1. import featureAbility from '@ohos.ability.featureAbility';

3. let context: featureAbility.Context = featureAbility.getContext();
4. context.getCallingBundle().then((data) => {
5. console.info(`getCallingBundle data: ${JSON.stringify(data)}`);
6. });
```

## Context.getCacheDir

PhonePC/2in1TabletTVWearable

getCacheDir(callback: AsyncCallback<string>): void

获取该应用程序的内部存储目录。使用callback异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<string> | 是 | 回调函数，返回该应用程序的内部存储目录。 |

**示例：**

```
1. import featureAbility from '@ohos.ability.featureAbility';

3. let context: featureAbility.Context = featureAbility.getContext();
4. context.getCacheDir((error, data) => {
5. if (error && error.code !== 0) {
6. console.error(`getCacheDir fail, error: ${JSON.stringify(error)}`);
7. } else {
8. console.info(`getCacheDir success, data: ${JSON.stringify(data)}`);
9. }
10. });
```

## Context.getCacheDir

PhonePC/2in1TabletTVWearable

getCacheDir(): Promise<string>

获取该应用程序的内部存储目录。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回该应用程序的内部存储目录。 |

**示例：**

```
1. import featureAbility from '@ohos.ability.featureAbility';

3. let context: featureAbility.Context = featureAbility.getContext();
4. context.getCacheDir().then((data) => {
5. console.info(`getCacheDir data: ${JSON.stringify(data)}`);
6. });
```

## Context.getFilesDir

PhonePC/2in1TabletTVWearable

getFilesDir(callback: AsyncCallback<string>): void

获取内部存储器上此应用程序的文件目录。使用callback异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<string> | 是 | 回调函数，返回内部存储器上此应用程序的文件目录。 |

**示例：**

```
1. import featureAbility from '@ohos.ability.featureAbility';

3. let context: featureAbility.Context = featureAbility.getContext();
4. context.getFilesDir((error, data) => {
5. if (error && error.code !== 0) {
6. console.error(`getFilesDir fail, error: ${JSON.stringify(error)}`);
7. } else {
8. console.info(`getFilesDir success, data: ${JSON.stringify(data)}`);
9. }
10. });
```

## Context.getFilesDir

PhonePC/2in1TabletTVWearable

getFilesDir(): Promise<string>

获取内部存储器上此应用程序的文件目录。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回内部存储器上此应用程序的文件目录。 |

**示例：**

```
1. import featureAbility from '@ohos.ability.featureAbility';

3. let context: featureAbility.Context = featureAbility.getContext();
4. context.getFilesDir().then((data) => {
5. console.info(`getFilesDir data: ${JSON.stringify(data)}`);
6. });
```

## Context.getOrCreateDistributedDir7+

PhonePC/2in1TabletTVWearable

getOrCreateDistributedDir(callback: AsyncCallback<string>): void

获取Ability或应用的分布式文件路径。使用callback异步回调。

如果分布式文件路径不存在，系统将创建一个路径并返回创建的路径。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<string> | 是 | 回调函数，返回Ability或应用的分布式文件路径。  若路径不存在，系统将创建一个路径并返回创建的路径。 |

**示例：**

```
1. import featureAbility from '@ohos.ability.featureAbility';

3. let context: featureAbility.Context = featureAbility.getContext();
4. context.getOrCreateDistributedDir((error, data) => {
5. if (error && error.code !== 0) {
6. console.error(`getOrCreateDistributedDir fail, error: ${JSON.stringify(error)}`);
7. } else {
8. console.info(`getOrCreateDistributedDir success, data: ${JSON.stringify(data)}`);
9. }
10. });
```

## Context.getOrCreateDistributedDir7+

PhonePC/2in1TabletTVWearable

getOrCreateDistributedDir(): Promise<string>

获取Ability或应用的分布式文件路径。使用Promise异步回调。

如果分布式文件路径不存在，系统将创建一个路径并返回创建的路径。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回Ability或应用的分布式文件路径。若为首次调用，则将创建目录。 |

**示例：**

```
1. import featureAbility from '@ohos.ability.featureAbility';

3. let context: featureAbility.Context = featureAbility.getContext();
4. context.getOrCreateDistributedDir().then((data) => {
5. console.info(`getOrCreateDistributedDir data: ${JSON.stringify(data)}`);
6. });
```

## Context.getAppType7+

PhonePC/2in1TabletTVWearable

getAppType(callback: AsyncCallback<string>): void

获取此应用的类型。使用callback异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<string> | 是 | 回调函数，返回此应用程序的类型。 |

**示例：**

```
1. import featureAbility from '@ohos.ability.featureAbility';

3. let context: featureAbility.Context = featureAbility.getContext();
4. context.getAppType((error, data) => {
5. if (error && error.code !== 0) {
6. console.error(`getAppType fail, error: ${JSON.stringify(error)}`);
7. } else {
8. console.info(`getAppType success, data: ${JSON.stringify(data)}`);
9. }
10. });
```

## Context.getAppType7+

PhonePC/2in1TabletTVWearable

getAppType(): Promise<string>

获取此应用的类型。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回此应用的类型。 |

**示例：**

```
1. import featureAbility from '@ohos.ability.featureAbility';

3. let context: featureAbility.Context = featureAbility.getContext();
4. context.getAppType().then((data) => {
5. console.info(`getAppType data: ${JSON.stringify(data)}`);
6. });
```

## Context.getHapModuleInfo7+

PhonePC/2in1TabletTVWearable

getHapModuleInfo(callback: AsyncCallback<HapModuleInfo>): void

获取应用的ModuleInfo对象。使用callback异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[HapModuleInfo](js-apis-bundlemanager-hapmoduleinfo.md)> | 是 | 回调函数，返回应用的ModuleInfo对象。 |

**示例：**

```
1. import featureAbility from '@ohos.ability.featureAbility';

3. let context: featureAbility.Context = featureAbility.getContext();
4. context.getHapModuleInfo((error, data) => {
5. if (error && error.code !== 0) {
6. console.error(`getHapModuleInfo fail, error: ${JSON.stringify(error)}`);
7. } else {
8. console.info(`getHapModuleInfo success, data: ${JSON.stringify(data)}`);
9. }
10. });
```

## Context.getHapModuleInfo7+

PhonePC/2in1TabletTVWearable

getHapModuleInfo(): Promise<HapModuleInfo>

获取应用的ModuleInfo对象。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[HapModuleInfo](js-apis-bundlemanager-hapmoduleinfo.md)> | Promise对象，返回应用的ModuleInfo对象。 |

**示例：**

```
1. import featureAbility from '@ohos.ability.featureAbility';

3. let context: featureAbility.Context = featureAbility.getContext();
4. context.getHapModuleInfo().then((data) => {
5. console.info(`getHapModuleInfo data: ${JSON.stringify(data)}`);
6. });
```

## Context.getAppVersionInfo7+

PhonePC/2in1TabletTVWearable

getAppVersionInfo(callback: AsyncCallback<AppVersionInfo>): void

获取应用的版本信息。使用callback异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[AppVersionInfo](js-apis-inner-app-appversioninfo.md)> | 是 | 回调函数，返回应用版本信息。 |

**示例：**

```
1. import featureAbility from '@ohos.ability.featureAbility';

3. let context: featureAbility.Context = featureAbility.getContext();
4. context.getAppVersionInfo((error, data) => {
5. if (error && error.code !== 0) {
6. console.error(`getAppVersionInfo fail, error: ${JSON.stringify(error)}`);
7. } else {
8. console.info(`getAppVersionInfo success, data: ${JSON.stringify(data)}`);
9. }
10. });
```

## Context.getAppVersionInfo7+

PhonePC/2in1TabletTVWearable

getAppVersionInfo(): Promise<AppVersionInfo>

获取应用的版本信息。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AppVersionInfo](js-apis-inner-app-appversioninfo.md)> | Promise对象，返回应用版本信息。 |

**示例：**

```
1. import featureAbility from '@ohos.ability.featureAbility';

3. let context: featureAbility.Context = featureAbility.getContext();
4. context.getAppVersionInfo().then((data) => {
5. console.info(`getAppVersionInfo data: ${JSON.stringify(data)}`);
6. });
```

## Context.getAbilityInfo7+

PhonePC/2in1TabletTVWearable

getAbilityInfo(callback: AsyncCallback<AbilityInfo>): void

查询当前归属Ability详细信息。使用callback异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[AbilityInfo](js-apis-bundlemanager-abilityinfo.md)> | 是 | 回调函数，返回当前归属Ability详细信息。 |

**示例：**

```
1. import featureAbility from '@ohos.ability.featureAbility';

3. let context: featureAbility.Context = featureAbility.getContext();
4. context.getAbilityInfo((error, data) => {
5. if (error && error.code !== 0) {
6. console.error(`getAbilityInfo fail, error: ${JSON.stringify(error)}`);
7. } else {
8. console.info(`getAbilityInfo success, data: ${JSON.stringify(data)}`);
9. }
10. });
```

## Context.getAbilityInfo7+

PhonePC/2in1TabletTVWearable

getAbilityInfo(): Promise<AbilityInfo>

查询当前归属Ability详细信息。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AbilityInfo](js-apis-bundlemanager-abilityinfo.md)> | Promise对象，返回当前归属Ability详细信息。 |

**示例：**

```
1. import featureAbility from '@ohos.ability.featureAbility';

3. let context: featureAbility.Context = featureAbility.getContext();
4. context.getAbilityInfo().then((data) => {
5. console.info(`getAbilityInfo data: ${JSON.stringify(data)}`);
6. });
```

## Context.getApplicationContext7+

PhonePC/2in1TabletTVWearable

getApplicationContext(): Context

获取应用上下文信息。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Context | 返回应用上下文信息。 |

**示例：**

```
1. import featureAbility from '@ohos.ability.featureAbility';

3. let context: featureAbility.Context = featureAbility.getContext().getApplicationContext();
```

## Context.isUpdatingConfigurations7+

PhonePC/2in1TabletTVWearable

isUpdatingConfigurations(callback: AsyncCallback<boolean>): void

检查此能力的配置是否正在更改。使用callback异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数，返回true表示该Ability的配置正在更改，否则返回false。 |

**示例：**

```
1. import featureAbility from '@ohos.ability.featureAbility';

3. let context: featureAbility.Context = featureAbility.getContext();
4. context.isUpdatingConfigurations((error, data) => {
5. if (error && error.code !== 0) {
6. console.error(`isUpdatingConfigurations fail, error: ${JSON.stringify(error)}`);
7. } else {
8. console.info(`isUpdatingConfigurations success, data: ${JSON.stringify(data)}`);
9. }
10. });
```

## Context.isUpdatingConfigurations7+

PhonePC/2in1TabletTVWearable

isUpdatingConfigurations(): Promise<boolean>

检查此能力的配置是否正在更改。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回true表示该Ability的配置正在更改，否则返回false。 |

**示例：**

```
1. import featureAbility from '@ohos.ability.featureAbility';

3. let context: featureAbility.Context = featureAbility.getContext();
4. context.isUpdatingConfigurations().then((data) => {
5. console.info(`isUpdatingConfigurations data: ${JSON.stringify(data)}`);
6. });
```

## Context.printDrawnCompleted7+

PhonePC/2in1TabletTVWearable

printDrawnCompleted(callback: AsyncCallback<void>): void

通知系统绘制此页面功能所需的时间。使用callback异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当通知系统绘制此页面功能所需的时间成功，err为undefined，否则为错误对象。 |

**示例：**

```
1. import featureAbility from '@ohos.ability.featureAbility';

3. let context: featureAbility.Context = featureAbility.getContext();
4. context.printDrawnCompleted((err) => {
5. console.error(`printDrawnCompleted err: ${JSON.stringify(err)}`);
6. });
```

## Context.printDrawnCompleted7+

PhonePC/2in1TabletTVWearable

printDrawnCompleted(): Promise<void>

通知系统绘制此页面功能所需的时间。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. import featureAbility from '@ohos.ability.featureAbility';

3. let context: featureAbility.Context = featureAbility.getContext();
4. context.printDrawnCompleted().then((data) => {
5. console.info(`printDrawnCompleted data: ${JSON.stringify(data)}`);
6. });
```

## PermissionOptions7+

PhonePC/2in1TabletTVWearable

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| pid | number | 否 | 是 | 进程id。 |
| uid | number | 否 | 是 | 用户id。 |

## PermissionRequestResult7+

PhonePC/2in1TabletTVWearable

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| requestCode | number | 否 | 否 | 用户传入的请求代码。 |
| permissions | Array<string> | 否 | 否 | 用户传入的权限。 |
| authResults | Array<number> | 否 | 否 | 请求权限的结果。 |
