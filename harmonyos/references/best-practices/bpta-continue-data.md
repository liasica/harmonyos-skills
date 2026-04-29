---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-continue-data
title: 应用接续数据迁移
breadcrumb: 最佳实践 > 自由流转 > 跨端迁移 > 应用接续数据迁移
category: best-practices
scraped_at: 2026-04-29T14:12:39+08:00
doc_updated_at: 2026-04-01
content_hash: sha256:bcc6bd1caed5a27d38b4b949b1e243b58801c4bcdf4e2ea959a2812771b5476a
---

## 概述

在应用接续实践过程中，需要选择合适的数据迁移方案进行迁移，迁移方案的选择与数据大小和是否涉及文件迁移有直接关系，选择方案如下：

|  | <100kb | >100kb |
| --- | --- | --- |
| 需要文件迁移 | [文件资产迁移](bpta-continue-data.md#section126685428435) | [文件资产迁移](bpta-continue-data.md#section126685428435) |
| 不需要文件迁移 | [使用want.param数据迁移](bpta-continue-data.md#section189241454175710) | [基础数据迁移](bpta-continue-data.md#section4145153364317) |

## 实现原理

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/TKU7lybAQHmeEq8umLE9XQ/zh-cn_image_0000002533352060.png?HW-CC-KV=V1&HW-CC-Date=20260429T061236Z&HW-CC-Expire=86400&HW-CC-Sign=2429EAE7AEF08AEF07102BAE38912D392E1C4858A38BF9DB0B8097F9B723EFD1 "点击放大")

实现原理见[运作机制](bpta-continue-cast.md#section1218874218264)。

## 开发步骤

接入应用接续需要[启用应用接续能力](bpta-continue-cast.md#section15192222815)、[配置应用启动模式类型](bpta-continue-cast.md#section10604645308)、[源端保存迁移数据](bpta-continue-cast.md#section634613594303)和[对端恢复数据](bpta-continue-cast.md#section12346113618453)，具体开发流程见[应用接续概述](bpta-continue-cast.md)，本文只关注在不同场景下迁移数据方案的选择。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/X9wtNLttQmCZ4Ogjo9KHZw/zh-cn_image_0000002533512004.png?HW-CC-KV=V1&HW-CC-Date=20260429T061236Z&HW-CC-Expire=86400&HW-CC-Sign=5CCC1474EAFA0FF3570472F99047DF3D1AC507C41AA72EBA4E990A67F1D921B8)

## 使用want.param数据迁移

1. 源端保存迁移数据

   ```
   1. // ...
   2. export default class EntryAbility extends UIAbility {
   3. // ...
   4. onContinue(wantParam: Record<string, Object>) {
   5. const continueInput = '迁移的数据';
   6. if (continueInput) {
   7. wantParam['data'] = continueInput;
   8. }
   9. // ...
   10. return AbilityConstant.OnContinueResult.AGREE;
   11. }
   12. // ...
   13. }
   ```
2. 对端恢复数据

   ```
   1. export default class EntryAbility extends UIAbility {
   2. storage: LocalStorage = new LocalStorage();
   3. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
   4. if (launchParam.launchReason === AbilityConstant.LaunchReason.CONTINUATION) {
   5. let continueInput = '';
   6. if (want.parameters !== undefined) {
   7. continueInput = JSON.stringify(want.parameters.data);
   8. console.info(`continue input ${continueInput}`)
   9. }
   10. // ...
   11. this.context.restoreWindowStage(this.storage);
   12. }
   13. // ...
   14. }

   16. // ...
   17. }
   ```

## 使用分布式对象迁移数据

### 基础数据迁移

1. 源端保存迁移数据

   在源端UIAbility的[onContinue()](../harmonyos-references/js-apis-app-ability-uiability.md#oncontinue)接口中创建分布式数据对象并保存数据，执行流程如下：

   1. 在onContinue()接口中使用create()接口创建分布式数据对象，将所要迁移的数据填充到分布式数据对象中。
   2. 调用genSessionId()接口生成分布式数据对象组网id，分布式数据对象调用setSessionId()方法将id传入，激活分布式数据对象。
   3. 使用save()接口将已激活的分布式数据对象持久化，确保源端退出后对端依然可以获取到数据。
   4. 将生成的sessionId通过want传递到对端，供对端激活同步使用。

   说明

   * 分布式数据对象需要先激活，再持久化，因此必须在调用setSessionId()后再调用save()接口。
   * 对于源端迁移后需要退出的应用，为了防止数据未保存完成应用就退出，应采用await的方式等待save()接口执行完毕。从API12 起，onContinue()接口提供了async版本供该场景使用。
   * 当前，wantParams中“sessionId”字段在迁移流程中被系统占用，建议开发者在wantParams中定义其他key值存储该分布式数据对象生成的id，避免数据异常。

   ```
   1. import { UIAbility, AbilityConstant, Want } from '@kit.AbilityKit';
   2. import { distributedDataObject } from '@kit.ArkData';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   4. import { hilog } from '@kit.PerformanceAnalysisKit';
   5. // ...

   7. const TAG: string = '[MigrationAbility]';
   8. const DOMAIN_NUMBER: number = 0xFF00;
   9. class ParentObject {
   10. mother: string
   11. father: string

   13. constructor(mother: string, father: string) {
   14. this.mother = mother
   15. this.father = father
   16. }
   17. }

   19. class SourceObject {
   20. name: string | undefined
   21. age: number | undefined
   22. isVis: boolean | undefined
   23. parent: ParentObject | undefined

   25. constructor(name: string | undefined, age: number | undefined, isVis: boolean | undefined, parent: ParentObject | undefined) {
   26. this.name = name
   27. this.age = age
   28. this.isVis = isVis
   29. this.parent = parent
   30. }
   31. }

   33. export default class MigrationAbility extends UIAbility {
   34. d_object?: distributedDataObject.DataObject;
   35. // ...

   37. // ...

   39. async onContinue(wantParam: Record<string, Object>): Promise<AbilityConstant.OnContinueResult> {
   40. // ...
   41. let parentSource: ParentObject = new ParentObject('jack mom', 'jack Dad');
   42. let source: SourceObject = new SourceObject('jack', 18, false, parentSource);

   44. this.d_object = distributedDataObject.create(this.context, source);

   46. let dataSessionId: string = distributedDataObject.genSessionId();
   47. this.d_object.setSessionId(dataSessionId);

   49. wantParam['dataSessionId'] = dataSessionId;

   51. this.d_object.save(wantParam.targetDevice as string).then((result:
   52. distributedDataObject.SaveSuccessResponse) => {
   53. hilog.info(DOMAIN_NUMBER, TAG, `Succeeded in saving. SessionId: ${result.sessionId},
   54. version:${result.version}, deviceId:${result.deviceId}`);
   55. }).catch((err: BusinessError) => {
   56. hilog.error(DOMAIN_NUMBER, TAG, 'Failed to save. Error: ', JSON.stringify(err) ?? '');
   57. });
   58. // ...
   59. }

   61. // ...
   62. }
   ```
2. 对端恢复数据

   在对端UIAbility的onCreate()/onNewWant()中，通过加入与源端一致的分布式数据对象组网进行数据恢复。执行流程如下：

   1. 创建空的分布式数据对象，用于接收恢复的数据；
   2. 从want中读取分布式数据对象组网id；
   3. 注册on()接口监听数据变更。在收到status为restore的事件的回调中，实现数据恢复完毕时需要进行的业务操作。
   4. 调用setSessionId()加入组网，激活分布式数据对象。

   说明

   * 对端加入组网的分布式数据对象不能为临时变量，因为在分布式数据对象on()接口为异步回调，可能在onCreate()/onNewWant()执行结束后才执行，临时变量被释放可能导致空指针异常。可以使用类成员变量避免该问题。
   * 对端用于创建分布式数据对象的Object，其属性应在激活分布式数据对象前置为undefined，否则会导致新数据加入组网后覆盖源端数据，数据恢复失败。
   * 应当在激活分布式数据对象之前，调用分布式数据对象的on()接口进行注册监听，防止错过restore事件导致数据恢复失败。

   ```
   1. const TAG: string = '[MigrationAbility]';
   2. const DOMAIN_NUMBER: number = 0xFF00;

   4. export default class MigrationAbility extends UIAbility {
   5. d_object?: distributedDataObject.DataObject;
   6. // ...

   8. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
   9. if (launchParam.launchReason === AbilityConstant.LaunchReason.CONTINUATION) {
   10. this.handleDistributedData(want);
   11. }
   12. }

   14. onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
   15. if (launchParam.launchReason === AbilityConstant.LaunchReason.CONTINUATION) {
   16. if (want.parameters !== undefined) {
   17. this.handleDistributedData(want);
   18. }
   19. }
   20. }

   22. handleDistributedData(want: Want) {
   23. let remoteSource: SourceObject = new SourceObject(undefined, undefined, undefined, undefined);
   24. this.d_object = distributedDataObject.create(this.context, remoteSource);
   25. let dataSessionId = '';
   26. if (want.parameters !== undefined) {
   27. dataSessionId = want.parameters.dataSessionId as string;
   28. }
   29. this.d_object.on('status', (sessionId: string, networkId: string, status: 'online' | 'offline' | 'restored') => {
   30. hilog.info(DOMAIN_NUMBER, TAG, 'status changed ' + sessionId + ' ' + status + ' ' + networkId);
   31. if (status === 'restored') {
   32. if (this.d_object) {
   33. hilog.info(DOMAIN_NUMBER, TAG, 'restored name:' + this.d_object['name']);
   34. hilog.info(DOMAIN_NUMBER, TAG, 'restored parents:' + JSON.stringify(this.d_object['parent']));
   35. // ...
   36. }
   37. }
   38. });
   39. this.d_object.setSessionId(dataSessionId);
   40. }

   42. // ...

   44. // ...
   45. }
   ```

### 文件资产迁移

* **单个文件资产迁移**

  对于图片、文档等文件类数据，需要先将其转换为资产commonType.Asset类型，再封装到分布式数据对象中进行迁移。迁移实现方式与普通的分布式数据对象类似，下面仅针对差异部分进行说明。

  + 在源端，将需要迁移的文件资产保存到分布式数据对象DataObject中，执行流程如下：
  1. 将文件资产拷贝到分布式文件目录下，相关接口与用法详见基础文件接口。

     ```
     1. let distributedDir: string = this.context.distributedFilesDir; // 获取分布式文件目录路径
     2. let fileName: string = '/test.txt'; // 文件名
     3. let filePath: string = distributedDir + fileName; // 文件路径

     5. try {
     6. let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
     7. hilog.info(DOMAIN_NUMBER, TAG, 'Create file success.');
     8. fileIo.writeSync(file.fd, '[Sample] Insert file content here.');
     9. fileIo.closeSync(file.fd);
     10. } catch (error) {
     11. let err: BusinessError = error as BusinessError;
     12. hilog.error(DOMAIN_NUMBER, TAG,
     13. `Failed to openSync / writeSync / closeSync. Code: ${err.code}, message: ${err.message}`);

     15. }
     ```
  2. 使用分布式文件目录下的文件创建Asset资产对象。

     ```
     1. let distributedUri: string = fileUri.getUriFromPath(filePath);

     3. let ctime: string = '';
     4. let mtime: string = '';
     5. let size: string = '';
     6. await fileIo.stat(filePath).then((stat: fileIo.Stat) => {
     7. ctime = stat.ctime.toString();
     8. mtime = stat.mtime.toString();
     9. size = stat.size.toString();

     11. })

     13. let attachment: commonType.Asset = {
     14. name: fileName,
     15. uri: distributedUri,
     16. path: filePath,
     17. createTime: ctime,
     18. modifyTime: mtime,
     19. size: size,
     20. }
     ```
  3. 将Asset资产对象作为分布式数据对象的根属性保存。

     ```
     1. let parentSource: ParentObject = new ParentObject('jack mom', 'jack Dad');
     2. let source: SourceObject = new SourceObject('jack', 18, false, parentSource, attachment);
     3. this.d_object = distributedDataObject.create(this.context, source);
     ```

  随后，与普通数据对象的迁移的源端实现相同，可以使用该数据对象加入组网，并进行持久化保存。
* **多文件资产迁移**

  若应用想要同步多个资产，可采用两种方式实现：

  1. 可将每个资产作为分布式数据对象的一个根属性实现，适用于要迁移的资产数量固定的场景。
  2. 可以将资产数组转化为Object传递，适用于需要迁移的资产个数会动态变化的场景（如用户选择了不定数量的图片）。当前不支持直接将资产数组作为根属性传递。

  其中方式1的实现可以直接参照添加一个资产的方式添加更多资产。方式2的示例如下所示：

  ```
  1. import { distributedDataObject, commonType } from '@kit.ArkData';
  2. import { UIAbility, AbilityConstant, Want } from '@kit.AbilityKit';
  3. // ...

  5. class SourceObject {
  6. name: string | undefined
  7. assets: Object | undefined
  8. constructor(name: string | undefined, assets: Object | undefined) {
  9. this.name = name
  10. this.assets = assets;
  11. }
  12. }

  15. export default class MigrationAbility_multi_asset extends UIAbility {
  16. d_object?: distributedDataObject.DataObject;
  17. // ...

  19. GetAssetsWrapper(assets: commonType.Assets): Record<string, commonType.Asset> {
  20. let wrapper: Record<string, commonType.Asset> = {}
  21. let num: number = assets.length;
  22. for (let i: number = 0; i < num; i++) {
  23. wrapper[`asset${i}`] = assets[i];
  24. }
  25. return wrapper;
  26. }

  29. async onContinue(wantParam: Record<string, Object>): Promise<AbilityConstant.OnContinueResult> {
  30. // ...
  31. let attachment1: commonType.Asset = {
  32. // ...
  33. }

  36. let attachment2: commonType.Asset = {
  37. // ...
  38. }

  40. let assets: commonType.Assets = [];
  41. assets.push(attachment1);
  42. assets.push(attachment2);

  45. let assetsWrapper: Object = this.GetAssetsWrapper(assets);
  46. let source: SourceObject = new SourceObject('jack', assetsWrapper);
  47. this.d_object = distributedDataObject.create(this.context, source);

  50. // ...
  51. }
  52. }
  ```
