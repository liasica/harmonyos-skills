---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-trustedauth-backupdata
title: 数字盾签名密钥备份与恢复
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 数字盾服务 > 数字盾签名密钥备份与恢复
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:30+08:00
doc_updated_at: 2026-08-03
content_hash: sha256:d597368f987fbf72b73855076ea7b874e93b8662a17eeb084efc68cdfef7acfa
---

## 场景介绍

在数字盾激活前，企业开发者应用需向密钥管理服务提交密钥生成申请，指定所需密钥的技术参数（如算法、长度等），成功生成的密钥将存储于密钥管理服务侧，应用可申请使用对应密钥进行数字盾服务相关业务数据的签名/验签操作。若应用被卸载，密钥管理服务将自动删除对应的密钥数据，导致应用重新安装后，数字盾功能无法继续使用。

若您希望当应用在原设备上重新安装后仍能通过历史数据恢复数字盾功能，请在激活数字盾后，执行以下操作：

1. 向密钥管理服务发起导出密钥的加密密文（密钥密文）申请。
2. 向数字盾服务发起密钥备份申请，将密钥密文安全存入数字盾系统。

在应用卸载重新安装后，如果您期望继续使用应用卸载前使用的密钥管理服务生成的密钥数据，减少用户重新激活数字盾密码流程，直接恢复历史数字盾功能时，则需要执行以下操作：

1. 向数字盾服务发起密钥恢复申请，用户在数字盾密码认证通过后，将应用卸载前备份的密钥数据导出至应用侧。
2. 将密钥数据发送至密钥管理服务，完成密钥恢复。

**说明** 

* 一旦用户关闭了数字盾服务，数字盾服务侧将会自动清理对应的密码数据及密钥数据，当应用重新激活数字盾时，需要重新进行密钥数据备份。
* 从密钥导入到数字盾密码关闭之间，密钥导入不支持重复导入到数字盾服务侧。

## 约束与限制

本功能在6.1.1(24)之前版本仅支持Phone；6.1.1(24)及之后版本，新增支持具备TUI能力的PC/2in1、具备TUI能力的Tablet。可通过接口[checkConfirmUITextFormat](../harmonyos-references/devicesecurity-trusted-auth-api.md#trustedauthenticationcheckconfirmuitextformat)查询设备是否具备TUI能力。不支持的设备在调用数字盾服务相关业务接口时，返回错误码1019100016。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/ALAKHvYXT7WUmrKUPI59Rg/zh-cn_image_0000002706834298.jpg)

## 接口说明

接口及使用方法请参见[API参考](../harmonyos-references/errorcode-devicesecurity-trusted-auth.md)。

| 接口名 | 描述 |
| --- | --- |
| [importData](../harmonyos-references/devicesecurity-trusted-auth-api.md#trustedauthenticationimportdata)(data: ArrayBuffer, authID: bigint): Promise<void> | 导入数据（即与HUKS签名验签时使用的加密密钥信息）。 |
| [exportData](../harmonyos-references/devicesecurity-trusted-auth-api.md#trustedauthenticationexportdata)(authID: bigint, label: TUILable): Promise<ArrayBuffer> | 导出数据（即与HUKS签名验签时使用的加密密钥信息）。 |

## 开发步骤

1. 导入huks trustedAuthentication 和相关依赖模块。

   ```typescript
    import { resourceManager } from '@kit.LocalizationKit'
    import { huks } from '@kit.UniversalKeystoreKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { trustedAuthentication } from '@kit.DeviceSecurityKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { common } from '@kit.AbilityKit';
   ```
2. 参考密钥管理服务提供的wrapKeyItem方法，完成密钥导出。

   ```typescript
   private async exportKeyFromHuks(): Promise<Uint8Array> {
     let wrapKeyProperties: Array<huks.HuksParam> = [
       {
         tag: huks.HuksTag.HUKS_TAG_KEY_WRAP_TYPE,
         value: huks.HuksKeyWrapType.HUKS_KEY_WRAP_TYPE_HUK_BASED
       }
     ];

     let wrapKeyOptions: huks.HuksOptions = {
       properties: wrapKeyProperties
     };

     try {
       // 从密钥管理服务导出生成密钥的密文数据
       let data = await huks.wrapKeyItem(KEY_ALIAS, wrapKeyOptions);
       let wrappedKey: Uint8Array = data.outData as Uint8Array;
       hilog.info(0x0000, 'testTag', 'exportKeyFromHuks success, size=' + wrappedKey.length);
       return wrappedKey;
     } catch (error) {
       hilog.error(0x0000, 'testTag', 'exportKeyFromHuks failed', JSON.stringify(error));
       throw new Error('Export key from HUKS failed:' + (error as BusinessError).message);
     }
   }
   ```
3. 从服务器获取当前账号在[设置数字盾密码](devicesecurity-trustedauth-setpwd.md)时获取的authID并以authID为索引向数字盾服务发起数据导入请求。

   ```typescript
   private async importDataToDigitalShield(wrappedKey: Uint8Array, authID: bigint): Promise<void> {
     try {
       let buffer: ArrayBuffer = wrappedKey.buffer.slice(
         wrappedKey.byteOffset, wrappedKey.byteOffset + wrappedKey.byteLength
       );
       await trustedAuthentication.importData(buffer, authID);
       hilog.info(DOMAIN, 'testTag', 'importDataToDigitalShield success');
     } catch (error) {
       hilog.error(DOMAIN, 'testTag', 'importDataToDigitalShield failed', JSON.stringify(error));
       throw new Error('Import data to Digital Shield failed:' + (error as BusinessError).message);
     }
   }
   ```
4. 当应用卸载重新安装后，应用侧可向数字盾服务器发起密钥恢复申请。

   ```typescript
   private async exportDataFromDigitalShield(authID: bigint): Promise<ArrayBuffer> {
     try {
       const context = AppStorage.get('context') as Context;
       const buffer: ArrayBuffer = await CryptoUtils.ImportImage(); // 获取应用要在TUI界面展示的logo图片
       const label: trustedAuthentication.TUILable = {
         image: buffer,
         title: context.resourceManager.getStringSync($r('app.string.ExportKeyInfoLabel').id)
       };
       let data: ArrayBuffer = await trustedAuthentication.exportData(authID, label);
       hilog.info(0x0000, 'testTag', 'exportDataFromDigitalShield success, size=' + data.byteLength);
       return data;
     } catch (error) {
       hilog.error(0x0000, 'testTag', 'exportDataFromDigitalShield failed', JSON.stringify(error));
       throw new Error('Export data from Digital Shield failed:' + (error as BusinessError).message);
     }
   }
   ```
5. 将从数字盾服务获取的密钥数据，发送至密钥管理服务进行密钥导入恢复。

   ```typescript
   private async importKeyToHuks(wrappedKey: Uint8Array): Promise<void> {
     let wrapKeyProperties: Array<huks.HuksParam> = [
       {
         tag: huks.HuksTag.HUKS_TAG_KEY_WRAP_TYPE,
         value: huks.HuksKeyWrapType.HUKS_KEY_WRAP_TYPE_HUK_BASED
       }
     ];

     let wrapKeyOptions: huks.HuksOptions = {
       properties: wrapKeyProperties
     };

     try {
       await huks.unwrapKeyItem(KEY_ALIAS, wrapKeyOptions, wrappedKey);
       hilog.info(DOMAIN, 'testTag', 'importKeyToHuks success');
     } catch (error) {
       hilog.error(DOMAIN, 'testTag', 'importKeyToHuks failed', JSON.stringify(error));
       throw new Error('Import key to HUKS failed:' + (error as BusinessError).message);
     }
   }
   ```
