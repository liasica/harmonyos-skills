---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-955
title: 如何实现PC悬浮弹出提示框功能
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何实现PC悬浮弹出提示框功能
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:05+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:317e93097b5e7f045c4852ca05f1cfedf4e9c252b0dc784c99b729330c8c1c10
---

## 问题现象

在开发PC应用时，要实现鼠标经过某个元素时弹出提示框（通常称为“工具提示”或“悬浮提示”）。具体的应用场景为：需要对表格的表头、表单的标签进行自定义，添加问号的悬浮提示。

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/ifKqpIC0RbW6N6_z4NksfA/zh-cn_image_0000002658920479.png "点击放大")

## 背景知识

* [Tips控制](../harmonyos-references/ts-universal-attributes-tips.md)为组件绑定Tips悬浮气泡，当鼠标悬浮在组件上时，自动显示提示信息；鼠标离开组件时，悬浮气泡自动隐藏。
* [onHover](../harmonyos-references/ts-universal-events-hover.md#onhover)当光标滑动或手写笔在屏幕上悬浮移动扫过组件时触发。
* [Popup控制](../harmonyos-references/ts-universal-attributes-popup.md)为组件绑定Popup气泡，并设置气泡内容，交互逻辑和显示状态。

## 解决方案

* **方案一**：通过将Tips悬浮气泡绑定到组件上，自动实现提示信息的显示与隐藏功能。

  ```ts
  @Entry
  @Component
  struct HoverPopup1 {
    str: string = 'Tips:自定义提示';

    build() {
      Row() {
        Text('表头名')
          .fontSize(30);
        Image($r('app.media.startIcon'))
          .width(30)
          .bindTips(this.str, {
            // 设置悬浮气泡的显示时延
            appearingTime: 10,
            // 设置悬浮气泡的隐藏时延
            disappearingTime: 300,
            appearingTimeWithContinuousOperation: 300,
            disappearingTimeWithContinuousOperation: 0,
            // 设置是否显示气泡箭头。值为true时，显示箭头；值为false时，不显示箭头
            enableArrow: true,
          });
      }
      .justifyContent(FlexAlign.Center)
      .height('100%')
      .width('100%');
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/xQ81SUgzTs26pcdE82FLBg/zh-cn_image_0000002628401266.png "点击放大")
* **方案二**：为图片组件绑定onHover悬浮事件监听与Popup控制气泡。当检测到有鼠标进入时，通过修改控制显示的状态变量来弹出气泡。

  ```ts
  @Entry
  @Component
  struct HoverPopup2 {
    str: string = 'Tips:自定义提示';
    @State handlePopup: boolean = false;

    build() {
      Row() {
        Text('表头名')
          .fontSize(30);
        Image($r('app.media.startIcon'))
          .width(30)
          .onHover((isHover: boolean, event: HoverEvent) => {
            console.info(`${event}`);
            if (isHover) {
              // 鼠标悬浮
              this.handlePopup = true;
            }
          })
          .bindPopup($$this.handlePopup, {
            message: this.str,
            autoCancel: true,
            enableArrow: true,
            onStateChange: (e) => {
              if (!e.isVisible) {
                this.handlePopup = false;
              }
            }
          });
      }
      .justifyContent(FlexAlign.Center)
      .height('100%')
      .width('100%');
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/TFsfp0CoRBGPjiDJPn7lEw/zh-cn_image_0000002658800525.png "点击放大")

## 常见FAQ

Q：使用onHover悬浮事件监听与Popup控制气泡的方案，为什么onHover仅监听悬浮，当离开时为什么不能直接修改控制展示的状态变量？

A：如果加入悬浮离开的逻辑，当气泡弹出时会出现鼠标悬浮事件离开，即立刻执行关闭气泡的逻辑，这便会造成气泡闪烁的现象。
