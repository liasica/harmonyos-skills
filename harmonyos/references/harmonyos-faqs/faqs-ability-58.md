---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-58
title: 如何拉起浏览器应用
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 如何拉起浏览器应用
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:46+08:00
doc_updated_at: 2026-03-20
content_hash: sha256:427d9dc0e3aa44837e6f239ffbf8cc5101ad6fb4f3b6619168e18cb9050291d5
---

开发者可以通过在 want 参数中隐式指定 action 为 ohos.want.action.viewData 来启动浏览器应用，并在 want的 uri 参数中配置要打开的网页链接。此时，系统将启动设备上的默认浏览器。如果设备上存在多个浏览器应用，并且希望用户能够自行选择要使用的浏览器，需要在 parameters 中设置 ohos.ability.params.showDefaultPicker 为 true。具体代码如下所示。

```
1. import { common, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. function startBrowsableAbility(context: common.UIAbilityContext): void {
5. let want: Want = {
6. action: 'ohos.want.action.viewData',
7. entities: ['entity.system.browsable'],
8. uri: 'https://www.huawei.com/',
9. parameters: {
10. 'ohos.ability.params.showDefaultPicker': true
11. }
12. };
13. context.startAbility(want)
14. .then(() => {
15. console.info('Start browsableAbility successfully.');
16. })
17. .catch((err: BusinessError) => {
18. console.error(`Failed to startAbility. Code: ${err.code}, message: ${err.message}`);
19. });
20. }

22. @Entry
23. @Component
24. struct BrowsableAbilityView {
25. @State message: string = 'Pull up the browser and open the Huawei official website';

27. build() {
28. Row() {
29. Column() {
30. Button(this.message)
31. .fontSize(24)
32. .fontWeight(FontWeight.Bold)
33. .onClick(() => {
34. const context: common.UIAbilityContext = this.getUIContext().getHostContext()! as common.UIAbilityContext;
35. startBrowsableAbility(context);
36. })
37. }
38. .width('100%')
39. }
40. .height('100%')
41. }
42. }
```

[PullUpBrowserApplication.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/AbilityKit/entry/src/main/ets/pages/PullUpBrowserApplication.ets#L21-L63)
