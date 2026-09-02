---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-trustedauth-setpwd
title: 设置数字盾密码
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 数字盾服务 > 数字盾密码管理 > 设置数字盾密码
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:30+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:087dd1b67c308438493260e726dd24a3ff4c86c49fae19a9d1b2726d5631f706
---

## 场景介绍

用户首次激活数字盾时，需通过可信用户交互（全称Trusted User Interface，下文简称TUI）安全界面设置专用密码，后续进行交易认证时，将通过该密码完成安全验证。

## 约束与限制

1. 本功能在6.1.1(24)之前版本仅支持Phone；6.1.1(24)及之后版本，新增支持具备TUI能力的PC/2in1、具备TUI能力的Tablet。可通过接口[checkConfirmUITextFormat](../harmonyos-references/devicesecurity-trusted-auth-api.md#trustedauthenticationcheckconfirmuitextformat)查询设备是否具备TUI能力。
2. 不支持的设备在调用数字盾服务相关业务接口时，返回错误码[1019100016](../harmonyos-references/errorcode-devicesecurity-trusted-auth.md#section1019100016-数字盾服务未使能)。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/T10TCWv-R3aokJZrphO1XA/zh-cn_image_0000002736433445.jpg)

数字盾开通时，需由应用服务器、应用客户端、Universal Keystore Kit和Device Security Kit共同协作完成。流程如下：

1. 应用服务器向应用客户端发起“开通数字盾”申请。
2. 查询设备是否支持TUI能力：应用客户端向Device Security Kit发送请求，查询设备是否具备TUI能力，Device Security Kit返回查询结果。
3. 查询系统支持开通数字盾的最高安全等级：应用客户端再次向Device Security Kit查询系统支持开通数字盾的最高安全等级，Device Security Kit返回查询结果。
4. 生成会话签名密钥：应用客户端使用密钥别名向Universal Keystore Kit请求生成会话密钥，Universal Keystore Kit返回密钥生成结果。
5. 初始化签名会话：应用客户端向Universal Keystore Kit发送“init会话”请求，Universal Keystore Kit返回会话句柄（handle）和challenge。
6. 应用客户端向Device Security Kit发送“开通数字盾申请”，Device Security Kit执行“设置盾密码”操作，并返回开通结果（包含authToken和authID）。
7. 完成update/finish签名操作：应用客户端将获取的authToken和待签名数据发送至Universal Keystore Kit发起认证签名操作，Universal Keystore Kit返回签名信息。
8. 绑定数字盾：应用服务器接收应用客户端返回的签名信息，并完成验签操作，验签通过后将用户账户与数字盾对应的authID、匿名authID绑定关联。

## 接口说明

接口及使用方法请参见[API参考](../harmonyos-references/devicesecurity-trusted-auth-api.md)。

| 接口名 | 描述 |
| --- | --- |
| [checkConfirmUITextFormat](../harmonyos-references/devicesecurity-trusted-auth-api.md#trustedauthenticationcheckconfirmuitextformat)(text: string): Promise<[TextCheckResult](../harmonyos-references/devicesecurity-trusted-auth-api.md#textcheckresult)> | 检查将在TUI呈现的内容是否可以单行完整展示，可间接判断设备是否具备TUI能力。 |
| [getSecurityLevel](../harmonyos-references/devicesecurity-trusted-auth-api.md#trustedauthenticationgetsecuritylevel)(authID?: bigint): Promise<[SecurityLevel](../harmonyos-references/devicesecurity-trusted-auth-api.md#securitylevel)> | 获取当前系统支持开通数字盾的最高安全等级或指定数字盾对应的安全等级。 |
| [enableTrustedAuthentication](../harmonyos-references/devicesecurity-trusted-auth-api.md#trustedauthenticationenabletrustedauthentication)(challenge: Uint8Array, pwdInfo: [PasswordInfo](../harmonyos-references/devicesecurity-trusted-auth-api.md#passwordinfo), label: [TUILable](../harmonyos-references/devicesecurity-trusted-auth-api.md#tuilable)): Promise<AuthInfo> | 创建数字盾密码。 |

## 开通数字盾界面介绍

下图为开通数字盾服务时对应的TUI（Trusted User Interface）界面示例，其中密码长度、对应TUI应用图标以及当前应用场景说明均由开发者调用接口时传入，当设置盾密码长度不符合要求、密码强度低、两次密码设置不一致时，均会有对应失败报错提醒。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/rcssM28HQZ-ilylEAnEQJQ/zh-cn_image_0000002706834290.png)

## 开发步骤

1. 导入相关模块。

   ```typescript
   import { resourceManager } from '@kit.LocalizationKit'
   import { huks } from '@kit.UniversalKeystoreKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { trustedAuthentication } from '@kit.DeviceSecurityKit';
   import { cryptoFramework } from '@kit.CryptoArchitectureKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { common } from '@kit.AbilityKit';
   ```
2. 调用[checkConfirmUITextFormat](../harmonyos-references/devicesecurity-trusted-auth-api.md#trustedauthenticationcheckconfirmuitextformat)接口，判断设备是否具备TUI能力。

   ```typescript
   async isSupportTUI():Promise<boolean> {
     if (canIUse('SystemCapability.Security.TrustedAuthentication')) {
       let text = 'a'; // 任意短字符串。
       try {
         const result = await trustedAuthentication.checkConfirmUITextFormat(text);
         if (result.result == 0) {
           return true;
         }
       } catch (error) {
         hilog.error(DOMAIN, 'testTag', 'The trusted authentication feature is not enabled.');
         return false;
       }
     }
     return false;
   }
   ```
3. 调用[getSecurityLevel](../harmonyos-references/devicesecurity-trusted-auth-api.md#trustedauthenticationgetsecuritylevel)接口，获取当前系统支持开通数字盾的最高安全等级，用于后续指定生成密钥及开通数字盾的安全等级。

   ```typescript
   async getSystemSecurityLevel(): Promise<trustedAuthentication.SecurityLevel> {
     try {
       const securityLevel = await trustedAuthentication.getSecurityLevel();
       hilog.info(0x0000, 'testTag', `The current system supports enabling the highest security level for the digital shield is: ${securityLevel}`);
       return securityLevel;
     } catch (error) {
       hilog.error(0x0000, 'testTag', 'get system securityLevel failed: %{public}d %{public}s',
         (error as BusinessError).code, (error as BusinessError).message);
       throw new Error('get system securityLevel failed: ' + (error as BusinessError).message);
     }
   }
   ```
4. 使用指定的会话密钥别名及指定密钥属性集合完成密钥生成，详细使用指导可参考密钥管理服务提供的[密钥生成开发指导](huks-key-generation-arkts.md)。

   **说明** 

   1、创建密钥时指定密钥属性集合中身份认证类型tag: huks.HuksTag.HUKS\_TAG\_USER\_AUTH\_TYPE时，必须要包括huks.HuksUserAuthType.HUKS\_USER\_AUTH\_TYPE\_TUI\_PIN认证方式，其余认证类型（如人脸或指纹）可以根据业务需要进行定制配置。

   2、若希望应用卸载后保留密钥、重装后继续使用，需使用密钥加密导出/导入功能，并在生成密钥时设置HUKS\_TAG\_IS\_ALLOWED\_WRAP指定密钥允许导出。

   3、当使用SE级别数字盾时，密钥也需要指定为SE级别，只需要申请[ohos.permission.ACCESS\_SE\_KEY](restricted-permissions.md#ohospermissionaccess_se_key)权限，并在生成或导入密钥时添加tag: huks.HuksTag.HUKS\_TAG\_KEY\_SECURITY\_LEVEL，值设置为huks.HuksKeySecurityLevel.HUKS\_KEY\_SECURITY\_LEVEL\_SE，使用密钥时无需指定。SE级别密钥与TEE级别密钥的使用规格存在差异，详见[SE级别密钥规格介绍](devicesecurity-trustedauth-setpwd.md#se与tee安全级别密钥规格差异)。

   ```typescript
    async TestGenKeyForTuiPinSign(): Promise<void> {
      let properties: Array<huks.HuksParam> = [{
        tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
        value: huks.HuksKeyAlg.HUKS_ALG_ECC
      }, {
        tag: huks.HuksTag.HUKS_TAG_PURPOSE,
        value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN | huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY
      }, {
        tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
        value: huks.HuksKeySize.HUKS_ECC_KEY_SIZE_256
      }, {
        tag: huks.HuksTag.HUKS_TAG_DIGEST,
        value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
      }, {
        tag: huks.HuksTag.HUKS_TAG_KEY_AUTH_PURPOSE,
        value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN
      },
      // 指定密钥身份认证的类型：TUI_PIN/指纹/人脸
      {
        tag: huks.HuksTag.HUKS_TAG_USER_AUTH_TYPE,
        value: huks.HuksUserAuthType.HUKS_USER_AUTH_TYPE_TUI_PIN | huks.HuksUserAuthType.HUKS_USER_AUTH_TYPE_FINGERPRINT |
        huks.HuksUserAuthType.HUKS_USER_AUTH_TYPE_FACE
      },
      // 指定密钥安全授权的类型（失效类型）：新录入生物特征（如指纹）后无效
      {
        tag: huks.HuksTag.HUKS_TAG_KEY_AUTH_ACCESS_TYPE,
        value: huks.HuksAuthAccessType.HUKS_AUTH_ACCESS_ALWAYS_VALID
      },
      // 指定挑战值的类型：默认类型
      {
        tag: huks.HuksTag.HUKS_TAG_CHALLENGE_TYPE,
        value: huks.HuksChallengeType.HUKS_CHALLENGE_TYPE_NORMAL
      },
      /* 允许导出密钥，用于后续密钥备份场景 */
      {
        tag: huks.HuksTag.HUKS_TAG_IS_ALLOWED_WRAP,
        value: true
      }];
      let huksOptions: huks.HuksOptions = {
        properties: properties,
        inData: new Uint8Array(new Array())
      }
      await publicGenKeyFunc(KEY_ALIAS, huksOptions);
    }
   ```
5. 初始化签名会话，详细使用指导可参考密钥管理服务提供的[签名/验签指导](huks-signing-signature-verification-arkts.md)。
6. 调用设置密码接口，发起数字盾密码创建申请。

   **说明** 

   开通数字盾的安全等级需与第4步生成密钥的安全等级保持一致，依据第3步获取的最高安全等级进行选择。

   * 指定开通SE级别数字盾时，需在第4步生成SE安全等级的密钥，并在调用[enableTrustedAuthentication](../harmonyos-references/devicesecurity-trusted-auth-api.md#trustedauthenticationenabletrustedauthentication)时，通过PasswordInfo的securityLevel字段指定为trustedAuthentication.SecurityLevel.SECURITY\_LEVEL\_SE。
   * 在不支持开通SE安全级别的设备上指定开通SE安全级别数字盾时，返回错误码801。
   * 隐私空间下仅支持开通TEE安全级别数字盾。
   * 如果因为硬件老化等原因出现SE芯片故障，调用对应接口返回错误码[1019100023](../harmonyos-references/errorcode-devicesecurity-trusted-auth.md#section1019100023-安全器件故障)，开发者可根据业务需要关闭数字盾，并指定生成TEE安全级别密钥，并开通TEE安全等级数字盾。

   ```typescript
   async SetPwd(challenge: Uint8Array, assetName: string): Promise<trustedAuthentication.AuthInfo> {
     try {
       const passwordInfo: trustedAuthentication.PasswordInfo = {
         pwdType: trustedAuthentication.PasswordType.PASSWORD_TYPE_DIGITAL,
         pwdMaxLength: 10,
         pwdMinLength: 6,
         maxAuthFailCount: 6
       };
       const context = AppStorage.get('context') as Context;
       const buffer: ArrayBuffer = await CryptoUtils.ImportImage(); // 获取应用要在TUI界面展示的logo图片
       const label: trustedAuthentication.TUILable = {
         image: buffer,
         title: context.resourceManager.getStringSync($r('app.string.OpenShield').id)
       }
       const authInfo = await trustedAuthentication.enableTrustedAuthentication(challenge, passwordInfo, label);
       let assetLabel = assetName + 'label';
       AssetUtils.AddDataToAssetStore(CryptoUtils.bigIntToUint8Array(authInfo.authID), assetName, assetLabel);
       hilog.info(0x0000, 'testTag', 'Open Shield Success：', authInfo.authID, authInfo.authToken.length,
         authInfo.authToken);
       return authInfo;
     } catch (error) {
       hilog.error(0x0000, 'testTag', 'Open Shield Fail：', error);
       throw new Error('Open Shield Fail：' + (error as BusinessError).message);
     }
   }
   ```
7. 参考密钥管理服务提供的[签名/验签指导](huks-signing-signature-verification-arkts.md)，使用第6步获取的authToken完成认证签名操作（initSession已在第5步完成），并结束会话。

   **说明** 

   * 数字盾签名场景为保障端到端安全性，应用服务器需在验签时感知authToken解析出的认证信息，因此签名时必须选择**携带认证信息**的签名类型（HUKS\_KEY\_PURPOSE\_SIGN且HUKS\_TAG\_KEY\_SECURE\_SIGN\_TYPE为HUKS\_SECURE\_SIGN\_WITH\_AUTHINFO）。该类型签名会在原始待签名数据之前自动附加41字节的认证信息后，再进行签名操作。
   * 签名返回数据的整体结构为：**41字节认证信息 + 原始数据签名值**。开发者需将签名的完整返回数据（含前置41字节认证信息）上送至应用服务器进行验签。
   * 应用服务器解析签名数据时，需先按上述偏移关系从签名数据中切分出前置41字节认证信息与签名值，并对签名值进行验签；验签通过后，可从认证信息中提取匿名化AuthId等字段，用于将用户账户与数字盾对应的authID、匿名化AuthId进行绑定关联（对应业务流程中的第8步）。
   * 41字节认证信息的具体含义及解析方式，与[携带认证信息的签名类型指导](huks-signing-signature-verification-overview.md#携带认证信息的签名类型)保持一致。

   * 签名返回数据（signature）整体结构如下表所示：

   | 数据段 | 字段 | 偏移（字节） | 长度（字节） | 说明 |
   | --- | --- | --- | --- | --- |
   | 认证信息 | 版本号 | 0 | 4 | 认证信息版本号。 |
   | 认证信息 | 用户认证类型 | 4 | 4 | 认证采用的用户认证类型（如TUI\_PIN、人脸、指纹等）。 |
   | 认证信息 | 匿名化AuthId | 8 | 32 | 数字盾的匿名化AuthId，用于服务器侧绑定账户。 |
   | 认证信息 | 是否校验数据哈希 | 40 | 1 | 原数据是否进行了数据哈希校验，涉及TUI显示内容防篡改保护时，取值1表示需校验。 |
   | 签名值 | 原始数据的签名值 | 41 | - | 对待签名原始数据（含前置认证信息）生成的签名值。 |

## SE与TEE安全级别密钥规格差异

从API 26.0.0起，数字盾服务支持开通SE安全级别的数字盾，开通前需指定生成SE安全级别密钥。与TEE安全级别密钥不同，SE密钥在独立的安全芯片中生成和使用，提供更高级别的安全防护。如需使用SE密钥，需显式指定[密钥安全级别](../harmonyos-references/js-apis-huks.md#hukskeysecuritylevel)。

### 约束与限制

* SE安全级别密钥依赖安全芯片，请先[查询设备硬件是否支持](../harmonyos-references/devicesecurity-trusted-auth-api.md#trustedauthenticationgetsecuritylevel)。
* 使用SE安全级别密钥需要申请权限[ohos.permission.ACCESS\_SE\_KEY](restricted-permissions.md#ohospermissionaccess_se_key)。
* SE安全级别密钥当前仅支持SM2、SM4算法，使用方式和规格与TEE安全级别密钥基本一致。但受资源限制，输入数据长度和会话并发数量与TEE级别不同，详细规格请查看[支持的接口及规格](devicesecurity-trustedauth-setpwd.md#支持的接口及规格)。
* SE安全级别密钥仅支持数字信封导入密钥，不支持明文导入密钥。
* SE密钥的生成与使用接口最大支持4路并发，超过此限制将返回繁忙错误。
* 使用SE密钥时仅支持单会话。若应用已创建SE会话，再次创建SE会话将覆盖原有会话，会话超时时间为120秒。当有应用正在使用未过期的SE会话时，其他应用创建SE会话会因会话超限而报错，需稍后重试。

### 支持的接口及规格

SE安全级别密钥支持以下HUKS接口：

**说明** 

只有生成密钥、安全导入密钥、加密导入密钥时需要指定SE安全级别，其他使用密钥接口无需指定。

| 接口 | 规格 | 说明 |
| --- | --- | --- |
| 密钥生成（[generateKeyItem](../harmonyos-references/js-apis-huks.md#huksgeneratekeyitem9-1)） | 仅支持SM2、SM4算法。 | 需要指定SE安全级别。支持群组密钥。 |
| 密钥删除（[deleteKeyItem](../harmonyos-references/js-apis-huks.md#huksdeletekeyitem9-1)） | - | 无需指定SE安全级别。 |
| 密钥查询（[getKeyItemProperties](../harmonyos-references/js-apis-huks.md#huksgetkeyitemproperties9-1)） | - | 无需指定SE安全级别。 |
| 导出公钥（[exportKeyItem](../harmonyos-references/js-apis-huks.md#huksexportkeyitem9-1)） | - | 无需指定SE安全级别。 |
| 安全导入密钥（[importWrappedKeyItem](../harmonyos-references/js-apis-huks.md#huksimportwrappedkeyitem9-1)） | 仅支持数字信封模式（[HUKS\_UNWRAP\_SUITE\_SM2\_SM4\_ECB\_NOPADDING](../harmonyos-references/js-apis-huks.md#huksunwrapsuite9)）。 | 密钥加密密钥（KEK）与待导入密钥的安全级别必须匹配。 |
| 加密导出导入密钥（[wrapKeyItem](../harmonyos-references/js-apis-huks.md#hukswrapkeyitem20)/[unwrapKeyItem](../harmonyos-references/js-apis-huks.md#huksunwrapkeyitem20)） | - | 加密导出密钥与加密导入密钥的安全级别必须匹配。 |
| 密钥使用（[initSession](../harmonyos-references/js-apis-huks.md#huksinitsession9)/[updateSession](../harmonyos-references/js-apis-huks.md#huksupdatesession9)/[finishSession](../harmonyos-references/js-apis-huks.md#huksfinishsession9)/[abortSession](../harmonyos-references/js-apis-huks.md#huksabortsession9-1)） | 详细规格请查看SM2算法规格和SM4算法规格。 | 仅支持加密解密和签名验签，无需指定SE安全级别。 |
| 密钥证明（[anonAttestKeyItem](../harmonyos-references/js-apis-huks.md#huksanonattestkeyitem11-1)） | 仅支持匿名证明。 | 无需指定SE安全级别。 |

**SM2算法规格**

| 算法 | 密钥长度 | 用途 | 摘要算法 | 填充模式 | 数据限制 |
| --- | --- | --- | --- | --- | --- |
| SM2 | 256 | 签名/验签 | SM3 | NoPadding | 输入数据≤512字节 |
| SM2 | 256 | 签名/验签 | NoDigest | NoPadding | 输入数据=32字节 |
| SM2 | 256 | 加密/解密 | SM3 | NoPadding | 数据总大小≤128字节 |

**SM4算法规格**

| 算法 | 密钥长度 | 用途 | 填充模式 | 分组模式 | 数据限制 |
| --- | --- | --- | --- | --- | --- |
| SM4 | 128 | 加密/解密 | PKCS7 | ECB | 单段≤256字节 |
| SM4 | 128 | 加密/解密 | PKCS7 | CBC | 单段≤256字节 |
| SM4 | 128 | 加密/解密 | NoPadding | CTR | 单段≤256字节 |
| SM4 | 128 | 加密/解密 | NoPadding | CBC | 单段≤256字节 |

**说明** 

SE安全级别密钥不支持AES、RSA、ECC算法。不支持SM4的CFB和OFB模式。

### 示例代码

**密钥生成**

使用[generateKeyItem](../harmonyos-references/js-apis-huks.md#huksgeneratekeyitem9-1)接口生成SE安全级别密钥时，需要通过[HUKS\_TAG\_KEY\_SECURITY\_LEVEL](../harmonyos-references/js-apis-huks.md#hukstag)指定安全级别。

```typescript
import { huks } from '@kit.UniversalKeystoreKit';

let keyAlias = 'se_sm2_sign_key';

let properties: huks.HuksParam[] = [
  { tag: huks.HuksTag.HUKS_TAG_ALGORITHM, value: huks.HuksKeyAlg.HUKS_ALG_SM2 },
  { tag: huks.HuksTag.HUKS_TAG_KEY_SIZE, value: huks.HuksKeySize.HUKS_SM2_KEY_SIZE_256 },
  { tag: huks.HuksTag.HUKS_TAG_PURPOSE, value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN | huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY },
  { tag: huks.HuksTag.HUKS_TAG_DIGEST, value: huks.HuksKeyDigest.HUKS_DIGEST_SM3 },
  { tag: huks.HuksTag.HUKS_TAG_KEY_SECURITY_LEVEL, value: huks.HuksKeySecurityLevel.HUKS_KEY_SECURITY_LEVEL_SE },
  { tag: huks.HuksTag.HUKS_TAG_USER_AUTH_TYPE, value: huks.HuksUserAuthType.HUKS_USER_AUTH_TYPE_TUI_PIN },
  { tag: huks.HuksTag.HUKS_TAG_KEY_AUTH_ACCESS_TYPE, value: huks.HuksAuthAccessType.HUKS_AUTH_ACCESS_ALWAYS_VALID },
  { tag: huks.HuksTag.HUKS_TAG_CHALLENGE_TYPE, value: huks.HuksChallengeType.HUKS_CHALLENGE_TYPE_NORMAL },
];

async function testGenerateKey() {
  try {
    await huks.generateKeyItem(keyAlias, { properties: properties });
    console.info('promise: generateKeyItem success');
  } catch (error) {
    console.error('promise: generateKeyItem failed, error: ' + error);
  }
}
```

**密钥删除**

使用[deleteKeyItem](../harmonyos-references/js-apis-huks.md#huksdeletekeyitem9-1)接口删除SE安全级别密钥时，无需指定安全级别参数。

```typescript
import { huks } from '@kit.UniversalKeystoreKit';

let keyAlias = 'se_sm2_sign_key';

let properties: huks.HuksParam[] = [
  { tag: huks.HuksTag.HUKS_TAG_ALGORITHM, value: huks.HuksKeyAlg.HUKS_ALG_SM2 },
  { tag: huks.HuksTag.HUKS_TAG_KEY_SIZE, value: huks.HuksKeySize.HUKS_SM2_KEY_SIZE_256 },
  { tag: huks.HuksTag.HUKS_TAG_PURPOSE, value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN | huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY },
  { tag: huks.HuksTag.HUKS_TAG_DIGEST, value: huks.HuksKeyDigest.HUKS_DIGEST_SM3 },
  { tag: huks.HuksTag.HUKS_TAG_KEY_SECURITY_LEVEL, value: huks.HuksKeySecurityLevel.HUKS_KEY_SECURITY_LEVEL_SE },
  { tag: huks.HuksTag.HUKS_TAG_USER_AUTH_TYPE, value: huks.HuksUserAuthType.HUKS_USER_AUTH_TYPE_TUI_PIN },
  { tag: huks.HuksTag.HUKS_TAG_KEY_AUTH_ACCESS_TYPE, value: huks.HuksAuthAccessType.HUKS_AUTH_ACCESS_ALWAYS_VALID },
  { tag: huks.HuksTag.HUKS_TAG_CHALLENGE_TYPE, value: huks.HuksChallengeType.HUKS_CHALLENGE_TYPE_NORMAL },
];

async function testDeleteKey() {
  try {
    await huks.generateKeyItem(keyAlias, { properties: properties });
    console.info('promise: generateKeyItem success');

    await huks.deleteKeyItem(keyAlias, { properties: [] });
    console.info('promise: deleteKeyItem success');
  } catch (error) {
    console.error('promise: deleteKeyItem failed, error: ' + error);
  }
}
```

**密钥查询**

使用[getKeyItemProperties](../harmonyos-references/js-apis-huks.md#huksgetkeyitemproperties9-1)接口查询SE安全级别密钥属性时，无需指定安全级别参数。

```typescript
import { huks } from '@kit.UniversalKeystoreKit';

let keyAlias = 'se_sm2_sign_key';

let properties: huks.HuksParam[] = [
  { tag: huks.HuksTag.HUKS_TAG_ALGORITHM, value: huks.HuksKeyAlg.HUKS_ALG_SM2 },
  { tag: huks.HuksTag.HUKS_TAG_KEY_SIZE, value: huks.HuksKeySize.HUKS_SM2_KEY_SIZE_256 },
  { tag: huks.HuksTag.HUKS_TAG_PURPOSE, value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN | huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY },
  { tag: huks.HuksTag.HUKS_TAG_DIGEST, value: huks.HuksKeyDigest.HUKS_DIGEST_SM3 },
  { tag: huks.HuksTag.HUKS_TAG_KEY_SECURITY_LEVEL, value: huks.HuksKeySecurityLevel.HUKS_KEY_SECURITY_LEVEL_SE },
  { tag: huks.HuksTag.HUKS_TAG_USER_AUTH_TYPE, value: huks.HuksUserAuthType.HUKS_USER_AUTH_TYPE_TUI_PIN },
  { tag: huks.HuksTag.HUKS_TAG_KEY_AUTH_ACCESS_TYPE, value: huks.HuksAuthAccessType.HUKS_AUTH_ACCESS_ALWAYS_VALID },
  { tag: huks.HuksTag.HUKS_TAG_CHALLENGE_TYPE, value: huks.HuksChallengeType.HUKS_CHALLENGE_TYPE_NORMAL },
];

async function testGetKeyProperties() {
  try {
    await huks.generateKeyItem(keyAlias, { properties: properties });
    console.info('promise: generateKeyItem success');

    let result = await huks.getKeyItemProperties(keyAlias, { properties: [] });
    console.info('promise: getKeyItemProperties success');
  } catch (error) {
    console.error('promise: getKeyItemProperties failed, error: ' + error);
  }
}
```

**导出公钥**

使用[exportKeyItem](../harmonyos-references/js-apis-huks.md#huksexportkeyitem9-1)导出SE安全级别密钥公钥时，无需指定安全级别参数。

```typescript
import { huks } from '@kit.UniversalKeystoreKit';

let keyAlias = 'se_sm2_sign_key';

let properties: huks.HuksParam[] = [
  { tag: huks.HuksTag.HUKS_TAG_ALGORITHM, value: huks.HuksKeyAlg.HUKS_ALG_SM2 },
  { tag: huks.HuksTag.HUKS_TAG_KEY_SIZE, value: huks.HuksKeySize.HUKS_SM2_KEY_SIZE_256 },
  { tag: huks.HuksTag.HUKS_TAG_PURPOSE, value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN | huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY },
  { tag: huks.HuksTag.HUKS_TAG_DIGEST, value: huks.HuksKeyDigest.HUKS_DIGEST_SM3 },
  { tag: huks.HuksTag.HUKS_TAG_KEY_SECURITY_LEVEL, value: huks.HuksKeySecurityLevel.HUKS_KEY_SECURITY_LEVEL_SE },
  { tag: huks.HuksTag.HUKS_TAG_USER_AUTH_TYPE, value: huks.HuksUserAuthType.HUKS_USER_AUTH_TYPE_TUI_PIN },
  { tag: huks.HuksTag.HUKS_TAG_KEY_AUTH_ACCESS_TYPE, value: huks.HuksAuthAccessType.HUKS_AUTH_ACCESS_ALWAYS_VALID },
  { tag: huks.HuksTag.HUKS_TAG_CHALLENGE_TYPE, value: huks.HuksChallengeType.HUKS_CHALLENGE_TYPE_NORMAL },
];

async function testExportKey() {
  try {
    await huks.generateKeyItem(keyAlias, { properties: properties });
    console.info('promise: generateKeyItem success');

    let exportResult = await huks.exportKeyItem(keyAlias, { properties: [] });
    let pubKeyData: Uint8Array = exportResult.outData as Uint8Array;
    console.info('promise: exportKeyItem success, length: ' + pubKeyData.length);
  } catch (error) {
    console.error('promise: exportKeyItem failed, error: ' + error);
  }
}
```

**安全导入密钥**

使用[importWrappedKeyItem](../harmonyos-references/js-apis-huks.md#huksimportwrappedkeyitem9-1)以数字信封格式安全导入SE安全级别密钥时，密钥加密密钥（KEK）与待导入密钥的安全级别必须匹配，详细步骤请参考[数字信封导入密钥(ArkTS)](huks-import-envelop-key-arkts.md)。

```typescript
import { huks } from '@kit.UniversalKeystoreKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

// int转Uint8Array
function intToUint8Array(value: number): Uint8Array {
  let buffer: ArrayBuffer = new ArrayBuffer(4);
  let view: DataView = new DataView(buffer);
  view.setUint32(0, value, true);
  return new Uint8Array(buffer);
}

// 拼接多个Uint8Array
function concatUint8Arrays(arrays: Uint8Array[]): Uint8Array {
  let totalLength: number = 0;
  for (let i = 0; i < arrays.length; i++) {
    totalLength += arrays[i].length;
  }
  let result: Uint8Array = new Uint8Array(totalLength);
  let offset: number = 0;
  for (let i = 0; i < arrays.length; i++) {
    result.set(arrays[i], offset);
    offset += arrays[i].length;
  }
  return result;
}

// 用cryptoFramework通过KEK公钥SM2加密。此加密方式仅作示例，实际应在安全环境中加密
async function encryptSm2WithCryptoFramework(kekAlias: string, plainData: Uint8Array): Promise<Uint8Array> {
  let exportResult: huks.HuksReturnResult = await huks.exportKeyItem(kekAlias, { properties: [] });
  let pubKeyData: Uint8Array = exportResult.outData as Uint8Array;
  let keyGenerator: cryptoFramework.AsyKeyGenerator = cryptoFramework.createAsyKeyGenerator('SM2_256');
  let pubKeyBlob: cryptoFramework.DataBlob = { data: pubKeyData };
  let keyPair: cryptoFramework.KeyPair = await keyGenerator.convertKey(pubKeyBlob, null);
  let cipher: cryptoFramework.Cipher = cryptoFramework.createCipher('SM2_256|SM3');
  await cipher.init(cryptoFramework.CryptoMode.ENCRYPT_MODE, keyPair.pubKey, null);
  let inputBlob: cryptoFramework.DataBlob = { data: plainData };
  let outputBlob: cryptoFramework.DataBlob = await cipher.doFinal(inputBlob);
  return outputBlob.data;
}

// 用SM4-ECB加密密钥材料
async function encryptSm4EcbWithCryptoFramework(transportKey: Uint8Array, plainData: Uint8Array): Promise<Uint8Array> {
  let symKeyGenerator: cryptoFramework.SymKeyGenerator = cryptoFramework.createSymKeyGenerator('SM4_128');
  let keyBlob: cryptoFramework.DataBlob = { data: transportKey };
  let symKey: cryptoFramework.SymKey = await symKeyGenerator.convertKey(keyBlob);
  let cipher: cryptoFramework.Cipher = cryptoFramework.createCipher('SM4_128|ECB|NoPadding');
  await cipher.init(cryptoFramework.CryptoMode.ENCRYPT_MODE, symKey, null);
  let inputBlob: cryptoFramework.DataBlob = { data: plainData };
  let outputBlob: cryptoFramework.DataBlob = await cipher.doFinal(inputBlob);
  return outputBlob.data;
}

async function testImportSm2Key() {
  // 生成KEK密钥
  let kekAlias = 'kek_sm2_sign';
  let kekProps: huks.HuksParam[] = [
    { tag: huks.HuksTag.HUKS_TAG_ALGORITHM, value: huks.HuksKeyAlg.HUKS_ALG_SM2 },
    { tag: huks.HuksTag.HUKS_TAG_KEY_SIZE, value: huks.HuksKeySize.HUKS_SM2_KEY_SIZE_256 },
    { tag: huks.HuksTag.HUKS_TAG_PURPOSE, value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT | huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT },
    { tag: huks.HuksTag.HUKS_TAG_DIGEST, value: huks.HuksKeyDigest.HUKS_DIGEST_SM3 },
    { tag: huks.HuksTag.HUKS_TAG_PADDING, value: huks.HuksKeyPadding.HUKS_PADDING_NONE },
    { tag: huks.HuksTag.HUKS_TAG_KEY_SECURITY_LEVEL, value: huks.HuksKeySecurityLevel.HUKS_KEY_SECURITY_LEVEL_SE },
    { tag: huks.HuksTag.HUKS_TAG_USER_AUTH_TYPE, value: huks.HuksUserAuthType.HUKS_USER_AUTH_TYPE_TUI_PIN },
    { tag: huks.HuksTag.HUKS_TAG_KEY_AUTH_ACCESS_TYPE, value: huks.HuksAuthAccessType.HUKS_AUTH_ACCESS_ALWAYS_VALID },
    { tag: huks.HuksTag.HUKS_TAG_CHALLENGE_TYPE, value: huks.HuksChallengeType.HUKS_CHALLENGE_TYPE_NORMAL },
  ];
  await huks.generateKeyItem(kekAlias, { properties: kekProps });

  // 加密密钥材料并构造导入数据
  let sm2PubKey: Uint8Array = new Uint8Array([0x30, 0x59, 0x30, 0x13, 0x06, 0x07, 0x2a, 0x86, 0x48, 0xce,
    0x3d, 0x02, 0x01, 0x06, 0x08, 0x2a, 0x81, 0x1c, 0xcf, 0x55, 0x01, 0x82, 0x2d, 0x03, 0x42, 0x00,
    0x04, 0x38, 0x9e, 0xd3, 0x95, 0xb7, 0x98, 0xdf, 0x60, 0xbf, 0x5a, 0x14, 0x71, 0x45, 0x2b, 0xd6,
    0xb7, 0x35, 0x1c, 0xd1, 0x38, 0x7a, 0x11, 0x98, 0x8a, 0x28, 0xd1, 0x37, 0x9b, 0x75, 0x12, 0xd8,
    0x06, 0x42, 0xc2, 0xbf, 0x3b, 0x52, 0x18, 0x6e, 0x9c, 0x41, 0x2d, 0x77, 0xc0, 0xa1, 0x6d, 0x9e,
    0x08, 0x9d, 0x4e, 0x16, 0x62, 0x57, 0x97, 0x56, 0x10, 0xd4, 0x7b, 0x3a, 0x5f, 0x96, 0xf6, 0x8c,
    0x19]);
  let sm2PrivKey: Uint8Array = new Uint8Array([0xa7, 0xde, 0x26, 0xf9, 0xe8, 0xad, 0xe8, 0x9b, 0x5a, 0x37,
    0xca, 0x5b, 0x70, 0x18, 0x18, 0xe0, 0x68, 0x04, 0xa9, 0x8b, 0x94, 0x9c, 0xcd, 0x86, 0x90, 0x22,
    0x9f, 0x17, 0xfd, 0xc4, 0x9c, 0x51]);

  let rand: cryptoFramework.Random = cryptoFramework.createRandom();
  let transportKeyBlob: cryptoFramework.DataBlob = await rand.generateRandom(16);
  let transportKey: Uint8Array = transportKeyBlob.data;
  let encTransportKey: Uint8Array = await encryptSm2WithCryptoFramework(kekAlias, transportKey);
  let encKeyData: Uint8Array = await encryptSm4EcbWithCryptoFramework(transportKey, sm2PrivKey);

  let importData: Uint8Array = concatUint8Arrays([
    intToUint8Array(encTransportKey.length), encTransportKey,
    intToUint8Array(encKeyData.length), encKeyData,
  ]);

  // 数字信封导入
  let importAlias = 'imported_sm2_sign';
  let importProps: huks.HuksParam[] = [
    { tag: huks.HuksTag.HUKS_TAG_ALGORITHM, value: huks.HuksKeyAlg.HUKS_ALG_SM2 },
    { tag: huks.HuksTag.HUKS_TAG_KEY_SIZE, value: huks.HuksKeySize.HUKS_SM2_KEY_SIZE_256 },
    { tag: huks.HuksTag.HUKS_TAG_PURPOSE, value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN | huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY },
    { tag: huks.HuksTag.HUKS_TAG_PADDING, value: huks.HuksKeyPadding.HUKS_PADDING_NONE },
    { tag: huks.HuksTag.HUKS_TAG_DIGEST, value: huks.HuksKeyDigest.HUKS_DIGEST_SM3 },
    { tag: huks.HuksTag.HUKS_TAG_UNWRAP_ALGORITHM_SUITE, value: huks.HuksUnwrapSuite.HUKS_UNWRAP_SUITE_SM2_SM4_ECB_NOPADDING },
    { tag: huks.HuksTag.HUKS_TAG_IMPORT_KEY_TYPE, value: huks.HuksImportKeyType.HUKS_KEY_TYPE_KEY_PAIR },
    { tag: huks.HuksTag.HUKS_TAG_ASYMMETRIC_PUBLIC_KEY_DATA, value: sm2PubKey },
    { tag: huks.HuksTag.HUKS_TAG_KEY_SECURITY_LEVEL, value: huks.HuksKeySecurityLevel.HUKS_KEY_SECURITY_LEVEL_SE },
    { tag: huks.HuksTag.HUKS_TAG_USER_AUTH_TYPE, value: huks.HuksUserAuthType.HUKS_USER_AUTH_TYPE_TUI_PIN },
    { tag: huks.HuksTag.HUKS_TAG_KEY_AUTH_ACCESS_TYPE, value: huks.HuksAuthAccessType.HUKS_AUTH_ACCESS_ALWAYS_VALID },
    { tag: huks.HuksTag.HUKS_TAG_CHALLENGE_TYPE, value: huks.HuksChallengeType.HUKS_CHALLENGE_TYPE_NORMAL },
  ];

  try {
    let importOptions: huks.HuksOptions = { properties: importProps, inData: importData };
    await huks.importWrappedKeyItem(importAlias, kekAlias, importOptions);
    console.info('promise: importWrappedKeyItem success');
  } catch (error) {
    console.error('promise: importWrappedKeyItem failed, error: ' + error);
  }
}
```

**加密导出/导入密钥**

使用[wrapKeyItem](../harmonyos-references/js-apis-huks.md#hukswrapkeyitem20)加密导出SE安全级别密钥时，无需参数中指定安全级别，使用[unwrapKeyItem](../harmonyos-references/js-apis-huks.md#huksunwrapkeyitem20)加密导入SE安全级别密钥时，安全级别需要与生成密钥时一致。

```typescript
import { huks } from '@kit.UniversalKeystoreKit';

let keyAlias = 'se_wrap_key';

let properties: huks.HuksParam[] = [
  { tag: huks.HuksTag.HUKS_TAG_ALGORITHM, value: huks.HuksKeyAlg.HUKS_ALG_SM4 },
  { tag: huks.HuksTag.HUKS_TAG_KEY_SIZE, value: huks.HuksKeySize.HUKS_SM4_KEY_SIZE_128 },
  { tag: huks.HuksTag.HUKS_TAG_PURPOSE, value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT | huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT },
  { tag: huks.HuksTag.HUKS_TAG_PADDING, value: huks.HuksKeyPadding.HUKS_PADDING_PKCS7 },
  { tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE, value: huks.HuksCipherMode.HUKS_MODE_CBC },
  { tag: huks.HuksTag.HUKS_TAG_KEY_SECURITY_LEVEL, value: huks.HuksKeySecurityLevel.HUKS_KEY_SECURITY_LEVEL_SE },
  { tag: huks.HuksTag.HUKS_TAG_USER_AUTH_TYPE, value: huks.HuksUserAuthType.HUKS_USER_AUTH_TYPE_TUI_PIN },
  { tag: huks.HuksTag.HUKS_TAG_KEY_AUTH_ACCESS_TYPE, value: huks.HuksAuthAccessType.HUKS_AUTH_ACCESS_ALWAYS_VALID },
  { tag: huks.HuksTag.HUKS_TAG_CHALLENGE_TYPE, value: huks.HuksChallengeType.HUKS_CHALLENGE_TYPE_NORMAL },
  { tag: huks.HuksTag.HUKS_TAG_IS_ALLOWED_WRAP, value: true },
];

let wrapKeyProperties: huks.HuksParam[] = [
  { tag: huks.HuksTag.HUKS_TAG_KEY_WRAP_TYPE, value: huks.HuksKeyWrapType.HUKS_KEY_WRAP_TYPE_HUK_BASED },
];

let wrapKeyOptions: huks.HuksOptions = {
  properties: wrapKeyProperties,
};

let wrappedData: Uint8Array;

async function testWrapKey() {
  try {
    // 生成密钥
    await huks.generateKeyItem(keyAlias, { properties: properties });
    console.info('promise: generateKeyItem success');

    // 加密导出密钥
    let wrapResult = await huks.wrapKeyItem(keyAlias, wrapKeyOptions);
    wrappedData = wrapResult.outData as Uint8Array;
    console.info('promise: wrapKeyItem success, length: ' + wrappedData.length);

    // 加密导入密钥
    await huks.unwrapKeyItem(keyAlias, wrapKeyOptions, wrappedData);
    console.info('promise: unwrapKeyItem success');
  } catch (error) {
    console.error('promise: wrap/unwrap failed, error: ' + error);
  }
}
```
