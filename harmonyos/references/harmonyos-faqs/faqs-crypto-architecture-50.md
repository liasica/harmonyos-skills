---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-50
title: HMAC使用用户身份认证控制访问
breadcrumb: FAQ > 系统开发 > 安全 > 加解密算法（Crypto Architecture） > HMAC使用用户身份认证控制访问
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:35+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:64caac94b161286a81520fc8e29912d23acb2937d33d0ceb89bb68514036a918
---

## 问题现象

Universal Keystore Kit中HMAC(ArkTS)算法是否支持添加用户身份认证访问控制？

在加解密中加上用户身份认证可以正常运行，但是加到HMAC就报错，HMAC与用户身份认证的文档都没有明确说明支持还是不支持？

## 背景知识

[HMAC(ArkTS)](../harmonyos-guides/huks-hmac-arkts.md)：密钥相关的哈希运算消息认证码（Hash-based Message Authentication Code）。

[用户身份认证访问控制开发指导](../harmonyos-guides/huks-user-identity-authentication.md)：生成/导入密钥时，可以指定密钥必须经过用户身份认证后才能使用。

## 解决方案

使用HMAC生成密钥：

```ts
// GenerateKey
async function GenerateKey(authAccess: number, challengeType: number, time: number, isFineGrained: boolean) {
  console.info('[HUKS>demo] GenerateKey begin, challengeType:' + challengeType);
  let properties = GetPropertiesDebug(authAccess, challengeType, time, isFineGrained);
  let options: huks.HuksOptions = {
    properties: properties
  };

  let aliasTest: string;
  if (!isFineGrained) {
    aliasTest = alias;
  } else {
    aliasTest = alias2;
  }

  await huks.generateKeyItem(aliasTest, options).then((data) => {
    console.info('[HUKS>demo] GenerateKey Success! Result: ' + JSON.stringify(data));
  }).catch((err: BusinessError) => {
    console.error('[HUKS>demo] GenerateKey Exception: ' + JSON.stringify(err));
  });
}
```

调用用户身份认证访问密钥：

```ts
async function UserAuthBeforeMac(handle: number, options: huks.HuksOptions) {
  let authTypeList: number[] = new Array();

  authTypeList[0] = userIAM_userAuth.UserAuthType.FINGERPRINT; // 指纹认证类型
  console.info('[HUKS] -> [IAM] auth Check START!!! userAuthType:[' + authTypeList + '] authTypeList: ' + authTypeList +
    '  challenge : ' + challengeData);
  const authParam: userIAM_userAuth.AuthParam = {
    challenge: challengeData,
    authType: authTypeList,
    authTrustLevel: userIAM_userAuth.AuthTrustLevel.ATL1
  };
  const widgetParam: userIAM_userAuth.WidgetParam = {
    title: '请输入密码',
  };
  try {
    console.info('[HUKS] -> [IAM] auth start ...');
    let userAuthInstance = await userIAM_userAuth.getUserAuthInstance(authParam, widgetParam);
    console.info('[HUKS] -> [IAM] get userAuth instance success');

    userAuthInstance.on('result', {
      onResult(result) {
        console.info('[HUKS] -> [IAM]  userAuthInstance callback result = ' + JSON.stringify(result));
        authTokenData = result.token;
        selfFinishSession(handle, options);
      }
    });
    userAuthInstance.start();
    console.info('[HUKS] -> [IAM] auth on success');
  } catch (error) {
    console.info('[HUKS] -> [IAM] auth catch error: ' + JSON.stringify(error));
  }
}
```

完整示例代码如下：

```ts
import huks from '@ohos.security.huks';
import userIAM_userAuth from '@ohos.userIAM.userAuth';
import { BusinessError } from '@ohos.base';

let alias = 'test_alias';
let alias2 = 'test_alias2';
let accessIndex: number = 2;
let challengeTypeIndex: number = 0;
let handle: number = 0;
let challengeData: Uint8Array;
let authTokenData: Uint8Array;
let plainText = 'hello_wxt';

function StringToUint8Array(str: string) {
  let arr: number[] = new Array();
  for (let i = 0, j = str.length; i < j; ++i) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

function GetPropertiesDebug(authAccess: number, challengeType: number, time: number, isFineGrained: boolean) {
  console.info('[HUKS>demo] GetProperties start...');
  let properties: Array<huks.HuksParam> = new Array();
  let index: number = 0;
  properties[index++] = {
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_HMAC
  };
  properties[index++] = {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: 256
  };
  properties[index++] = {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_MAC
  };
  properties[index++] = {
    tag: huks.HuksTag.HUKS_TAG_DIGEST,
    value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
  };

  let huksAccessType: number = authAccess;
  let timeout: number = time;

  switch (authAccess) {
    case 1:
      huksAccessType = huks.HuksAuthAccessType.HUKS_AUTH_ACCESS_INVALID_CLEAR_PASSWORD;
      break;
    case 2:
      huksAccessType = huks.HuksAuthAccessType.HUKS_AUTH_ACCESS_INVALID_NEW_BIO_ENROLL;
      break;
    case 3:
      huksAccessType = 4; // alwaysValid
      break;
    default:
      huksAccessType = 0;
  }
  properties[index++] = {
    tag: huks.HuksTag.HUKS_TAG_USER_AUTH_TYPE,
    value: huks.HuksUserAuthType.HUKS_USER_AUTH_TYPE_FINGERPRINT
  };
  properties[index++] = {
    tag: huks.HuksTag.HUKS_TAG_KEY_AUTH_ACCESS_TYPE,
    value: huksAccessType
  };
  properties[index++] = {
    tag: huks.HuksTag.HUKS_TAG_CHALLENGE_TYPE,
    value: challengeType
  };
  if (challengeType == huks.HuksChallengeType.HUKS_CHALLENGE_TYPE_CUSTOM) {
    properties[index++] = {
      tag: huks.HuksTag.HUKS_TAG_CHALLENGE_POS,
      value: huks.HuksChallengePosition.HUKS_CHALLENGE_POS_1
    };
  }
  ;
  if (challengeType == huks.HuksChallengeType.HUKS_CHALLENGE_TYPE_NONE) {
    properties[index++] = {
      tag: huks.HuksTag.HUKS_TAG_AUTH_TIMEOUT,
      value: timeout
    };
  }
  ;
  if (isFineGrained) {
    properties[index++] = {
      tag: huks.HuksTag.HUKS_TAG_KEY_AUTH_PURPOSE,
      value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY
    };
  }
  console.info('[HUKS>demo] GetProperties  finish : ');
  return properties;
}

// GenerateKey
async function GenerateKey(authAccess: number, challengeType: number, time: number, isFineGrained: boolean) {
  console.info('[HUKS>demo] GenerateKey begin, challengeType:' + challengeType);
  let properties = GetPropertiesDebug(authAccess, challengeType, time, isFineGrained);
  let options: huks.HuksOptions = {
    properties: properties
  };

  let aliasTest: string;
  if (!isFineGrained) {
    aliasTest = alias;
  } else {
    aliasTest = alias2;
  }

  await huks.generateKeyItem(aliasTest, options).then((data) => {
    console.info('[HUKS>demo] GenerateKey Success! Result: ' + JSON.stringify(data));
  }).catch((err: BusinessError) => {
    console.error('[HUKS>demo] GenerateKey Exception: ' + JSON.stringify(err));
  });
}

// DeleteKey
async function DeleteKey(isFineGrained: boolean) {
  console.info('[HUKS>demo] DeleteKey Begin');
  let emptyOption: huks.HuksOptions = {
    properties: []
  };

  let aliasTest: string;
  if (!isFineGrained) {
    aliasTest = alias;
  } else {
    aliasTest = alias2;
  }

  await huks.deleteKeyItem(aliasTest, emptyOption).then((data) => {
    console.info('[HUKS>demo] DeleteKey Success! Result: ' + JSON.stringify(data));

  }).catch((err: BusinessError) => {
    console.info('[HUKS>demo] DeleteKey Exception: ' + JSON.stringify(err));
  });
}

async function UserAuthBeforeMac(handle: number, options: huks.HuksOptions) {
  let authTypeList: number[] = new Array();

  authTypeList[0] = userIAM_userAuth.UserAuthType.FINGERPRINT; // 指纹认证类型
  console.info('[HUKS] -> [IAM] auth Check START!!! userAuthType:[' + authTypeList + '] authTypeList: ' + authTypeList +
    '  challenge : ' + challengeData);
  const authParam: userIAM_userAuth.AuthParam = {
    challenge: challengeData,
    authType: authTypeList,
    authTrustLevel: userIAM_userAuth.AuthTrustLevel.ATL1
  };
  const widgetParam: userIAM_userAuth.WidgetParam = {
    title: '请输入密码',
  };
  try {
    console.info('[HUKS] -> [IAM] auth start ...');
    let userAuthInstance = await userIAM_userAuth.getUserAuthInstance(authParam, widgetParam);
    console.info('[HUKS] -> [IAM] get userAuth instance success');

    userAuthInstance.on('result', {
      onResult(result) {
        console.info('[HUKS] -> [IAM]  userAuthInstance callback result = ' + JSON.stringify(result));
        authTokenData = result.token;
        selfFinishSession(handle, options);
      }
    });
    userAuthInstance.start();
    console.info('[HUKS] -> [IAM] auth on success');
  } catch (error) {
    console.info('[HUKS] -> [IAM] auth catch error: ' + JSON.stringify(error));
  }
}

async function selfFinishSession(handle: number, options: huks.HuksOptions) {
  console.info('[HUKS>demo] selfFinishSession Begin [' + handle + ']  #***** options: ' + JSON.stringify(options));
  await huks.finishSession(handle, options, authTokenData).then((data) => {
    console.info('[HUKS>demo] Sign() Sign Finish Success! Result: ' + JSON.stringify(data));
  }).catch((err: Error) => {
    console.error('[HUKS>demo] Sign() Sign Finish Exception: ' + JSON.stringify(err));
  });
}

async function Mac(challengeType: number) {
  console.info('[HUKS>demo] Mac Begin, challengeType: ' + challengeType);
  let properties: Array<huks.HuksParam> = new Array();
  let index = 0;
  properties[index++] = {
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_HMAC
  };
  properties[index++] = {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_MAC
  };
  properties[index++] = {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256
  };
  properties[index++] = {
    tag: huks.HuksTag.HUKS_TAG_DIGEST,
    value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
  };
  if (challengeType == huks.HuksChallengeType.HUKS_CHALLENGE_TYPE_CUSTOM) {
    properties[index++] = {
      tag: huks.HuksTag.HUKS_TAG_CHALLENGE_POS,
      value: huks.HuksChallengePosition.HUKS_CHALLENGE_POS_1
    };
  }

  let options: huks.HuksOptions = {
    properties: properties,
    inData: StringToUint8Array(plainText)
  };

  console.info('[HUKS>demo] Mac Init Begin');
  await huks.initSession(alias, options).then((data) => {
    handle = data.handle;
    challengeData = data.challenge as Uint8Array;
    console.info('[HUKS>demo] Mac() Mac Init Success! Result: ', JSON.stringify(data));
  }).catch((err: Error) => {
    console.error('[HUKS>demo] Mac() Mac Init Exception: ', JSON.stringify(err));
  });

  console.info('[HUKS>demo] Mac() Start to UserIAM, Auth Type: Finger');
  await UserAuthBeforeMac(handle, options);
}

@Entry
@Component
struct Index {
  @State message: string = 'Log: \n';
  controller: TextInputController = new TextInputController();
  private authAccessType: string[] = ['None', 'CLEAR_PASSWORD', 'NEW_BIO_ENROLL', 'AlwaysValid'];
  private challengeType: string[] = ['Normal', 'Custom', 'None'];
  private timeout: number = 60; // AuthToken有效期(s)

  build() {
    Column() {
      Row() {
        // AuthAccess类型
        Text('AuthAccess类型:')
          .fontSize(20)
          .margin({ left: 10, top: 10 });
        Select([{ value: this.authAccessType[0] }, { value: this.authAccessType[1] }, { value: this.authAccessType[2] },
          { value: this.authAccessType[3] }])
          .selected(0)
          .font({
            size: 20,
            weight: 400,
            family: 'serif',
            style: FontStyle.Normal
          })
          .selectedOptionFont({
            size: 30,
            weight: 500,
            family: 'serif',
            style: FontStyle.Normal
          })
          .optionFont({
            size: 20,
            weight: 400,
            family: 'serif',
            style: FontStyle.Normal
          })
          .onSelect((index: number, value: string) => {
            this.message += '您选择了AuthAccess类型-' + value + '\n';
            accessIndex = index;
          })
          .margin({ top: 10 });
      };

      // challenge类型
      Row() {
        Text('challenge类型:')
          .fontSize(20)
          .margin({ left: 10, top: 10 });
        Select([{ value: this.challengeType[0] }, { value: this.challengeType[1] }, { value: this.challengeType[2] }])
          .selected(0)
          .font({
            size: 20,
            weight: 400,
            family: 'serif',
            style: FontStyle.Normal
          })
          .selectedOptionFont({
            size: 30,
            weight: 500,
            family: 'serif',
            style: FontStyle.Normal
          })
          .optionFont({
            size: 20,
            weight: 400,
            family: 'serif',
            style: FontStyle.Normal
          })
          .onSelect((index: number, value: string) => {
            this.message += '您选择了challenge类型-' + value + '\n';
            challengeTypeIndex = index;
          })
          .margin({ top: 10 });
      };

      Row() {
        Button({ type: ButtonType.Normal, stateEffect: true }) {
          Text('generateKey')
            .fontSize(20)
            .fontColor(Color.White);
        }
        .borderRadius(8)
        .width('45%')
        .height('5%')
        .backgroundColor(0x317aff)
        .onClick(() => {
          this.message += 'generate key start\n';
          GenerateKey(accessIndex, challengeTypeIndex, this.timeout, false); // 生成密钥
          this.message += 'generate key end\n';
        })
        .margin(10);

        Button({ type: ButtonType.Normal, stateEffect: true }) {
          Text('deleteKey') // 删除密钥
            .fontSize(20)
            .fontColor(Color.White);
        }
        .borderRadius(8)
        .width('45%')
        .height('5%')
        .backgroundColor(0x317aff)
        .onClick(() => {
          this.message += 'delete key start\n';
          DeleteKey(false);
          this.message += 'delete key end\n';
        })
        .margin(10);
      };

      Row() {
        Button({ type: ButtonType.Normal, stateEffect: true }) {
          Text('Mac') // 用户认证获取密钥
            .fontSize(20)
            .fontColor(Color.White);
        }
        .borderRadius(8)
        .width('45%')
        .height('5%')
        .backgroundColor(0x317aff)
        .onClick(() => {
          this.message += 'mac data start\n';
          Mac(challengeTypeIndex);
          this.message += 'mac data end\n';
        })
        .margin(10);
      };

      Row() {
        Text(this.message)
          .fontSize(15)
          .width('100%')
          .margin(10);
      };
    }
    .alignItems(HorizontalAlign.Start);
  }
}
```
