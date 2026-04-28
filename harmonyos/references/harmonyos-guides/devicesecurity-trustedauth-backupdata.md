---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-trustedauth-backupdata
title: 数字盾签名密钥备份与恢复
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 数字盾服务 > 数字盾签名密钥备份与恢复
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:58+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a29ed994403d27cbf474435fe7260e6a38ff40918e769e36d74f1f98c54f13da
---

## 场景介绍

在数字盾激活前，应用需向密钥管理服务提交密钥生成申请，指定所需密钥的技术参数（如算法、长度等），成功生成的密钥将存储于密钥管理服务侧，应用可申请使用对应密钥进行数字盾服务相关业务数据的签名/验签操作。若应用被卸载，密钥管理服务将自动删除对应的密钥数据，导致应用重新安装后，数字盾功能无法继续使用。

若您希望当应用在原设备上重新安装后仍能通过历史数据恢复数字盾功能，请在激活数字盾后，执行以下操作：

1. 向密钥管理服务发起导出密钥的加密密文（密钥密文）申请。
2. 向数字盾服务发起密钥备份申请，将密钥密文安全存入数字盾系统。

在应用卸载重新安装后，如果您期望继续使用应用卸载前使用的密钥管理服务生成的密钥数据，减少用户重新激活数字盾密码流程，直接恢复历史数字盾功能时，则需要执行以下操作：

1. 向数字盾服务发起密钥恢复申请，用户在数字盾密码认证通过后，将应用卸载前备份的密钥数据导出至应用侧。
2. 将密钥数据发送至密钥管理服务，完成密钥恢复。

说明

* 一旦用户关闭了数字盾服务，数字盾服务侧将会自动清理对应的密码数据及密钥数据，当应用重新激活数字盾时，需要重新进行密钥数据备份。
* 从密钥导入到数字盾密码关闭之间，密钥导入不支持重复导入到数字盾服务侧。

## 约束与限制

本功能目前仅在手机设备支持。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/RL3mANNjQs2QU2CGTguAsQ/zh-cn_image_0000002583438443.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234257Z&HW-CC-Expire=86400&HW-CC-Sign=4F0FC5CBF7134E329692A88E02F7A0D9A04362426A73D92AE1F9334E9EDACBEF)

## 接口说明

接口及使用方法请参见[API参考](../harmonyos-references/devicesecurity-arktsapi-errcode-trusted-auth.md)。

| 接口名 | 描述 |
| --- | --- |
| [importData](../harmonyos-references/devicesecurity-trusted-auth-api.md#importdata)(data: ArrayBuffer, authID: bigint): Promise<void> | 导入数据（即与HUKS签名验签时使用的加密密钥信息） |
| [exportData](../harmonyos-references/devicesecurity-trusted-auth-api.md#exportdata)(authID: bigint, label: TUILable): Promise<ArrayBuffer> | 导出数据（即与HUKS签名验签时使用的加密密钥信息） |

## 开发步骤

1. 导入huks trustedAuthentication 和相关依赖模块。

   ```
   1. import { resourceManager } from '@kit.LocalizationKit'
   2. import { huks } from '@kit.UniversalKeystoreKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   4. import { trustedAuthentication } from '@kit.DeviceSecurityKit';
   5. import { hilog } from '@kit.PerformanceAnalysisKit';
   6. import { common } from '@kit.AbilityKit';
   ```
2. 参考密钥管理服务提供的wrapKeyItem方法，完成密钥导出。

   ```
   1. // 密钥别名
   2. let keyAlias = "testWrapKey";
   3. // 密钥属性集合
   4. let properties: Array<huks.HuksParam> = [
   5. {
   6. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
   7. value: huks.HuksKeyAlg.HUKS_ALG_AES
   8. },
   9. {
   10. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
   11. value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256
   12. },
   13. {
   14. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
   15. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT | huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
   16. },
   17. {
   18. tag: huks.HuksTag.HUKS_TAG_PADDING,
   19. value: huks.HuksKeyPadding.HUKS_PADDING_PKCS7
   20. },
   21. {
   22. tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
   23. value: huks.HuksCipherMode.HUKS_MODE_GCM
   24. },
   25. /* 生成密钥时指定允许加密导出 */
   26. {
   27. tag: huks.HuksTag.HUKS_TAG_IS_ALLOWED_WRAP,
   28. value: true
   29. }
   30. ];

   32. let options: huks.HuksOptions = {
   33. properties: properties,
   34. };

   36. let wrapKeyProperties: Array<huks.HuksParam> = [
   37. {
   38. tag: huks.HuksTag.HUKS_TAG_KEY_WRAP_TYPE,
   39. value: huks.HuksKeyWrapType.HUKS_KEY_WRAP_TYPE_HUK_BASED
   40. }
   41. ];

   43. let wrapKeyOptions: huks.HuksOptions = {
   44. properties: wrapKeyProperties,
   45. };

   47. let wrappedKey: Uint8Array | undefined = undefined;

   49. // 调用生成密钥接口
   50. await huks.generateKeyItem(keyAlias, options).then(() => {
   51. console.info(`promise: generateKeyItem success`);
   52. }).catch((error: Error) => {
   53. console.error(`promise: generateKeyItem failed`);
   54. });

   56. // 从密钥管理服务导出生成密钥的密文数据
   57. await huks.wrapKeyItem(keyAlias, wrapKeyOptions).then((data) => {
   58. wrappedKey = data.outData as Uint8Array;
   59. console.info(`promise: wrapKeyItem success, data = ${JSON.stringify(data)}`);
   60. }).catch((error: Error) => {
   61. console.error(`promise: wrapKeyItem failed`);
   62. });
   ```
3. 从服务器获取当前账号在[设置数字盾密码](devicesecurity-trustedauth-setpwd.md)时获取的authID并以authID为索引向数字盾服务发起数据导入请求。

   ```
   1. try {
   2. const authID: bigint = 11842183505170721246n; //实际填充为从服务器获取到的账号对应的authID值
   3. const buffer = new ArrayBuffer(8);
   4. const bufferArray = new Uint8Array(buffer);
   5. bufferArray.set([1, 2, 3, 4, 5, 6, 7, 8]);//实际使用时替换为从密钥管理服务获取的备份密钥信息
   6. await trustedAuthentication.importData(buffer, authID);
   7. } catch (err) {
   8. hilog.error(0x0000, 'testTag', `Failed to importData, code:${err.code}, message:${err.message}`);
   9. throw new Error('Import data failed:' + (err as BusinessError).message);
   10. }
   ```
4. 当应用卸载重新安装后，应用侧可向数字盾服务器发起密钥恢复申请。

   ```
   1. try {
   2. const authID: bigint = 11842183505170721246n; //实际填充为从服务器获取到的账号对应的authID值
   3. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
   4. const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
   5. const fileData : Uint8Array = await resourceMgr.getRawFileContent('test_logo_rgba.png'); //实际使用时请替换为应用要在TUI界面展示的logo图片名称
   6. const buffer = fileData.buffer;
   7. const label:trustedAuthentication.TUILable = {
   8. image: buffer as ArrayBuffer,
   9. title: "导出密钥信息",
   10. }
   11. const data = await trustedAuthentication.exportData(authID, label);
   12. } catch (err) {
   13. hilog.error(0x0000, 'testTag', `Failed to exportData, code:${err.code}, message:${err.message}`);
   14. throw new Error('Export data failed:' + (err as BusinessError).message);
   15. }
   ```
5. 将从数字盾服务获取的密钥数据，发送至密钥管理服务进行密钥导入恢复。

   ```
   1. // 在密钥管理服务侧进行密钥导入恢复，其中keyAlias、wrapKeyOptions、wrappedKey为步骤二定义参数
   2. await huks.unwrapKeyItem(keyAlias, wrapKeyOptions, wrappedKey).then((data) => {
   3. console.info(`promise: unwrapKeyItem success`);
   4. }).catch((error: Error) => {
   5. console.error(`promise: unwrapKeyItem failed`);
   6. });
   ```
