---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-199
title: 如何设置沉浸式窗口
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何设置沉浸式窗口
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:28+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4f5da8b58989e4c42783323e8fe8b57ab226cd8caf58bc780ffad660bdfc0592
---

在EntryAbility的onWindowStageCreate方法中通过windowStage获取window，然后分别调用setWindowLayoutFullScreen和setWindowSystemBarEnable方法。参考代码如下：

```screen
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    // 1.Get the main window of the application.
    let windowClass: window.Window | null = null;
    windowStage.getMainWindow((err: BusinessError, data) => {
      let errCode: number = err.code;
      if (errCode) {
        console.error('Failed to obtain the main window. Cause: ' + JSON.stringify(err));
        return;
      }
      windowClass = data;
      console.info('Succeeded in obtaining the main window. Data: ' + JSON.stringify(data));

      // 2.Realize immersive effects. Method 1: Set the navigation bar and status bar to not display.
      let names: Array<'status' | 'navigation'> = [];
      windowClass.setWindowSystemBarEnable(names).then(() => {
        console.info('Succeeded in setting the system bar to be visible.');
      });
      // 2.Realize immersive effects. Method 2: Set the window to a full screen layout, and coordinate with the transparency, background/text color, and highlighted icons of the navigation bar and status bar to maintain consistency with the main window display.
      let isLayoutFullScreen = true;
      windowClass.setWindowLayoutFullScreen(isLayoutFullScreen).then(() => {
        console.info('Succeeded in setting the window layout to full-screen mode.');
      });
      let sysBarProps: window.SystemBarProperties = {
        statusBarColor: '#ff00ff',
        navigationBarColor: '#00ff00',
        statusBarContentColor: '#ffffff',
        navigationBarContentColor: '#ffffff'
      };
      windowClass.setWindowSystemBarProperties(sysBarProps).then(() => {
        console.info('Succeeded in setting the system bar properties.');
      });
    })
    // 3.Load the corresponding target page for the immersive window.
    windowStage.loadContent("pages/page2", (err: BusinessError) => {
      let errCode: number = err.code;
      if (errCode) {
        console.error('Failed to load the content. Cause:' + JSON.stringify(err));
        return;
      }
      console.info('Succeeded in loading the content.');
    });
  }
};
```

**参考链接**

[窗口沉浸式](../harmonyos-guides/immersive-window-feature.md)
