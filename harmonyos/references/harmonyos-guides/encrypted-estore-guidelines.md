---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/encrypted-estore-guidelines
title: E类加密数据库的使用 (ArkTS)
breadcrumb: 指南 > 应用框架 > ArkData（方舟数据管理） > 数据可靠性与安全性 > E类加密数据库的使用 (ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:21+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6a6dc187973d02688a254ddbb2806e5d4ea1b04390f92f4e691121e7924a8d86
---

## 场景介绍

从安全角度考虑，为满足部分敏感数据的安全特性，提供了E类加密数据库的方案以提高锁屏下数据的安全性。存有敏感信息的应用在申请ohos.permission.PROTECT\_SCREEN\_LOCK\_DATA权限后会在[EL5](../harmonyos-references/js-apis-app-ability-contextconstant.md#areamode)路径下创建一个E类数据库。在锁屏的情况下（未调用Access接口获取保留文件密钥）会触发文件密钥的销毁，此时E类数据库不可读写。当锁屏解锁后，密钥会恢复，E类数据库恢复正常读写操作。这样的设计可以有效防止用户数据的泄露。

在锁屏的情况下，应用程序仍然可以继续写入数据。由于此时E类数据库不可读写，这可能会导致数据丢失。为了解决这个问题，当前提供了一种方案：在锁屏的情况下，将数据存储在[EL2](../harmonyos-references/js-apis-app-ability-contextconstant.md#areamode)路径下的C类数据库中。当解锁后，再将数据迁移到E类数据库中。这样可以确保数据在锁屏期间的安全性和完整性。

键值型数据库和关系型数据库均支持E类加密数据库。

## 实现机制

通过封装Mover类、Store类、SecretKeyObserver类和ECStoreManager类实现应用数据库密钥加锁和解锁状态下E类数据库和C类数据库的切换和操作。

Mover类：提供数据库数据迁移接口，在锁屏解锁后，若C类数据库中有数据，使用该接口将数据迁移到E类数据库。

Store类：提供了获取数据库，在数据库中插入数据、删除数据、更新数据和获取当前数据数量的接口。

SecretKeyObserver类：提供了获取当前密钥状态的接口，在密钥销毁后，关闭E类数据库。

ECStoreManager类：用于管理应用的E类数据库和C类数据库。

## 配置权限

使用EL5路径下的数据库，需要配置ohos.permission.PROTECT\_SCREEN\_LOCK\_DATA权限。

```
1. // module.json5
2. "requestPermissions": [
3. {
4. "name": "ohos.permission.PROTECT_SCREEN_LOCK_DATA"
5. }
6. ]
```

## 键值型数据库E类加密

本章节提供键值型数据库的E类加密数据库使用方式，提供[Mover](encrypted-estore-guidelines.md#mover)类、[Store](encrypted-estore-guidelines.md#store)类、[SecretKeyObserver](encrypted-estore-guidelines.md#secretkeyobserver)类和[ECStoreManager](encrypted-estore-guidelines.md#ecstoremanager)类的具体实现，并在[EntryAbility](encrypted-estore-guidelines.md#entryability)和[index按键事件](encrypted-estore-guidelines.md#index按键事件)中展示这几个类的使用方式。

### Mover

提供数据库数据迁移接口，在锁屏解锁后，若C类数据库中存在数据，使用该接口将数据迁移到E类数据库。

```
1. import { distributedKVStore } from '@kit.ArkData';
2. // Logger为hilog封装后实现的打印功能
3. import Logger from '../common/Logger';

5. export class Mover {
6. async move(eStore: distributedKVStore.SingleKVStore, cStore: distributedKVStore.SingleKVStore): Promise<void> {
7. if (eStore != null && cStore != null) {
8. let entries: distributedKVStore.Entry[] = await cStore.getEntries('key_test_string');
9. await eStore.putBatch(entries);
10. Logger.info(`ECDB_Encry move success`);
11. }
12. }
13. }
```

[Mover.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/KvStore/ECStoreSamples/entry/src/main/ets/entryability/Mover.ts#L16-L29)

### Store

提供了获取数据库，在数据库中插入数据、删除数据、更新数据和获取当前数据数量的接口。

```
1. import { distributedKVStore } from '@kit.ArkData';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. // Logger为hilog封装后实现的打印功能
4. import Logger from '../common/Logger';

6. let kvManager: distributedKVStore.KVManager;

8. export class StoreInfo {
9. kvManagerConfig: distributedKVStore.KVManagerConfig;
10. storeId: string;
11. option: distributedKVStore.Options;
12. }

14. export class Store {
15. async getECStore(storeInfo: StoreInfo): Promise<distributedKVStore.SingleKVStore> {
16. try {
17. kvManager = distributedKVStore.createKVManager(storeInfo.kvManagerConfig);
18. Logger.info('Succeeded in creating KVManager');
19. } catch (e) {
20. let error = e as BusinessError;
21. Logger.error(`Failed to create KVManager.code is ${error.code},message is ${error.message}`);
22. }
23. if (kvManager !== undefined) {
24. let kvStore: distributedKVStore.SingleKVStore | null;
25. try {
26. kvStore = await kvManager.getKVStore<distributedKVStore.SingleKVStore>(storeInfo.storeId, storeInfo.option);
27. if (kvStore != undefined) {
28. Logger.info(`ECDB_Encry succeeded in getting store : ${storeInfo.storeId}`);
29. return kvStore;
30. }
31. } catch (e) {
32. let error = e as BusinessError;
33. Logger.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
34. }
35. }
36. }

38. putOnedata(kvStore: distributedKVStore.SingleKVStore): void {
39. if (kvStore != undefined) {
40. const KEY_TEST_STRING_ELEMENT = 'key_test_string' + String(Date.now());
41. const VALUE_TEST_STRING_ELEMENT = 'value_test_string' + String(Date.now());
42. try {
43. kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT, (err) => {
44. if (err !== undefined) {
45. Logger.error(`Failed to put data. Code:${err.code},message:${err.message}`);
46. return;
47. }
48. Logger.info(`ECDB_Encry Succeeded in putting data.${KEY_TEST_STRING_ELEMENT}`);
49. });
50. } catch (e) {
51. let error = e as BusinessError;
52. Logger.error(`An unexpected error occurred. Code:${error.code},message:${error.message}`);
53. }
54. }
55. }

57. getDataNum(kvStore: distributedKVStore.SingleKVStore): void {
58. if (kvStore != undefined) {
59. let resultSet: distributedKVStore.KVStoreResultSet;
60. kvStore.getResultSet('key_test_string').then((result: distributedKVStore.KVStoreResultSet) => {
61. Logger.info(`ECDB_Encry Succeeded in getting result set num ${result.getCount()}`);
62. resultSet = result;
63. if (kvStore != null) {
64. kvStore.closeResultSet(resultSet).then(() => {
65. Logger.info('Succeeded in closing result set');
66. }).catch((err: BusinessError) => {
67. Logger.error(`Failed to close resultset.code is ${err.code},message is ${err.message}`);
68. });
69. }
70. }).catch((err: BusinessError) => {
71. Logger.error(`Failed to get resultset.code is ${err.code},message is ${err.message}`);
72. });
73. }
74. }

76. deleteOnedata(kvStore: distributedKVStore.SingleKVStore): void {
77. if (kvStore != undefined) {
78. kvStore.getEntries('key_test_string', (err: BusinessError, entries: distributedKVStore.Entry[]) => {
79. if (err != undefined) {
80. Logger.error(`Failed to get Entries.code is ${err.code},message is ${err.message}`);
81. return;
82. }
83. if (kvStore != null && entries.length != 0) {
84. kvStore.delete(entries[0].key, (err: BusinessError) => {
85. if (err != undefined) {
86. Logger.error(`Failed to delete.code is ${err.code},message is ${err.message}`);
87. return;
88. }
89. Logger.info('ECDB_Encry Succeeded in deleting');
90. });
91. }
92. });
93. }
94. }

96. updateOnedata(kvStore: distributedKVStore.SingleKVStore): void {
97. if (kvStore != undefined) {
98. kvStore.getEntries('key_test_string', async (err: BusinessError, entries: distributedKVStore.Entry[]) => {
99. if (err != undefined) {
100. Logger.error(`Failed to get Entries.code is ${err.code},message is ${err.message}`);
101. return;
102. }
103. if (kvStore != null && entries.length != 0) {
104. Logger.info(`ECDB_Encry old data:${entries[0].key},value :${entries[0].value.value.toString()}`);
105. await kvStore.put(entries[0].key, 'new value_test_string' + String(Date.now()) + 'new').then(() => {
106. }).catch((err: BusinessError) => {
107. Logger.error(`Failed to put.code is ${err.code},message is ${err.message}`);
108. });
109. Logger.info(`ECDB_Encry update success`);
110. }
111. });
112. }
113. }
114. }
```

[Store.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/KvStore/ECStoreSamples/entry/src/main/ets/entryability/Store.ts#L16-L130)

### SecretKeyObserver

该类提供了获取当前密钥状态的接口，在密钥销毁后，关闭E类数据库。

```
1. import { ECStoreManager } from './ECStoreManager';

3. export enum SecretStatus {
4. Lock,
5. UnLock
6. }

8. export class SecretKeyObserver {
9. onLock(): void {
10. this.lockStatus = SecretStatus.Lock;
11. this.storeManager.closeEStore();
12. }

14. onUnLock(): void {
15. this.lockStatus = SecretStatus.UnLock;
16. }

18. getCurrentStatus(): number {
19. return this.lockStatus;
20. }

22. initialize(storeManager: ECStoreManager): void {
23. this.storeManager = storeManager;
24. }

26. updateLockStatus(code: number) {
27. if (code === SecretStatus.Lock) {
28. this.onLock();
29. } else {
30. this.lockStatus = code;
31. }
32. }

34. // 初始获取锁屏状态
35. private lockStatus: number = SecretStatus.UnLock;
36. private storeManager: ECStoreManager;
37. }

39. export let lockObserve = new SecretKeyObserver();
```

[SecretKeyObserver.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/KvStore/ECStoreSamples/entry/src/main/ets/entryability/SecretKeyObserver.ts#L16-L56)

### ECStoreManager

ECStoreManager类用于管理应用的E类数据库和C类数据库。支持配置数据库信息、配置迁移函数的信息，可根据密钥状态为应用提供相应的数据库句柄，并提供了关闭E类数据库、数据迁移完成后销毁C类数据库等接口。

```
1. import { distributedKVStore } from '@kit.ArkData';
2. import { Mover } from './Mover';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { StoreInfo, Store } from './Store';
5. import { SecretStatus } from './SecretKeyObserver';
6. // Logger为hilog封装后实现的打印功能
7. import Logger from '../common/Logger';

9. let store = new Store();

11. export class ECStoreManager {
12. config(cInfo: StoreInfo, other: StoreInfo): void {
13. this.cInfo = cInfo;
14. this.eInfo = other;
15. }

17. configDataMover(mover: Mover): void {
18. this.mover = mover;
19. }

21. async getCurrentStore(screenStatus: number): Promise<distributedKVStore.SingleKVStore> {
22. Logger.info(`ECDB_Encry GetCurrentStore start screenStatus: ${screenStatus}`);
23. if (screenStatus === SecretStatus.UnLock) {
24. try {
25. this.eStore = await store.getECStore(this.eInfo);
26. } catch (e) {
27. let error = e as BusinessError;
28. Logger.error(`Failed to GetECStore.code is ${error.code},message is ${error.message}`);
29. }
30. // 解锁状态 获取e类库
31. if (this.needMove) {
32. if (this.eStore != undefined && this.cStore != undefined) {
33. await this.mover.move(this.eStore, this.cStore);
34. }
35. this.deleteCStore();
36. Logger.info(`ECDB_Encry Data migration is complete. Destroy cstore`);
37. this.needMove = false;
38. }
39. return this.eStore;
40. } else {
41. // 加锁状态 获取c类库
42. this.needMove = true;
43. try {
44. this.cStore = await store.getECStore(this.cInfo);
45. } catch (e) {
46. let error = e as BusinessError;
47. Logger.error(`Failed to GetECStore.code is ${error.code},message is ${error.message}`);
48. }
49. return this.cStore;
50. }
51. }

53. closeEStore(): void {
54. try {
55. let kvManager = distributedKVStore.createKVManager(this.eInfo.kvManagerConfig);
56. Logger.info('Succeeded in creating KVManager');
57. if (kvManager != undefined) {
58. kvManager.closeKVStore(this.eInfo.kvManagerConfig.bundleName, this.eInfo.storeId);
59. this.eStore = null;
60. Logger.info(`ECDB_Encry close EStore success`);
61. }
62. } catch (e) {
63. let error = e as BusinessError;
64. Logger.error(`Failed to create KVManager.code is ${error.code},message is ${error.message}`);
65. }
66. }

68. deleteCStore(): void {
69. try {
70. let kvManager = distributedKVStore.createKVManager(this.cInfo.kvManagerConfig);
71. Logger.info('Succeeded in creating KVManager');
72. if (kvManager != undefined) {
73. kvManager.deleteKVStore(this.cInfo.kvManagerConfig.bundleName, this.cInfo.storeId);
74. this.cStore = null;
75. Logger.info('ECDB_Encry delete cStore success');
76. }
77. } catch (e) {
78. let error = e as BusinessError;
79. Logger.error(`Failed to create KVManager.code is ${error.code},message is ${error.message}`);
80. }
81. }

83. private eStore: distributedKVStore.SingleKVStore = null;
84. private cStore: distributedKVStore.SingleKVStore = null;
85. private cInfo: StoreInfo | null = null;
86. private eInfo: StoreInfo | null = null;
87. private needMove: boolean = false;
88. private mover: Mover | null = null;
89. }
```

[ECStoreManager.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/KvStore/ECStoreSamples/entry/src/main/ets/entryability/ECStoreManager.ts#L16-L105)

### EntryAbility

模拟应用启动期间，注册对COMMON\_EVENT\_SCREEN\_LOCK\_FILE\_ACCESS\_STATE\_CHANGED公共事件的监听，并配置相应的数据库信息、密钥状态信息等。

```
1. import { AbilityConstant, application, contextConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { window } from '@kit.ArkUI';
4. import { distributedKVStore } from '@kit.ArkData';
5. import { ECStoreManager } from './ECStoreManager';
6. import { StoreInfo } from './Store';
7. import { Mover } from './Mover';
8. import { SecretKeyObserver } from './SecretKeyObserver';
9. import { commonEventManager } from '@kit.BasicServicesKit';
10. import { BusinessError } from '@kit.BasicServicesKit';
11. // Logger为hilog封装后实现的打印功能
12. import Logger from '../common/Logger';

14. export let storeManager = new ECStoreManager();
15. export let e_secretKeyObserver = new SecretKeyObserver();
16. let mover = new Mover();
17. let subscriber: commonEventManager.CommonEventSubscriber;

19. export function createCB(err: BusinessError, commonEventSubscriber: commonEventManager.CommonEventSubscriber) {
20. if (!err) {
21. Logger.info('ECDB_Encry createSubscriber');
22. subscriber = commonEventSubscriber;
23. try {
24. commonEventManager.subscribe(subscriber, (err: BusinessError, data: commonEventManager.CommonEventData) => {
25. if (err) {
26. Logger.error(`subscribe failed, code is ${err.code}, message is ${err.message}`);
27. } else {
28. Logger.info(`ECDB_Encry SubscribeCB ${data.code}`);
29. e_secretKeyObserver.updateLockStatus(data.code);
30. }
31. });
32. } catch (error) {
33. const err: BusinessError = error as BusinessError;
34. Logger.error(`subscribe failed, code is ${err.code}, message is ${err.message}`);
35. }
36. } else {
37. Logger.error(`createSubscriber failed, code is ${err.code}, message is ${err.message}`);
38. }
39. }

41. let cInfo: StoreInfo | null = null;
42. let eInfo: StoreInfo | null = null;

44. export default class EntryAbility extends UIAbility {
45. async onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): Promise<void> {
46. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
47. let cContext = this.context;
48. cInfo = {
49. 'kvManagerConfig': {
50. context: cContext,
51. bundleName: 'com.example.ecstoresamples'
52. },
53. 'storeId': 'cstore',
54. 'option': {
55. createIfMissing: true,
56. encrypt: false,
57. backup: false,
58. autoSync: false,
59. // kvStoreType不填时，默认创建多设备协同数据库
60. kvStoreType: distributedKVStore.KVStoreType.SINGLE_VERSION,
61. // 多设备协同数据库：kvStoreType: distributedKVStore.KVStoreType.DEVICE_COLLABORATION
62. securityLevel: distributedKVStore.SecurityLevel.S3
63. }
64. }
65. let eContext = await application.createModuleContext(this.context,'entry');
66. eContext.area = contextConstant.AreaMode.EL5;
67. eInfo = {
68. 'kvManagerConfig': {
69. context: eContext,
70. bundleName: 'com.example.ecstoresamples'
71. },
72. 'storeId': 'estore',
73. 'option': {
74. createIfMissing: true,
75. encrypt: false,
76. backup: false,
77. autoSync: false,
78. // kvStoreType不填时，默认创建多设备协同数据库
79. kvStoreType: distributedKVStore.KVStoreType.SINGLE_VERSION,
80. // 多设备协同数据库：kvStoreType: distributedKVStore.KVStoreType.DEVICE_COLLABORATION
81. securityLevel: distributedKVStore.SecurityLevel.S3
82. }
83. }
84. Logger.info(`ECDB_Encry store area : estore:${eContext.area},cstore${cContext.area}`);
85. // 监听COMMON_EVENT_SCREEN_LOCK_FILE_ACCESS_STATE_CHANGED事件 code == 1解锁状态，code==0加锁状态
86. try {
87. commonEventManager.createSubscriber({
88. events: [ 'COMMON_EVENT_SCREEN_LOCK_FILE_ACCESS_STATE_CHANGED' ]
89. }, createCB);
90. Logger.info(`ECDB_Encry success subscribe`);
91. } catch (error) {
92. const err: BusinessError = error as BusinessError;
93. Logger.error(`createSubscriber failed, code is ${err.code}, message is ${err.message}`);
94. }
95. storeManager.config(cInfo, eInfo);
96. storeManager.configDataMover(mover);
97. e_secretKeyObserver.initialize(storeManager);
98. }

100. onDestroy(): void {
101. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onDestroy');
102. }

104. onWindowStageCreate(windowStage: window.WindowStage): void {
105. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

107. windowStage.loadContent('pages/Index', (err) => {
108. if (err.code) {
109. hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
110. return;
111. }
112. hilog.info(0x0000, 'testTag', 'Succeeded in loading the content.');
113. });
114. }

116. onWindowStageDestroy(): void {
117. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
118. }

120. onForeground(): void {
121. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onForeground');
122. }

124. onBackground(): void {
125. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onBackground');
126. }
127. }
```

[EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/KvStore/ECStoreSamples/entry/src/main/ets/entryability/EntryAbility.ets#L16-L143)

### Index按键事件

使用Button按钮，通过点击按钮来模拟应用操作数据库，如插入数据、删除数据、更新数据和获取数据数量的操作等，展示数据库基本的增删改查能力。

```
1. import { storeManager, e_secretKeyObserver } from '../entryability/EntryAbility';
2. import { distributedKVStore } from '@kit.ArkData';
3. import { Store } from '../entryability/Store';

5. let storeOption = new Store();
6. let lockStatus: number = 1;

8. @Entry
9. @Component
10. struct Index {
11. @State message: string = 'Hello World';

13. build() {
14. Row() {
15. Column() {
16. Button('加锁/解锁').onClick((event: ClickEvent) => {
17. if (lockStatus) {
18. e_secretKeyObserver.onLock();
19. lockStatus = 0;
20. } else {
21. e_secretKeyObserver.onUnLock();
22. lockStatus = 1;
23. }
24. lockStatus ? this.message = '解锁' : this.message = '加锁';
25. }).margin(5)
26. .width(100) // 宽度，单位默认vp（可视像素）
27. .height(40) // 高度

29. Button('StoreType').onClick(async (event: ClickEvent) => {
30. e_secretKeyObserver.getCurrentStatus() ? this.message = 'estore' : this.message = 'cstore';
31. }).margin(5)
32. .width(100) // 宽度，单位默认vp（可视像素）
33. .height(40) // 高度

35. Button('Put').onClick(async (event: ClickEvent) => {
36. let store: distributedKVStore.SingleKVStore = await storeManager.getCurrentStore(e_secretKeyObserver.getCurrentStatus());
37. storeOption.putOnedata(store);
38. }).margin(5)
39. .width(100) // 宽度，单位默认vp（可视像素）
40. .height(40) // 高度

42. Button('Get').onClick(async (event: ClickEvent) => {
43. let store: distributedKVStore.SingleKVStore = await storeManager.getCurrentStore(e_secretKeyObserver.getCurrentStatus());
44. storeOption.getDataNum(store);
45. }).margin(5)
46. .width(100) // 宽度，单位默认vp（可视像素）
47. .height(40) // 高度

49. Button('Delete').onClick(async (event: ClickEvent) => {
50. let store: distributedKVStore.SingleKVStore = await storeManager.getCurrentStore(e_secretKeyObserver.getCurrentStatus());
51. storeOption.deleteOnedata(store);
52. }).margin(5)
53. .width(100) // 宽度，单位默认vp（可视像素）
54. .height(40) // 高度

56. Button('Update').onClick(async (event: ClickEvent) => {
57. let store: distributedKVStore.SingleKVStore = await storeManager.getCurrentStore(e_secretKeyObserver.getCurrentStatus());
58. storeOption.updateOnedata(store);
59. }).margin(5)
60. .width(100) // 宽度，单位默认vp（可视像素）
61. .height(40) // 高度

63. Text(this.message)
64. .fontSize(50)
65. .fontWeight(FontWeight.Bold)
66. }
67. .width('100%')
68. }
69. .height('100%')
70. }
71. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/KvStore/ECStoreSamples/entry/src/main/ets/pages/Index.ets#L16-L88)

## 关系型数据库E类加密

本章节提供关系型数据库的E类加密数据库使用方式，提供[Mover](encrypted-estore-guidelines.md#mover-1)类，[Store](encrypted-estore-guidelines.md#store-1)类，[SecretKeyObserver](encrypted-estore-guidelines.md#secretkeyobserver-1)类和[ECStoreManager](encrypted-estore-guidelines.md#ecstoremanager-1)类的具体实现，并在[EntryAbility](encrypted-estore-guidelines.md#entryability-1)和[index按键事件](encrypted-estore-guidelines.md#index按键事件-1)中展示这几个类的使用方式。

### Mover

提供数据库数据迁移接口，在锁屏解锁后，若C类数据库中有数据，使用该接口将数据迁移到E类数据库。

```
1. import { relationalStore } from '@kit.ArkData';

3. export class Mover {
4. async move(eStore: relationalStore.RdbStore, cStore: relationalStore.RdbStore) {
5. if (eStore != null && cStore != null) {
6. let predicates = new relationalStore.RdbPredicates('employee');
7. let resultSet = await cStore.query(predicates);
8. while (resultSet.goToNextRow()) {
9. let bucket = resultSet.getRow();
10. await eStore.insert('employee', bucket);
11. }
12. }
13. }
14. }
```

[Mover.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/RelationalStore/RdbStore/entry/src/main/ets/encryptedEStoreGuidelines/Mover.ts#L16-L31)

### Store

提供了获取数据库，在数据库中插入数据、删除数据、更新数据和获取当前数据数量的接口。其中StoreInfo类用于存储获取数据库相关信息。

```
1. import { relationalStore } from '@kit.ArkData';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { Context } from '@kit.AbilityKit';

5. export class StoreInfo {
6. context: Context;
7. config: relationalStore.StoreConfig;
8. storeId: string;
9. }

11. let id = 1;
12. const SQL_CREATE_TABLE = 'CREATE TABLE IF NOT EXISTS EMPLOYEE (ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT NOT NULL, AGE INTEGER, SALARY REAL, CODES BLOB)';

15. export class Store {
16. async getECStore(storeInfo: StoreInfo): Promise<relationalStore.RdbStore> {
17. let rdbStore: relationalStore.RdbStore | null;
18. try {
19. rdbStore = await relationalStore.getRdbStore(storeInfo.context, storeInfo.config);
20. if (rdbStore.version == 0) {
21. await rdbStore.executeSql(SQL_CREATE_TABLE);
22. console.info(`ECDB_Encry succeeded in getting Store ：${storeInfo.storeId}`);
23. rdbStore.version = 1;
24. }
25. } catch (e) {
26. let error = e as BusinessError;
27. console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
28. }
29. return rdbStore;
30. }

32. async putOnedata(rdbStore: relationalStore.RdbStore) {
33. if (rdbStore != undefined) {
34. const valueBucket: relationalStore.ValuesBucket = {
35. ID: id++,
36. NAME: 'Lisa',
37. AGE: 18,
38. SALARY: 100.5,
39. CODES: new Uint8Array([1, 2, 3, 4, 5]),
40. };
41. try {
42. await rdbStore.insert('EMPLOYEE', valueBucket);
43. console.info(`ECDB_Encry insert success`);
44. } catch (e) {
45. let error = e as BusinessError;
46. console.error(`An unexpected error occurred. Code:${error.code},message:${error.message}`);
47. }
48. }
49. }

51. async getDataNum(rdbStore: relationalStore.RdbStore) {
52. if (rdbStore != undefined) {
53. try {
54. let predicates = new relationalStore.RdbPredicates('EMPLOYEE');
55. let resultSet = await rdbStore.query(predicates);
56. let count = resultSet.rowCount;
57. console.info(`ECDB_Encry getdatanum success count : ${count}`);
58. } catch (e) {
59. let error = e as BusinessError;
60. console.error(`An unexpected error occurred. Code:${error.code},message:${error.message}`);
61. }
62. }
63. }

65. async deleteAlldata(rdbStore: relationalStore.RdbStore) {
66. if (rdbStore != undefined) {
67. try {
68. let predicates = new relationalStore.RdbPredicates('EMPLOYEE');
69. predicates.equalTo('AGE', 18);
70. await rdbStore.delete(predicates);
71. console.info(`ECDB_Encry delete Success`);
72. } catch (e) {
73. let error = e as BusinessError;
74. console.error(`An unexpected error occurred. Code:${error.code},message:${error.message}`);
75. }
76. }
77. }

79. async updateOnedata(rdbStore: relationalStore.RdbStore) {
80. if (rdbStore != undefined) {
81. try {
82. let predicates = new relationalStore.RdbPredicates('EMPLOYEE');
83. predicates.equalTo('NAME', 'Lisa');
84. const valueBucket: relationalStore.ValuesBucket = {
85. NAME: 'Anna',
86. SALARY: 100.5,
87. CODES: new Uint8Array([1, 2, 3, 4, 5]),
88. };
89. await rdbStore.update(valueBucket, predicates);
90. console.info(`ECDB_Encry update success`);
91. } catch (e) {
92. let error = e as BusinessError;
93. console.error(`An unexpected error occurred. Code:${error.code},message:${error.message}`);
94. }
95. }
96. }
97. }
```

[Store.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/RelationalStore/RdbStore/entry/src/main/ets/encryptedEStoreGuidelines/Store.ts#L16-L114)

### SecretKeyObserver

该类提供了获取当前密钥状态的接口，在密钥销毁后，关闭E类数据库。

```
1. import { ECStoreManager } from './ECStoreManager';

3. export enum SecretStatus {
4. Lock,
5. UnLock
6. }

8. export class SecretKeyObserver {
9. onLock(): void {
10. this.lockStatus = SecretStatus.Lock;
11. this.storeManager.closeEStore();
12. }

14. onUnLock(): void {
15. this.lockStatus = SecretStatus.UnLock;
16. }

18. getCurrentStatus(): number {
19. return this.lockStatus;
20. }

22. initialize(storeManager: ECStoreManager): void {
23. this.storeManager = storeManager;
24. }

26. updateLockStatus(code: number) {
27. if (this.lockStatus === SecretStatus.Lock) {
28. this.onLock();
29. } else {
30. this.lockStatus = code;
31. }
32. }

34. private lockStatus: number = SecretStatus.UnLock;
35. private storeManager: ECStoreManager;
36. }

38. export let lockObserve = new SecretKeyObserver();
```

[SecretKeyObserver.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/RelationalStore/RdbStore/entry/src/main/ets/encryptedEStoreGuidelines/SecretKeyObserver.ts#L16-L55)

### ECStoreManager

ECStoreManager类用于管理应用的E类数据库和C类数据库。支持配置数据库信息、配置迁移函数的信息，可根据密钥状态为应用提供相应的数据库句柄，并提供了关闭E类数据库、数据迁移完成后销毁C类数据库等接口。

```
1. import { relationalStore } from '@kit.ArkData';
2. import { Mover } from './Mover';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { StoreInfo, Store } from './Store';
5. import { SecretStatus } from './SecretKeyObserver';

7. let store = new Store();

9. export class ECStoreManager {
10. config(cInfo: StoreInfo, other: StoreInfo): void {
11. this.cInfo = cInfo;
12. this.eInfo = other;
13. }

15. configDataMover(mover: Mover): void {
16. this.mover = mover;
17. }

19. async getCurrentStore(screenStatus: number): Promise<relationalStore.RdbStore> {
20. if (screenStatus === SecretStatus.UnLock) {
21. try {
22. this.eStore = await store.getECStore(this.eInfo);
23. } catch (e) {
24. let error = e as BusinessError;
25. console.error(`Failed to GetECStore.code is ${error.code},message is ${error.message}`);
26. }
27. // 解锁状态 获取e类库
28. if (this.needMove) {
29. if (this.eStore != undefined && this.cStore != undefined) {
30. await this.mover.move(this.eStore, this.cStore);
31. console.info(`ECDB_Encry cstore data move to estore success`);
32. }
33. this.deleteCStore();
34. this.needMove = false;
35. }
36. return this.eStore;
37. } else {
38. // 加锁状态 获取c类库
39. this.needMove = true;
40. try {
41. this.cStore = await store.getECStore(this.cInfo);
42. } catch (e) {
43. let error = e as BusinessError;
44. console.error(`Failed to GetECStore.code is ${error.code},message is ${error.message}`);
45. }
46. return this.cStore;
47. }
48. }

50. closeEStore(): void {
51. this.eStore = undefined;
52. }

54. async deleteCStore() {
55. try {
56. await relationalStore.deleteRdbStore(this.cInfo.context, this.cInfo.storeId)
57. } catch (e) {
58. let error = e as BusinessError;
59. console.error(`Failed to create KVManager.code is ${error.code},message is ${error.message}`);
60. }
61. }

63. private eStore: relationalStore.RdbStore = null;
64. private cStore: relationalStore.RdbStore = null;
65. private cInfo: StoreInfo | null = null;
66. private eInfo: StoreInfo | null = null;
67. private needMove: boolean = false;
68. private mover: Mover | null = null;
69. }
```

[ECStoreManager.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/RelationalStore/RdbStore/entry/src/main/ets/encryptedEStoreGuidelines/ECStoreManager.ts#L16-L86)

### EntryAbility

模拟在应用启动期间，注册对COMMON\_EVENT\_SCREEN\_LOCK\_FILE\_ACCESS\_STATE\_CHANGED公共事件的监听，并配置相应的数据库信息、密钥状态信息等。

```
1. import { AbilityConstant, contextConstant, UIAbility, Want, application } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { window } from '@kit.ArkUI';
4. import { relationalStore } from '@kit.ArkData';
5. import { ECStoreManager } from '../encryptedEStoreGuidelines/ECStoreManager';
6. import { StoreInfo } from '../encryptedEStoreGuidelines/Store';
7. import { Mover } from '../encryptedEStoreGuidelines/Mover';
8. import { SecretKeyObserver } from '../encryptedEStoreGuidelines/SecretKeyObserver';
9. import { commonEventManager } from '@kit.BasicServicesKit';
10. import { BusinessError } from '@kit.BasicServicesKit';

12. export let storeManager = new ECStoreManager();
13. export let e_secretKeyObserver = new SecretKeyObserver();
14. let mover = new Mover();
15. let subscriber: commonEventManager.CommonEventSubscriber;

17. export function createCB(err: BusinessError, commonEventSubscriber: commonEventManager.CommonEventSubscriber) {
18. if (!err) {
19. console.info('ECDB_Encrypt createSubscriber');
20. subscriber = commonEventSubscriber;
21. try {
22. commonEventManager.subscribe(subscriber, (err: BusinessError, data: commonEventManager.CommonEventData) => {
23. if (err) {
24. console.error(`subscribe failed, code is ${err.code}, message is ${err.message}`);
25. } else {
26. console.info(`ECDB_Encrypt SubscribeCB ${data.code}`);
27. e_secretKeyObserver.updateLockStatus(data.code);
28. }
29. });
30. } catch (error) {
31. const err: BusinessError = error as BusinessError;
32. console.error(`subscribe failed, code is ${err.code}, message is ${err.message}`);
33. }
34. } else {
35. console.error(`createSubscriber failed, code is ${err.code}, message is ${err.message}`);
36. }
37. }

39. let cInfo: StoreInfo | null = null;
40. let eInfo: StoreInfo | null = null;

42. export default class EntryAbility extends UIAbility {
43. async onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): Promise<void> {
44. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
45. let cContext = this.context;
46. cInfo = {
47. context: cContext,
48. config: {
49. name: 'cstore.db',
50. securityLevel: relationalStore.SecurityLevel.S3,
51. },
52. storeId: 'cstore.db'
53. };
54. let eContext = await application.createModuleContext(this.context, 'entry');
55. eContext.area = contextConstant.AreaMode.EL5;
56. eInfo = {
57. context: eContext,
58. config: {
59. name: 'estore.db',
60. securityLevel: relationalStore.SecurityLevel.S3,
61. },
62. storeId: 'estore.db',
63. };
64. // 监听COMMON_EVENT_SCREEN_LOCK_FILE_ACCESS_STATE_CHANGED事件 code == 1解锁状态，code==0加锁状态
65. console.info(`ECDB_Encry store area : estore:${eContext.area},cstore${cContext.area}`)
66. try {
67. commonEventManager.createSubscriber({
68. events: ['COMMON_EVENT_SCREEN_LOCK_FILE_ACCESS_STATE_CHANGED']
69. }, createCB);
70. console.info(`ECDB_Encry success subscribe`);
71. } catch (error) {
72. const err: BusinessError = error as BusinessError;
73. console.error(`createSubscriber failed, code is ${err.code}, message is ${err.message}`);
74. }
75. storeManager.config(cInfo, eInfo);
76. storeManager.configDataMover(mover);
77. e_secretKeyObserver.initialize(storeManager);
78. }

80. onDestroy(): void {
81. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onDestroy');
82. }

84. onWindowStageCreate(windowStage: window.WindowStage): void {
85. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

87. windowStage.loadContent('pages/Index', (err) => {
88. if (err.code) {
89. hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
90. return;
91. }
92. hilog.info(0x0000, 'testTag', 'Succeeded in loading the content.');
93. });
94. }

96. onWindowStageDestroy(): void {
97. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
98. }

100. onForeground(): void {
101. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onForeground');
102. }

104. onBackground(): void {
105. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onBackground');
106. }
107. }
```

[EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/RelationalStore/RdbStore/entry/src/main/ets/entryability/EntryAbility.ets#L16-L124)

### Index按键事件

使用Button按钮，通过点击按钮来模拟应用操作数据库，如插入数据、删除数据、更新数据和获取数据数量的操作等，展示数据库基本的增删改查能力。

```
1. import { storeManager, e_secretKeyObserver } from '../entryability/EntryAbility';
2. import { relationalStore } from '@kit.ArkData';
3. import { Store } from './Store';

5. let storeOption = new Store();

7. let lockStatus: number = 1;

9. @Entry
10. @Component
11. struct Index {
12. @State message: string = '';

14. build() {
15. Row() {
16. Column() {
17. Button('加锁/解锁')
18. .onClick((event: ClickEvent) => {
19. if (lockStatus) {
20. e_secretKeyObserver.onLock();
21. lockStatus = 0;
22. } else {
23. e_secretKeyObserver.onUnLock();
24. lockStatus = 1;
25. }
26. lockStatus ? this.message = '解锁' : this.message = '加锁';
27. })
28. .margin('5')
29. .backgroundColor('#0D9FFB')
30. .width('50%')
31. .height('5%')
32. .type(ButtonType.Capsule)

34. Button('store type')
35. .onClick(async (event: ClickEvent) => {
36. e_secretKeyObserver.getCurrentStatus() ? this.message = 'estore' : this.message = 'cstore';
37. console.info(`ECDB_Encry current store : ${this.message}`);
38. })
39. .margin('5')
40. .backgroundColor('#0D9FFB')
41. .width('50%')
42. .height('5%')
43. .type(ButtonType.Capsule)

45. Button('put')
46. .onClick(async (event: ClickEvent) => {
47. let store: relationalStore.RdbStore = await storeManager.getCurrentStore(e_secretKeyObserver.getCurrentStatus());
48. storeOption.putOnedata(store);
49. })
50. .margin(5)
51. .backgroundColor('#0D9FFB')
52. .width('50%')
53. .height('5%')
54. .type(ButtonType.Capsule)

56. Button('Get')
57. .onClick(async (event: ClickEvent) => {
58. let store: relationalStore.RdbStore = await storeManager.getCurrentStore(e_secretKeyObserver.getCurrentStatus());
59. storeOption.getDataNum(store);
60. })
61. .margin(5)
62. .backgroundColor('#0D9FFB')
63. .width('50%')
64. .height('5%')
65. .type(ButtonType.Capsule)

67. Button('delete')
68. .onClick(async (event: ClickEvent) => {
69. let store: relationalStore.RdbStore = await storeManager.getCurrentStore(e_secretKeyObserver.getCurrentStatus());
70. storeOption.deleteAlldata(store);
71. })
72. .margin(5)
73. .backgroundColor('#0D9FFB')
74. .width('50%')
75. .height('5%')
76. .type(ButtonType.Capsule)

78. Button('update')
79. .onClick(async (event: ClickEvent) => {
80. let store: relationalStore.RdbStore = await storeManager.getCurrentStore(e_secretKeyObserver.getCurrentStatus());
81. storeOption.updateOnedata(store);
82. })
83. .margin(5)
84. .backgroundColor('#0D9FFB')
85. .width('50%')
86. .height('5%')
87. .type(ButtonType.Capsule)

89. Text(this.message)
90. .fontSize(50)
91. .fontWeight(FontWeight.Bold)
92. }
93. .width('100%')
94. }
95. .height('100%')
96. }
97. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/RelationalStore/RdbStore/entry/src/main/ets/encryptedEStoreGuidelines/Index.ets#L16-L114)
