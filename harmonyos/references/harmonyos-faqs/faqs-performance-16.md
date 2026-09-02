---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-16
title: 视频播放页面退出时声音暂停有延迟
breadcrumb: FAQ > 应用质量 > 技术质量 > 性能 > 视频播放页面退出时声音暂停有延迟
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3f220ac83843925fcfa6b55b9500465c97bcd941cc6231d50b0f26a47c1b092f
---

## 问题现象

用户在退出视频播放页面时，视频声音会继续播放一段时间才停止。

## 背景知识

* ArkUI Inspector：DevEco Studio提供的[布局分析](../harmonyos-guides/ide-arkui-inspector.md)工具，开发者可以借助它预览真机或模拟器中的UI效果，快速定位布局层级问题，也可以观察组件属性、不同组件之间的关系等。
* DevEco Profiler：集成在DevEco Studio中的性能调优工具，提供场景化的性能调优功能体验，可以检测应用的性能指标、录制Trace信息，通过分析Trace数据能够发现代码中的性能瓶颈，进而优化性能，更多详细内容可看[使用Profiler进行性能调优](../harmonyos-guides/ide-profiler-introduction.md)。

## 问题定位

1. 首先使用ArkUI Inspector抓取视频播放页面确认当前播放页面是ArkUI页面还是Web页面。
   * ArkUI页面（如下图示例应用使用Video组件播放视频）：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/I0FtxVQjSFWLJYpZJOWZoA/zh-cn_image_0000002628395118.png "点击放大")
   * Web页面（如下图示例应用使用Web组件显示视频页）：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/nkityJnhQPunDe5R7GXF-A/zh-cn_image_0000002658914339.png "点击放大")

2. 使用DevEco Profiler Frame分析工具抓取视频播放页退出时的Trace信息，根据步骤1确认的结果按以下步骤分析。
   * 视频播放页是ArkUI页面：

     展开应用主线程泳道，通过其中的子泳道H:ABILITY\_OR\_PAGE\_SWITCH找到页面退出的部分。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/Tv4L5VL5TOOsvjpCDBh0tA/zh-cn_image_0000002658794387.png "点击放大")

     在上方搜索框中输入H:AudioRenderer::Pause关键字，找到停止音频播放的部分，如果有多个H:AudioRenderer::Pause搜索结果，可通过点击搜索框右侧的箭头来找到靠近H:ABILITY\_OR\_PAGE\_SWITCH的那一个。如下图所示可看到停止音频播放是在页面切换完成之后执行的，而应用停止音频播放时，系统侧需要时间处理，因此会有延迟。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/1qH_3q2fS-qajo7KwDnJhg/zh-cn_image_0000002628555024.png "点击放大")

     从停止音频播放操作处看不出来是由什么触发的，但通常音频播放和停止是由应用控制的，因此可以通过查看线程的唤醒关系来确定。点击应用线程状态中的Runnable状态、查看其中WakeUp From Tid，从下图中可看到是由PlayerRequest线程唤醒的。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/n9rFT4uuSGKoCczgXHeo4A/zh-cn_image_0000002628395120.png "点击放大")

     PlayerRequest线程是属于音频服务media\_service的子线程，不属于应用部分，因此继续查看该线程的唤醒线程。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/aKwwI9IQTzKOxwEwxfdCaw/zh-cn_image_0000002658914341.png "点击放大")

     通过不断查看线程的唤醒关系，最终找到唤醒线程为主线程，从下图中可看到停止音频播放时在视频页面退出过渡完成之后才执行的，而暂停音频播放需要时间，因此会出现页面退出后声音延迟暂停的问题。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/pIdU3ne8SAaE3R3eKD7j7Q/zh-cn_image_0000002658794389.png "点击放大")
   * 视频播放页面是Web页面：

     首先展开应用主线程泳道，通过其中的子泳道H:ABILITY\_OR\_PAGE\_SWITCH找到页面退出的部分。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/PhNP3muhRfmlu-f3Xm8JcQ/zh-cn_image_0000002628555026.png "点击放大")

     然后确定停止音频播放的地方，Web页面音频开始播放、发送数据、停止播放时由AudioThread线程完成的，因此在应用泳道中找到AudioThread，同时通过H:RendererInClientInner::StopAudioStream关键字来确定停止音频播放的部分。从下图中可看到停止音频播放是在页面切换完成后执行的，而暂停音频播放需要时间，因此会出现页面退出后声音延迟暂停的问题。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/eGEitLPqTSWQFjq2laRPnA/zh-cn_image_0000002628395122.png "点击放大")

     Web页面音频播放和暂停是由Web相关的线程控制，可搜索H:AudioOutputDevice::Stop关键字确认Web侧触发音频停止的地方，然后通过该线程的Runnable线程状态查看该线程的唤醒线程，可看到Web侧音频停止是由应用Web渲染线程在执行SetPageLifecycleState时触发。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/HU_ERcsnTJmL0b6MAN6AEQ/zh-cn_image_0000002658914343.png "点击放大")

     对比SetPageLifecycleState和H:ABILITY\_OR\_PAGE\_SWITCH，可看到SetPageLifecycleState执行在页面切换完成，由此可知页面退出后，应用Web渲染线程会更新Web页面生命周期状态，同时停止音频播放，停止音频播放是在页面切换完成后执行的，导致页面退出后声音延迟暂停的问题。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/ZPRJV5W-RbiKZ1ThnZUnHQ/zh-cn_image_0000002658794391.png "点击放大")

## 分析结论

视频播放页面退出过程中，暂停音频播放是在页面退出完成后执行的，导致声音暂停有延迟。

## 修改建议

可重写[onBackPress](../harmonyos-references/ts-custom-component-lifecycle.md#onbackpress)，在开始退出时就停止音频播放。

* 采用Video组件播放视频：

  ```screen
  @Entry
  @Component
  struct VideoPage {
    controller: VideoController = new VideoController();

    onBackPress(): boolean | void {
      this.controller.stop();
    }

    build() {
      Column() {
        Video({
          src: $rawfile('sample.mp4'), // 测试需要替换成可引用到的资源
          controller: this.controller
        })
          .size({
            width: '100%',
            height: '100%'
          })
          .autoPlay(true)
      }
      .height('100%')
      .width('100%')
    }
  }
  ```
* 视频播放页面是Web页面：

  ```screen
  import { webview } from '@kit.ArkWeb';

  @Entry
  @Component
  struct VideoPage {
    controller: webview.WebviewController = new webview.WebviewController();

    onBackPress(): boolean | void {
      try {
        this.controller.stopAllMedia();
      } catch (error) {
        console.error('error: ', error);
      }
    }

    build() {
      Column() {
        Web({
          src: 'https://developer.huawei.com/consumer/cn/design/', // 测试需要替换成可引用到的资源
          controller: this.controller
        })
      }
      .height('100%')
      .width('100%')
    }
  }
  ```
