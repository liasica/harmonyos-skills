---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/applinking-cross-platform
title: 通过聚合链接按指定方式跳转至应用
breadcrumb: 指南 > 应用服务 > App Linking Kit（应用链接服务） > 通过聚合链接按指定方式跳转至应用
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:55506a3f72976aad10ee7becf042cdc5958687f68e81f64244a43896459d74bc
---

## 场景介绍

从6.0.0(20)版本开始，新增支持聚合链接能力。

可用于实现在HarmonyOS系统的设备上点击链接后，按照指定的方式进行跳转。当用户打开链接时，聚合链接会引导用户跳转到HarmonyOS平台预览页、应用市场详情页、自定义网址、深度链接地址等页面。

聚合链接主要用于直接向用户发送应用推广信息，例如通过短信/邮件/社交分享链接发送产品优惠活动或应用推广活动。

## 前提条件

已[开通App Linking服务](applinking-enable-applinking.md)。

## 开发流程

| 角色 | 操作步骤 |
| --- | --- |
| 云端开发 | [开通App Linking服务](applinking-enable-applinking.md)。 |
| 云端开发 | 先在AGC[申请链接前缀](applinking-cross-platform.md#申请链接前缀)并[添加网址允许清单](applinking-cross-platform.md#添加网址允许清单)，然后[创建聚合链接](applinking-cross-platform.md#创建聚合链接)。 |
| 客户端开发 | [在module.json5中配置聚合链接](applinking-cross-platform.md#在modulejson5中配置聚合链接)。 |
| 客户端开发 | [处理拉起方应用传入的链接](applinking-cross-platform.md#处理拉起方应用传入的链接)。 |
| 客户端开发 | [验证应用被拉起效果](applinking-cross-platform.md#验证应用被拉起效果)。 |

## 配置聚合链接能力

### 申请链接前缀

链接前缀是指聚合链接地址中包含的网址，其格式为https://域名。创建聚合链接前，需要申请链接前缀。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，点击“开发与服务”。
2. 在项目列表中点击HarmonyOS应用所在的项目（请确保所有平台的应用在同一项目下）。
3. 在左侧导航栏中选择“增长 > App Linking > 聚合链接”，选择“链接前缀”页签，点击“添加链接前缀”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/0L2W9wesRt2-gyO86PfKfQ/zh-cn_image_0000002583478807.png?HW-CC-KV=V1&HW-CC-Date=20260427T234831Z&HW-CC-Expire=86400&HW-CC-Sign=85A4FF4CF4BEF745419299799A2000F04638B5033BA373AD9EB490A32AA2EF4C)
4. 在AGC提供的免费域名（例如中国站点的域名：drcn.agconnect.link）前再设置一个前缀字符串，前缀字符串仅支持小写字母和数字，且必须确保此前缀唯一。设置完成后点击“下一步”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/g9gKqyKKSPSs-q4ocSbfbg/zh-cn_image_0000002552799158.png?HW-CC-KV=V1&HW-CC-Date=20260427T234831Z&HW-CC-Expire=86400&HW-CC-Sign=A4ECEEC77E214BF2A218ADBF3C69C2DF0642DC78F227A2DE09505ECDA8402216)
5. 等待域名地址验证通过后，页面将显示完整域名。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/QwwvQo2gQTmHjuLo3DLdsg/zh-cn_image_0000002583438853.png?HW-CC-KV=V1&HW-CC-Date=20260427T234831Z&HW-CC-Expire=86400&HW-CC-Sign=51D478BA1BEA6D350349B75AA271D92B15290789D7A3B19DB32808D11CABFEC7)

### 添加网址允许清单

创建聚合链接前，需要添加网址允许清单来指定深度链接地址和自定义网址中允许使用的网址格式。设置后，聚合链接仅允许重定向到符合允许清单规则的网址，从而防止网站诱骗。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，点击“开发与服务”。
2. 在项目列表中点击HarmonyOS应用所在的项目（请确保所有平台的应用在同一项目下）。
3. 在左侧导航栏中选择“增长 > App Linking > 聚合链接”，选择“网址允许清单”页签，点击“添加允许清单规则”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/v5vNiDdTRsK5XG6J36neMQ/zh-cn_image_0000002552958808.png?HW-CC-KV=V1&HW-CC-Date=20260427T234831Z&HW-CC-Expire=86400&HW-CC-Sign=34912C4473A2D8422937EF7153C4F0770F093D1016FD295B9E016312BDAF7AC4)
4. 使用正则表达式设置允许清单规则，设置完成后点击右上角的“发布”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/v9x6PJ38QsmzAQ9QYpIuyQ/zh-cn_image_0000002583478809.png?HW-CC-KV=V1&HW-CC-Date=20260427T234831Z&HW-CC-Expire=86400&HW-CC-Sign=27901B94C24CED68B77A375EB4F5011D3378F6A7D1BA466589F02ADE16DCF897)

### 创建聚合链接

配置聚合链接，按照指定的方式进行跳转。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，点击“开发与服务”。
2. 在项目列表中点击HarmonyOS应用所在的项目（请确保所有平台的应用在同一项目下）。
3. 在左侧导航栏中选择“增长 > App Linking > 聚合链接”，选择“聚合链接”页签，点击“创建聚合链接”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/ZBVyPhNkTjKuVLAEbqqdlw/zh-cn_image_0000002552799160.png?HW-CC-KV=V1&HW-CC-Date=20260427T234831Z&HW-CC-Expire=86400&HW-CC-Sign=96D5F58A4DF259D96D8BA0A66022289C6F57FD3037D614407E1A0FD523E8121F)
4. 设置短链接，完成后点击“下一步”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/XbgT_jh1T_qATb3YUw6W8A/zh-cn_image_0000002583438855.png?HW-CC-KV=V1&HW-CC-Date=20260427T234831Z&HW-CC-Expire=86400&HW-CC-Sign=BACA8C64DFF9F6463BF5967F47EC6D6720AFCD92D2DE074E7C4ED4173A75B40C)

   | 参数 | 参数说明 |
   | --- | --- |
   | 链接前缀 | 聚合链接的前缀。如果还未申请链接前缀，请参见[申请链接前缀](applinking-cross-platform.md#申请链接前缀)。  “链接前缀”下方的文本框中可设置聚合链接的短链接后缀字符串，默认由AGC自动生成。如果需要自行定义，请确保该字符串唯一。 |
   | 链接预览 | 聚合链接向用户发送的短链接地址。 |
5. 设置深度链接，完成后点击“下一步”。

   * 深度链接地址中使用的域名需满足“网址允许清单”要求。
   * 深度链接地址不允许设置为可执行文件格式。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/vheoMDjXSc66zKLhfFx3GA/zh-cn_image_0000002552958810.png?HW-CC-KV=V1&HW-CC-Date=20260427T234831Z&HW-CC-Expire=86400&HW-CC-Sign=40EA584344A8FCD232F39B0BCB5BD086076EE88FA2962ED62311F57F410B32DD)

   | 参数 | 参数说明 |
   | --- | --- |
   | 链接名称 | 配置聚合链接的自定义名称。 |
   | 深度链接地址（默认） | 应用将打开的深度链接地址。  如果未设置HarmonyOS深度链接地址(api>=12)，则会默认打开此链接。 |
   | （可选）HarmonyOS深度链接地址(api>=12) | 如果设置了HarmonyOS深度链接地址(api>=12)，则在HarmonyOS平台优先打开此链接。 |
6. 设置聚合链接在HarmonyOS系统的链接行为，完成后点击“下一步”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/rL6sisWhTD-VKz7qwbsJeA/zh-cn_image_0000002583478811.png?HW-CC-KV=V1&HW-CC-Date=20260427T234831Z&HW-CC-Expire=86400&HW-CC-Sign=1292348AFC19BEE454F13F1C26FD24C333C1559CD8C72668C8D0CCD6401A8F12)

   | 参数 | 参数说明 |
   | --- | --- |
   | 设置在HarmonyOS系统的链接行为(api>=12) | 1. 选择“在HarmonyOS应用中打开”，表示用户点击链接会跳转到HarmonyOS应用中的深度链接地址。  2. 选择或添加需要配置深度链接地址的HarmonyOS应用。 |
   | 未安装应用时，则重定向到 | 如果用户未安装HarmonyOS应用，可通过此选项将用户引导到“华为应用市场页面详情页”或“自定义网址”。  **说明：** 如果选择“自定义网址”，链接不允许设置为可执行文件格式。 |
7. （可选）在“设置跟踪参数”页面，设置广告跟踪参数，可用于广告、流量跟踪。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/OIIBWt0mQaeKMUyggqiv5w/zh-cn_image_0000002552799162.png?HW-CC-KV=V1&HW-CC-Date=20260427T234831Z&HW-CC-Expire=86400&HW-CC-Sign=1085B2CA12BE9BBF3E340AFF987E7DC15E7071960AA1FA4CF6361CF8B416F1DE)

   | 参数 | 参数说明 |
   | --- | --- |
   | 广告系列来源 | 广告渠道，如Huawei，也可自定义。 |
   | 广告系列媒介 | 广告媒介的标识，如pic 、email。 |
   | 广告系列名称 | 特定的推广活动描述，如“双11推广”。 |
8. （可选）设置社交分享标识，可用于社交软件之间的分享，设置完成后点击“下一步”。

   说明

   设置了社交分享标识参数后，可通过[社交分享标识说明](../AppGallery-connect-Guides/agc-applinking-socialdescription-0000001055261926.md)了解设置效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/G90KdK0vSlCGqgm_iXRaew/zh-cn_image_0000002583438857.png?HW-CC-KV=V1&HW-CC-Date=20260427T234831Z&HW-CC-Expire=86400&HW-CC-Sign=0BAFF1F626D4A8F3151F5910704AA35D5D8D23E28ABF1774E181D7D1C5CF4529)

   | 参数 | 参数说明 |
   | --- | --- |
   | 标题 | 聚合链接在社交平台上分享时展示的标题名称。 |
   | 图片URL | 聚合链接在社交平台上分享时展示的图片地址。 |
   | 描述说明 | 聚合链接在社交平台上分享时展示的说明信息。 |
9. （可选）设置预览页，可以将用户引导至合适的目标位置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/5-kl3cyvTbuHgWYQMi33Xw/zh-cn_image_0000002552958812.png?HW-CC-KV=V1&HW-CC-Date=20260427T234831Z&HW-CC-Expire=86400&HW-CC-Sign=620F261EBE6F1C5B67CEFE2ADED64EB1D78053D42A826525327E7381F9360CF9)

   | 参数 | 参数说明 |
   | --- | --- |
   | 显示预览页 | 应用未安装，点击聚合链接时，预览页的显示情况。  - 勾选：在点击聚合链接时，应用如果未安装，则在重定向到应用市场详情页前优先显示预览页。  - 不勾选（默认）：在点击时，应用如果未安装，则会根据浏览器的类型，尽可能地优先拉起应用市场详情页。  **说明：** 目前仅支持华为浏览器。 |
   | 预览页信息来源 | 勾选“显示预览页”后，可以选择预览页信息展示的内容。  - “分享标识内容”：采用分享标识信息构建预览页。  - “应用市场应用信息”：采用AGC中配置的应用信息构建预览页。 |
10. 全部设置完成后，点击右上角的“发布”，页签中将展示已发布的聚合链接列表。

* 点击网址中的二维码图标，或对应操作栏下方的“二维码下载”，可以下载该聚合链接的二维码图片。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/wWITOYxJT0eqxJsTFAu5SQ/zh-cn_image_0000002583478813.png?HW-CC-KV=V1&HW-CC-Date=20260427T234831Z&HW-CC-Expire=86400&HW-CC-Sign=E0A1DE18D57464FEA524328E359E24441D021C6E1808C7F4AB1CE2A16FF640FE)

  点击对应操作栏下方的“链接详情”，可以查看该聚合链接的详情，包括深度链接地址、HarmonyOS应用包名、短链接地址等。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/Z6NuZpipSz2N-L025MPFkA/zh-cn_image_0000002552799164.png?HW-CC-KV=V1&HW-CC-Date=20260427T234831Z&HW-CC-Expire=86400&HW-CC-Sign=B80AB07E0E000566AC3956DFA0A6C8004C9F89F4A02CBB79964F9D11D63E35BB)

### （可选）归档聚合链接

创建聚合链接后，如果不想继续管理该链接，而又不希望影响用户较长一段时间内的使用，可以选择归档聚合链接。

* 归档7天后的聚合链接将被隐藏，开发者无法通过AGC查看或撤销归档。
* 归档后的聚合链接默认从归档时起1年内有效，请谨慎操作。

**操作步骤如下：**

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，点击“开发与服务”。
2. 在项目列表中点击HarmonyOS应用所在的项目。
3. 在左侧导航栏中选择“增长 > App Linking > 聚合链接”。
4. 选择“聚合链接”页签，对已创建的聚合链接进行归档。

   * 单条归档：在聚合链接列表，选择待归档聚合链接对应“操作”列下方的“归档”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/KlveZZUdTX2cqfLkdjJqVg/zh-cn_image_0000002583438859.png?HW-CC-KV=V1&HW-CC-Date=20260427T234831Z&HW-CC-Expire=86400&HW-CC-Sign=84FA3A8503A16F7231637EF174A6B01C85DC6679A35C91550F8FAACD02147E9E)
   * 批量归档：在列表，勾选多条待归档，选择右上角“批量操作”的下拉选项中的“归档”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/ViaPqGq9R9ugw13jj1_spA/zh-cn_image_0000002552958814.png?HW-CC-KV=V1&HW-CC-Date=20260427T234831Z&HW-CC-Expire=86400&HW-CC-Sign=32AE1D30A60F3F6EAF3776CD91925F087D7015962777D6DB6CA4B4C2B094233D)

   说明

   可以通过时间筛选，选择查看“7天内已归档”的聚合链接。还可以点击“操作”列下方的“撤销归档”，将已归档的聚合链接恢复原状。

### 在module.json5中配置聚合链接

在HarmonyOS应用的[module.json5文件](module-configuration-file.md)中进行如下配置，用于接收聚合链接，以获取聚合链接中传递的数据。

* "entities"列表中必须包含"entity.system.browsable"。
* "actions"列表中必须包含"ohos.want.action.viewData"。
* "uris"列表中必须包含"scheme"为"https"且"host"为域名地址的元素，可选属性包含"path"、"pathStartWith"和"pathRegex"，具体请参见“[uris标签说明](app-uri-config.md#uris标签说明)”。
* "domainVerify"设置为true，表示开启域名校验开关。

说明

skills标签下默认包含一个skill对象，用于标识应用入口。应用跳转链接不能在该skill对象中配置，需要创建独立的skill对象。

如果存在多个跳转场景，需要在skills标签下创建不同的skill对象，否则会导致配置无法生效。

例如，聚合链接的域名是example.drcn.agconnect.link，则需进行如下配置。

```
1. {
2. "module": {
3. "abilities": [
4. {
5. "name": "EntryAbility",
6. "srcEntry": "./ets/entryability/EntryAbility.ets",
7. "icon": "$media:icon",
8. "label": "$string:EntryAbility_label",
9. // 请将exported配置为true；如果exported为false，仅具有权限的系统应用能够拉起该应用，否则无法拉起应用
10. "exported": true,
11. "startWindowIcon": "$media:icon",
12. "startWindowBackground": "$color:start_window_background",
13. "skills": [
14. {
15. "entities": [
16. "entity.system.home"
17. ],
18. "actions": [
19. "ohos.want.action.home"
20. ]
21. },
22. {
23. "entities": [
24. // entities必须包含"entity.system.browsable"
25. "entity.system.browsable"
26. ],
27. "actions": [
28. // actions必须包含"ohos.want.action.viewData"
29. "ohos.want.action.viewData"
30. ],
31. "uris": [
32. {
33. // scheme须配置为https
34. "scheme": "https",
35. // host须配置为聚合链接的域名
36. "host": "example.drcn.agconnect.link",
37. // path可选，表示聚合链接的短链接后缀字符串，例如example.drcn.agconnect.link/AIYx中的AIYx
38. // 如果应用只能处理部分特定的path，则此处应该配置应用所支持的path，避免出现应用不能处理的path链接也被引流到应用中的问题
39. "path": "AIYx"
40. }
41. ],
42. // domainVerify须设置为true
43. "domainVerify": true
44. }
45. // 若有其他跳转能力，如推送消息跳转、NFC跳转，可新增一个skill对象，防止与App Linking业务冲突
46. ]
47. }
48. ]
49. }
50. }
```

### 处理拉起方应用传入的链接

在HarmonyOS应用的Ability（如EntryAbility）的[onCreate()](../harmonyos-references/js-apis-app-ability-uiability.md#oncreate)或者[onNewWant()](../harmonyos-references/js-apis-app-ability-uiability.md#onnewwant)生命周期回调中添加如下代码，以处理传入的链接。

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { url } from '@kit.ArkTS';
4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. // 从want中获取传入的链接信息。
7. // 如传入的url为：https://example.drcn.agconnect.link/AIYx，开发者可根据自己的业务需求进行后续的处理。
8. let uri = want?.uri;
9. if (uri) {
10. try {
11. let urlObject = url.URL.parseURL(want?.uri);
12. if (urlObject.toString() === "https://example.drcn.agconnect.link/AIYx"){
13. // ...
14. }
15. // ...
16. } catch (error) {
17. hilog.error(0x0000, 'testTag', `Failed to parse url.`);
18. }
19. }
20. }
21. }
```

若要根据链接参数启动UIAbility的指定页面组件，请参考“[启动UIAbility的指定页面](uiability-intra-device-interaction.md#启动uiability的指定页面)”。

## 验证应用被拉起效果

* 方式一：[通过openLink接口拉起](applinking-cross-platform.md#通过openlink接口拉起)。
* 方式二：[通过系统浏览器或ArkWeb拉起](applinking-cross-platform.md#通过系统浏览器或arkweb拉起)。

### 通过openLink接口拉起

拉起方应用可以调用[UIAbilityContext.openLink()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#openlink12)接口，并将appLinkingOnly参数设为false或者不传，以App Linking优先的方式打开应用。

1. 在“entry/src/main/ets/common”目录下添加GlobalContext.ets文件，开发初始化和获取应用上下文的接口。

   ```
   1. import { common } from '@kit.AbilityKit';

   3. export class GlobalContext {
   4. private static context: common.UIAbilityContext;

   6. public static initContext(context: common.UIAbilityContext): void {
   7. GlobalContext.context = context;
   8. }

   10. public static getContext(): common.UIAbilityContext {
   11. return GlobalContext.context;
   12. }
   13. }
   ```
2. 在“entry/src/main/ets/entryability/EntryAbility.ets”文件中导入GlobalContext，在onCreate方法中使用GlobalContext.initContext(this.context)初始化全局应用上下文。
3. 在“entry/src/main/ets/pages/Index.ets”文件中，使用[UIAbilityContext.openLink()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#openlink12)接口配置聚合链接。

   ```
   1. import { hilog } from '@kit.PerformanceAnalysisKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. import { GlobalContext } from '../common/GlobalContext';

   5. @Entry
   6. @Component
   7. struct Index {
   8. build() {
   9. Button('start link', { type: ButtonType.Capsule, stateEffect: true })
   10. .width('87%')
   11. .height('5%')
   12. .margin({ bottom: '12vp' })
   13. .onClick(() => {
   14. let context = GlobalContext.getContext();
   15. // 如下link请填写开发者实际跳转的url
   16. let link: string = "https://example.drcn.agconnect.link/AIYx";
   17. context.openLink(link, { appLinkingOnly: false })
   18. .then(() => {
   19. hilog.info(0x0000, 'testTag', `Succeeded in opening link.`);
   20. })
   21. .catch((error: BusinessError) => {
   22. hilog.error(0x0000, 'testTag', `Failed to open link, code: ${error.code}, message: ${error.message}`);
   23. })
   24. })
   25. }
   26. }
   ```
4. 安装拉起方应用，点击拉起方应用中的跳转按钮。

   此时目标方应用未安装，若有聚合链接匹配的应用，点击链接会按照[创建聚合链接](applinking-cross-platform.md#创建聚合链接)时指定的方式进行跳转，例如跳转到HarmonyOS平台预览页、应用市场下载详情页、自定义网址等；若无聚合链接匹配的应用，则继续尝试以浏览器打开链接的方式打开应用。
5. 安装目标方应用后，首次启动时会跳转到深度链接指定的内容详情页面。

### 通过系统浏览器或ArkWeb拉起

ArkWeb深度集成了App Linking的能力，当用户在系统浏览器或者集成ArkWeb的应用网页上点击某个链接时，若有聚合链接匹配的应用，会通过App Linking能力优先拉起目标方应用。此机制有如下限制：

* 如果该聚合链接配置了在HarmonyOS系统的链接行为，会跳转到HarmonyOS平台预览页，引导用户打开或下载应用。
* 如果该聚合链接仅配置了深度链接，会跳转到深度链接指定的内容详情页面。
