---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-29
title: 应用前后台切换时，如何解决Video组件播放发生中断的问题
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 媒体（Media ） > 应用前后台切换时，如何解决Video组件播放发生中断的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:45+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0fc6e1a24b6f29fe0e90ae9ab209db8cf3003ac5fecfec62327827f0155c739a
---

## 问题现象

自定义的组件嵌入到主页面，在页面播放视频被切换到后台，再返回到前台时，视频播放状态异常。

**期待效果：** 视频播放状态应保持连续性，即切换到后台后，视频暂停；返回前台后，视频自动恢复播放。

**实际效果：** 当前视频播放状态未保持连续性，切换到后台后视频停止播放，返回前台后需要手动刷新页面才能恢复播放。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/jKlr0kz6R_GAvenSVC5a_w/zh-cn_image_0000002628552658.png "点击放大")

## 背景知识

* [onPrepared](../harmonyos-references/ts-media-components-video.md#onprepared)：视频准备完成时触发该事件，支持attributeModifier动态设置属性方法。
* Foreground和Background状态：Foreground和Background状态分别在UIAbility实例切换至前台和切换至后台时触发，对应于[onForeground()](../harmonyos-references/js-apis-app-ability-uiability.md#onforeground)回调和[onBackground()](../harmonyos-references/js-apis-app-ability-uiability.md#onbackground)回调。
* [Watch和自定义组件更新](../harmonyos-guides/arkts-watch.md)：@Watch用于监听状态变量的变化，当状态变量变化时，@Watch的回调方法将被调用。

## 问题定位

视频播放功能需要通过VideoController的start()方法启动。因此可以排查应用在前后台切换时controller.start()方法是否被调用。

## 分析结论

播放视频需要调用controller.start()，如下代码。虽然首次进入页面时，可以通过视频准备回调**onPrepared**调用controller.start()，但是前后台切换的时候，该回调不会被触发，因此controller.start()不会被调用，所以会出现视频无法继续播放的情况。

```ts
.onPrepared(()=>{
          this.controller.start()
        })
```

## 修改建议

为了实现前后台切换能够继续播放的效果，结合UIAbility组件生命周期和@Watch和自定义组件更新，考虑在前后台切换时，对APP全局变量的值进行修改，然后通过监听APP全局变量值，以及对其进行判断，来控制视频的停止和播放。

1. 在前后台切换时，对APP里的全局变量isForeGround进行赋值或者修改。

   **代码示例如下：**

   ```ts
     onForeground():void {
       // 切到前台，设置isForeGround值为true
       console.info('onForeground-切换到前台了');
       AppStorage.setOrCreate('isForeGround', true);
     }

     onBackground():void {
       // 切到后台，设置isForeGround值为false
       console.info('onBackground-切换到后台了');
       AppStorage.setOrCreate('isForeGround', false);
     }
   }
   ```

2. 在当前组件用Watch来监听APP全局变量。

   **代码示例如下：**

   ```ts
   //设置变量控制播控图标变化
   @State isplay: boolean = true;
   //设置变量记录播放状态
   state: boolean = true;
   //监听前后台变化
   @Watch('network') @StorageLink('isForeGround') isForeGround: boolean = false;

   network() {
     if (this.isForeGround && this.state) {
       // 切换到前台了且视频播放状态为true，视频继续播放
       this.isplay = true;
       this.controller.start();
     } else {
       // 切换到后台了，视频暂停播放
       this.state = this.isplay;
       this.isplay = false;
       this.controller.pause();
     }
   }
   ```

完整代码示例：

```ts
import { window } from '@kit.ArkUI';

@Entry
@Component
struct VideoControlPage {
  @State private isFullScreen: boolean = false;
  @State videoSrc: Resource = $rawfile('videoTest.mp4');
  private controller = new VideoController();
  @State currentTime: number = 0;
  @State durationTime: number = 100;
  //设置变量控制播控图标变化
  @State isplay: boolean = true;
  //设置变量记录播放状态
  state: boolean = true;
  //监听前后台变化
  @Watch('network') @StorageLink('isForeGround') isForeGround: boolean = false;

  network() {
    if (this.isForeGround && this.state) {
      // 切换到前台了且视频播放状态为true，视频继续播放
      this.isplay = true;
      this.controller.start();
    } else {
      // 切换到后台了，视频暂停播放
      this.state = this.isplay;
      this.isplay = false;
      this.controller.pause();
    }
  }

  build() {
    Stack() {
      Video({
        src: this.videoSrc,
        controller: this.controller
      })
        .width('100%')
        .height('100%')
        .loop(false)
        .controls(false)
        .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
        .onFullscreenChange((event) => {
          this.isFullScreen = event.fullscreen;
          this.changeOrientation(this.isFullScreen);
        })
        .objectFit(ImageFit.Auto)
        .onPrepared((event) => {
          this.controller.start();
          if (event) {
            this.durationTime = event.duration;
          }
        })
        .onUpdate((event) => {
          if (event) {
            this.currentTime = event.time;
          }
        });

      // 自定义的控制器
      Row() {
        Image(this.isplay ? $r('app.media.pause') : $r('app.media.play_fill'))
          .onClick(() => {
            this.isplay = !this.isplay;
            console.info('==', this.isplay);
            if (this.isplay) {
              this.controller.start();
            } else {
              this.controller.pause();
            }
          })
          .width(25)
        Row() {
          Slider({
            value: this.currentTime,
            min: 0,
            max: this.durationTime
          })
            .selectedColor('#fff')
            .trackColor('#7ff1f3f5')
            .width('100%')
            .onChange((value: number) => {
              this.controller.setCurrentTime(value); // 设置视频播放的进度跳转到value处
            })
        }
        .width(this.isFullScreen ? '80%' : '68%');

        // 展示剩余时长
        Text(`${String(Math.floor((this.currentTime / 60))).padStart(2, '0')}` + `:` +
          `${String(this.currentTime % 60).padStart(2, '0')}`)
          .textAlign(TextAlign.Center)
          .fontColor(Color.White);
        // 修改全屏控制方法，同时删除原问题代码中Video组件的onFullscreenChange判断条件
        Image(this.isFullScreen ? $r('app.media.left') : $r('app.media.right'))
          .onClick(() => {
            this.isFullScreen = !this.isFullScreen;
            this.changeOrientation(this.isFullScreen);
          })
          .width(25)
      }
      .offset({ x: 0, y: this.isFullScreen ? 170 : 100 })
      .justifyContent(FlexAlign.SpaceAround)
      .alignItems(VerticalAlign.Center)
      .width('100%')
      .padding(12)
      .zIndex(2);

    }
    .width('100%')
    .height('100%')
  }

  // 更改屏幕方向landscape为true横屏，false竖屏
  changeOrientation(landscape: boolean) {
    window.getLastWindow(this.getUIContext().getHostContext()).then((lastWindow) => {
      lastWindow.setPreferredOrientation(landscape ? window.Orientation.LANDSCAPE : window.Orientation.PORTRAIT);
    });
  }
}
```

**效果预览图：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/ZY5MIJ8mSdOxO-i94pOSYQ/zh-cn_image_0000002658911981.png "点击放大")
