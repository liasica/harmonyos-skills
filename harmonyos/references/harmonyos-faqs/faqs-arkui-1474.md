---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1474
title: 如何解决全屏播放视频时状态栏异常显示的问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 如何解决全屏播放视频时状态栏异常显示的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:14+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:61fced2167216a1478b2f60db7b67d7fa5640956014c996cfa72deddc6476e0c
---

## 问题现象

视频页设置了两种展示内容，通过改变窗口方向实现横屏、竖屏切换效果。全屏播放视频时状态栏隐藏，但退到后台再返回后，状态栏会显示并把视频顶下去。

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/_SuWUan3Su2GvgUZ4Rpayg/zh-cn_image_0000002628765248.gif "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/GpmjApkcTm-j4qoSh7heRQ/zh-cn_image_0000002658964569.gif "点击放大")

## 背景知识

* 视频开发时，可以通过调用窗口的[setPreferredOrientation()](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9)方法实现横竖屏转换。
* 对视频的各项参数和设置做初始化，可以放在[aboutToAppear()](../harmonyos-references/ts-custom-component-lifecycle.md#abouttoappear)方法内。
* 若需要在页面每次回到屏幕最前方时做操作，则可以放在[onPageShow()](../harmonyos-references/ts-custom-component-lifecycle.md#onpageshow)方法内。
* 在进行全屏播放时，通常需要隐藏状态栏，该效果可以通过设置窗口的[setWindowSystemBarEnable](../harmonyos-references/arkts-apis-window-window.md#setwindowsystembarenable9)属性实现。

## 问题定位

1. 熄屏后重新亮起也会复现问题，与退到后台场景的共通点是都会触发onPageShow()方法，判断问题出在onPageShow()方法内。
2. 根据状态栏变化这一现象，排查代码，查看是否有在onPageShow()方法内对状态栏的设置做操作。

```ts
onPageShow(): void {
  let SystemBarProperties: window.SystemBarProperties = {
    statusBarColor: '#FFFFFF',
    statusBarContentColor: '#000000'
  };
  let windowClass: window.Window | undefined = undefined;
  try {
    let promise = window.getLastWindow((this.getUIContext().getHostContext()))
    promise.then((data) => {
      windowClass = data
      windowClass.setWindowSystemBarEnable(['status'])
      windowClass.setWindowSystemBarProperties(SystemBarProperties)
    }).catch((err: BusinessError) => {
      console.error('getLastWindow error')
    })
  } catch (e) {
    console.error('setScreenOrientation error')
  }
}
```

## 分析结论

状态栏的初始化操作放在了onPageShow()方法内，点击全屏后设置了状态栏隐藏。而页面每次回到屏幕最前方时都会触发onPageShow，导致状态栏重新初始化，隐藏失效。从而造成全屏模式下退到后台再返回，状态栏把视频内容顶下去的问题。

## 修改建议

与onPageShow()不同，aboutToAppear()方法只会在页面第一次被创建的时候触发。将状态栏的初始化设置放在aboutToAppear()方法内，可以防止页面多次展示时误触。

```ts
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct VideoCreateComponent {
  // 需要替换为开发者所需的视频资源文件
  @State videoSrc: Resource | string = 'xxx';
  // 需要替换为开发者所需的图片资源文件
  @State previewUri: Resource | string = 'xxx';
  @State curRate: PlaybackSpeed = PlaybackSpeed.Speed_Forward_1_00_X;
  controller: VideoController = new VideoController();
  @State isLandscape: boolean = false;

  // 修改生命周期函数，onPageShow()是问题现象代码，aboutToAppear()是修正后的代码
  aboutToAppear(): void {
    let SystemBarProperties: window.SystemBarProperties = {
      statusBarColor: '#FFFFFF',
      statusBarContentColor: '#000000'
    };
    let windowClass: window.Window | undefined = undefined;
    try {
      let promise = window.getLastWindow((this.getUIContext().getHostContext()));
      promise.then((data) => {
        windowClass = data;
        windowClass.setWindowSystemBarEnable(['status']);
        windowClass.setWindowSystemBarProperties(SystemBarProperties);
      }).catch((err: BusinessError) => {
        console.error(`getLastWindow error: ${err}`);
      });
    } catch (e) {
      console.error(`setScreenOrientation error: ${e}`);
    };
  };

  build() {
    Column() {
      Video({
        src: this.videoSrc,
        previewUri: this.previewUri, // 设置预览图
        currentProgressRate: this.curRate, // 设置播放速度
        controller: this.controller,
        posterOptions: { showFirstFrame: false } // 关闭首帧送显
      })
        .width('100%')
        .height('50%')
        .autoPlay(false)
        .controls(true)
        .enableShortcutKey(false)
        .onStart(() => {
          console.info('onStart');
        })
        .onPause(() => {
          console.info('onPause');
        })
        .onFinish(() => {
          console.info('onFinish');
        })
        .onError(() => {
          console.info('onError');
        })
        .onStop(() => {
          console.info('onStop');
        })
        .onFullscreenChange((e?: FullscreenObject) => {
          if (e != undefined) {
            console.info(`onFullscreenChange is ${e.fullscreen}`);
            if (e.fullscreen) {
              this.isLandscape = true;
              this.setWindowLayOut();
            } else {
              this.isLandscape = false;
              this.setWindowLayOut();
            };
          };
        });
    };
  }

  isShowTop(names: Array<'status' | 'navigation'>) {
    let SystemBarProperties: window.SystemBarProperties = {
      statusBarColor: '#FFFFFF',
      statusBarContentColor: '#000000'
    };
    let windowClass: window.Window | undefined = undefined;
    try {
      let promise = window.getLastWindow((this.getUIContext().getHostContext()));
      promise.then((data) => {
        windowClass = data;
        windowClass.setWindowSystemBarEnable(names);
        windowClass.setWindowSystemBarProperties(SystemBarProperties);
      }).catch((err: BusinessError) => {
        console.error(`getLastWindow error: ${err}`);
      });
    } catch (e) {
      console.error(`setScreenOrientation error: ${e}`);
    };
  }

  setWindowLayOut() {
    // 调用该接口手动改变设备横竖屏状态（设置全屏模式，先强制横屏，再加上传感器模式）
    let context = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
    window.getLastWindow(context).then((windowClass) => {
      if (this.isLandscape) {
        // 设置屏幕横屏
        windowClass.setPreferredOrientation(window.Orientation.AUTO_ROTATION_LANDSCAPE);
        this.isShowTop([]);
      } else {
        // 设置屏幕竖屏
        windowClass.setPreferredOrientation(window.Orientation.AUTO_ROTATION_PORTRAIT);
        this.isShowTop(['status']);
      };
    });
  }
}

interface FullscreenObject {
  fullscreen: boolean;
}
```
