---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkui-uimana-faq-0013
title: 如何控制窗口旋转方向
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 常见问题 > 如何控制窗口旋转方向
category: harmonyos-faqs
scraped_at: 2026-10-21T07:11:10+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:a81cd5e06139f0f0bf783bc91e25cb72c964e58f5342bfaddc549ebda1a7b11c
---

**Q：如何监听当前屏幕的横竖屏状态？如何实现页面跟随屏幕横竖屏自动旋转？**

A：应用可以使用 display.on 监听屏幕状态的变化。

页面跟随屏幕旋转的方法如下：

1. Ability级别配置：在模块配置文件module.json5中配置abilities的orientation属性"。
2. 动态设置窗口方向：使用 window.setPreferredOrientation。

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

参考链接：[display.on](../harmonyos-references/js-apis-display.md#displayonaddremovechange)、[设置窗口的显示方向属性](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9)。

**Q：如何锁定设备竖屏，使得窗口不随屏幕旋转？**

A：使用setPreferredOrientation方法锁定竖屏，设置orientation为window.Orientation.PORTRAIT。参考代码如下：

```ts
//1.Get the window instance object, use the createWindow method to create a new window, and use the findWindow method to obtain an existing window
let windowClass: window.Window | undefined = undefined;
let config: window.Configuration = {
  name: "alertWindow",
  windowType: window.WindowType.TYPE_SYSTEM_ALERT,
  ctx: this.context
};
try {
  let promise = window.createWindow(config);
  promise.then((data)=> {
    windowClass = data;
    console.info('Succeeded in creating the window. Data:' + JSON.stringify(data));
  }).catch((err: BusinessError)=>{
    console.error('Failed to create the Window. Cause:' + JSON.stringify(err));
  });} catch (exception) {
  console.error('Failed to create the window. Cause: ' + JSON.stringify(exception));
}
//2.The window instance uses the setPreferred Orientation method to set the display orientation of the window. PORTRAIT is a fixed vertical screen, and other orientations can refer to the reference link
let orientation = window.Orientation.PORTRAIT;
try {
  let windowClass: window.Window = window.findWindow("test");
  windowClass.setPreferredOrientation(orientation, (err: BusinessError) => {
    const errCode: number = err.code;
    if (errCode) {
      console.error('Failed to set window orientation. Cause: ' + JSON.stringify(err));
      return;
    }
    console.info('Succeeded in setting window orientation.');
  });
} catch (exception) {
  console.error('Failed to set window orientation. Cause: ' + JSON.stringify(exception));
}
```

参考链接：[Orientation](../harmonyos-references/js-apis-display.md#orientation10)。
