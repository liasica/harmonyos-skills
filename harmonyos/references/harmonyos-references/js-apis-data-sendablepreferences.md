---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-sendablepreferences
title: @ohos.data.sendablePreferences (共享用户首选项)
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > ArkTS API > @ohos.data.sendablePreferences (共享用户首选项)
category: harmonyos-references
scraped_at: 2026-04-28T07:59:15+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:36b9ee79a972974cb57f5684582e93f7f91b0e5f5ff6ebc70d974e3a85403280
---

共享用户首选项为应用提供Key-Value键值型的数据处理能力，支持应用持久化轻量级数据，并对其修改和查询。

数据存储形式为键值对，键的类型为字符串型，值的存储数据类型包括number、string、boolean、bigint以及可序列化的object。

共享用户首选项的持久化文件存储在[preferencesDir](../harmonyos-guides/application-context-stage.md#获取应用文件路径)路径下，创建preferences对象前，需要保证preferencesDir路径可读写。持久化文件存储路径中的[加密等级](js-apis-app-ability-contextconstant.md#areamode)会影响文件的可读写状态，路径访问限制详见[应用文件目录与应用文件路径](../harmonyos-guides/app-sandbox-directory.md#应用文件目录与应用文件路径)。

共享用户首选项可以在ArkTS并发实例间（包括主线程、TaskPool&Worker工作线程）传递，传递的行为是引用传递，性能优于普通的[用户首选项](js-apis-data-preferences.md)，可参考[Sendable使用场景](../harmonyos-guides/sendable-guide.md)。

说明

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

共享用户首选项无法保证进程并发安全，会有文件损坏和数据丢失的风险，不支持在多进程场景下使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { sendablePreferences } from '@kit.ArkData';
```

## 常量

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

| 名称 | 类型 | 只读 | 说明 |
| --- | --- | --- | --- |
| MAX\_KEY\_LENGTH | number | 是 | Key的最大长度限制为1024个字节。 |
| MAX\_VALUE\_LENGTH | number | 是 | Value的最大长度限制为16MB。 |

## sendablePreferences.getPreferences

PhonePC/2in1TabletTVWearable

getPreferences(context: Context, options: Options): Promise<Preferences>

获取Preferences实例，使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 应用上下文。 |
| options | [Options](js-apis-data-sendablepreferences.md#options) | 是 | 与Preferences实例相关的配置选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Preferences](js-apis-data-sendablepreferences.md#preferences)> | Promise对象，返回Preferences实例。  该实例继承[ISendable](../harmonyos-guides/arkts-sendable.md#isendable)，可以在ArkTS并发实例间（包括主线程、TaskPool&Worker工作线程）传递，传递的行为是引用传递，参考[Sendable使用场景](../harmonyos-guides/sendable-guide.md)。 |

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

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { window } from '@kit.ArkUI';

5. let preferences: sendablePreferences.Preferences;

7. class EntryAbility extends UIAbility {
8. onWindowStageCreate(windowStage: window.WindowStage) {
9. let options: sendablePreferences.Options = { name: 'myStore' };
10. let promise = sendablePreferences.getPreferences(this.context, options);
11. promise.then((object: sendablePreferences.Preferences) => {
12. preferences = object;
13. console.info("Succeeded in getting preferences.");
14. }).catch((err: BusinessError) => {
15. console.error(`Failed to get preferences. code: ${err.code}, message: ${err.message}`);
16. });
17. }
18. }
```

## sendablePreferences.getPreferencesSync

PhonePC/2in1TabletTVWearable

getPreferencesSync(context: Context, options: Options): Preferences

获取Preferences实例，此为同步接口。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 应用上下文。 |
| options | [Options](js-apis-data-sendablepreferences.md#options) | 是 | 与Preferences实例相关的配置选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Preferences](js-apis-data-sendablepreferences.md#preferences) | 返回Preferences实例。  该实例继承[ISendable](../harmonyos-guides/arkts-sendable.md#isendable)，可以在ArkTS并发实例间（包括主线程、TaskPool&Worker工作线程）传递，传递的行为是引用传递，参考[Sendable使用场景](../harmonyos-guides/sendable-guide.md)。 |

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

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';

4. let preferences: sendablePreferences.Preferences;

6. class EntryAbility extends UIAbility {
7. onWindowStageCreate(windowStage: window.WindowStage) {
8. let options: sendablePreferences.Options = { name: 'myStore' };
9. preferences = sendablePreferences.getPreferencesSync(this.context, options);
10. }
11. }
```

## sendablePreferences.deletePreferences

PhonePC/2in1TabletTVWearable

deletePreferences(context: Context, options: Options): Promise<void>

从缓存中删除指定的Preferences实例，若Preferences实例有对应的持久化文件，则同时删除其持久化文件。使用Promise异步回调。

调用该接口后，不建议再使用旧的Preferences实例进行数据操作，否则会导致数据一致性问题。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 应用上下文。 |
| options | [Options](js-apis-data-sendablepreferences.md#options) | 是 | 与Preferences实例相关的配置选项。 |

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

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { window } from '@kit.ArkUI';

5. class EntryAbility extends UIAbility {
6. onWindowStageCreate(windowStage: window.WindowStage) {
7. let options: sendablePreferences.Options = { name: 'myStore' };
8. let promise = sendablePreferences.deletePreferences(this.context, options);
9. promise.then(() => {
10. console.info("Succeeded in deleting preferences.");
11. }).catch((err: BusinessError) => {
12. console.error(`Failed to delete preferences. code: ${err.code}, message: ${err.message}`);
13. });
14. }
15. }
```

## sendablePreferences.removePreferencesFromCache

PhonePC/2in1TabletTVWearable

removePreferencesFromCache(context: Context, options: Options): Promise<void>

从缓存中移除指定的Preferences实例，使用Promise异步回调。

应用首次调用[getPreferences](js-apis-data-sendablepreferences.md#sendablepreferencesgetpreferences)接口获取某个Preferences实例后，该实例会被缓存起来，后续调用[getPreferences](js-apis-data-sendablepreferences.md#sendablepreferencesgetpreferences)时不会再次从持久化文件中读取，直接从缓存中获取Preferences实例。调用此接口移除缓存中的实例之后，再次getPreferences将会重新读取持久化文件，生成新的Preferences实例。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 应用上下文。 |
| options | [Options](js-apis-data-sendablepreferences.md#options) | 是 | 与Preferences实例相关的配置选项。 |

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

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { window } from '@kit.ArkUI';

5. class EntryAbility extends UIAbility {
6. onWindowStageCreate(windowStage: window.WindowStage) {
7. let options: sendablePreferences.Options = { name: 'myStore' };
8. let promise = sendablePreferences.removePreferencesFromCache(this.context, options);
9. promise.then(() => {
10. console.info("Succeeded in removing preferences.");
11. }).catch((err: BusinessError) => {
12. console.error(`Failed to remove preferences. code: ${err.code}, message: ${err.message}`);
13. });
14. }
15. }
```

## sendablePreferences.removePreferencesFromCacheSync

PhonePC/2in1TabletTVWearable

removePreferencesFromCacheSync(context: Context, options: Options):void

从缓存中移除指定的Preferences实例，此为同步接口。

应用首次调用[getPreferences](js-apis-data-sendablepreferences.md#sendablepreferencesgetpreferences)接口获取某个Preferences实例后，该实例会被缓存起来，后续调用[getPreferences](js-apis-data-sendablepreferences.md#sendablepreferencesgetpreferences)时不会再次从持久化文件中读取，直接从缓存中获取Preferences实例。调用此接口移除缓存中的实例之后，再次getPreferences将会重新读取持久化文件，生成新的Preferences实例。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 应用上下文。 |
| options | [Options](js-apis-data-sendablepreferences.md#options) | 是 | 与Preferences实例相关的配置选项。 |

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

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';

4. class EntryAbility extends UIAbility {
5. onWindowStageCreate(windowStage: window.WindowStage) {
6. let options: sendablePreferences.Options = { name: 'myStore' };
7. sendablePreferences.removePreferencesFromCacheSync(this.context, options);
8. }
9. }
```

## Options

PhonePC/2in1TabletTVWearable

Preferences实例配置选项。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 否 | 否 | Preferences实例的名称。 |
| dataGroupId | string|null | 否 | 是 | 应用组ID，需要向应用市场获取，详见[dataGroupId申请流程](../harmonyos-guides/ime-kit-security.md#共享沙箱介绍)。基于dataGroupId的数据共享支持两种场景：1.同一应用的不同进程间共享，只支持三方应用中输入法和输入法的扩展场景使用；2.不同应用间的数据共享，只支持系统应用使用。  为可选参数。指定在此dataGroupId对应的沙箱路径下创建Preferences实例。当此参数不填时，默认在本应用沙箱目录下创建Preferences实例。  **模型约束：** 此属性仅在Stage模型下可用。 |

## Preferences

PhonePC/2in1TabletTVWearable

Preferences继承自[ISendable](../harmonyos-guides/arkts-sendable.md#isendable)，可以在ArkTS并发实例间（包括主线程、TaskPool&Worker工作线程）传递，传递的行为是引用传递，提供获取和修改存储数据的接口。

下列接口都需先使用[sendablePreferences.getPreferences](js-apis-data-sendablepreferences.md#sendablepreferencesgetpreferences)获取到Preferences实例，再通过此实例调用对应接口。

### get

PhonePC/2in1TabletTVWearable

get(key: string, defValue: lang.ISendable): Promise<lang.ISendable>

从缓存的Preferences实例中获取键对应的值，如果值为null或者非默认值类型，返回默认数据defValue，使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要获取的存储Key名称，不能为空，最大长度限制为[MAX\_KEY\_LENGTH](js-apis-data-sendablepreferences.md#常量)。 |
| defValue | [lang.ISendable](../harmonyos-guides/arkts-sendable.md#isendable) | 是 | 默认返回值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[lang.ISendable](../harmonyos-guides/arkts-sendable.md#isendable)> | Promise对象，返回键对应的值。  该实例继承[ISendable](../harmonyos-guides/arkts-sendable.md#isendable)，可以在ArkTS并发实例间（包括主线程、TaskPool&Worker工作线程）传递，传递的行为是引用传递，参考[Sendable使用场景](../harmonyos-guides/sendable-guide.md)。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户首选项错误码](errorcode-preferences.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { lang } from '@kit.ArkTS';

4. let promise = preferences.get('startup', 'default');
5. promise.then((data: lang.ISendable) => {
6. let dataStr = data as string;
7. console.info(`Succeeded in getting value of 'startup'. Data: ${dataStr}`);
8. }).catch((err: BusinessError) => {
9. console.error(`Failed to get value of 'startup'. code: ${err.code}, message: ${err.message}`);
10. });
```

### getSync

PhonePC/2in1TabletTVWearable

getSync(key: string, defValue: lang.ISendable): lang.ISendable

从缓存的Preferences实例中获取键对应的值，如果值为null或者非默认值类型，返回默认数据defValue，此为同步接口。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要获取的存储Key名称，不能为空，最大长度限制为[MAX\_KEY\_LENGTH](js-apis-data-sendablepreferences.md#常量)。 |
| defValue | [lang.ISendable](../harmonyos-guides/arkts-sendable.md#isendable) | 是 | 默认返回值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [lang.ISendable](../harmonyos-guides/arkts-sendable.md#isendable) | 返回键对应的值。  该实例继承[ISendable](../harmonyos-guides/arkts-sendable.md#isendable)，可以在ArkTS并发实例间（包括主线程、TaskPool&Worker工作线程）传递，传递的行为是引用传递，参考[Sendable使用场景](../harmonyos-guides/sendable-guide.md)。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户首选项错误码](errorcode-preferences.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**示例：**

```
1. import { lang } from '@kit.ArkTS';
2. let value: lang.ISendable = preferences.getSync('startup', 'default');
```

### getAll

PhonePC/2in1TabletTVWearable

getAll(): Promise<lang.ISendable>

获取缓存的Preferences实例中的所有键值数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[lang.ISendable](../harmonyos-guides/arkts-sendable.md#isendable)> | Promise对象，返回所有包含的键值数据。  该对象继承[ISendable](../harmonyos-guides/arkts-sendable.md#isendable)，可以在ArkTS并发实例间（包括主线程、TaskPool&Worker工作线程）传递，传递的行为是引用传递，参考[Sendable使用场景](../harmonyos-guides/sendable-guide.md)。 |

**错误码：**

以下错误码的详细介绍请参见[用户首选项错误码](errorcode-preferences.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 15500000 | Inner error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { lang } from '@kit.ArkTS';

4. let promise = preferences.getAll();
5. promise.then((keyValues: lang.ISendable) => {
6. for (let value of Object.keys(keyValues)) {
7. console.info("getAll " + JSON.stringify(value));
8. }
9. }).catch((err: BusinessError) => {
10. console.error(`Failed to get all key-values. code: ${err.code}, message: ${err.message}`);
11. });
```

### getAllSync

PhonePC/2in1TabletTVWearable

getAllSync(): lang.ISendable

获取缓存的Preferences实例中的所有键值数据，此为同步接口。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [lang.ISendable](../harmonyos-guides/arkts-sendable.md#isendable) | 返回所有包含的键值数据。  该对象继承[ISendable](../harmonyos-guides/arkts-sendable.md#isendable)，可以在ArkTS并发实例间（包括主线程、TaskPool&Worker工作线程）传递，传递的行为是引用传递，参考[Sendable使用场景](../harmonyos-guides/sendable-guide.md)。 |

**错误码：**

以下错误码的详细介绍请参见[用户首选项错误码](errorcode-preferences.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 15500000 | Inner error. |

**示例：**

```
1. import { lang } from '@kit.ArkTS';

3. let keyValues: lang.ISendable = preferences.getAllSync();
4. for (let value of Object.keys(keyValues)) {
5. console.info("getAll " + JSON.stringify(value));
6. }
```

### put

PhonePC/2in1TabletTVWearable

put(key: string, value: lang.ISendable): Promise<void>

将数据写入缓存的Preferences实例中，可通过[flush](js-apis-data-sendablepreferences.md#flush)将Preferences实例持久化，使用Promise异步回调。

说明

当value中包含非UTF-8格式的字符串时，请使用Uint8Array类型存储，否则会造成持久化文件出现格式错误造成文件损坏。

当对应的键已经存在时，put()方法会覆盖其值。可以使用hasSync()方法检查是否存在对应键值对。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要修改的存储的Key，不能为空，最大长度限制为[MAX\_KEY\_LENGTH](js-apis-data-sendablepreferences.md#常量)。 |
| value | [lang.ISendable](../harmonyos-guides/arkts-sendable.md#isendable) | 是 | 存储的新值。 |

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

3. let promise = preferences.put('startup', 'auto');
4. promise.then(() => {
5. console.info("Succeeded in putting value of 'startup'.");
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to put value of 'startup'. code: ${err.code}, message: ${err.message}`);
8. });
```

### putSync

PhonePC/2in1TabletTVWearable

putSync(key: string, value: lang.ISendable): void

将数据写入缓存的Preferences实例中，可通过[flush](js-apis-data-sendablepreferences.md#flush)将Preferences实例持久化，此为同步接口。

说明

当value中包含非UTF-8格式的字符串时，请使用Uint8Array类型存储，否则会造成持久化文件出现格式错误造成文件损坏。

当对应的键已经存在时，putSync()方法会覆盖其值。可以使用hasSync()方法检查是否存在对应键值对。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要修改的存储的Key，不能为空，最大长度限制为[MAX\_KEY\_LENGTH](js-apis-data-sendablepreferences.md#常量)。 |
| value | [lang.ISendable](../harmonyos-guides/arkts-sendable.md#isendable) | 是 | 存储的新值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户首选项错误码](errorcode-preferences.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**示例：**

```
1. preferences.putSync('startup', 'auto');
```

### has

PhonePC/2in1TabletTVWearable

has(key: string): Promise<boolean>

检查缓存的Preferences实例中是否包含名为给定Key的存储键值对，使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要检查的存储key名称，不能为空，最大长度限制为[MAX\_KEY\_LENGTH](js-apis-data-sendablepreferences.md#常量)。 |

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

3. let promise = preferences.has('startup');
4. promise.then((val: boolean) => {
5. if (val) {
6. console.info("The key 'startup' is contained.");
7. } else {
8. console.error("The key 'startup' does not contain.");
9. }
10. }).catch((err: BusinessError) => {
11. console.error(`Failed to check the key 'startup'. code: ${err.code}, message: ${err.message}`);
12. });
```

### hasSync

PhonePC/2in1TabletTVWearable

hasSync(key: string): boolean

检查缓存的Preferences实例中是否包含名为给定Key的存储键值对，此为同步接口。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要检查的存储key名称，不能为空，最大长度限制为[MAX\_KEY\_LENGTH](js-apis-data-sendablepreferences.md#常量)。 |

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
1. let isExist: boolean = preferences.hasSync('startup');
2. if (isExist) {
3. console.info("The key 'startup' is contained.");
4. } else {
5. console.error("The key 'startup' does not contain.");
6. }
```

### delete

PhonePC/2in1TabletTVWearable

delete(key: string): Promise<void>

从缓存的Preferences实例中删除名为给定Key的存储键值对，可通过[flush](js-apis-data-sendablepreferences.md#flush)将Preferences实例持久化，使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要删除的存储key名称，不能为空，最大长度限制为[MAX\_KEY\_LENGTH](js-apis-data-sendablepreferences.md#常量)。 |

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

3. let promise = preferences.delete('startup');
4. promise.then(() => {
5. console.info("Succeeded in deleting the key 'startup'.");
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to delete the key 'startup'. code: ${err.code}, message: ${err.message}`);
8. });
```

### deleteSync

PhonePC/2in1TabletTVWearable

deleteSync(key: string): void

从缓存的Preferences实例中删除名为给定Key的存储键值对，可通过[flush](js-apis-data-sendablepreferences.md#flush)将Preferences实例持久化，此为同步接口。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要删除的存储key名称，不能为空，最大长度限制为[MAX\_KEY\_LENGTH](js-apis-data-sendablepreferences.md#常量)。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户首选项错误码](errorcode-preferences.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**示例：**

```
1. preferences.deleteSync('startup');
```

### flush

PhonePC/2in1TabletTVWearable

flush(): Promise<void>

将缓存的Preferences实例中的数据异步存储到共享用户首选项的持久化文件中，使用Promise异步回调。

说明

当数据未修改或修改后的数据与缓存数据一致时，不会刷新持久化文件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

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

3. let promise = preferences.flush();
4. promise.then(() => {
5. console.info("Succeeded in flushing.");
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to flush. code: ${err.code}, message: ${err.message}`);
8. });
```

### flushSync14+

PhonePC/2in1TabletTVWearable

flushSync(): void

将缓存的Preferences实例中的数据存储到共享用户首选项的持久化文件中。

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
1. preferences.flushSync();
```

### clear

PhonePC/2in1TabletTVWearable

clear(): Promise<void>

清除缓存的Preferences实例中的所有数据，可通过[flush](js-apis-data-sendablepreferences.md#flush)将Preferences实例持久化，使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

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

3. let promise = preferences.clear();
4. promise.then(() => {
5. console.info("Succeeded in clearing.");
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to clear. code: ${err.code}, message: ${err.message}`);
8. });
```

### clearSync

PhonePC/2in1TabletTVWearable

clearSync(): void

清除缓存的Preferences实例中的所有数据，可通过[flush](js-apis-data-sendablepreferences.md#flush)将Preferences实例持久化，此为同步接口。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**错误码：**

以下错误码的详细介绍请参见[用户首选项错误码](errorcode-preferences.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 15500000 | Inner error. |

**示例：**

```
1. preferences.clearSync();
```

### on('change')

PhonePC/2in1TabletTVWearable

on(type: 'change', callback: Callback<string>): void

订阅数据变更，订阅的Key的值发生变更后，在执行[flush](js-apis-data-sendablepreferences.md#flush)方法后，触发callback回调。

说明

当调用[removePreferencesFromCache](js-apis-data-sendablepreferences.md#sendablepreferencesremovepreferencesfromcache)或者[deletePreferences](js-apis-data-sendablepreferences.md#sendablepreferencesdeletepreferences)后，订阅的数据变更会主动取消订阅，在重新[getPreferences](js-apis-data-sendablepreferences.md#sendablepreferencesgetpreferences)后需要重新订阅数据变更。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件类型，固定值'change'，表示数据变更。 |
| callback | Callback<string> | 是 | 回调函数。返回发生变更的Key。 |

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
5. };
6. preferences.on('change', observer);
7. preferences.putSync('startup', 'manual');
8. preferences.flush().then(() => {
9. console.info("Succeeded in flushing.");
10. }).catch((err: BusinessError) => {
11. console.error(`Failed to flush. code: ${err.code}, message: ${err.message}`);
12. });
```

### on('multiProcessChange')

PhonePC/2in1TabletTVWearable

on(type: 'multiProcessChange', callback: Callback<string>): void

订阅进程间数据变更，多个进程持有同一个首选项文件时，在任意一个进程（包括本进程）执行[flush](js-apis-data-sendablepreferences.md#flush)方法，持久化文件发生变更后，触发callback回调。

本接口提供给申请了[dataGroupId](js-apis-data-sendablepreferences.md#options)的应用进行使用，未申请的应用不推荐使用，多进程操作可能会损坏持久化文件，导致数据丢失。

说明

同一持久化文件在当前进程订阅进程间数据变更的最大数量为50次，超过最大限制后会订阅失败。建议在触发callback回调后及时取消订阅。

当调用[removePreferencesFromCache](js-apis-data-sendablepreferences.md#sendablepreferencesremovepreferencesfromcache)或者[deletePreferences](js-apis-data-sendablepreferences.md#sendablepreferencesdeletepreferences)后，订阅的数据变更会主动取消订阅，在重新[getPreferences](js-apis-data-sendablepreferences.md#sendablepreferencesgetpreferences)后需要重新订阅数据变更。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件类型，固定值'multiProcessChange'，表示多进程间的数据变更。 |
| callback | Callback<string> | 是 | 回调函数。返回发生变更的Key。 |

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
5. };
6. preferences.on('multiProcessChange', observer);
7. preferences.putSync('startup', 'manual');
8. preferences.flush().then(() => {
9. console.info("Succeeded in flushing.");
10. }).catch((err: BusinessError) => {
11. console.error(`Failed to flush. code: ${err.code}, message: ${err.message}`);
12. });
```

### on('dataChange')

PhonePC/2in1TabletTVWearable

on(type: 'dataChange', keys: Array<string>, callback: Callback<lang.ISendable>): void

精确订阅数据变更，只有被订阅的key值发生变更后，在执行[flush](js-apis-data-sendablepreferences.md#flush)方法后，触发callback回调。

说明

当调用[removePreferencesFromCache](js-apis-data-sendablepreferences.md#sendablepreferencesremovepreferencesfromcache)或者[deletePreferences](js-apis-data-sendablepreferences.md#sendablepreferencesdeletepreferences)后，订阅的数据变更会主动取消订阅，在重新[getPreferences](js-apis-data-sendablepreferences.md#sendablepreferencesgetpreferences)后需要重新订阅数据变更。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件类型，固定值'dataChange'，表示精确的数据变更。 |
| keys | Array<string> | 是 | 需要订阅的key集合。 |
| callback | Callback<[lang.ISendable](../harmonyos-guides/arkts-sendable.md#isendable)> | 是 | 回调函数。回调支持返回多个键值对，其中键为发生变更的订阅key，值为变更后的数据：支持number、string、boolean、bigint以及可序列化的object。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户首选项错误码](errorcode-preferences.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { lang } from '@kit.ArkTS';

4. let observer = (data: lang.ISendable) => {
5. console.info(`observer : ${data}`);
6. };
7. let keys = ['name', 'age'];
8. preferences.on('dataChange', keys, observer);
9. preferences.putSync('name', 'xiaohong');
10. preferences.putSync('weight', 125);
11. preferences.flush().then(() => {
12. console.info("Succeeded in flushing.");
13. }).catch((err: BusinessError) => {
14. console.error(`Failed to flush. code: ${err.code}, message: ${err.message}`);
15. });
```

### off('change')

PhonePC/2in1TabletTVWearable

off(type: 'change', callback?: Callback<string>): void

取消订阅数据变更。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

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
5. };
6. preferences.on('change', observer);
7. preferences.putSync('startup', 'auto');
8. preferences.flush().then(() => {
9. console.info("Succeeded in flushing.");
10. preferences.off('change', observer);
11. }).catch((err: BusinessError) => {
12. console.error(`Failed to flush. code: ${err.code}, message: ${err.message}`);
13. });
```

### off('multiProcessChange')

PhonePC/2in1TabletTVWearable

off(type: 'multiProcessChange', callback?: Callback<string>): void

取消订阅进程间数据变更。

本接口提供给申请了[dataGroupId](js-apis-data-sendablepreferences.md#options)的应用进行使用，未申请的应用不推荐使用，多进程操作可能会损坏持久化文件，导致数据丢失。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

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
5. };
6. preferences.on('multiProcessChange', observer);
7. preferences.putSync('startup', 'auto');
8. preferences.flush().then(() => {
9. console.info("Succeeded in flushing.");
10. preferences.off('multiProcessChange', observer);
11. }).catch((err: BusinessError) => {
12. console.error(`Failed to flush. code: ${err.code}, message: ${err.message}`);
13. });
```

### off('dataChange')

PhonePC/2in1TabletTVWearable

off(type: 'dataChange', keys: Array<string>, callback?: Callback<lang.ISendable>): void

取消精确订阅数据变更。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件类型，固定值'dataChange'，表示精确的数据变更。 |
| keys | Array<string> | 是 | 需要取消订阅的key集合，当keys为空数组时，表示取消订阅全部key；当keys为非空数组时，表示只取消订阅key集合中的key。 |
| callback | Callback<[lang.ISendable](../harmonyos-guides/arkts-sendable.md#isendable)> | 否 | 需要取消的回调函数，若callback不填写，表示所有的callback都需要处理；若callback填写，表示只处理该callback。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户首选项错误码](errorcode-preferences.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { lang } from '@kit.ArkTS';

4. let observer = (data: lang.ISendable) => {
5. console.info(`observer : ${data}`);
6. };
7. let keys = ['name', 'age'];
8. preferences.on('dataChange', keys, observer);
9. preferences.putSync('name', 'xiaohong');
10. preferences.putSync('weight', 125);
11. preferences.flush().then(() => {
12. console.info("Succeeded in flushing.");
13. preferences.off('dataChange', keys, observer);
14. }).catch((err: BusinessError) => {
15. console.error(`Failed to flush. code: ${err.code}, message: ${err.message}`);
16. });
```
