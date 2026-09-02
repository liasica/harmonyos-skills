---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-computer-9
title: 如何设置PC窗口透明
breadcrumb: FAQ > 多设备场景 > 电脑 > 常见问题 > 如何设置PC窗口透明
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:49+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0188f45e7822ed9991c15a5ebe0ff1e2ae8078e3abbf3309411e6dc676d9e5dc
---

## 问题现象

使用setWindowBackgroundColor设置窗口背景色后，仅在手机和平板设备上生效，请问如何设置PC窗口的背景色？

## 背景知识

* [setWindowBackgroundColor](../harmonyos-references/arkts-apis-window-window.md#setwindowbackgroundcolor9)设置窗口的背景色。Stage模型下，该接口需要在[loadContent()](../harmonyos-references/arkts-apis-window-window.md#loadcontent9)或[setUIContent()](../harmonyos-references/arkts-apis-window-window.md#setuicontent9)调用生效后使用。
* [setWindowContainerColor](../harmonyos-references/arkts-apis-window-window.md#setwindowcontainercolor20)设置主窗口容器在焦点态和非焦点态时的背景色。在Stage模型下，该接口需在调用loadContent()或setUIContent()后使用。
* 窗口容器背景色（setWindowContainerColor）覆盖整个窗口区域，包括标题栏和内容区域。当同时使用该接口和setWindowBackgroundColor设置背景色时，内容区域显示窗口背景色，标题栏显示窗口容器背景色。

## 解决方案

由于PC窗口存在标题栏，因此设置PC窗口透明背景色需要setWindowBackgroundColor与setWindowContainerColor搭配使用，setWindowContainerColor设置标题栏透明，setWindowBackgroundColor设置内容区域背景色透明，方可实现整个PC窗口透明效果。示例代码如下：

* 在module.json5中配置权限。

  ```screen
  "requestPermissions": [
    {
      'name': "ohos.permission.SET_WINDOW_TRANSPARENT"
    }
  ],
  ```
* 给PC窗口设置透明色（'#00000000'）。

  ```screen
  import { window } from '@kit.ArkUI';

  @Entry
  @Component
  struct Index {
    private message: string = 'Hello World';
    uiContext = this.getUIContext();

    // 在aboutToAppear()生命周期中设置PC窗口背景颜色
    aboutToAppear(): void {
      window.getLastWindow(this.uiContext?.getHostContext(), (err, data) => {
        try {
          data.setWindowBackgroundColor('#00000000');
          data.setWindowContainerColor('#00000000', '#FF000000');
        } catch (exception) {
          console.error(`Failed to set the background color. Cause code: ${exception.code}, message: ${exception.message}`);
        }
      });
    }

    build() {
      RelativeContainer() {
        Text(this.message)
          .id('Page2HelloWorld')
          .fontSize(50)
          .fontColor(Color.White)
          .fontWeight(FontWeight.Bold)
          .alignRules({
            center: { anchor: '__container__', align: VerticalAlign.Center },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          });
      };
    }
  }
  ```
