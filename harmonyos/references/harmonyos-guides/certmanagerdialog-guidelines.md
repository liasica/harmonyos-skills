---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/certmanagerdialog-guidelines
title: 证书管理对话框开发指导
breadcrumb: 指南 > 系统 > 安全 > Device Certificate Kit（设备证书服务） > 证书管理 > 证书管理对话框开发指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:51+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:56154e0d5c18d94bb46f5d846977cffe71596903227c0d7956b8abfd5c6c98e4
---

说明

本开发指导需使用API version 13及以上版本SDK。

证书管理对话框，可用于拉起证书管理页面并管理证书，如安装、存储、使用、销毁证书。

## 接口说明

详细接口说明可参考[@ohos.security.certManagerDialog (证书管理对话框模块)](../harmonyos-references/js-apis-certmanagerdialog.md)。

以上场景涉及的常用接口如下表所示。

| 实例名 | 接口名 | 描述 |
| --- | --- | --- |
| certificateManagerDialog | openCertificateManagerDialog(context: common.Context, pageType: CertificateDialogPageType): Promise<void> | 拉起证书管理对话框，显示相应的页面，使用Promise方式异步返回结果。 |
| certificateManagerDialog | openInstallCertificateDialog(context: common.Context, certType: CertificateType, certScope: CertificateScope, cert: Uint8Array): Promise<string>14+ | 调用安装证书对话框接口进行证书安装，使用Promise方式异步返回安装证书的唯一标识符。  仅2in1设备支持。 |
| certificateManagerDialog | openUninstallCertificateDialog(context: common.Context, certType: CertificateType, certUri: string): Promise<void>18+ | 调用删除证书对话框接口删除指定的证书，使用Promise方式异步返回结果。  仅2in1设备支持。 |
| certificateManagerDialog | openCertificateDetailDialog(context: common.Context, cert: Uint8Array, property: CertificateDialogProperty): Promise<void>18+ | 调用查看证书详情的对话框接口，展示证书的详情。使用Promise方式异步返回结果。  仅2in1设备支持。 |

## 开发步骤

1. 权限申请和声明。

   需要申请的权限：ohos.permission.ACCESS\_CERT\_MANAGER

   申请流程请参考：[申请应用权限](determine-application-mode.md)

   声明权限请参考：[声明权限](declare-permissions.md)
2. 导入相关模块。

   ```
   1. import { certificateManagerDialog } from '@kit.DeviceCertificateKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. import { common } from '@kit.AbilityKit';
   4. import { UIContext } from '@kit.ArkUI';
   ```
3. 拉起证书管理界面。

   ```
   1. import { certificateManagerDialog } from '@kit.DeviceCertificateKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. import { common } from '@kit.AbilityKit';

   5. async function certificateManagerDialogSample() {
   6. /* context为应用的上下文信息，由调用方自行获取，此处仅为示例 */
   7. let context: common.Context = new UIContext().getHostContext() as common.Context;
   8. /* pageType为页面类型，此处赋值PAGE_MAIN，即拉起证书管理主界面 */
   9. let pageType: certificateManagerDialog.CertificateDialogPageType =
   10. certificateManagerDialog.CertificateDialogPageType.PAGE_MAIN;
   11. try {
   12. certificateManagerDialog.openCertificateManagerDialog(context, pageType).then(() => {
   13. console.info('Succeeded in opening certificate manager dialog.');
   14. }).catch((err: BusinessError) => {
   15. console.error(`Failed to open certificate manager dialog. Code: ${err.code}, message: ${err.message}`);
   16. })
   17. } catch (error) {
   18. console.error(`Failed to open certificate manager dialog. Code: ${error.code}, message: ${error.message}`);
   19. }
   20. }
   ```

   [CertManagerDialogSample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/DeviceCertificateKit/CertificateManagement/entry/src/main/ets/samples/CertManagerDialogSample.ets#L15-L37)
4. 调用安装证书对话框接口进行证书安装、调用删除证书对话框接口进行证书删除、调用查看证书详情的对话框接口、展示证书的详情。以上场景仅2in1设备支持。

   ```
   1. import { certificateManagerDialog } from '@kit.DeviceCertificateKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. import { common } from '@kit.AbilityKit';
   4. import { UIContext } from '@kit.ArkUI';
   5. import { util } from '@kit.ArkTS';

   7. let certType = certificateManagerDialog.CertificateType.CA_CERT;
   8. let certUri: string = '';
   9. /* 用户CA证书数据需要业务赋值。 */
   10. let cert: Uint8Array = new util.TextEncoder().encodeInto(`-----BEGIN CERTIFICATE-----
   11. MIIDSTCCAjECFFRZKkiBuiZ+zqfjJOg05yeTePM9MA0GCSqGSIb3DQEBCwUAMGEx
   12. CzAJBgNVBAYTAmNuMQ0wCwYDVQQIDARvaG9zMQswCQYDVQQHDAJjbTEhMB8GA1UE
   13. CgwYSW50ZXJuZXQgV2lkZ2l0cyBQdHkgTHRkMRMwEQYDVQQDDApUZXN0Um9vdENB
   14. MB4XDTI1MTAxNTA3MzE0MloXDTI2MTAxNTA3MzE0MlowYTELMAkGA1UEBhMCY24x
   15. DTALBgNVBAgMBG9ob3MxCzAJBgNVBAcMAmNtMSEwHwYDVQQKDBhJbnRlcm5ldCBX
   16. aWRnaXRzIFB0eSBMdGQxEzARBgNVBAMMClRlc3RSb290Q0EwggEiMA0GCSqGSIb3
   17. DQEBAQUAA4IBDwAwggEKAoIBAQC5p4eoQJyTBvn01M8SwEi8dguTIPGmD3a8SGIj
   18. KXaB6ltv742H5EBjgk+zC8+Gis0ehEqwk3pVnnmByeYvrERxsUqDt69/FndlfTxI
   19. C2/2MxWVk97g/6TpJ5Lt2mTrH+rSOgUDyU27aPn12ZnDF1mLsT+U+CBmfj4+J4tW
   20. yzdFNj7kcKMQQok+L1dtFlDNMNpMA1UqADzoC3XgFl49CpDtoFId9DVsgUPkPfX1
   21. 89cCunomgJe1b17FzxfNu2yhbl5cnUEjeHGbmBgBIB7uG8tjGstnDPx7fl3Xrj+Q
   22. fRrwCpVKD9RxoyUBFbHttixxY5bHFUdvHRB251sxD+JfxxxLAgMBAAEwDQYJKoZI
   23. hvcNAQELBQADggEBAEGbNqcMU7C/lrIytI/OTtzYbkWDsfnRSPxlCUoZ2Xh3S83A
   24. SNQ9Ze5tDwWdW9Hlde9May6hzvuQSYeMLLnyM8WGResXCs7UbnSQe7fGfUu+xDGb
   25. h4tamnRFtZydxCCgDT9lIdHeutlPwOuxlR4HXpeowGeGJX0iFrdo6D0iXAY34hic
   26. yLQzuBqE/1s3PLA83Fi4EOOOV7P/ahmOLtBFlHbySHV68i9PNeNr9SDykH9/RgI9
   27. 5G8ZTZj8oSmbTGGtfNuVXybMyJMRlz6BkxG++kYcg7STRBqHGX7RrWHiupguNreO
   28. 4sJBdSpWBq172ZEyOvTqC4xX9lLYqwwBQ++TFoo=
   29. -----END CERTIFICATE-----`);

   31. async function installUserCADialogSample() {
   32. /* context为应用的上下文信息，由调用方自行获取，此处仅为示例。 */
   33. let context: common.Context = new UIContext().getHostContext() as common.Context;
   34. let certScope = certificateManagerDialog.CertificateScope.CURRENT_USER; /* 安装在当前用户下。 */
   35. try {
   36. /* 安装证书。 */
   37. certificateManagerDialog.openInstallCertificateDialog(context, certType, certScope, cert).then((result) => {
   38. console.info('Succeeded in opening install ca dialog.');
   39. certUri = result;
   40. }).catch((err: BusinessError) => {
   41. console.error(`Failed to open install ca dialog. Code: ${err.code}, message: ${err.message}`);
   42. })
   43. } catch (error) {
   44. console.error(`Failed to open install ca dialog. Code: ${error.code}, message: ${error.message}`);
   45. }
   46. }

   48. async function uninstallUserCADialogSample() {
   49. /* context为应用的上下文信息，由调用方自行获取，此处仅为示例。 */
   50. let context: common.Context = new UIContext().getHostContext() as common.Context;
   51. try {
   52. /* 删除证书。 */
   53. certificateManagerDialog.openUninstallCertificateDialog(context, certType, certUri).then(() => {
   54. console.info('Succeeded in opening uninstall ca dialog.');
   55. }).catch((err: BusinessError) => {
   56. console.error(`Failed to open uninstall ca dialog. Code: ${err.code}, message: ${err.message}`);
   57. })
   58. } catch (error) {
   59. console.error(`Failed to open uninstall ca dialog. Code: ${error.code}, message: ${error.message}`);
   60. }
   61. }

   63. async function certDetailDialogSample() {
   64. /* context为应用的上下文信息，由调用方自行获取，此处仅为示例。 */
   65. let context: common.Context = new UIContext().getHostContext() as common.Context;
   66. try {
   67. let property: certificateManagerDialog.CertificateDialogProperty = {
   68. showInstallButton: false    /* 不显示安装按钮。 */
   69. };
   70. /* 显示证书详情。 */
   71. certificateManagerDialog.openCertificateDetailDialog(context, cert, property).then(() => {
   72. console.info('Succeeded in opening show ca detail dialog.');
   73. }).catch((err: BusinessError) => {
   74. console.error(`Failed to open show ca detail dialog. Code: ${err.code}, message: ${err.message}`);
   75. })
   76. } catch (error) {
   77. console.error(`Failed to open show ca detail dialog. Code: ${error.code}, message: ${error.message}`);
   78. }
   79. }
   ```

   [CertManagerCaDialogSample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/DeviceCertificateKit/CertificateManagement/entry/src/main/ets/samples/CertManagerCaDialogSample.ets#L15-L95)
