---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-172
title: 如何处理H5页面的定时器退到后台不执行问题
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 如何处理H5页面的定时器退到后台不执行问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:33+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:1ce7c18c6a076ce836e149c02575eda4224bc5564cb22ed390ac448e156630ec
---

## 问题现象

WebView组件加载H5页面，H5页面有一个定时器在倒计时，退到后台后定时器会被冻结，如何让定时器在后台也正常工作。

## 背景知识

应用退至后台一小段时间后，应用进程会被挂起，无法执行对应的任务。如果应用在后台仍需要执行耗时不长的任务，如状态保存等，可以通过本文申请[短时任务](../harmonyos-guides/transient-task.md)，扩展应用在后台的运行时间。

## 解决方案

可以在应用进入后台时申请短时任务，让定时器继续执行任务，进入前台时取消短时任务。

完整示例参考如下：

* html文件：

  ```html
  <!DOCTYPE html>
  <html>
  <head>
      <meta charset="utf-8" />
      <title>纯 H5 倒计时</title>
      <style>
          html,body{height:100%;margin:0;font-size:60px;
          display:flex;align-items:center;justify-content:center;}
      </style>
  </head>
  <body>
  <div id="counter">--</div>

  <script>
      const TOTAL = 60;            // 总秒数
      let left = TOTAL;            // 剩余秒数
      const box = document.getElementById('counter');

      // 每1秒刷新一次
      const timer = setInterval(() => {
        if (left > 0) {
          left--;
          box.textContent = left + ' 秒';
        } else {
          clearInterval(timer);
          box.textContent = '时间到';
        }
      }, 1000);

      // 第一次渲染
      box.textContent = left + ' 秒';
  </script>
  </body>
  </html>
  ```

* WebviewTimer.ets文件：

  ```ts
  import { webview } from '@kit.ArkWeb';

  @Entry
  @Component
  struct WebviewTimer {
    controller = new webview.WebviewController();

    build() {
      Column() {
        Web({ src: $rawfile('timer.html'), controller: this.controller })
          .width('100%')
          .height('100%')
          .fileAccess(false)
          .geolocationAccess(false)
      }
    }
  }
  ```
* EntryAbility.ets文件：

  ```ts
  import { ConfigurationConstant, UIAbility } from '@kit.AbilityKit';
  import { hilog } from '@kit.PerformanceAnalysisKit';
  import { window } from '@kit.ArkUI';
  import { backgroundTaskManager } from '@kit.BackgroundTasksKit';

  const DOMAIN = 0x0000;

  export default class EntryAbility extends UIAbility {
    private delayId: number = -1;
    onCreate(): void {
      this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
      hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
    }

    onDestroy(): void {
      hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
    }

    onWindowStageCreate(windowStage: window.WindowStage): void {
      // Main window is created, set main page for this ability
      hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

      windowStage.loadContent('pages/WebviewTimer', (err) => {
        if (err.code) {
          hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
          return;
        }
        hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
      });
    }

    onWindowStageDestroy(): void {
      // Main window is destroyed, release UI related resources
      hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
    }

    // 退到后台5s内必须申请，否则失败
    onBackground() {
      console.info('EntryAbility → background');
      this.delayId = backgroundTaskManager.requestSuspendDelay(
        'keep-webview-timer-alive',
        () => {
          // 系统即将挂起前的回调，这里可主动保存数据
          console.info('短时任务即将超时');
        }
      ).requestId;
    }

    onForeground() {
      console.info('EntryAbility → foreground');
      if (this.delayId !== -1) {
        backgroundTaskManager.cancelSuspendDelay(this.delayId);
        this.delayId = -1;
      }
    }
  }
  ```

## 常见FAQ

Q：短时任务的限制有哪些？

A：一个应用会有一定的短时任务配额（根据系统状态和用户习惯调整），单日（24小时内）配额默认为10分钟，单次配额最大为3分钟，低电量时单次配额默认为1分钟，配额消耗完后不允许再申请短时任务，并且当日配额不会再刷新。
