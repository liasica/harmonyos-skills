---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-openlinkoptions
title: @ohos.app.ability.OpenLinkOptions (openLink的可选参数)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > Stage模型能力的接口 > @ohos.app.ability.OpenLinkOptions (openLink的可选参数)
category: harmonyos-references
scraped_at: 2026-04-28T07:58:21+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:58a2513c158b1f86a8dd21198bf73711b47bd7c97c084c8152658d6f693518a8
---

OpenLinkOptions可以作为[openLink()](js-apis-inner-application-uiabilitycontext.md#openlink12)的入参，用于标识是否仅打开AppLinking和传递键值对可选参数。

说明

* 本模块首批接口从API version 12 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块接口仅可在Stage模型下使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { OpenLinkOptions } from '@kit.AbilityKit';
```

## OpenLinkOptions

PhonePC/2in1TabletTVWearable

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| appLinkingOnly | boolean | 否 | 是 | 表示是否必须以[AppLinking](../harmonyos-guides/app-linking-startup.md)的方式启动UIAbility。  - 取值为true时，如果不存在与AppLinking相匹配的UIAbility，直接返回。  - 取值为false时，如果不存在与AppLinking相匹配的UIAbility，AppLinking会退化为[DeepLinking](../harmonyos-guides/deep-linking-startup.md)。默认值为false。  aa命令隐式拉起Ability时可以通过设置"--pb appLinkingOnly true/false"以AppLinking的方式进行启动。 |
| parameters | Record<string, Object> | 否 | 是 | 表示WantParams参数。  **说明**：具体使用规则请参考[want](js-apis-app-ability-want.md)中的parameters属性。 |
| hideFailureTipDialog21+ | boolean | 否 | 是 | 表示[Deep Linking](../harmonyos-guides/deep-linking-startup.md)找不到应用时是否显示“暂无可用打开方式”的弹窗。  - 取值为true时，不显示“暂无可用打开方式”的弹窗。  - 取值为false时，显示“暂无可用打开方式”的弹窗。默认值为false。  **说明**：appLinkingOnly字段为true时不会触发Deep Linking流程，该字段不会生效。  **元服务API**：从API version 21开始，该接口支持在元服务中使用。 |
| completionHandler21+ | [CompletionHandler](js-apis-app-ability-completionhandler.md#completionhandler) | 否 | 是 | 拉起应用结果的操作类，用于处理拉起应用的结果。  **元服务API**：从API version 21开始，该接口支持在元服务中使用。 |

**示例：**

```
1. import { common, OpenLinkOptions, wantConstant, CompletionHandler, bundleManager } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. const DOMAIN = 0xeeee;
6. const TAG: string = '[openLinkDemo]';

8. @Entry
9. @Component
10. struct Index {
11. @State message: string = 'I am caller';

13. build() {
14. Row() {
15. Column() {
16. Text(this.message)
17. .fontSize(50)
18. .fontWeight(FontWeight.Bold)
19. Button('start browser', { type: ButtonType.Capsule, stateEffect: true })
20. .width('87%')
21. .height('5%')
22. .margin({ bottom: '12vp' })
23. .onClick(() => {
24. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
25. let link: string = 'https://www.example.com';
26. let completionHandler: CompletionHandler = {
27. onRequestSuccess: (elementName: bundleManager.ElementName, message: string): void => {
28. console.info(`${elementName.bundleName}-${elementName.moduleName}-${elementName.abilityName} start succeeded: ${message}`);
29. },
30. onRequestFailure: (elementName: bundleManager.ElementName, message: string): void => {
31. console.error(`${elementName.bundleName}-${elementName.moduleName}-${elementName.abilityName} start failed: ${message}`);
32. }
33. };
34. let openLinkOptions: OpenLinkOptions = {
35. appLinkingOnly: true,
36. // hideFailureTipDialog字段需要在appLinkingOnly字段是false时才生效
37. // hideFailureTipDialog: true,
38. parameters: {
39. [wantConstant.Params.CONTENT_TITLE_KEY]: 'contentTitle',
40. keyString: 'str',
41. keyNumber: 200,
42. keyBool: false,
43. keyObj: {
44. keyObjKey: 'objValue',
45. }
46. },
47. completionHandler: completionHandler
48. };
49. try {
50. context.openLink(
51. link,
52. openLinkOptions,
53. (err, result) => {
54. hilog.error(DOMAIN, TAG, `openLink callback error.code: ${JSON.stringify(err)}`);
55. hilog.info(DOMAIN, TAG, `openLink callback result: ${JSON.stringify(result.resultCode)}`);
56. hilog.info(DOMAIN, TAG, `openLink callback result data: ${JSON.stringify(result.want)}`);
57. }
58. ).then(() => {
59. hilog.info(DOMAIN, TAG, `open link success.`);
60. }).catch((err: BusinessError) => {
61. hilog.error(DOMAIN, TAG, `open link failed, errCode: ${JSON.stringify(err.code)}`);
62. });
63. } catch (e) {
64. hilog.error(DOMAIN, TAG, `open link failed, errCode: ${JSON.stringify(e.code)}`);
65. }
66. })
67. }
68. .width('100%')
69. }
70. .height('100%')
71. }
72. }
```
