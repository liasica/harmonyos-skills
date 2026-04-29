---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/deep-linking-startup
title: 使用Deep Linking实现应用间跳转
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > Stage模型开发指导 > 应用间跳转 > 拉起指定应用 > 使用Deep Linking实现应用间跳转
category: harmonyos-guides
scraped_at: 2026-04-29T13:25:51+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:89745cb358a7b5dd7ada4e629cd98ef7d60cb4f63dd519a7fbe37a5f2e5fd612
---

采用Deep Linking进行跳转时，系统会根据接口中传入的uri信息，在本地已安装的应用中寻找到符合条件的应用并进行拉起。当匹配到多个应用时，会拉起应用选择框。

## 实现原理

Deep Linking基于隐式Want匹配机制中的uri匹配来查询、拉起目标应用。隐式Want的uri匹配规则详见[uri匹配规则](explicit-implicit-want-mappings.md#uri匹配规则)。

## 目标应用操作指导

### 配置module.json5文件

为了能够支持被其他应用访问，目标应用需要在[module.json5配置文件](module-configuration-file.md)中配置[skills标签](module-configuration-file.md#skills标签)。

说明

skills标签下默认包含一个skill对象，用于标识应用入口。应用跳转链接不能在该skill对象中配置，需要创建独立的skill对象。如果存在多个跳转场景，需要在skills标签下创建不同的skill对象，否则会导致配置无法生效。

Deep Linking中的scheme可以自定义，但不能以"ohos"开头，也不建议使用"https"、"http"、"file"

、"store"、"filemanager"、"hww"等系统已保留的scheme值，否则可能会拉起默认的系统应用而非目标应用。

配置示例如下：

```
1. {
2. "module": {
3. // ···
4. "abilities": [
5. // ···
6. {
7. // ···
8. "skills": [
9. {
10. "entities": [
11. "entity.system.home"
12. ],
13. "actions": [
14. "ohos.want.action.home"
15. ]
16. },
17. {
18. "actions": [
19. // actions不能为空，actions为空会造成目标方匹配失败。
20. "ohos.want.action.viewData"
21. ],
22. "uris": [
23. {
24. // scheme必选，可以自定义，以link为例，需要替换为实际的scheme
25. "scheme": "link",
26. "host": "www.example.com"
27. }
28. ]
29. } // 新增一个skill对象，用于跳转场景。如果存在多个跳转场景，需配置多个skill对象。
30. ]
31. },
32. // ···
33. ],
34. // ···
35. }
36. }
```

[module.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/PullLinking/entry/src/main/module.json5#L15-L355)

### 获取并解析拉起方传入的应用链接

在目标应用的UIAbility的[onCreate()](../harmonyos-references/js-apis-app-ability-uiability.md#oncreate)或者[onNewWant()](../harmonyos-references/js-apis-app-ability-uiability.md#onnewwant)生命周期回调中，获取、解析拉起方传入的应用链接。

```
1. // 以DeepAbility.ets为例
2. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
3. import { url } from '@kit.ArkTS';

5. const DOMAIN = 0x0000;

7. export default class DeepAbility extends UIAbility {
8. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
9. // 从want中获取传入的链接信息。
10. // 如传入的url为：link://www.example.com/programs?action=showall
11. let uri = want?.uri;
12. if (uri) {
13. // 从链接中解析query参数，拿到参数后，开发者可根据自己的业务需求进行后续的处理。
14. let urlObject = url.URL.parseURL(want?.uri);
15. let action = urlObject.params.get('action');
16. // 例如，当action为showall时，展示所有的节目。
17. if (action === 'showall') {
18. // ···
19. }
20. }
21. }
22. // ···
23. }
```

[DeepAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/PullLinking/entry/src/main/ets/DeepAbility/DeepAbility.ets#L17-L75)

## 拉起方应用实现应用跳转

下面通过三个案例，分别介绍如何使用[openLink()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#openlink12)与[startAbility()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startability)接口实现应用跳转，以及如何在[Web组件](../harmonyos-references/arkts-basic-components-web.md)中实现应用跳转。

### 使用openLink实现应用跳转

在[openLink](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#openlink12)接口的link字段中传入目标应用的URL信息，并将options字段中的[appLinkingOnly](../harmonyos-references/js-apis-app-ability-openlinkoptions.md#openlinkoptions)配置为false。

示例代码如下：

```
1. import { common, OpenLinkOptions } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const TAG: string = '[UIAbilityComponentsOpenLink]';
6. const DOMAIN_NUMBER: number = 0xFF00;

8. @Entry
9. @Component
10. struct DeepOpenLinkIndex {
11. build() {
12. Button('start link', { type: ButtonType.Capsule, stateEffect: true })
13. .width('87%')
14. .height('5%')
15. .margin({ bottom: '12vp' })
16. .onClick(() => {
17. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
18. let link: string = 'link://www.example.com'; // 此处为实际应用链接
19. let openLinkOptions: OpenLinkOptions = {
20. appLinkingOnly: false
21. };

23. try {
24. context.openLink(link, openLinkOptions)
25. .then(() => {
26. hilog.info(DOMAIN_NUMBER, TAG, 'openLink success.');
27. }).catch((err: BusinessError) => {
28. hilog.error(DOMAIN_NUMBER, TAG, `openLink failed. Code is ${err.code}, message is ${err.message}`);
29. });
30. } catch (paramError) {
31. hilog.error(DOMAIN_NUMBER, TAG, `Failed to start link. Code is ${paramError.code}, message is ${paramError.message}`);
32. }
33. })
34. }
35. }
```

[DeepOpenLinkIndex.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/PullLinking/entry/src/main/ets/pages/DeepOpenLinkIndex.ets#L15-L51)

### 使用startAbility实现应用跳转

[startAbility](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startability)接口是将应用链接放入Want中，通过调用[隐式Want匹配](explicit-implicit-want-mappings.md#隐式want匹配原理)的方法触发应用跳转。

示例代码如下：

```
1. import { common, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const TAG: string = '[UIAbilityComponentsOpenLink]';
6. const DOMAIN_NUMBER: number = 0xFF00;

8. @Entry
9. @Component
10. struct DeepStartIndex {
11. build() {
12. Button('start ability', { type: ButtonType.Capsule, stateEffect: true })
13. .width('87%')
14. .height('5%')
15. .margin({ bottom: '12vp' })
16. .onClick(() => {
17. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
18. let want: Want = {
19. uri: 'link://www.example.com' // 此处为实际应用链接
20. };

22. try {
23. context.startAbility(want).then(() => {
24. hilog.info(DOMAIN_NUMBER, TAG, 'startAbility success.');
25. }).catch((err: BusinessError) => {
26. hilog.error(DOMAIN_NUMBER, TAG, `startAbility failed. Code is ${err.code}, message is ${err.message}`);
27. });
28. } catch (paramError) {
29. hilog.error(DOMAIN_NUMBER, TAG, `Failed to start ability. Code is ${paramError.code}, message is ${paramError.message}`);
30. }
31. })
32. }
33. }
```

[DeepStartIndex.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/PullLinking/entry/src/main/ets/pages/DeepStartIndex.ets#L15-L49)

### 使用Web组件实现应用跳转

Web组件可以在[onLoadIntercept](../harmonyos-references/arkts-basic-components-web-events.md#onloadintercept10)的回调函数中实现应用跳转。

示例代码如下：

```
1. // DeepWebIndex.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { common } from '@kit.AbilityKit';
5. import { hilog } from '@kit.PerformanceAnalysisKit';

7. const DOMAIN_NUMBER = 0xF811;
8. const TAG = '[Sample_PullLinking]';

10. @Entry
11. @Component
12. struct DeepWebIndex {
13. controller: webview.WebviewController = new webview.WebviewController();

15. build() {
16. Column() {
17. Web({ src: $rawfile('index.html'), controller: this.controller })
18. .onLoadIntercept((event) => {
19. const url: string = event.data.getRequestUrl();
20. if (url === 'link://www.example.com') {
21. (this.getUIContext().getHostContext() as common.UIAbilityContext).openLink(url)
22. .then(() => {
23. hilog.info(DOMAIN_NUMBER, TAG, 'openLink success.');
24. }).catch((err: BusinessError) => {
25. hilog.error(DOMAIN_NUMBER, TAG, `openLink failed, err: ${JSON.stringify(err)}.`);
26. });
27. return true;
28. }
29. // 返回true表示阻止此次加载，否则允许此次加载
30. return false;
31. })
32. }
33. }
34. }
```

[DeepWebIndex.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/PullLinking/entry/src/main/ets/pages/DeepWebIndex.ets#L15-L50)

前端页面代码：

```
1. <!-- index.html -->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <meta charset="UTF-8">
6. </head>
7. <body>
8. <h1>Hello World</h1>
9. <!--方式一、通过绑定事件window.open方法实现跳转-->
10. <button class="doOpenLink" onclick="doOpenLink()">跳转其他应用一</button>
11. <!--方式二、通过超链接实现跳转-->
12. <a href="link://www.example.com">跳转其他应用二</a>
13. </body>
14. </html>
15. <script>
16. function doOpenLink() {
17. window.open("link://www.example.com")
18. }
19. </script>
```
