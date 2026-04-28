---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-298
title: 如何在Page中获取WindowStage实例
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何在Page中获取WindowStage实例
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:16+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:2dacb74b2efab6e4acdd9b0c9e1cf7760e3eaf828efbb67f3e685a9df1b263c0
---

方式一：在onWindowStageCreate方法中获取，此方式适用于Ability生命周期内需要持久化WindowStage实例的场景。

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { window } from '@kit.ArkUI';

5. export default class EntryAbility extends UIAbility {
6. // ...
7. onWindowStageCreate(windowStage: window.WindowStage): void {
8. // Main window is created, set main page for this ability
9. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

11. windowStage.loadContent('pages/Index', (err) => {
12. if (err.code) {
13. hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
14. return;
15. }
16. hilog.info(0x0000, 'testTag', 'Succeeded in loading the content.');
17. });
18. console.info('windowStage', JSON.stringify(windowStage))
19. // Store windowStage instance globally for cross-page access
20. AppStorage.setAndLink('windowStage', windowStage)
21. }

23. // ...
24. }
```

[EntryAbilityGetWindowStageInstance.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/entryability/EntryAbilityGetWindowStageInstance.ets#L21-L44)

方式二：UIAbilityContext提供了获取WindowStage实例的接口，此方式适用于需要动态获取WindowStage的页面级场景，无需持久化存储。

```
1. // Index.ets
2. import common from '@ohos.app.ability.common';

4. @Entry
5. @Component
6. struct Index {
7. @State showAbility: string = 'get windowStage'

9. build() {
10. Row() {
11. Column() {
12. Text(this.showAbility)
13. .fontSize(30)
14. .fontWeight(FontWeight.Bold)
15. .onClick(() => {
16. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
17. console.info('Obtained WindowStage instance:',JSON.stringify(context.windowStage))
18. });
19. }
20. .width('100%')
21. }
22. .height('100%')
23. }
24. }
```

[GetWindowStageInstanceInPage.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/GetWindowStageInstanceInPage.ets#L21-L44)

参考链接

[onWindowStageCreate](../harmonyos-references/js-apis-app-ability-uiability.md#onwindowstagecreate)

[UIAbilityContext](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md)
