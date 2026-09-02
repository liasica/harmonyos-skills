---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1312
title: 如何自定义bindPopup的交互式关闭功能
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何自定义bindPopup的交互式关闭功能
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:08+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:65bdb19d9ed4b1feb7ecd2105dfa3771899278be5d1982910685caba8b3ba086
---

## 问题现象

* 场景一：如何设置bindPopup的参数实现点击弹窗外部关闭弹窗？
* 场景二：bindPopup如何拦截系统返回事件，自定义返回逻辑？

## 背景知识

* [onWillDismiss](../harmonyos-references/js-apis-promptaction.md#basedialogoptions11)：交互式关闭回调函数。
* [bindPopup](../harmonyos-references/ts-universal-attributes-popup.md#bindpopup)：为组件绑定Popup气泡，API介绍请参考：[Popup控制](../harmonyos-references/ts-universal-attributes-popup.md)。
* bindPopup方法的传参[PopupOptions](../harmonyos-references/ts-universal-attributes-popup.md#popupoptions类型说明)中，autoCancel可以控制气泡是否关闭，默认值为true。该参数表示：页面有操作时，是否自动关闭气泡。
* [气泡提示（Popup）](../harmonyos-guides/arkts-popup-and-menu-components-popup.md)：Popup属性可绑定在组件上显示气泡弹窗提示，设置弹窗内容、交互逻辑和显示状态。主要用于屏幕录制、信息弹出提醒等显示状态。

## 解决方案

* **场景一**：将组件bindPopup方法的传参[PopupOptions](../harmonyos-references/ts-universal-attributes-popup.md#popupoptions类型说明)中的autoCancel设置为true，即可实现点击外部自动关闭气泡。
* **场景二**：可以使用onWillDismiss事件拦截气泡返回关闭，自定义返回事件逻辑。

  ```ts
  @Entry
  @Component
  struct SFI20250721204737765691 {
    @State handlePopup1: boolean = false;
    @State handlePopup2: boolean = false;
    @State str: string = '使用onWillDismiss事件拦截气泡返回关闭';

    build() {
      Column() {
        Button('Button1')
          .onClick(() => {
            this.handlePopup1 = true;
            this.str = '使用onWillDismiss事件拦截气泡返回关闭';
          })
          .bindPopup(this.handlePopup1, {
            message: this.str,
            messageOptions: {
              textColor: Color.Black,
              font: {
                size: '20vp',
                style: FontStyle.Normal
              }
            },
            placement: Placement.Bottom,
            enableArrow: false,
            targetSpace: '15vp',
            onStateChange: (e) => {
              let timer = setTimeout(() => {
                this.handlePopup1 = false;
              }, 10000);
              if (!e.isVisible) {
                this.handlePopup1 = false;
                clearTimeout(timer);
              }
            },
            onWillDismiss: (
              (dismissPopupAction: DismissPopupAction) => {
                console.info('dismissReason:' + JSON.stringify(dismissPopupAction.reason));
                if (dismissPopupAction.reason === DismissReason.PRESS_BACK) {
                  // 自定义返回事件逻辑
                  this.str = '自定义返回事件，执行成功。';
                }
                if (dismissPopupAction.reason === DismissReason.TOUCH_OUTSIDE) {
                  dismissPopupAction.dismiss();
                }
              }
            )
          })
          .margin(50);

        Button('Button2')
          .onClick(() => {
            this.handlePopup2 = true;
          })
          .bindPopup(this.handlePopup2, {
            message: '未拦截气泡返回关闭',
            messageOptions: {
              textColor: Color.Black,
              font: {
                size: '20vp',
                style: FontStyle.Normal
              }
            },
            placement: Placement.Bottom,
            enableArrow: false,
            targetSpace: '15vp',
            onStateChange: (e) => {
              let timer = setTimeout(() => {
                this.handlePopup2 = false;
              }, 10000);
              if (!e.isVisible) {
                this.handlePopup2 = false;
                clearTimeout(timer);
              }
            }
          })
          .margin(50);
      }
      .width('100%');
    }
  }
  ```

## 常见FAQ

Q：如何拦截气泡的退出事件？

A：通过配置onWillDismiss的boolean类型为false时，[拦截气泡的退出事件](../harmonyos-references/ts-universal-attributes-popup.md#示例6为气泡拦截退出事件)。
