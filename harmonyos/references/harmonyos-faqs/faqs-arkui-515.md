---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-515
title: 实现从外部获取RichEditor焦点
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 实现从外部获取RichEditor焦点
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:00+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ea64d6efbf99d50ea99c17af3cb9af8bf2262eaeae503ee4a88309c148d0926f
---

## 问题现象

RichEditor点击输入框后会自动获取焦点，然后弹出软键盘；那如何实现在输入框之外获取焦点，弹出软键盘？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/dMUTUV8YQV63ysbdBumblQ/zh-cn_image_0000002658787901.png "点击放大")

## 背景知识

在HarmonyOS中，想要实现[RichEditor](../harmonyos-references/ts-basic-components-richeditor.md)设置焦点后自动弹出软键盘，需要使用到焦点控制模块[focusControl](../harmonyos-references/ts-universal-attributes-focus.md#focuscontrol9)的requestFocus方法，可以主动让焦点转移至参数指定的组件上。非当前帧生效，在下一帧才生效，建议使用FocusController中的requestFocus。

## 解决方案

使用FocusController中的requestFocus主动获取焦点。

1. 先使用UIContext中的getFocusController()方法获取实例，再通过此实例调用对应方法。
2. 通过组件的id将焦点转移到组件树对应的实体节点，生效时间为当帧生效。
3. clearFocus清除焦点，将焦点强制转移到页面根容器节点，焦点链路上其他节点失去焦点。
4. 使用focusControl中的方法，调用此接口可以主动让焦点转移至参数指定的组件上，焦点转移生效时间为下一个帧信号。

完整示例参考如下：

```ts
@Entry
@Component
struct RequestExample {
  controller: RichEditorController = new RichEditorController();
  @State btColor: string = '#ff2787d9';
  @State btColor2: string = '#ff2787d9';

  build() {
    Column({ space: 20 }) {
      Column({ space: 5 }) {
        Stack() {
          RichEditor({ controller: this.controller })
            .copyOptions(CopyOptions.None)
            .align(Alignment.TopStart)
            .height(100)
            .borderWidth(1)
            .borderColor(Color.Black)
            .width('60%')
            .onSelect(() => {
            })
            .onFocus(() => {
              this.btColor = '#ffd5d5d5';
            })
            .onBlur(() => {
              this.btColor = '#ff2787d9';
            })
            .id('testButton');
        };

        Button('Button')
          .width(200)
          .height(70)
          .fontColor(Color.White)
          .focusOnTouch(true)
          .backgroundColor(this.btColor2)
          .onFocus(() => {
            this.btColor2 = '#ffd5d5d5';
          })
          .onBlur(() => {
            this.btColor2 = '#ff2787d9';
          })
          .id('testButton2');
        Divider()
          .vertical(false)
          .width('80%')
          .backgroundColor('#ff707070')
          .height(10);
        Button('FocusController.requestFocus')
          .width(200)
          .height(70)
          .fontColor(Color.White)
          .onClick(() => {
            this.getUIContext().getFocusController().requestFocus('testButton');
          })
          .backgroundColor('#ff2787d9');
        Button('focusControl.requestFocus')
          .width(200)
          .height(70)
          .fontColor(Color.White)
          .onClick(() => {
            focusControl.requestFocus('testButton2');
          })
          .backgroundColor('#ff2787d9');
        Button('clearFocus')
          .width(200)
          .height(70)
          .fontColor(Color.White)
          .onClick(() => {
            this.getUIContext().getFocusController().clearFocus();
          })
          .backgroundColor('#ff2787d9');
      };
    }
    .width('100%')
    .height('100%');
  }
}
```

上述示例包含以下3步：

1. 点击FocusController.requestFocus按钮，RichEditor输入框获取焦点。
2. 点击focusControl.requestFocus按钮，Button获取焦点。
3. 点击clearFocus按钮，Button失去焦点。

## 常见FAQ

Q：子窗口中的RichEditor富文本组件，如何在子窗口显示时，富文本组件自动获取焦点并弹出软键盘？

A：需要通过inputMethodController才可以在页面获取焦点时自动拉起键盘。
