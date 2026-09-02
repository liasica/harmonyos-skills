---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1062
title: TextInput组件如何使用showError展示错误文本
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > TextInput组件如何使用showError展示错误文本
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:26+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9eb96fe55fc23e103aad1b80b80e6471e4357a3ba5f1d7fc471ee4acc81c7252
---

## 问题现象

如何实现TextInput在用户输入错误时自动显示错误信息和调整UI布局？

问题截图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/lBVkJstLTya82M18aGx-kQ/zh-cn_image_0000002658806473.png "点击放大")

## 背景知识

* [TextInput](../harmonyos-references/ts-basic-components-textinput.md)单行文本输入框组件。
* [showError](../harmonyos-references/ts-basic-components-textinput.md#showerror10)设置错误状态下提示的错误文本或者不显示错误状态。当参数类型为ResourceStr并且输入内容不符合定义规范时，提示错误文本，当提示错误单行文本超长时，末尾以省略号显示。当参数类型为undefined时，不显示错误状态。

## 解决方案

1.使用状态变量修饰error，在onChange()回调里将需提示的错误文本赋值error，即可实现自动显示错误信息。

2.文本组件设置alignSelf(ItemAlign.Start)，实现提示错误文本时，UI跟随调整。

```ts
@Entry
@Component
struct ShowError {
  @State password: string = '';
  @State error: string = '';
  controller: TextInputController = new TextInputController();

  build() {
    Column() {
      Row() {
        Text('密码:')
          .fontSize(18)
          .textAlign(TextAlign.Center)
          .alignSelf(ItemAlign.Start)
          .height(50);

        TextInput({ placeholder: '请输入密码', text: $$this.password, controller: this.controller })
          .height(50)
          .showError(this.error)
          .newExtend()
          .borderRadius(20)
          .onChange((value: string) => {
            this.error = value;
            this.password = value;
          });
      }
      .margin(10);
    }
    .justifyContent(FlexAlign.Center)
    .height('100%')
    .width('100%')
    .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
    .backgroundColor('#F1F3F5');
  }
}

// 自定义属性
@Extend(TextInput)
function newExtend() {
  .layoutWeight(1)
  .placeholderColor('#99182431')
  .backgroundColor('#F1F3F5')
  .width('100%')
  .fontSize(14)
  .copyOption(CopyOptions.InApp)
  .borderWidth(1);
}
```
