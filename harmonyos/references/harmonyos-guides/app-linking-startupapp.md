---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-linking-startupapp
title: 通过App Linking应用链接拉起指定应用
breadcrumb: 指南 > 应用服务 > App Linking Kit（应用链接服务） > 通过App Linking应用链接拉起指定应用
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:93af4d0ec57b6bf79bb225c951042dc2a8adc2c78809bbeff7b08c2cbac956aa
---

## 场景介绍

使用App Linking应用链接进行跳转时，系统会根据接口传入的uri信息（HTTPS链接）将用户引导至目标应用中的特定内容，无论应用是否已安装，用户都可以访问到链接对应的内容，跳转体验相比Deep Linking方式更加顺畅。

例如：当开发者使用App Linking应用链接接入“扫码直达”服务后，用户可通过控制中心扫一扫这类系统级扫码入口，扫描应用的二维码、条形码并跳转到应用对应服务页，实现一步直达的体验。

说明

该能力目前仅适用于5.0.0(12)及以上版本的HarmonyOS应用，如果开发的是元服务，请参考[使用元服务链接跳转元服务](../atomic-guides/atomic-applinking.md)。

## 原理机制

* App Linking在Deep Linking基础上增加了域名校验环节，通过域名校验，可帮助用户消除歧义，识别合法归属于域名的应用，使链接更加安全可靠。
* App Linking对于同一HTTPS网址，有应用和网页两种内容的呈现方式。当应用安装时则优先打开应用去呈现内容；当应用未安装时，则打开浏览器呈现Web版的内容。

## 约束与限制

支持Phone、PC/2in1、Tablet设备。并且从5.1.1(19)版本开始，新增支持TV设备。

## 前提条件

已[开通App Linking服务](applinking-enable-applinking.md)。

## 开发流程

| 角色 | 操作步骤 |
| --- | --- |
| 云端开发 | [开通App Linking服务](applinking-enable-applinking.md)。 |
| 云端开发 | [建立域名与应用关联关系](app-linking-startupapp.md#建立域名与应用关联关系)。 |
| 云端开发 | [在AGC为应用创建关联的网址域名](app-linking-startupapp.md#在agc为应用创建关联的网址域名)。 |
| 客户端开发 | [在module.json5中配置关联的网址域名](app-linking-startupapp.md#在modulejson5中配置关联的网址域名)。 |
| 客户端开发 | [处理传入的链接](app-linking-startupapp.md#处理传入的链接)。 |
| 前端开发 | 开发链接对应的H5网页，应用未安装时呈现Web版内容。  **说明：** 本指南侧重于HarmonyOS应用相关的开发指导，网页的开发请开发者依据业务需求自行实现。 |
| 客户端开发 | [验证应用被拉起效果](app-linking-startupapp.md#验证应用被拉起效果)。 |

## 配置应用链接能力

### 建立域名与应用关联关系

在开发者的网站域名服务器上做如下配置。后续[在AGC为应用创建关联的网址域名](app-linking-startupapp.md#在agc为应用创建关联的网址域名)时，AGC会通过此文件确认哪些应用才是合法归属于此域名的，使链接更加安全可靠。

1. 创建域名配置文件applinking.json，内容如下：

   ```
   1. {
   2. "applinking": {
   3. "apps": [
   4. {
   5. "appIdentifier": "1234567",
   6. "index": 1
   7. },
   8. {
   9. "appIdentifier": "7654321",
   10. "index": 2
   11. }
   12. ]
   13. }
   14. }
   ```

   说明

   同一个网站域名可以关联多个应用，只需要在"apps"列表里放置多个"appIdentifier"元素即可，其中每个"appIdentifier"元素对应每个应用。

   | 参数名称 | 必选(M)/可选(O) | 类型 | 参数说明 |
   | --- | --- | --- | --- |
   | appIdentifier | M | String | 填写创建应用时生成的APP ID，获取方式请参见[查看应用信息](../app/agc-help-view-app-info-0000002282674569.md)。 |
   | index | O | Integer | 当App Linking匹配到多个应用时，若希望直接拉起某个指定应用，可以使用index来设置应用跳转的优先级。  index取值范围为[-100,100]，可以重复，不可以为空值，值越大表示优先级越高。  - 如果App Linking匹配到多个应用，但是都未配置index字段，系统会拉起所有匹配的应用，并弹出对话框询问用户选择拉起哪个应用。  - 如果App Linking匹配到多个应用，并且部分或全部配置了index字段，系统会拉起index值最大的应用。当有多个应用的index值最大时，系统会同时拉起这些应用，并弹出对话框询问用户选择拉起哪个应用。  **起始版本：** 6.1.0(23) |
2. 将applinking.json配置文件放在域名服务器的固定目录下：https://domain.name/.well-known/applinking.json。例如：开发者的服务器域名为www.example.com，则必须将applinking.json文件放在如下位置：

   https://www.example.com/.well-known/applinking.json

### 在AGC为应用创建关联的网址域名

基于HarmonyOS应用链接能力，需要为HarmonyOS应用创建关联的网址域名。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，点击“开发与服务”。
2. 在项目列表中点击HarmonyOS应用所在的项目。
3. 在左侧导航栏中选择“增长 > App Linking > 应用链接”，点击“创建”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/OoovsAebRCCLeXQfTnydRQ/zh-cn_image_0000002583478801.png?HW-CC-KV=V1&HW-CC-Date=20260427T234830Z&HW-CC-Expire=86400&HW-CC-Sign=C51CA3E7305CE958A65322B9AA92BD9552E78804C668A30F41A175E8226F7018)
4. 填写[建立域名与应用关联关系](app-linking-startupapp.md#建立域名与应用关联关系)的网址域名，例如：https://www.example.com。必须输入精确的域名，不可输入包含特殊字符的模糊网址。

   说明

   不可以在域名后面添加/，即不支持https://www.example.com/形式。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/0CwemQkqRlmlOjj5uCEyXQ/zh-cn_image_0000002552799152.png?HW-CC-KV=V1&HW-CC-Date=20260427T234830Z&HW-CC-Expire=86400&HW-CC-Sign=800242F99F096572EA267901C045311A34B41B2978EB2F8ADAD55384F8ADEACD)
5. 设置完成后点击“发布”，AGC会对该网站域名的配置文件所包含的应用与本项目内的应用列表进行交集校验。

   说明

   应用链接发布完成后，如果距离上次更新超过24小时，系统会去域名服务器上重新获取配置文件进行交集校验。

   例如：开发者在4月7日17:21创建了应用链接，系统会在4月8日17:30去域名服务器上重新获取配置文件，然后进行交集校验，更新发布状态。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/IRoJbQIuRi2IvhbARmz-kQ/zh-cn_image_0000002583438847.png?HW-CC-KV=V1&HW-CC-Date=20260427T234830Z&HW-CC-Expire=86400&HW-CC-Sign=AD345055375624DFAC7E4921834347AD3F1C5B1CB842737C24FFF08F3F5EE241)

   * 如果域名的配置文件中存在本项目中的应用，则发布成功，点击“查看”可显示该域名关联的应用信息。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/UfC4PrG4ToaghDEvJlyyzQ/zh-cn_image_0000002552958802.png?HW-CC-KV=V1&HW-CC-Date=20260427T234830Z&HW-CC-Expire=86400&HW-CC-Sign=2963C0BCC6B2E4E5ACE64E0736B020854A32D0A29F92649053D0DCD9FC25617D)
   * 如果还在校验中，则状态为“发布中”。
   * 如果配置文件中没有包含任何本项目中的应用，则发布失败，点击“查看”可显示发布失败原因。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/sEPkpmu3TmCvbIcAZeYfKw/zh-cn_image_0000002583478803.png?HW-CC-KV=V1&HW-CC-Date=20260427T234830Z&HW-CC-Expire=86400&HW-CC-Sign=0EB511ACE87651EA62FD81E6B6F3F3BE3AF3B56161342AB61A9F1487F4085DAB)

### 在module.json5中配置关联的网址域名

在应用的[module.json5文件](module-configuration-file.md)中进行如下配置，以声明应用关联的域名地址，并开启域名校验开关。当URL符合module.json5中配置的host和路径规则时，可拉起开发者的App。

* "entities"列表中必须包含"entity.system.browsable"。
* "actions"列表中必须包含"ohos.want.action.viewData"。
* "uris"列表中必须包含"scheme"为"https"且"host"为域名地址的元素，可选属性包含"path"、"pathStartWith"和"pathRegex"，具体请参见“[uris标签说明](app-uri-config.md#uris标签说明)”。
* "domainVerify"设置为true，表示开启域名校验开关。

说明

skills标签下默认包含一个skill对象，用于标识应用入口。应用跳转链接不能在该skill对象中配置，需要创建独立的skill对象。

如果存在多个跳转场景，需要在skills标签下创建不同的skill对象，否则会导致配置无法生效。

例如，声明应用关联的域名是www.example.com，则需进行如下配置。

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
19. // 从5.1.1(19)开始，须配置为"ohos.want.action.home"。对于5.1.0(18)及之前版本，请配置为"action.system.home"。
20. "ohos.want.action.home"
21. ]
22. },
23. {
24. "entities": [
25. // entities必须包含"entity.system.browsable"
26. "entity.system.browsable"
27. ],
28. "actions": [
29. // actions必须包含"ohos.want.action.viewData"
30. "ohos.want.action.viewData"
31. ],
32. "uris": [
33. {
34. // scheme须配置为https
35. "scheme": "https",
36. // host须配置为关联的网址域名
37. "host": "www.example.com",
38. // path可选，表示域名服务器上的目录或文件路径，例如www.example.com/path1中的path1
39. // 如果应用只能处理部分特定的path，则此处应该配置应用所支持的path，避免出现应用不能处理的path链接也被引流到应用中的问题
40. "path": "path1"
41. }
42. ],
43. // domainVerify须设置为true
44. "domainVerify": true
45. }
46. // 若有其他跳转能力，如推送消息跳转、NFC跳转，可新增一个skill对象，防止与App Linking业务冲突
47. ]
48. }
49. ]
50. }
51. }
```

### 处理传入的链接

在应用的Ability（如EntryAbility）的onCreate()或者onNewWant()生命周期回调中添加如下代码，以处理传入的链接。

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { url } from '@kit.ArkTS';
4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. // 从want中获取传入的链接信息。
7. // 如传入的url为：https://www.example.com/programs?action=showall
8. let uri = want?.uri;
9. if (uri) {
10. // 从链接中解析query参数，拿到参数后，开发者可根据自己的业务需求进行后续的处理。
11. try {
12. let urlObject = url.URL.parseURL(want?.uri);
13. let action = urlObject.params.get('action');
14. // 例如，当action为showall时，展示所有的节目。
15. if (action === "showall"){
16. // ...
17. }
18. // ...
19. } catch (error) {
20. hilog.error(0x0000, 'testTag', `Failed to parse url.`);
21. }
22. }
23. }
24. }
```

若要根据链接参数启动UIAbility的指定页面组件，请参考“[启动UIAbility的指定页面](uiability-intra-device-interaction.md#启动uiability的指定页面)”。

## 验证应用被拉起效果

1. 对应用进行[手动签名](ide-signing.md#section297715173233)。

   不能使用DevEco Studio的自动签名功能，必须使用手动签名，否则无法拉起应用。
2. 编译打包，并安装应用至调试设备。
3. 验证App Linking应用链接拉起效果。

   * 方式一：[点击链接验证](app-linking-startupapp.md#点击链接验证)。
   * 方式二：[通过openLink接口拉起](app-linking-startupapp.md#通过openlink接口拉起)。
   * 方式三：[通过系统浏览器或ArkWeb拉起](app-linking-startupapp.md#通过系统浏览器或arkweb拉起)。
   * 方式四：[通过系统级扫码入口拉起](app-linking-startupapp.md#通过系统级扫码入口拉起)。

### 点击链接验证

将App Linking应用链接地址存入备忘录中，并点击验证该链接是否可以拉起应用。

### 通过openLink接口拉起

拉起方应用通过[UIAbilityContext.openLink()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#openlink12)接口，传入目标应用的链接，拉起目标应用。

openLink接口提供了两种拉起目标应用的方式，开发者可根据业务需求进行选择。

* 方式一： 仅以App Linking的方式打开应用。

  将appLinkingOnly参数设为true，若有App Linking匹配的应用，则直接打开目标应用。若无App Linking匹配的应用，则抛异常给开发者进行处理。

  适用于无法打开目标应用时，开发者做了相应的异常处理。例如：拉起方应用集成了ArkWeb，当目标应用不存在时，可通过ArkWeb打开链接。
* 方式二： 以App Linking优先的方式打开应用。

  将appLinkingOnly参数设为false或者不传，若有App Linking匹配的应用，则直接打开目标应用。若无App Linking匹配的应用，则尝试以浏览器打开链接的方式打开应用。

  适用于无法打开目标应用时，开发者未做任何处理。此时目标应用不存在时，会通过系统浏览器打开链接。

本文为了方便验证App Linking的配置是否正确，选择方式一，示例如下。

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
3. 在“entry/src/main/ets/pages/Index.ets”文件中，使用[UIAbilityContext.openLink()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#openlink12)接口打开应用。

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
   15. let link: string = "https://www.example.com/programs?action=showall";
   16. // 仅以App Linking的方式打开应用
   17. context.openLink(link, { appLinkingOnly: true })
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

### 通过系统浏览器或ArkWeb拉起

ArkWeb深度集成了App Linking的能力，当用户在系统浏览器或者集成ArkWeb的应用的网页上点击某个链接时，若有链接匹配的应用，系统则会通过App Linking能力优先拉起目标应用，并在应用内展示相应的内容。此机制有如下限制：

1. 如果用户当前浏览的网页的域名与点击的App Linking链接的域名完全一致，则系统会继续在系统浏览器或ArkWeb中打开该链接，以维持连贯的用户浏览体验。
2. 如果域名不完全一致（例如example.com和app.example.com），则系统会通过App Linking能力优先拉起目标应用，并在应用内展示相应的内容。

### 通过系统级扫码入口拉起

通过系统级扫码入口扫描App Linking应用链接对应的二维码，然后查看跳转效果。以“扫码直达”服务的美团单车场景为例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/1Ab413-OQgK7g1rmcNmI5w/zh-cn_image_0000002552799154.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234830Z&HW-CC-Expire=86400&HW-CC-Sign=329E5EE4B3A45F99A65F97119F6CCCF45D3878278198AF9980A55966F10DF846)

## FAQ

### 应用的module.json5文件skills设置不正确，如何处理？

检查"host"字段中应用所对应的域名是否与AGC创建的网址域名一致。

### 开发者网站服务器配置不正确，如何处理？

按照以下步骤排查：

1. 检查服务器的JSON配置，并确保appIdentifier的值正确无误。
2. 检查applinking.json是否放置在正确的目录（.well-known）下，通过浏览器等方式访问该json文件的地址：https://your.domain.name/.well-known/applinking.json，确保能正常访问。

### 系统尚未完成域名校验，如何处理？

按照以下步骤排查：

1. 在设备上安装应用，需等待至少20秒，以确保系统完成域名校验的流程。
2. 系统进行域名校验时，如存在断网、弱网等情况，可能导致域名校验失败，域名校验失败后，系统将在24小时内重新进行域名校验。

### 如何确认域名校验是否成功？

如需查看应用域名验证结果，请在DevEco Studio中打开终端，并使用以下命令查询验证结果：

**hdc shell hidumper -s AppDomainVerifyManager**

运行hidumper命令后，即可在控制台上看到success消息。

```
1. BundleName:
2. appIdentifier:123456789
3. domain verify status:
4. https://www.example.com:success
```

* 如果存在client-error消息，请按照以下步骤排查：

  1. 检查消息中的appIdentifier是否与AGC中的APP ID一致。
  2. 检查在AGC配置的域名发布是否成功。
* 如果存在http\_unknown消息，请确保设备可以访问网络，并重新安装应用。
* 如果存在其他消息，请联系[技术支持](../harmonyos-releases/support.md)获取帮助。

### 设备首次启动，若无法通过App Linking拉起系统预装应用，如何处理？

设备首次启动后，系统将在20分钟内尝试对预装应用进行域名校验，若在20分钟内设备一直无法访问网络，则可能导致预装应用域名校验失败。若出现此类问题，请重启手机，或者等待24小时后重试。系统将在下次开机或24小时后对预装应用重新尝试进行域名校验。

### 访问CDN（Content Delivery Network，内容分发网络）时发现内容未及时更新，如何处理？

CDN缓存时间为10分钟，请耐心等待一段时间后再次访问。

### 应用和域名的对应关系如何？

应用和域名的关系是多对多的关系：一个应用可以关联多个不同的域名，同样地，一个域名也可以关联多个不同的应用。

### 如果同一域名关联了多个应用，那么该域名的链接将拉起哪个应用？

开发者可以通过配置applinking.json以关联多个应用。如果每个应用的module.json5的uris字段配置的都是一样的，那么系统将弹出列表框供用户选择要拉起的目标应用。 为了更好的体验，开发者也可以通过链接的path去区分拉起的目标应用，如链接https://www.example.com/path1拉起目标应用1，链接https://www.example.com/path2拉起目标应用2。

### 配置App Linking应用链接时提示“下载源JSON文件被拒，请确认安全策略是否符合要求”，如何处理？

配置文件需要放在域名服务器的固定目录下：

https://domain.name/.well-known/applinking.json

例如：开发者的服务器域名为www.example.com，则必须将applinking.json文件放在如下位置：

https://www.example.com/.well-known/applinking.json
