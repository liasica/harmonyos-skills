---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gameservice-gameplayer-huawei
title: 接入华为账号登录（必选）
breadcrumb: 指南 > 应用服务 > Game Service Kit（游戏服务） > 基础游戏服务（必选） > 游戏登录 > 网络游戏登录 > 接入华为账号登录（必选）
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:07+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:03491a5535dd9754800470d055a2a91b7b1c3619b8a833d839c6114c2d622998
---

接入后，华为平台会将HarmonyOS 4及以下游戏的玩家标识playerId/openId赋值给HarmonyOS 5.0及以上游戏的玩家标识gamePlayerId，为新老系统游戏的账号资产（角色、区服信息、游戏进度等）实现互通。互通前后，华为账号ID不会发生变化，也不涉及开发者服务器和数据库层面的变动。

华为账号的实名认证、未成年人防沉迷由基础游戏服务实现，华为账号的支付合规控制（例如未成年人支付限额）由IAP Kit（应用内支付服务）实现。

## 接入策略

游戏必须接入华为账号登录。

## 开发准备

### 创建游戏

在华为应用市场发布游戏，要求前往AppGallery Connect创建游戏类应用，具体操作请参见[创建HarmonyOS应用](../app/agc-help-create-app-0000002247955506.md)。其中：

* “应用类型”：选择“HarmonyOS应用”。
* “应用分类”：选择“游戏”。

**说明** 

用于正式上架的游戏包名建议不要包含test、dev等信息。

### 申请版署实名认证

按照版署《关于开展网络游戏防沉迷实名认证系统接口对接工作的通知》，各游戏出版运营企业均要求在2021年6月1日前完成接入[网络游戏防沉迷实名认证系统](https://wlc.nppa.gov.cn/fcm_company/index.html#/login?redirect=/)，并获取“bizID（游戏备案识别码）”，再将bizID配置到AppGallery Connect，华为将为游戏自动对接国家新闻出版署的实名认证系统并开启强制实名认证，开发者无需进行额外的开发。具体操作请参见[版署实名认证申请](../games-guides/game-center-identification-applyfor-0000002392353221.md)。

### 申请备案

请参考[APP核准（APP备案）指引](../App/50130.md)完成游戏备案。

**说明** 

HarmonyOS 4及以下游戏与HarmonyOS 5.0及以上游戏要求分别申请备案。

### 生成签名证书

数字证书和Profile文件等签名信息可以确保游戏的完整性：

* 调试阶段：[手动签名](ide-signing-manual.md)、[申请调试证书](../app/agc-help-debug-cert-0000002283256797.md)、[申请调试Profile](../app/agc-help-debug-profile-0000002248181278.md)。
* 发布阶段：[手动签名](ide-signing-manual.md)、[申请发布证书](../app/agc-help-release-cert-0000002283336729.md)、[申请发布Profile](../app/agc-help-release-profile-0000002248341090.md)。

### 配置签名证书指纹

AppGallery Connect会自动生成证书对应的公钥信息，并计算出对应的SHA256指纹。开发者前往AppGallery Connect获取并配置SHA256指纹，且每个游戏至多添加4个签名证书指纹，配置签名证书指纹的具体操作请参见[配置公钥指纹](../app/agc-help-cert-fingerprint-0000002278002933.md)。

**说明** 

请在调试阶段添加调试证书对应的指纹，在发布阶段添加发布证书对应的指纹。

### 配置APP ID和Client ID

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，在“开发与服务”下选择项目及项目下的游戏，获取“应用”下的APP ID和Client ID。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/3Jffv_DsSY6ogH4MGjWkpA/zh-cn_image_0000002712245148.png)
2. 在工程的entry模块module.json5文件中，新增metadata并配置client\_id和app\_id，同时新增requestPermissions以配置网络权限。如下所示：

   ```typescript
   "module": {
     "name": "entry",
     "type": "xxx",
     "description": "xxxx",
     "mainElement": "xxxx",
     "deviceTypes": [],
     "pages": "xxxx",
     "abilities": [],
     "metadata": [ // 配置如下信息
       {
         "name": "client_id",
         "value": "xxxxxx" // 配置为前面步骤中获取的Client ID
       },
       {
         "name": "app_id",
         "value": "xxxxxx" // 配置为前面步骤中获取的APP ID
       }
     ],
     "requestPermissions": [ // 配置网络权限
       {
         "name": "ohos.permission.INTERNET"
       }
     ]
   }
   ```

### 配置APP ID映射关系

为了实现HarmonyOS 5.0及以上系统与HarmonyOS 4及以下系统间的游戏资产互通，开发者在上架游戏前，需要配置APP ID映射关系。

开发者需在配置映射关系时确保HarmonyOS 4及以下游戏的玩家标识类型（playerId/openId）准确无误，以保障数据继承的准确性。

若APP ID映射关系缺失或配置错误，可能导致账号资产无法互通。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，在“开发与服务”下选择项目及项目下的游戏，左侧菜单选择“构建 > 游戏服务”，在右侧点击“新增配置”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/zEy4oRU3Ti2cP8-Xdpd6wA/zh-cn_image_0000002742004097.png)
2. 在弹出的“新增配置信息”窗口中选择HAP游戏和APK游戏，完成后点击“下一步”。

   **说明** 

   请正确配置HAP游戏与APK游戏的映射关系。若开发者配置错误类型的游戏，将有提示框提示重新选择游戏。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/chZHVFylRP20E2MFZNWs5A/zh-cn_image_0000002712405108.png)

   | 信息项 | 说明 |
   | --- | --- |
   | HarmonyOS 5.0及以上游戏 | 请选择待上架的HAP游戏。 |
   | HarmonyOS 4及以下游戏 | 请选择已上架或待上架的APK游戏。  若无待上架的游戏，请先创建草稿状态的APK游戏。 |
3. 在弹出的窗口中继续填写信息，完成后点击“下一步”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/4DdWP3zZQq60uEvwop_9Vg/zh-cn_image_0000002742124057.png)

   | 信息项 | 说明 |
   | --- | --- |
   | 支持数据继承的玩家标识类型 | 请选择HarmonyOS 4及以下游戏的玩家标识类型：  - **playerId**：老系统游戏确认使用**playerId**作为玩家标识，请选择“**playerId**”。选择后，新系统游戏的玩家标识gamePlayerId=playerId。  - **openId**：如下情况请选择“**openId**”  - 情况一：老系统游戏确认使用**openId**作为玩家标识。  - 情况二：老系统游戏确认使用**unionId**作为玩家标识。此时，请同时勾选“使用了unionId”，并通过[通过gamePlayerId获取playerId/openId/unionId](../harmonyos-references/gameservice-convertid.md)用gamePlayerId（openId）换取unionId，若unionId未在游戏侧找到玩家记录，则当前玩家为新系统游戏的新用户。  - 情况三：部分游戏由于处于playerId替换为openId方案的过渡期，导致老系统游戏的玩家标识存在**playerId与openId混用**的情况，例如A玩家使用openId，B玩家使用playerId。此时，若无法通过gamePlayerId在游戏侧找到玩家记录，可通过[通过gamePlayerId获取playerId/openId/unionId](../harmonyos-references/gameservice-convertid.md)接口用gamePlayerId（openId）换取playerId，若playerId能在游戏侧找到玩家记录，表明该玩家是使用playerId作为玩家标识的老用户，否则该玩家为新系统游戏的新用户。  - 情况四：HarmonyOS 4及以下游戏未上架时。 |
   | 接入unionId的HarmonyOS 4及以下游戏实现数据继承需要进行转换处理 | 若老系统的游戏确认使用**unionId**作为玩家标识，请勾选“使用了unionId”。 |

   **说明** 

   玩家标识严格区分大小写，例如gamePlayerId=xxx和gamePlayerId=XXX表示两个不同的玩家。
4. （可选）填写开发者服务器的回调地址，回调地址要求支持HTTPS协议，且具有合法商用证书，完成后点击“确定”提交APP ID映射关系的审批申请。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/BxIRryCgRzyPaYC_aI5WZw/zh-cn_image_0000002712245150.png)

   若用户注销华为账号，华为游戏服务器向开发者服务器发送事件通知，通知游戏自行清理账号数据。
5. 若出现异常情况，将在如下提示框以红字提醒。建议点击“取消”并重新配置映射关系，若忽略异常情况点击“确定”继续提交申请，可能会造成映射关系审批不通过。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/74HWFEpMRbaf57103AlC2A/zh-cn_image_0000002742004099.png)
6. 提交申请后，华为工作人员完成审核需要1-3个工作日，请耐心等待。APP ID映射关系生效后如需重新配置，请先提交映射关系的删除申请。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/pd6Q_KLsSuye2TuNdbm7LQ/zh-cn_image_0000002712405110.png)

   配置/删除APP ID映射关系的审核结果将通过互动中心或邮件进行通知。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/5ytqbKuuT6agYlZ3FPkqHA/zh-cn_image_0000002742124059.png)

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/huEFzfHzTDaevH1WtYDGsg/zh-cn_image_0000002712245152.png)

1. 玩家启动游戏。
2. 游戏调用[init](../harmonyos-references/gameservice-gameplayer.md#gameplayerinit-1)接口初始化Game Service Kit。初始化后，弹出华为游戏服务与隐私的声明窗口，玩家确认同意后，则继续往下执行。
3. 游戏调用[on](../harmonyos-references/gameservice-gameplayer.md#gameplayeronplayerchanged)接口注册事件监听。若监听到[PlayerChangedEvent](../harmonyos-references/gameservice-gameplayer.md#playerchangedevent)事件，先清除本地缓存信息，再重新调用[unionLogin](../harmonyos-references/gameservice-gameplayer.md#gameplayerunionlogin)登录逻辑，showLoginDialog设置为true，重新拉起联合登录面板。
4. 游戏调用[unionLogin](../harmonyos-references/gameservice-gameplayer.md#gameplayerunionlogin)接口。

   **说明** 

   建议使用session缓存登录状态，玩家下次登录进入游戏无需再调用[unionLogin](../harmonyos-references/gameservice-gameplayer.md#gameplayerunionlogin)接口，但仍需调用[verifyLocalPlayer](../harmonyos-references/gameservice-gameplayer.md#gameplayerverifylocalplayer)接口。
5. 向玩家展示联合登录面板。
6. 玩家选择“华为账号登录”。
7. 游戏顶部弹出欢迎横幅，并向游戏返回accountName（选择华为账号登录返回值为hw\_account）、accountIdentifier（选择华为账号登录返回值为hw\_account）、gamePlayerId等信息。
8. 【**异步流程**】玩家信息核验。建议在服务端校验玩家信息，若没有服务器，无需校验一致性。

   1. 游戏调用[createLoginWithHuaweiIDRequest](../harmonyos-references/account-api-authentication.md#createloginwithhuaweiidrequest)接口，获取用于服务器校验的Authorization Code。

      **说明** 

      Authorization Code只有5分钟有效期，且仅能使用一次，不可复用。
   2. 游戏向开发者服务器上传Authorization Code、gamePlayerId等信息。
   3. 开发者服务器携带Authorization Code，请求[获取用户级凭证](../harmonyos-references/account-api-obtain-user-token.md)接口，获取Access Token。
   4. 开发者服务器携带Access Token，请求[获取玩家标识](../harmonyos-references/gameservice-getplayerinfo.md)接口，获取gamePlayerId。
   5. 开发者服务器把从华为游戏服务器获取的gamePlayerId与客户端获取的gamePlayerId进行一致性核验。若核验不通过，已通过合规校验进入游戏的玩家也需强制退出游戏。
9. 游戏调用[verifyLocalPlayer](../harmonyos-references/gameservice-gameplayer.md#gameplayerverifylocalplayer)接口，校验当前用户设备登录华为账号的实名认证、未成年人防沉迷信息。校验通过后，玩家进入游戏。若校验未通过请根据返回的[错误码](../harmonyos-references/errorcode-gameservice.md)进行相应处理。
10. 若玩家在游戏内创建角色，建议游戏调用[savePlayerRole](../harmonyos-references/gameservice-gameplayer.md#gameplayersaveplayerrole)上报角色信息。

    **说明** 

    若游戏无区服角色，或限制为1个区服角色，此时，建议游戏允许玩家直接进入游戏，而无需玩家点击“进入游戏”或者选择区服角色才能进入游戏。

## 接口说明

具体API说明请详见[接口文档](../harmonyos-references/gameservice-gameplayer.md)。

| 接口名 | 描述 |
| --- | --- |
| [init](../harmonyos-references/gameservice-gameplayer.md#gameplayerinit-1)(context: common.UIAbilityContext, callback: AsyncCallback<void>): void | 游戏启动时，需要对Game Service Kit进行初始化。在调用其他API接口前，必须先调用此API接口。使用callback异步回调。 |
| [on](../harmonyos-references/gameservice-gameplayer.md#gameplayeronplayerchanged)(type: 'playerChanged', callback: Callback<PlayerChangedResult>): void | 玩家变化事件监听接口，通过callback异步回调获取玩家变化结果信息。 |
| [unionLogin](../harmonyos-references/gameservice-gameplayer.md#gameplayerunionlogin)(context: common.UIAbilityContext, loginParam: UnionLoginParam): Promise<UnionLoginResult> | 华为账号和游戏官方账号联合登录接口，通过Promise对象获取返回值。 |
| [verifyLocalPlayer](../harmonyos-references/gameservice-gameplayer.md#gameplayerverifylocalplayer)(context: common.UIAbilityContext, thirdUserInfo: ThirdUserInfo): Promise<void> | 合规校验接口，校验当前设备登录的华为账号的实名认证、游戏防沉迷信息，通过Promise对象获取返回值。 |
| [savePlayerRole](../harmonyos-references/gameservice-gameplayer.md#gameplayersaveplayerrole)(context: common.UIAbilityContext, request: GSKPlayerRole): Promise<void> | 保存角色信息到华为游戏服务器，使用默认的上下文信息，通过Promise对象获取返回值。 |

## 开发步骤

### 接口调用流程图

接入华为账号登录的接口调用流程如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/K1tGNZrWQDaoPL01h0tM4g/zh-cn_image_0000002742004101.png)

### 导入模块

导入Account Kit模块、Game Service Kit模块及相关公共模块。

```typescript
import { authentication } from '@kit.AccountKit';
import { gamePlayer } from '@kit.GameServiceKit';
import { common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { Callback, BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';
import { util } from '@kit.ArkTS';
```

### 初始化

调用[init](../harmonyos-references/gameservice-gameplayer.md#gameplayerinit-1)接口初始化Game Service Kit。

**说明** 

* 调用接口时严格要求继承UIAbility，并且获取上下文的时机是onWindowStageCreate生命周期中页面加载成功后。
* 要求游戏先成功调用初始化[init](../harmonyos-references/gameservice-gameplayer.md#gameplayerinit-1)接口后再调用其他接口，否则将导致审核被驳回。

```typescript
onWindowStageCreate(windowStage: window.WindowStage) {
  windowStage.loadContent('pages/index', (err, data) => {
    try {
      gamePlayer.init(this.context, ()=>{
        hilog.info(0x0000, 'testTag', `Succeeded in initializing.`);
      });
    } catch (error) {
      let err = error as BusinessError;
      hilog.error(0x0000, 'testTag', `Failed to init. Code: ${err.code}, message: ${err.message}`);
    }
  });
}
```

初始化后，游戏弹出华为游戏服务与隐私的声明窗口，用户同意签署，则继续往下执行。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/AL5gHdJeTEqvbObvNGWu7g/zh-cn_image_0000002712405112.png)

若当前华为账号同意过华为游戏服务与隐私的声明，后续使用该华为账号登录的游戏将不再弹出该窗口。

### 注册事件监听

调用[on](../harmonyos-references/gameservice-gameplayer.md#gameplayeronplayerchanged)接口注册[PlayerChangedEvent](../harmonyos-references/gameservice-gameplayer.md#playerchangedevent)事件监听，及时感知游戏过程中账号的变化。

```typescript
private onPlayerChangedEventCallback(result: gamePlayer.PlayerChangedResult) {
  if (result.event === gamePlayer.PlayerChangedEvent.SWITCH_GAME_ACCOUNT) {
     // ...
    // 游戏号已切换，完成本地缓存清理工作后，再次调用unionLogin接口等
  }
}
// ...
// 调用on接口注册playerChanged事件监听
try {
  gamePlayer.on('playerChanged', this.onPlayerChangedEventCallback);
  hilog.info(0x0000, 'testTag', `Succeeded in registering.`);
} catch (error) {
  let err = error as BusinessError;
  hilog.error(0x0000, 'testTag', `Failed to register. Code: ${err.code}, message: ${err.message}`);
}
```

目前有如下两个场景可以监听到账号变化：

| 序号 | 能监听到账号切换的场景 | 监听到账号切换后的措施 |
| --- | --- | --- |
| 场景一 | 玩家点击“欢迎横幅->管理->切换”或者点击“欢迎横幅->管理->X”。  详情请参见[欢迎横幅管理游戏账号](gameservice-gameplayer-huawei.md#欢迎横幅管理游戏账号)。 | 若监听到账号变化，游戏应先清除本地缓存信息（session或其他用户缓存），再重新调用[unionLogin](../harmonyos-references/gameservice-gameplayer.md#gameplayerunionlogin)接口（showLoginDialog设置为true），重新拉起联合登录面板。 |
| 场景二 | 用户在设备上切换华为账号后，游戏重启但没有调用unionLogin，直接调用verifyLocalPlayer。此时，verifyLocalPlayer接口会返回[1002000015](../harmonyos-references/errorcode-gameservice.md#section1002000015-当前玩家信息无效)错误码，同时触发on回调。 | 若监听到账号变化，游戏应先清除本地缓存信息（session或其他用户缓存），再重新调用[unionLogin](../harmonyos-references/gameservice-gameplayer.md#gameplayerunionlogin)接口（showLoginDialog设置为true），重新拉起联合登录面板。 |

### 展示联合登录面板

调用[unionLogin](../harmonyos-references/gameservice-gameplayer.md#gameplayerunionlogin)接口，向玩家展示联合登录面板。

```typescript
let context = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
let thirdAccountInfo1: gamePlayer.ThirdAccountInfo = {
  'accountName': 'testName1', // 游戏官方账号在联合登录面板上的显示名称。建议传入具体的“xx账号登录”、“xx通行证登录”等，例如“游友账号登录”，不建议使用“官方账号登录”等容易有歧义的账号名称。若游戏存在多语言版本，需要开发者自行判断语种并传入当前语种对应的账号名称
  'accountIcon': $r('app.media.icon'), // 游戏官方账号图标资源信息，图标大小总和不能超过35KB
  'accountIdentifier': 'testIdentifier1', // 当前账号的唯一标识符，此标识符用来标识账号并在登录结果处理中用于判断识别玩家选择的账号
  'isOnTop': true // 当前账号是否置顶显示，且仅会置顶第一个传入true的账号
};
let request: gamePlayer.UnionLoginParam = {
  showLoginDialog: false, // 是否弹出联合登录面板。true表示强制弹出面板，false表示优先使用玩家上一次的登录选择，不弹出联合登录面板，若玩家首次登录或卸载重装，则正常弹出
  thirdAccountInfos: [
    thirdAccountInfo1 // 若游戏无官包或无官方账号体系，请传空数组
  ]
};
try {
  gamePlayer.unionLogin(context, request).then((result: gamePlayer.UnionLoginResult) => {
    hilog.info(0x0000, 'testTag', `Succeeded in logging in: ${result?.accountName}`);
  }).catch((error: BusinessError) => {
    hilog.error(0x0000, 'testTag', `Failed to login. Code: ${error.code}, message: ${error.message}`);
  });
} catch (error) {
  let err = error as BusinessError;
  hilog.error(0x0000, 'testTag', `Failed to login. Code: ${err.code}, message: ${err.message}`);
}
```

联合登录面板为官方统一样式，不支持开发者自定义联合登录面板样式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/xRtkJespTl26WU0H-Znw1Q/zh-cn_image_0000002712405106.png)

用户完成登录流程后，游戏顶部弹出欢迎横幅，并向游戏返回accountName（选择华为账号登录返回值为hw\_account）、accountIdentifier（选择华为账号登录返回值为hw\_account）、gamePlayerId等信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/XxhTDD2KTLCXTeZEqImZdQ/zh-cn_image_0000002742124061.png)

游戏获取到的gamePlayerId（HarmonyOS 5.0及以上系统）与openId/playerId（HarmonyOS 4及以下系统）数值相等。开发者可以根据gamePlayerId实现HarmonyOS 5.0及以上游戏和HarmonyOS 4及以下游戏的账号资产互通。

若在开发者服务器找到玩家记录，表明该玩家是老用户。若未找到玩家记录，表明该玩家为新用户，开发者可以为该玩家在HarmonyOS 5.0及以上系统创建新的游戏号。

### 异步步骤：核验玩家信息

由于[unionLogin](../harmonyos-references/gameservice-gameplayer.md#gameplayerunionlogin)接口返回的gamePlayerId存在被篡改的风险，建议在开发者服务端核验玩家信息，即从开发者服务器获取gamePlayerId与[unionLogin](../harmonyos-references/gameservice-gameplayer.md#gameplayerunionlogin)接口返回的gamePlayerId做比对，确保玩家信息一致性。若无服务器，无需校验一致性。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/xGPFNEZ7Q3aO1Dhn8g16Kg/zh-cn_image_0000002712245154.png)

1. 调用[createLoginWithHuaweiIDRequest](../harmonyos-references/account-api-authentication.md#createloginwithhuaweiidrequest)创建认证请求并设置参数。

   ```typescript
   // 创建认证请求，并设置参数
   let loginRequest = new authentication.HuaweiIDProvider().createLoginWithHuaweiIDRequest();
   loginRequest.state = util.generateRandomUUID();
   ```

   调用[AuthenticationController](../harmonyos-references/account-api-authentication.md#authenticationcontroller)对象的[executeRequest](../harmonyos-references/account-api-authentication.md#executerequest)方法执行认证请求，并在Callback中处理认证结果，获取到Authorization Code。

   **说明** 

   Authorization Code有效时间为5分钟，且仅能使用一次，不可复用。

   ```typescript
   // 执行认证请求
   try {
     let controller = new authentication.AuthenticationController(this.getUIContext()?.getHostContext());
     controller.executeRequest(loginRequest, (err, data) => {
       if (err) {
         hilog.error(0x0000, 'testTag', `Failed to login. Code: ${err.code}, message: ${err.message}`);
         return;
       }
       let loginWithHuaweiIDResponse = data as authentication.LoginWithHuaweiIDResponse;
       let state = loginWithHuaweiIDResponse.state;
       if (state != undefined && loginRequest.state != state) {
         hilog.error(0x0000, 'testTag', `Failed to login. State is different.`);
         return;
       }
       hilog.info(0x0000, 'testTag', `Succeeded in logging in.`);
       let loginWithHuaweiIDCredential = loginWithHuaweiIDResponse.data!;
       let authorizationCode = loginWithHuaweiIDCredential.authorizationCode;
       // 开发者处理authorizationCode
     });
   } catch (error) {
     let err = error as BusinessError;
     hilog.error(0x0000, 'testTag', `Failed to login. Code: ${err.code}, message: ${err.message}`);
   }
   ```
2. 游戏向开发者服务器上传[unionLogin](../harmonyos-references/gameservice-gameplayer.md#gameplayerunionlogin)接口返回的gamePlayerId。
3. 携带Authorization Code，请求[获取用户级凭证](../harmonyos-references/account-api-obtain-user-token.md)接口，获取Access Token。

   **说明** 

   由于Access Token的有效期仅为60分钟，当Access Token失效或者即将失效时（可通过[NSP\_STATUS错误码](../harmonyos-references/account-api-get-token-info.md#错误码)判断），可以使用Refresh Token（有效期180天）通过[获取用户级凭证](../harmonyos-references/account-api-obtain-user-token.md)向华为账号服务器请求获取新的Access Token。
4. 携带Access Token，请求[获取玩家标识](../harmonyos-references/gameservice-getplayerinfo.md)接口，获取华为服务器侧的玩家标识gamePlayerId。
5. 将华为服务器返回的玩家标识gamePlayerId与步骤**2**传入的玩家标识gamePlayerId进行玩家信息核验。

   若gamePlayerId一致，表示玩家标识gamePlayerId核验通过，允许玩家进入游戏。若核验不通过，已通过合规校验进入游戏的玩家也需强制退出游戏。

### 合规校验

调用[verifyLocalPlayer](../harmonyos-references/gameservice-gameplayer.md#gameplayerverifylocalplayer)接口对用户设备登录华为账号的实名认证和未成年人防沉迷进行合规校验，校验通过后，玩家进入游戏。

```typescript
let context = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
// ThirdUserInfo是使用游戏官方账号登录游戏的玩家合规信息，接入华为账号登录时无需传入该信息，但在接入游戏官方账号登录时要求传入相关信息
let request: gamePlayer.ThirdUserInfo = {
  thirdOpenId: '123xxxx', // 游戏官方账号ID，接入华为账号登录时传空
  isRealName: true // 玩家是否实名，该值为true时表示已实名，为false时表示未实名，接入华为账号登录时不传该字段
};
try {
  gamePlayer.verifyLocalPlayer(context, request).then(() => {
    hilog.info(0x0000, 'testTag', `Succeeded in verifying.`);
  }).catch((error: BusinessError) => {
    hilog.error(0x0000, 'testTag', `Failed to verify. Code: ${error.code}, message: ${error.message}`);
  });
} catch (error) {
  let err = error as BusinessError;
  hilog.error(0x0000, 'testTag', `Failed to verify. Code: ${err.code}, message: ${err.message}`);
}
```

华为账号的实名认证、未成年人防沉迷由基础游戏服务实现，华为账号的支付合规控制（例如未成年人支付限额）由IAP Kit（应用内支付服务）实现。

| 合规校验 | 校验项 | 国家政策 | 解决方案 |
| --- | --- | --- | --- |
| 华为账号实名认证 | 校验用户设备登录的华为账号是否已实名认证。 | 根据相关法律法规要求，所有网络游戏玩家必须使用真实有效身份信息注册并登录网络游戏。 | 若玩家使用未实名认证的华为账号登录游戏时，基础游戏服务向玩家弹出实名认证窗口，要求玩家进行实名认证。若玩家取消实名认证，则返回[1002000004](../harmonyos-references/errorcode-gameservice.md#section1002000004-实名认证返回强制实名但用户取消或需要强制实名但没有实名)错误码。 |
| 未成年人防沉迷 | 校验已实名认证为未成年人的华为账号是否在规定时间内登录游戏。 | 根据国家新闻出版署的最新规定，所有网络游戏企业仅可在周五、周六、周日和法定节假日每日20时至21时向未成年人提供1小时网络游戏服务，其他时间均不得以任何形式向未成年人提供网络游戏服务。 | - 已实名认证为未成年人的华为账号在规定时间内登录游戏，当游戏进行到晚上21时，基础游戏服务会弹窗提示玩家已到游戏时间，强制玩家退出游戏并返回[1002000006](../harmonyos-references/errorcode-gameservice.md#section1002000006-玩家未成年并且当前不在可游戏时间)错误码。  - 已实名认证为未成年人的华为账号在非规定游戏时间内登录游戏，基础游戏服务会弹框提示玩家不允许游戏，强制玩家退出游戏并返回[1002000006](../harmonyos-references/errorcode-gameservice.md#section1002000006-玩家未成年并且当前不在可游戏时间)错误码。 |
| 未成年人支付限额 | 校验已实名认证为未成年人的华为账号是否限额付费。 | 根据国家新闻出版署的最新规定，网络游戏企业不得为未满8周岁的用户提供游戏付费服务。同一网络游戏企业所提供的游戏付费服务，8周岁以上未满16周岁的用户，单次充值金额不得超过50元人民币，每月充值金额累计不得超过200元人民币；16周岁以上未满18周岁的用户，单次充值金额不得超过100元人民币，每月充值金额累计不得超过400元人民币。 | 已实名认证为未成年人的华为账号在游戏内超额付费，IAP Kit会弹窗提示消费金额超出限制。  用户在使用华为应用内支付时，华为会自动根据国家新闻出版署的要求进行支付限额控制，开发者无需处理。 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/aRLwN6DiS_-mpZH7jeE_eg/zh-cn_image_0000002742004103.png)

### 提交玩家角色信息

推荐接入。

玩家成功登录游戏并选择角色、区服后，游戏将角色信息提交到华为游戏服务器，可用于后续基于角色维度的联运活动规划，为玩家提供更好的体验和更丰富的能力。

调用[savePlayerRole](../harmonyos-references/gameservice-gameplayer.md#gameplayersaveplayerrole)接口，将角色信息上报至华为游戏服务器。

**说明** 

若游戏没有角色系统，roleId请传入'0'，roleName请传入'default'，请勿传""和null。

```typescript
let context = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
let request: gamePlayer.GSKPlayerRole = {
  roleId: '123', // 玩家角色ID，如游戏没有角色系统，请传入'0'，不可以传入""和null
  roleName: 'Jason', // 玩家角色名，如游戏没有角色系统，请传入'default'，不可以传入""和null
  serverId: '456',
  serverName: 'Zhangshan',
  gamePlayerId: '789', // 请根据实际获取到的gamePlayerId传值
  thirdOpenId: '123' // 接入华为账号登录时不传该字段。接入游戏官方账号登录时，请根据实际获取到的thirdOpenId传值
};
try {
  gamePlayer.savePlayerRole(context, request).then(() => {
    hilog.info(0x0000, 'testTag', `Succeeded in saving.`);
  });
} catch (error) {
  let err = error as BusinessError;
  hilog.error(0x0000, 'testTag', `Failed to save. Code: ${err.code}, message: ${err.message}`);
}
```

### 欢迎横幅管理游戏账号

不涉及角色交易、或不存在多个游戏号的游戏可忽略。

接入角色交易、或存在多个游戏号的游戏，玩家成功登录后会在顶部欢迎横幅出现“管理”按钮。

若玩家在“顶部欢迎横幅 > 管理 > 管理游戏号”中切换/删除游戏号时，开发者的实现逻辑如下：

1. 在[on](../harmonyos-references/gameservice-gameplayer.md#gameplayeronplayerchanged)接口回调中清理游戏的登录缓存。
2. 在[on](../harmonyos-references/gameservice-gameplayer.md#gameplayeronplayerchanged)接口回调中重新调用[unionLogin](../harmonyos-references/gameservice-gameplayer.md#gameplayerunionlogin)接口，将**showLoginDialog**参数设置为**true**，即可强制拉起联合登录面板，允许玩家重新选择华为账号登录或游戏官方账号登录。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/t3VQwKb4RgWFI-r_UqssKA/zh-cn_image_0000002712405114.png)
