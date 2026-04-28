---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/certmanager-ca-certs-guidelines
title: CA证书开发指导
breadcrumb: 指南 > 系统 > 安全 > Device Certificate Kit（设备证书服务） > 证书管理 > CA证书开发指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:51+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1e2f7d4c9d878e3610d45ea8b41721fa28f783b14b749d23545901e718cb7c66
---

说明

本开发指导需使用API version 12及以上版本SDK。

## 场景说明

典型场景。

* 安装用户CA证书。调用者可以将用户CA证书安装在当前用户或者设备公共位置下。
  + 安装在当前用户时，仅当前用户的业务可以访问该证书。
  + 安装在设备公共位置下，所有用户下的业务都可以访问。
* 获取用户CA证书列表。可以选择获取当前用户或者设备公共位置下的用户CA证书列表。
* 获取用户CA证书详情。
* 删除指定的用户CA证书。
* 获取CA证书的存储路径。

## 接口说明

详细接口说明可参考[@ohos.security.certManager (证书管理模块)](../harmonyos-references/js-apis-certmanager.md)。

以上场景涉及的常用接口如下表所示。

| 实例名 | 接口名 | 描述 |
| --- | --- | --- |
| certificateManager | installUserTrustedCertificateSync(cert: Uint8Array, certScope: CertScope) : CMResult18+ | 安装用户CA证书。 |
| certificateManager | uninstallUserTrustedCertificateSync(certUri: string) : void18+ | 删除用户CA证书。 |
| certificateManager | getAllUserTrustedCertificates(): Promise<CMResult> | 获取当前用户和设备公共位置的所有用户根CA证书列表。 |
| certificateManager | getAllUserTrustedCertificates(scope: CertScope): Promise<CMResult>18+ | 根据证书的位置获取用户根CA证书列表。 |
| certificateManager | getUserTrustedCertificate(certUri: string): Promise<CMResult> | 获取用户根CA证书的详细信息。 |
| certificateManager | getCertificateStorePath(property: CertStoreProperty): string18+ | 获取证书的存储路径。 |

## 开发步骤

1. 权限申请和声明。

   使用安装和删除接口需要申请权限：ohos.permission.ACCESS\_ENTERPRISE\_USER\_TRUSTED\_CERT或ohos.permission.ACCESS\_USER\_TRUSTED\_CERT

   使用获取列表和获取详情接口需要申请权限：ohos.permission.ACCESS\_CERT\_MANAGER

   申请流程请参考：[申请应用权限](determine-application-mode.md)

   声明权限请参考：[声明权限](declare-permissions.md)
2. 导入相关模块。

   ```
   1. import { certificateManager } from '@kit.DeviceCertificateKit';
   ```
3. 安装用户CA证书、获取用户CA证书列表、获取用户证书详情、删除用户CA证书。

   ```
   1. import { certificateManager } from '@kit.DeviceCertificateKit';
   2. import { util } from '@kit.ArkTS';

   4. async function userCASample() {
   5. /* 安装的用户CA证书数据需要业务赋值。 */
   6. let userCAData: Uint8Array = new util.TextEncoder().encodeInto('-----BEGIN CERTIFICATE-----\n' +
   7. 'MIIDSTCCAjECFFRZKkiBuiZ+zqfjJOg05yeTePM9MA0GCSqGSIb3DQEBCwUAMGEx\n' +
   8. 'CzAJBgNVBAYTAmNuMQ0wCwYDVQQIDARvaG9zMQswCQYDVQQHDAJjbTEhMB8GA1UE\n' +
   9. 'CgwYSW50ZXJuZXQgV2lkZ2l0cyBQdHkgTHRkMRMwEQYDVQQDDApUZXN0Um9vdENB\n' +
   10. 'MB4XDTI1MTAxNTA3MzE0MloXDTI2MTAxNTA3MzE0MlowYTELMAkGA1UEBhMCY24x\n' +
   11. 'DTALBgNVBAgMBG9ob3MxCzAJBgNVBAcMAmNtMSEwHwYDVQQKDBhJbnRlcm5ldCBX\n' +
   12. 'aWRnaXRzIFB0eSBMdGQxEzARBgNVBAMMClRlc3RSb290Q0EwggEiMA0GCSqGSIb3\n' +
   13. 'DQEBAQUAA4IBDwAwggEKAoIBAQC5p4eoQJyTBvn01M8SwEi8dguTIPGmD3a8SGIj\n' +
   14. 'KXaB6ltv742H5EBjgk+zC8+Gis0ehEqwk3pVnnmByeYvrERxsUqDt69/FndlfTxI\n' +
   15. 'C2/2MxWVk97g/6TpJ5Lt2mTrH+rSOgUDyU27aPn12ZnDF1mLsT+U+CBmfj4+J4tW\n' +
   16. 'yzdFNj7kcKMQQok+L1dtFlDNMNpMA1UqADzoC3XgFl49CpDtoFId9DVsgUPkPfX1\n' +
   17. '89cCunomgJe1b17FzxfNu2yhbl5cnUEjeHGbmBgBIB7uG8tjGstnDPx7fl3Xrj+Q\n' +
   18. 'fRrwCpVKD9RxoyUBFbHttixxY5bHFUdvHRB251sxD+JfxxxLAgMBAAEwDQYJKoZI\n' +
   19. 'hvcNAQELBQADggEBAEGbNqcMU7C/lrIytI/OTtzYbkWDsfnRSPxlCUoZ2Xh3S83A\n' +
   20. 'SNQ9Ze5tDwWdW9Hlde9May6hzvuQSYeMLLnyM8WGResXCs7UbnSQe7fGfUu+xDGb\n' +
   21. 'h4tamnRFtZydxCCgDT9lIdHeutlPwOuxlR4HXpeowGeGJX0iFrdo6D0iXAY34hic\n' +
   22. 'yLQzuBqE/1s3PLA83Fi4EOOOV7P/ahmOLtBFlHbySHV68i9PNeNr9SDykH9/RgI9\n' +
   23. '5G8ZTZj8oSmbTGGtfNuVXybMyJMRlz6BkxG++kYcg7STRBqHGX7RrWHiupguNreO\n' +
   24. '4sJBdSpWBq172ZEyOvTqC4xX9lLYqwwBQ++TFoo=\n' +
   25. '-----END CERTIFICATE-----');

   27. let certUri: string = '';
   28. let certScope = certificateManager.CertScope.CURRENT_USER;
   29. try {
   30. /* 在当前用户下，安装用户CA证书。 */
   31. let result = certificateManager.installUserTrustedCertificateSync(userCAData, certScope);
   32. certUri = (result.uri != undefined) ? result.uri : '';
   33. console.info(`Succeeded in install user ca cert, certUri is ${certUri}`);
   34. } catch (err) {
   35. console.error(`Failed to install user ca cert. Code: ${err.code}, message: ${err.message}`);
   36. }

   38. try {
   39. /* 获取用户CA证书详情。 */
   40. let result = await certificateManager.getUserTrustedCertificate(certUri);
   41. if (result === undefined || result.certInfo == undefined) {
   42. console.error('The result of getting user ca cert is undefined.');
   43. } else {
   44. let certInfo = result.certInfo;
   45. console.info('Succeeded in getting user ca cert.');
   46. }
   47. } catch (err) {
   48. console.error(`Failed to get user ca certificate. Code: ${err.code}, message: ${err.message}`);
   49. }

   51. try {
   52. /* 获取当前用户下的用户CA证书列表。 */
   53. let result = await certificateManager.getAllUserTrustedCertificates(certScope);
   54. if (result == undefined) { /* 用户根CA证书个数为0时，返回result为undefined。 */
   55. console.info('the count of the user trusted certificates is 0');
   56. } else if (result.certList == undefined) {
   57. console.error('The result of getting current user trusted certificates is undefined.');
   58. } else {
   59. let list = result.certList;
   60. console.info('Succeeded in getting user ca cert list.');
   61. }
   62. } catch (err) {
   63. console.error(`Failed to get user ca certificate. Code: ${err.code}, message: ${err.message}`);
   64. }

   66. try {
   67. /* 删除安装的用户CA证书。 */
   68. certificateManager.uninstallUserTrustedCertificateSync(certUri);
   69. } catch (err) {
   70. console.error(`Failed to uninstall user ca certificate. Code: ${err.code}, message: ${err.message}`);
   71. }
   72. }
   ```

   [CertManagerUserCASample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/DeviceCertificateKit/CertificateManagement/entry/src/main/ets/samples/CertManagerUserCASample.ets#L15-L88)
4. 获取系统CA证书路径、用户CA证书路径。应用可以直接通过该路径访问CA证书。

   ```
   1. import { certificateManager } from '@kit.DeviceCertificateKit';

   3. function getUserCaPathSample() {
   4. try {
   5. /* 获取系统CA的存储位置。 */
   6. let property1: certificateManager.CertStoreProperty = {
   7. certType: certificateManager.CertType.CA_CERT_SYSTEM,
   8. }
   9. let systemCAPath = certificateManager.getCertificateStorePath(property1);
   10. console.info(`Success to get system ca path: ${systemCAPath}`);

   12. /* 获取当前用户的用户CA存储位置。 */
   13. let property2: certificateManager.CertStoreProperty = {
   14. certType: certificateManager.CertType.CA_CERT_USER,
   15. certScope: certificateManager.CertScope.CURRENT_USER,
   16. }
   17. let userCACurrentPath = certificateManager.getCertificateStorePath(property2);
   18. console.info(`Success to get current user's user ca path: ${userCACurrentPath}`);

   20. /* 获取设备公共的用户CA存储位置。 */
   21. let property3: certificateManager.CertStoreProperty = {
   22. certType: certificateManager.CertType.CA_CERT_USER,
   23. certScope: certificateManager.CertScope.GLOBAL_USER,
   24. }
   25. let globalCACurrentPath = certificateManager.getCertificateStorePath(property3);
   26. console.info(`Success to get global user's user ca path: ${globalCACurrentPath}`);
   27. } catch (error) {
   28. console.error(`Failed to get store path. Code: ${error.code}, message: ${error.message}`);
   29. }
   30. }
   ```

   [CertManagerGetCAPathSample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/DeviceCertificateKit/CertificateManagement/entry/src/main/ets/samples/CertManagerGetCAPathSample.ets#L16-L47)
