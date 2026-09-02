---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1002
title: ActionSheet如何设置item样式
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > ActionSheet如何设置item样式
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:25+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b3af690f0b59de522c968de6b99f0e63ffe3b80111b8910cfdd6aaef3b427fa1
---

## 问题现象

ActionSheet默认的item样式间距过小，不便于交互，如何设置item样式？

```ts
@Entry
@Component
struct ShowActionSheetExample {
  build() {
    Column() {
      Button('showActionSheet')
        .margin(30)
        .onClick(() => {
          this.getUIContext().showActionSheet({
            title: 'ActionSheet title',
            message: 'message',
            autoCancel: false,
            width: 300,
            height: 300,
            cornerRadius: 20,
            borderWidth: 1,
            borderStyle: BorderStyle.Solid,
            borderColor: Color.Blue,
            backgroundColor: Color.White,
            transition: TransitionEffect.asymmetric(TransitionEffect.OPACITY
              .animation({ duration: 3000, curve: Curve.Sharp })
              .combine(TransitionEffect.scale({ x: 1.5, y: 1.5 }).animation({ duration: 3000, curve: Curve.Sharp })),
              TransitionEffect.OPACITY.animation({ duration: 100, curve: Curve.Smooth })
                .combine(TransitionEffect.scale({ x: 0.5, y: 0.5 }).animation({ duration: 100, curve: Curve.Smooth }))),
            confirm: {
              value: 'Confirm button',
              action: () => {
                console.info('Get Alert Dialog handled');
              }
            },
            alignment: DialogAlignment.Center,
            sheets: [
              {
                title: 'apples',
                action: () => {
                  console.info('apples');
                }
              },
              {
                title: 'bananas',
                action: () => {
                  console.info('bananas');
                }
              },
              {
                title: 'pears',
                action: () => {
                  console.info('pears');
                }
              }
            ]
          });
        })
    }.width('100%').margin({ top: 5 })
  }
}
```

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/9EIIahzkREC1mOkXjSEBDg/zh-cn_image_0000002658804039.png "点击放大")

## 背景知识

* [列表选择器弹窗](../harmonyos-references/ts-methods-action-sheet.md)适用于呈现多个操作选项，尤其当界面中仅需展示操作列表而无其他内容时适用这种方案。
* 列表选择器弹窗通过UIContext中的[showActionSheet](../harmonyos-references/arkts-apis-uicontext-uicontext.md#showactionsheet)接口实现，可以通过修改配置width、height、transition等接口来自定义弹窗样式及弹出效果。

## 解决方案

ActionSheet的item之间的间距过小，可以给ActionSheet每个item的title添加换行符来实现，具体可参考如下代码：

```ts
@Entry
@Component
struct ShowActionSheetExample {
  build() {
    RelativeContainer() {
      Button('showActionSheet')
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .margin(30)
        .onClick(() => {
          this.getUIContext().showActionSheet({
            title: '水果列表',
            message: '以下为有货的水果',
            autoCancel: false,
            width: 300,
            height: 300,
            cornerRadius: 20,
            backgroundColor: Color.White,
            confirm: {
              value: '确认',
              action: () => {
                console.info('Get Alert Dialog handled');
              }
            },
            alignment: DialogAlignment.Center,
            sheets: [
              {
                title: '\napples\n',
                action: () => {
                  console.info('apples');
                }
              },
              {
                title: '\nbananas\n',
                action: () => {
                  console.info('bananas');
                }
              },
              {
                title: '\npears\n',
                action: () => {
                  console.info('pears');
                }
              }
            ]
          });
        });
    }.width('100%').margin({ top: 5 });
  }
}
```
