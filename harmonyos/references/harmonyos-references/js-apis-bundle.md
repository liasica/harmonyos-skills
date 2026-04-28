---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle
title: @ohos.bundle (Bundle模块)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 已停止维护的接口 > @ohos.bundle (Bundle模块)
category: harmonyos-references
scraped_at: 2026-04-28T07:58:51+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:96e5a40f59099b53e9043a6a0df2e6815f30c87d25b1f9f9b2d49f794f101eca
---

本模块提供应用信息查询能力，支持[包信息](js-apis-bundle-bundleinfo.md)、[应用信息](js-apis-bundle-applicationinfo.md)、[Ability组件信息](js-apis-bundle-abilityinfo.md)等信息的查询，以及应用禁用状态的查询、设置等。

说明

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

从API version 9开始，该模块不再维护，建议使用[@ohos.bundle.bundleManager](js-apis-bundlemanager.md)替代。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import bundle from '@ohos.bundle';
```

## 权限列表

PhonePC/2in1TabletTVWearable

| 权限 | 权限等级 | 描述 |
| --- | --- | --- |
| ohos.permission.GET\_BUNDLE\_INFO | normal | 查询指定应用信息。 |
| ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED | system\_basic | 可查询所有应用信息。 |

权限等级参考[权限APL等级说明](../harmonyos-guides/app-permission-mgmt-overview.md#权限机制中的基本概念)。

## bundle.getApplicationInfodeprecated

PhonePC/2in1TabletTVWearable

说明

从API version 7开始支持，从API version 9开始废弃，替代接口仅向系统应用开放。

getApplicationInfo(bundleName: string, bundleFlags: number, userId?: number): Promise<ApplicationInfo>

根据给定的Bundle名称获取ApplicationInfo。使用Promise异步回调。

获取调用方自己的信息时不需要权限。

**需要权限：**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED 或 ohos.permission.GET\_BUNDLE\_INFO

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleName | string | 是 | 要查询的应用Bundle名称。 |
| bundleFlags | number | 是 | 用于指定返回的应用信息对象中包含信息的标记。取值范围请参考[BundleFlag说明](js-apis-bundle.md#bundleflagdeprecated)中应用信息相关flag。 |
| userId | number | 否 | 用户ID。默认值：调用方所在用户，取值范围：大于等于0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ApplicationInfo](js-apis-bundle-applicationinfo.md)> | Promise形式返回应用程序信息。 |

**示例：**

```
1. import bundle from '@ohos.bundle';
2. import { BusinessError } from '@ohos.base';

4. let bundleName: string = "com.example.myapplication";
5. let bundleFlags: number = 0;
6. let userId: number = 100;

8. bundle.getApplicationInfo(bundleName, bundleFlags, userId)
9. .then((data) => {
10. console.info('Operation successful. Data: ' + JSON.stringify(data));
11. }).catch((error: BusinessError) => {
12. console.error('Operation failed. Cause: ' + JSON.stringify(error));
13. })
```

## bundle.getApplicationInfodeprecated

PhonePC/2in1TabletTVWearable

说明

从API version 7开始支持，从API version 9开始废弃，替代接口仅向系统应用开放。

getApplicationInfo(bundleName: string, bundleFlags: number, userId: number, callback: AsyncCallback<ApplicationInfo>): void

根据给定的Bundle名称获取指定用户下的ApplicationInfo，使用callback异步回调。

获取调用方自己的信息时不需要权限。

**需要权限：**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED 或 ohos.permission.GET\_BUNDLE\_INFO

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleName | string | 是 | 要查询的应用Bundle名称。 |
| bundleFlags | number | 是 | 用于指定返回的应用信息对象中包含信息的标记。取值范围：参考[BundleFlag说明](js-apis-bundle.md#bundleflagdeprecated)中应用信息相关flag。 |
| userId | number | 是 | 用户ID。取值范围：大于等于0。 |
| callback | AsyncCallback<[ApplicationInfo](js-apis-bundle-applicationinfo.md)> | 是 | 程序启动作为入参的回调函数，返回应用程序信息。 |

**示例：**

```
1. import bundle from '@ohos.bundle';

3. let bundleName: string = "com.example.myapplication";
4. let bundleFlags: number = 0;
5. let userId: number = 100;

7. bundle.getApplicationInfo(bundleName, bundleFlags, userId, (err, data) => {
8. if (err) {
9. console.error('Operation failed. Cause: ' + JSON.stringify(err));
10. return;
11. }
12. console.info('Operation successful. Data:' + JSON.stringify(data));
13. })
```

## bundle.getApplicationInfodeprecated

PhonePC/2in1TabletTVWearable

说明

从API version 7开始支持，从API version 9开始废弃，替代接口仅向系统应用开放。

getApplicationInfo(bundleName: string, bundleFlags: number, callback: AsyncCallback<ApplicationInfo>): void

根据给定的Bundle名称获取ApplicationInfo，使用callback异步回调。

获取调用方自己的信息时不需要权限。

**需要权限：**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED 或 ohos.permission.GET\_BUNDLE\_INFO

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleName | string | 是 | 要查询的应用Bundle名称。 |
| bundleFlags | number | 是 | 用于指定返回的应用信息对象中包含信息的标记。取值范围：参考[BundleFlag说明](js-apis-bundle.md#bundleflagdeprecated)中应用信息相关flag。 |
| callback | AsyncCallback<[ApplicationInfo](js-apis-bundle-applicationinfo.md)> | 是 | 程序启动作为入参的回调函数，返回应用程序信息。 |

**示例：**

```
1. import bundle from '@ohos.bundle';

3. let bundleName: string = "com.example.myapplication";
4. let bundleFlags: number = 0;

6. bundle.getApplicationInfo(bundleName, bundleFlags, (err, data) => {
7. if (err) {
8. console.error('Operation failed. Cause: ' + JSON.stringify(err));
9. return;
10. }
11. console.info('Operation successful. Data:' + JSON.stringify(data));
12. })
```

## bundle.getAllBundleInfodeprecated

PhonePC/2in1TabletTVWearable

说明

从API version 7开始支持，从API version 9开始废弃，替代接口仅向系统应用开放。

getAllBundleInfo(bundleFlag: BundleFlag, userId?: number): Promise<Array<BundleInfo>>

获取指定用户所有的BundleInfo，使用Promise形式异步回调。

**需要权限：**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleFlag | BundleFlag | 是 | 用于指定返回的包信息对象中包含信息的标记。取值范围：参考[BundleFlag说明](js-apis-bundle.md#bundleflagdeprecated)中包信息相关flag。 |
| userId | number | 否 | 用户ID。默认值：调用方所在用户，取值范围：大于等于0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[BundleInfo](js-apis-bundle-bundleinfo.md)>> | Promise形式返回所有可用的BundleInfo |

**示例：**

```
1. import bundle from '@ohos.bundle';
2. import { BusinessError } from '@ohos.base';

4. let bundleFlag: number = 0;
5. let userId: number = 100;

7. bundle.getAllBundleInfo(bundleFlag, userId)
8. .then((data) => {
9. console.info('Operation successful. Data: ' + JSON.stringify(data));
10. }).catch((error: BusinessError) => {
11. console.error('Operation failed. Cause: ' + JSON.stringify(error));
12. })
```

## bundle.getAllBundleInfodeprecated

PhonePC/2in1TabletTVWearable

说明

从API version 7开始支持，从API version 9开始废弃，替代接口仅向系统应用开放。

getAllBundleInfo(bundleFlag: BundleFlag, callback: AsyncCallback<Array<BundleInfo>>): void

获取当前用户所有的BundleInfo，使用callback异步回调。

**需要权限：**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleFlag | BundleFlag | 是 | 用于指定返回的应用信息对象中包含信息的标记。取值范围：参考[BundleFlag说明](js-apis-bundle.md#bundleflagdeprecated)中包信息相关flag。 |
| callback | AsyncCallback<Array<[BundleInfo](js-apis-bundle-bundleinfo.md)>> | 是 | 程序启动作为入参的回调函数，返回所有可用的BundleInfo。 |

**示例：**

```
1. import bundle from '@ohos.bundle';

3. let bundleFlag: number = 0;

5. bundle.getAllBundleInfo(bundleFlag, (err, data) => {
6. if (err) {
7. console.error('Operation failed. Cause: ' + JSON.stringify(err));
8. return;
9. }
10. console.info('Operation successful. Data:' + JSON.stringify(data));
11. })
```

## bundle.getAllBundleInfodeprecated

PhonePC/2in1TabletTVWearable

说明

从API version 7开始支持，从API version 9开始废弃，替代接口仅向系统应用开放。

getAllBundleInfo(bundleFlag: BundleFlag, userId: number, callback: AsyncCallback<Array<BundleInfo>>): void

获取系统中指定用户下所有的BundleInfo，使用callback异步回调。

**需要权限：**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleFlag | BundleFlag | 是 | 用于指定返回的应用信息对象中包含信息的标记。取值范围：参考[BundleFlag说明](js-apis-bundle.md#bundleflagdeprecated)中包信息相关flag。 |
| userId | number | 是 | 用户ID。默认值：调用方所在用户，取值范围：大于等于0。 |
| callback | AsyncCallback<Array<[BundleInfo](js-apis-bundle-bundleinfo.md)>> | 是 | 程序启动作为入参的回调函数，返回指定用户下所有包的BundleInfo。 |

**示例：**

```
1. import bundle from '@ohos.bundle';

3. let bundleFlag: number = 0;
4. let userId: number = 100;

6. bundle.getAllBundleInfo(bundleFlag, userId, (err, data) => {
7. if (err) {
8. console.error('Operation failed. Cause: ' + JSON.stringify(err));
9. return;
10. }
11. console.info('Operation successful. Data:' + JSON.stringify(data));
12. })
```

## bundle.getBundleInfodeprecated

PhonePC/2in1TabletTVWearable

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[getBundleInfo](js-apis-bundlemanager.md#bundlemanagergetbundleinfo14-2)替代。

getBundleInfo(bundleName: string, bundleFlags: number, options?: BundleOptions): Promise<BundleInfo>

根据给定的Bundle名称获取BundleInfo，使用Promise异步回调。

获取调用方自己的信息时不需要权限。

**需要权限：**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED 或 ohos.permission.GET\_BUNDLE\_INFO

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleName | string | 是 | 要查询的应用Bundle名称。 |
| bundleFlags | number | 是 | 用于指定返回的应用信息对象中包含信息的标记。取值范围：参考[BundleFlag说明](js-apis-bundle.md#bundleflagdeprecated)中包信息相关flag。 |
| options | [BundleOptions](js-apis-bundle.md#bundleoptionsdeprecated) | 否 | 包含userid的查询选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[BundleInfo](js-apis-bundle-bundleinfo.md)> | Promise对象，获取成功时返回包信息。 |

**示例：**

```
1. import bundle from '@ohos.bundle';
2. import { BusinessError } from '@ohos.base';

4. let bundleName: string = "com.example.myapplication";
5. let bundleFlags: number = 1;
6. let options: bundle.BundleOptions = {
7. "userId": 100
8. };

10. bundle.getBundleInfo(bundleName, bundleFlags, options)
11. .then((data) => {
12. console.info('Operation successful. Data: ' + JSON.stringify(data));
13. }).catch((error: BusinessError) => {
14. console.error('Operation failed. Cause: ' + JSON.stringify(error));
15. })
```

## bundle.getBundleInfodeprecated

PhonePC/2in1TabletTVWearable

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[getBundleInfo](js-apis-bundlemanager.md#bundlemanagergetbundleinfo14-1)替代。

getBundleInfo(bundleName: string, bundleFlags: number, callback: AsyncCallback<BundleInfo>): void

根据给定的Bundle名称获取BundleInfo，使用callback异步回调。

获取调用方自己的信息时不需要权限。

**需要权限：**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED 或 ohos.permission.GET\_BUNDLE\_INFO

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleName | string | 是 | 需要查询的应用Bundle名称。 |
| bundleFlags | number | 是 | 用于指定返回的应用信息对象中包含信息的标记。取值范围：参考[BundleFlag说明](js-apis-bundle.md#bundleflagdeprecated)中包信息相关flag。 |
| callback | AsyncCallback<[BundleInfo](js-apis-bundle-bundleinfo.md)> | 是 | 程序启动作为入参的回调函数，返回包信息。 |

**示例：**

```
1. import bundle from '@ohos.bundle';

3. let bundleName: string = "com.example.myapplication";
4. let bundleFlags: number = 1;

6. bundle.getBundleInfo(bundleName, bundleFlags, (err, data) => {
7. if (err) {
8. console.error('Operation failed. Cause: ' + JSON.stringify(err));
9. return;
10. }
11. console.info('Operation successful. Data:' + JSON.stringify(data));
12. })
```

## bundle.getBundleInfodeprecated

PhonePC/2in1TabletTVWearable

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[getBundleInfo](js-apis-bundlemanager.md#bundlemanagergetbundleinfo14)替代。

getBundleInfo(bundleName: string, bundleFlags: number, options: BundleOptions, callback: AsyncCallback<BundleInfo>): void

根据给定的Bundle名称获取BundleInfo，使用callback异步回调。

获取调用方自己的信息时不需要权限。

**需要权限：**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED 或 ohos.permission.GET\_BUNDLE\_INFO

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleName | string | 是 | 要查询的应用Bundle名称。 |
| bundleFlags | number | 是 | 用于指定返回的应用信息对象中包含信息的标记。取值范围：参考[BundleFlag说明](js-apis-bundle.md#bundleflagdeprecated)中包信息相关flag。 |
| options | [BundleOptions](js-apis-bundle.md#bundleoptionsdeprecated) | 是 | 包含userid。 |
| callback | AsyncCallback<[BundleInfo](js-apis-bundle-bundleinfo.md)> | 是 | 程序启动作为入参的回调函数，返回包信息。 |

**示例：**

```
1. import bundle from '@ohos.bundle';

3. let bundleName: string = "com.example.myapplication";
4. let bundleFlags: number = 1;
5. let options: bundle.BundleOptions = {
6. "userId": 100
7. };

9. bundle.getBundleInfo(bundleName, bundleFlags, options, (err, data) => {
10. if (err) {
11. console.error('Operation failed. Cause: ' + JSON.stringify(err));
12. return;
13. }
14. console.info('Operation successful. Data:' + JSON.stringify(data));
15. })
```

## bundle.getAllApplicationInfodeprecated

PhonePC/2in1TabletTVWearable

说明

从API version 7开始支持，从API version 9开始废弃，替代接口仅向系统应用开放。

getAllApplicationInfo(bundleFlags: number, userId?: number): Promise<Array<ApplicationInfo>>

获取指定用户下所有已安装的应用信息，使用promise异步回调。

**需要权限：**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleFlags | number | 是 | 用于指定返回的应用信息对象中包含信息的标记。取值范围：参考[BundleFlag说明](js-apis-bundle.md#bundleflagdeprecated)中应用信息相关flag。 |
| userId | number | 否 | 用户ID。默认值：调用方所在用户，取值范围：大于等于0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[ApplicationInfo](js-apis-bundle-applicationinfo.md)>> | Promise对象，获取成功时返回应用信息列表。 |

**示例：**

```
1. import bundle from '@ohos.bundle';
2. import { BusinessError } from '@ohos.base';

4. let bundleFlags: number = 8;
5. let userId: number = 100;

7. bundle.getAllApplicationInfo(bundleFlags, userId)
8. .then((data) => {
9. console.info('Operation successful. Data: ' + JSON.stringify(data));
10. }).catch((error: BusinessError) => {
11. console.error('Operation failed. Cause: ' + JSON.stringify(error));
12. })
```

## bundle.getAllApplicationInfodeprecated

PhonePC/2in1TabletTVWearable

说明

从API version 7开始支持，从API version 9开始废弃，替代接口仅向系统应用开放。

getAllApplicationInfo(bundleFlags: number, userId: number, callback: AsyncCallback<Array<ApplicationInfo>>): void

获取指定用户下所有已安装的应用信息，使用callback异步回调。

**需要权限：**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleFlags | number | 是 | 用于指定返回的应用信息对象中包含信息的标记。取值范围：参考[BundleFlag说明](js-apis-bundle.md#bundleflagdeprecated)中应用信息相关flag。 |
| userId | number | 是 | 用户ID。默认值：调用方所在用户，取值范围：大于等于0。 |
| callback | AsyncCallback<Array<[ApplicationInfo](js-apis-bundle-applicationinfo.md)>> | 是 | 程序启动作为入参的回调函数，返回应用信息列表。 |

**示例：**

```
1. import bundle from '@ohos.bundle';

3. let bundleFlags: number = bundle.BundleFlag.GET_APPLICATION_INFO_WITH_PERMISSION;
4. let userId: number = 100;

6. bundle.getAllApplicationInfo(bundleFlags, userId, (err, data) => {
7. if (err) {
8. console.error('Operation failed. Cause: ' + JSON.stringify(err));
9. return;
10. }
11. console.info('Operation successful. Data:' + JSON.stringify(data));
12. })
```

## bundle.getAllApplicationInfodeprecated

PhonePC/2in1TabletTVWearable

说明

从API version 7开始支持，从API version 9开始废弃，替代接口仅向系统应用开放。

getAllApplicationInfo(bundleFlags: number, callback: AsyncCallback<Array<ApplicationInfo>>): void

获取调用方所在用户下已安装的应用信息，使用callback异步回调。

**需要权限：**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleFlags | number | 是 | 用于指定返回的应用信息对象中包含信息的标记。取值范围：参考[BundleFlag说明](js-apis-bundle.md#bundleflagdeprecated)中应用信息相关flag。 |
| callback | AsyncCallback<Array<[ApplicationInfo](js-apis-bundle-applicationinfo.md)>> | 是 | 程序启动作为入参的回调函数，返回应用信息列表。 |

**示例：**

```
1. import bundle from '@ohos.bundle';

3. let bundleFlags: number = bundle.BundleFlag.GET_APPLICATION_INFO_WITH_PERMISSION;

5. bundle.getAllApplicationInfo(bundleFlags, (err, data) => {
6. if (err) {
7. console.error('Operation failed. Cause: ' + JSON.stringify(err));
8. return;
9. }
10. console.info('Operation successful. Data:' + JSON.stringify(data));
11. })
```

## bundle.getBundleArchiveInfodeprecated

PhonePC/2in1TabletTVWearable

说明

从API version 7开始支持，从API version 9开始废弃，替代接口仅向系统应用开放。

getBundleArchiveInfo(hapFilePath: string, bundleFlags: number) : Promise<BundleInfo>

获取有关HAP中包含的应用程序包的信息，使用Promise异步回调。

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| hapFilePath | string | 是 | HAP存放路径。支持当前应用程序的绝对路径和数据目录沙箱路径。 |
| bundleFlags | number | 是 | 用于指定要返回的BundleInfo对象中包含信息的标记。取值范围：参考[BundleFlag说明](js-apis-bundle.md#bundleflagdeprecated)中包信息相关flag。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[BundleInfo](js-apis-bundle-bundleinfo.md)> | 返回值为Promise对象，Promise中包含有关HAP中包含的应用程序的信息。 |

**示例：**

```
1. import bundle from '@ohos.bundle';
2. import { BusinessError } from '@ohos.base';

4. let hapFilePath: string = "/data/storage/el2/base/test.hap";
5. let bundleFlags: number = 0;

7. bundle.getBundleArchiveInfo(hapFilePath, bundleFlags)
8. .then((data) => {
9. console.info('Operation successful. Data: ' + JSON.stringify(data));
10. }).catch((error: BusinessError) => {
11. console.error('Operation failed. Cause: ' + JSON.stringify(error));
12. })
```

## bundle.getBundleArchiveInfodeprecated

PhonePC/2in1TabletTVWearable

说明

从API version 7开始支持，从API version 9开始废弃，替代接口仅向系统应用开放。

getBundleArchiveInfo(hapFilePath: string, bundleFlags: number, callback: AsyncCallback<BundleInfo>) : void

获取有关HAP中包含的应用程序包的信息，使用callback异步回调。

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| hapFilePath | string | 是 | HAP存放路径，支持当前应用程序的绝对路径和数据目录沙箱路径。 |
| bundleFlags | number | 是 | 用于指定要返回的BundleInfo对象中包含信息的标记。取值范围：参考[BundleFlag说明](js-apis-bundle.md#bundleflagdeprecated)中包信息相关flag。 |
| callback | AsyncCallback<[BundleInfo](js-apis-bundle-bundleinfo.md)> | 是 | 程序启动作为入参的回调函数，返回HAP中包含的应用程序包的信息。 |

**示例：**

```
1. import bundle from '@ohos.bundle';

3. let hapFilePath: string = "/data/storage/el2/base/test.hap";
4. let bundleFlags: number = 0;

6. bundle.getBundleArchiveInfo(hapFilePath, bundleFlags, (err, data) => {
7. if (err) {
8. console.error('Operation failed. Cause: ' + JSON.stringify(err));
9. return;
10. }
11. console.info('Operation successful. Data:' + JSON.stringify(data));
12. })
```

## bundle.getAbilityInfodeprecated

PhonePC/2in1TabletTVWearable

说明

从API version 7开始支持，从API version 9开始废弃，替代接口仅向系统应用开放。

getAbilityInfo(bundleName: string, abilityName: string): Promise<AbilityInfo>

通过Bundle名称和组件名获取Ability组件信息，使用Promise形式异步回调。

获取调用方自己的信息时不需要权限。

**需要权限：**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED 或 ohos.permission.GET\_BUNDLE\_INFO

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleName | string | 是 | 应用Bundle名称。 |
| abilityName | string | 是 | Ability组件名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AbilityInfo](js-apis-bundle-abilityinfo.md)> | Promise形式返回Ability信息。 |

**示例：**

```
1. import bundle from '@ohos.bundle';
2. import { BusinessError } from '@ohos.base';

4. let bundleName: string = "com.example.myapplication";
5. let abilityName: string = "EntryAbility";

7. bundle.getAbilityInfo(bundleName, abilityName)
8. .then((data) => {
9. console.info('Operation successful. Data: ' + JSON.stringify(data));
10. }).catch((error: BusinessError) => {
11. console.error('Operation failed. Cause: ' + JSON.stringify(error));
12. })
```

## bundle.getAbilityInfodeprecated

PhonePC/2in1TabletTVWearable

说明

从API version 7开始支持，从API version 9开始废弃，替代接口仅向系统应用开放。

getAbilityInfo(bundleName: string, abilityName: string, callback: AsyncCallback<AbilityInfo>): void

通过Bundle名称和组件名获取Ability组件信息，使用callback异步回调。

获取调用方自己的信息时不需要权限。

**需要权限：**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED 或 ohos.permission.GET\_BUNDLE\_INFO

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleName | string | 是 | 应用Bundle名称。 |
| abilityName | string | 是 | Ability名称。 |
| callback | AsyncCallback<[AbilityInfo](js-apis-bundle-abilityinfo.md)> | 是 | 程序启动作为入参的回调函数，返回Ability信息。 |

**示例：**

```
1. import bundle from '@ohos.bundle';

3. let bundleName: string = "com.example.myapplication";
4. let abilityName: string = "EntryAbility";

6. bundle.getAbilityInfo(bundleName, abilityName, (err, data) => {
7. if (err) {
8. console.error('Operation failed. Cause: ' + JSON.stringify(err));
9. return;
10. }
11. console.info('Operation successful. Data:' + JSON.stringify(data));
12. })
```

## bundle.getAbilityLabel8+ deprecated

PhonePC/2in1TabletTVWearable

说明

从API version 8开始支持，从API version 9开始废弃，替代接口仅向系统应用开放。

getAbilityLabel(bundleName: string, abilityName: string): Promise<string>

通过Bundle名称和ability名称获取应用名称，使用Promise异步回调。

获取调用方自己的信息时不需要权限。

**需要权限：**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED 或 ohos.permission.GET\_BUNDLE\_INFO

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleName | string | 是 | 应用Bundle名称。 |
| abilityName | string | 是 | Ability名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise形式返回应用名称信息。 |

**示例：**

```
1. import bundle from '@ohos.bundle';
2. import { BusinessError } from '@ohos.base';

4. let bundleName: string = "com.example.myapplication";
5. let abilityName: string = "EntryAbility";

7. bundle.getAbilityLabel(bundleName, abilityName)
8. .then((data) => {
9. console.info('Operation successful. Data: ' + JSON.stringify(data));
10. }).catch((error: BusinessError) => {
11. console.error('Operation failed. Cause: ' + JSON.stringify(error));
12. })
```

## bundle.getAbilityLabel8+ deprecated

PhonePC/2in1TabletTVWearable

说明

从API version 8开始支持，从API version 9开始废弃，替代接口仅向系统应用开放。

getAbilityLabel(bundleName: string, abilityName: string, callback : AsyncCallback<string>): void

通过Bundle名称和Ability组件名获取应用名称，使用callback异步回调。

获取调用方自己的信息时不需要权限。

**需要权限：**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED 或 ohos.permission.GET\_BUNDLE\_INFO

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleName | string | 是 | 应用Bundle名称。 |
| abilityName | string | 是 | Ability名称。 |
| callback | AsyncCallback<string> | 是 | 程序启动作为入参的回调函数，返回应用名称信息。 |

**示例：**

```
1. import bundle from '@ohos.bundle';

3. let bundleName: string = "com.example.myapplication";
4. let abilityName: string = "EntryAbility";

6. bundle.getAbilityLabel(bundleName, abilityName, (err, data) => {
7. if (err) {
8. console.error('Operation failed. Cause: ' + JSON.stringify(err));
9. return;
10. }
11. console.info('Operation successful. Data:' + JSON.stringify(data));
12. })
```

## bundle.isAbilityEnabled8+ deprecated

PhonePC/2in1TabletTVWearable

说明

从API version 8开始支持，从API version 9开始废弃，替代接口仅向系统应用开放。

isAbilityEnabled(info: AbilityInfo): Promise<boolean>

根据给定的AbilityInfo查询ability是否已经启用，使用Promise异步回调。

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| info | [AbilityInfo](js-apis-bundle-abilityinfo.md) | 是 | Ability的配置信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise形式返回boolean代表是否启用。 |

**示例：**

```
1. import bundle from '@ohos.bundle';
2. import { BusinessError } from '@ohos.base';

4. let bundleName: string = "com.example.myapplication";
5. let abilityName: string = "EntryAbility";

7. bundle.getAbilityInfo(bundleName, abilityName).then((abilityInfo) => {
8. bundle.isAbilityEnabled(abilityInfo).then((data) => {
9. console.info('Operation successful. Data: ' + JSON.stringify(data));
10. }).catch((error: BusinessError) => {
11. console.error('Operation failed. Cause: ' + JSON.stringify(error));
12. })
13. })
```

## bundle.isAbilityEnabled8+ deprecated

PhonePC/2in1TabletTVWearable

说明

从API version 8开始支持，从API version 9开始废弃，替代接口仅向系统应用开放。

isAbilityEnabled(info : AbilityInfo, callback : AsyncCallback<boolean>): void

根据给定的AbilityInfo查询ability是否已经启用，使用callback异步回调。

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| info | [AbilityInfo](js-apis-bundle-abilityinfo.md) | 是 | Ability的配置信息。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数，返回boolean代表是否启用。 |

**示例：**

```
1. import bundle from '@ohos.bundle';

3. let bundleName: string = "com.example.myapplication";
4. let abilityName: string = "EntryAbility";

6. bundle.getAbilityInfo(bundleName, abilityName).then((abilityInfo) => {
7. bundle.isAbilityEnabled(abilityInfo, (err, data) => {
8. if (err) {
9. console.error('Operation failed. Cause: ' + JSON.stringify(err));
10. return;
11. }
12. console.info('Operation successful. Data:' + JSON.stringify(data));
13. })
14. })
```

## bundle.isApplicationEnabled8+ deprecated

PhonePC/2in1TabletTVWearable

说明

从API version 8开始支持，从API version 9开始废弃，替代接口仅向系统应用开放。

isApplicationEnabled(bundleName: string): Promise<boolean>

根据给定的bundleName查询指定应用程序是否已经启用，使用Promise异步回调。

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleName | string | 是 | 要查询的应用Bundle名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise形式返回boolean代表是否启用。 |

**示例：**

```
1. import bundle from '@ohos.bundle';
2. import { BusinessError } from '@ohos.base';

4. let bundleName: string = "com.example.myapplication";

6. bundle.isApplicationEnabled(bundleName)
7. .then((data) => {
8. console.info('Operation successful. Data: ' + JSON.stringify(data));
9. }).catch((error: BusinessError) => {
10. console.error('Operation failed. Cause: ' + JSON.stringify(error));
11. })
```

## bundle.isApplicationEnabled8+ deprecated

PhonePC/2in1TabletTVWearable

说明

从API version 8开始支持，从API version 9开始废弃，替代接口仅向系统应用开放。

isApplicationEnabled(bundleName: string, callback : AsyncCallback<boolean>): void

根据给定的bundleName查询指定应用程序是否已经启用，使用callback异步回调。

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleName | string | 是 | 要查询的应用Bundle名称。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数，返回boolean代表是否启用。 |

**示例：**

```
1. import bundle from '@ohos.bundle';

3. let bundleName: string = "com.example.myapplication";

5. bundle.isApplicationEnabled(bundleName, (err, data) => {
6. if (err) {
7. console.error('Operation failed. Cause: ' + JSON.stringify(err));
8. return;
9. }
10. console.info('Operation successful. Data:' + JSON.stringify(data));
11. })
```

## bundle.queryAbilityByWantdeprecated

PhonePC/2in1TabletTVWearable

说明

从API version 7开始支持，从API version 9开始废弃，替代接口仅向系统应用开放。

queryAbilityByWant(want: Want, bundleFlags: number, userId?: number): Promise<Array<AbilityInfo>>

根据给定的意图获取Ability组件信息，使用Promise异步回调。

获取调用方自己的信息时不需要权限。

**需要权限：**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED 或 ohos.permission.GET\_BUNDLE\_INFO

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-application-want.md) | 是 | 包含要查询的应用Bundle名称的意图。 |
| bundleFlags | number | 是 | 用于指定返回abilityInfo信息。取值范围：参考[BundleFlag说明](js-apis-bundle.md#bundleflagdeprecated)中Ability信息相关flag。 |
| userId | number | 否 | 用户ID。默认值：调用方所在用户，取值范围：大于等于0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[AbilityInfo](js-apis-bundle-abilityinfo.md)>> | Promise形式返回Ability信息。 |

**示例：**

```
1. import bundle from '@ohos.bundle';
2. import { BusinessError } from '@ohos.base';
3. import Want from '@ohos.app.ability.Want';

5. let bundleFlags: number = 0;
6. let userId: number = 100;
7. let want: Want = {
8. bundleName: "com.example.myapplication",
9. abilityName: "EntryAbility"
10. };

12. bundle.queryAbilityByWant(want, bundleFlags, userId)
13. .then((data) => {
14. console.info('Operation successful. Data: ' + JSON.stringify(data));
15. }).catch((error: BusinessError) => {
16. console.error('Operation failed. Cause: ' + JSON.stringify(error));
17. })
```

## bundle.queryAbilityByWantdeprecated

PhonePC/2in1TabletTVWearable

说明

从API version 7开始支持，从API version 9开始废弃，替代接口仅向系统应用开放。

queryAbilityByWant(want: Want, bundleFlags: number, userId: number, callback: AsyncCallback<Array<AbilityInfo>>): void

根据给定的意图获取指定用户下Ability信息，使用callback异步回调。

获取调用方自己的信息时不需要权限。

**需要权限：**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED 或 ohos.permission.GET\_BUNDLE\_INFO

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-application-want.md) | 是 | 指示包含要查询的应用Bundle名称的意图。 |
| bundleFlags | number | 是 | 用于指定返回abilityInfo信息。取值范围：参考[BundleFlag说明](js-apis-bundle.md#bundleflagdeprecated)中Ability信息相关flag。 |
| userId | number | 是 | 用户ID。取值范围：大于等于0。 |
| callback | AsyncCallback<Array<[AbilityInfo](js-apis-bundle-abilityinfo.md)>> | 是 | 程序启动作为入参的回调函数，返回Ability信息。 |

**示例：**

```
1. import bundle from '@ohos.bundle';
2. import Want from '@ohos.app.ability.Want';

4. let bundleFlags: number = 0;
5. let userId: number = 100;
6. let want: Want = {
7. bundleName: "com.example.myapplication",
8. abilityName: "EntryAbility"
9. };

11. bundle.queryAbilityByWant(want, bundleFlags, userId, (err, data) => {
12. if (err) {
13. console.error('Operation failed. Cause: ' + JSON.stringify(err));
14. return;
15. }
16. console.info('Operation successful. Data:' + JSON.stringify(data));
17. })
```

## bundle.queryAbilityByWantdeprecated

PhonePC/2in1TabletTVWearable

说明

从API version 7开始支持，从API version 9开始废弃，替代接口仅向系统应用开放。

queryAbilityByWant(want: Want, bundleFlags: number, callback: AsyncCallback<Array<AbilityInfo>>): void

根据给定的意图获取Ability信息，使用callback异步回调。

获取调用方自己的信息时不需要权限。

**需要权限：**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED 或 ohos.permission.GET\_BUNDLE\_INFO

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-application-want.md) | 是 | 指示包含要查询的应用Bundle名称的意图。 |
| bundleFlags | number | 是 | 用于指定返回abilityInfo信息。取值范围：参考[BundleFlag说明](js-apis-bundle.md#bundleflagdeprecated)中Ability信息相关flag。 |
| callback | AsyncCallback<Array<[AbilityInfo](js-apis-bundle-abilityinfo.md)>> | 是 | 程序启动作为入参的回调函数，返回Ability信息。 |

**示例：**

```
1. import bundle from '@ohos.bundle';
2. import Want from '@ohos.app.ability.Want';

4. let bundleFlags: number = 0;
5. let want: Want = {
6. bundleName: "com.example.myapplication",
7. abilityName: "EntryAbility"
8. };

10. bundle.queryAbilityByWant(want, bundleFlags, (err, data) => {
11. if (err) {
12. console.error('Operation failed. Cause: ' + JSON.stringify(err));
13. return;
14. }
15. console.info('Operation successful. Data:' + JSON.stringify(data));
16. })
```

## bundle.getLaunchWantForBundledeprecated

PhonePC/2in1TabletTVWearable

说明

从API version 7开始支持，从API version 9开始废弃，替代接口仅向系统应用开放。

getLaunchWantForBundle(bundleName: string): Promise<Want>

查询拉起指定应用的want对象，使用Promise异步回调。

**需要权限：**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleName | string | 是 | 要查询的应用Bundle名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Want](js-apis-application-want.md)> | 返回值为Promise对象，Promise中包含拉起指定应用的Want对象。 |

**示例：**

```
1. import bundle from '@ohos.bundle';
2. import { BusinessError } from '@ohos.base';

4. let bundleName: string = "com.example.myapplication";

6. bundle.getLaunchWantForBundle(bundleName)
7. .then((data) => {
8. console.info('Operation successful. Data: ' + JSON.stringify(data));
9. }).catch((error: BusinessError) => {
10. console.error('Operation failed. Cause: ' + JSON.stringify(error));
11. })
```

## bundle.getLaunchWantForBundledeprecated

PhonePC/2in1TabletTVWearable

说明

从API version 7开始支持，从API version 9开始废弃，替代接口仅向系统应用开放。

getLaunchWantForBundle(bundleName: string, callback: AsyncCallback<Want>): void

查询拉起指定应用的want对象，使用callback异步回调。

**需要权限：**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleName | string | 是 | 要查询的应用Bundle名称。 |
| callback | AsyncCallback<[Want](js-apis-application-want.md)> | 是 | 程序启动作为入参的回调函数，返回拉起指定应用的want对象。 |

**示例：**

```
1. import bundle from '@ohos.bundle';

3. let bundleName: string = "com.example.myapplication";

5. bundle.getLaunchWantForBundle(bundleName, (err, data) => {
6. if (err) {
7. console.error('Operation failed. Cause: ' + JSON.stringify(err));
8. return;
9. }
10. console.info('Operation successful. Data:' + JSON.stringify(data));
11. })
```

## bundle.getNameForUid8+ deprecated

PhonePC/2in1TabletTVWearable

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[getBundleNameByUid](js-apis-bundlemanager.md#bundlemanagergetbundlenamebyuid14-1)替代。

getNameForUid(uid: number): Promise<string>

通过uid获取对应的Bundle名称，使用Promise异步回调。

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uid | number | 是 | 要查询的uid。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | 返回值为Promise对象，Promise中包含指定uid的Bundle名称。 |

**示例：**

```
1. import bundle from '@ohos.bundle';
2. import { BusinessError } from '@ohos.base';

4. let uid: number = 20010005;

6. bundle.getNameForUid(uid)
7. .then((data) => {
8. console.info('Operation successful. Data: ' + JSON.stringify(data));
9. }).catch((error: BusinessError) => {
10. console.error('Operation failed. Cause: ' + JSON.stringify(error));
11. })
```

## bundle.8+ deprecated

PhonePC/2in1TabletTVWearable

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[getBundleNameByUid](js-apis-bundlemanager.md#bundlemanagergetbundlenamebyuid14)替代。

getNameForUid(uid: number, callback: AsyncCallback<string>) : void

通过uid获取对应的Bundle名称，使用callback异步回调。

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uid | number | 是 | 要查询的uid。 |
| callback | AsyncCallback<string> | 是 | 程序启动作为入参的回调函数，返回指定uid的Bundle名称。 |

**示例：**

```
1. import bundle from '@ohos.bundle';

3. let uid: number = 20010005;

5. bundle.getNameForUid(uid, (err, data) => {
6. if (err) {
7. console.error('Operation failed. Cause: ' + JSON.stringify(err));
8. return;
9. }
10. console.info('Operation successful. Data:' + JSON.stringify(data));
11. })
```

## bundle.getAbilityIcon8+ deprecated

PhonePC/2in1TabletTVWearable

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[resourceManager.getMediaContent](js-apis-resource-manager.md#getmediacontent9)替代。

getAbilityIcon(bundleName: string, abilityName: string): Promise<image.PixelMap>

通过bundleName和abilityName获取对应Icon的[PixelMap](arkts-apis-image-pixelmap.md)，使用Promise异步回调。

获取调用方自己的信息时不需要权限。

**需要权限：**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED 或 ohos.permission.GET\_BUNDLE\_INFO

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleName | string | 是 | 要查询的应用Bundle名称。 |
| abilityName | string | 是 | 要查询的Ability组件名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<image.PixelMap> | 返回值为[PixelMap](arkts-apis-image-pixelmap.md)。 |

**示例：**

```
1. import bundle from '@ohos.bundle';
2. import { BusinessError } from '@ohos.base';

4. let bundleName: string = "com.example.myapplication";
5. let abilityName: string = "EntryAbility";

7. bundle.getAbilityIcon(bundleName, abilityName)
8. .then((data) => {
9. console.info('Operation successful. Data: ' + JSON.stringify(data));
10. }).catch((error: BusinessError) => {
11. console.error('Operation failed. Cause: ' + JSON.stringify(error));
12. })
```

## bundle.getAbilityIcon8+ deprecated

PhonePC/2in1TabletTVWearable

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[resourceManager.getMediaContent](js-apis-resource-manager.md#getmediacontent9)替代。

getAbilityIcon(bundleName: string, abilityName: string, callback: AsyncCallback<image.PixelMap>): void

通过bundleName和abilityName获取对应Icon的[PixelMap](arkts-apis-image-pixelmap.md)，使用callback异步回调。

获取调用方自己的信息时不需要权限。

**需要权限：**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED 或 ohos.permission.GET\_BUNDLE\_INFO

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleName | string | 是 | 要查询的应用Bundle名称。 |
| abilityName | string | 是 | 要查询的Ability组件名。 |
| callback | AsyncCallback<image.PixelMap> | 是 | 程序启动作为入参的回调函数，返回指定[PixelMap](arkts-apis-image-pixelmap.md)。 |

**示例：**

```
1. import bundle from '@ohos.bundle';

3. let bundleName: string = "com.example.myapplication";
4. let abilityName: string = "EntryAbility";

6. bundle.getAbilityIcon(bundleName, abilityName, (err, data) => {
7. if (err) {
8. console.error('Operation failed. Cause: ' + JSON.stringify(err));
9. return;
10. }
11. console.info('Operation successful. Data:' + JSON.stringify(data));
12. })
```

## InstallErrorCodedeprecated

PhonePC/2in1TabletTVWearable

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[包管理子系统通用错误码](errorcode-bundle.md)替代。

**系统能力：** SystemCapability.BundleManager.BundleFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SUCCESS | 0 | 安装成功。 |
| STATUS\_INSTALL\_FAILURE | 1 | 安装失败（不存在安装的应用）。 |
| STATUS\_INSTALL\_FAILURE\_ABORTED | 2 | 安装中止。 |
| STATUS\_INSTALL\_FAILURE\_INVALID | 3 | 安装参数无效。 |
| STATUS\_INSTALL\_FAILURE\_CONFLICT | 4 | 安装冲突 （常见于升级和已有应用基本信息不一致）。 |
| STATUS\_INSTALL\_FAILURE\_STORAGE | 5 | 存储包信息失败。 |
| STATUS\_INSTALL\_FAILURE\_INCOMPATIBLE | 6 | 安装不兼容（常见于版本降级安装或者签名信息错误）。 |
| STATUS\_UNINSTALL\_FAILURE | 7 | 卸载失败 （不存在卸载的应用）。 |
| STATUS\_UNINSTALL\_FAILURE\_BLOCKED | 8 | 卸载中止 （没有使用）。 |
| STATUS\_UNINSTALL\_FAILURE\_ABORTED | 9 | 卸载中止 （参数无效导致）。 |
| STATUS\_UNINSTALL\_FAILURE\_CONFLICT | 10 | 卸载冲突 （卸载系统应用失败， 结束应用进程失败）。 |
| STATUS\_INSTALL\_FAILURE\_DOWNLOAD\_TIMEOUT | 0x0B | 安装失败 （下载超时）。 |
| STATUS\_INSTALL\_FAILURE\_DOWNLOAD\_FAILED | 0x0C | 安装失败 （下载失败）。 |
| STATUS\_RECOVER\_FAILURE\_INVALID8+ | 0x0D | 恢复预置应用失败。 |
| STATUS\_ABILITY\_NOT\_FOUND | 0x40 | Ability未找到。 |
| STATUS\_BMS\_SERVICE\_ERROR | 0x41 | BMS服务错误。 |
| STATUS\_FAILED\_NO\_SPACE\_LEFT8+ | 0x42 | 设备空间不足。 |
| STATUS\_GRANT\_REQUEST\_PERMISSIONS\_FAILED8+ | 0x43 | 应用授权失败。 |
| STATUS\_INSTALL\_PERMISSION\_DENIED8+ | 0x44 | 缺少安装权限。 |
| STATUS\_UNINSTALL\_PERMISSION\_DENIED8+ | 0x45 | 缺少卸载权限。 |

## BundleFlagdeprecated

PhonePC/2in1TabletTVWearable

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[bundleManager.BundleFlag](js-apis-bundlemanager.md#bundleflag)替代。

包信息标志，指示需要获取的包信息的内容。

当接口与标志不匹配时，该标志会被忽略，例如获取application时使用GET\_ABILITY\_INFO\_WITH\_PERMISSION对结果不会产生影响。

标志可以叠加使用，例如使用GET\_APPLICATION\_INFO\_WITH\_PERMISSION + GET\_APPLICATION\_INFO\_WITH\_DISABLE可以使结果同时包含应用权限信息和被禁用的应用信息。

**系统能力：** SystemCapability.BundleManager.BundleFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| GET\_BUNDLE\_DEFAULT | 0x00000000 | 获取默认的应用信息。 |
| GET\_BUNDLE\_WITH\_ABILITIES | 0x00000001 | 获取包括Ability信息的包信息。 |
| GET\_ABILITY\_INFO\_WITH\_PERMISSION | 0x00000002 | 获取包括权限的Ability信息。 |
| GET\_ABILITY\_INFO\_WITH\_APPLICATION | 0x00000004 | 获取包括Application的ability信息。 |
| GET\_APPLICATION\_INFO\_WITH\_PERMISSION | 0x00000008 | 获取包括权限的应用信息。 |
| GET\_BUNDLE\_WITH\_REQUESTED\_PERMISSION | 0x00000010 | 获取包括所需权限的包信息。 |
| GET\_ABILITY\_INFO\_WITH\_METADATA8+ | 0x00000020 | 获取ability的元数据信息。 |
| GET\_APPLICATION\_INFO\_WITH\_METADATA8+ | 0x00000040 | 获取应用的元数据信息。 |
| GET\_ABILITY\_INFO\_SYSTEMAPP\_ONLY8+ | 0x00000080 | 获取仅包括系统应用的ability信息。 |
| GET\_ABILITY\_INFO\_WITH\_DISABLE8+ | 0x00000100 | 获取包括被禁用的ability信息。 |
| GET\_APPLICATION\_INFO\_WITH\_DISABLE8+ | 0x00000200 | 获取包括被禁用的应用信息。 |
| GET\_ALL\_APPLICATION\_INFO | 0xFFFF0000 | 获取应用所有的信息。 |

## BundleOptionsdeprecated

PhonePC/2in1TabletTVWearable

说明

从API version 7开始支持，从API version 9开始废弃，暂无替代接口。

查询选项，包含userId。

**系统能力：** SystemCapability.BundleManager.BundleFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| userId | number | 否 | 是 | 用户ID。默认值：调用方所在用户，取值范围：大于等于0。 |

## AbilityTypedeprecated

PhonePC/2in1TabletTVWearable

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[bundleManager.AbilityType](js-apis-bundlemanager.md#abilitytype)替代。

Ability组件类型。

**系统能力：** SystemCapability.BundleManager.BundleFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNKNOWN | 无 | 未知Ability类型。 |
| PAGE | 无 | 表示基于Page模板开发的FA，用于提供与用户交互的能力。 |
| SERVICE | 无 | 表示基于Service模板开发的PA，用于提供后台运行任务的能力。 |
| DATA | 无 | 表示基于Data模板开发的PA，用于对外部提供统一的数据访问对象。 |

## DisplayOrientationdeprecated

PhonePC/2in1TabletTVWearable

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[bundleManager.DisplayOrientation](js-apis-bundlemanager.md#displayorientation)替代。

屏幕显示方向。

**系统能力：** SystemCapability.BundleManager.BundleFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNSPECIFIED | 无 | 屏幕方向--不指定。 |
| LANDSCAPE | 无 | 屏幕方向--横屏。 |
| PORTRAIT | 无 | 屏幕方向--竖屏。 |
| FOLLOW\_RECENT | 无 | 屏幕方向--紧跟上一个组件。 |

## LaunchModedeprecated

PhonePC/2in1TabletTVWearable

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[bundleManager.LaunchType](js-apis-bundlemanager.md#launchtype)替代。

Ability组件的启动模式。

**系统能力：** SystemCapability.BundleManager.BundleFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SINGLETON | 0 | Ability只有一个实例。 |
| STANDARD | 1 | Ability有多个实例。 |

## AbilitySubTypedeprecated

PhonePC/2in1TabletTVWearable

说明

从API version 7开始支持，从API version 9开始废弃，暂无替代接口。

Ability组件的子类型。

**系统能力：** SystemCapability.BundleManager.BundleFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNSPECIFIED | 0 | 未定义Ability子类型。 |
| CA | 1 | Ability子类型是带有 UI 的服务。 |

## ColorModedeprecated

PhonePC/2in1TabletTVWearable

说明

从API version 7开始支持，从API version 9开始废弃，暂无替代接口。

应用、卡片等的颜色模式。

**系统能力：** SystemCapability.BundleManager.BundleFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| AUTO\_MODE | -1 | 自动模式。 |
| DARK\_MODE | 0 | 黑色模式。 |
| LIGHT\_MODE | 1 | 亮度模式。 |

## GrantStatusdeprecated

PhonePC/2in1TabletTVWearable

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[bundleManager.PermissionGrantState](js-apis-bundlemanager.md#permissiongrantstate)替代。

权限授予状态。

**系统能力：** SystemCapability.BundleManager.BundleFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PERMISSION\_DENIED | -1 | 拒绝授予权限。 |
| PERMISSION\_GRANTED | 0 | 授予权限。 |
