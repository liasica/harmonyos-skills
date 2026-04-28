---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-preferences
title: @ohos.data.preferences (用户首选项)
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > ArkTS API > @ohos.data.preferences (用户首选项)
category: harmonyos-references
scraped_at: 2026-04-28T07:59:12+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:d320b92fe95ac51a9a4e3ea242a5966ea405929482ed54d53a7e220a70ca9b6a
---

用户首选项为应用提供Key-Value键值型的数据处理能力，支持应用持久化轻量级数据，并对其修改和查询。

数据存储采用键值对形式，键为字符串类型，值可为数字、字符串、布尔类型及其对应的数组。

用户首选项的持久化文件存储在[preferencesDir](../harmonyos-guides/application-context-stage.md#获取应用文件路径)路径下，创建preferences对象前，需要保证preferencesDir路径可读写。持久化文件存储路径中的[加密等级](js-apis-app-ability-contextconstant.md#areamode)会影响文件的可读写状态，路径访问限制详见[应用文件目录与应用文件路径](../harmonyos-guides/app-sandbox-directory.md#应用文件目录与应用文件路径)。

说明

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

首选项无法保证进程并发安全，会有文件损坏和数据丢失的风险，不支持在多进程场景下使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { preferences } from '@kit.ArkData';
```

## 常量

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

| 名称 | 类型 | 只读 | 说明 |
| --- | --- | --- | --- |
| MAX\_KEY\_LENGTH | number | 是 | Key的最大长度限制为1024个字节。 |
| MAX\_VALUE\_LENGTH | number | 是 | Value的最大长度限制为16MB。 |

## preferences.getPreferences

PhonePC/2in1TabletTVWearable

getPreferences(context: Context, name: string, callback: AsyncCallback<Preferences>): void

获取Preferences实例，使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文。  FA模型的应用Context定义见[Context](js-apis-inner-app-context.md)。  Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| name | string | 是 | Preferences实例的名称。 |
| callback | AsyncCallback<[Preferences](js-apis-data-preferences.md#preferences)> | 是 | 回调函数。当获取Preferences实例成功，err为undefined，返回Preferences实例；否则err为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户首选项错误码](errorcode-preferences.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**示例：**

FA模型示例：

```
1. import { featureAbility } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let context = featureAbility.getContext();
5. let dataPreferences: preferences.Preferences | null = null;

7. preferences.getPreferences(context, 'myStore', (err: BusinessError, val: preferences.Preferences) => {
8. if (err) {
9. console.error("Failed to get preferences. code =" + err.code + ", message =" + err.message);
10. return;
11. }
12. dataPreferences = val;
13. console.info("Succeeded in getting preferences.");
14. })
```

Stage模型示例：

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { window } from '@kit.ArkUI';

5. let dataPreferences: preferences.Preferences | null = null;

7. class EntryAbility extends UIAbility {
8. onWindowStageCreate(windowStage: window.WindowStage) {
9. preferences.getPreferences(this.context, 'myStore', (err: BusinessError, val: preferences.Preferences) => {
10. if (err) {
11. console.error("Failed to get preferences. code =" + err.code + ", message =" + err.message);
12. return;
13. }
14. dataPreferences = val;
15. console.info("Succeeded in getting preferences.");
16. })
17. }
18. }
```

## preferences.getPreferences

PhonePC/2in1TabletTVWearable

getPreferences(context: Context, name: string): Promise<Preferences>

获取Preferences实例，使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文。  FA模型的应用Context定义见[Context](js-apis-inner-app-context.md)。  Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| name | string | 是 | Preferences实例的名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Preferences](js-apis-data-preferences.md#preferences)> | Promise对象，返回Preferences实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户首选项错误码](errorcode-preferences.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**示例：**

FA模型示例：

```
1. // 获取context
2. import { featureAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let context = featureAbility.getContext();

7. let dataPreferences: preferences.Preferences | null = null;
8. let promise = preferences.getPreferences(context, 'myStore');
9. promise.then((object: preferences.Preferences) => {
10. dataPreferences = object;
11. console.info("Succeeded in getting preferences.");
12. }).catch((err: BusinessError) => {
13. console.error("Failed to get preferences. code =" + err.code + ", message =" + err.message);
14. })
```

Stage模型示例：

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { window } from '@kit.ArkUI';

5. let dataPreferences: preferences.Preferences | null = null;

7. class EntryAbility extends UIAbility {
8. onWindowStageCreate(windowStage: window.WindowStage) {
9. let promise = preferences.getPreferences(this.context, 'myStore');
10. promise.then((object: preferences.Preferences) => {
11. dataPreferences = object;
12. console.info("Succeeded in getting preferences.");
13. }).catch((err: BusinessError) => {
14. console.error("Failed to get preferences. code =" + err.code + ", message =" + err.message);
15. })
16. }
17. }
```

## preferences.getPreferences10+

PhonePC/2in1TabletTVWearable

getPreferences(context: Context, options: Options, callback: AsyncCallback<Preferences>): void

获取Preferences实例，使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文。  FA模型的应用Context定义见[Context](js-apis-inner-app-context.md)。  Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| options | [Options](js-apis-data-preferences.md#options10) | 是 | 与Preferences实例相关的配置选项。 |
| callback | AsyncCallback<[Preferences](js-apis-data-preferences.md#preferences)> | 是 | 回调函数。当获取Preferences实例成功，err为undefined，返回Preferences实例；否则err为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户首选项错误码](errorcode-preferences.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 801 | Capability not supported. |
| 15500000 | Inner error. |
| 15501001 | The operations is supported in stage mode only. |
| 15501002 | Invalid dataGroupId. |

**示例：**

FA模型示例：

```
1. // 获取context
2. import { featureAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let context = featureAbility.getContext();
6. let dataPreferences: preferences.Preferences | null = null;

8. let options: preferences.Options = { name: 'myStore' };
9. preferences.getPreferences(context, options, (err: BusinessError, val: preferences.Preferences) => {
10. if (err) {
11. console.error("Failed to get preferences. code =" + err.code + ", message =" + err.message);
12. return;
13. }
14. dataPreferences = val;
15. console.info("Succeeded in getting preferences.");
16. })
```

Stage模型示例：

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { window } from '@kit.ArkUI';

5. let dataPreferences: preferences.Preferences | null = null;

7. class EntryAbility extends UIAbility {
8. onWindowStageCreate(windowStage: window.WindowStage) {
9. let options: preferences.Options = { name: 'myStore' };
10. preferences.getPreferences(this.context, options, (err: BusinessError, val: preferences.Preferences) => {
11. if (err) {
12. console.error("Failed to get preferences. code =" + err.code + ", message =" + err.message);
13. return;
14. }
15. dataPreferences = val;
16. console.info("Succeeded in getting preferences.");
17. })
18. }
19. }
```

## preferences.getPreferences10+

PhonePC/2in1TabletTVWearable

getPreferences(context: Context, options: Options): Promise<Preferences>

获取Preferences实例，使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文。  FA模型的应用Context定义见[Context](js-apis-inner-app-context.md)。  Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| options | [Options](js-apis-data-preferences.md#options10) | 是 | 与Preferences实例相关的配置选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Preferences](js-apis-data-preferences.md#preferences)> | Promise对象，返回Preferences实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户首选项错误码](errorcode-preferences.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 801 | Capability not supported. |
| 15500000 | Inner error. |
| 15501001 | The operations is supported in stage mode only. |
| 15501002 | Invalid dataGroupId. |

**示例：**

FA模型示例：

```
1. // 获取context
2. import { featureAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let context = featureAbility.getContext();

7. let dataPreferences: preferences.Preferences | null = null;
8. let options: preferences.Options = { name: 'myStore' };
9. let promise = preferences.getPreferences(context, options);
10. promise.then((object: preferences.Preferences) => {
11. dataPreferences = object;
12. console.info("Succeeded in getting preferences.");
13. }).catch((err: BusinessError) => {
14. console.error("Failed to get preferences. code =" + err.code + ", message =" + err.message);
15. })
```

Stage模型示例：

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { window } from '@kit.ArkUI';

5. let dataPreferences: preferences.Preferences | null = null;

7. class EntryAbility extends UIAbility {
8. onWindowStageCreate(windowStage: window.WindowStage) {
9. let options: preferences.Options = { name: 'myStore' };
10. let promise = preferences.getPreferences(this.context, options);
11. promise.then((object: preferences.Preferences) => {
12. dataPreferences = object;
13. console.info("Succeeded in getting preferences.");
14. }).catch((err: BusinessError) => {
15. console.error("Failed to get preferences. code =" + err.code + ", message =" + err.message);
16. })
17. }
18. }
```

## preferences.getPreferencesSync10+

PhonePC/2in1TabletTVWearable

getPreferencesSync(context: Context, options: Options): Preferences

获取Preferences实例，此为同步接口。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文。  FA模型的应用Context定义见[Context](js-apis-inner-app-context.md)。  Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| options | [Options](js-apis-data-preferences.md#options10) | 是 | 与Preferences实例相关的配置选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Preferences](js-apis-data-preferences.md#preferences) | 返回Preferences实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户首选项错误码](errorcode-preferences.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 801 | Capability not supported. |
| 15500000 | Inner error. |
| 15501001 | The operations is supported in stage mode only. |
| 15501002 | Invalid dataGroupId. |

**示例：**

FA模型示例：

```
1. // 获取context
2. import { featureAbility } from '@kit.AbilityKit';

4. let context = featureAbility.getContext();
5. let dataPreferences: preferences.Preferences | null = null;

7. let options: preferences.Options = { name: 'myStore' };
8. dataPreferences = preferences.getPreferencesSync(context, options);
```

Stage模型示例：

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';

4. let dataPreferences: preferences.Preferences | null = null;

6. class EntryAbility extends UIAbility {
7. onWindowStageCreate(windowStage: window.WindowStage) {
8. let options: preferences.Options = { name: 'myStore' };
9. dataPreferences = preferences.getPreferencesSync(this.context, options);
10. }
11. }
```

## preferences.deletePreferences

PhonePC/2in1TabletTVWearable

deletePreferences(context: Context, name: string, callback: AsyncCallback<void>): void

从缓存中删除指定的Preferences实例，若Preferences实例有对应的持久化文件，则同时删除其持久化文件。使用callback异步回调。

调用该接口后，不建议再使用旧的Preferences实例进行数据操作，否则会导致数据一致性问题，应将Preferences实例置为null，系统会统一回收。

不支持该接口与其他preference接口并发调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文。  FA模型的应用Context定义见[Context](js-apis-inner-app-context.md)。  Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| name | string | 是 | Preferences实例的名称。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当移除成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户首选项错误码](errorcode-preferences.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |
| 15500010 | Failed to delete the user preferences persistence file. |

**示例：**

FA模型示例：

```
1. // 获取context
2. import { featureAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let context = featureAbility.getContext();

7. preferences.deletePreferences(context, 'myStore', (err: BusinessError) => {
8. if (err) {
9. console.error("Failed to delete preferences. code =" + err.code + ", message =" + err.message);
10. return;
11. }
12. console.info("Succeeded in deleting preferences.");
13. })
```

Stage模型示例：

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { window } from '@kit.ArkUI';

5. class EntryAbility extends UIAbility {
6. onWindowStageCreate(windowStage: window.WindowStage) {
7. preferences.deletePreferences(this.context, 'myStore', (err: BusinessError) => {
8. if (err) {
9. console.error("Failed to delete preferences. code =" + err.code + ", message =" + err.message);
10. return;
11. }
12. console.info("Succeeded in deleting preferences.");
13. })
14. }
15. }
```

## preferences.deletePreferences

PhonePC/2in1TabletTVWearable

deletePreferences(context: Context, name: string): Promise<void>

从缓存中删除指定的Preferences实例，若Preferences实例有对应的持久化文件，则同时删除其持久化文件。使用Promise异步回调。

调用该接口后，不建议再使用旧的Preferences实例进行数据操作，否则会导致数据一致性问题，应将Preferences实例置为null，系统会统一回收。

不支持该接口与其他preference接口并发调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文。  FA模型的应用Context定义见[Context](js-apis-inner-app-context.md)。  Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| name | string | 是 | Preferences实例的名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户首选项错误码](errorcode-preferences.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |
| 15500010 | Failed to delete the user preferences persistence file. |

**示例：**

FA模型示例：

```
1. // 获取context
2. import { featureAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let context = featureAbility.getContext();

7. let promise = preferences.deletePreferences(context, 'myStore');
8. promise.then(() => {
9. console.info("Succeeded in deleting preferences.");
10. }).catch((err: BusinessError) => {
11. console.error("Failed to delete preferences. code =" + err.code + ", message =" + err.message);
12. })
```

Stage模型示例：

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { window } from '@kit.ArkUI';

5. class EntryAbility extends UIAbility {
6. onWindowStageCreate(windowStage: window.WindowStage) {
7. let promise = preferences.deletePreferences(this.context, 'myStore');
8. promise.then(() => {
9. console.info("Succeeded in deleting preferences.");
10. }).catch((err: BusinessError) => {
11. console.error("Failed to delete preferences. code =" + err.code + ", message =" + err.message);
12. })
13. }
14. }
```

## preferences.deletePreferences10+

PhonePC/2in1TabletTVWearable

deletePreferences(context: Context, options: Options, callback: AsyncCallback<void>): void

从缓存中删除指定的Preferences实例，若Preferences实例有对应的持久化文件，则同时删除其持久化文件。使用callback异步回调。

调用该接口后，不建议再使用旧的Preferences实例进行数据操作，否则会导致数据一致性问题，应将Preferences实例置为null，系统会统一回收。

不支持该接口与其他preference接口并发调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文。  FA模型的应用Context定义见[Context](js-apis-inner-app-context.md)。  Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| options | [Options](js-apis-data-preferences.md#options10) | 是 | 与Preferences实例相关的配置选项。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当移除成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户首选项错误码](errorcode-preferences.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 801 | Capability not supported. |
| 15500000 | Inner error. |
| 15500010 | Failed to delete the user preferences persistence file. |
| 15501001 | The operations is supported in stage mode only. |
| 15501002 | Invalid dataGroupId. |

**示例：**

FA模型示例：

```
1. // 获取context
2. import { featureAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let context = featureAbility.getContext();

7. let options: preferences.Options = { name: 'myStore' };
8. preferences.deletePreferences(context, options, (err: BusinessError) => {
9. if (err) {
10. console.error("Failed to delete preferences. code =" + err.code + ", message =" + err.message);
11. return;
12. }
13. console.info("Succeeded in deleting preferences.");
14. })
```

Stage模型示例：

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { window } from '@kit.ArkUI';

5. class EntryAbility extends UIAbility {
6. onWindowStageCreate(windowStage: window.WindowStage) {
7. let options: preferences.Options = { name: 'myStore' };
8. preferences.deletePreferences(this.context, options, (err: BusinessError) => {
9. if (err) {
10. console.error("Failed to delete preferences. code =" + err.code + ", message =" + err.message);
11. return;
12. }
13. console.info("Succeeded in deleting preferences.");
14. })
15. }
16. }
```

## preferences.deletePreferences10+

PhonePC/2in1TabletTVWearable

deletePreferences(context: Context, options: Options): Promise<void>

从缓存中删除指定的Preferences实例，若Preferences实例有对应的持久化文件，则同时删除其持久化文件。使用Promise异步回调。

调用该接口后，不建议再使用旧的Preferences实例进行数据操作，否则会导致数据一致性问题，应将Preferences实例置为null，系统会统一回收。

不支持该接口与其他preference接口并发调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文。  FA模型的应用Context定义见[Context](js-apis-inner-app-context.md)。  Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| options | [Options](js-apis-data-preferences.md#options10) | 是 | 与Preferences实例相关的配置选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户首选项错误码](errorcode-preferences.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 801 | Capability not supported. |
| 15500000 | Inner error. |
| 15500010 | Failed to delete the user preferences persistence file. |
| 15501001 | The operations is supported in stage mode only. |
| 15501002 | Invalid dataGroupId. |

**示例：**

FA模型示例：

```
1. // 获取context
2. import { featureAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let context = featureAbility.getContext();

7. let options: preferences.Options = { name: 'myStore' };
8. let promise = preferences.deletePreferences(context, options);
9. promise.then(() => {
10. console.info("Succeeded in deleting preferences.");
11. }).catch((err: BusinessError) => {
12. console.error("Failed to delete preferences. code =" + err.code + ", message =" + err.message);
13. })
```

Stage模型示例：

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { window } from '@kit.ArkUI';

5. class EntryAbility extends UIAbility {
6. onWindowStageCreate(windowStage: window.WindowStage) {
7. let options: preferences.Options = { name: 'myStore' };
8. let promise = preferences.deletePreferences(this.context, options);
9. promise.then(() => {
10. console.info("Succeeded in deleting preferences.");
11. }).catch((err: BusinessError) => {
12. console.error("Failed to delete preferences. code =" + err.code + ", message =" + err.message);
13. })
14. }
15. }
```

## preferences.removePreferencesFromCache

PhonePC/2in1TabletTVWearable

removePreferencesFromCache(context: Context, name: string, callback: AsyncCallback<void>): void

从缓存中移除指定的Preferences实例，使用callback异步回调。

应用首次调用[getPreferences](js-apis-data-preferences.md#preferencesgetpreferences)接口获取某个Preferences实例后，该实例会被缓存起来，后续调用[getPreferences](js-apis-data-preferences.md#preferencesgetpreferences)时不会再次从持久化文件中读取，直接从缓存中获取Preferences实例。调用此接口移除缓存中的实例之后，再次getPreferences将会重新读取持久化文件，生成新的Preferences实例。

调用该接口后，不建议再使用旧的Preferences实例进行数据操作，否则会导致数据一致性问题，应将Preferences实例置为null，系统会统一回收。

若使用[GSKV存储模式](../harmonyos-guides/data-persistence-by-preferences.md#gskv存储)，推荐在进程退出时手动调用一次该接口。此操作会将数据缓存页写入磁盘，可一定程度上减少下一次调用getPreferences接口时的耗时。否则，下一次调用getPreferences接口时底层需要进行数据恢复，数据恢复的耗时取决于未写入磁盘的数据缓存页数量。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文。  FA模型的应用Context定义见[Context](js-apis-inner-app-context.md)。  Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| name | string | 是 | Preferences实例的名称。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当移除成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户首选项错误码](errorcode-preferences.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**示例：**

FA模型示例：

```
1. // 获取context
2. import { featureAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let context = featureAbility.getContext();
6. preferences.removePreferencesFromCache(context, 'myStore', (err: BusinessError) => {
7. if (err) {
8. console.error("Failed to remove preferences. code =" + err.code + ", message =" + err.message);
9. return;
10. }
11. console.info("Succeeded in removing preferences.");
12. })
```

Stage模型示例：

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { window } from '@kit.ArkUI';

5. class EntryAbility extends UIAbility {
6. onWindowStageCreate(windowStage: window.WindowStage) {
7. preferences.removePreferencesFromCache(this.context, 'myStore', (err: BusinessError) => {
8. if (err) {
9. console.error("Failed to remove preferences. code =" + err.code + ", message =" + err.message);
10. return;
11. }
12. console.info("Succeeded in removing preferences.");
13. })
14. }
15. }
```

## preferences.removePreferencesFromCache

PhonePC/2in1TabletTVWearable

removePreferencesFromCache(context: Context, name: string): Promise<void>

从缓存中移除指定的Preferences实例，使用Promise异步回调。

应用首次调用[getPreferences](js-apis-data-preferences.md#preferencesgetpreferences)接口获取某个Preferences实例后，该实例会被缓存起来，后续调用[getPreferences](js-apis-data-preferences.md#preferencesgetpreferences)时不会再次从持久化文件中读取，直接从缓存中获取Preferences实例。调用此接口移除缓存中的实例之后，再次getPreferences将会重新读取持久化文件，生成新的Preferences实例。

调用该接口后，不建议再使用旧的Preferences实例进行数据操作，否则会导致数据一致性问题，应将Preferences实例置为null，系统会统一回收。

若使用[GSKV存储模式](../harmonyos-guides/data-persistence-by-preferences.md#gskv存储)，推荐在进程退出时手动调用一次该接口。此操作会将数据缓存页写入磁盘，可一定程度上减少下一次调用getPreferences接口时的耗时。否则，下一次调用getPreferences接口时底层需要进行数据恢复，数据恢复的耗时取决于未写入磁盘的数据缓存页数量。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文。  FA模型的应用Context定义见[Context](js-apis-inner-app-context.md)。  Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| name | string | 是 | Preferences实例的名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户首选项错误码](errorcode-preferences.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**示例：**

FA模型示例：

```
1. // 获取context
2. import { featureAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let context = featureAbility.getContext();
6. let promise = preferences.removePreferencesFromCache(context, 'myStore');
7. promise.then(() => {
8. console.info("Succeeded in removing preferences.");
9. }).catch((err: BusinessError) => {
10. console.error("Failed to remove preferences. code =" + err.code + ", message =" + err.message);
11. })
```

Stage模型示例：

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { window } from '@kit.ArkUI';

5. class EntryAbility extends UIAbility {
6. onWindowStageCreate(windowStage: window.WindowStage) {
7. let promise = preferences.removePreferencesFromCache(this.context, 'myStore');
8. promise.then(() => {
9. console.info("Succeeded in removing preferences.");
10. }).catch((err: BusinessError) => {
11. console.error("Failed to remove preferences. code =" + err.code + ", message =" + err.message);
12. })
13. }
14. }
```

## preferences.removePreferencesFromCacheSync10+

PhonePC/2in1TabletTVWearable

removePreferencesFromCacheSync(context: Context, name: string): void

从缓存中移除指定的Preferences实例，此为同步接口。

应用首次调用[getPreferences](js-apis-data-preferences.md#preferencesgetpreferences)接口获取某个Preferences实例后，该实例会被缓存起来，后续调用[getPreferences](js-apis-data-preferences.md#preferencesgetpreferences)时不会再次从持久化文件中读取，直接从缓存中获取Preferences实例。调用此接口移除缓存中的实例之后，再次getPreferences将会重新读取持久化文件，生成新的Preferences实例。

调用该接口后，不建议再使用旧的Preferences实例进行数据操作，否则会导致数据一致性问题，应将Preferences实例置为null，系统会统一回收。

若使用[GSKV存储模式](../harmonyos-guides/data-persistence-by-preferences.md#gskv存储)，推荐在进程退出时手动调用一次该接口。此操作会将数据缓存页写入磁盘，可一定程度上减少下一次调用getPreferences接口时的耗时。否则，下一次调用getPreferences接口时底层需要进行数据恢复，数据恢复的耗时取决于未写入磁盘的数据缓存页数量。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文。  FA模型的应用Context定义见[Context](js-apis-inner-app-context.md)。  Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| name | string | 是 | Preferences实例的名称。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户首选项错误码](errorcode-preferences.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**示例：**

FA模型示例：

```
1. // 获取context
2. import { featureAbility } from '@kit.AbilityKit';
3. let context = featureAbility.getContext();
4. preferences.removePreferencesFromCacheSync(context, 'myStore');
```

Stage模型示例：

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';

4. class EntryAbility extends UIAbility {
5. onWindowStageCreate(windowStage: window.WindowStage) {
6. preferences.removePreferencesFromCacheSync(this.context, 'myStore');
7. }
8. }
```

## preferences.removePreferencesFromCache10+

PhonePC/2in1TabletTVWearable

removePreferencesFromCache(context: Context, options: Options, callback: AsyncCallback<void>): void

从缓存中移除指定的Preferences实例，使用callback异步回调。

应用首次调用[getPreferences](js-apis-data-preferences.md#preferencesgetpreferences)接口获取某个Preferences实例后，该实例会被缓存起来，后续调用[getPreferences](js-apis-data-preferences.md#preferencesgetpreferences)时不会再次从持久化文件中读取，直接从缓存中获取Preferences实例。调用此接口移除缓存中的实例之后，再次getPreferences将会重新读取持久化文件，生成新的Preferences实例。

调用该接口后，不建议再使用旧的Preferences实例进行数据操作，否则会导致数据一致性问题，应将Preferences实例置为null，系统会统一回收。

若使用[GSKV存储模式](../harmonyos-guides/data-persistence-by-preferences.md#gskv存储)，推荐在进程退出时手动调用一次该接口。此操作会将数据缓存页写入磁盘，可一定程度上减少下一次调用getPreferences接口时的耗时。否则，下一次调用getPreferences接口时底层需要进行数据恢复，数据恢复的耗时取决于未写入磁盘的数据缓存页数量。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文。  FA模型的应用Context定义见[Context](js-apis-inner-app-context.md)。  Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| options | [Options](js-apis-data-preferences.md#options10) | 是 | 与Preferences实例相关的配置选项。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当移除成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户首选项错误码](errorcode-preferences.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 801 | Capability not supported. |
| 15500000 | Inner error. |
| 15501001 | The operations is supported in stage mode only. |
| 15501002 | Invalid dataGroupId. |

**示例：**

FA模型示例：

```
1. // 获取context
2. import { featureAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let context = featureAbility.getContext();
6. let options: preferences.Options = { name: 'myStore' };
7. preferences.removePreferencesFromCache(context, options, (err: BusinessError) => {
8. if (err) {
9. console.error("Failed to remove preferences. code =" + err.code + ", message =" + err.message);
10. return;
11. }
12. console.info("Succeeded in removing preferences.");
13. })
```

Stage模型示例：

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { window } from '@kit.ArkUI';

5. class EntryAbility extends UIAbility {
6. onWindowStageCreate(windowStage: window.WindowStage) {
7. let options: preferences.Options = { name: 'myStore' };
8. preferences.removePreferencesFromCache(this.context, options, (err: BusinessError) => {
9. if (err) {
10. console.error("Failed to remove preferences. code =" + err.code + ", message =" + err.message);
11. return;
12. }
13. console.info("Succeeded in removing preferences.");
14. })
15. }
16. }
```

## preferences.removePreferencesFromCache10+

PhonePC/2in1TabletTVWearable

removePreferencesFromCache(context: Context, options: Options): Promise<void>

从缓存中移除指定的Preferences实例，使用Promise异步回调。

应用首次调用[getPreferences](js-apis-data-preferences.md#preferencesgetpreferences)接口获取某个Preferences实例后，该实例会被缓存起来，后续调用[getPreferences](js-apis-data-preferences.md#preferencesgetpreferences)时不会再次从持久化文件中读取，直接从缓存中获取Preferences实例。调用此接口移除缓存中的实例之后，再次getPreferences将会重新读取持久化文件，生成新的Preferences实例。

调用该接口后，不建议再使用旧的Preferences实例进行数据操作，否则会导致数据一致性问题，应将Preferences实例置为null，系统会统一回收。

若使用[GSKV存储模式](../harmonyos-guides/data-persistence-by-preferences.md#gskv存储)，推荐在进程退出时手动调用一次该接口。此操作会将数据缓存页写入磁盘，可一定程度上减少下一次调用getPreferences接口时的耗时。否则，下一次调用getPreferences接口时底层需要进行数据恢复，数据恢复的耗时取决于未写入磁盘的数据缓存页数量。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文。  FA模型的应用Context定义见[Context](js-apis-inner-app-context.md)。  Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| options | [Options](js-apis-data-preferences.md#options10) | 是 | 与Preferences实例相关的配置选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户首选项错误码](errorcode-preferences.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 801 | Capability not supported. |
| 15500000 | Inner error. |
| 15501001 | The operations is supported in stage mode only. |
| 15501002 | Invalid dataGroupId. |

**示例：**

FA模型示例：

```
1. // 获取context
2. import { featureAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let context = featureAbility.getContext();
6. let options: preferences.Options = { name: 'myStore' };
7. let promise = preferences.removePreferencesFromCache(context, options);
8. promise.then(() => {
9. console.info("Succeeded in removing preferences.");
10. }).catch((err: BusinessError) => {
11. console.error("Failed to remove preferences. code =" + err.code + ", message =" + err.message);
12. })
```

Stage模型示例：

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { window } from '@kit.ArkUI';

5. class EntryAbility extends UIAbility {
6. onWindowStageCreate(windowStage: window.WindowStage) {
7. let options: preferences.Options = { name: 'myStore' };
8. let promise = preferences.removePreferencesFromCache(this.context, options);
9. promise.then(() => {
10. console.info("Succeeded in removing preferences.");
11. }).catch((err: BusinessError) => {
12. console.error("Failed to remove preferences. code =" + err.code + ", message =" + err.message);
13. })
14. }
15. }
```

## preferences.removePreferencesFromCacheSync10+

PhonePC/2in1TabletTVWearable

removePreferencesFromCacheSync(context: Context, options: Options):void

从缓存中移除指定的Preferences实例，此为同步接口。

应用首次调用[getPreferences](js-apis-data-preferences.md#preferencesgetpreferences)接口获取某个Preferences实例后，该实例会被缓存起来，后续调用[getPreferences](js-apis-data-preferences.md#preferencesgetpreferences)时不会再次从持久化文件中读取，直接从缓存中获取Preferences实例。调用此接口移除缓存中的实例之后，再次getPreferences将会重新读取持久化文件，生成新的Preferences实例。

调用该接口后，不建议再使用旧的Preferences实例进行数据操作，否则会导致数据一致性问题，应将Preferences实例置为null，系统会统一回收。

若使用[GSKV存储模式](../harmonyos-guides/data-persistence-by-preferences.md#gskv存储)，推荐在进程退出时手动调用一次该接口。此操作会将数据缓存页写入磁盘，可一定程度上减少下一次调用getPreferences接口时的耗时。否则，下一次调用getPreferences接口时底层需要进行数据恢复，数据恢复的耗时取决于未写入磁盘的数据缓存页数量。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文。  FA模型的应用Context定义见[Context](js-apis-inner-app-context.md)。  Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| options | [Options](js-apis-data-preferences.md#options10) | 是 | 与Preferences实例相关的配置选项。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户首选项错误码](errorcode-preferences.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 801 | Capability not supported. |
| 15500000 | Inner error. |
| 15501001 | The operations is supported in stage mode only. |
| 15501002 | Invalid dataGroupId. |

**示例：**

FA模型示例：

```
1. // 获取context
2. import { featureAbility } from '@kit.AbilityKit';
3. let context = featureAbility.getContext();
4. let options: preferences.Options = { name: 'myStore' };
5. preferences.removePreferencesFromCacheSync(context, options);
```

Stage模型示例：

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';

4. class EntryAbility extends UIAbility {
5. onWindowStageCreate(windowStage: window.WindowStage) {
6. let options: preferences.Options = { name: 'myStore' };
7. preferences.removePreferencesFromCacheSync(this.context, options);
8. }
9. }
```

## StorageType18+

PhonePC/2in1TabletTVWearable

Preferences的存储模式枚举。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| XML | 0 | 表示[XML存储模式](../harmonyos-guides/data-persistence-by-preferences.md#xml存储)，这是Preferences的默认存储模式。  **特点：** 数据XML格式进行存储。对数据的操作发生在内存中，需要调用flush接口进行落盘。 |
| GSKV | 1 | 表示[GSKV存储模式](../harmonyos-guides/data-persistence-by-preferences.md#gskv存储)。  **特点：** 数据以GSKV数据库模式进行存储。对数据的操作实时落盘，无需调用flush接口对数据进行落盘。 |

说明

* 在选择存储模式前，建议调用isStorageTypeSupported检查当前平台是否支持对应存储模式。
* 当选择某一模式通过getPreferences接口获取实例后，不允许中途切换模式。
* 首选项不支持不同模式间数据的迁移，若需将数据从一种模式切换至另一种模式，需通过读写首选项的形式进行数据迁移。
* 若需要变更首选项的存储路径，不能通过移动或覆盖文件的方式进行，需通过读写首选项的形式进行数据迁移。

## preferences.isStorageTypeSupported18+

PhonePC/2in1TabletTVWearable

isStorageTypeSupported(type: StorageType): boolean

判断当前平台是否支持传入的存储模式，此为同步接口。如果当前平台支持传入的存储模式时，该接口返回true；反之，返回false。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [StorageType](js-apis-data-preferences.md#storagetype18) | 是 | 需要判断是否支持的存储模式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true表示当前平台支持当前校验的存储模式，false表示当前平台不支持当前校验的存储模式。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户首选项错误码](errorcode-preferences.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: Incorrect parameter types. |

**示例：**

```
1. let xmlType = preferences.StorageType.XML;
2. let gskvType = preferences.StorageType.GSKV;
3. let isXmlSupported = preferences.isStorageTypeSupported(xmlType);
4. let isGskvSupported = preferences.isStorageTypeSupported(gskvType);
5. console.info("Is xml supported in current platform: " + isXmlSupported);
6. console.info("Is gskv supported in current platform: " + isGskvSupported);
```

## Options10+

PhonePC/2in1TabletTVWearable

Preferences实例配置选项。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 否 | 否 | Preferences实例的名称。名称长度需大于零且小于等于255字节，名称中不能包含'/'且不能以'/'结尾。  **元服务API：** 从API version 11开始，该参数支持在元服务中使用。 |
| dataGroupId | string|null|undefined | 否 | 是 | 应用组ID，需要向应用市场获取，详见[dataGroupId申请流程](../harmonyos-guides/ime-kit-security.md#共享沙箱介绍)。基于dataGroupId的数据共享支持两种场景：1.同一应用的不同进程间共享，只支持三方应用中输入法和输入法的扩展场景使用；2.不同应用间的数据共享，只支持系统应用使用。  为可选参数。指定在此dataGroupId对应的沙箱路径下创建Preferences实例。当此参数不填时，默认在本应用沙箱目录下创建Preferences实例。  **模型约束：** 此属性仅在Stage模型下可用。  **元服务API：** 从API version 11开始，该参数支持在元服务中使用。 |
| storageType18+ | [StorageType](js-apis-data-preferences.md#storagetype18)|null|undefined | 否 | 是 | 存储模式，为可选参数。表示当前Preferences实例需要使用的存储模式。当此参数不填时，默认使用XML存储模式。当选择某种存储模式创建Preferences后，不支持中途切换存储模式。  **元服务API：** 从API version 18开始，该参数支持在元服务中使用。 |

## Preferences

PhonePC/2in1TabletTVWearable

首选项实例，提供获取和修改存储数据的接口。

下列接口都需先使用[preferences.getPreferences](js-apis-data-preferences.md#preferencesgetpreferences)获取到Preferences实例，再通过此实例调用对应接口。

### get

PhonePC/2in1TabletTVWearable

get(key: string, defValue: ValueType, callback: AsyncCallback<ValueType>): void

从缓存的Preferences实例中获取键对应的值，如果值为null或者非默认值类型，返回默认数据defValue，使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要获取的存储Key名称，不能为空，最大长度限制为[MAX\_KEY\_LENGTH](js-apis-data-preferences.md#常量)。 |
| defValue | [ValueType](js-apis-data-preferences.md#valuetype) | 是 | 默认返回值。 |
| callback | AsyncCallback<[ValueType](js-apis-data-preferences.md#valuetype)> | 是 | 回调函数。当获取成功时，err为undefined，data为键对应的值；否则err为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户首选项错误码](errorcode-preferences.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. dataPreferences.get('startup', 'default', (err: BusinessError, val: preferences.ValueType) => {
4. if (err) {
5. console.error("Failed to get value of 'startup'. code =" + err.code + ", message =" + err.message);
6. return;
7. }
8. console.info("Succeeded in getting value of 'startup'. val： " + val);
9. })
```

### get

PhonePC/2in1TabletTVWearable

get(key: string, defValue: ValueType): Promise<ValueType>

从缓存的Preferences实例中获取键对应的值，如果值为null或者非默认值类型，返回默认数据defValue，使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要获取的存储Key名称，不能为空，最大长度限制为[MAX\_KEY\_LENGTH](js-apis-data-preferences.md#常量)。 |
| defValue | [ValueType](js-apis-data-preferences.md#valuetype) | 是 | 默认返回值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ValueType](js-apis-data-preferences.md#valuetype)> | Promise对象，返回键对应的值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户首选项错误码](errorcode-preferences.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let promise = dataPreferences.get('startup', 'default');
4. promise.then((data: preferences.ValueType) => {
5. console.info("Succeeded in getting value of 'startup'. Data: " + data);
6. }).catch((err: BusinessError) => {
7. console.error("Failed to get value of 'startup'. code =" + err.code + ", message =" + err.message);
8. })
```

### getSync10+

PhonePC/2in1TabletTVWearable

getSync(key: string, defValue: ValueType): ValueType

从缓存的Preferences实例中获取键对应的值，如果值为null或者非默认值类型，返回默认数据defValue，此为同步接口。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要获取的存储Key名称，不能为空，最大长度限制为[MAX\_KEY\_LENGTH](js-apis-data-preferences.md#常量)。 |
| defValue | [ValueType](js-apis-data-preferences.md#valuetype) | 是 | 默认返回值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ValueType](js-apis-data-preferences.md#valuetype) | 返回键对应的值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户首选项错误码](errorcode-preferences.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**示例：**

```
1. let value: preferences.ValueType = dataPreferences.getSync('startup', 'default');
```

### getAll

PhonePC/2in1TabletTVWearable

getAll(callback: AsyncCallback<Object>): void

获取缓存的Preferences实例中的所有键值数据。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Object> | 是 | 回调函数。当获取成功，err为undefined，value为所有键值数据；否则err为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户首选项错误码](errorcode-preferences.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Mandatory parameters are left unspecified. |
| 15500000 | Inner error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. // 由于ArkTS中无Object.keys，且无法使用for..in...
4. // 若报ArkTS问题，请将此方法单独抽离至一个ts文件中并暴露，在需要用到的ets文件中引入使用
5. function getObjKeys(obj: Object): string[] {
6. let keys = Object.keys(obj);
7. return keys;
8. }

10. dataPreferences.getAll((err: BusinessError, value: Object) => {
11. if (err) {
12. console.error("Failed to get all key-values. code =" + err.code + ", message =" + err.message);
13. return;
14. }
15. let allKeys = getObjKeys(value);
16. console.info("getAll keys = " + allKeys);
17. console.info("getAll object = " + JSON.stringify(value));
18. })
```

### getAll

PhonePC/2in1TabletTVWearable

getAll(): Promise<Object>

获取缓存的Preferences实例中的所有键值数据。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Object> | Promise对象，返回所有包含的键值数据。 |

**错误码：**

以下错误码的详细介绍请参见[用户首选项错误码](errorcode-preferences.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 15500000 | Inner error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. // 由于ArkTS中无Object.keys，且无法使用for..in...
4. // 若报ArkTS问题，请将此方法单独抽离至一个ts文件中并暴露，在需要用到的ets文件中引入使用
5. function getObjKeys(obj: Object): string[] {
6. let keys = Object.keys(obj);
7. return keys;
8. }

10. let promise = dataPreferences.getAll();
11. promise.then((value: Object) => {
12. let allKeys = getObjKeys(value);
13. console.info('getAll keys = ' + allKeys);
14. console.info("getAll object = " + JSON.stringify(value));
15. }).catch((err: BusinessError) => {
16. console.error("Failed to get all key-values. code =" + err.code + ", message =" + err.message);
17. })
```

### getAllSync10+

PhonePC/2in1TabletTVWearable

getAllSync(): Object

获取缓存的Preferences实例中的所有键值数据，此为同步接口。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Object | 返回所有包含的键值数据。 |

**错误码：**

以下错误码的详细介绍请参见[用户首选项错误码](errorcode-preferences.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 15500000 | Inner error. |

**示例：**

```
1. // 由于ArkTS中无Object.keys，且无法使用for..in...
2. // 若报ArkTS问题，请将此方法单独抽离至一个ts文件中并暴露，在需要用到的ets文件中引入使用
3. function getObjKeys(obj: Object): string[] {
4. let keys = Object.keys(obj);
5. return keys;
6. }

8. let value = dataPreferences.getAllSync();
9. let allKeys = getObjKeys(value);
10. console.info('getAll keys = ' + allKeys);
11. console.info("getAll object = " + JSON.stringify(value));
```

### put

PhonePC/2in1TabletTVWearable

put(key: string, value: ValueType, callback: AsyncCallback<void>): void

将数据写入缓存的Preferences实例中，可通过[flush](js-apis-data-preferences.md#flush)将Preferences实例持久化，使用callback异步回调。

说明

当value中包含非UTF-8格式的字符串时，请使用Uint8Array类型存储，否则会造成持久化文件出现格式错误造成文件损坏。

当对应的键已经存在时，put()方法会覆盖其值。可以使用hasSync()方法检查是否存在对应键值对。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要修改的存储的Key，不能为空，最大长度限制为[MAX\_KEY\_LENGTH](js-apis-data-preferences.md#常量)。 |
| value | [ValueType](js-apis-data-preferences.md#valuetype) | 是 | 存储的新值。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当数据写入成功，err为undefined；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户首选项错误码](errorcode-preferences.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. dataPreferences.put('startup', 'auto', (err: BusinessError) => {
4. if (err) {
5. console.error("Failed to put value of 'startup'. code =" + err.code + ", message =" + err.message);
6. return;
7. }
8. console.info("Succeeded in putting value of 'startup'.");
9. })
```

### put

PhonePC/2in1TabletTVWearable

put(key: string, value: ValueType): Promise<void>

将数据写入缓存的Preferences实例中，可通过[flush](js-apis-data-preferences.md#flush)将Preferences实例持久化，使用Promise异步回调。

说明

当value中包含非UTF-8格式的字符串时，请使用Uint8Array类型存储，否则会造成持久化文件出现格式错误造成文件损坏。

当对应的键已经存在时，put()方法会覆盖其值。可以使用hasSync()方法检查是否存在对应键值对。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要修改的存储的Key，不能为空，最大长度限制为[MAX\_KEY\_LENGTH](js-apis-data-preferences.md#常量)。 |
| value | [ValueType](js-apis-data-preferences.md#valuetype) | 是 | 存储的新值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户首选项错误码](errorcode-preferences.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let promise = dataPreferences.put('startup', 'auto');
4. promise.then(() => {
5. console.info("Succeeded in putting value of 'startup'.");
6. }).catch((err: BusinessError) => {
7. console.error("Failed to put value of 'startup'. code =" + err.code + ", message =" + err.message);
8. })
```

### putSync10+

PhonePC/2in1TabletTVWearable

putSync(key: string, value: ValueType): void

将数据写入缓存的Preferences实例中，可通过[flush](js-apis-data-preferences.md#flush)将Preferences实例持久化，此为同步接口。

说明

当value中包含非UTF-8格式的字符串时，请使用Uint8Array类型存储，否则会造成持久化文件出现格式错误造成文件损坏。

当对应的键已经存在时，putSync()方法会覆盖其值。可以使用hasSync()方法检查是否存在对应键值对。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要修改的存储的Key，不能为空，最大长度限制为[MAX\_KEY\_LENGTH](js-apis-data-preferences.md#常量)。 |
| value | [ValueType](js-apis-data-preferences.md#valuetype) | 是 | 存储的新值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户首选项错误码](errorcode-preferences.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**示例：**

```
1. dataPreferences.putSync('startup', 'auto');
```

### has

PhonePC/2in1TabletTVWearable

has(key: string, callback: AsyncCallback<boolean>): void

检查缓存的Preferences实例中是否包含指定Key的存储键值对，使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要检查的存储key名称，不能为空，最大长度限制为[MAX\_KEY\_LENGTH](js-apis-data-preferences.md#常量)。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回Preferences实例是否包含给定key的存储键值对，true表示存在，false表示不存在。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户首选项错误码](errorcode-preferences.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. dataPreferences.has('startup', (err: BusinessError, val: boolean) => {
4. if (err) {
5. console.error("Failed to check the key 'startup'. code =" + err.code + ", message =" + err.message);
6. return;
7. }
8. if (val) {
9. console.info("The key 'startup' is contained.");
10. } else {
11. console.info("The key 'startup' is not contained.");
12. }
13. })
```

### has

PhonePC/2in1TabletTVWearable

has(key: string): Promise<boolean>

检查缓存的Preferences实例中是否包含指定Key的存储键值对，使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要检查的存储key名称，不能为空，最大长度限制为[MAX\_KEY\_LENGTH](js-apis-data-preferences.md#常量)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回Preferences实例是否包含给定key的存储键值对，true表示存在，false表示不存在。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户首选项错误码](errorcode-preferences.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let promise = dataPreferences.has('startup');
4. promise.then((val: boolean) => {
5. if (val) {
6. console.info("The key 'startup' is contained.");
7. } else {
8. console.info("The key 'startup' does not contain.");
9. }
10. }).catch((err: BusinessError) => {
11. console.error("Failed to check the key 'startup'. code =" + err.code + ", message =" + err.message);
12. })
```

### hasSync10+

PhonePC/2in1TabletTVWearable

hasSync(key: string): boolean

检查缓存的Preferences实例中是否包含指定Key的存储键值对，此为同步接口。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要检查的存储key名称，不能为空，最大长度限制为[MAX\_KEY\_LENGTH](js-apis-data-preferences.md#常量)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回Preferences实例是否包含给定key的存储键值对，true表示存在，false表示不存在。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户首选项错误码](errorcode-preferences.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**示例：**

```
1. let isExist: boolean = dataPreferences.hasSync('startup');
2. if (isExist) {
3. console.info("The key 'startup' is contained.");
4. } else {
5. console.info("The key 'startup' does not contain.");
6. }
```

### delete

PhonePC/2in1TabletTVWearable

delete(key: string, callback: AsyncCallback<void>): void

从缓存的Preferences实例中删除名为给定Key的存储键值对，可通过[flush](js-apis-data-preferences.md#flush)将Preferences实例持久化，使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要删除的存储Key名称，不能为空，最大长度限制为[MAX\_KEY\_LENGTH](js-apis-data-preferences.md#常量)。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当删除成功，err为undefined；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户首选项错误码](errorcode-preferences.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. dataPreferences.delete('startup', (err: BusinessError) => {
4. if (err) {
5. console.error("Failed to delete the key 'startup'. code =" + err.code + ", message =" + err.message);
6. return;
7. }
8. console.info("Succeeded in deleting the key 'startup'.");
9. })
```

### delete

PhonePC/2in1TabletTVWearable

delete(key: string): Promise<void>

从缓存的Preferences实例中删除名为给定Key的存储键值对，可通过[flush](js-apis-data-preferences.md#flush)将Preferences实例持久化，使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要删除的存储key名称，不能为空，最大长度限制为[MAX\_KEY\_LENGTH](js-apis-data-preferences.md#常量)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户首选项错误码](errorcode-preferences.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let promise = dataPreferences.delete('startup');
4. promise.then(() => {
5. console.info("Succeeded in deleting the key 'startup'.");
6. }).catch((err: BusinessError) => {
7. console.error("Failed to delete the key 'startup'. code =" + err.code +", message =" + err.message);
8. })
```

### deleteSync10+

PhonePC/2in1TabletTVWearable

deleteSync(key: string): void

从缓存的Preferences实例中删除名为给定Key的存储键值对，可通过[flush](js-apis-data-preferences.md#flush)将Preferences实例持久化，此为同步接口。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要删除的存储key名称，不能为空，最大长度限制为[MAX\_KEY\_LENGTH](js-apis-data-preferences.md#常量)。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户首选项错误码](errorcode-preferences.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**示例：**

```
1. dataPreferences.deleteSync('startup');
```

### flush

PhonePC/2in1TabletTVWearable

flush(callback: AsyncCallback<void>): void

将缓存的Preferences实例中的数据异步存储到用户首选项的持久化文件中，使用callback异步回调。

说明

当数据未修改或修改后的数据与缓存数据一致时，不会刷新持久化文件。

只在XML存储模式下使用，在GSKV存储模式下无需调用，因为当选择该模式时首选项对数据的操作会实时落盘。Preferences存储模式可见[存储模式说明](../harmonyos-guides/data-persistence-by-preferences.md#存储模式说明)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当保存成功，err为undefined；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户首选项错误码](errorcode-preferences.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Mandatory parameters are left unspecified. |
| 15500000 | Inner error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. dataPreferences.flush((err: BusinessError) => {
4. if (err) {
5. console.error("Failed to flush. code =" + err.code + ", message =" + err.message);
6. return;
7. }
8. console.info("Succeeded in flushing.");
9. })
```

### flush

PhonePC/2in1TabletTVWearable

flush(): Promise<void>

将缓存的Preferences实例中的数据异步存储到用户首选项的持久化文件中，使用Promise异步回调。

说明

当数据未修改或修改后的数据与缓存数据一致时，不会刷新持久化文件。

只在XML存储模式下使用，在GSKV存储模式下无需调用，因为当选择该模式时首选项对数据的操作会实时落盘。Preferences存储模式可见[存储模式说明](../harmonyos-guides/data-persistence-by-preferences.md#存储模式说明)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[用户首选项错误码](errorcode-preferences.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 15500000 | Inner error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let promise = dataPreferences.flush();
4. promise.then(() => {
5. console.info("Succeeded in flushing.");
6. }).catch((err: BusinessError) => {
7. console.error("Failed to flush. code =" + err.code + ", message =" + err.message);
8. })
```

### flushSync14+

PhonePC/2in1TabletTVWearable

flushSync(): void

将缓存的Preferences实例中的数据存储到用户首选项的持久化文件中。

说明

当数据未修改或修改后的数据与缓存数据一致时，不会刷新持久化文件。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**错误码：**

以下错误码的详细介绍请参见[用户首选项错误码](errorcode-preferences.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 15500000 | Inner error. |

**示例：**

```
1. dataPreferences.flushSync();
```

### clear

PhonePC/2in1TabletTVWearable

clear(callback: AsyncCallback<void>): void

清除缓存的Preferences实例中的所有数据，可通过[flush](js-apis-data-preferences.md#flush)将Preferences实例持久化，使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当清除成功，err为undefined；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户首选项错误码](errorcode-preferences.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Mandatory parameters are left unspecified. |
| 15500000 | Inner error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. dataPreferences.clear((err: BusinessError) =>{
4. if (err) {
5. console.error("Failed to clear. code =" + err.code + ", message =" + err.message);
6. return;
7. }
8. console.info("Succeeded in clearing.");
9. })
```

### clear

PhonePC/2in1TabletTVWearable

clear(): Promise<void>

清除缓存的Preferences实例中的所有数据，可通过[flush](js-apis-data-preferences.md#flush)将Preferences实例持久化，使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[用户首选项错误码](errorcode-preferences.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 15500000 | Inner error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let promise = dataPreferences.clear();
4. promise.then(() => {
5. console.info("Succeeded in clearing.");
6. }).catch((err: BusinessError) => {
7. console.error("Failed to clear. code =" + err.code + ", message =" + err.message);
8. })
```

### clearSync10+

PhonePC/2in1TabletTVWearable

clearSync(): void

清除缓存的Preferences实例中的所有数据，可通过[flush](js-apis-data-preferences.md#flush)将Preferences实例持久化，此为同步接口。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**示例：**

```
1. dataPreferences.clearSync();
```

### on('change')

PhonePC/2in1TabletTVWearable

on(type: 'change', callback: Callback<string>): void

订阅数据变更，订阅的Key的值发生变更后，在执行[flush](js-apis-data-preferences.md#flush)方法后，触发callback回调。

说明

当调用[removePreferencesFromCache](js-apis-data-preferences.md#preferencesremovepreferencesfromcache)或[deletePreferences](js-apis-data-preferences.md#preferencesdeletepreferences)后，订阅的数据变更会主动取消订阅，在重新[getPreferences](js-apis-data-preferences.md#preferencesgetpreferences)后需要重新订阅数据变更。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件类型，固定值'change'，表示数据变更。 |
| callback | Callback<string> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户首选项错误码](errorcode-preferences.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let observer = (key: string) => {
4. console.info("The key " + key + " changed.");
5. }
6. dataPreferences.on('change', observer);
7. dataPreferences.putSync('startup', 'manual');
8. dataPreferences.flush((err: BusinessError) => {
9. if (err) {
10. console.error("Failed to flush. Cause: " + err);
11. return;
12. }
13. console.info("Succeeded in flushing.");
14. })
```

### on('multiProcessChange')10+

PhonePC/2in1TabletTVWearable

on(type: 'multiProcessChange', callback: Callback<string>): void

订阅进程间数据变更，多个进程持有同一个首选项文件时，在任意一个进程（包括本进程）执行[flush](js-apis-data-preferences.md#flush)方法，持久化文件发生变更后，触发callback回调。

本接口提供给申请了[dataGroupId](js-apis-data-preferences.md#options10)的应用进行使用，未申请的应用不推荐使用，多进程操作可能会损坏持久化文件，导致数据丢失。

说明

同一持久化文件在当前进程订阅进程间数据变更的最大数量为50次，超过最大限制后会订阅失败。建议在触发callback回调后及时取消订阅。

当调用[removePreferencesFromCache](js-apis-data-preferences.md#preferencesremovepreferencesfromcache)或[deletePreferences](js-apis-data-preferences.md#preferencesdeletepreferences)后，订阅的数据变更会主动取消订阅，在重新[getPreferences](js-apis-data-preferences.md#preferencesgetpreferences)后需要重新订阅数据变更。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件类型，固定值'multiProcessChange'，表示多进程间的数据变更。 |
| callback | Callback<string> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户首选项错误码](errorcode-preferences.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |
| 15500019 | Failed to obtain the subscription service. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let observer = (key: string) => {
4. console.info("The key " + key + " changed.");
5. }
6. dataPreferences.on('multiProcessChange', observer);
7. dataPreferences.putSync('startup', 'manual');
8. dataPreferences.flush((err: BusinessError) => {
9. if (err) {
10. console.error("Failed to flush. Cause: " + err);
11. return;
12. }
13. console.info("Succeeded in flushing.");
14. })
```

### on('dataChange')12+

PhonePC/2in1TabletTVWearable

on(type: 'dataChange', keys: Array<string>, callback: Callback<Record<string, ValueType>>): void

精确订阅数据变更，只有被订阅的key值发生变更后，在执行[flush](js-apis-data-preferences.md#flush)方法后，触发callback回调。

说明

当调用[removePreferencesFromCache](js-apis-data-preferences.md#preferencesremovepreferencesfromcache)或[deletePreferences](js-apis-data-preferences.md#preferencesdeletepreferences)后，订阅的数据变更会主动取消订阅，在重新[getPreferences](js-apis-data-preferences.md#preferencesgetpreferences)后需要重新订阅数据变更。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件类型，固定值'dataChange'，表示精确的数据变更。 |
| keys | Array<string> | 是 | 需要订阅的key集合。 |
| callback | Callback<Record<string, [ValueType](js-apis-data-preferences.md#valuetype)>> | 是 | 回调函数。回调支持返回多个键值对，其中键为发生变更的订阅key，值为变更后的数据：支持number、string、boolean、Array<number>、Array<string>、Array<boolean>、Uint8Array、object类型。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户首选项错误码](errorcode-preferences.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let observer = (data: Record<string, preferences.ValueType>) => {
4. for (const keyValue of Object.entries(data)) {
5. console.info(`observer : ${keyValue}`);
6. }
7. console.info("The observer called.");
8. }
9. let keys = ['name', 'age'];
10. dataPreferences.on('dataChange', keys, observer);
11. dataPreferences.putSync('name', 'xiaohong');
12. dataPreferences.putSync('weight', 125);
13. dataPreferences.flush((err: BusinessError) => {
14. if (err) {
15. console.error("Failed to flush. Cause: " + err);
16. return;
17. }
18. console.info("Succeeded in flushing.");
19. })
```

### off('change')

PhonePC/2in1TabletTVWearable

off(type: 'change', callback?: Callback<string>): void

取消订阅数据变更。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件类型，固定值'change'，表示数据变更。 |
| callback | Callback<string> | 否 | 需要取消的回调函数，不填写则全部取消。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户首选项错误码](errorcode-preferences.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let observer = (key: string) => {
4. console.info("The key " + key + " changed.");
5. }
6. dataPreferences.on('change', observer);
7. dataPreferences.putSync('startup', 'auto');
8. dataPreferences.flush((err: BusinessError) => {
9. if (err) {
10. console.error("Failed to flush. Cause: " + err);
11. return;
12. }
13. console.info("Succeeded in flushing.");
14. })
15. dataPreferences.off('change', observer);
```

### off('multiProcessChange')10+

PhonePC/2in1TabletTVWearable

off(type: 'multiProcessChange', callback?: Callback<string>): void

取消订阅进程间数据变更。

本接口提供给申请了[dataGroupId](js-apis-data-preferences.md#options10)的应用进行使用，未申请的应用不推荐使用，多进程操作可能会损坏持久化文件，导致数据丢失。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件类型，固定值'multiProcessChange'，表示多进程间的数据变更。 |
| callback | Callback<string> | 否 | 需要取消的回调函数，不填写则全部取消。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户首选项错误码](errorcode-preferences.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let observer = (key: string) => {
4. console.info("The key " + key + " changed.");
5. }
6. dataPreferences.on('multiProcessChange', observer);
7. dataPreferences.putSync('startup', 'auto');
8. dataPreferences.flush((err: BusinessError) => {
9. if (err) {
10. console.error("Failed to flush. Cause: " + err);
11. return;
12. }
13. console.info("Succeeded in flushing.");
14. })
15. dataPreferences.off('multiProcessChange', observer);
```

### off('dataChange')12+

PhonePC/2in1TabletTVWearable

off(type: 'dataChange', keys: Array<string>, callback?: Callback<Record<string, ValueType>>): void

取消精确订阅数据变更。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件类型，固定值'dataChange'，表示精确的数据变更。 |
| keys | Array<string> | 是 | 需要取消订阅的key集合，当keys为空数组时，表示取消订阅全部key；当keys为非空数组时，表示只取消订阅key集合中的key。 |
| callback | Callback<Record<string, [ValueType](js-apis-data-preferences.md#valuetype)>> | 否 | 需要取消的回调函数，若callback不填写，表示所有的callback都需要处理；若callback填写，表示只处理该callback。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户首选项错误码](errorcode-preferences.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let observer = (data: Record<string, preferences.ValueType>) => {
4. for (const keyValue of Object.entries(data)) {
5. console.info(`observer : ${keyValue}`);
6. }
7. console.info("The observer called.");
8. }
9. let keys = ['name', 'age'];
10. dataPreferences.on('dataChange', keys, observer);
11. dataPreferences.putSync('name', 'xiaohong');
12. dataPreferences.putSync('weight', 125);
13. dataPreferences.flush((err: BusinessError) => {
14. if (err) {
15. console.error("Failed to flush. Cause: " + err);
16. return;
17. }
18. console.info("Succeeded in flushing.");
19. })
20. dataPreferences.off('dataChange', keys, observer);
```

## ValueType

PhonePC/2in1TabletTVWearable

type ValueType = number | string | boolean | Array<number> | Array<string> | Array<boolean> | Uint8Array | object | bigint

表示支持的值类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

| 类型 | 说明 |
| --- | --- |
| number | 表示值类型为数字。 |
| string | 表示值类型为字符串。 |
| boolean | 表示值类型为布尔值。 |
| Array<number> | 表示值类型为数字类型的数组。 |
| Array<boolean> | 表示值类型为布尔类型的数组。 |
| Array<string> | 表示值类型为字符串类型的数组。 |
| Uint8Array11+ | 表示值类型为8位无符号整型的数组。 |
| object12+ | 表示值类型为对象。 |
| bigint12+ | 表示值类型为任意精度格式的整数。 |
