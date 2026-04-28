---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-101
title: 如何判断应用当前在前台/后台
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 如何判断应用当前在前台/后台
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:51+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:a5bc586c0566695d7cb9d14ea933b932b663f6aa0b82223a903f21ec4231fd33
---

可以通过以下两种方式获取：

* 方案一：通过窗口的[on('windowStageEvent')](../harmonyos-references/arkts-apis-window-windowstage.md#onwindowstageevent9)接口，开启 WindowStage 生命周期变化的监听，获取当前的生命周期状态。

  代码示例：

  ```
  1. // EntryAbility.ets
  2. onWindowStageCreate(windowStage: window.WindowStage): void {
  3. // Main window is created, set main page for this ability
  4. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
  5. try {
  6. windowStage.on('windowStageEvent', (data) => {
  7. if (data === window.WindowStageEventType.SHOWN) {
  8. hilog.info(0x0000, 'testTag', '%{public}s', 'window stage is shown');
  9. } else if (data === window.WindowStageEventType.HIDDEN) {
  10. hilog.info(0x0000, 'testTag', '%{public}s', 'window stage is hidden');
  11. }
  12. });
  13. } catch (err) {
  14. hilog.error(0x0000, 'testTag', '%{public}s', 'Failed to enable the listener for ' +
  15. 'window stage event changes. Cause:' + JSON.stringify(err));
  16. }
  17. windowStage.loadContent('pages/Index', (err, data) => {
  18. if (err.code) {
  19. hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
  20. return;
  21. }
  22. hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
  23. });
  24. }
  ```

  [EntryAbilityStageEvent.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/AbilityKit/entry/src/main/ets/entryability/EntryAbilityStageEvent.ets#L22-L45)
* 方案二：通过ApplicationContext的[getRunningProcessInformation()](../harmonyos-references/js-apis-inner-application-applicationcontext.md#applicationcontextgetrunningprocessinformation)方法获取进程信息，其中包含[当前进程运行状态](../harmonyos-references/js-apis-app-ability-appmanager.md#processstate10)，可以判断是否处于前台。
