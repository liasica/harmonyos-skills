---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-34
title: 如何监听当前屏幕的横竖屏状态？如何实现页面跟随屏幕横竖屏自动旋转
breadcrumb: FAQ > 应用框架开发 > UI框架 > 屏幕管理 > 如何监听当前屏幕的横竖屏状态？如何实现页面跟随屏幕横竖屏自动旋转
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:12+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:572ac40fd4828a38aad40c022cf129b81e72d7ffe69f9c8bdf53129e51c274ab
---

应用可以使用 display.on 监听屏幕状态的变化。

页面跟随屏幕旋转的方法如下：

1、Ability级别配置：在模块配置文件module.json5中配置abilities的orientation属性"。

2、动态设置窗口方向：使用 window.setPreferredOrientation。

```ts
import { window, display } from '@kit.ArkUI';

const TAG = 'ScreenTest'
const ORIENTATION: Array<string> = ['Portrait', 'Landscape', 'Reverse Portrait', 'Reverse Landscape']

@Entry
@Component
struct ScreenTest {
  context = this.getUIContext();
  @State rotation: number = 0
  @State message: string = ORIENTATION[this.rotation]

  aboutToAppear() {
    this.setOrientation()

    let callback = async () => {
      // ...
    }
    try {
      display.on("change", callback); // Listen for screen state changes
    } catch (exception) {
      console.error(TAG, 'Failed to register callback. Code: ' + JSON.stringify(exception));
    }
  }

  setOrientation() {
    try {
      window.getLastWindow(this.context.getHostContext(), (err, data) => { // 获取window实例
        if (err.code) {
          console.error(TAG, 'Failed to obtain the top window. Cause: ' + JSON.stringify(err));
          return;
        }
        let windowClass = data;
        console.info(TAG, 'Succeeded in obtaining the top window. Data: ' + JSON.stringify(data));

        let orientation = window.Orientation.AUTO_ROTATION; // 设置窗口方向为传感器自动旋转模式。
        try {
          windowClass.setPreferredOrientation(orientation, (err) => {
            if (err.code) {
              console.error(TAG, 'Failed to set window orientation. Cause: ' + JSON.stringify(err));
              return;
            }
            console.info(TAG, 'Succeeded in setting window orientation.');
          });
        } catch (exception) {
          console.error(TAG, 'Failed to set window orientation. Cause: ' + JSON.stringify(exception));
        }
        ;
      });
    } catch (exception) {
      console.error(TAG, 'Failed to obtain the top window. Cause: ' + JSON.stringify(exception));
    }
    ;
  }

  build() {
    Row() {
      Column() {
        Text(`${this.rotation}`).fontSize(25)
        Text(`${this.message}`).fontSize(25)
      }
      .width("100%")
    }
    .height("100%")
  }
}
```

**参考链接**

[display.on](../harmonyos-references/js-apis-display.md#displayonaddremovechange)、[设置窗口的显示方向属性](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9)
