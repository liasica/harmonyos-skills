---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/certmanager-system-credential-guidelines
title: 系统证书凭据开发指导
breadcrumb: 指南 > 系统 > 安全 > Device Certificate Kit（设备证书服务） > 证书管理服务 > 系统证书凭据开发指导
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:21+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f3bc511152eb2279d36105267c775b4d97f67a0c0f48e10b7539bd8dc11075d5
---

系统证书凭据用于系统服务（如WLAN、VPN服务）连接服务器时，服务器对接入设备进行身份认证。系统证书凭据功能提供了系统级别的证书凭据（包含证书链和私钥）的安全存储和签名能力。系统证书凭据的公私钥对存储在[Universal Keystore Kit](huks-overview.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/abRwjo-jQKetUEFgEikhcQ/zh-cn_image_0000002742123431.png)

系统证书凭据可以由设备的用户进行安装和管理，也可以由应用通过API拉起证书管理服务的对话框，引导用户完成安装。

**说明** 

本开发指导需使用API版本23及以上版本SDK。

系统证书凭据只能由系统服务进行读取和使用。

系统证书凭据安装成功后，用户需要到系统设置应用界面进行对应的配置，WLAN、VPN等系统服务才能使用安装的系统证书凭据。

## 约束与限制

系统证书凭据的安装和签名、验签操作，依赖[密钥管理服务](huks-overview.md)（HUKS）能力。

## 开发步骤

1. 权限申请和声明。

   需要申请的权限：ohos.permission.ACCESS\_CERT\_MANAGER

   声明权限请参考：[声明权限](declare-permissions.md)
2. 导入相关模块。

   ```ts
   import { certificateManagerDialog } from '@kit.DeviceCertificateKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { common } from '@kit.AbilityKit';
   import { UIContext } from '@kit.ArkUI';
   import { util } from '@kit.ArkTS';
   ```
3. 安装系统证书凭据。

   调用openInstallCertificateDialog接口可拉起系统证书凭据安装的对话框（certType参数设置为CREDENTIAL\_SYSTEM），安装页面需要用户输入正确的密钥库文件密码。

   **说明** 

   系统证书凭据功能当前仅支持RSA、ECC及SM2算法类型的证书和私钥。

   openInstallCertificateDialog接口当前只支持P12格式的密钥库文件。

## 样例代码

```typescript
import { certificateManagerDialog } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import { UIContext } from '@kit.ArkUI';
import { util } from '@kit.ArkTS';

function systemCredSample(): void {
  /* context为应用的上下文信息，调用方自行获取，此处仅为示例 */
  let context: common.Context = new UIContext().getHostContext() as common.Context;

  /* 安装的凭据数据需要业务赋值，本例数据非凭据数据。 */
  let keystoreBase64Str = 'MIIMJgIBAzCCC+AGCSqGSIb3DQEHAaCCC9EEggvNMIILyTCCBW4GCSqGSIb3DQEH' +
    // ...
    'G615kxCjeS6uixCHuij3pgQUhHiChcSeohRPrVkVPSPmYr9tjAYCAgQA';
  /* 凭据数据转换为Uint8Array，凭据数据为der格式 */
  let keystore: Uint8Array = new util.Base64Helper().decodeSync(keystoreBase64Str);

  try {
    /* 安装系统证书凭据 */
    certificateManagerDialog.openInstallCertificateDialog(
      context,
      certificateManagerDialog.CertificateType.CREDENTIAL_SYSTEM,
      certificateManagerDialog.CertificateScope.CURRENT_USER,
      keystore
    ).then((keyUri: string) => {
      console.info(`Install system credential success, keyUri: ${keyUri}`);
    }).catch((error: BusinessError) => {
      console.error(`Failed to install system credential. Code: ${error.code}, message: ${error.message}`);
    });
  } catch (error) {
    console.error(`Failed to install system credential. Code: ${error.code}, message: ${error.message}`);
  }
  return;
}
```
