---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-trustedauth-setpwd
title: 设置数字盾密码
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 数字盾服务 > 数字盾密码管理 > 设置数字盾密码
category: harmonyos-guides
scraped_at: 2026-04-29T13:31:33+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8e9f5b4a6c3ada608d084127fe18acfad7576984484a68c1659cc887db80c018
---

## 场景介绍

用户首次激活数字盾时，需通过可信用户交互（全称Trusted User Interface，下文简称TUI）安全界面设置专用密码，后续进行交易认证时，将通过该密码完成安全验证。

## 约束与限制

本功能目前仅在手机设备支持。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/E6JNVeE7Qb2wiUMIlxEWFw/zh-cn_image_0000002558605232.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053132Z&HW-CC-Expire=86400&HW-CC-Sign=B0998ACE160E83A5F56AC9E85747EF54283ABD2AC9F2741D0DEB984109BAD981)

## 接口说明

接口及使用方法请参见[API参考](../harmonyos-references/devicesecurity-trusted-auth-api.md)。

| 接口名 | 描述 |
| --- | --- |
| [enableTrustedAuthentication](../harmonyos-references/devicesecurity-trusted-auth-api.md#enabletrustedauthentication)(challenge: Uint8Array, pwdInfo: PasswordInfo, label: TUILable): Promise<AuthInfo> | 创建数字盾密码 |

## 开通数字盾界面介绍

如图为开通数字盾服务时对应的TUI（Trusted User Interface）界面示例，其中密码长度、对应TUI应用图标以及当前应用场景说明均由开发者调用接口时传入，当设置盾密码长度不符合要求、密码强度低、两次密码设置不一致时，均会有对应失败报错提醒。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/YKWMnWtDRuGrg_OQpoGNTg/zh-cn_image_0000002589324757.png?HW-CC-KV=V1&HW-CC-Date=20260429T053132Z&HW-CC-Expire=86400&HW-CC-Sign=683F99496C3C340C57DD01AA8452CC0B3B4E1739D9132386859E2E55A67D086E)

## 开发步骤

1. 导入huks 、trustedAuthentication 和相关依赖模块。

   ```
   1. import { resourceManager } from '@kit.LocalizationKit'
   2. import { huks } from '@kit.UniversalKeystoreKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   4. import { trustedAuthentication } from '@kit.DeviceSecurityKit';
   5. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
   6. import { hilog } from '@kit.PerformanceAnalysisKit';
   7. import { common } from '@kit.AbilityKit';
   ```
2. 参考密钥管理服务提供的[密钥生成开发指导](huks-key-generation-arkts.md)，使用指定的会话密钥别名及指定密钥属性集合完成密钥生成。

   说明

   创建密钥时指定密钥属性集合中身份认证类型tag: huks.HuksTag.HUKS\_TAG\_USER\_AUTH\_TYPE时，必须要包括huks.HuksUserAuthType.HUKS\_USER\_AUTH\_TYPE\_TUI\_PIN认证方式，其余认证类型可以根据业务需要进行定制配置。

   ```
   1. // 密钥属性集示例
   2. let properties: Array<huks.HuksParam> = [{
   3. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
   4. value: huks.HuksKeyAlg.HUKS_ALG_ECC
   5. }, {
   6. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
   7. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN | huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY
   8. }, {
   9. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
   10. value: huks.HuksKeySize.HUKS_ECC_KEY_SIZE_256,
   11. }, {
   12. tag: huks.HuksTag.HUKS_TAG_DIGEST,
   13. value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
   14. },
   15. {
   16. tag: huks.HuksTag.HUKS_TAG_KEY_AUTH_PURPOSE,
   17. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN
   18. },
   19. // 指定密钥身份认证的类型：TUI_PIN/指纹/人脸
   20. {
   21. tag: huks.HuksTag.HUKS_TAG_USER_AUTH_TYPE,
   22. value: huks.HuksUserAuthType.HUKS_USER_AUTH_TYPE_TUI_PIN | huks.HuksUserAuthType.HUKS_USER_AUTH_TYPE_FINGERPRINT | huks.HuksUserAuthType.HUKS_USER_AUTH_TYPE_FACE
   23. },
   24. // 指定密钥安全授权的类型（失效类型）：新录入生物特征（如指纹）后无效
   25. {
   26. tag: huks.HuksTag.HUKS_TAG_KEY_AUTH_ACCESS_TYPE,
   27. value: huks.HuksAuthAccessType.HUKS_AUTH_ACCESS_ALWAYS_VALID
   28. },
   29. // 指定挑战值的类型：默认类型
   30. {
   31. tag: huks.HuksTag.HUKS_TAG_CHALLENGE_TYPE,
   32. value: huks.HuksChallengeType.HUKS_CHALLENGE_TYPE_NORMAL
   33. }];
   ```
3. 参考密钥管理服务提供的[签名/验签指导](huks-signing-signature-verification-arkts.md)，初始化签名会话。
4. 调用设置密码接口，发起数字盾密码创建申请。

   ```
   1. // 设置数字盾密码
   2. async function SetPwd(challenge: Uint8Array, context: common.UIAbilityContext):Promise<trustedAuthentication.AuthInfo> {
   3. try {
   4. // 数字盾密码定制属性参数
   5. const passwordInfo: trustedAuthentication.PasswordInfo = {
   6. pwdType: trustedAuthentication.PasswordType.PASSWORD_TYPE_DIGITAL,
   7. pwdMaxLength: 10,
   8. pwdMinLength: 6,
   9. maxAuthFailCount: 6
   10. };

   12. const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
   13. const fileData : Uint8Array = await resourceMgr.getRawFileContent('test_logo_rgba.png');//实际使用时请替换为应用要在TUI界面展示的logo图片名称
   14. const buffer = fileData.buffer;
   15. const label:trustedAuthentication.TUILable = {
   16. image: buffer as ArrayBuffer,
   17. title: "开通数字盾",
   18. }
   19. const authInfo = await trustedAuthentication.enableTrustedAuthentication(challenge, passwordInfo, label);
   20. return authInfo;
   21. } catch (err) {
   22. hilog.error(0x0000, 'testTag', `Failed to enableTrustedAuthentication, code:${err.code}, message:${err.message}`);
   23. throw new Error('Enable trusted authentication failed:' + (err as BusinessError).message);
   24. }
   25. }
   26. const rand = cryptoFramework.createRandom();
   27. const len: number = 32;
   28. const challenge: Uint8Array = rand?.generateRandomSync(len)?.data;//实际使用时请替换为通过UniversalKeystoreKit初始化会话获取的challenge
   29. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
   30. let authInfo: trustedAuthentication.AuthInfo = await SetPwd(challenge, context);
   ```
5. 参考密钥管理服务提供的[签名/验签指导](huks-signing-signature-verification-arkts.md), 对通过密码设置获取到的authToken数据进行签名，并结束会话。
