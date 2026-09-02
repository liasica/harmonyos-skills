---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-refined-user-identity-authentication
title: 细粒度用户身份认证访问控制开发指导
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 密钥使用 > 访问控制 > 细粒度用户身份认证访问控制开发指导
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:32+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:2af3d3d5c5b379ac6ff1ca7e253b86dc0127d1e6742c1debeaf7d8bbaf27e794
---

细粒度用户身份认证访问控制是基于已有用户身份认证访问控制的扩展，提供了基于生物特征和锁屏密码二次身份认证的细粒度访问控制能力，允许设置密钥在加密、解密、签名、验签、密钥协商、密钥派生的单个或多个场景时是否需要进行身份验证。

比如，业务需要使用HUKS密钥加密保存账号密码信息等数据，要求在加密的时候不进行指纹等身份认证，解密的时候需要进行指纹等身份认证，这时就需要依赖HUKS提供细粒度的二次身份认证访问控制机制。

使用该功能仅需在密钥生成阶段，通过额外指定用于细粒度用户身份认证访问控制的HuksTag：HUKS\_TAG\_KEY\_AUTH\_PURPOSE，来指定在某种算法用途的情况下需要使用用户身份认证访问控制能力。

**说明** 

对于对称加解密场景，仅AES/CBC、AES/GCM、SM4/CBC模式支持细粒度访问控制。

## 开发步骤

### 密钥生成和数据加密

```typescript
import { huks } from '@kit.UniversalKeystoreKit';
import { userAuth } from '@kit.UserAuthenticationKit';
import { BusinessError } from '@kit.BasicServicesKit';

const KEY_ALIAS = 'test_sm4_key_alias';
const CIPHER_IN_DATA = 'Hks_SM4_Cipher_Test_101010101010101010110_string'; // 明文数据
const IV = '1234567890123456'; // 初始化向量
const AUTH_TYPE = userAuth.UserAuthType.PIN; // 认证类型：PIN码
const AUTH_TRUST_LEVEL = userAuth.AuthTrustLevel.ATL1; // 认证信任级别

let sessionHandle = 0; // 会话句柄
let challenge: Uint8Array; // 挑战值
let authToken: Uint8Array; // 认证令牌
let encryptedData: Uint8Array; // 加密后的密文
let decryptedData: Uint8Array; // 解密后的明文

class ThrowObject {
  public isThrow: boolean = false;
}

function stringToUint8Array(str: string): Uint8Array {
  let arr: number[] = [];
  for (let i = 0, j = str.length; i < j; ++i) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

/* 步骤1：密钥生成模块 */
const KEY_GENERATION_PROPERTIES: huks.HuksParam[] = [
  {
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_SM4,
  },
  {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT | huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT,
  },
  {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_SM4_KEY_SIZE_128,
  },
  {
    tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
    value: huks.HuksCipherMode.HUKS_MODE_CBC,
  },
  {
    tag: huks.HuksTag.HUKS_TAG_PADDING,
    value: huks.HuksKeyPadding.HUKS_PADDING_NONE,
  },
  {
    tag: huks.HuksTag.HUKS_TAG_USER_AUTH_TYPE,
    value: huks.HuksUserAuthType.HUKS_USER_AUTH_TYPE_PIN
  },
  {
    tag: huks.HuksTag.HUKS_TAG_KEY_AUTH_ACCESS_TYPE,
    value: huks.HuksAuthAccessType.HUKS_AUTH_ACCESS_INVALID_CLEAR_PASSWORD
  },
  {
    tag: huks.HuksTag.HUKS_TAG_CHALLENGE_TYPE,
    value: huks.HuksChallengeType.HUKS_CHALLENGE_TYPE_NORMAL
  },
  {
    tag: huks.HuksTag.HUKS_TAG_KEY_AUTH_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
  }
];

function generateKeyItem(keyAlias: string, huksOptions: huks.HuksOptions, throwObject: ThrowObject): Promise<void> {
  return new Promise<void>((resolve, reject) => {
    try {
      huks.generateKeyItem(keyAlias, huksOptions, (error, data) => {
        if (error) {
          reject(error);
        } else {
          resolve(data);
        }
      });
    } catch (error) {
      throwObject.isThrow = true;
      const err = error instanceof Error ? error : new Error(String(error));
      throw err;
    }
  });
}

/* 生成SM4密钥 */
async function step1GenerateKey(): Promise<void> {
  const generateOptions: huks.HuksOptions = {
    properties: KEY_GENERATION_PROPERTIES,
    inData: new Uint8Array([])
  };

  let throwObject: ThrowObject = { isThrow: true };
  try {
    await generateKeyItem(KEY_ALIAS, generateOptions, throwObject)
      .then((data) => {
        console.info(`密钥生成成功: ${JSON.stringify(data)}`);
      })
      .catch((error: Error) => {
        if (throwObject.isThrow) {
          const err = error instanceof Error ? error : new Error(String(error));
          throw err;
        } else {
          console.error(`密钥生成失败: ${JSON.stringify(error)}`);
        }
      });
  } catch (error) {
    console.error(`密钥生成参数无效: ${JSON.stringify(error)}`);
    const err = error instanceof Error ? error : new Error(String(error));
    throw err;
  }
}

/* 步骤2：加密模块 */
const ENCRYPTION_PROPERTIES: huks.HuksParam[] = [
  {
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_SM4,
  },
  {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT,
  },
  {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_SM4_KEY_SIZE_128,
  },
  {
    tag: huks.HuksTag.HUKS_TAG_PADDING,
    value: huks.HuksKeyPadding.HUKS_PADDING_NONE,
  },
  {
    tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
    value: huks.HuksCipherMode.HUKS_MODE_CBC,
  },
  {
    tag: huks.HuksTag.HUKS_TAG_IV,
    value: stringToUint8Array(IV),
  }
];

function initEncryptSession(keyAlias: string, huksOptions: huks.HuksOptions,
  throwObject: ThrowObject): Promise<huks.HuksSessionHandle> {
  return new Promise<huks.HuksSessionHandle>((resolve, reject) => {
    try {
      huks.initSession(keyAlias, huksOptions, (error, data) => {
        if (error) {
          reject(error);
        } else {
          resolve(data);
        }
      });
    } catch (error) {
      throwObject.isThrow = true;
      const err = error instanceof Error ? error : new Error(String(error));
      throw err;
    }
  });
}

function finishEncryptSession(handle: number, huksOptions: huks.HuksOptions,
  throwObject: ThrowObject): Promise<huks.HuksReturnResult> {
  return new Promise<huks.HuksReturnResult>((resolve, reject) => {
    try {
      huks.finishSession(handle, huksOptions, (error, data) => {
        if (error) {
          reject(error);
        } else {
          resolve(data);
        }
      });
    } catch (error) {
      throwObject.isThrow = true;
      const err = error instanceof Error ? error : new Error(String(error));
      throw err;
    }
  });
}

/* 加密数据 */
async function step2EncryptData(): Promise<void> {
  const encryptOptions: huks.HuksOptions = {
    properties: ENCRYPTION_PROPERTIES,
    inData: new Uint8Array([])
  };

  /* 初始化加密会话 */
  let throwObject: ThrowObject = { isThrow: true };
  try {
    await initEncryptSession(KEY_ALIAS, encryptOptions, throwObject)
      .then((data) => {
        console.info(`加密会话初始化成功: ${JSON.stringify(data)}`);
        sessionHandle = data.handle as number;
        challenge = data.challenge as Uint8Array;
      })
      .catch((error: Error) => {
        if (throwObject.isThrow) {
          const err = error instanceof Error ? error : new Error(String(error));
          throw err;
        } else {
          console.error(`加密会话初始化失败: ${JSON.stringify(error)}`);
        }
      });
  } catch (error) {
    console.error(`加密会话初始化参数无效: ${JSON.stringify(error)}`);
    const err = error instanceof Error ? error : new Error(String(error));
    throw err;
  }

  /* 执行加密操作 */
  encryptOptions.inData = stringToUint8Array(CIPHER_IN_DATA);
  throwObject = { isThrow: true };
  try {
    await finishEncryptSession(sessionHandle, encryptOptions, throwObject)
      .then((data) => {
        encryptedData = data.outData as Uint8Array;
        console.info(`数据加密成功: ${JSON.stringify(data)}`);
      })
      .catch((error: Error) => {
        if (throwObject.isThrow) {
          const err = error instanceof Error ? error : new Error(String(error));
          throw err;
        } else {
          console.error(`数据加密失败: ${JSON.stringify(error)}`);
        }
      });
  } catch (error) {
    console.error(`数据加密参数无效: ${JSON.stringify(error)}`);
    const err = error instanceof Error ? error : new Error(String(error));
    throw err;
  }
}
```

### 用户认证

```typescript
/* 步骤3：用户认证模块 */
function performUserAuthentication(huksChallenge: Uint8Array): void {
  /* 配置认证参数 */
  const authTypeList: userAuth.UserAuthType[] = [AUTH_TYPE];
  const authParam: userAuth.AuthParam = {
    challenge: huksChallenge,
    authType: authTypeList,
    authTrustLevel: AUTH_TRUST_LEVEL
  };

  const widgetParam: userAuth.WidgetParam = {
    title: 'PIN',
  };

  /* 获取认证实例 */
  let auth: userAuth.UserAuthInstance;
  try {
    auth = userAuth.getUserAuthInstance(authParam, widgetParam);
    console.info('认证实例获取成功');
  } catch (error) {
    console.error('认证实例获取失败: ' + JSON.stringify(error));
    const err = error instanceof Error ? error : new Error(String(error));
    throw err;
  }

  /* 订阅认证结果 */
  try {
    auth.on('result', {
      onResult(result) {
        console.info('用户认证成功，获取到token: ' + JSON.stringify(result));
        authToken = result.token;
        step32CompleteDecryption();
      }
    });
    console.info('认证结果订阅成功');
  } catch (error) {
    console.error('认证结果订阅失败: ' + JSON.stringify(error));
    const err = error instanceof Error ? error : new Error(String(error));
    throw err;
  }

  try {
    auth.start();
    console.info('认证流程已启动，等待用户输入PIN码...');
  } catch (error) {
    console.error('认证启动失败: ' + JSON.stringify(error));
    const err = error instanceof Error ? error : new Error(String(error));
    throw err;
  }
}
```

### 数据解密和验证

```typescript
/* 步骤4：解密模块 */
const DECRYPTION_PROPERTIES: huks.HuksParam[] = [
  {
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_SM4,
  },
  {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT,
  },
  {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_SM4_KEY_SIZE_128,
  },
  {
    tag: huks.HuksTag.HUKS_TAG_PADDING,
    value: huks.HuksKeyPadding.HUKS_PADDING_NONE,
  },
  {
    tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
    value: huks.HuksCipherMode.HUKS_MODE_CBC,
  },
  {
    tag: huks.HuksTag.HUKS_TAG_IV,
    value: stringToUint8Array(IV),
  }
];

function initDecryptSession(keyAlias: string, huksOptions: huks.HuksOptions,
  throwObject: ThrowObject): Promise<huks.HuksSessionHandle> {
  return new Promise<huks.HuksSessionHandle>((resolve, reject) => {
    try {
      huks.initSession(keyAlias, huksOptions, (error, data) => {
        if (error) {
          reject(error);
        } else {
          resolve(data);
        }
      });
    } catch (error) {
      throwObject.isThrow = true;
      const err = error instanceof Error ? error : new Error(String(error));
      throw err;
    }
  });
}

function finishDecryptSession(handle: number, huksOptions: huks.HuksOptions, token: Uint8Array,
  throwObject: ThrowObject): Promise<huks.HuksReturnResult> {
  return new Promise<huks.HuksReturnResult>((resolve, reject) => {
    try {
      huks.finishSession(handle, huksOptions, token, (error, data) => {
        if (error) {
          reject(error);
        } else {
          resolve(data);
        }
      });
    } catch (error) {
      throwObject.isThrow = true;
      const err = error instanceof Error ? error : new Error(String(error));
      throw err;
    }
  });
}

/* 初始化解密会话并触发用户认证 */
async function step31DecryptionAndAuth(): Promise<void> {

  const decryptOptions: huks.HuksOptions = {
    properties: DECRYPTION_PROPERTIES,
    inData: new Uint8Array([])
  };

  /* 初始化解密会话，获取挑战值 */
  let throwObject: ThrowObject = { isThrow: true };
  try {
    await initDecryptSession(KEY_ALIAS, decryptOptions, throwObject)
      .then((data) => {
        console.info(`解密会话初始化成功: ${JSON.stringify(data)}`);
        sessionHandle = data.handle as number;
        challenge = data.challenge as Uint8Array;
        console.info('获取到挑战值: ' + challenge.toString());

        /* 触发用户认证流程 */
        performUserAuthentication(challenge);
      })
      .catch((error: Error) => {
        if (throwObject.isThrow) {
          const err = error instanceof Error ? error : new Error(String(error));
          throw err;
        } else {
          console.error(`解密会话初始化失败: ${JSON.stringify(error)}`);
        }
      });
  } catch (error) {
    console.error(`解密会话初始化参数无效: ${JSON.stringify(error)}`);
    const err = error instanceof Error ? error : new Error(String(error));
    throw err;
  }
}

/* 完成解密操作 */
async function step32CompleteDecryption(): Promise<void> {
  const decryptOptions: huks.HuksOptions = {
    properties: DECRYPTION_PROPERTIES,
    inData: encryptedData // 使用之前加密的密文
  };

  let throwObject: ThrowObject = { isThrow: true };
  try {
    await finishDecryptSession(sessionHandle, decryptOptions, authToken, throwObject)
      .then((data) => {
        decryptedData = data.outData as Uint8Array;
        console.info(`数据解密成功: ${JSON.stringify(data)}`);

        /* 验证解密结果 */
        const originalData = stringToUint8Array(CIPHER_IN_DATA);
        if (decryptedData.toString() === originalData.toString()) {
          console.info('解密验证成功！解密后的数据与原始明文一致');
        } else {
          console.error('解密验证失败！解密后的数据与原始明文不一致');
        }
      })
      .catch((error: BusinessError) => {
        if (throwObject.isThrow) {
          const err = error instanceof Error ? error : new Error(String(error));
          throw err;
        } else {
          console.error(`数据解密失败: ${JSON.stringify(error)}`);
        }
      });
  } catch (error) {
    console.error(`数据解密参数无效: ${JSON.stringify(error)}`);
    const err = error instanceof Error ? error : new Error(String(error));
    throw err;
  }
}

/* 主函数：执行完整的SM4加密解密流程 */
async function main(): Promise<void> {
    /* 步骤1：生成密钥 */
    await step1GenerateKey();
    /* 步骤2：加密数据 */
    await step2EncryptData();
    /* 步骤3：初始化解密并进行用户认证 */
    await step31DecryptionAndAuth();
}
```
