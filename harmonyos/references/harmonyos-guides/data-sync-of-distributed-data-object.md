---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-sync-of-distributed-data-object
title: 分布式数据对象跨设备数据同步 (ArkTS)
breadcrumb: 指南 > 应用框架 > ArkData（方舟数据管理） > 同应用跨设备数据同步（分布式） > 分布式数据对象跨设备数据同步 (ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-29T13:26:19+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1fff0b04d5ed227968506ed54537591854316cc44fb89b08d8ffe99497b4ba46
---

## 场景介绍

传统方式下，设备之间的数据同步，需要开发者完成消息处理逻辑，包括：建立通信链接、消息收发处理、错误重试、数据冲突解决等操作，工作量非常大。而且设备越多，调试复杂度也将同步增加。

其实设备之间的状态、消息发送进度、发送的数据等都是“变量”。如果这些变量支持“全局”访问，那么开发者跨设备访问这些变量就能像操作本地变量一样，从而能够自动高效、便捷地实现数据多端同步。

分布式数据对象即实现了对“变量”的“全局”访问。向应用开发者提供内存对象的创建、查询、删除、修改、订阅等基本数据对象的管理能力，同时具备分布式能力。为开发者在分布式应用场景下提供简单易用的JS接口，轻松实现多设备间同应用的数据协同，同时设备间可以监听对象的状态和数据变更。满足超级终端场景下，相同应用多设备间的数据对象协同需求。与传统方式相比，分布式数据对象大大减少了开发者的工作量。

目前分布式数据对象只能在[跨端迁移](../best-practices/bpta-continue-data.md)和[通过跨设备Call调用实现多端协同](uiability-cross-device-interaction.md)的场景中使用。

## 基本概念

* **分布式内存数据库**：分布式内存数据库将数据缓存在内存中，以便应用获得更快的数据存取速度，不会将数据进行持久化。若数据库关闭，则数据不会保留。
* **分布式数据对象**：分布式数据对象是一个JS对象型的封装。每一个分布式数据对象实例会创建一个内存数据库中的数据表，每个应用程序创建的内存数据库相互隔离，对分布式数据对象的“读取”或“赋值”会自动映射到对应数据库的get/put操作。

  分布式数据对象的生命周期包括以下状态：

  + 未初始化：未实例化，或已被销毁。
  + 本地数据对象：已创建对应的数据表，但是还无法进行数据同步。
  + 分布式数据对象：已创建对应的数据表，设备在线且组网内设置同样sessionId的对象数>=2，可以跨设备同步数据。若设备掉线或将sessionId置为空，分布式数据对象退化为本地数据对象。

## 运作机制

**图1** 分布式数据对象运作机制

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/GvVIO9wSTqKv1zqxv28ngg/zh-cn_image_0000002589243825.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T052618Z&HW-CC-Expire=86400&HW-CC-Sign=98260794AC97943A5F2D77E54FC4DF11ADAB3ADFDA62D79995DCF733E0896F7F)

分布式数据对象生长在分布式内存数据库之上，在分布式内存数据库上进行了JS对象型的封装，能像操作本地变量一样操作分布式数据对象，数据的跨设备同步由系统自动完成。

### JS对象型存储与封装机制

* 为每个分布式数据对象实例创建一个内存数据库，通过sessionId标识，每个应用程序创建的内存数据库相互隔离。
* 在分布式数据对象实例化的时候，（递归）遍历对象所有属性，使用“Object.defineProperty”定义所有属性的set和get方法，set和get中分别对应数据库一条记录的put和get操作，Key对应属性名，Value对应属性值。
* 在开发者对分布式数据对象进行“读取”或者“赋值”的时候，都会自动调用到set和get方法，映射到对应数据库的操作。

**表1** 分布式数据对象和分布式数据库的对应关系

| 分布式对象实例 | 对象实例 | 属性名称 | 属性值 |
| --- | --- | --- | --- |
| 分布式内存数据库 | 一个数据库（sessionId标识） | 一条数据库记录的key | 一条数据库记录的value |

### 跨设备同步和数据变更通知机制

分布式数据对象，最重要的功能就是对象之间的数据同步。可信组网内的设备可以在本地创建分布式数据对象，并设置sessionId。不同设备上的分布式数据对象，通过设置相同的sessionId，建立对象之间的同步关系。

如下图所示，设备A和设备B上的“分布式数据对象1”，其sessionId均为session1，这两个对象建立了session1的同步关系。

**图2** 对象的同步关系

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/Saex79iqSSyVCCOf76y7FQ/zh-cn_image_0000002558764018.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T052618Z&HW-CC-Expire=86400&HW-CC-Sign=62E4C64A5D44693F0D9BE9A8588A9325978293DB36CEEC95E4BBD534C148C396)

一个同步关系中，一个设备只能有一个对象加入。比如上图中，设备A的“分布式数据对象1”已经加入了session1的同步关系，所以设备A的“分布式数据对象2”就加入失败了。

建立同步关系后，每个Session有一份共享对象数据。加入了同一个Session的对象，支持以下操作：

（1）读取/修改Session中的数据。

（2）监听数据变更，感知其他设备对共享对象数据的修改。

（3）监听状态变更，感知其他设备的加入和退出。

分布式数据对象加入session时，如果它的数据与session中的数据不同，则它会更新session中的数据。如果希望分布式数据对象加入sessionId时不更新session中的数据，并且得到session中的数据，需要将对象的属性的值设置为undefined（资产类型的属性则是将它的各个属性值设置为空字符串）。

### 同步的最小单位

关于分布式数据对象的数据同步，值得注意的是，同步的最小单位是“属性”。比如，下图中对象1包含三个属性：name、age和parents。当其中一个属性变更时，则数据同步时只需同步此变更的属性。

对象属性支持基本类型（数字类型、布尔类型、字符串类型）以及复杂类型（数组、基本类型嵌套）。针对复杂类型的数据修改，目前仅支持对根属性的修改，暂不支持对下级属性的修改。

```
1. dataObject['parents'] = {mom: "amy"}; // 支持的修改
2. dataObject['parents']['mom'] = "amy"; // 不支持的修改
```

**图3** 数据同步视图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/sDHcaf5-RIi-5A0TpWAfMg/zh-cn_image_0000002558604362.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T052618Z&HW-CC-Expire=86400&HW-CC-Sign=6748AA2F08B6882D560322B2905A9C0A21795073635950911B6058655E8740D6)

### 对象持久化缓存机制

分布式对象主要运行在应用程序的进程空间。当调用分布式对象持久化接口时，通过分布式数据库对对象进行持久化和同步，进程退出后数据也不会丢失。分布式数据库会自动实现同步，可调用[on('change')](../harmonyos-references/js-apis-data-distributedobject.md#onchange20)监听数据变更。

该场景是分布式对象的扩展场景，主要用于以下情况：

* 在设备上创建持久化对象后APP退出，重新打开APP，创建持久化对象，加入同一个Session，数据可以恢复到APP退出前的数据。
* 在设备A上创建持久化对象并同步后持久化到设备B后，A设备的APP退出，设备B打开APP，创建持久化对象，加入同一个Session，数据可以恢复到A设备退出前的数据。

### 资产同步机制

在分布式对象中，可以使用[资产类型](../harmonyos-references/js-apis-data-commontype.md#asset)来描述本地实体资产文件，分布式对象跨设备同步时，该文件会和数据一起同步到其他设备上。

在API version 20之前版本，仅支持资产类型，不支持[资产类型数组](../harmonyos-references/js-apis-data-commontype.md#assets)。如需同步多个资产，可将每个资产作为分布式对象的一个根属性实现。

从API version 20开始，支持[资产类型数组](../harmonyos-references/js-apis-data-commontype.md#assets)的同步。

## 约束限制

* 目前分布式数据对象只能在[跨端迁移](../best-practices/bpta-continue-data.md)和[通过跨设备Call调用实现多端协同](uiability-cross-device-interaction.md)的场景中使用。跨端迁移场景下，每个分布式数据对象大小不超过150KB；多端协同场景下，每个分布式数据对象大小不超过500KB。
* 分布式数据对象的数据同步发生在同一个应用程序下，且同sessionId之间。
* 设备A修改1KB数据，设备B收到变更通知，50ms内完成。
* 单个应用程序最多只能创建16个分布式数据对象实例。
* 考虑到性能和用户体验，最多不超过3个设备进行数据协同。
* 如对复杂类型的数据进行修改，仅支持修改根属性，暂不支持下级属性修改。[资产同步机制](data-sync-of-distributed-data-object.md#资产同步机制)中，资产类型的数据支持下一级属性修改。
* 支持JS接口间的互通，与其他语言不互通。

## 接口说明

以下是分布式对象跨设备数据同步功能的相关接口，更多接口及使用方式请见[分布式数据对象](../harmonyos-references/js-apis-data-distributedobject.md)。

| 接口名称 | 描述 |
| --- | --- |
| create(context: Context, source: object): DataObject | 创建并得到一个分布式数据对象实例。 |
| genSessionId(): string | 创建一个sessionId，可作为分布式数据对象的sessionId。 |
| setSessionId(sessionId: string, callback: AsyncCallback<void>): void | 设置同步的sessionId，当可信组网中有多个设备时，多个设备间的对象如果设置为同一个sessionId，就能自动同步。 |
| setSessionId(callback: AsyncCallback<void>): void | 退出所有已加入的session。 |
| on(type: 'change', callback: (sessionId: string, fields: Array<string>) => void): void | 监听分布式数据对象的数据变更。 |
| off(type: 'change', callback?: (sessionId: string, fields: Array<string>) => void): void | 取消监听分布式数据对象的数据变更。 |
| on(type: 'status', callback: (sessionId: string, networkId: string, status: 'online' | 'offline' ) => void): void | 监听分布式数据对象的上下线。 |
| off(type: 'status', callback?: (sessionId: string, networkId: string, status: 'online' |'offline' ) => void): void | 取消监听分布式数据对象的上下线。 |
| save(deviceId: string, callback: AsyncCallback<SaveSuccessResponse>): void | 保存分布式数据对象。 |
| revokeSave(callback: AsyncCallback<RevokeSaveSuccessResponse>): void | 撤回保存的分布式数据对象。 |
| bindAssetStore(assetKey: string, bindInfo: BindInfo, callback: AsyncCallback<void>): void | 绑定融合资产。 |
| setAsset(assetKey: string, uri: string): void | 设置单个资产。 |
| setAssets(assetKey: string, uris: Array<string>): void | 设置资产数组。 |
| on(type: 'change', callback: DataObserver<void>): void | 监听分布式对象的数据变更。 |
| off(type: 'change', callback?: DataObserver<void>): void | 删除分布式对象数据变更监听的回调实例。 |
| on(type: 'status', callback: StatusObserver<void>): void | 监听分布式对象的状态变更。 |
| off(type: 'status', callback?: StatusObserver<void>): void | 删除分布式对象状态变更监听的回调实例。 |

## 开发步骤

### 在跨端迁移中使用分布式数据对象迁移数据

1. 迁移发起端在onContinue接口中创建分布式数据对象并保存数据到接收端：

   1.1 调用create接口创建并得到一个分布式数据对象实例。

   1.2 调用genSessionId接口创建一个sessionId，调用setSessionId接口设置同步的sessionId，并将这个sessionId放入wantParam。

   1.3 从wantParam获取接收端设备networkId，使用这个networkId调用save接口保存数据到接收端。
2. 接收端在onCreate和onNewWant接口中创建分布式数据对象并注册恢复状态监听：

   2.1 调用create接口创建并得到一个分布式数据对象实例。

   2.2 注册恢复状态监听。收到状态为'restored'的回调通知时，表示接收端分布式数据对象已恢复发起端保存过来的数据。

   2.3 从want.parameters中获取发起端放入的sessionId，调用setSessionId接口设置同步的sessionId。

说明

* 跨端迁移时，在迁移发起端调用setSessionId接口设置同步的sessionId后，必须再调用save接口保存数据到接收端。跨端迁移过程中save接口仅在首次调用时数据可以同步到接收端（原理是：首次从发起端设备获取数据后迁移任务即已完成，后续数据以接收端设备为准，不需要再同步）。
* 在应用迁移启动时，无论是冷启动还是热启动，都会在执行完onCreate()/onNewWant()后，触发[onWindowStageRestore()](../harmonyos-references/js-apis-app-ability-uiability.md#onwindowstagerestore)生命周期函数，不执行[onWindowStageCreate()](../harmonyos-references/js-apis-app-ability-uiability.md#onwindowstagecreate)生命周期函数。开发者如果在onWindowStageCreate()中进行了一些应用启动时必要的初始化，那么迁移后需要在onWindowStageRestore()中执行同样的初始化操作，避免应用异常。
* 跨端迁移需要配置continuable标签，详见[应用接续开发步骤](../best-practices/bpta-continue-data.md)。
* wantParam中的"sessionId"字段可能被其他服务占用，建议自定义一个key存取sessionId。
* 可以使用资产类型记录资产附件（文件、图片、视频等类型文件）的相关信息，迁移资产类型数据时，对应的资产附件会一起迁移到对端。
* 接收端需要将业务数据的初始值设置为undefined，才能恢复发起端保存的数据，否则接收端的数据会覆盖同步到发起端。如果是资产数据，需要将资产数据的各个属性设置为空字符串而不是将整个资产数据设置为undefined。
* API version 20版本之前不支持资产类型数组，如果要迁移多个文件，在业务数据中定义多条资产数据来记录。从API version 20开始，支持资产类型数组的同步。
* 目前仅支持迁移分布式文件目录下的文件，非分布式文件目录下的文件可以复制或移动到分布式文件目录下再进行迁移。文件的操作和URI的获取详见[文件管理](../harmonyos-references/js-apis-file-fs.md)和[文件URI](../harmonyos-references/js-apis-file-fileuri.md)。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
3. import { commonType, distributedDataObject } from '@kit.ArkData';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. // 业务数据定义
7. export class ContentInfo {
8. public mainTitle: string | undefined;
9. public textContent: string | undefined;
10. public imageUriArray: Array<ImageInfo> | undefined;
11. public isShowLocalInfo: boolean | undefined;
12. public isAddLocalInfo: boolean | undefined;
13. public selectLocalInfo: string | undefined;
14. public attachments?: commonType.Assets | undefined;

16. constructor(
17. mainTitle: string | undefined,
18. textContent: string | undefined,
19. imageUriArray: Array<ImageInfo> | undefined,
20. isShowLocalInfo: boolean | undefined,
21. isAddLocalInfo: boolean | undefined,
22. selectLocalInfo: string | undefined,
23. attachments?: commonType.Assets | undefined
24. ) {
25. this.mainTitle = mainTitle;
26. this.textContent = textContent;
27. this.imageUriArray = imageUriArray;
28. this.isShowLocalInfo = isShowLocalInfo;
29. this.isAddLocalInfo = isAddLocalInfo;
30. this.selectLocalInfo = selectLocalInfo;
31. this.attachments = attachments;
32. }

34. flatAssets(): object {
35. let obj: object = this;
36. if (!this.attachments) {
37. return obj;
38. }
39. for (let i = 0; i < this.attachments.length; i++) {
40. obj[`attachments${i}`] = this.attachments[i];
41. }
42. return obj;
43. }
44. }

46. export interface ImageInfo {
47. /**
48. * image PixelMap.
49. */
50. imagePixelMap: PixelMap;

52. /**
53. * Image name.
54. */
55. imageName: string;
56. }

58. const DOMAIN: number = 0x0000;
59. const TAG: string = '[DistributedDataObject]';
60. let dataObject: distributedDataObject.DataObject;

62. export default class EntryAbility extends UIAbility {
63. private imageUriArray: Array<ImageInfo> = [];
64. private distributedObject: distributedDataObject.DataObject | undefined = undefined;

66. // 1. 迁移发起端在onContinue接口中创建分布式数据对象并保存数据到接收端
67. async onContinue(wantParam: Record<string, Object | undefined>): Promise<AbilityConstant.OnContinueResult> {
68. // 1.1 获取需要设置的分布式对象的资产关键uri
69. try {
70. let sessionId: string = distributedDataObject.genSessionId();
71. wantParam.distributedSessionId = sessionId;

73. let distrUriArray: string[] = [];
74. let assetUriArray = AppStorage.get<Array<string>>('assetUriArray');
75. if (assetUriArray) {
76. distrUriArray = assetUriArray;
77. }
78. // 1.2 创建分布式数据对象
79. let contentInfo: ContentInfo = new ContentInfo(
80. AppStorage.get('mainTitle'),
81. AppStorage.get('textContent'),
82. AppStorage.get('imageUriArray'),
83. AppStorage.get('isShowLocalInfo'),
84. AppStorage.get('isAddLocalInfo'),
85. AppStorage.get('selectLocalInfo'),
86. );
87. let source = contentInfo.flatAssets();
88. this.distributedObject = distributedDataObject.create(this.context, source);

90. // 1.3 将需要设置的分布式对象的资产或资产数组填充完成
91. if (assetUriArray?.length === 1) {
92. this.distributedObject?.setAsset('attachments', distrUriArray[0]).then(() => {
93. hilog.info(DOMAIN, TAG, 'OnContinue setAsset');
94. })
95. } else {
96. this.distributedObject?.setAssets('attachments', distrUriArray).then(() => {
97. hilog.info(DOMAIN, TAG, 'OnContinue setAssets');
98. })
99. }
100. // 1.4 将设置的资产或资产数组保存至迁移发起端
101. this.distributedObject?.setSessionId(sessionId);
102. this.distributedObject?.save(wantParam.targetDevice as string).catch((err: BusinessError) => {
103. hilog.error(DOMAIN, TAG, 'OnContinue failed to save. code: ', err.code);
104. hilog.error(DOMAIN, TAG, 'OnContinue failed to save. message: ', err.message);
105. });
106. } catch (error) {
107. hilog.error(DOMAIN, TAG, 'OnContinue failed code: ', error.code);
108. hilog.error(DOMAIN, TAG, 'OnContinue failed message: ', error.message);
109. }
110. hilog.info(DOMAIN, TAG, 'OnContinue success!');
111. return AbilityConstant.OnContinueResult.AGREE;
112. }

114. // 2. 接收端在onCreate和onNewWant接口中创建分布式数据对象并加入组网进行数据恢复
115. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
116. if (launchParam.launchReason === AbilityConstant.LaunchReason.CONTINUATION) {
117. if (want.parameters && want.parameters.distributedSessionId) {
118. this.restoreDistributedObject(want);
119. }
120. }
121. }

123. // 2. 接收端在onCreate和onNewWant接口中创建分布式数据对象并加入组网进行数据恢复
124. onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
125. if (launchParam.launchReason === AbilityConstant.LaunchReason.CONTINUATION) {
126. if (want.parameters && want.parameters.distributedSessionId) {
127. this.restoreDistributedObject(want);
128. }
129. }
130. }

132. async restoreDistributedObject(want: Want): Promise<void> {
133. if (!want.parameters || !want.parameters.distributedSessionId) {
134. hilog.error(DOMAIN, TAG, 'missing sessionId');
135. return;
136. }

138. // 2.1 调用create接口创建并得到一个分布式数据对象实例
139. let mailInfo: ContentInfo = new ContentInfo(undefined, undefined, [], undefined, undefined, undefined, undefined);
140. dataObject = distributedDataObject.create(this.context, mailInfo);

142. // 2.2 注册恢复状态监听。收到状态为'restored'的回调通知时，表示接收端分布式数据对象已恢复发起端保存过来的数据（有资产数据时，对应的文件也迁移过来了）
143. dataObject.on('status', (sessionId: string, networkId: string, status: string) => {
144. hilog.info(DOMAIN, TAG, `status change, sessionId:  ${sessionId}`);
145. hilog.info(DOMAIN, TAG, `status change, networkId:  ${networkId}`);
146. if (status === 'restored') { // 收到'restored'的状态通知表示已恢复发起端保存的数据
147. hilog.info(DOMAIN, TAG, `title: ${dataObject['title']}, text: ${dataObject['text']}`);
148. AppStorage.setOrCreate('mainTitle', dataObject['mainTitle']);
149. AppStorage.setOrCreate('textContent', dataObject['textContent']);
150. AppStorage.setOrCreate('imageUriArray', dataObject['imageUriArray']);
151. AppStorage.setOrCreate('isShowLocalInfo', dataObject['isShowLocalInfo']);
152. AppStorage.setOrCreate('isAddLocalInfo', dataObject['isAddLocalInfo']);
153. AppStorage.setOrCreate('selectLocalInfo', dataObject['selectLocalInfo']);
154. AppStorage.setOrCreate<Array<ImageInfo>>('imageUriArray', this.imageUriArray);
155. }
156. });

158. // 2.3 从want.parameters中获取发起端放入的sessionId，调用setSessionId接口设置同步的sessionId
159. let sessionId = want.parameters.distributedSessionId as string;
160. hilog.info(DOMAIN, TAG, `get sessionId: ${sessionId}`);
161. dataObject.setSessionId(sessionId);
162. }
163. }
```

[EntryBackupAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/DataObject/CrossDeviceMigration/entry/src/main/ets/entrybackupability/EntryBackupAbility.ets#L16-L181)

### 在多端协同中使用分布式数据对象

1. 调用端调用startAbilityByCall接口拉起对端Ability：

   1.1 调用genSessionId接口创建一个sessionId，通过分布式设备管理接口获取对端设备networkId。

   1.2 组装want，并将sessionId放入want。

   1.3 调用startAbilityByCall接口拉起对端Ability。
2. 调用端拉起对端Ability后创建分布式数据对象并加入组网：

   2.1 创建分布式数据对象实例。

   2.2 注册数据变更监听。

   2.3 设置同步sessionId加入组网。
3. 被调用端被拉起后创建和恢复分布式数据对象：

   3.1 创建分布式数据对象实例。

   3.2 注册数据变更监听。

   3.3 从want中获取源端放入的sessionId，使用这个sessionId加入组网。

说明

* 暂时只支持在[通过跨设备Call调用实现多端协同](uiability-cross-device-interaction.md)的场景中使用分布式数据对象进行数据同步。
* 跨设备Call调用实现的多端协同开发需要申请ohos.permission.DISTRIBUTED\_DATASYNC权限和配置单实例启动标签，详见[通过跨设备Call调用实现多端协同](uiability-cross-device-interaction.md)。
* wantParam中的"sessionId"字段可能被其他服务占用，建议自定义一个key存取sessionId。
* 使用分布式设备管理获取对端设备networkId详见[设备信息查询开发指导](devicemanager-guidelines.md#设备信息查询开发指导)。

示例代码如下：

```
1. import { AbilityConstant, Caller, UIAbility, Want } from '@kit.AbilityKit';
2. import { distributedDataObject } from '@kit.ArkData';
3. import { distributedDeviceManager } from '@kit.DistributedServiceKit';
4. import { BusinessError } from '@kit.BasicServicesKit';
5. import { JSON } from '@kit.ArkTS';
6. import { hilog } from '@kit.PerformanceAnalysisKit';

8. // 业务数据定义
9. class Data {
10. public title: string | undefined;
11. public text: string | undefined;

13. constructor(title: string | undefined, text: string | undefined) {
14. this.title = title;
15. this.text = text;
16. }
17. }

19. const DOMAIN: number = 0x0000;
20. const TAG: string = '[DistributedDataObject]';

22. let sessionId: string;
23. let caller: Caller;
24. let dataObject: distributedDataObject.DataObject;
25. const changeCallBack: distributedDataObject.DataObserver = (sessionId: string, fields: Array<string>) => {
26. console.info(`change, sessionId: ${sessionId}, fields: ${JSON.stringify(fields)}`);
27. }

29. export default class EntryAbility extends UIAbility {
30. // 1. 调用端调用startAbilityByCall接口拉起对端Ability
31. callRemote() {
32. if (caller) {
33. hilog.error(DOMAIN, TAG, 'call remote already');
34. return;
35. }

37. // 1.1 调用genSessionId接口创建一个sessionId，通过分布式设备管理接口获取对端设备networkId
38. sessionId = distributedDataObject.genSessionId();
39. hilog.info(DOMAIN, TAG, `gen sessionId: ${sessionId}`);
40. let deviceId = getRemoteDeviceId();
41. if (deviceId === '') {
42. hilog.warn(DOMAIN, TAG, 'no remote device');
43. return;
44. }
45. hilog.info(DOMAIN, TAG, `get remote deviceId: ${deviceId}`);

47. // 1.2 组装want，并将sessionId放入want
48. let want: Want = {
49. bundleName: 'com.example.collaboration',
50. abilityName: 'EntryAbility',
51. deviceId: deviceId,
52. parameters: {
53. 'ohos.aafwk.param.callAbilityToForeground': true, // 前台启动，非必须
54. 'distributedSessionId': sessionId
55. }
56. }
57. try {
58. // 1.3 调用startAbilityByCall接口拉起对端Ability
59. this.context.startAbilityByCall(want).then((res) => {
60. if (!res) {
61. hilog.error(DOMAIN, TAG, 'startAbilityByCall failed');
62. }
63. caller = res;
64. })
65. } catch (e) {
66. let err = e as BusinessError;
67. hilog.error(DOMAIN, TAG, `get remote deviceId error, error code: ${err.code}, error message: ${err.message}`);
68. }
69. }

71. // 2. 拉起对端Ability后创建分布式数据对象
72. createDataObject() {
73. if (!caller) {
74. hilog.error(DOMAIN, TAG, 'call remote first');
75. return;
76. }
77. if (dataObject) {
78. hilog.error(DOMAIN, TAG, 'create dataObject already');
79. return;
80. }

82. // 2.1 创建分布式数据对象实例
83. let data = new Data('The title', 'The text');
84. dataObject = distributedDataObject.create(this.context, data);

86. // 2.2 注册数据变更监听
87. dataObject.on('change', changeCallBack);
88. // 2.3 设置同步sessionId加入组网
89. dataObject.setSessionId(sessionId);
90. }

92. // 3. 被调用端被拉起后创建和恢复分布式数据对象
93. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
94. if (want.parameters && want.parameters.distributedSessionId) {
95. // 3.1 创建分布式数据对象实例
96. let data = new Data(undefined, undefined);
97. dataObject = distributedDataObject.create(this.context, data);

99. // 3.2 注册数据变更监听
100. dataObject.on('change', changeCallBack);
101. // 3.3 从want中获取源端放入的sessionId，使用这个sessionId加入组网
102. let sessionId = want.parameters.distributedSessionId as string;
103. hilog.info(DOMAIN, TAG, `onCreate get sessionId: ${sessionId}`);
104. dataObject.setSessionId(sessionId);
105. }
106. }
107. }

109. // 获取可信组网中的设备
110. function getRemoteDeviceId() {
111. let deviceId = '';
112. try {
113. let deviceManager = distributedDeviceManager.createDeviceManager('com.example.collaboration');
114. let devices = deviceManager.getAvailableDeviceListSync();
115. if (devices[0] && devices[0].networkId) {
116. deviceId = devices[0].networkId;
117. }
118. } catch (e) {
119. let err = e as BusinessError;
120. hilog.error(DOMAIN, TAG, `get remote deviceId error, error code: ${err.code}, error message: ${err.message}`);
121. }
122. return deviceId;
123. }
```

[EntryBackupAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/DataObject/CrossDeviceCollaboration/entry/src/main/ets/entrybackupability/EntryBackupAbility.ets#L16-L141)
