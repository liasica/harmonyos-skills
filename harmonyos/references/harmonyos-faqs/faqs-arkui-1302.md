---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1302
title: 如何监听软键盘的弹出和收起事件
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 如何监听软键盘的弹出和收起事件
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:14+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:c16d8a8b810772cf816943893d62c6d14cd3aaf1154acc78b4606829549823f7
---

## 问题现象

如何监听软键盘的弹出和收起事件，on('keyboardShow')没有效果？

## 背景知识

* [on('keyboardHeightChange')](../harmonyos-references/arkts-apis-window-window.md#onkeyboardheightchange7)：开启固定态软键盘高度变化的监听。
* [焦点事件](../harmonyos-references/ts-universal-focus-event.md)：页面焦点在可获焦组件间移动时触发的事件，组件可使用焦点事件来处理相关逻辑。
* [on('avoidAreaChange')](../harmonyos-references/arkts-apis-window-window.md#onavoidareachange9)：开启当前应用窗口系统规避区变化的监听，包括软键盘区域的监听。
* [on('keyboardShow'|'keyboardHide')](../harmonyos-references/js-apis-inputmethodengine.md#onkeyboardshowkeyboardhide9)：订阅输入法软键盘显示或隐藏事件。

## 解决方案

当前非输入法应用不提供直接监听软键盘的弹出和收起，可通过监听键盘高度变化、监听窗口的系统规避区域变化或通过使用输入框的焦点事件等方式来间接监听软键盘的弹出和收起。

输入法应用可通过on('keyboardShow'|'keyboardHide')接口订阅输入法软键盘显示或隐藏事件。

* 监听键盘高度变化：通过window.on('keyboardHeightChange')事件可以监听键盘的高度变化。当键盘弹出时，返回的高度值为非零值；当键盘收起时，返回的高度值为0。示例代码如下：

  ```ts
  currentWindow.on('keyboardHeightChange', (data) => {
    if (data > 0) {
      console.info('键盘高度大于0，键盘已弹出');
    } else {
      console.info('键盘高度为0，键盘已收起');
    }
  });
  ```
* 使用输入框的焦点事件：通过TextInput组件的onFocus和onBlur事件可以间接判断键盘的弹出和收起。当输入框获得焦点时，通常会触发键盘弹出；当输入框失去焦点时，键盘会收起。示例代码如下：

  ```ts
  TextInput({ placeholder: '请输入' })
    .width(350)
    .onFocus(() => {
      console.info('输入框获焦，键盘已弹出');
    })
    .onBlur(() => {
      console.info('输入框失焦，键盘已收起');
    });
  ```
* 监听窗口的系统规避区域变化：通过监听窗口的avoidAreaChange事件，可以获取键盘高度的变化。当键盘弹出时，系统规避区域的高度会变化。示例代码如下：

  ```ts
  currentWindow.on('avoidAreaChange', data => {
    if (data.type === window.AvoidAreaType.TYPE_KEYBOARD) {
      if (data.area.bottomRect.height > 0) {
        console.info('底部规避区高度大于0，键盘已弹出');
      } else {
        console.info('底部规避区高度为0，键盘已收起');
      }
    }
  });
  ```
* 使用on('keyboardShow'|'keyboardHide')接口订阅输入法软键盘显示或隐藏事件（**仅支持输入法应用调用**），用法可参考官方[示例](../harmonyos-references/js-apis-inputmethodengine.md#onkeyboardshowkeyboardhide9)。

完整示例参考如下：

```ts
import { window } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  aboutToAppear(): void {
    window.getLastWindow(this.getUIContext().getHostContext()).then(currentWindow => {
      currentWindow.on('keyboardHeightChange', (data) => {
        if (data > 0) {
          console.info('键盘高度大于0，键盘已弹出');
        } else {
          console.info('键盘高度为0，键盘已收起');
        }
      });
      currentWindow.on('avoidAreaChange', data => {
        if (data.type === window.AvoidAreaType.TYPE_KEYBOARD) {
          if (data.area.bottomRect.height > 0) {
            console.info('底部规避区高度大于0，键盘已弹出');
          } else {
            console.info('底部规避区高度为0，键盘已收起');
          }
        }
      });
    });
  }

  build() {
    Column() {
      TextInput({ placeholder: '请输入' })
        .width(350)
        .onFocus(() => {
          console.info('输入框获焦，键盘已弹出');
        })
        .onBlur(() => {
          console.info('输入框失焦，键盘已收起');
        });
    };
  }
}
```
