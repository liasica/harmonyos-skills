---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-computer-5
title: 自由多窗模式下，应用页面与标题栏三键区域重叠
breadcrumb: FAQ > 多设备场景 > 电脑 > 常见问题 > 自由多窗模式下，应用页面与标题栏三键区域重叠
category: harmonyos-faqs
scraped_at: 2026-10-28T07:46:38+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b7af9dd0abe7382658d4ba5f36f87d6c1402c64f86266fb6210710fd9270ac59
---

## 问题现象

应用在自由多窗模式下，标题栏右侧的最大化、最小化、关闭按钮与页面重叠，导致页面内容被遮挡。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/Z-VGdNb-TdCK4t8ISIs2XQ/zh-cn_image_0000002628392458.png "点击放大")

## 背景知识

* [getWindowDecorHeight](../harmonyos-references/arkts-apis-window-window.md#getwindowdecorheight11)：获取窗口的标题栏高度。
* [setWindowDecorVisible](../harmonyos-references/arkts-apis-window-window.md#setwindowdecorvisible11)：设置窗口标题栏是否可见。

## 问题定位

1. 检查代码中是否通过setWindowDecorVisible设置窗口标题栏隐藏，设置隐藏后，标题栏中的三键区域会下沉到页面区域中显示。
2. 检查代码中是否使用getWindowDecorHeight获取标题栏三键按钮区域的高度。
3. 检查代码中是否使用padding设置页面顶部边距，避开三键按钮区域。

## 分析结论

应用未使用getWindowDecorHeight获取标题栏三键按钮区域的高度，并对页面使用padding设置边距避让三键按钮区域，导致页面内容被三键按钮区域遮挡。

## 修改建议

使用getWindowDecorHeight获取标题栏三键按钮区域，同时页面使用padding避让该区域。

```screen
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct DecorHeightDemo {
  @State titleHeight: number = 0;

  aboutToAppear(): void {
    try {
      let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      let windowStage = context.windowStage;
      let windowClass = windowStage.getMainWindowSync();
      // 获取标题栏高度
      this.titleHeight = windowClass.getWindowDecorHeight();
      windowClass.setWindowDecorVisible(false);
    } catch (exception) {
      console.error(`Failed to enable the listener for window title buttons area changes. Cause code: ${exception.code}, message: ${exception.message}`);
    }
  }

  build() {
    Column() {
      Text('测试页面内容是否会被遮挡');
    }
    .width('100%')
    .height('100%')
    .alignItems(HorizontalAlign.End)
    // 使用padding避让
    .padding({ top: this.titleHeight });
  }
}
```
