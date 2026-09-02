---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1362
title: TextInput组件如何实现文本默认选中效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > TextInput组件如何实现文本默认选中效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:21+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:5f6c399b9af654f7c0f31eee4e798e70e1d2797b756b6e5482361d5573ad4502
---

## 问题现象

页面初次构建完成时，如何使TextInput组件获取焦点并且默认文本全部选中？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/i9MWexYBQmWr8SnFbIBhkA/zh-cn_image_0000002658841263.png "点击放大")

## 背景知识

* [TextInput](../harmonyos-references/ts-basic-components-textinput.md)：单行文本输入框组件。
* [defaultFocus](../harmonyos-references/ts-universal-attributes-focus.md#defaultfocus9)：设置当前组件是否为当前页面上的默认焦点。
* [setTextSelection](../harmonyos-references/ts-basic-components-textinput.md#settextselection10)：设置文本选择区域并高亮显示。

## 解决方案

1. 使用defaultFocus属性可使TextInput组件在页面初次构建完成时自动获取焦点。
2. 配合setTextSelection方法设置文本选择区域并高亮显示实现文本默认选中效果。

示例参考如下：

```screen
@Entry
@Component
struct SelectedIndex {
  text: string = 'Hello World';
  controller: TextInputController = new TextInputController();

  build() {
    Row() {
      TextInput({
        text: '选中默认文本内容',
        placeholder: 'input your word...',
        controller: this.controller
      })
        .width('100%')
        .defaultFocus(true) // 默认获取焦点
        .onFocus(() => {
          this.controller.setTextSelection(0, this.text.length); // 选择文本区域
        });
    }
    .padding({ left: 16, right: 16 })
    .width('100%')
    .height('100%');
  }
}
```

## 总结

setTextSelection要在TextInput组件获焦时执行才能生效。
