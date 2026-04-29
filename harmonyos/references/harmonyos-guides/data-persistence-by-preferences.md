---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-persistence-by-preferences
title: 通过用户首选项实现数据持久化 (ArkTS)
breadcrumb: 指南 > 应用框架 > ArkData（方舟数据管理） > 应用数据持久化 > 通过用户首选项实现数据持久化 (ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-29T13:26:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e0ad10f63c956ea64093c5d721c0ef948f40c2086c4009cfab3ec0fdddf667b3
---

## 场景介绍

用户首选项(Preferences)为应用提供Key-Value键值型的数据处理能力，支持应用持久化轻量级数据，并对其修改和查询。当用户有轻量级的键值型数据需要存储时，可以采用Preferences来进行存储。一般适用于保存用户的个性化设置，例如字体大小、是否开启夜间模式等。

## 运作机制

如图所示，用户程序通过ArkTS接口调用用户首选项读写对应的数据文件。开发者可以将用户首选项持久化文件的内容加载到Preferences实例，每个文件唯一对应到一个Preferences实例，系统会通过静态容器将该实例存储在内存中，直到主动从内存中移除该实例或删除该文件。

应用首选项的持久化文件保存在应用沙箱内部，可以通过context获取其路径。具体请参见[获取应用文件路径](application-context-stage.md#获取应用文件路径)。

**图1** 用户首选项运作机制

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/Z4rHVszfQhmxu5USQpXF0w/zh-cn_image_0000002589323881.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T052615Z&HW-CC-Expire=86400&HW-CC-Sign=CDABF64B96765322AF089F015B5228A674653466DE7697873655D12AA573EC70)

## 存储模式说明

用户首选项默认使用XML格式进行存储，从API version 18开始，可选择GSKV存储模式。

### XML存储

XML存储指的是数据会以XML的形式存储到文件中，该模式的优点是通用性强，支持跨平台。当选择该模式时，首选项对数据的操作主要发生在内存中，开发者可以在需要的时候再调用[flush](../harmonyos-references/js-apis-data-preferences.md#flush)接口进行数据持久化。针对单进程、小数据量场景，推荐使用该存储模式。

### GSKV存储

GSKV是从API version 18起提供的一种存储模式，数据以二进制的形式存储在文件中，该模式的优点是支持多进程并发读写。当选择该模式时，首选项对数据的操作会实时落盘。针对多进程并发场景，推荐使用该存储模式。

## 约束限制

### 首选项通用限制

* Key键为string类型，要求非空且长度不超过1024个字节。
* 如果Value值为string类型，请使用UTF-8编码格式，可以为空，不为空时长度不超过16MB。
* 当调用[removePreferencesFromCache](../harmonyos-references/js-apis-data-preferences.md#preferencesremovepreferencesfromcache)或者[deletePreferences](../harmonyos-references/js-apis-data-preferences.md#preferencesdeletepreferences)后，订阅的数据变更会主动取消订阅，重新[getPreferences](../harmonyos-references/js-apis-data-preferences.md#preferencesgetpreferences)后需要重新订阅数据变更。
* 不允许deletePreferences与其他接口多线程、多进程并发调用，否则可能会发生不可预期行为。
* 不支持数据加密存储。如果需要进行数据加密，应用应该先将数据进行加密，然后将密文通过Uint8Array类型存储到Preferences中。

### XML模式约束限制

* XML模式（首选项的默认模式）无法保证进程并发安全，会有文件损坏和数据丢失的风险，不支持在多进程场景下使用。
* 当存储的数据中包含非UTF-8格式的字符串时，请使用Uint8Array类型存储，否则会造成持久化文件出现格式错误造成文件损坏。
* 内存会随着存储数据量的增大而增大，所以存储的数据量应该是轻量级的，建议存储的数据不超过50MB。数据量较大时，在使用同步接口创建Preferences对象和持久化数据时会成为耗时操作，不建议在主线程中使用，否则可能会出现appfreeze问题。

### GSKV模式约束限制

* GSKV模式不支持跨平台，使用该模式前需调用[isStorageTypeSupported](../harmonyos-references/js-apis-data-preferences.md#preferencesisstoragetypesupported18)接口判断当前平台是否支持该模式。

## 接口说明

以下是用户首选项持久化功能的相关接口，更多接口及使用方式请见[用户首选项](../harmonyos-references/js-apis-data-preferences.md)。

| 接口名称 | 描述 |
| --- | --- |
| getPreferencesSync(context: Context, options: Options): Preferences | 获取Preferences实例。该接口存在异步接口。 |
| putSync(key: string, value: ValueType): void | 将数据写入Preferences实例，可通过flush将Preferences实例持久化。该接口存在异步接口。 |
| hasSync(key: string): boolean | 检查Preferences实例是否包含名为给定Key的存储键值对，true表示包含，false表示不包含。给定的Key值不能为空。该接口存在异步接口。 |
| getSync(key: string, defValue: ValueType): ValueType | 获取键对应的值，如果值为null或非默认值类型，将返回默认数据defValue。该接口存在异步接口。 |
| deleteSync(key: string): void | 从Preferences实例中删除名为给定Key的存储键值对。该接口存在异步接口。 |
| flush(callback: AsyncCallback<void>): void | 将当前Preferences实例的数据异步存储到用户首选项持久化文件中。 |
| on(type: 'change', callback: Callback<string>): void | 订阅数据变更，订阅的数据发生变更后，在执行flush方法后，触发callback回调。 |
| off(type: 'change', callback?: Callback<string>): void | 取消订阅数据变更。 |
| deletePreferences(context: Context, options: Options, callback: AsyncCallback<void>): void | 从内存中移除指定的Preferences实例。若Preferences实例有对应的持久化文件，则同时删除其持久化文件。 |
| isStorageTypeSupported(type: StorageType): boolean | 判断当前平台是否支持希望使用的存储模式。true表示支持，false表示不支持。 |

## 开发步骤

1. 导入@kit.ArkData模块。

   ```
   1. import { preferences } from '@kit.ArkData';
   ```
2. （可选）选择存储模式。

   该步骤为可选步骤。首选项默认使用XML模式存储数据，从API version 18开始，新增提供并支持使用GSKV存储模式。

   在选择GSKV存储模式之前，需要使用isStorageTypeSupported()接口判断当前平台是否支持GSKV模式。

   若接口返回false，则说明当前平台不支持GSKV模式，请使用XML模式进行数据存储。

   ```
   1. let isGskvSupported = preferences.isStorageTypeSupported(preferences.StorageType.GSKV);
   2. Logger.info('Is gskv supported on this platform: ' + isGskvSupported);
   ```
3. 获取Preferences实例。

   针对默认的XML存储模式，使用getPreferencesSync()方法获取Preferences实例。

   context的定义如下：

   ```
   1. const context = EntryAbility.getContext();
   ```

   针对默认的XML存储模式，使用getPreferencesSync()方法获取Preferences实例。

   ```
   1. import { UIAbility } from '@kit.AbilityKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. import { window } from '@kit.ArkUI';

   5. let dataPreferences: preferences.Preferences | null = null;

   7. class EntryAbility extends UIAbility {
   8. onWindowStageCreate(windowStage: window.WindowStage) {
   9. let options: preferences.Options = { name: 'myStore' };
   10. dataPreferences = preferences.getPreferencesSync(context, options);
   11. }
   12. }
   ```

   针对GSKV存储模式，使用getPreferencesSync()方法获取Preferences实例。

   若希望使用GSKV存储模式且当前平台支持该模式，可以通过以下方式获取GSKV存储模式的Preferences实例。需要注意的是，当选择某一存储模式后，不允许再对存储模式进行切换。

   ```
   1. import { UIAbility } from '@kit.AbilityKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. import { window } from '@kit.ArkUI';

   5. let dataPreferences: preferences.Preferences | null = null;

   7. class EntryAbility extends UIAbility {
   8. onWindowStageCreate(windowStage: window.WindowStage) {
   9. let options: preferences.Options = { name: 'myStore', storageType: preferences.StorageType.GSKV };
   10. dataPreferences = preferences.getPreferencesSync(context, options);
   11. }
   12. }
   ```
4. 写入数据。

   使用putSync()方法将数据写入Preferences实例中。

   针对默认存储模式（XML存储模式），在写入数据后，如有需要，可使用flush()方法将Preferences实例的数据存储到持久化文件。

   针对GSKV存储模式，在写入数据后，数据会实时持久化到文件中。

   说明

   当对应的键已经存在时，putSync()方法会覆盖其值。可以使用hasSync()方法检查是否存在对应键值对。

   示例代码如下所示：

   ```
   1. if (dataPreferences.hasSync('startup')) {
   2. Logger.info('The key startup is contained.');
   3. } else {
   4. Logger.info('The key startup does not contain.');
   5. // 此处以此键值对不存在时写入数据为例
   6. dataPreferences.putSync('startup', 'auto');
   7. // 在XML模式下，当字符串包含非UTF-8格式的字符时，需要将字符串转为Uint8Array类型再存储，长度均不超过16 * 1024 * 1024个字节。
   8. let uInt8Array1 = new util.TextEncoder().encodeInto('~！@#￥%……&*（）——+？');
   9. dataPreferences.putSync('uInt8', uInt8Array1);
   10. }
   ```
5. 读取数据。

   使用getSync()方法获取数据，即指定键对应的值。如果值为null或非默认值类型，则返回默认数据。

   示例代码如下所示：

   ```
   1. let val = dataPreferences.getSync('startup', 'default');
   2. Logger.info('The startup value is ' + val);
   3. let uInt8Array2 : preferences.ValueType = dataPreferences.getSync('uInt8', new Uint8Array(0));
   4. // 将获取到的Uint8Array转换为字符串
   5. let textDecoder = util.TextDecoder.create('utf-8');
   6. val = textDecoder.decodeToString(uInt8Array2 as Uint8Array);
   7. Logger.info('The uInt8 value is ' + val);
   ```
6. 删除数据。

   使用deleteSync()方法删除指定键值对，示例代码如下所示：

   ```
   1. dataPreferences.deleteSync('startup');
   ```
7. 数据持久化。

   应用存入数据到Preferences实例后，可以使用flush()方法实现数据持久化。示例代码如下所示：

   ```
   1. dataPreferences.flush((err: BusinessError) => {
   2. if (err) {
   3. Logger.error(`Failed to flush. Code:${err.code}, message:${err.message}`);
   4. return;
   5. }
   6. Logger.info('Succeeded in flushing.');
   7. })
   ```
8. 订阅数据变更。

   应用订阅数据变更需要指定observer作为回调方法。

   针对首选项的默认存储模式（XML存储模式），订阅的Key值发生变更后，当执行flush()方法时，触发observer回调。

   示例代码如下所示：

   ```
   1. let observer = (key: string) => {
   2. Logger.info('The key ' + key + ' changed.');
   3. }
   4. dataPreferences.on('change', observer);
   5. // 数据产生变更，由'auto'变为'manual'
   6. dataPreferences.put('startup', 'manual', (err: BusinessError) => {
   7. if (err) {
   8. Logger.error(`Failed to put the value of 'startup'. Code:${err.code},message:${err.message}`);
   9. return;
   10. }
   11. Logger.info('Succeeded in putting the value of startup.');
   12. if (dataPreferences !== null) {
   13. dataPreferences.flush((err: BusinessError) => {
   14. if (err) {
   15. Logger.error(`Failed to flush. Code:${err.code}, message:${err.message}`);
   16. return;
   17. }
   18. Logger.info('Succeeded in flushing.');
   19. })
   20. }
   21. })
   ```

   针对GSKV存储模式，订阅的Key值发生变更后（无需调用flush），observer被触发回调。

   示例代码如下所示：

   ```
   1. let observer = (key: string) => {
   2. Logger.info('The key ' + key + ' changed.');
   3. }
   4. dataPreferences.on('change', observer);
   5. // 数据产生变更，由'auto'变为'manual'
   6. dataPreferences.put('startup', 'manual', (err: BusinessError) => {
   7. if (err) {
   8. Logger.error(`Failed to put the value of 'startup'. Code:${err.code},message:${err.message}`);
   9. return;
   10. }
   11. Logger.info('Succeeded in putting the value of startup.');
   12. })
   ```
9. 删除指定文件。

   使用deletePreferences()方法从内存中移除指定文件对应的Preferences实例及其数据。若该Preference存在对应的持久化文件，则一并删除，包括指定文件及其备份文件、损坏文件。

   说明

   * 调用该接口后，应用不允许再使用该Preferences实例进行数据操作，否则会出现数据一致性问题。
   * 成功删除后，数据及文件将不可恢复。
   * 在GSKV模式中，该接口不支持与其他接口并发调用（包括多进程），否则会出现不可预期行为。

   context的定义如下：

   ```
   1. const context = EntryAbility.getContext();
   ```

   示例代码如下所示：

   ```
   1. let options: preferences.Options = { name: 'myStore' };
   2. preferences.deletePreferences(context, options, (err: BusinessError) => {
   3. if (err) {
   4. Logger.error(`Failed to delete preferences. Code:${err.code}, message:${err.message}`);
   5. return;
   6. }
   7. Logger.info('Succeeded in deleting preferences.');
   8. })
   ```

## 示例代码

* [首选项](https://gitcode.com/HarmonyOS_Samples/preferences)
