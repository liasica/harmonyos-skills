---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-279
title: 如何在代码中触发应用后台运行
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何在代码中触发应用后台运行
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:13+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:e783f6bd20d24efb696e34881acd206c8a7fe9341c87ed4382072a9764b72d70
---

[minimize](../harmonyos-references/arkts-apis-window-window.md#minimize11)方法提供该能力。若主窗口调用，可以将窗口最小化，并支持在Dock栏中还原。若子窗口调用，可以将窗口隐藏。

参考代码如下：

在EntryAbility.ets的onWindowStageCreate回调中全局保存windowStage：

```
1. AppStorage.setOrCreate('context',windowStage);
```

[EntryAbilityBackRunning.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/entryability/EntryAbilityBackRunning.ets#L40-L40)

在页面中获取windowStage并调用方法实现最小化：

```
1. import { window } from '@kit.ArkUI';

3. @Component
4. export struct BackgroundExecution {
5. @State message: string = 'Run in the background';

7. build() {
8. Column() {
9. Button(this.message)
10. .width('40%')
11. .onClick(() => {
12. let windowStage = AppStorage.get('context') as window.WindowStage;
13. if (windowStage) {
14. // It can be minimized when it is the main window and hidden when it is a sub-window.
15. windowStage.getMainWindowSync().minimize();
16. }
17. })
18. }
19. .height('100%')
20. .width('100%')
21. .justifyContent(FlexAlign.Center)
22. }
23. }
```

[TriggeringApplicationBackendRunningInCode.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/TriggeringApplicationBackendRunningInCode.ets#L21-L43)
