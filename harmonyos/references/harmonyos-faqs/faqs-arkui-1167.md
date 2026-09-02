---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1167
title: 如何使两个TextInput组件有序输入内容
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何使两个TextInput组件有序输入内容
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:07+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ace7a79a80896abbbbe655b7f8cb8b03b3bf07232261b8f2a801c9490726cbdf
---

## 问题现象

有两个TextInput组件A和B，在B组件输入的时候，需先判断A组件是否有输入内容，如果A组件没有输入内容，B组件不允许输入并提示：请先输入A组件。只有当A组件有输入内容时，B组件才可以正常输入内容并展示。请问该场景如何实现？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/YCdoLFM8RjiusOfM3McVXw/zh-cn_image_0000002658809139.gif "点击放大")

## 背景知识

* [TextInput](../harmonyos-references/ts-basic-components-textinput.md)：单行文本输入框组件。
* [@ohos.promptAction](../harmonyos-references/js-apis-promptaction.md)：创建并显示文本提示框、对话框和操作菜单。
* [focusable](../harmonyos-references/ts-universal-attributes-focus.md#focusable)：设置当前组件是否可以获焦。

## 解决方案

1. 设置一个状态变量isShow控制B组件是否可以获取焦点。
2. 在onChange事件中使用if/else条件判断。
3. 当A组件有输入内容时，赋值isShow为true，此时B组件获取焦点能够输入。当A组件没有输入内容时，赋值isShow值为false，此时B组件获取不了焦点也不能够输入内容。

完整示例参考如下：

```ts
@Entry
@Component
struct OrderIndex {
  @State message: string = '';
  @State isShow: boolean = false;
  private uiContext: UIContext = this.getUIContext();

  build() {
    Column() {
      TextInput({ placeholder: 'A' })
        .margin({ top: 16, bottom: 16 })
        .onChange((val: string) => {
          this.message = val;
          if (val !== '') {
            this.isShow = true;
          } else {
            this.isShow = false;
          }
        });
      TextInput({ placeholder: 'B', })
        .focusable(this.isShow) // 是否可以获焦
        .onClick(() => {
          if (!this.isShow) {
            this.uiContext.getPromptAction().showToast({
              message: '请先输入A组件'
            });
          }
        });
    }
    .height('100%')
    .margin({ left: 16, right: 16 });
  }
}
```
