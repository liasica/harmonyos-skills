---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-215
title: 如何动态控制键盘绑定在不同的TextInput上
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何动态控制键盘绑定在不同的TextInput上
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:59+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:6cd573061448023ea45f8575224d0cf275ea58af114b2a4dc0ce2dd4fc0efa1a
---

软键盘的收起和弹出与输入框的获焦和失焦相关。可以通过 focusControl 动态控制输入框焦点的转移，从而控制软键盘的显示和隐藏。将焦点转移到目标输入框可以实现键盘的动态切换。参考代码如下：

```ts
@Entry
@Component
struct DynamicControlKeyboard {
  // Whether focus is on "key1" TextInput
  private flag: boolean = true;
  @Builder
  customKeyboardBuilder() {
    Row() {
      Text('Customize keyboard')
    }
    .justifyContent(FlexAlign.Center)
    .width('1260px')
    .height('1161px')
    .backgroundColor(Color.Brown)
  }
  build() {
    Column({space: 10}) {
      TextInput()
        .key('key1')
        .onAppear(() => {
          focusControl.requestFocus('key1');
        })
        .defaultFocus(true)
      TextInput()
        .key('key2')
        .customKeyboard(this.customKeyboardBuilder())
      Button('Switch TextInput')
        .onClick(() => {
          if (this.flag) {
            console.info('TextInput2 ==> ' + focusControl.requestFocus('key2'));
          } else {
            console.info('TextInput1 ==> ' + focusControl.requestFocus('key1'));
          }
          this.flag = !this.flag;
        })
      Button()
        .width(0)
        .height(0)
        .key('key3')
    }
    .padding({ top: 20 })
    .width('100%')
    .height('100%')
    .onClick(() => {
      focusControl.requestFocus('key3');
    })
  }
}
```

效果如图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/g4X9_vyIT22ZO1tVoC4gKQ/zh-cn_image_0000002624475924.png)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/2ctK9rJKR3SUThdi3cXR4g/zh-cn_image_0000002654835233.png "点击放大")

**参考链接**

[focusControl](../harmonyos-references/ts-universal-attributes-focus.md#focuscontrol9)
