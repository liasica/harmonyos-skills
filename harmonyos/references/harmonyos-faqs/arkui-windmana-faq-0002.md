---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkui-windmana-faq-0002
title: 软键盘事件监听与避让模式设置常见问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 常见问题 > 软键盘事件监听与避让模式设置常见问题
category: harmonyos-faqs
scraped_at: 2026-10-15T07:14:27+08:00
doc_updated_at: 2026-10-14
content_hash: sha256:69046be8ca6ad52ca3bdbf9e8e9bdfee19dea10beed9452720936ff955889609
---

**Q：如何监听软键盘的弹出和收起事件，on('keyboardShow')没有效果？**

**A**：当前非输入法应用不提供直接监听软键盘的弹出和收起，可通过监听键盘高度变化、监听窗口的系统规避区域变化或通过使用输入框的焦点事件等方式来间接监听软键盘的弹出和收起。输入法应用可通过on('keyboardShow'|'keyboardHide')接口订阅输入法软键盘显示或隐藏事件。

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

* 使用on('keyboardShow'|'keyboardHide')接口订阅输入法软键盘显示或隐藏事件（仅支持输入法应用调用），用法可参考官方[示例](../harmonyos-references/js-apis-inputmethodengine.md#onkeyboardshowkeyboardhide9)。

示例完整代码如下：

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

**Q：如何在键盘弹出时，让内容上移，而不是整个页面上移？**

**A**：可通过setKeyboardAvoidMode接口设置键盘避让模式为KeyboardAvoidMode.RESIZE，表示压缩模式。参考代码如下：

```ts
// EntryAbility.ets
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window, KeyboardAvoidMode, UIContext } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
  }

  onDestroy(): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onDestroy');
  }
  onWindowStageCreate(windowStage: window.WindowStage) {
    // Main window is created, set main page for this ability
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

    windowStage.loadContent('pages/Index', (err, data) => {
      let uiContext :UIContext = windowStage.getMainWindowSync().getUIContext();
      uiContext.setKeyboardAvoidMode(KeyboardAvoidMode.RESIZE);
      if (err.code) {
        hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
        return;
      }
      hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
    });
  }

  onWindowStageDestroy(): void {
    // Main window is destroyed, release UI related resources
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
  }

  onForeground(): void {
    // Ability has brought to foreground
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onForeground');
  }

  onBackground(): void {
    // Ability has back to background
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onBackground');
  }
}
```

参考链接：[setKeyboardAvoidMode](../harmonyos-references/arkts-apis-uicontext-uicontext.md#setkeyboardavoidmode11)。
