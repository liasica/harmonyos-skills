---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1378
title: 如何实现视频流列表功能
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现视频流列表功能
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:24+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:322dc7a466acc82aa9290c1fbb2e6559d26d3eb2d7260bbf8625d57a6f25c8be
---

## 问题现象

应用内有视频流列表功能，用户点击进入视频列表页面后固定推送三十个视频，请问该如何实现？

## 背景知识

在HarmonyOS开发中，[Swiper组件](../harmonyos-references/ts-container-swiper.md)主要用于创建轮播图或滑动视图，而[LazyForEach](../harmonyos-references/ts-rendering-control-lazyforeach.md)用于实现数据的懒加载，两者结合可以有效地优化固定数量数据集的加载和显示性能。视频播放可以通过[Video组件](../harmonyos-references/ts-media-components-video.md)或[AVPlayer接口](../harmonyos-references/arkts-apis-media-avplayer.md)实现。

## 解决方案

* **功能一：视频播放。**
  + **实现原理：** 视频播放可以选择Video组件或者AVPlayer接口，本文以Video组件为例，结合Stack实现自定义视频控制栏和功能。如果对拓展性有较高要求，可以自行选择AVPlayer接口实现。
  + **示例代码：**

    ```ets
    @Component
    struct VideoShow {
      @Prop videoSrc: string = '';
      controller: VideoController = new VideoController();
      @State isPlay: boolean = false;//是否播放
      @Prop isAutoPlay: boolean = false;//是否自动播放

      build() {
        Column() {
          Stack() {
            Video({src: $rawfile(this.videoSrc), controller: this.controller})
              .controls(false)
              .autoPlay(this.isAutoPlay)
              .onClick(() => {
                this.isPlay = !this.isPlay;
                if (this.isPlay) { // 控制视频播放状态
                  this.controller.pause();
                } else {
                  this.controller.start();
                }
              })
          }
        }
        .width('100%')
        .height('100%')
      }
    }
    ```
* **功能二：滑动列表。**
  + **实现原理：** 将Swiper组件设置为竖向滑动，实现列表的整页滑动，视频数据则使用LazyForEach加载。同时设置页面沉浸式，优化视频观感。
  + **示例代码：**

    ```ets
    import { window } from '@kit.ArkUI';
    import { common } from '@kit.AbilityKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';

    class MyDataSourceLTwo implements IDataSource {// 加载数据
      private list: string[] = [];

      constructor(list: string[]) {
        this.list = list;
      }

      totalCount(): number {
        return this.list.length;
      }

      getData(index: number): string {
        return this.list[index];
      }

      registerDataChangeListener(): void {
        console.info(`注册数据变化监听`);
      }

      unregisterDataChangeListener() {
        console.info(`取消数据变化监听`);
      }
    }
    @Entry
    @Component
    struct ShortVideo {
      private data: MyDataSourceLTwo = new MyDataSourceLTwo([]);
      @State nowNum: number = 0;
      context: Context | undefined = undefined;

      setVideoFull() { // 设置沉浸式
        let windowClass: window.Window | undefined = undefined;
        try {
          let promise = window.getLastWindow(this.context);
          promise.then((data) => {
            windowClass = data;
            windowClass.setWindowLayoutFullScreen(true).then(() => {
              hilog.info(0x0000, 'testTag', 'Succeeded in setting the window layout to full-screen mode.');
            }).catch((err: BusinessError) => {
              hilog.error(0x0000, 'testTag',
                'Failed to set the window layout to full-screen mode. Cause:' + JSON.stringify(err));
            });
            //状态栏隐藏
            windowClass.setSpecificSystemBarEnabled('status', true).then(() => {
              hilog.info(0x0000, 'testTag', 'Succeeded in setting the status bar to be invisible.');
            }).catch((err: BusinessError) => {
              hilog.error(0x0000, 'testTag', `Failed to set the status bar to be invisible. Code is ${err.code},
              message is ${err.message}`);
            });
            //导航条隐藏
            windowClass.setSpecificSystemBarEnabled('navigationIndicator', false).then(() => {
              hilog.info(0x0000, 'testTag', 'Succeed in setting the system bar to be invisible');
            }).catch((err: BusinessError) => {
              hilog.error(0x0000, 'testTag',
                `Failed to set the system bar to be invisible. Cause code: ${err.code}, message: ${err.message}`);
            });
          }).catch((err: BusinessError) => {
            console.error('getLastWindow error', err);
          });
        } catch (e) {
          console.error('setScreenOrientation error');
        }
      }

      aboutToAppear(): void {
        let list: string[] = [];
        for (let i = 1; i <= 3; i++) {
          list.push('videoTest.mp4');
        }
        this.data = new MyDataSourceLTwo(list);
        this.context = this.getUIContext().getHostContext() as common.Context;
        this.setVideoFull();
      }

      build() {
        Column() {
          Swiper() {
            LazyForEach(this.data, (item: string, index: number) => {
              VideoShow({
                videoSrc: this.nowNum === index ? item : '',
                isAutoPlay: this.nowNum === index ? true : false
              });
            })
          }
          .width('100%')
          .height('100%')
          .vertical(true) // 设置竖向
          .indicator(false) // 设置不显示导航点
          .loop(false) // 设置不循环
          .onChange((index: number) => {
            this.nowNum = index;
          })
        }
        .width('100%')
        .height('100%')
      }
    }
    ```

**完整示例代码：**

```ets
import { window } from '@kit.ArkUI';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class MyDataSourceLTwo implements IDataSource {// 加载数据
  private list: string[] = [];

  constructor(list: string[]) {
    this.list = list;
  }

  totalCount(): number {
    return this.list.length;
  }

  getData(index: number): string {
    return this.list[index];
  }

  registerDataChangeListener(): void {
    console.info(`注册数据变化监听`);
  }

  unregisterDataChangeListener() {
    console.info(`取消数据变化监听`);
  }
}
@Entry
@Component
struct ShortVideo {
  private data: MyDataSourceLTwo = new MyDataSourceLTwo([]);
  @State nowNum: number = 0;
  context: Context | undefined = undefined;

  setVideoFull() { // 设置沉浸式
    let windowClass: window.Window | undefined = undefined;
    try {
      let promise = window.getLastWindow(this.context);
      promise.then((data) => {
        windowClass = data;
        windowClass.setWindowLayoutFullScreen(true).then(() => {
          hilog.info(0x0000, 'testTag', 'Succeeded in setting the window layout to full-screen mode.');
        }).catch((err: BusinessError) => {
          hilog.error(0x0000, 'testTag',
            'Failed to set the window layout to full-screen mode. Cause:' + JSON.stringify(err));
        });
        //状态栏隐藏
        windowClass.setSpecificSystemBarEnabled('status', true).then(() => {
          hilog.info(0x0000, 'testTag', 'Succeeded in setting the status bar to be invisible.');
        }).catch((err: BusinessError) => {
          hilog.error(0x0000, 'testTag', `Failed to set the status bar to be invisible. Code is ${err.code},
          message is ${err.message}`);
        });
        //导航条隐藏
        windowClass.setSpecificSystemBarEnabled('navigationIndicator', false).then(() => {
          hilog.info(0x0000, 'testTag', 'Succeed in setting the system bar to be invisible');
        }).catch((err: BusinessError) => {
          hilog.error(0x0000, 'testTag',
            `Failed to set the system bar to be invisible. Cause code: ${err.code}, message: ${err.message}`);
        });
      }).catch((err: BusinessError) => {
        console.error('getLastWindow error', err);
      });
    } catch (e) {
      console.error('setScreenOrientation error');
    }
  }

  aboutToAppear(): void {
    let list: string[] = [];
    for (let i = 1; i <= 3; i++) {
      list.push('videoTest.mp4');
    }
    this.data = new MyDataSourceLTwo(list);
    this.context = this.getUIContext().getHostContext() as common.Context;
    this.setVideoFull();
  }

  build() {
    Column() {
      Swiper() {
        LazyForEach(this.data, (item: string, index: number) => {
          VideoShow({
            videoSrc: this.nowNum === index ? item : '',
            isAutoPlay: this.nowNum === index ? true : false
          });
        })
      }
      .width('100%')
      .height('100%')
      .vertical(true) // 设置竖向
      .indicator(false) // 设置不显示导航点
      .loop(false) // 设置不循环
      .onChange((index: number) => {
        this.nowNum = index;
      })
    }
    .width('100%')
    .height('100%')
  }
}

@Component
struct VideoShow {
  @Prop videoSrc: string = '';
  controller: VideoController = new VideoController();
  @State isPlay: boolean = false;//是否播放
  @Prop isAutoPlay: boolean = false;//是否自动播放

  build() {
    Column() {
      Stack() {
        Video({src: $rawfile(this.videoSrc), controller: this.controller})
          .controls(false)
          .autoPlay(this.isAutoPlay)
          .onClick(() => {
            this.isPlay = !this.isPlay;
            if (this.isPlay) { // 控制视频播放状态
              this.controller.pause();
            } else {
              this.controller.start();
            }
          })
      }
    }
    .width('100%')
    .height('100%')
  }
}
```

效果图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/uYWW81MESFuW_Hwy-X2L6g/zh-cn_image_0000002658841819.png "点击放大")

## 常见FAQ

Q：当加载数据量较大时，Swiper组件会出现加载缓慢、丢帧的问题，该如何优化？

A：可以为LazyForEach懒加载设置[cachedCount](../harmonyos-references/ts-container-swiper.md#cachedcount8)来指定缓存数量，或者使用[@Reusable](../harmonyos-guides/arkts-reusable.md)复用组件，具体实现可参考：[Swiper组件加载丢帧优化](../best-practices/bpta-swiper_high_performance_development_guide.md)。
