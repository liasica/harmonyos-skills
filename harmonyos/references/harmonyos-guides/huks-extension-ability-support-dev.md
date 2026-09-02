---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-extension-ability-support-dev
title: CryptoExtensionAbility适配开发指导
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 外部密钥管理扩展 > 驱动HAP ExtensionAbility适配指导 > CryptoExtensionAbility适配开发指导
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:33+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:431228f73387c27fd57dee015ad33a00ab4fe9d124ef2234d976e1966fa89562
---

## 约束限制

针对CryptoExtensionAbility接口调用限制，详细请参考API中的[约束限制](../harmonyos-references/js-apis-cryptoextensionability.md#约束限制)。

## 适配指导

本文档旨在指导驱动厂商如何继承实现[CryptoExtensionAbility](../harmonyos-references/js-apis-cryptoextensionability.md)需要的接口能力，此处给出实现参考，其他实现依照业务需要依次调用driver封装的底层驱动函数。

在DevEco Studio工程中手动新建一个CryptoExtensionAbility组件，具体步骤如下：

1. 在工程Module对应的ets目录下，右键选择“New > Directory”，新建一个目录，名称可以自己定义，例如cryptoability。
2. 在cryptoability目录，右键选择“New > ArkTS File”，新建一个文件，名称可以自己定义，例如CryptoAbility.ets。

   其目录结构如下所示：

   ```txt
   ├── ets
   │   └── cryptoability
   │       └── CryptoAbility.ets
   ```
3. 开发CryptoExtensionAbility需要配置[ohos.permission.CRYPTO\_EXTENSION\_REGISTER](restricted-permissions.md#ohospermissioncrypto_extension_register)权限，该权限属于[受限开放权限](restricted-permissions.md)，请按照[申请受限权限](declare-permissions-in-acl.md)指引为应用进行申请。

   ```json5
   // entry/src/main/module.json5
   {
     "module": {
       // ...
       "requestPermissions": [
         {
           "name": "ohos.permission.CRYPTO_EXTENSION_REGISTER"
         }
       ],
     }
   }
   ```
4. 在工程Module对应的module.json5配置文件中注册AppServiceExtensionAbility组件，name标签表示ability名称，长度最大为127字节，srcEntry标签表示当前CryptoExtensionAbility组件所对应的代码路径，type标签需要设置为“crypto”，exported标签设置为false表示不允许三方应用调用，配置多个ability时要求每个name标签必须是唯一的。

   ```json5
   // entry/src/main/module.json5
   {
     "module": {
       // ...
       "extensionAbilities": [
           {
             "name": "CryptoExtension",
             "srcEntry": "./ets/cryptoability/CryptoAbility.ets",
             "type": "crypto",
             "exported": false
           }
       ],
     }
   }
   ```
5. 在CryptoAbility.ets文件中，增加导入CryptoExtensionAbility的依赖包，自定义类继承CryptoExtensionAbility组件并实现其中的接口函数。导入CryptoExtensionAbility需要实现在[CryptoExtensionAbility](../harmonyos-references/js-apis-cryptoextensionability.md)中给出的所有函数，此处给出实现参考，与底层驱动的调用对应关系见下文。

   **注意** 

   1. 句柄资源和PIN认证状态需要做基于UID的隔离，在onOpenResource、onCloseResource、onAuthUkeyPin、onGetUkeyPinAuthState和onClearUkeyPinAuthState接口的入参params中会包含业务的UID信息（通过[HUKS\_EXT\_CRYPTO\_TAG\_UID](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptotag)可获取业务身份），可基于此做句柄资源和PIN认证状态的隔离。
   2. 接口函数的错误不支持自定义返回，不按接口定义方式返回会导致异常。

   ```ts
   import { huks, huksExternalCrypto, CryptoExtensionAbility, HuksCryptoExtensionCertInfo, HuksCryptoExtensionResult } from '@kit.UniversalKeystoreKit';
   import { util } from '@kit.ArkTS';
   import { cryptoFramework } from '@kit.CryptoArchitectureKit';
   import { deviceInfo } from '@kit.BasicServicesKit';

   export class CryptoExtension extends CryptoExtensionAbility {
     // 本步骤内的接口函数实现均需在class内，为方便开发者理解及使用，每个接口函数在下文详细解释。
   }
   ```

   **接口介绍：**

   （1）onOpenResource在UKey签名验签操作中用于打开指定资源（如建立会话或连接）。resourceId表示要打开的资源标识，应用身份可以在params中由[HUKS\_EXT\_CRYPTO\_TAG\_UID](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptotag)参数携带。当调用成功时，返回值中的resultCode成员设置为0，handle成员非空；调用失败时，resultCode携带错误码信息。

   ```ts
   onOpenResource(resourceId: string, params: Array<huksExternalCrypto.HuksExternalCryptoParam>): Promise<HuksCryptoExtensionResult> {
     // 构造结果对象，默认返回操作失败，返回值为HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL
     let result: HuksCryptoExtensionResult = {
       resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
     };

     // 获取 appId
     let appId: string | undefined = params.find((param =>
       param.tag === huksExternalCrypto.HuksExternalCryptoTag.HUKS_EXT_CRYPTO_TAG_UID))?.value.toString();
     if (appId === undefined) {
       return Promise.resolve(result);
     }

     // 解析 resource index，API版本不同解析方式也不同。
     let index: string;
     const apiVersion = deviceInfo.sdkApiVersion;
     if (apiVersion >= 26) {
       index = resourceId;
     } else {
       index = JSON.parse(resourceId)['index'];
     }

     // ...
     let res: HuksCryptoExtensionResult = {
       resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
     }
     try {
       let driver: YourUKeyDriver = YourDriverInstance;
       res = driver.YourDriver_onOpenResource(index, ...);
       // 场景：打开资源成功
       result.resultCode = res.resultCode
       result.handle = res.handle
     } catch (error) {
       // 场景：打开资源失败
       result.resultCode = res.resultCode
       console.error('promise: onOpenResource failed.');
     }
     return Promise.resolve(result);
   }
   ```

   （2）onCloseResource在UKey签名验签操作中用于关闭指定资源（如释放会话或连接）。handle为待关闭资源的句柄，应用身份可以在params中由[HUKS\_EXT\_CRYPTO\_TAG\_UID](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptotag)参数携带。当调用成功时，返回值中的resultCode成员设置为0；调用失败时，resultCode携带错误码信息。

   ```ts
   onCloseResource(handle: string, params: Array<huksExternalCrypto.HuksExternalCryptoParam>): Promise<HuksCryptoExtensionResult> {
     // ...
     let result: HuksCryptoExtensionResult = {
       resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
     };
     
     let res: HuksCryptoExtensionResult = {
       resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
     }
     try {
       let driver: YourUKeyDriver = YourDriverInstance;
       res = driver.YourDriver_closeOpenResource(handle, ...);
       // 场景：关闭资源成功
       result.resultCode = res.resultCode
     } catch (error) {
       // 场景：关闭资源失败
       result.resultCode = res.resultCode
       console.error('promise: onCloseResource failed.');
     }
     return Promise.resolve(result);
   }
   ```

   （3）onGetProperty在UKey签名验签操作中用于获取指定资源的属性信息。handle为资源句柄，propertyId为待获取的属性标识，应用身份可以在params中由[HUKS\_EXT\_CRYPTO\_TAG\_UID](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptotag)参数携带。当调用成功时，返回值中的resultCode成员设置为0，返回值中的property成员包含属性信息。调用失败时，resultCode携带错误码信息。

   在onGetProperty中须实现导出公钥功能，以便上游业务使用PIN加密传输并完成PIN码认证。加密算法支持RSA、SM2等。当入参propertyId为SKF\_ExportPublicKey时，返回的公钥信息采用JSON格式，包含以下4个必选字段，分别是publicKey（公钥数据）、algo（算法类型及密钥长度）、transformation（密码学操作参数，如填充模式）、size（公钥数据长度）。具体实现可参考下方示例代码中onGetProperty接口的相关部分。

   ```ts
   onGetProperty(handle: string, propertyId: string, params: Array<huksExternalCrypto.HuksExternalCryptoParam>): Promise<HuksCryptoExtensionResult> {
     // ...
     let emptyArray: Array<huksExternalCrypto.HuksExternalCryptoParam> = [];
     let result: HuksCryptoExtensionResult = {
       resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
       property: emptyArray
     };

     // 导出公钥
     if (propertyId == 'SKF_ExportPublicKey') {
       result.resultCode = 0
       let encryptionAlgo: string = 'RSA1024'
       let padding: string = 'PRIMES_2';
       // 1. 创建一个AsyKeyGenerator实例。
       let rsaGenerator = cryptoFramework.createAsyKeyGenerator(`${encryptionAlgo}|${padding}`);
       // 2. 使用密钥生成器随机生成非对称密钥对。
       let keyPair = rsaGenerator.generateKeyPairSync();
       // 3. 将公钥导出，并转换为Json字符串
       const pkData = Array.from(keyPair.pubKey.getEncoded().data);
       let transformation: string = 'RSA1024|PKCS1'
       const encoder = new util.TextEncoder();
       let info = encoder.encodeInto(JSON.stringify({
         publicKey: pkData,
         algo: encryptionAlgo,
         transformation: transformation,
         size: pkData.length
       }));
       // 4. 保存私钥，后续用于解密加密的数据
       let privKey = keyPair.priKey
       // 返回用来加密传pin的公钥和加密算法信息，详见导出公钥文档
       result.property = [
         { tag: huksExternalCrypto.HuksExternalCryptoTag.HUKS_EXT_CRYPTO_TAG_EXTRA_DATA, value: info }
       ]
       return Promise.resolve(result);
     }

     let res: HuksCryptoExtensionResult = {
       resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
     }
     try {
       // 场景：获取属性成功
       let driver: YourUKeyDriver = YourDriverInstance;
       res = driver.YourDriver_onGetProperty(...);
       result.resultCode = res.resultCode
       result.property = res.property
     } catch (error) {
       // 场景：获取属性失败
       result.resultCode = res.resultCode
       console.error('promise: onGetProperty failed.');
     }
     return Promise.resolve(result);
   }
   ```

   （4）从API版本26.0.0开始，onSetProperty用于执行设置属性操作。handle为资源句柄，propertyId为待设置的属性标识。操作参数在params中传入。当调用成功时，返回值中的resultCode成员设置为0，表示设置属性成功。调用失败时，resultCode携带错误码信息。

   ```ts
   onSetProperty(handle: string, propertyId: string, params: Array<huksExternalCrypto.HuksExternalCryptoParam>): Promise<HuksCryptoExtensionResult> {
     let result: HuksCryptoExtensionResult = {
       resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
     };

     try {
       let driver: YourUKeyDriver = YourDriverInstance;
       result = driver.YourDriver_onSetProperty(handle, propertyId, params);
       result.resultCode = 0;
     } catch (error) {
       result.resultCode = HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL;
       console.error('promise: onSetProperty failed.');
     }
     return Promise.resolve(result);
   }
   ```

   （5）onAuthUkeyPin用于在UKey签名之前验证PIN码。加密后的PIN码通过param中传入[HUKS\_EXT\_CRYPTO\_TAG\_UKEY\_PIN](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptotag)参数携带，需使用onGetProperty中保存的私钥进行解密。

   当PIN码校验成功时，返回值中的resultCode成员设置为0，返回值中的authState设置为[HUKS\_EXT\_CRYPTO\_PIN\_AUTH\_SUCCEEDED](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalpinauthstate)。当PIN码不正确时，resultCode携带错误码信息，返回值中的retryCount设置为剩余重试次数，每次认证失败重试次数减1，当重试次数为0时，resultCode设置为[HUKS\_CRYPTO\_EXTENSION\_ERR\_PIN\_LOCKED](../harmonyos-references/js-apis-cryptoextensionability.md#hukscryptoextensionresultcode)，authState设置为[HUKS\_EXT\_CRYPTO\_PIN\_LOCKED](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalpinauthstate)。

   ```ts
   onAuthUkeyPin(handle: string, params: Array<huksExternalCrypto.HuksExternalCryptoParam>): Promise<HuksCryptoExtensionResult> {
     let pin: string | undefined = undefined;
     for (let param of params) {
       if (param.tag == huksExternalCrypto.HuksExternalCryptoTag.HUKS_EXT_CRYPTO_TAG_UKEY_PIN) {
         let originPinData = param.value as Uint8Array;
         // 根据导出公钥所传出的加密算法和填充方式进行解密originPinData获取pin
         // ...
       }
     }
     // ...
     let result: HuksCryptoExtensionResult = {
       resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
       authState: huksExternalCrypto.HuksExternalPinAuthState.HUKS_EXT_CRYPTO_PIN_NO_AUTH,
       retryCount: 0
     };

     let res: HuksCryptoExtensionResult = {
       resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
     }
     try {
       // 场景：PIN码认证成功
       let driver: YourUKeyDriver = YourDriverInstance;
       res = driver.YourDriver_onAuthUkeyPin(pin, ...);
       result.resultCode = res.resultCode
       result.authState = res.authState
     } catch (error) {
       // 场景：PIN码认证失败
       result.resultCode = res.resultCode
       result.retryCount = res.retryCount
       console.error('promise: onAuthUkeyPin failed.');
     }
     return Promise.resolve(result);
   }
   ```

   （6）onGetUkeyPinAuthState用于应用查询PIN码的认证状态。当调用成功时，返回值中的resultCode成员设置为0，返回值中的authState设置为对应的认证状态。调用失败时，resultCode携带错误码信息。

   ```ts
   onGetUkeyPinAuthState(handle: string, params: Array<huksExternalCrypto.HuksExternalCryptoParam>): Promise<HuksCryptoExtensionResult> {
     // ...
     let result: HuksCryptoExtensionResult = {
       resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
       authState: 0
     };

     let res: HuksCryptoExtensionResult = {
       resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
     }
     try {
       // 场景：获取PIN码认证状态成功
       let driver: YourUKeyDriver = YourDriverInstance;
       res = driver.YourDriver_onAuthUkeyPin(...);
       result.resultCode = res.resultCode
       result.authState = res.authState
       if (result.authState != 0) {
         // 场景： PIN码已认证
         // ...
       } else {
         // 场景： PIN码未认证
         // ...
       }
     } catch (error) {
       // 场景：获取PIN码认证状态失败
       result.resultCode = res.resultCode
       console.error('promise: onGetUkeyPinAuthState failed.');
     }
     return Promise.resolve(result);
   }
   ```

   （7）onClearUkeyPinAuthState用于重置PIN码的认证状态。当调用成功时，返回值中的resultCode成员设置为0。调用失败时，resultCode携带错误码信息。

   ```ts
   onClearUkeyPinAuthState(handle: string, params: Array<huksExternalCrypto.HuksExternalCryptoParam>): Promise<HuksCryptoExtensionResult> {
     // ...
     let result: HuksCryptoExtensionResult = {
       resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
     };

     let res: HuksCryptoExtensionResult = {
       resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
     }
     try {
       // 场景：清除PIN码认证状态成功
       let driver: YourUKeyDriver = YourDriverInstance;
       res = driver.YourDriver_onClearUkeyPinAuthState(...);
       result.resultCode = res.resultCode
     } catch (error) {
       // 场景：清除PIN码认证状态失败
       result.resultCode = res.resultCode
       console.error('promise: onClearUkeyPinAuthState failed.');
     }
     return Promise.resolve(result);
   }
   ```

   （8）onInitSession在UKey签名验签操作中用于初始化密钥会话。应用身份可以在param中由[HUKS\_EXT\_CRYPTO\_TAG\_UID](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptotag)参数携带。当调用成功时，返回值中的resultCode成员设置为0，handle成员非空。调用失败时，resultCode携带错误码信息。

   ```ts
   onInitSession(handle: string, params: huks.HuksOptions): Promise<HuksCryptoExtensionResult> {
     // ...
     let result: HuksCryptoExtensionResult = {
       resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
       handle: ""
     };

     let res: HuksCryptoExtensionResult = {
       resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
     }
     try {
       // 场景：三段式init阶段成功
       let driver: YourUKeyDriver = YourDriverInstance;
       res = driver.YourDriver_onInitSession(...);
       result.resultCode = res.resultCode
       result.handle = res.handle
     } catch (error) {
       // 场景：三段式init阶段失败
       result.resultCode = res.resultCode
       console.error('promise: onInitSession failed.');
     }
     return Promise.resolve(result);
   }
   ```

   （9）onUpdateSession在UKey签名验签操作中用于分段传输大批量数据。应用身份可以在param中由[HUKS\_EXT\_CRYPTO\_TAG\_UID](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptotag)参数携带。当调用成功时，返回值中的resultCode成员设置为0。调用失败时，resultCode携带错误码信息。

   ```ts
   onUpdateSession(handle: string, params: huks.HuksOptions): Promise<HuksCryptoExtensionResult> {
     // ...
     let certs: Uint8Array = new Uint8Array();
     let result: HuksCryptoExtensionResult = {
       resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
       outData: certs
     };

     let res: HuksCryptoExtensionResult = {
       resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
     }
     try {
       // 场景：三段式update阶段成功
       let driver: YourUKeyDriver = YourDriverInstance;
       res = driver.YourDriver_onUpdateSession(...);
       result.resultCode = res.resultCode
       result.outData = res.outData
     } catch (error) {
       // 场景：三段式update阶段失败
       result.resultCode = res.resultCode
       console.error('promise: onUpdateSession failed.');
     }
     return Promise.resolve(result);
   }
   ```

   （10）onFinishSession在UKey签名操作中用于传输最后一段明文，在验签操作中用于传输签名。应用身份可以在param中由[HUKS\_EXT\_CRYPTO\_TAG\_UID](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptotag)参数携带。当调用成功时，返回值中的resultCode成员设置为0。调用失败时，resultCode携带错误码信息。

   ```ts
   onFinishSession(handle: string, params: huks.HuksOptions): Promise<HuksCryptoExtensionResult> {
     // ...
     let certs: Uint8Array = new Uint8Array();
     let result: HuksCryptoExtensionResult = {
       resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
       outData: certs
     };

     let res: HuksCryptoExtensionResult = {
       resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
     };
     try {
       // 场景：三段式finish阶段成功
       let driver: YourUKeyDriver = YourDriverInstance;
       res = driver.YourDriver_onFinishSession(...);
       result.resultCode = res.resultCode
       result.outData = res.outData
     } catch (error) {
       // 场景：三段式finish阶段失败
       result.resultCode = res.resultCode
       console.error('promise: onFinishSession failed.');
     }
     return Promise.resolve(result);
   }
   ```

   （11）onExportCertificate用于查询某个resourceId下的证书。可以通过解析参数[HUKS\_EXT\_CRYPTO\_TAG\_PURPOSE](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptotag)获取业务希望的证书类型。如未指定，默认获取的证书类型是签名证书。

   其值含义如下：

   0：默认用途。

   1：用于查询所有凭据。

   2：用于凭据签名。

   3：用于凭据加密。

   ```ts
   onExportCertificate(resourceId: string, params: Array<huksExternalCrypto.HuksExternalCryptoParam>): Promise<HuksCryptoExtensionResult> {
     // ...
     let certInfoSetArray: Array<HuksCryptoExtensionCertInfo> = []
     let result: HuksCryptoExtensionResult = {
       resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
       certs: certInfoSetArray
     };

     let res: HuksCryptoExtensionResult = {
       resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
     }
     try {
       // 场景：导出证书成功
       let driver: YourUKeyDriver = YourDriverInstance;
       res = driver.YourDriver_onExportCertificate(...);
       result.resultCode = res.resultCode
       result.certs = res.certs
     } catch (error) {
       // 场景：导出证书失败
       result.resultCode = res.resultCode
       console.error('promise: onExportCertificate failed.');
     }
     return Promise.resolve(result);
   }
   ```

   （12）onEnumCertificates在UKey签名验签操作中用于枚举证书列表。应用身份可以在params中由[HUKS\_EXT\_CRYPTO\_TAG\_UID](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptotag)参数携带。当调用成功时，返回值中的resultCode成员设置为0，返回值中的certs成员包含证书列表（类型为Array<[HuksCryptoExtensionCertInfo](../harmonyos-references/js-apis-cryptoextensionability.md#hukscryptoextensioncertinfo)>）。调用失败时，resultCode携带错误码信息。

   ```ts
   onEnumCertificates(params: Array<huksExternalCrypto.HuksExternalCryptoParam>): Promise<HuksCryptoExtensionResult> {
     // ...
     let certInfoSetArray: Array<HuksCryptoExtensionCertInfo> = []
     let result: HuksCryptoExtensionResult = {
       resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
       certs: certInfoSetArray
     };

     let res: HuksCryptoExtensionResult = {
       resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
     }
     try {
       // 场景：导出所有证书成功
       let driver: YourUKeyDriver = YourDriverInstance;
       res = driver.YourDriver_onEnumCertificates(...);
       result.resultCode = res.resultCode
       result.certs = res.certs
     } catch (error) {
       // 场景：导出所有证书失败
       result.resultCode = res.resultCode
       console.error('promise: onEnumCertificates failed.');
     }
     return Promise.resolve(result);
   }
   ```

   （13）从API版本26.0.0开始，onGetResourceId用于获取密钥扩展能力的资源ID。params中需携带以下必选参数：[HUKS\_EXT\_CRYPTO\_TAG\_ABILITY\_NAME](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptotag)表示Ability名称、[HUKS\_EXT\_CRYPTO\_TAG\_BUNDLE\_NAME](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptotag)表示Bundle名称、[HUKS\_EXT\_CRYPTO\_TAG\_RESOURCE\_INFO](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptotag)表示厂商自定义的资源信息。当调用成功时，返回值中的resultCode成员设置为0，resourceId成员非空。调用失败时，resultCode携带错误码信息。

   ```ts
   onGetResourceId(params: huksExternalCrypto.HuksExternalCryptoParam[]): Promise<HuksCryptoExtensionResult> {
     let result: HuksCryptoExtensionResult = {
       resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
     };

     // 获取必选参数：资源信息
     let resourceInfo: Uint8Array | undefined = params.find((param =>
       param.tag === huksExternalCrypto.HuksExternalCryptoTag.HUKS_EXT_CRYPTO_TAG_RESOURCE_INFO))?.value as Uint8Array;
     if (resourceInfo === undefined) {
       return Promise.resolve(result);
     }
      
     try {
       let driver: YourUKeyDriver = YourDriverInstance;
       let resourceId: string = driver.YourDriver_onGetResourceId(abilityName, bundleName, resourceInfo);
       result.resultCode = 0;
       result.resourceId = resourceId;
     } catch (error) {
       result.resultCode = HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL;
       console.error('promise: onGetResourceId failed.');
     }
     return Promise.resolve(result);
   }
   ```

   （14）从API版本26.0.0开始，onImportCertificate用于导入证书到扩展设备。certInfo包含待导入的证书信息，包括证书用途、资源ID和证书数据。当调用成功时，返回值中的resultCode成员设置为0。调用失败时，resultCode携带错误码信息。

   ```ts
   onImportCertificate(handle: string, certInfo: HuksCryptoExtensionCertInfo, params?: huksExternalCrypto.HuksExternalCryptoParam[]): Promise<HuksCryptoExtensionResult> {
     let result: HuksCryptoExtensionResult = {
       resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
     };
     
     try {
       let driver: YourUKeyDriver = YourDriverInstance;
       result = driver.YourDriver_onImportCertificate(handle, certInfo, params);
       result.resultCode = 0;
     } catch (error) {
       result.resultCode = HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL;
       console.error('promise: onImportCertificate failed.');
     }
     return Promise.resolve(result);
   }
   ```

   （15）从API版本26.0.0开始，onGenerateKeyItem用于在扩展设备内生成密钥对。params中的参数为可选参数，由Extension厂商定义支持范围。如未传入相应参数，厂商需设置默认行为。当调用成功时，返回值中的resultCode成员设置为0；调用失败时，resultCode携带错误码信息。

   ```ts
   onGenerateKeyItem(handle: string, params: huks.HuksParam[]): Promise<HuksCryptoExtensionResult> {
     let result: HuksCryptoExtensionResult = {
       resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
     };

     // 解析可选参数
     let algorithm: huks.HuksKeyAlg | undefined = params.find(
       param => param.tag === huks.HuksTag.HUKS_TAG_ALGORITHM)?.value as huks.HuksKeyAlg;
     let keySize: huks.HuksKeySize | undefined = params.find(
       param => param.tag === huks.HuksTag.HUKS_TAG_KEY_SIZE)?.value as huks.HuksKeySize;
     let purpose: huks.HuksKeyPurpose | undefined = params.find(
       param => param.tag === huks.HuksTag.HUKS_TAG_PURPOSE)?.value as huks.HuksKeyPurpose;

     // 如未传入参数，设置默认值
     if (algorithm === undefined) {
       algorithm = huks.HuksKeyAlg.HUKS_ALG_RSA;
     }
     if (keySize === undefined) {
       keySize = huks.HuksKeySize.HUKS_RSA_KEY_SIZE_2048;
     }
     if (purpose === undefined) {
       purpose = huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN;
     }
       
     try {
       let driver: YourUKeyDriver = YourDriverInstance;
       result = driver.YourDriver_onGenerateKeyItem(handle, algorithm, keySize, purpose);
       result.resultCode = 0;
     } catch (error) {
       result.resultCode = HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL;
       console.error('promise: onGenerateKeyItem failed.');
     }
     return Promise.resolve(result);
   }
   ```

   （16）从API版本26.0.0开始，onExportKeyItem用于导出指定密钥的公钥。params中的参数为可选参数，由Extension厂商定义支持范围。如未传入相应参数，厂商需设置默认行为。推荐传入密钥用途（HUKS\_TAG\_PURPOSE）参数，以便导出指定用途的公钥。当调用成功时，返回值中的resultCode成员设置为0，outData携带导出的公钥数据；调用失败时，resultCode携带错误码信息。

   ```ts
   onExportKeyItem(handle: string, params: huks.HuksParam[]): Promise<HuksCryptoExtensionResult> {
     let result: HuksCryptoExtensionResult = {
       resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
     };

     // 解析可选参数，推荐传入密钥用途
     let purpose: huks.HuksKeyPurpose | undefined = params.find(
       param => param.tag === huks.HuksTag.HUKS_TAG_PURPOSE)?.value as huks.HuksKeyPurpose;

     // 如未传入用途参数，设置默认值（推荐默认签名用途）
     if (purpose === undefined) {
       purpose = huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN;
     }
      
     try {
       let driver: YourUKeyDriver = YourDriverInstance;
       let pubKey: Uint8Array = driver.YourDriver_onExportKeyItem(handle, purpose);
       result.resultCode = 0;
       result.outData = pubKey;
     } catch (error) {
       result.resultCode = HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL;
       console.error('promise: onExportKeyItem failed.');
     }
     return Promise.resolve(result);
   }
   ```

   （17）从API版本26.0.0开始，onImportWrappedKeyItem用于导入加密封装的密钥对。params中的参数为可选参数，由Extension厂商定义支持范围。如未传入相应参数，厂商需设置默认行为。wrappedHandle用于指定解封密钥的密钥资源句柄，wrappedKey为封装密钥数据。当调用成功时，返回值中的resultCode成员设置为0；调用失败时，resultCode携带错误码信息。

   ```ts
   onImportWrappedKeyItem(handle: string, wrappedHandle: string, params: huks.HuksParam[], wrappedKey: Uint8Array): Promise<HuksCryptoExtensionResult> {
     let result: HuksCryptoExtensionResult = {
       resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
     };

     // 解析可选参数
     let algorithm: huks.HuksKeyAlg | undefined = params.find(
       param => param.tag === huks.HuksTag.HUKS_TAG_ALGORITHM)?.value as huks.HuksKeyAlg;
     let keySize: huks.HuksKeySize | undefined = params.find(
       param => param.tag === huks.HuksTag.HUKS_TAG_KEY_SIZE)?.value as huks.HuksKeySize;
     let purpose: huks.HuksKeyPurpose | undefined = params.find(
       param => param.tag === huks.HuksTag.HUKS_TAG_PURPOSE)?.value as huks.HuksKeyPurpose;

     // 如未传入参数，设置默认值
     if (algorithm === undefined) {
       algorithm = huks.HuksKeyAlg.HUKS_ALG_RSA;
     }
     if (keySize === undefined) {
       keySize = huks.HuksKeySize.HUKS_RSA_KEY_SIZE_2048;
     }
     if (purpose === undefined) {
       purpose = huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT;
     }
      
     try {
       let driver: YourUKeyDriver = YourDriverInstance;
       result = driver.YourDriver_onImportWrappedKeyItem(handle, wrappedHandle, algorithm, keySize, purpose, wrappedKey);
       result.resultCode = 0;
     } catch (error) {
       result.resultCode = HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL;
       console.error('promise: onImportWrappedKeyItem failed.');
     }
     return Promise.resolve(result);
   }
   ```

## 驱动应用注册、解注册CryptoExtensionAbility适配

### 注册CryptoExtensionAbility

驱动HAP检测到UKey存在时，向系统注册CryptoExtensionAbility。例如：UKey插入等。

**示例：**

```ts
// ./ets/cryptoability/CryptoAbility.ts

import { huksExternalCrypto } from '@kit.UniversalKeystoreKit';

let ExtPropertiesTemp: Array<huksExternalCrypto.HuksExternalCryptoParam> = [
  {
      tag: huksExternalCrypto.HuksExternalCryptoTag.HUKS_EXT_CRYPTO_TAG_ABILITY_NAME,
      value: stringToUint8Array("YourCryptoExtensionName")
  }
]

// provider名称，为保证全局唯一，建议包含厂商信息。
let provider = "testProvider"
huksExternalCrypto.registerProvider(provider, ExtPropertiesTemp);
```

### 解注册CryptoExtensionAbility

驱动HAP检测到UKey不存在时，向系统解注册CryptoExtensionAbility。例如：UKey拔出等。

**示例：**

```ts
huksExternalCrypto.unregisterProvider(provider, ExtPropertiesTemp);
```
