---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-772
title: Text绑定自定义菜单
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Text绑定自定义菜单
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:03+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:013b39a762d18eee9e555416e6837d0ea0403059d5ee1ff03e301393faf8cb4c
---

## 问题现象

Text组件绑定自定义菜单如何实现以下效果：

* bindSelectionMenu展示的菜单在用户触碰屏幕时自动消失。
* 长按出现自定义菜单，双击手势不出现默认菜单。

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/VycHdmELR7S69-C6mIMM5g/zh-cn_image_0000002658795071.png "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/UHS5Z8rQQmCU0mIpMR0CSw/zh-cn_image_0000002628555700.png "点击放大")

## 背景知识

* [绑定手势方法](../harmonyos-references/ts-gesture-settings.md)为组件绑定不同类型的手势事件，并设置事件的响应方法。
* [bindSelectionMenu](../harmonyos-references/ts-basic-components-text.md#bindselectionmenu11)方法能设置Text自定义选择菜单，使用方法可参考[文本绑定自定义菜单](../harmonyos-references/ts-basic-components-text.md#示例8文本绑定自定义菜单)。

## 解决方案

* 在页面最外层组件添加点击事件，关闭菜单，实现触摸屏幕菜单消失的效果。
* 双击手势出现默认菜单是系统默认规格，可以为Text组件绑定双击事件覆盖默认行为。

```ts
@Entry
@Component
struct BindMenuPage {
  controller: TextController = new TextController();

  build() {
    Column() {
      Text(undefined, { controller: this.controller }) {
        Span('Hello World');
        ImageSpan($r('app.media.startIcon')) // 图片资源需自行替换
          .width('100px').height('100px');
      }
      .parallelGesture(
        // 重写双击手势事件，关闭菜单
        TapGesture({ count: 2 })
          .onAction(() => {
            this.controller.closeSelectionMenu();
          }), GestureMask.Normal)
      .copyOption(CopyOptions.InApp)
      // 设置TextResponseType.LONG_PRESS，可以通过长按方式弹出自定义菜单
      .bindSelectionMenu(TextSpanType.DEFAULT, this.LongPressImageCustomMenu, TextResponseType.LONG_PRESS);
    }.width('100%').height('100%')
    .justifyContent(FlexAlign.Center)
    .onClick(() => {
      // 在页面根节点设置点击事件，关闭菜单
      this.controller.closeSelectionMenu(); // 关闭菜单
    });
  }

  @Builder
  LongPressImageCustomMenu() {
    Column() {
      Menu() {
        MenuItemGroup() {
          // 图片资源需自行替换
          MenuItem({ startIcon: $r('app.media.startIcon'), content: 'Long Press Image Menu 1', labelInfo: '' });
          MenuItem({ startIcon: $r('app.media.startIcon'), content: 'Long Press Image Menu 2', labelInfo: '' });
          MenuItem({ startIcon: $r('app.media.startIcon'), content: 'Long Press Image Menu 3', labelInfo: '' });
        };
      }
      .backgroundColor('#F0F0F0');
    };
  }
}
```
