---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/onlineauthentication-did
title: DID数字身份
breadcrumb: 指南 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > DID数字身份
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:31+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f2e1ae819240679c7b5322706e370aebc861c5d4a18ac8d9cd97759aa279526c
---

从API版本26.0.0开始，Online Authentication Kit（在线认证服务）新增数字身份特性，提供了基于DID（Decentralized Identifier，去中心化身份）协议的数字身份在移动端的能力。应用部署符合DID协议的服务器之后，结合移动端的数字身份能力，可实现跨平台互通互认的数字身份业务场景。数字身份服务主要提供了以下能力：

* DID密钥创建及使用：应用为用户创建DID时，支持应用创建及使用与用户DID关联的密钥。
* DID导入、查询及删除：应用为用户创建DID时，支持应用导入DID标识、DID文档等信息到设备中。
* 可验证凭证VC（Verifiable Credentials，可验证凭证）导入、查询及删除：应用为用户颁发数字身份凭证（即VC）时，支持应用导入VC到设备TEE环境中安全存储，保障用户隐私，并支持查询、删除VC。
* 可验证声明VP（Verifiable Presentation，可验证声明）出示：应用需要请求用户的数字身份凭证VP时，数字身份服务在获取用户同意后，会在TEE中将VC中需要披露的属性组装成VP返回给应用。支持用户生物认证授权出示凭证、凭证的部分披露，保障用户身份凭证的安全与隐私。

## 场景介绍

针对传统身份凭证验证方式（如上传证件照片）存在的体验繁琐、隐私泄露等问题，Online Authentication Kit提供数字身份能力，支持DID分布式数字身份协议，可以支撑业务将数字化身份凭证（例如数字化证件凭证）安全存储于设备终端TEE中，用户可通过生物认证授权安全便捷地使用凭证。在优化用户体验的同时，有效增强用户身份信息的隐私性与安全性。

## 约束与限制

需满足以下条件，才能使用本功能。

* 应用已部署符合DID标准协议的服务器。
* 移动端设备需要支持生物特征（指纹/3D人脸），查询当前移动端设备是否支持ATL4级别的认证可信等级。

  ```typescript
  import { BusinessError } from '@kit.BasicServicesKit';
  import { userAuth } from '@kit.UserAuthenticationKit';

  try {
    // 示例，查询设备人脸识别是否支持ATL4级别的认证可信等级
    userAuth.getAvailableStatus(userAuth.UserAuthType.FACE, userAuth.AuthTrustLevel.ATL4);
    console.info('current auth trust level is supported');
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    console.error(`current auth trust level is not supported. Code is ${err?.code}, message is ${err?.message}`);
  }
  ```
* 数字身份服务会将凭证信息、匿名化的指纹ID和面容ID等个人信息返回至应用，以提供绑定具体生物特征的免密认证能力。应用将个人信息上云前，需要向用户明示并且取得同意，详细请参考[个人数据处理说明](onlineauthentication-personal-data-processing-description.md)。

## 业务流程

### 启用数字身份流程

应用需要为用户创建数字身份时，可以使用数字身份服务创建及使用与用户DID关联的密钥、导入用户DID文档等信息至设备。创建数字身份后，应用可基于用户DID标识为用户颁发凭证，并使用用户DID密钥对数据签名授权。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/Zs_DAjehTzqj2P0pRcCV6w/zh-cn_image_0000002706674380.png)

流程说明：

1. 应用云侧下发指定密钥别名信息等参数。
2. 应用构造[GenerateKeyRequest](../harmonyos-references/onlineauthentication-did-api.md#generatekeyrequest)，指定密钥别名、算法类型、用途等参数，调用[generateKey](../harmonyos-references/onlineauthentication-did-api.md#didgeneratekey)接口生成DID密钥。
3. DID API返回公钥、证书链等信息。
4. 应用将公钥等信息上报至应用云侧，由应用云侧完成公钥上链等操作，并获取DID文档等信息。
5. 应用调用[importDid](../harmonyos-references/onlineauthentication-did-api.md#didimportdid)接口将DID文档等信息导入。

### 颁发数字凭证流程

应用为用户颁发数字身份凭证（例如教师凭证等），可以使用数字身份服务将数字身份凭证导入至设备安全存储，用于后续便携出示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/7BKPCmTaTri-t5r1mJlw9A/zh-cn_image_0000002736433469.png)

流程说明：

1. 应用从发行方获取加密（也可不加密）的可验证凭证。
2. 构造[ImportDigitalCredentialRequest](../harmonyos-references/onlineauthentication-did-api.md#importdigitalcredentialrequest)，配置解密参数、显示配置等，调用[importDigitalCredential](../harmonyos-references/onlineauthentication-did-api.md#didimportdigitalcredential)接口导入凭证。
3. DID API验证凭证格式并安全存储，返回调用结果，凭证概要信息。

### 出示数字凭证流程

应用作为验证方，需要请求用户的数字身份凭证用于验证用户身份或者发放相应权益时，可以使用数字身份服务请求获取用户凭证，用户确认出示的凭证及披露的属性字段后，数字身份服务会将凭证出示到验证方应用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/Nhk0aokZSbSOqmHhMEGCgw/zh-cn_image_0000002706834314.png)

流程说明：

1. 应用云侧下发请求凭证的参数。
2. 应用构造[GetDigitalCredentialRequest](../harmonyos-references/onlineauthentication-did-api.md#getdigitalcredentialrequest)，指定凭证类型、验证方信息等，调用[getDigitalCredential](../harmonyos-references/onlineauthentication-did-api.md#didgetdigitalcredential)接口获取凭证。
3. DID API返回可验证表达（VP）给应用。

## 接口说明

业务使用DID能力进行数字身份的启用、数字凭证的导入、数字凭证的出示等。具体API说明详见[接口文档](../harmonyos-references/onlineauthentication-did-api.md#didgeneratekey)。

| 接口名称 | 描述 |
| --- | --- |
| [generateKey](../harmonyos-references/onlineauthentication-did-api.md#didgeneratekey)(context: [common.Context](../harmonyos-references/js-apis-inner-application-context.md#context), generateKeyRequest: [GenerateKeyRequest](../harmonyos-references/onlineauthentication-did-api.md#generatekeyrequest)): Promise<[GenerateKeyResponse](../harmonyos-references/onlineauthentication-did-api.md#generatekeyresponse)> | 生成DID密钥。使用Promise异步回调。 |
| [importDid](../harmonyos-references/onlineauthentication-did-api.md#didimportdid)(context: common.Context, importDidRequest: [ImportDidRequest](../harmonyos-references/onlineauthentication-did-api.md#importdidrequest)): Promise<void> | 导入DID信息。使用Promise异步回调。 |
| [queryDid](../harmonyos-references/onlineauthentication-did-api.md#didquerydid)(context: common.Context, queryDidRequest: [QueryDidRequest](../harmonyos-references/onlineauthentication-did-api.md#querydidrequest)): Promise<[QueryDidResponse](../harmonyos-references/onlineauthentication-did-api.md#querydidresponse)> | 查询DID信息。使用Promise异步回调。 |
| [deleteDid](../harmonyos-references/onlineauthentication-did-api.md#diddeletedid)(context: common.Context, did: string): Promise<void> | 删除DID。使用Promise异步回调。 |
| [sign](../harmonyos-references/onlineauthentication-did-api.md#didsign)(context: common.Context, signRequest: [SignRequest](../harmonyos-references/onlineauthentication-did-api.md#signrequest)): Promise<[SignResponse](../harmonyos-references/onlineauthentication-did-api.md#signresponse)> | 数据签名。使用Promise异步回调。 |
| [importDigitalCredential](../harmonyos-references/onlineauthentication-did-api.md#didimportdigitalcredential)(context: common.Context, importDigitalCredentialRequest: [ImportDigitalCredentialRequest](../harmonyos-references/onlineauthentication-did-api.md#importdigitalcredentialrequest)): Promise<[ImportDigitalCredentialResponse](../harmonyos-references/onlineauthentication-did-api.md#importdigitalcredentialresponse)> | 导入数字凭证。使用Promise异步回调。 |
| [queryDigitalCredential](../harmonyos-references/onlineauthentication-did-api.md#didquerydigitalcredential)(context: common.Context, did?: string, credentialId?: string): Promise<[QueryDigitalCredentialResponse](../harmonyos-references/onlineauthentication-did-api.md#querydigitalcredentialresponse)> | 查询数字凭证。使用Promise异步回调。 |
| [deleteDigitalCredential](../harmonyos-references/onlineauthentication-did-api.md#diddeletedigitalcredential)(context: common.Context, did?: string, credentialId?: string): Promise<void> | 删除数字凭证。使用Promise异步回调。 |
| [getDigitalCredential](../harmonyos-references/onlineauthentication-did-api.md#didgetdigitalcredential)(context: common.Context, getDigitalCredentialRequest: [GetDigitalCredentialRequest](../harmonyos-references/onlineauthentication-did-api.md#getdigitalcredentialrequest)): Promise<[GetDigitalCredentialResponse](../harmonyos-references/onlineauthentication-did-api.md#getdigitalcredentialresponse)> | 获取数字凭证。使用Promise异步回调。 |

## 开发准备

* 开发者需要部署符合W3C DID协议的服务器。
* 开发者基于数字身份服务开发时，需要申请如下通行密钥服务权限。在申请权限前，请保证符合[权限使用的基本原则](app-permission-mgmt-overview.md#权限使用的基本原则)。申请方式请参考：[申请受限权限](declare-permissions-in-acl.md)。

  | 应用能力 | 需要权限 |
  | --- | --- |
  | 数字身份 | ohos.permission.ACCESS\_FIDO2\_ONLINEAUTH |

## 开发步骤

### 启用数字身份

1. 导入DID模块，构造密钥生成请求。

   ```typescript
   import { did } from '@kit.OnlineAuthenticationKit';
   import { buffer } from '@kit.ArkTS';
   import { common } from '@kit.AbilityKit';
   import { BusinessError } from '@kit.BasicServicesKit'; // 这些导入did等相关模块的函数放在文件最开头，后续的示例代码不再一一展示写出

   // 以下获取context的代码要放进UI组件类中调用，通用的获取方法，后续的示例代码不再一一展示写出
   let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

   async function generateKey() {
     // 构造密钥生成请求
     let generateKeyRequest: did.GenerateKeyRequest = {
       keyAlias: 'myDidKey',
       keyConfig: {
         algorithm: did.KeyAlgo.SM2,
         purposeList: [did.KeyPurpose.SIGN, did.KeyPurpose.VERIFY]
       },
       authenticatorConfig: {
         authTypeList: [did.AuthType.UVM_FINGERPRINT],
         requireBioId: true
       }
     };

     try {
       let response: did.GenerateKeyResponse = await did.generateKey(context, generateKeyRequest);
       console.info('Succeeded in generating did key, Public Key:', response.publicKey,
         'Certificate Chain:', response.certChain);
       // 处理返回的公钥、证书链等信息
     } catch (error) {
       const err: BusinessError = error as BusinessError;
       console.error(`Failed to generate did key. Code: ${err.code}, message: ${err.message}`);
     }
   }
   ```
2. 构造DID导入请求，调用importDid接口，将DID文档等信息导入设备。

   ```typescript
   async function importDid() {
      let importDidRequest: did.ImportDidRequest = {
         isUpdate: false,
         did: 'did:example:123456',
         didKeyList: [{
            keyAlias: 'myDidKey',
            keyId: 'keyId123'
         }],
         didDoc: JSON.stringify({
            '@context': 'https://www.w3.org/ns/did/v1',
            id: 'did:example:123456',
            // ... 其他DID文档内容
         })
      };

      try {
         await did.importDid(context, importDidRequest);
         console.info('Succeeded in importing did');
      } catch (error) {
         const err: BusinessError = error as BusinessError;
         console.error(`Failed to import did. Code: ${err.code}, message: ${err.message}`);
      }
   }
   ```
3. 构造查询请求，调用queryDid接口，查询DID有没有导入成功。

   ```typescript
   async function queryDid() {
      let queryDidRequest: did.QueryDidRequest = {
         did: 'did:example:123456',
         queryDidConfig: {
            requireDidKey: true,
            requireDidDoc: true,
            requireAdditionalData: true
         }
      };

      try {
         let response: did.QueryDidResponse = await did.queryDid(context, queryDidRequest);
         console.info('Succeeded in querying did, Did Key List:', response.didKeyList,
            'Did Doc:', response.didDoc);
         // 处理返回的DID密钥、DID文档等信息
      } catch (error) {
         const err: BusinessError = error as BusinessError;
         console.error(`Failed to query did. Code: ${err.code}, message: ${err.message}`);
      }
   }
   ```
4. 如果已存在相关DID以及DID密钥，调用sign接口可以为待签名数字签名。

   ```typescript
   async function sign() {
      let data: string = 'data to sign';
      let signRequest: did.SignRequest = {
         inData: new Uint8Array(buffer.from(data).buffer),
         keyId: 'keyId123'
      };

      try {
         let response: did.SignResponse = await did.sign(context, signRequest);
         console.info('Succeeded in signing data, Signed Data:', response.outData);
         // 处理签名结果
      } catch (error) {
         const err: BusinessError = error as BusinessError;
         console.error(`Failed to sign data. Code: ${err.code}, message: ${err.message}`);
      }
   }
   ```
5. 调用deleteDid删除对应的DID信息。

   ```typescript
   async function deleteDid() {
      try {
         await did.deleteDid(context, 'did:example:123456');
         console.info('Succeeded in deleting did');
      } catch (error) {
         const err: BusinessError = error as BusinessError;
         console.error(`Failed to delete did. Code: ${err.code}, message: ${err.message}`);
      }
   }
   ```

### 颁发数字凭证

1. 构造凭证导入请求，配置安全参数和显示参数。

   ```typescript
   async function importDigitalCredential() {
      let importCredentialRequest: did.ImportDigitalCredentialRequest = {
         did: 'did:example:123456',
         credentialType: did.CredentialType.VC,
         isUpdate: false,
         credentialData: JSON.stringify({
            '@context': ['https://www.w3.org/2018/credentials/v1'],
            type: ['VerifiableCredential'],
            issuer: 'did:example:issuer',
            issuanceDate: '2024-01-01T00:00:00Z',
            credentialSubject: Object, // ... 凭证主题内容
            proof: Object, // ... 签名信息
         }),
         displayConfig: {
            credentialDisplayName: '身份证',
            issuerDisplayName: '公安部门',
            propertyDisplayName: '姓名'
         },
         securityConfig: {
            authConfig: {
               requireAuth: true
            }
         }
      };

      try {
         let response: did.ImportDigitalCredentialResponse =
            await did.importDigitalCredential(context, importCredentialRequest);
         console.info('Succeeded in importing digital credential, Credential Summary:',
            response.credentialSummary);
      } catch (error) {
         const err: BusinessError = error as BusinessError;
         console.error(`Failed to import digital credential. Code: ${err.code}, message: ${err.message}`);
      }
   }
   ```

   注意，数字身份服务仅支持解析以下两种格式的VC，请根据以下格式组装VC。

   ```typescript
   // VC格式1
   // 注：仅支持解析以下列出字段，若多传不可识别的字段，默认不解析，但是会正常存储，也会作为VC的一部分组装进后续的VP中。不同的VC格式会走向不同的默克尔根计算方式，请根据实际需要选择。
   {
      "@context": [
          "https://www.w3.org/2018/credentials/v1"
      ],
      "id": "vc.XXXXXXXX", // 表示VC的标识
      "types": [
          "XXXXXXXX"
      ], // 凭证类型，例如教师凭证类型
      "type": [
          "VerifiableCredential",
          "SelectiveDisclosureVC"
      ],  // VC的类型
      "credentialSubject": {
          "property1": "XXXXXXXX",
          "property2": "XXXXXXXX",
          ...
      }, // 凭证的属性字段
      "issuer": "did:XXXXXXXX", // 颁发方的did
      "issuanceDate": "2025-02-25T12:23:43Z", // 颁发时间
      "expirationDate": "2031-02-08T13:06:40Z",// 失效时间
      "auxVerificationInfo": { // 用于计算默克尔根的信息
          "type": "MerkleTree",
          "salt": {
              "seed": "XXXXXXXX"
          }
      },
      "proof": { // VC的签名
          "type": "SM3WithSM2",
          "created": "2025-02-25T12:23:43Z",
          "verificationMethod": "did:XXXXXXXX#key-X",
          "proofPurpose": "assertionMethod",
          "proofValue": "XXXXXXXX"
      }
   }

   // VC格式2
   // 注：仅支持解析以下列出字段，若多传不可识别的字段，默认不解析，但是会正常存储，也会作为VC的一部分组装进后续的VP中。不同的VC格式会走向不同的默克尔根计算方式，请根据实际需要选择。
   {
      "@context": [
          "https://www.w3.org/2018/credentials/v1",
          "https://www.w3.org/2018/credentials/examples/v1"
      ],
      "type": [
          "CredentialType", // 凭证类型
          "SelectiveDisclosureCredentialType" // VC类型
      ],
      "id": "did:credential:XXXXXXXX", // VC的标识ID
      "issuer": "did:XXXXXXXX", // 颁发方的DID
      "issuanceDate": "2024-07-11T13:50:18+08:00", // 颁发时间
      "expirationDate": "2024-07-11T13:50:18+08:00", // 失效时间
      "credentialSubject": {
          "did": "did:XXXXXXXX", // 用户的DID
          "claims": {
              "subject": { // 凭证属性字段
                  "property1": "XXXXXXXX",
                  "property2": "XXXXXXXX",
                  ...
              },
              "seed": "XXXXXXXX" // 用于计算默克尔根
          }
      },
      "proof": { // VC中的签名
          "type": "SM2Signature2024",
          "created": "2024-07-11T13:50:18+08:00",
          "creator": "did:XXXXXXXX",
          "verificationMethod": "did:XXXXXXXX#key-X",
          "proofPurpose": "assertionMethod",
          "proofValue": "XXXXXXXX"
      }
   }
   ```
2. 调用queryDigitalCredential接口查询凭证是否导入成功。

   ```typescript
   async function queryDigitalCredential() {
      try {
         let response: did.QueryDigitalCredentialResponse =
            await did.queryDigitalCredential(context, 'did:example:123456');
         console.info('Succeeded in querying digital credential, Credential Summary List:',
            response.credentialSummaryList);
         // 处理凭证摘要列表
      } catch (error) {
         const err: BusinessError = error as BusinessError;
         console.error(`Failed to query digital credential. Code: ${err.code}, message: ${err.message}`);
      }
   }
   ```
3. 调用deleteDigitalCredential接口删除对应的数字凭证。

   ```typescript
   async function deleteDigitalCredential() {
      try {
         await did.deleteDigitalCredential(context, 'did:example:123456', 'credential123');
         console.info('Succeeded in deleting digital credential');
      } catch (error) {
         const err: BusinessError = error as BusinessError;
         console.error(`Failed to delete digital credential. Code: ${err.code}, message: ${err.message}`);
      }
   }
   ```

### 出示数字凭证

构造凭证获取请求，调用getDigitalCredential接口。

```typescript
async function getDigitalCredential() {
  let getCredentialRequest: did.GetDigitalCredentialRequest = {
      credentialType: did.CredentialType.VP,
      displayConfig: {
        verifierDisplayName: '某应用',
        purpose: '身份验证'
      },
      holderConfigList: [{
        holderDid: 'did:example:123456',
        holderDidKeyId: 'keyId123'
      }],
      credentialFilterList: [{
        credentialId: 'credential123',
        issuerDid: 'did:example:issuer'
      }]
  };

  try {
      let response: did.GetDigitalCredentialResponse =
        await did.getDigitalCredential(context, getCredentialRequest);
      console.info('Succeeded in getting digital credential');
      // 处理返回的凭证数据
  } catch (error) {
      const err: BusinessError = error as BusinessError;
      console.error(`Failed to get digital credential. Code: ${err.code}, message: ${err.message}`);
  }
}
```

注意，数字身份服务仅支持组装以下两种格式的VP，请根据以下格式解析并验证VP。

```typescript
// VP格式1
{
    "id": "vp.XXXXXXXX", // VP的标识
    "type": [ // VP的类型
    "VerifiablePresentation",
    "SelectiveDisclosureVP"
    ],
    "holder": "did:XXXXXXXX", // 用户的DID
    "verifiableCrendential": [
    {
        // VC中选择披露的属性，以及其余所有字段（含VC的proof）
        "@context": [
        "https://www.w3.org/2018/credentials/v1"
        ],
        "id": "vc.XXXXXXXX",
        "types": [
        "XXXXXXXX"
        ],
        // ... 其他字段

        // 用于计算默克尔根的信息
        "auxVerificationInfo": {
        "type": "MerkleTree",
        "salt": {
            "seed": "XXXXXXXX"
        },
        "dataSalt": {
            "property1": "XXXXXXXX",
            "property2": "XXXXXXXX"
        },
        "dataIndex": {
            "property1": [1, 1, 1, 1],
            "property2": [0, 1, 1, 1]
        },
        "merkleSibling": {
            "property1": [
            "XXXXXXXX",
            "XXXXXXXX",
            "XXXXXXXX",
            "XXXXXXXX"
            ],
            "property2": [
            "XXXXXXXX",
            "XXXXXXXX",
            "XXXXXXXX",
            "XXXXXXXX"
            ]
        }
        }
    }
    ],
    "proof": { // VP的签名
    "type": "SM3WithSM2",
    "created": "2026-07-21T09:35:34+08:00",
    "verificationMethod": "did:XXXXXXXX", // 用户的DID
    "proofPurpose": "assertionMethod",
    "proofValue": "XXXXXXXX"
    }
}

// VP格式2
{
    "@context": [
    "https://www.w3.org/2018/credentials/v1",
    "https://www.w3.org/2018/credentials/examples/v1"
    ],
    "created": "2026-07-21T09:37:20+08:00", // 创建时间
    "domain": "did:testVerifierDid", // 验证方的DID
    "type": [ // VP的DID
    "VerifiablePresentation"
    ],
    "proof": {
    // VP的签名
    "created": "2026-07-21T09:37:20+08:00",
    "creator": "testDid",
    "proofPurpose": "assertionMethod",
    "type": "SM2Signature2024",
    "verificationMethod": "did:testDidKeyId",
    "proofValue": "XXXXXXXX"
    },
    "verifiableCredential": [
    {
        // VC中选择披露的属性，以及其余所有字段
        "@context": [
        "https://www.w3.org/2018/credentials/v1",
        "https://www.w3.org/2018/credentials/examples/v1"
        ],
        "type": [
        "DisableCredentialType",
        "SelectiveDisclosureCredentialType"
        ],
        
        ...

        "credentialSubject": {
        "did": "did:XXXXXXXX",
        "claims": {
            "disclosedSalt": {
            // 用于默克尔根的计算
            "property1": "XXXXXXXX",
            "property2": "XXXXXXXX"
            // ...
            },
            "subject": {
            "property1": "XXXXXXXX",
            "property2": "XXXXXXXX"
            // ...
            }
        }
        }
    }
    ]
}
```
