---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-59
title: 进入应用时一直停留在启动页
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > 进入应用时一直停留在启动页
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:50+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9beef9d4ee3960b010211cef9ea30fff3344f82ab14d062968ade9e83402b867
---

## 问题现象

进入应用时，一直停留在启动页，无法进入应用。

## 背景知识

* [Video](../harmonyos-references/ts-media-components-video.md)：用于播放视频文件并控制其播放状态的组件。
* [onFinish](../harmonyos-references/ts-media-components-video.md#onfinish)：播放结束时触发该事件，支持attributeModifier动态设置属性方法。
* [组件可见区域变化事件](../harmonyos-references/ts-universal-component-visible-area-change-event.md)：组件可见区域变化事件是组件在屏幕中的显示区域面积变化时触发的事件，提供了判断组件是否完全或部分显示在屏幕中的能力，适用于广告曝光埋点之类的场景。

## 问题定位

1. 在hilog日志中搜索关键字app cold start，在17:51:34应用冷启动结束，应用发生故障的时间点是17:51:48，需要排查在这段时间之内应用经历的生命周期。

   ```screen
   05-06 17:51:34.771 14900 14958 I C03F00/com.hx.example/ArkCompiler: [gc] SmartGC: app cold start just finished
   ```
2. 搜索关键字JsUIAbility call js，应用在17:51:32切换到前台，在17:51:36因为侧滑手势切换到后台，在17:51:49通过热启动切换到前台。

   ```screen
   05-06 17:51:32.867 14900 14900 I C01332/com.hx.example/UIAbility: [js_ui_ability.cpp:1568]JsUIAbility call js, name: onCreate
   05-06 17:51:32.875 14900 14900 I C01332/com.hx.example/UIAbility: [js_ui_ability.cpp:1568]JsUIAbility call js, name: onWindowStageCreate
   05-06 17:51:32.878 14900 14900 I C01332/com.hx.example/UIAbility: [js_ui_ability.cpp:1568]JsUIAbility call js, name: onForeground
   05-06 17:51:36.143 14900 14900 I C01332/com.hx.example/UIAbility: [js_ui_ability.cpp:1568]JsUIAbility call js, name: onBackPressed
   05-06 17:51:36.151 14900 14900 I C01332/com.hx.example/UIAbility: [js_ui_ability.cpp:1568]JsUIAbility call js, name: onBackground
   05-06 17:51:36.881 14900 14900 I C01332/com.hx.example/UIAbility: [js_ui_ability.cpp:1568]JsUIAbility call js, name: onNewWant
   05-06 17:51:36.882 14900 14900 I C01332/com.hx.example/UIAbility: [js_ui_ability.cpp:1568]JsUIAbility call js, name: onForeground
   05-06 17:51:45.977 14900 14900 I C01332/com.hx.example/UIAbility: [js_ui_ability.cpp:1568]JsUIAbility call js, name: onBackground
   05-06 17:51:49.731 14900 14900 I C01332/com.hx.example/UIAbility: [js_ui_ability.cpp:1568]JsUIAbility call js, name: onNewWant
   05-06 17:51:49.738 14900 14900 I C01332/com.hx.example/UIAbility: [js_ui_ability.cpp:1568]JsUIAbility call js, name: onForeground
   ```
3. 应用启动页在正常情况下会播放视频，视频播放结束后会跳转到主页，在异常场景下视频未播放完成，对比正常的日志，在视频播放结束后会产生日志video finish。

   ```screen
   07-11 09:32:42.256   64899-64899  com.hx.example  I     video finish., %{public}s
   ```
4. 判断应用监听了[Video](../harmonyos-references/ts-media-components-video.md)的[onFinish](../harmonyos-references/ts-media-components-video.md#onfinish)事件，在视频播放结束的回调函数中跳转到主页。在首次冷启动情况下，若用户在视频播放完成前通过侧滑操作将应用退至后台，后续热启动时视频将无法继续播放，导致[onFinish](../harmonyos-references/ts-media-components-video.md#onfinish)事件无法被正确触发。

## 分析结论

启动页视频未播放结束就退出应用到后台，视频暂停，后续热启动视频不会继续播放，无法触发页面跳转逻辑，导致无法进入应用。

## 修改建议

监听[组件可见区域变化事件](../harmonyos-references/ts-universal-component-visible-area-change-event.md)，在Video组件重新可见时继续播放视频。

```screen
@Entry
@Component
export struct VideoPage {
  videoSrc: Resource = $rawfile('TestVideo.mp4'); // 替换为启动页视频
  controller : VideoController = new VideoController();

  build() {
    Column() {
      Video({
        src : this.videoSrc,
        controller: this.controller
      })
        .autoPlay(true)
        .loop(false)
        .objectFit(ImageFit.Contain)
        .onFinish(() => {
          // 此处执行页面跳转
        })
        .onVisibleAreaChange([0.0, 1.0], (isExpanding: boolean, currentRatio: number) => {
          // 当Video组件全部可见时，继续播放
          if (isExpanding || currentRatio >= 1.0) {
            console.info('Test Video is fully visible.');
            this.controller.start();
          }
          // 当Video组件不可见时，暂停播放
          if (!isExpanding && currentRatio <= 0.0) {
            console.info('Test Video is completely invisible.');
            this.controller.pause();
          }
        })
    }
    .height('100%')
    .width('100%')
    .justifyContent(FlexAlign.Center)
  }
}
```
