---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-680
title: TextInput绑定的Popup气泡无法弹出
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > TextInput绑定的Popup气泡无法弹出
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:21+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:306025c95f8e4aff8f5cfbe5bb3c114d8c4cd35a65f43ecbbd28c2f63d316661
---

## 问题现象

当TextInput组件提示文本为'请输入服务器标识'时，点击输入框组件，Popup气泡可以正常弹出。当提示文本为'请输入服务器标识/IP/域名'时，气泡无法弹出。

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/zpSARoBiRPGAFYWY93EjOg/zh-cn_image_0000002628554740.png "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/ArR8N0nrTmOrV5IgEwjD4A/zh-cn_image_0000002628394844.png "点击放大")

## 背景知识

* [智能填充服务](../harmonyos-guides/scenario-fusion-introduction-to-smart-fill.md)提供场景化的输入建议，完善应用/元服务的系统开发能力，实现用户对复杂表单的一键填充。其支持填充的字段可以参考[ContentType使用场景说明](../harmonyos-guides/scenario-fusion-intelligentfilling-appendix.md)。
* [TextInput](../harmonyos-references/ts-basic-components-textinput.md)组件是单行文本输入框组件，该组件可通过[enableAutoFill](../harmonyos-references/ts-basic-components-textinput.md#enableautofill11)设置是否启用自动填充，组件默认启用自动填充。

## 问题定位

输入组件（即TextInput、TextArea等输入组件）会解析placeholder得到相关字段触发智能填充，当前TextInput的placeholder属性存在关键字'名'会产生联想填充，导致气泡无法弹出。

## 分析结论

配置了TextInput组件的placeholder属性会触发智能填充，与自定义的bindPopup冲突了，导致bindPopup被关闭，无法显示。

## 修改建议

TextInput组件设置enableAutoFill属性值为false，禁用自动填充。

```ts
@Entry
@Component
struct CustomPopup {
  @State message: string = '';
  @State customPopup: boolean = false;

  @Builder
  popupBuilder() {
    Row({ space: 2 }) {
      Image($r('app.media.startIcon')).width(24).height(24)
      Text('Custom Popup').fontSize(10);
    }.width(110).height(50).padding(10).backgroundColor('#ffffff')
  }

  build() {
    Column() {
      TextInput({ text: this.message, placeholder: '请输入服务器标识/IP/域名' })
        .margin({
          top: 50
        })
        .enableAutoFill(false) // 属性值为false，禁用自动填充。
        .bindPopup(this.customPopup, {
          builder: this.popupBuilder,
          placement: Placement.Top,
          mask: false,
          popupColor: Color.Yellow,
          enableArrow: true,
          showInSubWindow: false,
          onStateChange: (e) => {
            if (!e.isVisible) {
              this.customPopup = false;
            }
          }
        })
        .onChange((value: string) => {
          if (value === '') {
            this.customPopup = true;
          } else {
            this.customPopup = false;
          }
        })
        .onEditChange((isEditing: boolean) => {
          if (isEditing) {
            this.customPopup = true;
          }
        })
    }
    .padding({ left: 16, right: 16 })
    .width('100%')
    .height('100%')
  }
}
```
