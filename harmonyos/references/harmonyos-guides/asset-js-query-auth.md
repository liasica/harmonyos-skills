---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/asset-js-query-auth
title: 查询需要用户认证的关键资产(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Asset Store Kit（关键资产存储服务） > Asset Store Kit开发指导(ArkTS) > 查询需要用户认证的关键资产(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:12+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9f16981be7cb2a482d5f2656c367931f82098627d5dee752de95fca0cca6f0d4
---

## 接口介绍

可通过API文档查看此功能的相关接口：

| 异步接口 | 同步接口 | 说明 |
| --- | --- | --- |
| [preQuery(query: AssetMap)](../harmonyos-references/js-apis-asset.md#assetprequery) | [preQuerySync(query: AssetMap)](../harmonyos-references/js-apis-asset.md#assetprequerysync12) | 查询预处理。 |
| [query(query: AssetMap)](../harmonyos-references/js-apis-asset.md#assetquery) | [querySync(query: AssetMap)](../harmonyos-references/js-apis-asset.md#assetquerysync12) | 查询关键资产。 |
| [postQuery(handle: AssetMap)](../harmonyos-references/js-apis-asset.md#assetpostquery) | [postQuerySync(handle: AssetMap)](../harmonyos-references/js-apis-asset.md#assetpostquerysync12) | 查询后置处理。 |

查询需要用户认证的关键资产时，关键资产属性的内容（AssetMap）参数如下表所示：

注意

下表中“ALIAS”和名称包含“DATA\_LABEL”的关键资产属性，用于存储业务自定义信息，其内容不会被加密，请勿存放敏感个人数据。

* **preQuery参数列表**

  | 属性名称（Tag） | 属性内容（Value） | 是否必选 | 说明 |
  | --- | --- | --- | --- |
  | ALIAS | 类型为Uint8Array，长度为1-256字节。 | 可选 | 关键资产别名，每条关键资产的唯一索引。 |
  | ACCESSIBILITY | 类型为number，取值范围详见[Accessibility](../harmonyos-references/js-apis-asset.md#accessibility)。 | 可选 | 基于锁屏状态的访问控制。 |
  | REQUIRE\_PASSWORD\_SET | 类型为boolean。 | 可选 | 是否仅在设置了锁屏密码的情况下，可访问关键资产。为true时表示查询仅用户设置了锁屏密码才允许访问的关键资产；为false时表示查询无论用户是否设置锁屏密码，均可访问的关键资产。 |
  | AUTH\_TYPE | 类型为number，取值范围详见[AuthType](../harmonyos-references/js-apis-asset.md#authtype)。 | 可选 | 访问关键资产所需的用户认证类型。 |
  | AUTH\_VALIDITY\_PERIOD | 类型为number，取值范围：1-600，单位为秒。 | 可选 | 用户认证的有效期，默认值为60。 |
  | SYNC\_TYPE | 类型为number，取值范围详见[SyncType](../harmonyos-references/js-apis-asset.md#synctype)。 | 可选 | 关键资产支持的同步类型。 |
  | IS\_PERSISTENT | 类型为boolean。 | 可选 | 在应用卸载时是否需要保留关键资产。为true时表示查询应用卸载后会被保留的关键资产；为false时表示查询应用卸载后会被删除的关键资产。 |
  | DATA\_LABEL\_CRITICAL\_1 | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且有完整性保护。  **说明：** API12前长度为1-512字节。 |
  | DATA\_LABEL\_CRITICAL\_2 | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且有完整性保护。  **说明：** API12前长度为1-512字节。 |
  | DATA\_LABEL\_CRITICAL\_3 | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且有完整性保护。  **说明：** API12前长度为1-512字节。 |
  | DATA\_LABEL\_CRITICAL\_4 | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且有完整性保护。  **说明：** API12前长度为1-512字节。 |
  | DATA\_LABEL\_NORMAL\_1 | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且无完整性保护。  **说明：** API12前长度为1-512字节。 |
  | DATA\_LABEL\_NORMAL\_2 | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且无完整性保护。  **说明：** API12前长度为1-512字节。 |
  | DATA\_LABEL\_NORMAL\_3 | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且无完整性保护。  **说明：** API12前长度为1-512字节。 |
  | DATA\_LABEL\_NORMAL\_4 | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且无完整性保护。  **说明：** API12前长度为1-512字节。 |
  | DATA\_LABEL\_NORMAL\_LOCAL\_112+ | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属的本地信息，内容由业务自定义且无完整性保护，该项信息不会进行同步。 |
  | DATA\_LABEL\_NORMAL\_LOCAL\_212+ | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属的本地信息，内容由业务自定义且无完整性保护，该项信息不会进行同步。 |
  | DATA\_LABEL\_NORMAL\_LOCAL\_312+ | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属的本地信息，内容由业务自定义且无完整性保护，该项信息不会进行同步。 |
  | DATA\_LABEL\_NORMAL\_LOCAL\_412+ | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属的本地信息，内容由业务自定义且无完整性保护，该项信息不会进行同步。 |
  | REQUIRE\_ATTR\_ENCRYPTED14+ | 类型为boolean。 | 可选 | 是否查询业务自定义附属信息被加密的数据。为true时表示查询业务自定义附属信息加密存储的数据，为false时表示查询业务自定义附属信息不加密存储的数据。默认值为false。 |
  | GROUP\_ID18+ | 类型为Uint8Array，长度为7-127字节。 | 可选 | 待查询的关键资产所属群组，默认查询不属于任何群组的关键资产。 |
* **query参数列表**

  | 属性名称（Tag） | 属性内容（Value） | 是否必选 | 说明 |
  | --- | --- | --- | --- |
  | ALIAS | 类型为Uint8Array，长度为1-256字节。 | 必选 | 关键资产别名，每条关键资产的唯一索引。 |
  | AUTH\_CHALLENGE | 类型为Uint8Array，长度为32字节。 | 必选 | 用户认证的挑战值。 |
  | AUTH\_TOKEN | 类型为Uint8Array。  API 20开始：长度为1-1024字节。  API 11-19：长度为148字节。 | 必选 | 用户认证通过的授权令牌。 |
  | RETURN\_TYPE | 类型为number，asset.ReturnType.ALL。 | 必选 | 关键资产查询返回的结果类型。 |
  | ACCESSIBILITY | 类型为number，取值范围详见[Accessibility](../harmonyos-references/js-apis-asset.md#accessibility)。 | 可选 | 基于锁屏状态的访问控制。 |
  | REQUIRE\_PASSWORD\_SET | 类型为boolean。 | 可选 | 是否仅在设置了锁屏密码的情况下，可访问关键资产。为true时表示查询仅用户设置了锁屏密码才允许访问的关键资产；为false时表示查询无论用户是否设置锁屏密码，均可访问的关键资产。 |
  | AUTH\_TYPE | 类型为number，取值范围详见[AuthType](../harmonyos-references/js-apis-asset.md#authtype)。 | 可选 | 访问关键资产所需的用户认证类型。 |
  | SYNC\_TYPE | 类型为number，取值范围详见[SyncType](../harmonyos-references/js-apis-asset.md#synctype)。 | 可选 | 关键资产支持的同步类型。 |
  | IS\_PERSISTENT | 类型为boolean。 | 可选 | 在应用卸载时是否需要保留关键资产。为true时表示查询应用卸载后会被保留的关键资产；为false时表示查询应用卸载后会被删除的关键资产。 |
  | DATA\_LABEL\_CRITICAL\_1 | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且有完整性保护。  **说明：** API12前长度为1-512字节。 |
  | DATA\_LABEL\_CRITICAL\_2 | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且有完整性保护。  **说明：** API12前长度为1-512字节。 |
  | DATA\_LABEL\_CRITICAL\_3 | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且有完整性保护。  **说明：** API12前长度为1-512字节。 |
  | DATA\_LABEL\_CRITICAL\_4 | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且有完整性保护。  **说明：** API12前长度为1-512字节。 |
  | DATA\_LABEL\_NORMAL\_1 | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且无完整性保护。  **说明：** API12前长度为1-512字节。 |
  | DATA\_LABEL\_NORMAL\_2 | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且无完整性保护。  **说明：** API12前长度为1-512字节。 |
  | DATA\_LABEL\_NORMAL\_3 | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且无完整性保护。  **说明：** API12前长度为1-512字节。 |
  | DATA\_LABEL\_NORMAL\_4 | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且无完整性保护。  **说明：** API12前长度为1-512字节。 |
  | DATA\_LABEL\_NORMAL\_LOCAL\_112+ | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属的本地信息，内容由业务自定义且无完整性保护，该项信息不会进行同步。 |
  | DATA\_LABEL\_NORMAL\_LOCAL\_212+ | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属的本地信息，内容由业务自定义且无完整性保护，该项信息不会进行同步。 |
  | DATA\_LABEL\_NORMAL\_LOCAL\_312+ | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属的本地信息，内容由业务自定义且无完整性保护，该项信息不会进行同步。 |
  | DATA\_LABEL\_NORMAL\_LOCAL\_412+ | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属的本地信息，内容由业务自定义且无完整性保护，该项信息不会进行同步。 |
  | REQUIRE\_ATTR\_ENCRYPTED14+ | 类型为boolean。 | 可选 | 是否查询业务自定义附属信息被加密的数据。为true时表示查询业务自定义附属信息加密存储的数据，为false时表示查询业务自定义附属信息不加密存储的数据。默认值为false。 |
  | GROUP\_ID18+ | 类型为Uint8Array，长度为7-127字节。 | 可选 | 待查询的关键资产所属群组，默认查询不属于任何群组的关键资产。 |
* **postQuery参数列表**

  | 属性名称（Tag） | 属性内容（Value） | 是否必选 | 说明 |
  | --- | --- | --- | --- |
  | AUTH\_CHALLENGE | 类型为Uint8Array，长度为32字节。 | 必选 | 用户认证的挑战值。 |
  | GROUP\_ID18+ | 类型为Uint8Array，长度为7-127字节。 | 可选 | 待清理关键资产所属群组，默认清理内存中不属于任何群组的关键资产。 |

## 代码示例

说明

本模块提供了异步和同步两套接口，以下为异步接口的使用示例，同步接口详见[@ohos.security.asset (关键资产存储服务)](../harmonyos-references/js-apis-asset.md)。

在查询前，需确保已有需要用户认证的关键资产，可参考[指南文档](asset-js-add.md)新增关键资产，否则将抛出NOT\_FOUND错误（错误码24000002）。

查询别名是demo\_alias且需要用户认证的关键资产。示例中引入的@ohos.userIAM.userAuth用法详见userAuth文档中的[start](../harmonyos-references/js-apis-useriam-userauth.md#start10)接口。

1. 引用头文件，定义工具函数。

   ```
   1. import { asset } from '@kit.AssetStoreKit';
   2. import { util } from '@kit.ArkTS';
   3. import { userAuth } from '@kit.UserAuthenticationKit';
   4. import { BusinessError } from '@kit.BasicServicesKit';

   6. function stringToArray(str: string): Uint8Array {
   7. let textEncoder = new util.TextEncoder();
   8. return textEncoder.encodeInto(str);
   9. }

   11. function arrayToString(arr: Uint8Array): string {
   12. let textDecoder = util.TextDecoder.create('utf-8', { ignoreBOM: true });
   13. let str = textDecoder.decodeToString(arr, { stream: false });
   14. return str;
   15. }
   ```

   [query\_auth.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/AssetStoreKit/AssetStoreArkTS/entry/src/main/ets/operations/query_auth.ets#L16-L32)
2. 参考如下示例代码，进行业务功能开发。

   ```
   1. async function userAuthenticate(challenge: Uint8Array): Promise<Uint8Array> {
   2. return new Promise((resolve, reject) => {
   3. const authParam: userAuth.AuthParam = {
   4. challenge: challenge,
   5. authType: [userAuth.UserAuthType.PIN],
   6. authTrustLevel: userAuth.AuthTrustLevel.ATL1,
   7. };
   8. const widgetParam: userAuth.WidgetParam = { title: '请输入锁屏密码' };
   9. try {
   10. let userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
   11. userAuthInstance.on('result', {
   12. onResult(result) {
   13. if (result.result == userAuth.UserAuthResultCode.SUCCESS) {
   14. console.info(`User identity authentication succeeded.`);
   15. resolve(result.token);
   16. } else {
   17. console.error(`User identity authentication failed.`);
   18. reject();
   19. }
   20. }
   21. });
   22. userAuthInstance.start();
   23. } catch (error) {
   24. let err = error as BusinessError;
   25. console.error(`User identity authentication failed. Code is ${err.code}, message is ${err.message}`);
   26. reject();
   27. }
   28. })
   29. }

   31. function preQueryAsset(): Promise<Uint8Array> {
   32. return new Promise((resolve, reject) => {
   33. try {
   34. let query: asset.AssetMap = new Map();
   35. query.set(asset.Tag.ALIAS, stringToArray('user_auth_asset'));
   36. asset.preQuery(query).then((challenge: Uint8Array) => {
   37. resolve(challenge);
   38. }).catch(() => {
   39. reject();
   40. })
   41. } catch (error) {
   42. let err = error as BusinessError;
   43. console.error(`Failed to pre-query Asset. Code is ${err.code}, message is ${err.message}`);
   44. reject();
   45. }
   46. });
   47. }

   49. async function postQueryAsset(challenge: Uint8Array) {
   50. let handle: asset.AssetMap = new Map();
   51. handle.set(asset.Tag.AUTH_CHALLENGE, challenge);
   52. try {
   53. await asset.postQuery(handle);
   54. console.info(`Succeeded in post-querying Asset.`);
   55. } catch (error) {
   56. let err = error as BusinessError;
   57. console.error(`Failed to post-query Asset. Code is ${err.code}, message is ${err.message}`);
   58. }
   59. }

   61. export async function queryUserAuthAsset(): Promise<string> {
   62. let result: string = '';
   63. // step1. 调用asset.preQuery获取挑战值。
   64. await preQueryAsset().then(async (challenge: Uint8Array) => {
   65. try {
   66. // step2. 传入挑战值，拉起用户认证框。
   67. let authToken: Uint8Array = await userAuthenticate(challenge);
   68. // step3 用户认证通过后，传入挑战值和授权令牌，查询关键资产明文。
   69. let query: asset.AssetMap = new Map();
   70. query.set(asset.Tag.ALIAS, stringToArray('user_auth_asset'));
   71. query.set(asset.Tag.RETURN_TYPE, asset.ReturnType.ALL);
   72. query.set(asset.Tag.AUTH_CHALLENGE, challenge);
   73. query.set(asset.Tag.AUTH_TOKEN, authToken);
   74. let res: asset.AssetMap[] = await asset.query(query);
   75. for (let i = 0; i < res.length; i++) {
   76. // 解析secret。
   77. let secret: Uint8Array = res[i].get(asset.Tag.SECRET) as Uint8Array;
   78. // 将Uint8Array转换为string类型。
   79. let secretStr: string = arrayToString(secret);
   80. }
   81. // step4. 关键资产明文查询成功后，需要调用asset.postQuery进行查询的后置处理。
   82. postQueryAsset(challenge);
   83. result = 'Succeeded in querying user-auth Asset';
   84. } catch (error) {
   85. // step5. preQuery成功，后续操作失败，也需要调用asset.postQuery进行查询的后置处理。
   86. postQueryAsset(challenge);
   87. result = 'Failed to query user-auth Asset';
   88. }
   89. }).catch((err: BusinessError) => {
   90. console.error(`Failed to pre-query Asset. Code is ${err.code}, message is ${err.message}`);
   91. result = 'Failed to query user-auth Asset';
   92. })
   93. return result;
   94. }
   ```

   [query\_auth.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/AssetStoreKit/AssetStoreArkTS/entry/src/main/ets/operations/query_auth.ets#L34-L129)
