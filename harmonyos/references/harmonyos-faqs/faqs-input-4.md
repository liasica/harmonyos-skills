---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-input-4
title: 鼠标指针在文字部分一直是手指点击状态
breadcrumb: FAQ > 系统开发 > 基础功能 > 多模输入（Input） > 鼠标指针在文字部分一直是手指点击状态
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:40+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c21236af6afcd2233d63dd70553118555ac531d0d51ea9b3051ebcc98df5fd22
---

## 问题现象

鼠标悬浮页面文字上，鼠标指针一直是手指点击状态。

## 背景知识

* [Pointer](../harmonyos-guides/pointerstyle-guidelines.md)：鼠标光标控制提供鼠标光标显示和隐藏、光标样式查询和设置的能力。
* [pointer.setPointerStyle](../harmonyos-references/js-apis-pointer.md#pointersetpointerstyle)：通过setPointerStyle接口可以设置鼠标样式类型。
* [悬浮事件](../harmonyos-references/ts-universal-events-hover.md)：光标滑动或手写笔在屏幕上悬浮移动扫过组件时触发。

## 问题定位

排查应用是否使用了[pointer.setPointerStyle](../harmonyos-references/js-apis-pointer.md#pointersetpointerstyle)接口设置了鼠标在悬浮文字上的光标的样式为HAND\_POINTING。

## 分析结论

应用通过[pointer.setPointerStyle](../harmonyos-references/js-apis-pointer.md#pointersetpointerstyle)接口设置了鼠标在悬浮文字上的光标的样式为HAND\_POINTING。

## 修改建议

通过在文本组件的[onHover](../harmonyos-references/ts-universal-events-hover.md#onhover)回调函数中使用[pointer.setPointerStyle](../harmonyos-references/js-apis-pointer.md#pointersetpointerstyle)接口将鼠标悬浮文字上的[光标样式](../harmonyos-references/js-apis-pointer.md#pointerstyle)修改为默认。

```ts
import { pointer } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    Column() {
      Text('鼠标悬浮文字上的样式')
        .onHover(() => {
          window.getLastWindow(this.getUIContext().getHostContext(), (error: BusinessError, win: window.Window) => {
            if (error.code) {
              console.error('Failed to obtain the top window. Cause: ' + JSON.stringify(error));
              return;
            }
            let windowId = win.getWindowProperties().id;
            if (windowId < 0) {
              console.info(`Invalid windowId`);
              return;
            }
            try {
              pointer.setPointerStyle(windowId, pointer.PointerStyle.DEFAULT, () => {
                console.info(`Set pointer style success`);
              });
            } catch (error) {
              console.error(`Set pointer style failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
            }
          });
        });
    }.justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Center)
    .width('100%')
    .height('100%');
  }
}
```
