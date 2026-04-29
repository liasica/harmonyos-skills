---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-trustedauth-verifybypwd
title: 交易信息密码认证
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 数字盾服务 > 交易信息密码认证
category: harmonyos-guides
scraped_at: 2026-04-29T13:31:34+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1a7791a6413ca619b9f0b652ac16d8c5854c84952b0b00fffc2c9483d2892ec3
---

## 场景介绍

在交易信息密码认证场景中，可以利用创建的数字盾密码对交易信息进行认证，可通过密钥管理服务提供的签名认证功能来确认交易内容是否被篡改，以确保整个交易过程的安全性。

## 约束与限制

本功能目前仅在手机设备支持。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/2l7gn10IRoW9SyXB9b2IDw/zh-cn_image_0000002558764892.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053133Z&HW-CC-Expire=86400&HW-CC-Sign=2027D2510B1C5ACB9777A0A44AF4F695C9CDB042770319EF2E7E1C771BD9102E)

## 接口说明

接口及使用方法请参见[API参考](../harmonyos-references/devicesecurity-arktsapi-errcode-trusted-auth.md)。

| 接口名 | 描述 |
| --- | --- |
| [procContentAuthentication](../harmonyos-references/devicesecurity-trusted-auth-api.md#proccontentauthentication)(challenge: Uint8Array, authID: bigint, authMsg: AuthReqParams, label: TUILable): Promise<AuthToken> | 交易信息处理接口 |

## 交易信息密码认证界面介绍

如图1、图2、图3为使用数字盾密码进行交易认证时对应的TUI界面示例，其中交易信息密码认证分为两种场景：

1. 当用户交易信息不超过6行时，则以下图1中无翻页形式进行密码认证。
2. 当用户交易信息超过6行时，则以下图2-3中翻页形式进行密码认证，且当交易信息超过19行时，则Device Security Kit拒绝拉起TUI界面。

**图1** 无翻页密码认证

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/n9Jw_7ySRfmO7VMzomvXhA/zh-cn_image_0000002558605236.png?HW-CC-KV=V1&HW-CC-Date=20260429T053133Z&HW-CC-Expire=86400&HW-CC-Sign=20C770E138C2F5401D01F46A969346C2CA808212FC3542E9DBEA8383C80DDCC5)

**图2** 翻页密码认证-1

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/9rp0ec1dTLKRYSEmCaA-jg/zh-cn_image_0000002589324761.png?HW-CC-KV=V1&HW-CC-Date=20260429T053133Z&HW-CC-Expire=86400&HW-CC-Sign=DBCAE7A248978C3959F0A65E0A342A4BF95DCFE0BEF8440C59585BEB4788ECB7)

**图3** 翻页密码认证-2

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/_zq-AO8LSjONrl1ccjcpAQ/zh-cn_image_0000002589244699.png?HW-CC-KV=V1&HW-CC-Date=20260429T053133Z&HW-CC-Expire=86400&HW-CC-Sign=A73DACC23AE0A78B98BF29BE7E451FE016C57D770A57127B527158205E8BAE46)

交易信息格式说明如下：

1. **带标记格式**，以key:value|flag形式，flag取值如下：

   * 0：表示不展示该行内容。
   * 1：单行截断展示（若内容超出一行则截断）。
   * 2：自动换行展示（若内容超出一行则换行）。

   如当交易信息为“收款户名：王\*\*|1”，表示key为“收款户名”， value为“王\*\*”，flag为1，该内容若超过一行则截断显示。

   说明

   * 当行内出现“|”符号时，系统默认按此格式解析，若交易内容格式未全部以该格式输出，则会显示失败。
   * 若flag=1（截断模式）的key过长导致value无法显示时，则会显示失败。
2. **无标记格式**，直接输入内容（无“|”符号）。

   * 系统将完整展示所有内容，超出一行时自动换行。

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
   8. import { util } from '@kit.ArkTS';
   ```
2. 发起交易认证前，需从服务器获取当前账号在[设置数字盾密码](devicesecurity-trustedauth-setpwd.md)时获取的authID。
3. 参考密钥管理服务提供的[签名/验签指导](huks-signing-signature-verification-arkts.md)，初始化签名会话。

   说明

   * 设置签名密钥时密钥属性集合中需要指定tag: huks.HuksTag.HUKS\_TAG\_KEY\_SECURE\_SIGN\_TYPE值为huks.HuksSecureSignType.HUKS\_SECURE\_SIGN\_WITH\_AUTHINFO，即可对附加的交易信息做签名认证。

   ```
   1. // 设置签名密钥属性示例
   2. let properties: Array<huks.HuksParam> = [{
   3. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
   4. value: huks.HuksKeyAlg.HUKS_ALG_ECC
   5. }, {
   6. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
   7. value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256
   8. }, {
   9. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
   10. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN
   11. }, {
   12. tag: huks.HuksTag.HUKS_TAG_DIGEST,
   13. value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
   14. },
   15. // 表示对附加的交易信息做签名认证
   16. {
   17. tag: huks.HuksTag.HUKS_TAG_KEY_SECURE_SIGN_TYPE,
   18. value: huks.HuksSecureSignType.HUKS_SECURE_SIGN_WITH_AUTHINFO
   19. }];
   ```
4. 调用交易认证接口，发起密码认证交易申请，当用户密码认证通过后，即可获得携带交易信息hash的authToken。

   ```
   1. async function ContentVerifyByPwd(challenge: Uint8Array, context: common.UIAbilityContext):Promise<trustedAuthentication.AuthToken> {
   2. try {
   3. const authID: bigint = 11842183505170721246n;//实际填充为从服务器获取到的账号对应的authID值
   4. const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
   5. const fileData : Uint8Array = await resourceMgr.getRawFileContent('test_logo_rgba.png'); //实际使用时请替换为应用要在TUI界面展示的logo图片名称
   6. const reqParams:trustedAuthentication.AuthReqParams = {
   7. reqType: trustedAuthentication.AuthType.AUTH_TYPE_TUI_PIN,
   8. authContent: ["用户：王xx", "账号：95588180804408xxxx", "交易金额：1000000000"],//实际使用时填充为交易信息，每一行交易信息为其中的一个字符串成员
   9. }
   10. const buffer = fileData.buffer;
   11. const label:trustedAuthentication.TUILable = {
   12. image: buffer as ArrayBuffer,
   13. title: "密码交易认证",
   14. }
   15. const result = await trustedAuthentication.procContentAuthentication(challenge, authID, reqParams, label);
   16. return result;
   17. } catch (err) {
   18. hilog.error(0x0000, 'testTag', `Failed to procContentAuthentication, code:${err.code}, message:${err.message}`);
   19. throw new Error('Content verify by password failed:' + (err as BusinessError).message);
   20. }
   21. }
   22. const rand = cryptoFramework.createRandom();
   23. const len: number = 32;
   24. const challenge: Uint8Array = rand?.generateRandomSync(len)?.data;//实际使用时请替换为通过UniversalKeystoreKit初始化会话获取的challenge
   25. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
   26. const authToken: trustedAuthentication.AuthToken = await ContentVerifyByPwd(challenge, context);
   ```
5. 参考密钥管理服务提供的[针对携带认证信息的签名/验签指导](huks-signing-signature-verification-arkts.md#eccsha256携带认证信息的签名类型), 对交易信息authToken数据进行签名验证，并结束会话。

   说明

   需要注意的是，在交易认证过程中输入的交易信息格式如下：

   ```
   1. //示例交易信息
   2. authContent: ["用户：王xx", "账号：95588180804408xxxx", "交易金额：1000000000"];
   ```

   而密钥管理服务验签时的inputData信息为Uint8Array，需要将所有信息按照\n拼接，并将UTF-8信息转换为Uint8Array

   ```
   1. function encodeUtf8(s: string): number[] {
   2. const encoder = new util.TextEncoder();

   4. const dest = new Uint8Array(s.length * 4);
   5. const result = encoder.encodeIntoUint8Array(s, dest);
   6. const encodedBytes = dest.subarray(0, result.written);
   7. return Array.from(encodedBytes);
   8. };
   9. //实际为应用向密钥管理服务传入的验签数据
   10. let str = "用户：王xx\n账号：95588180804408xxxx\n交易金额：1000000000";
   11. const utf8Bytes = new Uint8Array(encodeUtf8(str));
   ```
6. 参考密钥管理服务提供的[签名/验签指导](huks-signing-signature-verification-arkts.md), 对签名数据进行验签操作，验签通过后可完成对应账户的转账扣款。
