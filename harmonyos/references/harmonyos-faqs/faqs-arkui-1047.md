---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1047
title: TextInput如何动态设置下划线颜色
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > TextInput如何动态设置下划线颜色
category: harmonyos-faqs
scraped_at: 2026-10-28T07:47:16+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:50094eb61e94ff4d6df6afe298c9772c9c9517a60aa6bc4c80506dc143f2dab5
---

## 问题现象

TextInput设置InputType.NUMBER\_DECIMAL类型后，切换焦点，如何解决showUnderline下划线的状态颜色无变化的问题？

## 背景知识

* [TextInput](../harmonyos-references/ts-basic-components-textinput.md)单行文本输入框组件。
* [showUnderline](../harmonyos-references/ts-basic-components-textinput.md#showunderline10)：设置是否开启下划线。
* [outline](../harmonyos-references/ts-universal-attributes-outline.md#outline)属性是绘制于元素周围的一条线，位于边框边缘的外围，可起到突出元素的作用。

## 解决方案

TextInput设置showUnderline下划线只支持InputType.Normal类型，其他类型不生效。可通过outline属性实现动态设置下划线颜色的效果。

1. 创建颜色变量bottomLineColor，设置为outline属性的color。
2. 在onFocus、onBlur设置切换焦点时的颜色即可。

```ts
@Entry
@Component
struct TextInputExample {
  @State bottomLineColor: string = '#F1F3F5';

  build() {
    Column({ space: 20 }) {
      TextInput({ placeholder: '请输入文本内容' })
        .width('100%')
        .type(InputType.NUMBER_DECIMAL)
        .showUnderline(true)
        .borderRadius(0)
        .backgroundColor(Color.White)
        // 设置下划线
        .outline({
          width: { bottom: 1 },
          color: this.bottomLineColor
        })
        .onFocus(() => {
          // 获焦设置蓝色
          this.bottomLineColor = '#0A59F7';
        })
        .onBlur(() => {
          // 失焦设置灰
          this.bottomLineColor = '#F1F3F5';
        })
      TextInput({ placeholder: '提示文本内容' })
        .width('100%')
        .type(InputType.NUMBER_DECIMAL)
        .showUnderline(true)
        .borderRadius(0)
        .backgroundColor(Color.White)
    }
    .width('100%')
    .padding(16)
  }
}
```

运行效果：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/6QbjhK7nRD6X5lXb2UcUyg/zh-cn_image_0000002658804821.png "点击放大")
