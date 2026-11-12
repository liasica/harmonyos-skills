---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-extension-ability-support-dev
title: CryptoExtensionAbility适配开发指导
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 密钥管理扩展 > CryptoExtensionAbility适配 > CryptoExtensionAbility适配开发指导
category: harmonyos-guides
scraped_at: 2026-11-12T09:51:41+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:837ff5cd5df1bdc49ee64e5b9a0f85dbfb367ceec4bc7bdf837aaefbac8c3930
---

## 约束限制

针对CryptoExtensionAbility接口调用限制，详细请参考API中的[约束限制](../harmonyos-references/js-apis-cryptoextensionability.md#约束限制)。

## 适配指导

本文档旨在指导**密钥管理扩展应用开发者**如何继承实现[CryptoExtensionAbility](../harmonyos-references/js-apis-cryptoextensionability.md)中的接口能力，涵盖项目搭建、核心实现模式、所有接口的参考示例。此处给出实现参考，可根据业务按需实现其中部分接口，其他实现依照业务需要依次调用driver封装的底层驱动函数。

在DevEco Studio工程中手动新建一个CryptoExtensionAbility组件，具体步骤如下：

1. 在工程Module对应的ets目录下，右键选择“New > Directory”，新建一个目录，名称可以自己定义，例如cryptoability。
2. 在cryptoability目录，右键选择“New > ArkTS File”，新建一个文件，名称可以自己定义，例如CryptoAbility.ets。

   其目录结构如下所示：

   ```txt
   ├── ets
   │   └── cryptoability
   │       └── CryptoAbility.ets
   ```
3. 开发CryptoExtensionAbility需要配置[ohos.permission.CRYPTO\_EXTENSION\_REGISTER](restricted-permissions.md#ohospermissioncrypto_extension_register)权限，该权限属于[受限开放权限](restricted-permissions.md)，请按照[申请受限权限](declare-permissions-in-acl.md)指引申请。

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
4. 在工程Module对应的module.json5配置文件中注册CryptoExtensionAbility组件到[extensionAbilities](module-configuration-file.md#extensionabilities标签)标签中。

   * name标签表示ability名称，最大长度为127字节。配置多个ability时要求每个name标签必须是唯一的。
   * srcEntry标签表示当前CryptoExtensionAbility组件所对应的代码路径。
   * type标签需要设置为“crypto”。
   * exported标签设置为false表示不允许三方应用调用。

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
5. 在CryptoAbility.ets文件中导入依赖包，自定义类继承[CryptoExtensionAbility](../harmonyos-references/js-apis-cryptoextensionability.md)组件并按需实现其中的接口函数。此处给出实现参考，与底层驱动的调用对应关系参见下文。

   ```typescript
   import { huks, huksExternalCrypto, CryptoExtensionAbility, HuksCryptoExtensionCertInfo, HuksCryptoExtensionResult, HuksCryptoExtensionResultCode } from '@kit.UniversalKeystoreKit';
   import { util } from '@kit.ArkTS';
   import { cryptoFramework } from '@kit.CryptoArchitectureKit';
   import { deviceInfo } from '@kit.BasicServicesKit';

   export class CryptoExtension extends CryptoExtensionAbility {
     // 建议的状态管理机制，仅供参考
     // 1. 句柄映射表：key = "${uid}:${handle}"，value = 底层UKey句柄
     private handleMap: Map<string, YourDriverHandle> = new Map();

     // 2. 会话状态表：key = "${uid}:${sessionHandle}"，value = 会话中间数据
     private sessionMap: Map<string, SessionState> = new Map();

     // 3. PIN认证状态表：key = "${uid}:${ukeyApplicationId}"，value = authState
     private authStateMap: Map<string, number> = new Map();

     // 4. PIN解密私钥（在onGetProperty中生成，onAuthUkeyPin中使用）
     private pinDecryptKey: cryptoFramework.PriKey | null = null;
     private pinDecryptAlgo: string = '';               // 对应的解密算法
     private pinDecryptTransformation: string = '';     // 对应的填充模式

     // 5. 句柄生成计数器
     private handleCounter: number = 0;

     // 从Array类型params中提取UID
     private extractUid(params: Array<huksExternalCrypto.HuksExternalCryptoParam> | HuksCryptoExtensionParam[]): string | undefined {
       const arr = params as Array<huksExternalCrypto.HuksExternalCryptoParam>;
       const param = arr.find(p =>
         p.tag === huksExternalCrypto.HuksExternalCryptoTag.HUKS_EXT_CRYPTO_TAG_UID
       );
       return param?.value?.toString();
     }

     // 从huks.HuksOptions/HuksCryptoExtensionParams类型params中提取UID
     private extractUidFromSessionParams(params: huks.HuksOptions | HuksCryptoExtensionParams): string | undefined {
       const props = (params as huks.HuksOptions).properties as Array<huksExternalCrypto.HuksExternalCryptoParam> | undefined;
       if (!props) return undefined;
       const param = props.find(p =>
         p.tag === huksExternalCrypto.HuksExternalCryptoTag.HUKS_EXT_CRYPTO_TAG_UID
       );
       return param?.value?.toString();
     }

     // 构造隔离key
     private makeStorageKey(uid: string, ...parts: string[]): string {
       return [uid, ...parts].join(':');
     }

     // 生成唯一handle
     private generateUniqueHandle(): string {
       this.handleCounter += 1;
       return `handle-${this.handleCounter}-${Date.now()}`;
     }

     // 统一错误返回辅助
     private failResult(result: HuksCryptoExtensionResult, code: number, error?: unknown): HuksCryptoExtensionResult {
       result.resultCode = code;
       if (error !== undefined) {
         result.errInfo = {
           errno: (error as UKeyDriverError)?.driverCode ?? -1,
           errorDesc: String(error)
         };
       }
       return result;
     }

     // 本步骤内的接口函数实现均需在class内，为方便开发者理解及使用，每个接口函数在下文详细解释。
   }
   ```

## 开发示例

### 调用onOpenResource打开资源

onOpenResource用于打开指定资源（如建立会话或连接），handle为资源句柄。当调用成功时，返回值中的resultCode成员需设置为0，handle成员非空；调用失败时，resultCode携带错误码信息。

```typescript
onOpenResource(resourceId: string, params: Array<huksExternalCrypto.HuksExternalCryptoParam>): Promise<HuksCryptoExtensionResult> {
  const result: HuksCryptoExtensionResult = {
    resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
  };

  const uid = this.extractUid(params);
  if (uid === undefined) {
    return Promise.resolve(result);
  }

  // 解析resource index，API版本22需要解析index字段，在API版本26.0.0及以上可直接使用。
  const apiVersion = deviceInfo.sdkApiVersion;
  let index: string;
  if (apiVersion >= 26) {
    index = resourceId;
  } else {
    try {
     index = JSON.parse(resourceId)['index'];
    } catch (e) {
     result.resultCode = HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL;
     return Promise.resolve(result);
    }
  }

  let driverHandle: YourDriverHandle | null = null;
  try {
    const driverRes = YourDriverInstance.YourDriver_onOpenResource(index);
    if (driverRes.resultCode !== 0 || driverRes.driverHandle === undefined) {
     result.resultCode = driverRes.resultCode;
     if (driverRes.errInfo) result.errInfo = driverRes.errInfo;
     return Promise.resolve(result);
    }
    driverHandle = driverRes.driverHandle;

    const handle = this.generateUniqueHandle();
    const key = this.makeStorageKey(uid, handle);
    this.handleMap.set(key, driverHandle);

    result.resultCode = 0;
    result.handle = handle;
  } catch (error) {
    // 关键：驱动已分配句柄但后续失败，需要主动关闭
    if (driverHandle !== null) {
     try { YourDriverInstance.YourDriver_onCloseResource(driverHandle); } catch (_) {}
    }
    this.failResult(result, HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_UKEY_DRIVER_FAIL, error);
    console.error('promise: onOpenResource failed.');
  }
  return Promise.resolve(result);
}
```

### 调用onCloseResource关闭资源

onCloseResource用于关闭指定资源（如释放会话或连接）,handle为待关闭资源的句柄。当调用成功时，返回值中的resultCode成员需设置为0；调用失败时，resultCode携带错误码信息。

```typescript
onCloseResource(handle: string, params: Array<huksExternalCrypto.HuksExternalCryptoParam> | HuksCryptoExtensionParam[]): Promise<HuksCryptoExtensionResult> {
  const result: HuksCryptoExtensionResult = {
    resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
  };
  
  const uid = this.extractUid(params);
  if (uid === undefined) {
    return Promise.resolve(result);
  }
  
  // 查找UKey内部映射句柄
  const key = this.makeStorageKey(uid, handle);
  const driverHandle = this.handleMap.get(key);
  if (driverHandle === undefined) {
    result.resultCode = HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_HANDLE_NOT_EXIST;
    return Promise.resolve(result);
  }

  try {
    const driverRes = YourDriverInstance.YourDriver_onCloseResource(driverHandle);
    this.handleMap.delete(key);
    result.resultCode = driverRes.resultCode;
    if (driverRes.errInfo) result.errInfo = driverRes.errInfo;
  } catch (error) {
    this.failResult(result, HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_UKEY_DRIVER_FAIL, error);
    console.error('promise: onCloseResource failed.');
  }
  return Promise.resolve(result);
}
```

### 调用onGetProperty获取资源信息

onGetProperty用于获取指定资源的属性信息，handle为资源句柄，propertyId为待获取的属性标识。当调用成功时，返回值中的resultCode成员需设置为0，返回值中的property成员包含属性信息。调用失败时，resultCode携带错误码信息。

在onGetProperty中必须实现导出公钥功能，以便上游业务使用PIN加密传输并完成PIN码认证。加密算法支持RSA、SM2等。当入参propertyId为SKF\_ExportPublicKey时，返回的公钥信息采用JSON格式，包含以下4个必选字段，分别是publicKey（公钥数据）、algo（算法类型及密钥长度）、transformation（密码学操作参数，如填充模式）、size（公钥数据长度）。具体实现可参考下方示例代码中onGetProperty接口的相关部分。

```typescript
onGetProperty(handle: string, propertyId: string, params: Array<huksExternalCrypto.HuksExternalCryptoParam> | HuksCryptoExtensionParam[]): Promise<HuksCryptoExtensionResult> {
  const result: HuksCryptoExtensionResult = {
    resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
    property: []
  };

  const uid = this.extractUid(params);
  if (uid === undefined) {
    return Promise.resolve(result);
  }
  
  // 必须实现：导出公钥用于PIN加密
  if (propertyId === 'SKF_ExportPublicKey') {
    const encryptionAlgo = 'RSA1024';
    const padding = 'PKCS1';
    const transformation = `${encryptionAlgo}|${padding}`;

    // 1. 创建一个AsyKeyGenerator实例。
    const rsaGenerator = cryptoFramework.createAsyKeyGenerator(`${encryptionAlgo}|${padding}`);
    // 2. 使用密钥生成器随机生成非对称密钥对，并保存私钥。
    const keyPair = rsaGenerator.generateKeyPairSync();
    this.pinDecryptKey = keyPair.priKey;
    this.pinDecryptAlgo = `${encryptionAlgo}|${padding}`;
    // 3. 将公钥导出，并转换为Json字符串
    const pkData = Array.from(keyPair.pubKey.getEncoded().data);
    const encoder = new util.TextEncoder();
    const info = encoder.encodeInto(JSON.stringify({
      publicKey: pkData,
      algo: encryptionAlgo,
      transformation: transformation,
      size: pkData.length
    }));
    // 返回用来加密传PIN的公钥和加密算法信息，详见导出公钥文档
    result.resultCode = 0;
    result.property = [{
      tag: huksExternalCrypto.HuksExternalCryptoTag.HUKS_EXT_CRYPTO_TAG_EXTRA_DATA,
      value: info
    }];
    return Promise.resolve(result);
  }

   // 其他propertyId委托驱动处理
   try {
     const driverHandle = this.handleMap.get(this.makeStorageKey(uid, handle));
     if (driverHandle === undefined) {
       result.resultCode = HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_HANDLE_NOT_EXIST;
       return Promise.resolve(result);
     }
     const driverRes = YourDriverInstance.YourDriver_onGetProperty(driverHandle, propertyId);
     result.resultCode = driverRes.resultCode;
     result.property = driverRes.property;
     if (driverRes.errInfo) result.errInfo = driverRes.errInfo;
   } catch (error) {
     this.failResult(result, HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_UKEY_DRIVER_FAIL, error);
     console.error('promise: onGetProperty failed.');
   }
   return Promise.resolve(result);
}
```

### 调用onAuthUkeyPin验证PIN码

onAuthUkeyPin用于在使用私钥进行签名之前验证PIN码。加密后的PIN码通过param中传入[HUKS\_EXT\_CRYPTO\_TAG\_UKEY\_PIN](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptotag)参数携带，需使用onGetProperty中保存的私钥进行解密。

* **验证成功**：当PIN码校验成功时，返回值中的resultCode成员需设置为0，返回值中的authState设置为[HUKS\_EXT\_CRYPTO\_PIN\_AUTH\_SUCCEEDED](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalpinauthstate)。
* **验证失败**：当PIN码不正确时，resultCode携带错误码信息，返回值中的retryCount设置为剩余重试次数，每次认证失败重试次数减1。
* **UKey锁住**：当重试次数为0时，resultCode设置为[HUKS\_CRYPTO\_EXTENSION\_ERR\_PIN\_LOCKED](../harmonyos-references/js-apis-cryptoextensionability.md#hukscryptoextensionresultcode)，authState设置为[HUKS\_EXT\_CRYPTO\_PIN\_LOCKED](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalpinauthstate)。

  ```typescript
  onAuthUkeyPin(handle: string, params: Array<huksExternalCrypto.HuksExternalCryptoParam> | HuksCryptoExtensionParam[]): Promise<HuksCryptoExtensionResult> {
    const result: HuksCryptoExtensionResult = {
      resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
      authState: huksExternalCrypto.HuksExternalPinAuthState.HUKS_EXT_CRYPTO_PIN_NO_AUTH,
      retryCount: 0
    };

    const uid = this.extractUid(params);
    if (uid === undefined) {
      return Promise.resolve(result);
    }

    // 1. 获取密文
    const pinParam = params.find(p =>
      p.tag === huksExternalCrypto.HuksExternalCryptoTag.HUKS_EXT_CRYPTO_TAG_UKEY_PIN
    );
    if (pinParam === undefined) return Promise.resolve(result);
    const encryptedPin = pinParam.value as Uint8Array;

    // 2. 用onGetProperty中保存的私钥解密
    if (this.pinDecryptKey === null) {
      result.resultCode = HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_PIN_NO_AUTH;
      return Promise.resolve(result);
    }
    let plainPin: string;
    try {
      const cipher = cryptoFramework.createCipher(this.pinDecryptAlgo);
      cipher.init(cryptoFramework.CryptoMode.DECRYPT_MODE, this.pinDecryptKey, null);
      const plainBytes = cipher.doFinal(encryptedPin);
      plainPin = new util.TextDecoder().decodeToString(plainBytes);
    } catch (error) {
      result.resultCode = HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL;
      return Promise.resolve(result);
    }

    // 3. 调驱动验证
    const driverHandle = this.handleMap.get(this.makeStorageKey(uid, handle));
    if (driverHandle === undefined) {
      result.resultCode = HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_HANDLE_NOT_EXIST;
      return Promise.resolve(result);
    }
    try {
      const driverRes = YourDriverInstance.YourDriver_onAuthUkeyPin(driverHandle, plainPin);
      result.resultCode = driverRes.resultCode;
      result.retryCount = driverRes.retryCount;
      if (driverRes.errInfo) result.errInfo = driverRes.errInfo;

      if (driverRes.resultCode === 0) {
        // 认证成功，维护认证状态
        const authKey = this.makeStorageKey(uid, 'Application-' + handle);
        this.authStateMap.set(authKey, huksExternalCrypto.HuksExternalPinAuthState.HUKS_EXT_CRYPTO_PIN_AUTH_SUCCEEDED);
        result.authState = huksExternalCrypto.HuksExternalPinAuthState.HUKS_EXT_CRYPTO_PIN_AUTH_SUCCEEDED;
      } else if (driverRes.retryCount === 0) {
        result.resultCode = HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_PIN_LOCKED;
        result.authState = huksExternalCrypto.HuksExternalPinAuthState.HUKS_EXT_CRYPTO_PIN_LOCKED;
      } else {
        result.resultCode = HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_PIN_INCORRECT;
      }
    } catch (error) {
      this.failResult(result, HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_UKEY_DRIVER_FAIL, error);
    }
    return Promise.resolve(result);
  }
  ```

### 调用onGetUkeyPinAuthState查询PIN码认证状态

onGetUkeyPinAuthState用于查询PIN码认证状态。当调用成功时，返回值中的resultCode成员需设置为0，返回值中的authState设置为对应的认证状态。调用失败时，resultCode携带错误码信息。

```typescript
onGetUkeyPinAuthState(handle: string, params: Array<huksExternalCrypto.HuksExternalCryptoParam> | HuksCryptoExtensionParam[]): Promise<HuksCryptoExtensionResult> {
 const result: HuksCryptoExtensionResult = {
   resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
   authState: huksExternalCrypto.HuksExternalPinAuthState.HUKS_EXT_CRYPTO_PIN_NO_AUTH
 };
  
 const uid = this.extractUid(params);
 if (uid === undefined) {
   return Promise.resolve(result);
 }
 
 // 在缓存中获取认证状态，或调用Driver接口实时获取状态并更新缓存
 const authKey = this.makeStorageKey(uid, 'Application-' + handle);
 result.authState = this.authStateMap.get(authKey) ?? huksExternalCrypto.HuksExternalPinAuthState.HUKS_EXT_CRYPTO_PIN_NO_AUTH;
 result.resultCode = 0;
 return Promise.resolve(result);
}
```

### 调用onClearUkeyPinAuthState重置PIN码状态

onClearUkeyPinAuthState用于重置PIN码认证状态。当调用成功时，返回值中的resultCode成员需设置为0。调用失败时，resultCode携带错误码信息。

```typescript
onClearUkeyPinAuthState(handle: string, params: Array<huksExternalCrypto.HuksExternalCryptoParam> | HuksCryptoExtensionParam[]): Promise<HuksCryptoExtensionResult> {
 const result: HuksCryptoExtensionResult = {
   resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
 };

 const uid = this.extractUid(params);
 if (uid === undefined) {
   return Promise.resolve(result);
 }

 // 在缓存中清除认证状态，或调用Driver接口清除状态并更新缓存
 const authKey = this.makeStorageKey(uid, 'Application-' + handle);
 this.authStateMap.delete(authKey);
 result.resultCode = 0;
 return Promise.resolve(result);
}
```

### 调用onInitSession初始化密钥会话

onInitSession用于初始化密钥会话。当调用成功时，返回值中的resultCode成员需设置为0，handle成员非空。调用失败时，resultCode携带错误码信息。

```typescript
onInitSession(handle: string, params: huks.HuksOptions | HuksCryptoExtensionParams): Promise<HuksCryptoExtensionResult> {
  const result: HuksCryptoExtensionResult = {
    resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
    handle: ""
  };

  const uid = this.extractUidFromSessionParams(params);
  if (uid === undefined) {
    return Promise.resolve(result);
  }

  const driverHandle = this.handleMap.get(this.makeStorageKey(uid, handle));
  if (driverHandle === undefined) {
    result.resultCode = HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_HANDLE_NOT_EXIST;
    return Promise.resolve(result);
  }

  let driverSession: YourDriverSessionHandle | null = null;
  let sessionHandle = '';
  try {
    const initRes: YourDriverSessionResult = YourDriverInstance.YourDriver_onInitSession(driverHandle, params) as YourDriverSessionResult;
    if (initRes.resultCode !== 0) {
      result.resultCode = initRes.resultCode;
      if (initRes.errInfo) result.errInfo = initRes.errInfo;
      return Promise.resolve(result);
    }
    driverSession = initRes.driverSession;
    sessionHandle = initRes.sessionHandle;
  } catch (error) {
    return Promise.resolve(this.failResult(result, HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_UKEY_DRIVER_FAIL, error));
  }

  // 成功时缓存，失败时回滚驱动侧
  try {
    const sessionKey = this.makeStorageKey(uid, sessionHandle);
    const state: SessionState = {
      driverSession: driverSession,
      accumData: new Uint8Array(),
    };
    this.sessionMap.set(sessionKey, state);
    result.resultCode = 0;
    result.handle = sessionHandle;
  } catch (error) {
    // 缓存失败，回滚驱动侧会话
    if (driverSession !== null) {
      try { YourDriverInstance.YourDriver_onFinishSession(driverSession); } catch (_) {}
    }
    this.failResult(result, HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL, error);
  }
  return Promise.resolve(result);
}
```

### 调用onUpdateSession分段传输数据

onUpdateSession用于分段传输大批量数据。当调用成功时，返回值中的resultCode成员需设置为0。调用失败时，resultCode携带错误码信息。

```typescript
onUpdateSession(initHandle: string, params: huks.HuksOptions | HuksCryptoExtensionParams): Promise<HuksCryptoExtensionResult> {
  const result: HuksCryptoExtensionResult = {
    resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
    outData: new Uint8Array()
  };

  const uid = this.extractUidFromSessionParams(params);
  if (uid === undefined) {
    return Promise.resolve(result);
  }

  const sessionKey = this.makeStorageKey(uid, initHandle);
  const session = this.sessionMap.get(sessionKey);
  if (session === undefined) {
    result.resultCode = HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_HANDLE_NOT_EXIST;
    return Promise.resolve(result);
  }

  try {
    const driverRes: YourDriverUpdateResult = YourDriverInstance.YourDriver_onUpdateSession(session.driverSession, params);
    result.resultCode = driverRes.resultCode;
    result.outData = driverRes.outData;
    if (driverRes.errInfo) result.errInfo = driverRes.errInfo;
  } catch (error) {
    this.failResult(result, HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_UKEY_DRIVER_FAIL, error);
  }
  return Promise.resolve(result);
}
```

### 调用onFinishSession完成数据传输

onFinishSession用于传输最后一段明文，在验签操作中用于传输签名。当调用成功时，返回值中的resultCode成员需设置为0。调用失败时，resultCode携带错误码信息。

```typescript
onFinishSession(initHandle: string, params: huks.HuksOptions | HuksCryptoExtensionParams): Promise<HuksCryptoExtensionResult> {
  const result: HuksCryptoExtensionResult = {
    resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
    outData: new Uint8Array()
  };

  const uid = this.extractUidFromSessionParams(params);
  if (uid === undefined) {
    return Promise.resolve(result);
  }

  const sessionKey = this.makeStorageKey(uid, initHandle);
  const session = this.sessionMap.get(sessionKey);
  if (session === undefined) {
    result.resultCode = HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_HANDLE_NOT_EXIST;
    return Promise.resolve(result);
  }

  try {
    const driverRes: YourDriverFinishResult = YourDriverInstance.YourDriver_onFinishSession(session.driverSession, params);
    result.resultCode = driverRes.resultCode;
    result.outData = driverRes.outData;
    if (driverRes.errInfo) result.errInfo = driverRes.errInfo;
  } catch (error) {
    this.failResult(result, HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_UKEY_DRIVER_FAIL, error);
  } finally {
    // 无论成败都清理会话缓存
    this.sessionMap.delete(sessionKey);
  }
  return Promise.resolve(result);
}
```

### 调用onExportCertificate查询证书

onExportCertificate用于查询某个resourceId下的证书。可以通过解析参数[HUKS\_EXT\_CRYPTO\_TAG\_PURPOSE](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptotag)获取业务希望的证书类型。如未指定，密钥管理扩展应用实现方需设置默认类型（建议签名证书）。

```typescript
onExportCertificate(resourceId: string, params?: Array<huksExternalCrypto.HuksExternalCryptoParam> | HuksCryptoExtensionParam[]): Promise<HuksCryptoExtensionResult> {
 const result: HuksCryptoExtensionResult = {
   resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
   certs: []
 };

 const paramList = params ?? [];
 // 建议0值为默认用途，详细建议可参见CryptoExtensionAbility扩展能力介绍文档
 const purpose = (paramList as Array<huksExternalCrypto.HuksExternalCryptoParam>).find(p => 
   p.tag === huksExternalCrypto.HuksExternalCryptoTag.HUKS_EXT_CRYPTO_TAG_PURPOSE
 )?.value as number ?? 0;

 try {
   const driverRes: YourDriverExportCertResult = YourDriverInstance.YourDriver_onExportCertificate(resourceId, purpose);
   result.resultCode = driverRes.resultCode;
   result.certs = driverRes.certs;
   if (driverRes.errInfo) result.errInfo = driverRes.errInfo;
 } catch (error) {
   this.failResult(result, HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_UKEY_DRIVER_FAIL, error);
 }
 return Promise.resolve(result);
}
```

### 调用onEnumCertificates查询证书列表

onEnumCertificates用于枚举证书列表。当调用成功时，返回值中的resultCode成员需设置为0，返回值中的certs成员包含证书列表（类型为Array<[HuksCryptoExtensionCertInfo](../harmonyos-references/js-apis-cryptoextensionability.md#hukscryptoextensioncertinfo)>）。调用失败时，resultCode携带错误码信息。

```typescript
onEnumCertificates(params?: Array<huksExternalCrypto.HuksExternalCryptoParam> | HuksCryptoExtensionParam[]): Promise<HuksCryptoExtensionResult> {
 let result: HuksCryptoExtensionResult = {
   resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
   certs: []
 };

 const paramList = params ?? [];
 // 建议0值为默认用途，详细建议可参见CryptoExtensionAbility扩展能力介绍文档
 const purpose = (paramList as Array<huksExternalCrypto.HuksExternalCryptoParam>).find(p => 
   p.tag === huksExternalCrypto.HuksExternalCryptoTag.HUKS_EXT_CRYPTO_TAG_PURPOSE
 )?.value as number ?? 0;

 try {
   const driverRes: YourDriverEnumCertResult = YourDriverInstance.YourDriver_onEnumCertificates(purpose);
   result.resultCode = driverRes.resultCode;
   result.certs = driverRes.certs;
   if (driverRes.errInfo) result.errInfo = driverRes.errInfo;
 } catch (error) {
   this.failResult(result, HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_UKEY_DRIVER_FAIL, error);
 }
 return Promise.resolve(result);
}
```

### 调用onImportCertificate导入证书

从API版本26.0.0开始，onImportCertificate用于导入证书到密钥管理扩展服务中。certInfo包含待导入的证书信息，包括证书用途、资源ID和证书数据。当调用成功时，返回值中的resultCode成员设置为0。调用失败时，resultCode携带错误码信息。

```typescript
onImportCertificate(handle: string, params: HuksCryptoExtensionParam[], certInfo: HuksCryptoExtensionCertInfo): Promise<HuksCryptoExtensionResult> {
  const result: HuksCryptoExtensionResult = {
    resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
  };

  const uid = this.extractUid(params);
  if (uid === undefined) {
    return Promise.resolve(result);
  }

  const driverHandle = this.handleMap.get(this.makeStorageKey(uid, handle));
  if (driverHandle === undefined) {
    result.resultCode = HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_HANDLE_NOT_EXIST;
    return Promise.resolve(result);
  }

  try {
    const driverRes: YourDriverResult = YourDriverInstance.YourDriver_onImportCertificate(driverHandle, params, certInfo);
    result.resultCode = driverRes.resultCode;
    if (driverRes.errInfo) result.errInfo = driverRes.errInfo;
  } catch (error) {
    this.failResult(result, HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_UKEY_DRIVER_FAIL, error);
  }
  return Promise.resolve(result);
}
```

### 调用onSetProperty设置属性

从API版本26.0.0开始，onSetProperty用于执行设置属性操作，handle为资源句柄，propertyId为待设置的属性标识，操作参数在params中传入。当调用成功时，返回值中的resultCode成员需设置为0，表示设置属性成功。调用失败时，resultCode携带错误码信息。

```typescript
onSetProperty(handle: string, propertyId: string, params: HuksCryptoExtensionParam[]): Promise<HuksCryptoExtensionResult> {
 let result: HuksCryptoExtensionResult = {
   resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
 };

 const uid = this.extractUid(params);
 if (uid === undefined) {
   return Promise.resolve(result);
 }

  try {
    const driverHandle = this.handleMap.get(this.makeStorageKey(uid, handle));
    if (driverHandle === undefined) {
      result.resultCode = HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_HANDLE_NOT_EXIST;
      return Promise.resolve(result);
    }
    const driverRes = YourDriverInstance.YourDriver_onSetProperty(driverHandle, propertyId, params);
    result.resultCode = driverRes.resultCode;
    if (driverRes.errInfo) result.errInfo = driverRes.errInfo;
  } catch (error) {
    this.failResult(result, HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_UKEY_DRIVER_FAIL, error);
    console.error('promise: onSetProperty failed.');
  }
  return Promise.resolve(result);
}
```

### 调用onGetResourceId获取资源ID

从API版本26.0.0开始，onGetResourceId用于获取密钥扩展能力的资源ID。当调用成功时，返回值中的resultCode成员需设置为0，resourceId成员非空。调用失败时，resultCode携带错误码信息。

```typescript
onGetResourceId(params: HuksCryptoExtensionParam[]): Promise<HuksCryptoExtensionResult> {
  const result: HuksCryptoExtensionResult = {
    resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
  };

  // 解析必选参数
  const resourceInfo = (params as Array<huksExternalCrypto.HuksExternalCryptoParam>).find(p => 
    p.tag === huksExternalCrypto.HuksExternalCryptoTag.HUKS_EXT_CRYPTO_TAG_RESOURCE_INFO
  )?.value as Uint8Array;
  const abilityName = (params as Array<huksExternalCrypto.HuksExternalCryptoParam>).find(p => 
    p.tag === huksExternalCrypto.HuksExternalCryptoTag.HUKS_EXT_CRYPTO_TAG_ABILITY_NAME
  )?.value.toString();
  const bundleName = (params as Array<huksExternalCrypto.HuksExternalCryptoParam>).find(p => 
    p.tag === huksExternalCrypto.HuksExternalCryptoTag.HUKS_EXT_CRYPTO_TAG_BUNDLE_NAME
  )?.value.toString();

  if (resourceInfo === undefined || abilityName === undefined || bundleName === undefined) {
    return Promise.resolve(result);
  }

  try {
    const driverRes: YourDriverGetResourceIdResult = YourDriverInstance.YourDriver_onGetResourceId(abilityName, bundleName, resourceInfo);
    result.resultCode = driverRes.resultCode;
    result.resourceId = driverRes.resourceId;
    if (driverRes.errInfo) result.errInfo = driverRes.errInfo;
  } catch (error) {
    this.failResult(result, HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL, error);
  }
  return Promise.resolve(result);
}
```

### 调用onGenerateKeyItem生成密钥

从API版本26.0.0开始，onGenerateKeyItem用于在密钥管理扩展服务中生成密钥对。params中的参数为可选参数，由密钥管理扩展应用实现方定义支持范围。如未传入相应参数，密钥管理扩展应用实现方需设置默认行为。当调用成功时，返回值中的resultCode成员需设置为0；调用失败时，resultCode携带错误码信息。

```typescript
onGenerateKeyItem(handle: string, params: HuksCryptoExtensionParam[]): Promise<HuksCryptoExtensionResult> {
 const result: HuksCryptoExtensionResult = {
   resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
 };

 const uid = this.extractUid(params);
 if (uid === undefined) {
   return Promise.resolve(result);
 }

 const driverHandle = this.handleMap.get(this.makeStorageKey(uid, handle));
 if (driverHandle === undefined) {
   result.resultCode = HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_HANDLE_NOT_EXIST;
   return Promise.resolve(result);
 }

 // 解析参数；如未传入参数，驱动应用应设置默认值
 const algorithm = (params.find(p => p.tag === huks.HuksTag.HUKS_TAG_ALGORITHM)?.value
   as huks.HuksKeyAlg) ?? huks.HuksKeyAlg.HUKS_ALG_RSA;
 const keySize = (params.find(p => p.tag === huks.HuksTag.HUKS_TAG_KEY_SIZE)?.value
   as huks.HuksKeySize) ?? huks.HuksKeySize.HUKS_RSA_KEY_SIZE_2048;
 const purpose = (params.find(p => p.tag === huks.HuksTag.HUKS_TAG_PURPOSE)?.value
   as huks.HuksKeyPurpose) ?? huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN;

 try {
   const driverRes: YourDriverResult = YourDriverInstance.YourDriver_onGenerateKeyItem(driverHandle, algorithm, keySize, purpose);
   result.resultCode = driverRes.resultCode;
   if (driverRes.errInfo) result.errInfo = driverRes.errInfo;
 } catch (error) {
   this.failResult(result, HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_UKEY_DRIVER_FAIL, error);
 }
 return Promise.resolve(result);
}
```

### 调用onExportKeyItem导出公钥

从API版本26.0.0开始，onExportKeyItem用于导出指定密钥的公钥。params中的参数为可选参数，由密钥管理扩展应用定义支持范围。如未传入相应参数，密钥管理扩展应用实现方需设置默认行为。推荐传入密钥用途（HUKS\_TAG\_PURPOSE）参数，以便导出指定用途的公钥。当调用成功时，返回值中的resultCode成员需设置为0，outData携带导出的公钥数据；调用失败时，resultCode携带错误码信息。

```typescript
onExportKeyItem(handle: string, params: HuksCryptoExtensionParam[]): Promise<HuksCryptoExtensionResult> {
 const result: HuksCryptoExtensionResult = {
   resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
   outData: new Uint8Array()
 };

 const uid = this.extractUid(params);
 if (uid === undefined) {
   return Promise.resolve(result);
 }

 const driverHandle = this.handleMap.get(this.makeStorageKey(uid, handle));
 if (driverHandle === undefined) {
   result.resultCode = HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_HANDLE_NOT_EXIST;
   return Promise.resolve(result);
 }

 // 推荐使用HUKS_TAG_PURPOSE参数
 const purpose = (params.find(p => p.tag === huks.HuksTag.HUKS_TAG_PURPOSE)?.value
   as huks.HuksKeyPurpose) ?? huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN;

 try {
   const driverRes: YourDriverExportKeyResult = YourDriverInstance.YourDriver_onExportKeyItem(driverHandle, purpose);
   result.resultCode = driverRes.resultCode;
   result.outData = driverRes.pubKey;
   if (driverRes.errInfo) result.errInfo = driverRes.errInfo;
 } catch (error) {
   this.failResult(result, HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_UKEY_DRIVER_FAIL, error);
 }
 return Promise.resolve(result);
}
```

### 调用onImportWrappedKeyItem导入密钥对

从API版本26.0.0开始，onImportWrappedKeyItem用于导入加密封装的密钥对。params中的参数为可选参数，由密钥管理扩展应用实现方定义支持范围。如未传入相应参数，密钥管理扩展应用实现方需设置默认行为。wrappedHandle用于指定解封密钥的密钥资源句柄，wrappedKey为封装密钥数据。当调用成功时，返回值中的resultCode成员需设置为0；调用失败时，resultCode携带错误码信息。

```typescript
onImportWrappedKeyItem(handle: string, wrappingHandle: string, params: HuksCryptoExtensionParam[], wrappedKey: Uint8Array): Promise<HuksCryptoExtensionResult> {
 const result: HuksCryptoExtensionResult = {
   resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
 };

 const uid = this.extractUid(params);
 if (uid === undefined) {
   return Promise.resolve(result);
 }

 const driverHandle = this.handleMap.get(this.makeStorageKey(uid, handle));
 if (driverHandle === undefined) {
   result.resultCode = HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_HANDLE_NOT_EXIST;
   return Promise.resolve(result);
 }

 // 解析参数；如未传入参数，驱动应用应设置默认值
 const algorithm = (params.find(p => p.tag === huks.HuksTag.HUKS_TAG_ALGORITHM)?.value
   as huks.HuksKeyAlg) ?? huks.HuksKeyAlg.HUKS_ALG_RSA;
 const keySize = (params.find(p => p.tag === huks.HuksTag.HUKS_TAG_KEY_SIZE)?.value
   as huks.HuksKeySize) ?? huks.HuksKeySize.HUKS_RSA_KEY_SIZE_2048;
 const purpose = (params.find(p => p.tag === huks.HuksTag.HUKS_TAG_PURPOSE)?.value
   as huks.HuksKeyPurpose) ?? huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT;

 try {
   const driverRes: YourDriverResult = YourDriverInstance.YourDriver_onImportWrappedKeyItem(
     driverHandle, wrappingHandle, algorithm, keySize, purpose, wrappedKey
   );
   result.resultCode = driverRes.resultCode;
   if (driverRes.errInfo) result.errInfo = driverRes.errInfo;
 } catch (e) {
   this.failResult(result, HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_UKEY_DRIVER_FAIL, e);
 }
 return Promise.resolve(result);
}
```
