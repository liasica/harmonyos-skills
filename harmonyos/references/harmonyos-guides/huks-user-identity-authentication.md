---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-user-identity-authentication
title: 用户身份认证访问控制开发指导
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 密钥使用 > 访问控制 > 用户身份认证访问控制开发指导
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:32+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:8575ea01bc99f5e3e95405053d299a4d9b80fd9a2292e02116c483ea8ba3545c
---

场景介绍及相关概念说明请参考[用户身份认证访问控制简介](huks-identity-authentication-overview.md)。

## 开发步骤

### 生成密钥

指定指纹访问控制类型及相关属性。

生成或导入密钥时，在密钥属性集中需指定三个参数：用户认证类型[HuksUserAuthType](../harmonyos-references/js-apis-huks.md#huksuserauthtype9)、授权访问类型[HuksAuthAccessType](../harmonyos-references/js-apis-huks.md#huksauthaccesstype9)、挑战值类型[HuksChallengeType](../harmonyos-references/js-apis-huks.md#hukschallengetype9)。

## 开发案例

```typescript
import { huks } from '@kit.UniversalKeystoreKit';
import { userAuth } from '@kit.UserAuthenticationKit';

const KEY_ALIAS = 'test_sm4_key_alias';
const IV = '1234567890123456';
const CIPHER_IN_DATA = 'Hks_SM4_Cipher_Test_101010101010101010110_string';
const AUTH_TYPE = userAuth.UserAuthType.PIN;
const AUTH_TRUST_LEVEL = userAuth.AuthTrustLevel.ATL1;

let sessionHandle: number;
let challenge: Uint8Array;
let authToken: Uint8Array;
let encryptedData: Uint8Array;

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
    value: huks.HuksKeyAlg.HUKS_ALG_SM4
  },
  {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT | huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
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
  }
];

/* 生成密钥 */
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
        console.info('密钥生成成功');
      })
      .catch((error: Error) => {
        if (throwObject.isThrow) {
          const err = error instanceof Error ? error : new Error(String(error));
          throw err;
        } else {
          console.error('密钥生成失败: ' + JSON.stringify(error));
        }
      });
  } catch (error) {
    console.error('密钥生成参数错误: ' + JSON.stringify(error));
    const err = error instanceof Error ? error : new Error(String(error));
    throw err;
  }
}

/* 步骤2：初始化会话模块 - 初始化加密会话并获取挑战值 */
const INIT_SESSION_PROPERTIES: huks.HuksParam[] = [
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
    tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
    value: huks.HuksCipherMode.HUKS_MODE_CBC,
  },
  {
    tag: huks.HuksTag.HUKS_TAG_PADDING,
    value: huks.HuksKeyPadding.HUKS_PADDING_NONE,
  },
  {
    tag: huks.HuksTag.HUKS_TAG_IV,
    value: stringToUint8Array(IV),
  }
];

/* 初始化会话 */
function initSession(keyAlias: string, huksOptions: huks.HuksOptions,
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

/* 初始化会话并获取挑战值 */
async function step2InitSession(): Promise<void> {
  const initOptions: huks.HuksOptions = {
    properties: INIT_SESSION_PROPERTIES,
    inData: new Uint8Array([])
  };

  let throwObject: ThrowObject = { isThrow: true };
  try {
    await initSession(KEY_ALIAS, initOptions, throwObject)
      .then((data) => {
        sessionHandle = data.handle;
        challenge = data.challenge as Uint8Array;
        console.info('会话初始化成功，挑战值: ' + challenge.toString());
      })
      .catch((error: Error) => {
        if (throwObject.isThrow) {
          const err = error instanceof Error ? error : new Error(String(error));
          throw err;
        } else {
          console.error('会话初始化失败: ' + JSON.stringify(error));
        }
      });
  } catch (error) {
    console.error('会话初始化参数错误: ' + JSON.stringify(error));
    const err = error instanceof Error ? error : new Error(String(error));
    throw err;
  }
}
```

### 通过PIN码认证获取授权令牌

```typescript
/* 步骤3：用户认证模块 - 通过PIN码认证获取授权令牌 */
/* 执行用户认证 */
function performUserAuthentication(huksChallenge: Uint8Array): void {
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
    console.info('认证实例创建成功');
  } catch (error) {
    console.error('认证实例创建失败: ' + JSON.stringify(error));
    const err = error instanceof Error ? error : new Error(String(error));
    throw err;
  }

  /* 订阅认证结果 */
  try {
    auth.on('result', {
      onResult(result) {
        console.info('用户认证成功，获取到令牌');
        authToken = result.token;
        step4EncryptWithToken();
      }
    });
    console.info('认证结果订阅成功');
  } catch (error) {
    console.error('认证结果订阅失败: ' + JSON.stringify(error));
    const err = error instanceof Error ? error : new Error(String(error));
    throw err;
  }

  /* 开始认证 */
  try {
    auth.start();
    console.info('等待用户输入PIN码');
  } catch (error) {
    console.error('认证启动失败: ' + JSON.stringify(error));
    const err = error instanceof Error ? error : new Error(String(error));
    throw err;
  }
}
```

### 使用认证令牌进行加密操作

```typescript
/* 步骤4：加密操作模块 - 使用认证令牌进行加密操作 */
/* 加密参数配置 */
const ENCRYPT_PROPERTIES: huks.HuksParam[] = [
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

/* 更新会话 */
function updateSession(handle: number, huksOptions: huks.HuksOptions, token: Uint8Array,
  throwObject: ThrowObject): Promise<huks.HuksReturnResult> {
  return new Promise<huks.HuksReturnResult>((resolve, reject) => {
    try {
      huks.updateSession(handle, huksOptions, token, (error, data) => {
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

/* 完成会话 */
function finishSession(handle: number, huksOptions: huks.HuksOptions, token: Uint8Array,
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

/* 使用认证令牌进行加密 */
async function step4EncryptWithToken(): Promise<void> {
  const encryptOptions: huks.HuksOptions = {
    properties: ENCRYPT_PROPERTIES,
    inData: stringToUint8Array(CIPHER_IN_DATA)
  };

  /* 更新会话，传入认证令牌 */
  let throwObject: ThrowObject = { isThrow: true };
  try {
    await updateSession(sessionHandle, encryptOptions, authToken, throwObject)
      .then((data) => {
        console.info('会话更新成功');
      })
      .catch((error: Error) => {
        if (throwObject.isThrow) {
          const err = error instanceof Error ? error : new Error(String(error));
          throw err;
        } else {
          console.error('会话更新失败: ' + JSON.stringify(error));
        }
      });
  } catch (error) {
    console.error('会话更新参数错误: ' + JSON.stringify(error));
    const err = error instanceof Error ? error : new Error(String(error));
    throw err;
  }

  /* 完成会话，传入认证令牌 */
  throwObject = { isThrow: false };
  try {
    await finishSession(sessionHandle, encryptOptions, authToken, throwObject)
      .then((data) => {
        encryptedData = data.outData as Uint8Array;
        console.info('加密完成');

        /* 验证加密结果 */
        const originalData = stringToUint8Array(CIPHER_IN_DATA);
        if (encryptedData.toString() === originalData.toString()) {
          console.error('加密验证失败：加密数据与原始数据相同');
        } else {
          console.info('加密验证成功：数据已正确加密');
        }
      })
      .catch((error: Error) => {
        if (throwObject.isThrow) {
          const err = error instanceof Error ? error : new Error(String(error));
          throw err;
        } else {
          console.error('会话完成失败: ' + JSON.stringify(error));
        }
      });
  } catch (error) {
    console.error('会话完成参数错误: ' + JSON.stringify(error));
    const err = error instanceof Error ? error : new Error(String(error));
    throw err;
  }
}

/* 主流程入口 - 执行完整的密钥生成、认证和加密流程 */
async function main(): Promise<void> {
  await step1GenerateKey();
  await step2InitSession();
  performUserAuthentication(challenge);
}
```
