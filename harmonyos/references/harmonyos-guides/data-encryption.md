---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-encryption
title: 数据库加密 (ArkTS)
breadcrumb: 指南 > 应用框架 > ArkData（方舟数据管理） > 数据可靠性与安全性 > 数据库加密 (ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:21+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6c705e68bd38d61775c1324ebcab4d9347d0503dfd09fddd35685031a5c14403
---

## 场景介绍

为了增强数据库的安全性，数据库提供了一个安全适用的数据库加密能力，从而对数据库存储的内容实施有效保护。通过数据库加密等安全方法实现了数据库数据存储的保密性和完整性要求，使得数据库以密文方式存储并在密态方式下工作，确保了数据安全。

键值型数据库的加密属性在创建时确定，不可修改；关系型数据库从API version 22开始，支持通过[rekeyEx](../harmonyos-references/arkts-apis-data-relationalstore-rdbstore.md#rekeyex22)接口调整其加密属性。

键值型数据库和关系型数据库均支持数据库加密操作，其中关系型数据库支持自定义加密/解密的密钥和其他参数。

## 键值型数据库加密

键值型数据库，通过options中encrypt参数来设置是否加密，默认为false，表示不加密。encrypt参数为true时表示加密。

具体接口及功能，可见[分布式键值数据库](../harmonyos-references/js-apis-distributedkvstore.md)。

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

## 关系型数据库加密

关系型数据库，通过[StoreConfig](../harmonyos-references/arkts-apis-data-relationalstore-i.md#storeconfig)中encrypt属性来设置是否加密。encrypt参数为true时表示加密；为false时表示不加密；默认值为false。

当encrypt为true时，支持开发者通过ArkTS API中的可选属性cryptoParam设置自定义的加密/解密密钥和算法等参数。

针对cryptoParam的配置与否，有如下两种场景：

场景1：不配置cryptoParam属性，此时会使用默认的加密配置进行数据库的加密/解密。

```
1. import { relationalStore } from '@kit.ArkData';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit'
4. import { UIContext } from '@kit.ArkUI';
5. import { common } from '@kit.AbilityKit';
```

[Encryption.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/RelationalStore/NativeDataEncryption/entry/src/main/ets/pages/encryption/Encryption.ets#L17-L21)

```
1. let store: relationalStore.RdbStore | undefined = undefined;

3. /* context为应用的上下文信息，由调用方自行获取，此处仅为示例。 */
4. const context = new UIContext().getHostContext() as common.UIAbilityContext;
5. try {
6. const STORE_CONFIG: relationalStore.StoreConfig = {
7. name: 'RdbTest.db',
8. securityLevel: relationalStore.SecurityLevel.S3,
9. encrypt: true
10. };
11. store = await relationalStore.getRdbStore(context, STORE_CONFIG);
12. hilog.info(DOMAIN, 'Encryption', 'Succeeded in getting RdbStore.');
13. } catch (e) {
14. const err = e as BusinessError;
15. hilog.error(DOMAIN, 'Encryption', `Failed to get RdbStore. Code:${err.code}, message:${err.message}`);
16. }
```

[Encryption.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/RelationalStore/NativeDataEncryption/entry/src/main/ets/pages/encryption/Encryption.ets#L28-L44)

场景2：配置cryptoParam属性，此时会使用开发者自定义的密钥和算法参数进行数据库的加密/解密。

```
1. let store: relationalStore.RdbStore | undefined = undefined;
2. // 初始化需要使用的密钥，示例中使用硬编码密钥仅用于演示目的， 实际应用中应使用安全的密钥管理服务
3. let key = new Uint8Array(32);
4. for (let i = 0; i < 32; i++) {
5. key[i] = i;
6. }

8. // 初始化加密算法
9. const CRYPTO_PARAM: relationalStore.CryptoParam = {
10. encryptionKey: key, // 必选参数，使用指定的密钥打开加密数据库。为空则由数据库负责生成并保存密钥，并使用生成的密钥打开数据库文件。
11. iterationCount: 25000, // 可选参数，迭代次数。迭代次数必须大于零。不指定或等于零则使用默认值10000和默认加密算法。
12. encryptionAlgo: relationalStore.EncryptionAlgo.AES_256_CBC, // 可选参数，加密/解密算法。如不指定，默认算法为AES_256_GCM。
13. hmacAlgo: relationalStore.HmacAlgo.SHA256, // 可选参数，HMAC算法。如不指定，默认值为SHA256。
14. kdfAlgo: relationalStore.KdfAlgo.KDF_SHA512, // 可选参数，KDF算法。如不指定，默认值和HMAC算法相等。
15. cryptoPageSize: 2048 // 可选参数，加密/解密时使用的页大小。必须为1024到65536范围内的整数并且为2的幂。如不指定，默认值为1024。
16. }

18. const STORE_CONFIG: relationalStore.StoreConfig = {
19. name: 'encrypted.db',
20. securityLevel: relationalStore.SecurityLevel.S3,
21. encrypt: true,
22. cryptoParam: CRYPTO_PARAM
23. }

25. /* context为应用的上下文信息，由调用方自行获取，此处仅为示例。 */
26. const context = new UIContext().getHostContext() as common.UIAbilityContext;
27. try {
28. store = await relationalStore.getRdbStore(context, STORE_CONFIG);
29. if (store == null) {
30. hilog.error(DOMAIN, 'Encryption', 'Failed to get RdbStore.');
31. } else {
32. hilog.info(DOMAIN, 'Encryption', 'Succeeded in getting RdbStore.');
33. }
34. // 调用完后需要将密钥清零
35. CRYPTO_PARAM.encryptionKey.fill(0);
36. key.fill(0);
37. } catch (e) {
38. const err = e as BusinessError;
39. hilog.error(DOMAIN, 'Encryption', `Failed to get RdbStore. Code:${err.code}, message:${err.message}`);
40. }
```

[Encryption.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/RelationalStore/NativeDataEncryption/entry/src/main/ets/pages/encryption/Encryption.ets#L51-L90)

如果开发者不关心加密使用的算法及参数，则无需配置cryptoParam属性，使用默认加密配置即可。当开发者需要自定义加密配置，或需要打开非默认配置的加密数据库时，则需要配置cryptoParam属性。
