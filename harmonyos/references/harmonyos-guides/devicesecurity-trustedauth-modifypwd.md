---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-trustedauth-modifypwd
title: 修改数字盾密码
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 数字盾服务 > 数字盾密码管理 > 修改数字盾密码
category: harmonyos-guides
scraped_at: 2026-11-19T09:48:06+08:00
doc_updated_at: 2026-10-28
content_hash: sha256:74e3fd2ce67f57353238c019f5cb76a6e97e82f82dd23d7e068d1ff7e712e1a5
---

## 场景介绍

激活数字盾后，用户可在完成旧密码认证后，修改数字盾密码信息。

## 约束与限制

本功能在6.1.1(24)之前版本仅支持Phone；6.1.1(24)及之后版本，新增支持具备TUI能力的PC/2in1、具备TUI能力的Tablet。可通过接口[checkConfirmUITextFormat](../harmonyos-references/devicesecurity-trusted-auth-api.md#trustedauthenticationcheckconfirmuitextformat)查询设备是否具备TUI能力。不支持的设备在调用数字盾服务相关业务接口时，返回错误码1019100016。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/YmzXL_jkRN2d_MslfLEMhA/zh-cn_image_0000002791565730.jpg?HW-CC-KV=V1&HW-CC-Date=20261119T014715Z&HW-CC-Expire=31536000000&HW-CC-Sign=8BA11D463B6C62F6D5684330CA1FAFA4AA98F27157B10A4D5D2024D0DA32C3C3)

## 接口说明

接口及使用方法请参见[API参考](../harmonyos-references/devicesecurity-trusted-auth-api.md)。

| 接口名 | 描述 |
| --- | --- |
| [modifyTrustedAuthenticationPwd](../harmonyos-references/devicesecurity-trusted-auth-api.md#trustedauthenticationmodifytrustedauthenticationpwd)(challenge: Uint8Array, pwdInfo: PasswordInfo, authID: bigint, label: TUILable): Promise<AuthToken> | 修改数字盾密码。 |

## 修改数字盾密码界面介绍

如图1、图2为修改数字盾密码时对应的TUI界面示例，用户需使用旧密码认证通过后，方可设置新密码。密码认证失败时，剩余认证次数减1，当剩余认证次数为0时，则锁定数字盾服务。新密码长度、对应TUI应用图标以及当前企业开发者应用场景说明均由开发者调用接口时传入。

**图1** 旧密码认证

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/6cEPSJMDQ1CFlNHabZ1HXg/zh-cn_image_0000002820525683.png?HW-CC-KV=V1&HW-CC-Date=20261119T014715Z&HW-CC-Expire=31536000000&HW-CC-Sign=4936B776AC387FBE1BC1FF72859C42EE048E7C5AD77F39C349CF69A139F83C7C)

**图2** 新密码设置

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/7yBzL4ObSgiOvdCczij8wg/zh-cn_image_0000002820405683.png?HW-CC-KV=V1&HW-CC-Date=20261119T014715Z&HW-CC-Expire=31536000000&HW-CC-Sign=DD90657546AF84B4431D3AACCCAAE2B30081DE39CDCBA995046A45075CD4B79C)

## 开发步骤

1. 导入huks 、trustedAuthentication 和相关依赖模块。

   ```typescript
   import { resourceManager } from '@kit.LocalizationKit'
   import { huks } from '@kit.UniversalKeystoreKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { trustedAuthentication } from '@kit.DeviceSecurityKit';
   import { cryptoFramework } from '@kit.CryptoArchitectureKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { common } from '@kit.AbilityKit';
   ```
2. 修改密码前，需从服务器获取当前账号在[设置数字盾密码](devicesecurity-trustedauth-setpwd.md)时获取的authID。
3. 参考密钥管理服务提供的[签名/验签指导](huks-signing-signature-verification-arkts.md)，初始化签名会话。
4. 调用数字盾服务修改密码接口，发起数字盾密码修改申请。

   ```typescript
   async ModifyPwd(challenge: Uint8Array, assetName: string): Promise<trustedAuthentication.AuthToken> {
     try {
       const passwordInfo: trustedAuthentication.PasswordInfo = {
         pwdType: trustedAuthentication.PasswordType.PASSWORD_TYPE_DIGITAL,
         pwdMaxLength: 10,
         pwdMinLength: 6,
         maxAuthFailCount: 6
       };
       let resArray: Uint8Array = await AssetUtils.QueryDataFromAssetStore(assetName);
       let credentialID: bigint = CryptoUtils.uint8ArrayToBigInt(resArray); // 实际填充为从服务器获取到的账号对应的credentialID值
       const context = AppStorage.get('context') as Context;
       const buffer: ArrayBuffer = await CryptoUtils.ImportImage(); // 获取应用要在TUI界面展示的logo图片
       const label: trustedAuthentication.TUILable = {
         image: buffer,
         title: context.resourceManager.getStringSync($r('app.string.ModifyShield').id)
       }
       const authInfo =
         await trustedAuthentication.modifyTrustedAuthenticationPwd(challenge, passwordInfo, credentialID, label);
       hilog.info(0x0000, 'testTag', 'Modify Shield Success：', authInfo.authToken);
       return authInfo;
     } catch (error) {
       hilog.error(0x0000, 'testTag', 'Modify Shield Fail：', error);
       throw new Error('Modify Shield Fail：' + (error as BusinessError).message);
     }
   }
   ```
5. 参考密钥管理服务提供的[签名/验签指导](huks-signing-signature-verification-arkts.md), 对通过修改密码获取到的authToken数据进行签名，并结束会话。
