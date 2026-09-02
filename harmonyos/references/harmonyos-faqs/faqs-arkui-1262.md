---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1262
title: RichEditor自定义菜单文本复制
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > RichEditor自定义菜单文本复制
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:17+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:59640aa86b76ccec64fc2ba721b46e50d7d1c7d5ea3560c7373ebda9e37b122a
---

## 问题现象

RichEditor自定义菜单中如何实现复制功能？

## 背景知识

* [RichEditor](../harmonyos-references/ts-basic-components-richeditor.md)：支持图文混排和文本交互式编辑的组件。
* [bindSelectionMenu](../harmonyos-references/ts-basic-components-richeditor.md#bindselectionmenu)：设置自定义选择菜单。
* [onSelect](../harmonyos-references/ts-basic-components-richeditor.md#onselect)：鼠标左键双击选中内容时，会触发回调；松开鼠标左键后，会再次触发回调。手指长按选中内容时，会触发回调；松开手指后，会再次触发回调。
* [getSpans](../harmonyos-references/ts-basic-components-richeditor.md#getspans)：获取span信息。
* [@ohos.pasteboard (剪贴板)](../harmonyos-references/js-apis-pasteboard.md)：本模块提供管理系统剪贴板的能力，支持系统复制、粘贴功能。

## 解决方案

实现步骤如下：

1. 使用@Builder创建一个自定义菜单组件，实现复制按钮。
2. 为自定义菜单组件的复制按钮添加onClick事件，判断按钮为复制时，使用getSpans获取选择的span信息，判断span信息的类型，过滤出纯文本，并复制。
3. 将复制的纯文本添加进剪贴板。
4. 使用bindSelectionMenu属性绑定RichEditor自定义菜单组件。

代码如下：

```typescript
import { pasteboard } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

@Entry
@Component
struct RichEditorExample {
  controller: RichEditorController = new RichEditorController();
  @State start: number = -1;
  @State end: number = -1;
  private optionsPopup: string[] = ['复制'];
  @State textStyle: RichEditorTextStyle = {};
  @State textContent: string = '';
  @State imageStyle: RichEditorImageSpanStyle = {};
  @State imageStr: ResourceStr | undefined = '';

  onPageShow(): void {
    window.getLastWindow(this.getUIContext().getHostContext(), (err, win) => {
      if (err.code) {
        return;
      }
      win.setWindowLayoutFullScreen(true);
    });
  }

  // 自定义菜单
  @Builder
  LongPressTextCustomMenu() {
    Row() {
      ForEach(this.optionsPopup, (item: string, index) => {
        Text(item)
          .padding(12)
          .onClick(() => {
            if (item === '复制') {
              this.controller.getSpans({
                start: this.start,
                end: this.end
              }).forEach(item => {
                if (typeof (item as RichEditorImageSpanResult).imageStyle !== 'undefined') {
                  this.imageStr = (item as RichEditorImageSpanResult).valueResourceStr;
                  this.imageStyle = (item as RichEditorImageSpanResult).imageStyle;
                } else {
                  this.textContent =
                    (item as RichEditorTextSpanResult).value.slice((item as RichEditorTextSpanResult).offsetInSpan[0],
                      (item as RichEditorTextSpanResult).offsetInSpan[1]);
                  this.textStyle = (item as RichEditorTextSpanResult).textStyle;
                }
              });
              let pasteboardData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, this.textContent);
              // 获取系统剪贴板对象
              let systemPasteboard = pasteboard.getSystemPasteboard();
              systemPasteboard.setData(pasteboardData); // 将数据放入剪贴板
              systemPasteboard.getData().then((data) => { // 读取剪贴板内容
                if (data) {
                  this.getUIContext().getPromptAction().showToast({ message: '复制成功' });
                } else {
                  this.getUIContext().getPromptAction().showToast({ message: '复制失败' });
                }
              });
            }
            // 取消选中
            this.start = -1;
            this.end = -1;
            // 关闭自定义菜单
            this.controller.closeSelectionMenu();
          });
        // 设置间隔
        if (index < this.optionsPopup.length - 1) {
          Divider().height(10).vertical(true);
        }
      });
    }

    .backgroundColor(Color.White)
    .shadow({
      radius: 10,
      color: '#ffe0dede',
      offsetY: 20
    })
    .borderRadius(25);
  }

  build() {
    Column() {
      RichEditor({ controller: this.controller })
        .height(200)
        .margin({ top: 80 })
        .width('100%')
        .copyOptions(CopyOptions.LocalDevice)
        .bindSelectionMenu(RichEditorSpanType.DEFAULT, this.LongPressTextCustomMenu,
          RichEditorResponseType.DEFAULT) // 自定义菜单
        .onSelect((value: RichEditorSelection) => {
          this.start = value.selection[0];
          this.end = value.selection[1];
          console.info('输出：this.text', this.start, this.end);
        })
        .onReady(() => {
          this.controller.addTextSpan('012345',
            {
              style:
              {
                fontColor: Color.Black,
                fontSize: 30
              }
            });
          // 在实际使用时可替换为需要的图片
          this.controller.addImageSpan($r('app.media.startIcon'),
            {
              imageStyle:
              {
                size: [57, 57]
              }
            });
        })
        .onPaste(() => {
        });
    }
    .height('100%')
    .backgroundColor('#fff3f1f1');
  }
}
```

效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/KGP7XVAtR-aIqAMM7n2BCQ/zh-cn_image_0000002658955327.png "点击放大")
