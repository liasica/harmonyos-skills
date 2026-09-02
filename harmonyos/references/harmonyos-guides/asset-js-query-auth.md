---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/asset-js-query-auth
title: 查询需要用户认证的关键资产(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Asset Store Kit（关键资产存储服务） > Asset Store Kit开发指导(ArkTS) > 查询需要用户认证的关键资产(ArkTS)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:27+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:8d561e38e8133a87ddb8122dcf9c97ce3d2126f653862ff4156d7b0d0217cd44
---

## 接口介绍

可通过API文档查看此功能的相关接口：

| 异步接口 | 同步接口 | 说明 |
| --- | --- | --- |
| [preQuery(query: AssetMap)](../harmonyos-references/js-apis-asset.md#assetprequery) | [preQuerySync(query: AssetMap)](../harmonyos-references/js-apis-asset.md#assetprequerysync12) | 查询预处理。 |
| [query(query: AssetMap)](../harmonyos-references/js-apis-asset.md#assetquery) | [querySync(query: AssetMap)](../harmonyos-references/js-apis-asset.md#assetquerysync12) | 查询关键资产。 |
| [postQuery(handle: AssetMap)](../harmonyos-references/js-apis-asset.md#assetpostquery) | [postQuerySync(handle: AssetMap)](../harmonyos-references/js-apis-asset.md#assetpostquerysync12) | 查询后置处理。 |

查询需要用户认证的关键资产时，关键资产属性的内容（AssetMap）参数如下表所示：

**注意** 

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
  | DATA\_LABEL\_CRITICAL\_1 | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且有完整性保护。  **说明：** 在API version 12及之前版本，长度为1-512字节。 |
  | DATA\_LABEL\_CRITICAL\_2 | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且有完整性保护。  **说明：** 在API version 12及之前版本，长度为1-512字节。 |
  | DATA\_LABEL\_CRITICAL\_3 | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且有完整性保护。  **说明：** 在API version 12及之前版本，长度为1-512字节。 |
  | DATA\_LABEL\_CRITICAL\_4 | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且有完整性保护。  **说明：** 在API version 12及之前版本，长度为1-512字节。 |
  | DATA\_LABEL\_NORMAL\_1 | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且无完整性保护。  **说明：** 在API version 12及之前版本，长度为1-512字节。 |
  | DATA\_LABEL\_NORMAL\_2 | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且无完整性保护。  **说明：** 在API version 12及之前版本，长度为1-512字节。 |
  | DATA\_LABEL\_NORMAL\_3 | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且无完整性保护。  **说明：** 在API version 12及之前版本，长度为1-512字节。 |
  | DATA\_LABEL\_NORMAL\_4 | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且无完整性保护。  **说明：** 在API version 12及之前版本，长度为1-512字节。 |
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
  | DATA\_LABEL\_CRITICAL\_1 | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且有完整性保护。  **说明：** 在API version 12及之前版本，长度为1-512字节。 |
  | DATA\_LABEL\_CRITICAL\_2 | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且有完整性保护。  **说明：** 在API version 12及之前版本，长度为1-512字节。 |
  | DATA\_LABEL\_CRITICAL\_3 | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且有完整性保护。  **说明：** 在API version 12及之前版本，长度为1-512字节。 |
  | DATA\_LABEL\_CRITICAL\_4 | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且有完整性保护。  **说明：** 在API version 12及之前版本，长度为1-512字节。 |
  | DATA\_LABEL\_NORMAL\_1 | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且无完整性保护。  **说明：** 在API version 12及之前版本，长度为1-512字节。 |
  | DATA\_LABEL\_NORMAL\_2 | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且无完整性保护。  **说明：** 在API version 12及之前版本，长度为1-512字节。 |
  | DATA\_LABEL\_NORMAL\_3 | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且无完整性保护。  **说明：** 在API version 12及之前版本，长度为1-512字节。 |
  | DATA\_LABEL\_NORMAL\_4 | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且无完整性保护。  **说明：** 在API version 12及之前版本，长度为1-512字节。 |
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

**说明** 

本模块提供了异步和同步两套接口，以下为异步接口的使用示例，同步接口详见[@ohos.security.asset (关键资产存储服务)](../harmonyos-references/js-apis-asset.md)。

在查询前，需确保已有需要用户认证的关键资产，可参考[指南文档](asset-js-add.md)新增关键资产，否则将抛出NOT\_FOUND错误（错误码24000002）。

查询别名是demo\_alias且需要用户认证的关键资产。示例中引入的@ohos.userIAM.userAuth用法详见userAuth文档中的[start](../harmonyos-references/js-apis-useriam-userauth.md#start10)接口。

1. 引用头文件，定义工具函数。

   ```typescript
   import { asset } from '@kit.AssetStoreKit';
   import { util } from '@kit.ArkTS';
   import { userAuth } from '@kit.UserAuthenticationKit';
   import { BusinessError } from '@kit.BasicServicesKit';

   function stringToArray(str: string): Uint8Array {
     let textEncoder = new util.TextEncoder();
     return textEncoder.encodeInto(str);
   }

   function arrayToString(arr: Uint8Array): string {
     let textDecoder = util.TextDecoder.create('utf-8', { ignoreBOM: true });
     let str = textDecoder.decodeToString(arr, { stream: false });
     return str;
   }
   ```
2. 参考如下示例代码，进行业务功能开发。

   ```typescript
   async function userAuthenticate(challenge: Uint8Array): Promise<Uint8Array> {
     return new Promise((resolve, reject) => {
       const authParam: userAuth.AuthParam = {
         challenge: challenge,
         authType: [userAuth.UserAuthType.PIN],
         authTrustLevel: userAuth.AuthTrustLevel.ATL1,
       };
       const widgetParam: userAuth.WidgetParam = { title: '请输入锁屏密码' };
       try {
         let userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
         userAuthInstance.on('result', {
           onResult(result) {
             if (result.result == userAuth.UserAuthResultCode.SUCCESS) {
               console.info(`User identity authentication succeeded.`);
               resolve(result.token);
             } else {
               console.error(`User identity authentication failed.`);
               reject();
             }
           }
         });
         userAuthInstance.start();
       } catch (error) {
         let err = error as BusinessError;
         console.error(`User identity authentication failed. Code is ${err.code}, message is ${err.message}`);
         reject();
       }
     })
   }

   function preQueryAsset(): Promise<Uint8Array> {
     return new Promise((resolve, reject) => {
       try {
         let query: asset.AssetMap = new Map();
         query.set(asset.Tag.ALIAS, stringToArray('user_auth_asset'));
         asset.preQuery(query).then((challenge: Uint8Array) => {
           resolve(challenge);
         }).catch(() => {
           reject();
         })
       } catch (error) {
         let err = error as BusinessError;
         console.error(`Failed to pre-query Asset. Code is ${err.code}, message is ${err.message}`);
         reject();
       }
     });
   }

   async function postQueryAsset(challenge: Uint8Array) {
     let handle: asset.AssetMap = new Map();
     handle.set(asset.Tag.AUTH_CHALLENGE, challenge);
     try {
       await asset.postQuery(handle);
       console.info(`Succeeded in post-querying Asset.`);
     } catch (error) {
       let err = error as BusinessError;
       console.error(`Failed to post-query Asset. Code is ${err.code}, message is ${err.message}`);
     }
   }

   export async function queryUserAuthAsset(): Promise<string> {
     let result: string = '';
     // step1. 调用asset.preQuery获取挑战值。
     await preQueryAsset().then(async (challenge: Uint8Array) => {
       try {
         // step2. 传入挑战值，拉起用户认证框。
         let authToken: Uint8Array = await userAuthenticate(challenge);
         // step3 用户认证通过后，传入挑战值和授权令牌，查询关键资产明文。
         let query: asset.AssetMap = new Map();
         query.set(asset.Tag.ALIAS, stringToArray('user_auth_asset'));
         query.set(asset.Tag.RETURN_TYPE, asset.ReturnType.ALL);
         query.set(asset.Tag.AUTH_CHALLENGE, challenge);
         query.set(asset.Tag.AUTH_TOKEN, authToken);
         let res: asset.AssetMap[] = await asset.query(query);
         for (let i = 0; i < res.length; i++) {
           // 解析secret。
           let secret: Uint8Array = res[i].get(asset.Tag.SECRET) as Uint8Array;
           // 将Uint8Array转换为string类型。
           let secretStr: string = arrayToString(secret);
         }
         // step4. 关键资产明文查询成功后，需要调用asset.postQuery进行查询的后置处理。
         postQueryAsset(challenge);
         result = 'Succeeded in querying user-auth Asset';
       } catch (error) {
         // step5. preQuery成功，后续操作失败，也需要调用asset.postQuery进行查询的后置处理。
         postQueryAsset(challenge);
         result = 'Failed to query user-auth Asset';
       }
     }).catch((err: BusinessError) => {
       console.error(`Failed to pre-query Asset. Code is ${err.code}, message is ${err.message}`);
       result = 'Failed to query user-auth Asset';
     })
     return result;
   }
   ```
