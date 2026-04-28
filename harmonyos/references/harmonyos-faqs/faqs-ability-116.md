---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-116
title: 如何跳转到系统文件管理App界面
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 如何跳转到系统文件管理App界面
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:53+08:00
doc_updated_at: 2026-03-20
content_hash: sha256:578d02862fc0889e769b43f79d568dd9122a6ef1583122d9795503bfc334778f
---

可以使用openLink的方式打开，在[openLink](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#openlink12)接口的link字段中传入系统文件管理页面的URL信息，示例代码如下：

```
1. import { common, OpenLinkOptions } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. const TAG: string = '[UIAbilityComponentsOpenLink]';
6. const DOMAIN_NUMBER: number = 0xFF00;

8. @Entry
9. @Component
10. struct Index {
11. @State message: string = '拉起文件管理';
12. context = this.getUIContext();

14. build() {
15. Row() {
16. Column() {
17. Button(this.message)
18. .width('100%')
19. .fontWeight(FontWeight.Bold)
20. .onClick(() => {
21. let context: common.UIAbilityContext = this.context.getHostContext() as common.UIAbilityContext;
22. let link: string = 'filemanager://openDirectory';
23. let openLinkOptions: OpenLinkOptions = {
24. parameters: {
25. 'fileUri': ''
26. }
27. };
28. try {
29. context.openLink(link, openLinkOptions)
30. .then(() => {
31. hilog.info(DOMAIN_NUMBER, TAG, 'Open link success.');
32. }).catch((err: BusinessError) => {
33. hilog.error(DOMAIN_NUMBER, TAG, `Open link failed. Code is ${err.code}, message is ${err.message}`);
34. });
35. } catch (paramError) {
36. hilog.error(DOMAIN_NUMBER, TAG,
37. `Failed to start link. Code is ${paramError.code}, message is ${paramError.message}`);
38. }
39. })
40. }
41. .padding({ left: 16, right: 16 })
42. .width('100%')
43. }
44. .height('100%')
45. }
46. }
```

[JumpSystemFileManagement.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/AbilityKit/entry/src/main/ets/pages/JumpSystemFileManagement.ets#L21-L67)

**参考链接：**

[UIAbilityContext.openLink](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#openlink12)
