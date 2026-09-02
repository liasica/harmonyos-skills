---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pointerstyle-guidelines
title: 鼠标光标开发指导
breadcrumb: 指南 > 系统 > 基础功能 > Input Kit（多模输入服务） > 鼠标光标开发指导
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:36+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0e22faf12009c2318c590f981a8d0405a60c62ba682ded3bc955f7ea9eca41f9
---

## 场景介绍

鼠标光标控制提供鼠标光标显示和隐藏、光标样式查询和设置的能力。使用场景例如：用户在全屏观看视频时，开发者可以控制鼠标光标的显示隐藏；当用户执行取色时，开发者可以将鼠标光标样式切换为取色器样式。

## 导入模块

```js
import { pointer } from '@kit.InputKit';
```

## 接口说明

鼠标光标控制常用接口如下表所示，接口详细介绍请参见[@ohos.multimodalInput.pointer (鼠标光标)](../harmonyos-references/js-apis-pointer.md)。

| 接口名称 | 描述 |
| --- | --- |
| isPointerVisible(callback: AsyncCallback<boolean>): void | 获取鼠标光标显示或隐藏状态。 |
| setPointerVisible(visible: boolean, callback: AsyncCallback<void>): void | 设置鼠标光标显示或隐藏状态，该接口会影响全局鼠标光标的显示状态。 |
| setPointerStyle(windowId: number, pointerStyle: PointerStyle, callback: AsyncCallback<void>): void | 设置鼠标光标样式，该接口会影响指定窗口鼠标光标样式。 |
| getPointerStyle(windowId: number, callback: AsyncCallback<PointerStyle>): void | 查询鼠标光标样式。 |

## 设置鼠标光标隐藏

用户在全屏观看视频时，可以调用鼠标光标的隐藏接口设置鼠标光标不可见，提升用户体验。

### 开发步骤

1. 应用切换到全屏播放。
2. 在应用中调用鼠标光标隐藏接口隐藏光标。
3. 应用退出全屏播放。
4. 在应用中调用鼠标光标显示接口显示光标。

```typescript
Text("Click to hide pointer")
  .onClick(() => {
    // 1.应用切换到全屏播放
    // 2.调用鼠标光标隐藏接口隐藏光标
    try {
      pointer.setPointerVisible(false, (error: Error) => {
        if (error) {
          hilog.error(DOMAIN, 'Pointer', `Set pointer visible failed, error: %{public}s`,
            JSON.stringify(error, ["code", "message"]));
          return;
        }
        hilog.info(DOMAIN, 'Pointer', 'Set pointer visible success.');
      });
    } catch (error) {
      hilog.error(DOMAIN, 'Pointer', `The mouse pointer hide attributes is failed. %{public}s`,
        JSON.stringify(error, ["code", "message"]));
    }
  })
  // ...

// 3.应用退出全屏播放
// 4.调用鼠标光标显示接口显示光标
Text("Click to display pointer")
  .onClick(() => {
    try {
      pointer.setPointerVisible(true, (error: Error) => {
        if (error) {
          hilog.error(DOMAIN, 'Pointer', `Set pointer visible failed, error: %{public}s`,
            JSON.stringify(error, ["code", "message"]));
          return;
        }
        hilog.info(DOMAIN, 'Pointer', 'Set pointer visible success.');
      });
    } catch (error) {
      hilog.error(DOMAIN, 'Pointer', `Set pointer visible failed, error: %{public}s`,
        JSON.stringify(error, ["code", "message"]));
    }
  })
  // ...
```

## 设置鼠标光标样式

当开发者设计取色器特性时，可以将鼠标光标样式切换为取色器样式，完成取色后，设置鼠标光标样式为默认样式，该接口设置和查询当前应用内指定窗口的光标样式，总共可设置49种光标样式，具体参考[PointerStyle](../harmonyos-references/js-apis-pointer.md#pointerstyle)。

### 开发步骤

1. 开发者使能取色功能。
2. 调用窗口实例获取对应的窗口ID。
3. 设置鼠标光标样式为取色器样式。
4. 取色结束。
5. 设置鼠标光标样式为默认样式。

```typescript
Text(`Click to set the mouse pointer style to the color picker style`)
  .onClick(() => {
    // 1.开发者使能取色功能
    // 2.调用窗口实例获取对应的窗口id
    window.getLastWindow(this.getUIContext().getHostContext(),
      (error: BusinessError, windowClass: window.Window) => {
        if (error.code) {
          hilog.error(DOMAIN, 'Pointer', 'Failed to obtain the top window. Cause: %{public}s',
            JSON.stringify(error));
          return;
        }
        let windowId = windowClass.getWindowProperties().id;
        if (windowId < 0) {
          hilog.info(DOMAIN, 'Pointer', 'Invalid windowId');
          return;
        }
        try {
          // 3.设置鼠标光标样式为取色器样式
          pointer.setPointerStyle(windowId, pointer.PointerStyle.COLOR_SUCKER).then(() => {
            hilog.info(DOMAIN, 'Pointer', 'Successfully set mouse pointer style');
          });
        } catch (error) {
          hilog.error(DOMAIN, 'Pointer', `Failed to set the pointer style, error=%{public}s, msg=%{public}s`,
            JSON.stringify(error), error.message);
        }
      });
  })
  // ...

Text(`Click to set the mouse pointer style to default style`)
  .onClick(() => {
    // 4.取色结束
    window.getLastWindow(this.getUIContext().getHostContext(),
      (error: BusinessError, windowClass: window.Window) => {
        if (error.code) {
          hilog.error(DOMAIN, 'Pointer', 'Failed to obtain the top window. Cause: %{public}s',
            JSON.stringify(error));
          return;
        }
        let windowId = windowClass.getWindowProperties().id;
        if (windowId < 0) {
          hilog.info(DOMAIN, 'Pointer', 'Invalid windowId');
          return;
        }
        try {
          // 5.设置鼠标光标样式为默认样式
          pointer.setPointerStyle(windowId, pointer.PointerStyle.DEFAULT).then(() => {
            hilog.info(DOMAIN, 'Pointer', 'Successfully set mouse pointer style');
          });
        } catch (error) {
          hilog.error(DOMAIN, 'Pointer', `Failed to set the pointer style, error=%{public}s, msg=%{public}s`,
            JSON.stringify(error), error.message);
        }
      });
  })
```
