---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/certmanager-private-credential-guidelines
title: 应用证书凭据开发指导
breadcrumb: 指南 > 系统 > 安全 > Device Certificate Kit（设备证书服务） > 证书管理服务 > 应用证书凭据开发指导
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:21+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:54c928dfd2a001ca61bf5979944facbef92ed7fe6a6cbfe7e705685f034d6ec9
---

如果您的应用服务器需要为您的应用颁发证书凭据，并在您的应用访问服务器接口时通过证书凭据进行身份认证，则您的应用可以使用本功能进行应用证书凭据的安装和使用。

应用证书凭据功能为应用提供了应用级别的证书凭据（包含证书链和私钥）的安全存储和管理能力，且支持应用间的访问隔离。

您的应用可以读取已安装应用证书凭据的证书链，及使用对应私钥进行签名，但不能读取私钥数据（保护私钥数据的安全）。应用证书凭据的公私钥对存储在[Universal Keystore Kit](huks-overview.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/dljy37E0TzqA8S7R0pD5CA/zh-cn_image_0000002742003469.png)

**说明** 

本开发指导需使用API版本11及以上版本SDK。

如需在不同应用间共享访问同一个证书凭据，请使用“[用户证书凭据](certmanager-user-credential-guidelines.md)”功能。

## 约束与限制

应用证书凭据的安装和签名、验签操作，依赖[密钥管理服务](huks-overview.md)（HUKS）能力。

## 开发步骤

1. 权限申请和声明。

   需要申请的权限：ohos.permission.ACCESS\_CERT\_MANAGER

   声明权限请参考：[声明权限](declare-permissions.md)
2. 导入相关模块。

   ```ts
   import { certificateManager } from '@kit.DeviceCertificateKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { util } from '@kit.ArkTS';
   ```
3. 安装应用证书凭据。

   您的应用在接收到应用服务器颁发的证书凭据后，通常打包为密钥库文件（KeyStore文件），可调用installPrivateCertificate接口把证书凭据安装到证书管理服务，安装接口返回KeyUri用于后续的证书凭据查询和签名操作。

   installPrivateCertificate接口还需要输入证书凭据别名，用于区分不同的应用证书凭据。如果应用使用相同的别名再次安装应用证书凭据，证书管理服务将覆盖并更新已安装的应用证书凭据数据。

   **说明** 

   应用证书凭据功能当前仅支持RSA、ECC及SM2算法类型的证书和私钥。

   installPrivateCertificate接口当前只支持P12格式的密钥库文件。
4. 使用应用证书凭据。

   在您的应用需要使用应用证书凭据进行应用的身份认证时，您可以通过如下步骤提供认证相关的数据：

   * 读取应用证书凭据的证书链。

     调用getPrivateCertificate接口，传入安装接口返回的KeyUri，从响应中的CMResult.credential.credentialData字段获取证书链（为pem格式的证书文件）。
   * 使用应用证书凭据的私钥对数据进行签名。

     1. 调用init接口初始化签名会话，传入安装接口返回的KeyUri和签名算法参数（如：填充方式和摘要算法），并返回签名会话的句柄handle。
     2. 调用update接口传入签名会话的句柄handle和待签名的数据。如果待签名的数据量比较大，可以调用多次update接口，每次传入部分数据。
     3. 调用finish接口结束签名会话并获取签名数据。

   **说明** 

   签名、验签操作支持的参数组合，详见HUKS声明的[签名/验签介绍及算法规格](huks-signing-signature-verification-overview.md)中RSA、ECC及SM2的描述。
5. 卸载已安装的应用证书凭据。

   当您的应用不再需要使用应用证书凭据时，可调用uninstallPrivateCertificate接口卸载已安装的应用证书凭据。例如您的应用证书凭据与登录用户绑定，在用户退出登录时卸载对应用户的应用证书凭据。

## 样例代码

```typescript
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { util } from '@kit.ArkTS';

async function privateCredSample() {
  /* 安装的凭据数据需要业务赋值，本例数据非凭据数据。 */
  let keystoreBase64Str = 'MIIMJgIBAzCCC+AGCSqGSIb3DQEHAaCCC9EEggvNMIILyTCCBW4GCSqGSIb3DQEH' +
    // ...
    'G615kxCjeS6uixCHuij3pgQUhHiChcSeohRPrVkVPSPmYr9tjAYCAgQA';
  /* 凭据数据转换为Uint8Array，凭据数据为der格式 */
  let keystore: Uint8Array = new util.Base64Helper().decodeSync(keystoreBase64Str);

  /* 安装凭据对应的密码，业务赋值。 */
  let keystorePwd: string = 'huawei';
  let appKeyUri: string = '';
  try {
    /* 安装应用证书凭据。 */
    const res: certificateManager.CMResult = await certificateManager.installPrivateCertificate(keystore, keystorePwd, 'testPriCredential');
    appKeyUri = (res.uri != undefined) ? res.uri : '';
    console.info(`InstallPrivateCertificate success appKeyUri: ${appKeyUri}`);
  } catch (err) {
    let e: BusinessError = err as BusinessError;
    console.error(`Failed to install private certificate. Code: ${e.code}, message: ${e.message}`);
  }

  try {
    /* 获取应用证书凭据。 */
    let res: certificateManager.CMResult = await certificateManager.getPrivateCertificate(appKeyUri);
    if (res === undefined || res.credential == undefined) {
      console.error('The result of getting private certificate is undefined.');
    } else {
      let credential = res.credential;
      console.info('Succeeded in getting private certificate.');
    }
  } catch (err) {
    console.error(`Failed to get private certificate. Code: ${err.code}, message: ${err.message}`);
  }

  try {
    /* srcData为待签名、验签的数据，业务自行赋值。 */
    let srcData: Uint8Array = new Uint8Array([
      0x86, 0xf7, 0x0d, 0x01, 0x07, 0x01,
    ]);

    /* 构造签名的属性参数。 */
    const signSpec: certificateManager.CMSignatureSpec = {
      purpose: certificateManager.CmKeyPurpose.CM_KEY_PURPOSE_SIGN,
      padding: certificateManager.CmKeyPadding.CM_PADDING_PSS,
      digest: certificateManager.CmKeyDigest.CM_DIGEST_SHA256
    };

    /* 签名。 */
    const signHandle: certificateManager.CMHandle = await certificateManager.init(appKeyUri, signSpec);
    await certificateManager.update(signHandle.handle, srcData);
    const signResult: certificateManager.CMResult = await certificateManager.finish(signHandle.handle);

    /* 构造验签的属性参数。 */
    const verifySpec: certificateManager.CMSignatureSpec = {
      purpose: certificateManager.CmKeyPurpose.CM_KEY_PURPOSE_VERIFY,
      padding: certificateManager.CmKeyPadding.CM_PADDING_PSS,
      digest: certificateManager.CmKeyDigest.CM_DIGEST_SHA256
    };

    /* 验签。 */
    const verifyHandle: certificateManager.CMHandle = await certificateManager.init(appKeyUri, verifySpec);
    await certificateManager.update(verifyHandle.handle, srcData);
    const verifyResult = await certificateManager.finish(verifyHandle.handle, signResult.outData);
    console.info('Succeeded in signing and verifying.');
  } catch (err) {
    let e: BusinessError = err as BusinessError;
    console.error(`Failed to sign or verify. Code: ${e.code}, message: ${e.message}`);
  }

  try {
    /* 删除应用证书凭据。 */
    await certificateManager.uninstallPrivateCertificate(appKeyUri);
  } catch (err) {
    let e: BusinessError = err as BusinessError;
    console.error(`Failed to uninstall private certificate. Code: ${e.code}, message: ${e.message}`);
  }
}
```
