---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-202
title: 如何获取状态栏和导航栏高度
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何获取状态栏和导航栏高度
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:59+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:7d7d7ac5508ceb81d7c5fcf3c857a450907b678a41a27192850e3ac117401e24
---

获取系统状态栏和导航栏等规避区域。使用系统提供的 getWindowAvoidArea 获取系统规避区域。返回值中的 topRect.height 即为系统状态栏的高度，单位为 px。参考代码如下：

```ts
// MainAbility.ets
import { common, UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

/**
 * Get the height of the system status bar and navigation bar
 * @param context
 * @returns
 */
async function getWindowAvoidArea(context: common.UIAbilityContext): Promise<window.AvoidArea | null> {
  try {
    // The default area of the system includes the status bar and navigation bar
    const mainWindow = await window.getLastWindow(context);
    const avoidAreaType = window.AvoidAreaType.TYPE_SYSTEM;
    const avoidArea = mainWindow.getWindowAvoidArea(avoidAreaType);
    const avoidAreaTypeNavigationBar = window.AvoidAreaType.TYPE_NAVIGATION_INDICATOR;
    const avoidAreaNavigationBar = mainWindow.getWindowAvoidArea(avoidAreaTypeNavigationBar);
    const height = avoidArea.topRect.height;
    const heightNavigationBar = avoidAreaNavigationBar.bottomRect.height;
    return avoidArea
  } catch (e) {
    console.log('getWindowAvoidArea fail');
    return null
  }
}

export default class MainAbility extends UIAbility {
  // do something
  async onWindowStageCreate(windowStage: window.WindowStage) {
    getWindowAvoidArea(this.context);
    windowStage.loadContent('pages/index');
  }

  // do something
}
```

**参考链接**

[getWindowAvoidArea](../harmonyos-references/js-apis-arkui-uiextension.md#getwindowavoidarea)
