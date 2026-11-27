---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkui-uimana-faq-0013
title: 横竖屏旋转锁定与设备适配常见问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 常见问题 > 横竖屏旋转锁定与设备适配常见问题
category: harmonyos-faqs
scraped_at: 2026-11-27T10:50:45+08:00
doc_updated_at: 2026-11-26
content_hash: sha256:efa6918b219bb7ac96661f7793e165fb390db19f7f79317d2edaa7ef8ef167b6
---

**Q：如何监听当前屏幕的横竖屏状态？如何实现页面跟随屏幕横竖屏自动旋转？**

**A：**应用可以使用 display.on 监听屏幕状态的变化。

页面跟随屏幕旋转的方法如下：

1、Ability级别配置：在模块配置文件module.json5中配置abilities的orientation属性。

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

参考链接：[display.on](../doccenter-references/api/js-apis-display.md#displayonadd--remove--change)、[设置窗口的显示方向属性](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9)。

**Q：如何锁定设备竖屏，使得窗口不随屏幕旋转？**

**A：**使用setPreferredOrientation方法锁定竖屏，设置orientation为window.Orientation.PORTRAIT。参考代码如下：

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

**Q：如何根据获取的设备类型判断是平板还是手机？如果是平板强制屏幕横屏展示不跟随系统进行竖屏切换，如果是手机强制屏幕竖屏展示不跟随系统进行横屏切换。**

A：可以通过@ohos.deviceInfo接口的deviceType属性来获取设备类型，具体请参考[设备类型枚举](../harmonyos-references/js-apis-device-info.md#devicetypes20)。再通过setPreferredOrientation来设置主窗口的显示方向属性，其中参数Orientation为窗口显示方向类型枚举。代码示例如下：

```ts
import { ConfigurationConstant, UIAbility } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { deviceInfo } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

const DOMAIN = 0x0000;

export default class EntryAbility extends UIAbility {
  onCreate(): void {
    try {
      this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
    } catch (err) {
      hilog.error(DOMAIN, 'testTag', 'Failed to set colorMode. Cause: %{public}s', JSON.stringify(err));
    }
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
  }

  onDestroy(): void {
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    let windowClass: window.Window | undefined = undefined;
    windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        hilog.error(DOMAIN, 'testTag', 'Failed to obtain the main window. Cause: %{public}s', JSON.stringify(err));
        return;
      }
      windowClass = data;
      // 获取设备类型
      let deviceTypeInfo: string = deviceInfo.deviceType;
      hilog.info(DOMAIN, 'testTag', 'the value of the deviceType is:', JSON.stringify(deviceTypeInfo));
      let orientation = window.Orientation.AUTO_ROTATION;
      // 判断设备是手机or平板，来设置窗口显示方向
      if (deviceTypeInfo == 'phone') {
        orientation = window.Orientation.PORTRAIT;
      } else if (deviceTypeInfo == 'tablet') {
        orientation = window.Orientation.LANDSCAPE;
      }
      try {
        windowClass.setPreferredOrientation(orientation, (err: BusinessError) => {
          const errCode: number = err.code;
          if (errCode) {
            hilog.error(DOMAIN, 'testTag', 'Failed to set window orientation. Cause: %{public}s', JSON.stringify(err));

            return;
          }
          hilog.info(DOMAIN, 'testTag', 'Succeeded in setting window orientation.');
        });
      } catch (exception) {
        hilog.error(DOMAIN, 'testTag', 'Failed to set window orientation. Cause: %{public}s', JSON.stringify(err));
      }
    });

    // Main window is created, set main page for this ability
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

    windowStage.loadContent('pages/Index', (err) => {
      if (err.code) {
        hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
        return;
      }
      hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
    });
  }

  onWindowStageDestroy(): void {
    // Main window is destroyed, release UI related resources
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
  }

  onForeground(): void {
    // Ability has brought to foreground
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onForeground');
  }

  onBackground(): void {
    // Ability has back to background
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onBackground');
  }
};
```

**Q：如何设置应用在启动后就默认横屏显示？**

**A：**可以配置module.json5中abilities标签的Orientation字段，例如LANDSCAPE（仅支持横屏）或AUTO\_ROTATION\_LANDSCAPE（支持在横屏和反向横屏中切换）。
