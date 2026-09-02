---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/certmanager-ca-certs-guidelines
title: CA证书开发指导
breadcrumb: 指南 > 系统 > 安全 > Device Certificate Kit（设备证书服务） > 证书管理服务 > CA证书开发指导
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:29+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:c956dcb2448397eb463fd319f36c98289b523ae431ca18e07489cc5bc8f094ba
---

在对其他实体（设备、服务器）的证书凭据进行校验时，您的应用需要使用CA证书。例如您的应用使用预置的CA证书对应用服务器的HTTPS证书链进行可信校验。根据通信实现方式的不同，证书信任的配置方案也存在差异，下面分两种典型场景说明：

场景1：通过网络通信服务进行HTTPS连接。

您的应用可以参考[Network Kit配置证书校验](http-request.md#配置证书校验)内容，利用Device Certificate Kit的系统CA证书、用户CA证书，对HTTPS证书链进行校验。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/47bOYRxlQnmq55CPkx6Axg/zh-cn_image_0000002736433431.png)

场景2：采用底层或自定义的安全协议进行通信。

如果您的应用需要采用底层或自定义的安全协议与应用服务器进行通信，则您的应用可能需要从Device Certificate Kit读取系统CA证书和用户CA证书对服务器的证书链进行校验。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/nkRjc4bKTP6pi7DphfnBDQ/zh-cn_image_0000002706834276.png)

Device Certificate Kit的CA证书管理功能包含如下能力：

* 系统CA证书管理：由操作系统预安装的CA证书，包括国密算法（SM算法）和国际算法（RSA和ECC算法）的CA证书。

  只有通过[《华为根证书计划》](https://www.huawei.com/cn/root-certification-program)审核的CA证书才能预安装到HarmonyOS系统中。

  系统CA证书包含了业界常用的商业CA证书，可以覆盖绝大部分互联网应用和网站的证书链校验需求。

  设备的用户和应用只能读取系统CA证书，不能进行安装和更新。
* 用户CA证书管理：归属于设备用户的CA证书，由用户或MDM应用进行管理。仅当签发应用服务器证书的CA证书未包含在系统CA证书内，才需要安装用户CA证书，例如企业内部服务器使用的证书由企业自建CA证书颁发。

  用户CA证书划分为两个作用范围（Scope）：

  1. 当前用户级的CA证书：设备的用户间隔离，只有设备的当前登录用户才能访问和管理。设备用户可以通过系统设置应用进行管理，应用也可以通过API拉起证书管理服务的对话框（仅限PC/2in1设备支持），引导用户安装或卸载当前用户的CA证书。
  2. 所有用户级的CA证书：设备的所有用户都可以读取，当前只能通过MDM应用在企业设备上进行安装和管理。

  | 用户CA证书的作用范围（Scope） | 作用范围说明 | 证书管理方式 | 设备用户可执行的操作 | 应用可执行的操作 | 典型应用场景 |
  | --- | --- | --- | --- | --- | --- |
  | 当前用户 | 用户间隔离 | 由用户管理 | 安装/卸载/查看 | 读取，拉起安装/卸载对话框 | 在BYOD设备访问企业内部的服务器。 |
  | 所有用户 | 所有用户共享 | 由MDM应用管理 | 查看 | 读取 | 在企业设备访问企业内部的服务器。 |

**说明** 

本开发指导需使用API版本18及以上版本SDK。

使用并信任当前用户级的CA证书，设备的用户可以通过网络代理工具对您应用的通信消息进行中间人攻击，这可能导致您的应用产生安全风险。

具体请参考[网络连接安全配置](network-connection-security-configuration.md)进行安全配置。

## 基本概念

* 商业CA证书：由正规的第三方商业数字证书认证机构（CA）颁发和运营的商用CA证书，具备公开权威公信力。
* 自建CA证书：企业/组织自行搭建部署的私有数字证书颁发机构（CA）颁发的CA证书，一般用于企业/组织内网服务、测试环境等。
* MDM（Mobile Device Management）应用：也称企业设备管理应用，指集成了MDM功能的应用，能够集中管理、监控和保护企业内的移动设备（如智能手机、平板电脑、笔记本电脑等）。它允许IT管理员远程配置设备、强制执行安全策略、部署应用程序，并确保企业数据的安全。具体请参考[MDM Kit](mdm-kit-intro.md)相关资料。
* 企业设备：由企业MDM应用管理和控制的设备，该设备一般由企业进行采购并发放给企业员工进行日常办公。
* BYOD（Bring Your Own Device）：自带设备办公，指一些企业允许员工携带自己平板或智能手机到公司，并使用这些设备接入办公环境。例如用户企业办公或者外来访客携带设备访问工厂、实验室等场景。

## 开发步骤

1. 权限申请和声明。

   MDM应用调用安装和卸载CA证书接口需要申请权限：ohos.permission.ACCESS\_ENTERPRISE\_USER\_TRUSTED\_CERT

   调用其他接口需要申请权限：ohos.permission.ACCESS\_CERT\_MANAGER

   声明权限请参考：[声明权限](declare-permissions.md)
2. 导入相关模块。

   ```ts
   import { certificateManager, certificateManagerDialog } from '@kit.DeviceCertificateKit';
   import { util } from '@kit.ArkTS';
   import { common } from '@kit.AbilityKit';
   import { UIContext } from '@kit.ArkUI';
   ```
3. 安装和卸载用户CA证书。

   * 场景1：在BYOD设备安装用户CA证书。

     应用调用openInstallCertificateDialog接口可拉起安装用户CA证书的对话框（certType参数设置为CA\_CERT），安装页面需要对设备用户的身份进行认证。该接口只支持安装当前用户级的CA证书。

     **说明** 

     安装并信任用户CA证书，拥有CA证书的攻击者可能会获取到设备用户在访问网站或使用应用时传输的敏感信息。

     拉起安装用户CA证书的对话框接口当前仅支持PC/2in1设备。
   * 场景2：MDM应用在企业设备安装和卸载用户CA证书。

     MDM应用可调用installUserTrustedCertificateSync接口安装用户CA证书，接口需要指定待安装的CA证书文件，并返回已安装的CA证书标识（certUri）。

     MDM应用可调用uninstallUserTrustedCertificateSync接口卸载已安装的用户CA证书，输入已安装的CA证书标识certUri。
4. 读取系统CA证书和用户CA证书。

   证书管理服务提供了共享目录供应用读取系统CA证书和用户CA证书文件，您的应用可以先通过getCertificateStorePath接口获取对应CA证书的存储目录，然后从目录中读取CA证书文件（为pem格式的证书文件）。

   系统CA证书按照国际和国密算法类型分别存储在两个目录，可以通过getCertificateStorePath接口的property.certAlg参数获取指定算法的证书存储目录。

   用户CA证书按照当前用户级和所有用户级分别存储在不同的目录，可以通过getCertificateStorePath接口的property.certScope参数获取指定级别的证书存储目录。

## 样例代码

```typescript
import { certificateManager, certificateManagerDialog } from '@kit.DeviceCertificateKit';
import { util } from '@kit.ArkTS';
import { common } from '@kit.AbilityKit';
import { UIContext } from '@kit.ArkUI';

async function userCASample(): Promise<void> {
  /* 安装的用户CA证书数据需要业务赋值。 */
  let userCAData: Uint8Array = new util.TextEncoder().encodeInto('-----BEGIN CERTIFICATE-----\n' +
    'MIIDSTCCAjECFFRZKkiBuiZ+zqfjJOg05yeTePM9MA0GCSqGSIb3DQEBCwUAMGEx\n' +
    'CzAJBgNVBAYTAmNuMQ0wCwYDVQQIDARvaG9zMQswCQYDVQQHDAJjbTEhMB8GA1UE\n' +
    'CgwYSW50ZXJuZXQgV2lkZ2l0cyBQdHkgTHRkMRMwEQYDVQQDDApUZXN0Um9vdENB\n' +
    'MB4XDTI1MTAxNTA3MzE0MloXDTI2MTAxNTA3MzE0MlowYTELMAkGA1UEBhMCY24x\n' +
    'DTALBgNVBAgMBG9ob3MxCzAJBgNVBAcMAmNtMSEwHwYDVQQKDBhJbnRlcm5ldCBX\n' +
    'aWRnaXRzIFB0eSBMdGQxEzARBgNVBAMMClRlc3RSb290Q0EwggEiMA0GCSqGSIb3\n' +
    'DQEBAQUAA4IBDwAwggEKAoIBAQC5p4eoQJyTBvn01M8SwEi8dguTIPGmD3a8SGIj\n' +
    'KXaB6ltv742H5EBjgk+zC8+Gis0ehEqwk3pVnnmByeYvrERxsUqDt69/FndlfTxI\n' +
    'C2/2MxWVk97g/6TpJ5Lt2mTrH+rSOgUDyU27aPn12ZnDF1mLsT+U+CBmfj4+J4tW\n' +
    'yzdFNj7kcKMQQok+L1dtFlDNMNpMA1UqADzoC3XgFl49CpDtoFId9DVsgUPkPfX1\n' +
    '89cCunomgJe1b17FzxfNu2yhbl5cnUEjeHGbmBgBIB7uG8tjGstnDPx7fl3Xrj+Q\n' +
    'fRrwCpVKD9RxoyUBFbHttixxY5bHFUdvHRB251sxD+JfxxxLAgMBAAEwDQYJKoZI\n' +
    'hvcNAQELBQADggEBAEGbNqcMU7C/lrIytI/OTtzYbkWDsfnRSPxlCUoZ2Xh3S83A\n' +
    'SNQ9Ze5tDwWdW9Hlde9May6hzvuQSYeMLLnyM8WGResXCs7UbnSQe7fGfUu+xDGb\n' +
    'h4tamnRFtZydxCCgDT9lIdHeutlPwOuxlR4HXpeowGeGJX0iFrdo6D0iXAY34hic\n' +
    'yLQzuBqE/1s3PLA83Fi4EOOOV7P/ahmOLtBFlHbySHV68i9PNeNr9SDykH9/RgI9\n' +
    '5G8ZTZj8oSmbTGGtfNuVXybMyJMRlz6BkxG++kYcg7STRBqHGX7RrWHiupguNreO\n' +
    '4sJBdSpWBq172ZEyOvTqC4xX9lLYqwwBQ++TFoo=\n' +
    '-----END CERTIFICATE-----');

  let certUri: string = '';

  /* 场景1：在BYOD设备安装用户CA证书 */
  try {
    certUri = await installUserCACertDialog(userCAData);
  } catch (error) {
    console.error(`Failed to install user CA certificate.`);
  }
  /* 获取CA证书 */
  getUserCaCertSample();
  /* 场景1：在BYOD设备卸载用户CA证书 */
  uninstallUserCACertDialog(certUri);

  /* 场景2：MDM应用在企业设备安装用户CA证书 */
  certUri = installUserCACertEnterprise(userCAData);
  /* 获取CA证书 */
  getUserCaCertSample();
  /* 场景2：MDM应用在企业设备卸载用户CA证书 */
  uninstallUserCACertEnterprise(certUri);
}

async function installUserCACertDialog(userCAData: Uint8Array): Promise<string> {
  return new Promise<string>((resolve, reject) => {
    /* 场景1：在BYOD设备安装用户CA证书 */
    try {
      /* context为应用的上下文信息，调用方自行获取，此处仅为示例 */
      let context: common.Context = new UIContext().getHostContext() as common.Context;
      /* 安装用户CA证书 */
      certificateManagerDialog.openInstallCertificateDialog(
        context,
        certificateManagerDialog.CertificateType.CA_CERT,
        certificateManagerDialog.CertificateScope.CURRENT_USER,
        userCAData
      ).then((keyUri: string) => {
        console.info(`Installing user CA certificate successful, keyUri: ${keyUri}`);
        resolve(keyUri);
      }).catch((error: BusinessError) => {
        console.error(`Failed to install user CA certificate. Code: ${error.code}, message: ${error.message}`);
        reject(error);
      });
    } catch (error) {
      console.error(`Failed to install user CA certificate. Code: ${error.code}, message: ${error.message}`);
      reject(error);
    }
  })
}

function installUserCACertEnterprise(userCAData: Uint8Array): string {
  /* 场景2：MDM应用在企业设备安装用户CA证书 */
  try {
    /* 在当前用户下，安装用户CA证书。 */
    let result = certificateManager.installUserTrustedCertificateSync(
      userCAData,
      certificateManager.CertScope.CURRENT_USER
    );
    let certUri = result.uri ?? '';
    console.info(`Sync install user CA certificate successful, certUri is ${certUri}`);
    return certUri
  } catch (err) {
    console.error(`Failed to sync install user CA certificate. Code: ${err.code}, message: ${err.message}`);
  }
  return '';
}

async function uninstallUserCACertDialog(certUri: string): Promise<void> {
  try {
    /* 场景1：在BYOD设备卸载用户CA证书 */
    /* context为应用的上下文信息，调用方自行获取，此处仅为示例 */
    let context: common.Context = new UIContext().getHostContext() as common.Context;
    certificateManagerDialog.openUninstallCertificateDialog(
      context,
      certificateManagerDialog.CertificateType.CA_CERT,
      certUri
    ).then(() => {
      console.info(`Uninstall user ca certificate successful.`);
    }).catch((error: BusinessError) => {
      console.error(`Failed to uninstall user ca certificate. Code: ${error.code}, message: ${error.message}`);
    });
  } catch (err) {
    console.error(`Failed to uninstall user ca certificate. Code: ${err.code}, message: ${err.message}`);
  }
}

function getUserCaCertSample(): void {
  try {
    /* 获取系统CA的存储位置。 */
    let property1: certificateManager.CertStoreProperty = {
      certType: certificateManager.CertType.CA_CERT_SYSTEM,
    }
    /* 您可以从systemCAPath目录读取CA证书。 */
    let systemCAPath = certificateManager.getCertificateStorePath(property1);
    console.info(`Success to get system ca path: ${systemCAPath}`);

    /* 获取当前用户的用户CA存储位置。 */
    let property2: certificateManager.CertStoreProperty = {
      certType: certificateManager.CertType.CA_CERT_USER,
      certScope: certificateManager.CertScope.CURRENT_USER,
    }
    /* 您可以从userCACurrentPath目录读取CA证书。 */
    let userCACurrentPath = certificateManager.getCertificateStorePath(property2);
    console.info(`Success to get current user's user ca path: ${userCACurrentPath}`);

    /* 获取设备公共的用户CA存储位置。 */
    let property3: certificateManager.CertStoreProperty = {
      certType: certificateManager.CertType.CA_CERT_USER,
      certScope: certificateManager.CertScope.GLOBAL_USER,
    }
    /* 您可以从globalCACurrentPath目录读取CA证书。 */
    let globalCACurrentPath = certificateManager.getCertificateStorePath(property3);
    console.info(`Success to get global user's user ca path: ${globalCACurrentPath}`);
  } catch (error) {
    console.error(`Failed to get store path. Code: ${error.code}, message: ${error.message}`);
  }
}

async function uninstallUserCACertEnterprise(certUri: string): Promise<void> {
  try {
    /* 场景2：MDM应用在企业设备卸载用户CA证书 */
    certificateManager.uninstallUserTrustedCertificateSync(certUri);
    console.info(`Uninstall user ca certificate successful.`);
  } catch (err) {
    console.error(`Failed to uninstall user ca certificate. Code: ${err.code}, message: ${err.message}`);
  }
}
```
