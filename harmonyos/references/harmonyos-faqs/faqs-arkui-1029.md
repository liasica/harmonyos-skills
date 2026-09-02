---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1029
title: 如何判断目标窗口上方是否被全部遮挡
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 如何判断目标窗口上方是否被全部遮挡
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:14+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f44d69427d920712bb72e2fcb954d5a5d7ac480b6570807d4eea783833fde353
---

## 问题现象

PC应用会议窗口，应用会判断若该窗口被完全遮挡，则会弹出小窗口用来显示“声音、麦克风”等信息，若未被完全遮挡，则不显示。针对这种场景如何进行判断？

## 背景知识

* [on('windowVisibilityChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowvisibilitychange11)：开启本窗口可见状态变化事件的监听。
* [on('occlusionStateChanged')](../harmonyos-references/arkts-apis-window-window.md#onocclusionstatechanged22)：开启窗口可见性状态变化事件的监听。对于非主窗，其阴影区域部分也会参与到可见性遮挡计算中。

## 解决方案

判断目标窗口上方是否被完全遮挡有2种方案：

* **方案一**：通过判断应用窗口是否可见，来判断应用窗口是否被完全遮挡。示例代码如下：

  ```screen
  onWindowStageCreate(windowStage: window.WindowStage): void {
    // Main window is created, set main page for this ability
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
        return;
      }
      windowClass = data;
      try {
        windowClass.on('windowVisibilityChange', (boolean) => {
          console.info('Window visibility changed, isVisible=' + boolean);
        });
      } catch (exception) {
        console.error(`Failed to register callback. Cause code: ${exception.code}, message: ${exception.message}`);
      }
    });

    windowStage.loadContent('pages/Index', (err) => {
      if (err.code) {
        hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
        return;
      }
      hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
    });
  }
  ```
* **方案二**：API22开始，可通过监听on('occlusionStateChanged')获取[OcclusionState](../harmonyos-references/arkts-apis-window-e.md#occlusionstate22)来判断目标窗口上方是否完全可见。代码参考[on('occlusionStateChanged')](../harmonyos-references/arkts-apis-window-window.md#onocclusionstatechanged22)示例。

## 常见FAQ

Q：通过createSubWindow创建子窗口，子窗口遮挡主窗口时是否会触发主窗口on('windowVisibilityChange')监听。

A：默认情况下，创建的子窗口背景色是不透明的，所以会触发主窗口on('windowVisibilityChange')监听。不想触发可见性监听，可通过[setWindowBackgroundColor](../harmonyos-references/arkts-apis-window-window.md#setwindowbackgroundcolor9)设置ARGB颜色，且透明通道（A）不能为FF（如'#FE00FF00'），即设置部分透明度。
