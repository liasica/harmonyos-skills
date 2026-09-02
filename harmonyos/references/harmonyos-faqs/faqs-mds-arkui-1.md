---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-mds-arkui-1
title: 横竖屏切换时应用布局会发生留白、溢出屏幕的现象
breadcrumb: FAQ > 多设备场景 > UI框架 > 方舟UI框架（ArkUI） > 横竖屏切换时应用布局会发生留白、溢出屏幕的现象
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:49+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3386880378fb11ab591ecb20f649e005757b7abe1ef065eaa149b1ddff58ce4d
---

## 问题现象

应用直接横屏冷启动显示正常，切换竖屏底部留白；应用直接竖屏冷启动显示正常，切换横屏两侧溢出。

## 背景知识

[横竖屏切换](../best-practices/bpta-landscape-and-portrait-development.md)：横竖屏切换功能实现应用内既支持竖屏显示也支持横屏显示的效果。

## 问题定位

1. 应用单独横屏或单独竖屏启动无问题，说明应用启动时监听了设备的显示尺寸，并设置相应的组件大小。
2. 横竖屏切换时，应用却发生了留白、溢出等异常现象，建议检查代码中是否使用[on('windowSizeChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowstatuschange11)监听了设备尺寸变化，判断当前是横屏还是竖屏。
3. 检查异常的页面是否通过判断当前是横屏还是竖屏，分别展示不同的布局。

## 分析结论

应用未监听设备的横竖屏变化，并动态的更改页面布局的宽高，导致页面在横竖屏切换的过程中，出现了留白、溢出等异常情况。

## 修改建议

通过on('windowSizeChange')监听设备的横竖屏变化，并动态的更改页面布局。

```screen
import { window } from '@kit.ArkUI';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct LandscapeDemo {
  @State isLandscape: boolean = false;

  getWindow(): window.Window {
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    let windowStage = context.windowStage;
    let windowClass = windowStage.getMainWindowSync();
    return windowClass;
  }

  onPageShow(): void {
    let windowClass: window.Window = this.getWindow();
    let properties = windowClass.getWindowProperties();
    let rect = properties.windowRect;
    this.isLandscape = rect.width > rect.height;
  }

  aboutToAppear() {
    let windowClass: window.Window = this.getWindow();
    // 监听窗口尺寸的变化
    windowClass.on('windowSizeChange', (data) => {
      this.isLandscape = data.width > data.height;
    });
  }

  build() {
    Column() {
      if (this.isLandscape === true) {
        // 横屏的布局
        Text('当前是横屏状态');
      } else {
        // 竖屏的布局
        Text('当前是竖屏状态');
      }
    }
    .width('100%')
    .height('100%');
  }
}
```
