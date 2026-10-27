---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/ability-kit-faq-0012
title: 应用前后台状态判断与监听常见问题
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 常见问题 > 应用前后台状态判断与监听常见问题
category: harmonyos-faqs
scraped_at: 2026-10-28T07:46:47+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:5ea7e870b5c7f9132ea63edbe03ada2fb38160579c598fed153443abbfc01e42
---

**Q：如何判断应用当前在前台/后台？**

**A**：可以通过以下两种方式获取：

* 方案一：通过窗口的[on('windowStageEvent')](../harmonyos-references/arkts-apis-window-windowstage.md#onwindowstageevent9)接口，开启 WindowStage 生命周期变化的监听，获取当前的生命周期状态。

  代码示例：

  ```ts
  // EntryAbility.ets
  onWindowStageCreate(windowStage: window.WindowStage): void {
    // Main window is created, set main page for this ability
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
    try {
      windowStage.on('windowStageEvent', (data) => {
        if (data === window.WindowStageEventType.SHOWN) {
          hilog.info(0x0000, 'testTag', '%{public}s', 'window stage is shown');
        } else if (data === window.WindowStageEventType.HIDDEN) {
          hilog.info(0x0000, 'testTag', '%{public}s', 'window stage is hidden');
        }
      });
    } catch (err) {
      hilog.error(0x0000, 'testTag', '%{public}s', 'Failed to enable the listener for ' +
        'window stage event changes. Cause:' + JSON.stringify(err));
    }
    windowStage.loadContent('pages/Index', (err, data) => {
      if (err.code) {
        hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
        return;
      }
      hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
    });
  }
  ```
* 方案二：通过ApplicationContext的[getRunningProcessInformation()](../harmonyos-references/js-apis-inner-application-applicationcontext.md#applicationcontextgetrunningprocessinformation)方法获取进程信息，其中包含[当前进程运行状态](../harmonyos-references/js-apis-app-ability-appmanager.md#processstate10)，可以判断是否处于前台。
