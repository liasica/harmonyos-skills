---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-765
title: TextInput组件禁止长按事件
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > TextInput组件禁止长按事件
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:03+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:397ed594ff2f6f850a017fc6a6cb257d4465d587919354dc928f8c9889548442
---

## 问题现象

TextInput组件长按输入框内文本时会自动选中文本，如何实现禁止长按事件？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/piXyo911QK67AvL-XyAmVQ/zh-cn_image_0000002628555694.gif "点击放大")

## 背景知识

* [TextInput](../harmonyos-references/ts-basic-components-textinput.md)是单行文本输入框组件，仅支持单文本样式。当用户长按输入框内的文本时会自动选中文本，其默认触发时间为500ms。
* [LongPressGesture](../harmonyos-references/ts-basic-gestures-longpressgesture.md)用于触发长按手势事件，触发长按手势的最少手指数为1，默认最短长按时间为500毫秒。可配置duration参数控制最短长按时长。

## 解决方案

系统长按事件触发时间为500ms，可以设置LongPressGesture长按手势事件触发时间小于500ms，实现拦截系统长按事件的效果。

```screen
@Entry
@Component
struct TextInputNoLongPress {
  @State message: string = '';

  build() {
    Column() {
      Text(`输入的内容: ${this.message}`)
        .margin({ top: 100, bottom: 30 });
      TextInput({ placeholder: '请输入内容' })
        .borderRadius(0)
        .onChange((value: string) => {
          this.message = value;
        })
        .gesture(
          LongPressGesture({ repeat: true, duration: 400 })
            // 由于repeat设置为true，长按动作存在时会连续触发，触发间隔为duration（默认值500ms）
            .onAction(() => {
              return true;
            })
            .onActionEnd(() => {
            })
        )
        .selectionMenuHidden(true);
    }
    .height('100%')
    .width('100%')
    .padding(16);
  }
}
```
