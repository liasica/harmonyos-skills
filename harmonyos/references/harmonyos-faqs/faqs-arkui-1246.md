---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1246
title: 切换横屏操作后侧滑退出，页面仍为横屏
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 切换横屏操作后侧滑退出，页面仍为横屏
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:13+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:4ba8a59be88cb378158e9b64f60a9bf5cf92aedbeefc6dd1fdb1c6c357018c6e
---

## 问题现象

应用主界面为竖屏状态，点击进入某个横屏页面后，使用侧边返回退到主界面仍为横屏状态。

## 背景知识

[屏幕侧的rotation](../best-practices/bpta-multi-device-window-direction.md#section737072712182)：显示设备的屏幕顺时针旋转角度。

## 问题定位

根据Hilog日志进行问题排查。

1. 在Hilog日志中检索关键字displayOrientation，发现有如下日志信息：

   ```screen
   06-30 16:34:07.318   5739-5739     C0394E/应用包名/AceWindow  应用包名  I     [(-2:100000:singleton)] Update orientation to : 3
   06-30 16:34:07.318   5739-5739     C04208/应用包名/WMSLayout  应用包名  I     [] UpdateViewportConfig(1227): Id:179 reason:3 windowRect:[0,0,2720,1260] displayOrientation:3
   06-30 16:34:07.555   5739-6655     C01406/应用包名/OHOS::RS  应用包名  I     RSUIDirector::ProcessMessages messageId:1, cmdCount:15, instanceId:100000
   06-30 16:34:07.555   5739-5739     C01406/应用包名/OHOS::RS  应用包名  I     RSUIDirector::PostTask messageId:1, cmdCount:15, instanceId:100000
   ```

   则说明，应用当前设置了屏幕旋转为270°。
2. 在Hilog日志中检索关键字OnBackPressed，发现有如下日志信息：

   ```screen
   06-30 16:34:08.767   5739-6655     C0420C/应用包名/WMSEvent       应用包名  I     [] HandleBackEvent(3975): called
   06-30 16:34:08.767   5739-6655     C03900/应用包名/Ace            应用包名  I     [(-1:100000:singleton)] [应用包名][entry][100000]: OnBackPressed called
   06-30 16:34:08.767   5739-5739     C03903/应用包名/AceSubWindow   应用包名  W     [(-2:100000:singleton)] Fail to find subwindow in subwindowMap_, instanceId is 100000.
   06-30 16:34:08.767   5739-5739     C03953/应用包名/SelectOverlay  应用包名  I     [(100000:100000:scope)] isDestroyed:0,isClosed:0
   06-30 16:34:08.768   5739-5739     C03925/应用包名/AceRouter      应用包名  I     [(100000:100000:scope)] router user onBackPress return true
   06-30 16:34:08.768   5739-5739     C03900/应用包名/Ace            应用包名  I     [(100000:100000:scope)] router consumed backpressed event
   06-30 16:34:09.082   5739-5960     A00000/应用包名/erOHOS_Native  应用包名  W     flutter settings log message: dispose state:<optimized out>#802d9
   06-30 16:34:09.084   5739-5739     C02B2B/应用包名/AVPlayerNapi   应用包名  I     #685 JsRelease In
   ```

   此时说明侧滑动作已经响应，用户重写了onBackPress方法。继续查看后续的日志，发现没有设置窗口方向的相关日志。此时，窗口保持旋转为270°的状态。

## 分析结论

应用在响应用户操作，将屏幕旋转后。重写onBackPress方法的逻辑中，没有将屏幕重新旋转回正常的状态。

## 修改建议

在onBackPress方法中，设置屏幕旋转，将其调整回正常的状态。参考如下示例代码：

```screen
setOrientation(type: number) {
  try {
    window.getLastWindow(this.context, (err, data) => {
      //获取window实例
      if (err.code) {
        return;
      }
      let windowClass = data;
      try {
        windowClass.setPreferredOrientation(type, (err) => {
          if (err.code) {
            return;
          }
        });
      } catch (exception) {
      }
    });
  } catch (exception) {
  }
}
```

```screen
onBackPress(): boolean | void {
  this.setOrientation(window.Orientation.PORTRAIT);
  return false;
}
```

完整代码：

```screen
import { window } from '@kit.ArkUI';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct BackPressDemo {
  @State message: string = 'Hello World';
  private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

  setOrientation(type: number) {
    try {
      window.getLastWindow(this.context, (err, data) => {
        //获取window实例
        if (err.code) {
          return;
        }
        let windowClass = data;
        try {
          windowClass.setPreferredOrientation(type, (err) => {
            if (err.code) {
              return;
            }
          });
        } catch (exception) {
        }
      });
    } catch (exception) {
    }
  }

  onBackPress(): boolean | void {
    this.setOrientation(window.Orientation.PORTRAIT);
    return false;
  }

  aboutToAppear(): void {
    this.setOrientation(window.Orientation.LANDSCAPE);
  }

  aboutToDisappear(): void {
    this.setOrientation(window.Orientation.PORTRAIT);
  }

  build() {
    RelativeContainer() {
      Text(this.message)
        .fontSize($r('app.float.page_text_font_size'))
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          this.message = 'Welcome';
        })
    }
    .height('100%')
    .width('100%')
  }
}
```
