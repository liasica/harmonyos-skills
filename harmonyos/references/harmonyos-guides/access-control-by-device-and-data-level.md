---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/access-control-by-device-and-data-level
title: 基于设备分类和数据分级的访问控制 (ArkTS)
breadcrumb: 指南 > 应用框架 > ArkData（方舟数据管理） > 数据可靠性与安全性 > 基于设备分类和数据分级的访问控制 (ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:21+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e84d2482c0010257179f1217748716a1077fd5269ae2ef9916b9c9242b44666d
---

## 基本概念

分布式数据管理对数据实施分类分级保护，提供基于数据安全标签以及设备安全等级的访问控制机制。

数据安全标签和设备安全等级越高，加密措施和访问控制措施越严格，数据安全性越高。

### 数据安全标签

按照数据分类分级规范要求，可将数据分为S1、S2、S3、S4四个安全等级。

| 风险等级 | 风险标准 | 定义 | 样例 |
| --- | --- | --- | --- |
| 严重 | S4 | 业界法律法规定义的特殊数据类型，涉及个人的最私密领域的信息或一旦泄露、篡改、破坏、销毁可能会给个人或组织造成重大的不利影响的数据。 | 政治观点、宗教和哲学信仰、工会成员资格、基因数据、生物信息、健康和性生活状况，性取向等或设备认证鉴权、个人信用卡等财务信息等。 |
| 高 | S3 | 数据的泄露、篡改、破坏、销毁可能会给个人或组织导致严峻的不利影响。 | 个人实时精确定位信息、运动轨迹等。 |
| 中 | S2 | 数据的泄露、篡改、破坏、销毁可能会给个人或组织导致严重的不利影响。 | 个人的详细通信地址、姓名昵称等。 |
| 低 | S1 | 数据的泄露、篡改、破坏、销毁可能会给个人或组织导致有限的不利影响。 | 性别、国籍、用户申请记录等。 |

### 设备安全等级

根据设备安全能力，比如是否有TEE、是否有安全存储芯片等，将设备安全等级分为SL1、SL2、SL3、SL4、SL5五个等级。例如，手表通常为低安全的SL1设备，手机、平板通常为高安全的SL4设备。

在设备组网时可以通过hidumper -s 3511查看设备安全等级。

## 跨设备同步访问控制机制

数据跨设备同步时，基于数据安全标签和设备安全等级进行访问控制。数据库的数据安全标签不高于对端设备的设备安全等级时，数据才能同步。具体访问控制矩阵如下：

| 设备安全级别 | 可同步的数据安全标签 |
| --- | --- |
| SL1 | S1 |
| SL2 | S1~S2 |
| SL3 | S1~S3 |
| SL4 | S1~S4 |
| SL5 | S1~S4 |

例如，手表通常为低安全的SL1设备。若创建数据安全标签为S1的数据库，则此数据库数据可以在这些设备间同步；若创建的数据库标签为S2-S4，则不能在这些设备间同步。

## 场景介绍

分布式数据库的访问控制机制确保了数据存储和同步时的安全能力。在创建数据库时，应当基于数据分类分级规范合理地设置数据库的安全标签，确保数据库内容和数据标签的一致性。

## 使用键值型数据库实现数据分级

键值型数据库，通过securityLevel参数设置数据库的安全等级，安全等级具体可见[SecurityLevel](../harmonyos-references/js-apis-distributedkvstore.md#securitylevel)枚举。此处以创建安全等级为S3的数据库为例。

具体接口及功能，可见[分布式键值数据库](../harmonyos-references/js-apis-distributedkvstore.md)。

说明

在单设备使用场景下，KV数据库支持修改securityLevel开库参数进行安全等级升级。数据库安全等级升级操作需要注意以下几点：

* 该操作不支持需要进行跨设备同步的数据库，不同安全等级的数据库之间不能进行数据同步，需要跨设备同步的数据库如果要升级安全等级，建议重新创建更高安全等级的数据库。
* 该操作需在关闭当前数据库之后，通过修改securityLevel开库参数重新设置数据库的安全等级，再进行开库操作。
* 该操作只支持升级，不支持降级。例如支持S2->S3的升级，不支持S3->S2的降级。

```
1. // 导入模块
2. // 在pages目录下新建KvStoreInterface.ets
3. import { distributedKVStore } from '@kit.ArkData';
4. import { BusinessError } from '@kit.BasicServicesKit';
5. import EntryAbility from '../entryability/EntryAbility';
6. // Logger为hilog封装后实现的打印功能
7. import Logger from '../common/Logger';

9. let kvManager: distributedKVStore.KVManager | undefined = undefined;
10. let kvStore: distributedKVStore.SingleKVStore | undefined = undefined;
11. let appId: string = 'com.example.kvstoresamples';
12. let storeId: string = 'storeId';
13. const context = EntryAbility.getContext();

15. // 下面所有接口的代码都实现在KvInterface中
16. export class KvInterface {
17. }
```

```
1. public CreateKvManager = (() => {
2. Logger.info('CreateKvManager start');
3. if (typeof (kvManager) === 'undefined') {
4. const kvManagerConfig: distributedKVStore.KVManagerConfig = {
5. bundleName: appId,
6. context: context
7. };
8. try {
9. // 创建KVManager实例
10. kvManager = distributedKVStore.createKVManager(kvManagerConfig);
11. Logger.info('Succeeded in creating KVManager.');
12. } catch (err) {
13. Logger.error(`Failed to create KVManager. Code:${err.code},message:${err.message}`);
14. }
15. } else {
16. Logger.info ('KVManager has created');
17. }
18. })
```

[KvStoreInterface.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/KvStore/KvStoreSamples/entry/src/main/ets/pages/KvStoreInterface.ets#L29-L48)

```
1. public GetKvStore = (() => {
2. Logger.info('GetKvStore start');
3. if (kvManager === undefined) {
4. Logger.info('KvManager not initialized');
5. return;
6. }
7. try {
8. let child1 = new distributedKVStore.FieldNode('id');
9. child1.type = distributedKVStore.ValueType.INTEGER;
10. child1.nullable = false;
11. child1.default = '1';
12. let child2 = new distributedKVStore.FieldNode('name');
13. child2.type = distributedKVStore.ValueType.STRING;
14. child2.nullable = false;
15. child2.default = 'zhangsan';

17. let schema = new distributedKVStore.Schema();
18. schema.root.appendChild(child1);
19. schema.root.appendChild(child2);
20. schema.indexes = ['$.id', '$.name'];
21. // 0表示COMPATIBLE模式，1表示STRICT模式。
22. schema.mode = 1;
23. // 支持在检查Value时，跳过skip指定的字节数，且取值范围为[0,4M-2]。
24. schema.skip = 0;

26. const options: distributedKVStore.Options = {
27. createIfMissing: true,
28. // 设置数据库加密
29. encrypt: true,
30. backup: false,
31. autoSync: false,
32. // kvStoreType不填时，默认创建多设备协同数据库
33. kvStoreType: distributedKVStore.KVStoreType.SINGLE_VERSION,
34. // 多设备协同数据库：kvStoreType: distributedKVStore.KVStoreType.DEVICE_COLLABORATION,
35. schema: schema,
36. // schema未定义可以不填，定义方法请参考上方schema示例。
37. securityLevel: distributedKVStore.SecurityLevel.S3
38. };
39. kvManager.getKVStore<distributedKVStore.SingleKVStore>(storeId, options,
40. (err, store: distributedKVStore.SingleKVStore) => {
41. if (err) {
42. Logger.error(`Failed to get KVStore: Code:${err.code},message:${err.message}`);
43. return;
44. }
45. Logger.info('Succeeded in getting KVStore.');
46. kvStore = store;
47. // 请确保获取到键值数据库实例后，再进行相关数据操作
48. });
49. } catch (e) {
50. let error = e as BusinessError;
51. Logger.error(`An unexpected error occurred. Code:${error.code},message:${error.message}`);
52. }
53. })
```

[KvStoreInterface.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/KvStore/KvStoreSamples/entry/src/main/ets/pages/KvStoreInterface.ets#L50-L104)

## 使用关系型数据库实现数据分级

关系型数据库，通过securityLevel参数设置数据库的安全等级，安全等级具体可见[SecurityLevel](../harmonyos-references/arkts-apis-data-relationalstore-e.md#securitylevel)枚举。此处以创建安全等级为S3的数据库为例。

具体接口及功能，可见[@ohos.data.relationalStore (关系型数据库)](../harmonyos-references/arkts-apis-data-relationalstore.md)。

```
1. import { relationalStore } from '@kit.ArkData';
2. import { UIContext } from '@kit.ArkUI';
3. import { common } from '@kit.AbilityKit';

5. let store: relationalStore.RdbStore | undefined = undefined;

7. export async function accessControlByDeviceAndDataLevel() {
8. /* context为应用的上下文信息，由调用方自行获取，此处仅为示例。 */
9. const context = new UIContext().getHostContext() as common.UIAbilityContext;
10. try {
11. const STORE_CONFIG: relationalStore.StoreConfig = {
12. name: 'RdbTest.db',
13. // 设置数据库安全级别为S3
14. securityLevel: relationalStore.SecurityLevel.S3
15. };
16. store = await relationalStore.getRdbStore(context, STORE_CONFIG);
17. console.info('Succeeded in getting RdbStore.')
18. } catch (err) {
19. console.error(`Failed to get RdbStore. Code:${err.code}, message:${err.message}`);
20. }
21. }
```

[accessControlByDeviceAndDataLevel.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/RelationalStore/RdbStore/entry/src/main/ets/pages/accessControlByDeviceAndDataLevel.ets#L16-L35)
