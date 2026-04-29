---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gameservice-single-access
title: 单机游戏登录
breadcrumb: 指南 > 应用服务 > Game Service Kit（游戏服务） > 基础游戏服务（必选） > 游戏登录 > 单机游戏登录
category: harmonyos-guides
scraped_at: 2026-04-29T13:38:09+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:32c44745c7b9de5938ca69b6649f5247537438f790e979cdbb88f08ad837d8d5
---

单机游戏是指数据本地化存储，不依赖服务器的游戏。

单机游戏接入基础游戏服务后，支持玩家使用华为账号快速进入游戏，且单机游戏的华为账号实名认证、未成年人防沉迷功能由基础游戏服务实现。

## 开发准备

### 创建游戏

在华为应用市场发布游戏，要求前往AppGallery Connect创建游戏类应用，具体操作请参见[创建HarmonyOS应用](../app/agc-help-create-app-0000002247955506.md)。其中：

* “应用类型”：选择“HarmonyOS应用”。
* “应用分类”：选择“游戏”。

说明

用于正式上架的游戏包名建议不要包含test、dev等信息。

### 申请版署实名认证

按照版署《关于开展网络游戏防沉迷实名认证系统接口对接工作的通知》，各游戏出版运营企业均要求在2021年6月1日前完成接入[网络游戏防沉迷实名认证系统](https://wlc.nppa.gov.cn/fcm_company/index.html#/login?redirect=/)，并获取“bizID（游戏备案识别码）”，再将bizID配置到AppGallery Connect，华为将为游戏自动对接国家新闻出版署的实名认证系统并开启强制实名认证，开发者无需进行额外的开发。具体操作请参见[版署实名认证申请](../games-guides/game-center-identification-applyfor-0000002392353221.md)。

### 生成签名证书

数字证书和Profile文件等签名信息可以确保游戏的完整性：

* 调试阶段：[手动签名](ide-signing.md#section297715173233)、[申请调试证书](../app/agc-help-debug-cert-0000002283256797.md)、[申请调试Profile](../app/agc-help-debug-profile-0000002248181278.md)。
* 发布阶段：[手动签名](ide-signing.md#section297715173233)、[申请发布证书](../app/agc-help-release-cert-0000002283336729.md)、[申请发布Profile](../app/agc-help-release-profile-0000002248341090.md)。

### 配置签名证书指纹

AppGallery Connect会自动生成证书对应的公钥信息，并计算出对应的SHA256指纹。开发者前往AppGallery Connect获取并配置SHA256指纹，且每个游戏至多添加4个签名证书指纹，配置签名证书指纹的具体操作请参见[配置公钥指纹](../app/agc-help-cert-fingerprint-0000002278002933.md)。

说明

请在调试阶段添加调试证书对应的指纹，在发布阶段添加发布证书对应的指纹。

### 配置APP ID和Client ID

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，在“开发与服务”下选择项目及项目下的游戏，获取“应用”下的APP ID和Client ID。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/jS2i11HASF60P2qHbBe-nQ/zh-cn_image_0000002589325255.png?HW-CC-KV=V1&HW-CC-Date=20260429T053808Z&HW-CC-Expire=86400&HW-CC-Sign=D3ACE5D9B6CF73E0EF0C2539BB585203A9A87969EB456F586FD3B47D09B249F1)
2. 在工程的entry模块module.json5文件中，新增metadata并配置client\_id和app\_id，同时新增requestPermissions以配置网络权限。如下所示：

   ```
   1. "module": {
   2. "name": "entry",
   3. "type": "xxx",
   4. "description": "xxxx",
   5. "mainElement": "xxxx",
   6. "deviceTypes": [],
   7. "pages": "xxxx",
   8. "abilities": [],
   9. "metadata": [ // 配置如下信息
   10. {
   11. "name": "client_id",
   12. "value": "xxxxxx" // 配置为前面步骤中获取的Client ID
   13. },
   14. {
   15. "name": "app_id",
   16. "value": "xxxxxx" // 配置为前面步骤中获取的APP ID
   17. }
   18. ],
   19. "requestPermissions": [ // 配置网络权限
   20. {
   21. "name": "ohos.permission.INTERNET"
   22. }
   23. ]
   24. }
   ```

### 配置APP ID映射关系

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，在“开发与服务”下选择项目及项目下的游戏，左侧菜单选择“构建 > 游戏服务”，在右侧点击“新增配置”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/H0hQDGsiRbu0QR0HqCEuoA/zh-cn_image_0000002589245191.png?HW-CC-KV=V1&HW-CC-Date=20260429T053808Z&HW-CC-Expire=86400&HW-CC-Sign=149E74060D58BFF8C4EB56FBBFE42E0B22C41E99F446855C3C6245ACE3EE2576)
2. 在弹出的“新增配置信息”窗口中选择HAP游戏和APK游戏，完成后点击“下一步”。

   说明

   请正确配置HAP游戏与APK游戏的映射关系。若开发者配置错误类型的游戏，将有提示框提示重新选择游戏。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/n7syxLfPTYypd85mlJ8xIw/zh-cn_image_0000002558765386.png?HW-CC-KV=V1&HW-CC-Date=20260429T053808Z&HW-CC-Expire=86400&HW-CC-Sign=BBB96231644EF806DA5545529588AC363B4726B7CB2A3AFEAF276E5E608A0507)

   | 信息项 | 说明 |
   | --- | --- |
   | HarmonyOS 5.0及以上游戏 | 请选择待上架的HAP游戏。 |
   | HarmonyOS 4及以下游戏 | 请选择已上架或待上架的APK游戏。 |
3. 在弹出的窗口中继续填写信息，完成后点击“下一步”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/eUvwFEy1RN6xisRKza9a3Q/zh-cn_image_0000002558605730.png?HW-CC-KV=V1&HW-CC-Date=20260429T053808Z&HW-CC-Expire=86400&HW-CC-Sign=B8328B89D0F98091C5A1623133E57B9DCA39C03348A7B664F4AEA39F915E68C2)
4. （可选）填写开发者服务器的回调地址，完成后点击“确定”提交APP ID映射关系的审批申请。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/04LofuCLQsW0fE2fKLVFAQ/zh-cn_image_0000002589325257.png?HW-CC-KV=V1&HW-CC-Date=20260429T053808Z&HW-CC-Expire=86400&HW-CC-Sign=314FF2EB4FF32E41B325D59FCFA3F34540B7E3C3B2777D0CECDEB23B49082BAB)
5. 若出现异常情况（例如在架状态不符合要求），将在提示框以红字提醒，建议点击“取消”并重新配置映射关系。若忽略异常情况点击“确定”继续提交申请，可能会造成映射关系审批不通过。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/5ca4RmgXQYiQy8ISq2OHEA/zh-cn_image_0000002589245193.png?HW-CC-KV=V1&HW-CC-Date=20260429T053808Z&HW-CC-Expire=86400&HW-CC-Sign=3DC2CBE7F27EE82A211197CABD84C5D095A0DB224896E96FD9E05546633FCE65)
6. 提交申请后，华为工作人员完成审核需要1-3个工作日，请耐心等待。

   APP ID映射关系生效后如需重新配置，请先提交映射关系的删除申请。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/OqA7HnzkRJeoy7nYiwXX6w/zh-cn_image_0000002558765388.png?HW-CC-KV=V1&HW-CC-Date=20260429T053808Z&HW-CC-Expire=86400&HW-CC-Sign=ADEC5C89C12A67E7329A4FA699B619480C9005AE74DEFE068FE38C92920A1172)

   配置/删除APP ID映射关系的审核结果将通过互动中心或邮件进行通知。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/UIchM7V2RMuyiaTeWw3hUA/zh-cn_image_0000002558605732.png?HW-CC-KV=V1&HW-CC-Date=20260429T053808Z&HW-CC-Expire=86400&HW-CC-Sign=B421E9B2FB45974DB7D7250B60D3EA806435909DFF9E2B6081F89C18317C9002)

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/6pnh3lX9QlO3dFHEKYvmjQ/zh-cn_image_0000002558765394.png?HW-CC-KV=V1&HW-CC-Date=20260429T053808Z&HW-CC-Expire=86400&HW-CC-Sign=9BE1A36DF462F2A5338ACEF6CDF9BF9E50B0A77B290DBD5E30DDFCAF5D6A9802)

1. 玩家启动游戏。
2. 游戏调用[init](../harmonyos-references/gameservice-gameplayer.md#gameplayerinit-1)接口初始化Game Service Kit。初始化后，弹出华为隐私协议窗口，玩家确认同意后，则继续往下执行。
3. 游戏调用[unionLogin](../harmonyos-references/gameservice-gameplayer.md#gameplayerunionlogin)接口，要求showLoginDialog参数为false，thirdAccountInfos参数传空数组。
4. 游戏顶部弹出欢迎横幅，并向游戏返回accountName（使用华为账号登录返回值为hw\_account）、accountIdentifier（选择华为账号登录返回值为hw\_account）、gamePlayerId等信息。
5. 调用[verifyLocalPlayer](../harmonyos-references/gameservice-gameplayer.md#gameplayerverifylocalplayer)接口，对用户设备登录的华为账号进行如下合规校验。合规校验通过后，玩家进入游戏。

   1. 若玩家未完成实名认证，[verifyLocalPlayer](../harmonyos-references/gameservice-gameplayer.md#gameplayerverifylocalplayer)接口自动弹出实名认证窗口要求玩家进行实名认证。
   2. 若玩家账号实名认证为未成年人，[verifyLocalPlayer](../harmonyos-references/gameservice-gameplayer.md#gameplayerverifylocalplayer)接口将自动检测未成年人的游戏时间。若玩家不在指定时间内登录游戏，将强制玩家退出游戏并返回[1002000006](../harmonyos-references/gameservice-error-code.md#section1002000006-玩家未成年并且当前不在可游戏时间)错误码。

## 接口说明

具体API说明请详见[接口文档](../harmonyos-references/gameservice-gameplayer.md)。

| 接口名 | 描述 |
| --- | --- |
| [init](../harmonyos-references/gameservice-gameplayer.md#gameplayerinit-1)(context: common.UIAbilityContext, callback: AsyncCallback<void>): void | 游戏初始化接口，使用默认的上下文信息，使用callback回调。 |
| [unionLogin](../harmonyos-references/gameservice-gameplayer.md#gameplayerunionlogin)(context: common.UIAbilityContext, loginParam: UnionLoginParam): Promise<UnionLoginResult> | 登录接口，通过Promise对象获取返回值。 |
| [verifyLocalPlayer](../harmonyos-references/gameservice-gameplayer.md#gameplayerverifylocalplayer)(context: common.UIAbilityContext, thirdUserInfo: ThirdUserInfo): Promise<void> | 合规校验接口，校验当前设备登录的华为账号的实名认证、游戏防沉迷信息，通过Promise对象获取返回值。 |

## 开发步骤

### 导入模块

导入Game Service Kit模块及相关公共模块。

```
1. import { gamePlayer } from '@kit.GameServiceKit';
2. import { common } from '@kit.AbilityKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { BusinessError } from '@kit.BasicServicesKit';
5. import { window } from '@kit.ArkUI';
```

### 初始化

调用[init](../harmonyos-references/gameservice-gameplayer.md#gameplayerinit-1)接口初始化Game Service Kit。

说明

* 调用接口时严格要求继承UIAbility，并且获取上下文的时机是onWindowStageCreate生命周期中页面加载成功后。
* 要求游戏先成功调用初始化[init](../harmonyos-references/gameservice-gameplayer.md#gameplayerinit-1)接口后再调用其他接口，否则将导致审核被驳回。

```
1. onWindowStageCreate(windowStage: window.WindowStage) {
2. windowStage.loadContent("pages/index", (err, data) => {
3. try {
4. gamePlayer.init(this.context,()=>{
5. hilog.info(0x0000, 'testTag', `Succeeded in initializing.`);
6. });
7. } catch (error) {
8. let err = error as BusinessError;
9. hilog.error(0x0000, 'testTag', `Failed to init. Code: ${err.code}, message: ${err.message}`);
10. }
11. });
12. }
```

初始化后，游戏弹出华为隐私协议窗口，用户同意签署协议，则继续往下执行。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/XU3CHTZwQ5yfMOcRH63rcA/zh-cn_image_0000002558765390.png?HW-CC-KV=V1&HW-CC-Date=20260429T053808Z&HW-CC-Expire=86400&HW-CC-Sign=3E0F997D1A0E6E27A5E5E72AF4BE1317F1D33481AFDA3944829A1813D0F00FC6)

若当前华为账号同意过游戏服务隐私协议，后续使用该华为账号登录的游戏将不会再弹出隐私协议窗口。

### 登录游戏

调用[unionLogin](../harmonyos-references/gameservice-gameplayer.md#gameplayerunionlogin)接口登录游戏。

```
1. let context = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
2. let request: gamePlayer.UnionLoginParam = {
3. showLoginDialog: false, // 是否弹出联合登录面板。true表示强制弹出面板，false表示优先使用玩家上一次的登录选择，不弹出联合登录面板，若玩家首次登录或卸载重装，则正常弹出
4. thirdAccountInfos: [] // 单机游戏请传空数组
5. };
6. try {
7. gamePlayer.unionLogin(context, request).then((result: gamePlayer.UnionLoginResult) => {
8. hilog.info(0x0000, 'testTag', `Succeeded in logging in: ${result?.accountName}`);
9. }).catch((error: BusinessError) => {
10. hilog.error(0x0000, 'testTag', `Failed to login. Code: ${error.code}, message: ${error.message}`);
11. });
12. } catch (error) {
13. let err = error as BusinessError;
14. hilog.error(0x0000, 'testTag', `Failed to login. Code: ${err.code}, message: ${err.message}`);
15. }
```

用户完成登录流程后，游戏顶部弹出欢迎横幅，并向游戏返回accountName（华为账号登录返回值为hw\_account）、gamePlayerId等信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/HV6Tqa5pQRm5i9MqCxvp8A/zh-cn_image_0000002558605734.png?HW-CC-KV=V1&HW-CC-Date=20260429T053808Z&HW-CC-Expire=86400&HW-CC-Sign=8E99E14C6AF3DF0E09CFCCD4FF691E665526005C44C8D4249DD6C522AA3CF83F)

### 合规校验

调用[verifyLocalPlayer](../harmonyos-references/gameservice-gameplayer.md#gameplayerverifylocalplayer)接口对用户设备登录华为账号的实名认证和未成年人防沉迷进行合规校验，校验通过后，玩家进入游戏。

```
1. let context = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
2. let request: gamePlayer.ThirdUserInfo = {
3. thirdOpenId: '' // 单机游戏传空
4. };
5. try {
6. gamePlayer.verifyLocalPlayer(context, request).then(() => {
7. hilog.info(0x0000, 'testTag', `Succeeded in verifying.`);
8. }).catch((error: BusinessError) => {
9. hilog.error(0x0000, 'testTag', `Failed to verify. Code: ${error.code}, message: ${error.message}`);
10. });
11. } catch (error) {
12. let err = error as BusinessError;
13. hilog.error(0x0000, 'testTag', `Failed to verify. Code: ${err.code}, message: ${err.message}`);
14. }
```

华为账号的实名认证、未成年人防沉迷由基础游戏服务实现，华为账号的支付合规控制（例如未成年人支付限额）由IAP Kit（应用内支付服务）实现。

| 合规校验 | 校验项 | 国家政策 | 解决方案 |
| --- | --- | --- | --- |
| 华为账号实名认证 | 校验用户设备登录的华为账号是否已实名认证。 | 根据相关法律法规要求，所有网络游戏玩家必须使用真实有效身份信息注册并登录网络游戏。 | 若玩家使用未实名认证的华为账号登录游戏时，基础游戏服务向玩家弹出实名认证窗口，要求玩家进行实名认证。若玩家取消实名认证，则返回[1002000004](../harmonyos-references/gameservice-error-code.md#section1002000004-实名认证返回强制实名但用户取消或需要强制实名但没有实名)错误码。 |
| 未成年人防沉迷 | 校验已实名认证为未成年人的华为账号是否在规定时间内登录游戏。 | 根据国家新闻出版署的最新规定，所有网络游戏企业仅可在周五、周六、周日和法定节假日每日20时至21时向未成年人提供1小时网络游戏服务，其他时间均不得以任何形式向未成年人提供网络游戏服务。 | - 已实名认证为未成年人的华为账号在规定时间内登录游戏，当游戏进行到晚上21时，基础游戏服务会弹窗提示玩家已到游戏时间，强制玩家退出游戏并返回[1002000006](../harmonyos-references/gameservice-error-code.md#section1002000006-玩家未成年并且当前不在可游戏时间)错误码。  - 已实名认证为未成年人的华为账号在非规定游戏时间内登录游戏，基础游戏服务会弹框提示玩家不允许游戏，强制玩家退出游戏并返回[1002000006](../harmonyos-references/gameservice-error-code.md#section1002000006-玩家未成年并且当前不在可游戏时间)错误码。 |
| 未成年人支付限额 | 校验已实名认证为未成年人的华为账号是否限额付费。 | 根据国家新闻出版署的最新规定，网络游戏企业不得为未满8周岁的用户提供游戏付费服务。同一网络游戏企业所提供的游戏付费服务，8周岁以上未满16周岁的用户，单次充值金额不得超过50元人民币，每月充值金额累计不得超过200元人民币；16周岁以上未满18周岁的用户，单次充值金额不得超过100元人民币，每月充值金额累计不得超过400元人民币。 | 已实名认证为未成年人的华为账号在游戏内超额付费，IAP Kit会弹窗提示消费金额超出限制。  用户在使用华为应用内支付时，华为会自动根据国家新闻出版署的要求进行支付限额控制，开发者无需处理。 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/YDK7pLFrRRKSwTO0VWXPig/zh-cn_image_0000002589245197.png?HW-CC-KV=V1&HW-CC-Date=20260429T053808Z&HW-CC-Expire=86400&HW-CC-Sign=A4A012BC7B21A2D271C946D2311D947ECDD932585828D15A9E41BE38CC2C7EB4)
