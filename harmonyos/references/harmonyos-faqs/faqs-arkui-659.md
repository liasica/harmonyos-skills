---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-659
title: Video组件如何获取视频的时长和播放进度
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Video组件如何获取视频的时长和播放进度
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:02+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:51401c130656c6a69e7dfa55220f30ad82723b1ee304c9a3fa39a0dfc7e52c0d
---

## 问题现象

如何创建一个用于播放视频的自定义组件Player，其内部使用Video组件，然后在另一个自定义父组件内调用Player组件，希望在父组件中获取视频的时长和播放进度信息。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/FK2N7JlzQceYLJ6d6pe2ZQ/zh-cn_image_0000002658913865.png "点击放大")

## 背景知识

* [Video](../harmonyos-guides/arkts-common-components-video-player.md)组件：封装了视频播放的基础能力，需要设置数据源以及基础信息即可播放视频，但相对扩展能力较弱。如果开发者想自定义视频播放，请参考[视频播放](../harmonyos-guides/video-playback.md)。
* [onPrepared](../harmonyos-references/ts-media-components-video.md#onprepared)：视频准备完成时触发该事件，支持[attributeModifier](../harmonyos-references/ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。
* [onUpdate](../harmonyos-references/ts-media-components-video.md#onupdate)：播放进度变化时触发该事件，支持attributeModifier动态设置属性方法。
* [@Prop装饰器](../harmonyos-guides/arkts-prop.md)：@Prop装饰的变量可以和父组件建立单向同步关系。

## 解决方案

通过事件回调机制来实现。核心思路是：

1. 子组件(Player)定义回调接口：在Player组件中，定义可以被父组件传递进来的回调函数onPrepared和onUpdate，分别用于获取视频时长和监控播放进度变化。
2. 父组件传递回调函数：父组件在调用Player时，通过属性方式传入具体的回调函数实现。
3. 子组件在适当时机调用：Player内部的Video组件在onPrepared（获取时长）和onUpdate（获取进度）等事件触发时，调用父组件传过来的回调函数。

父组件:

```ts
@Component
@Entry
struct MovePage {
  @State duration: number = 0; // 视频总时长状态
  @State time: number = 0; // 当前播放时间状态

  build() {
    Column({ space: 20 }) {
      Column() {
        Player({
          src: $rawfile('example.mp4'),
          isControls: true,
          onPrepared: (duration: number) => {
            this.duration = duration;
          },
          onUpdate: (time: number) => {
            this.time = time;
          }
        });
      }
      .width('100%')
      .height('70%');

      Column({ space: 5 }) {
        Text('视频总时长：' + this.duration + 's');
        Text('当前播放进度：' + this.time + 's');
      }.width('100%');
    }
    .width('100%')
    .height('100%');
  }
}
```

子组件：

```ts
@Component
export default struct Player {
  @Prop src: string | Resource;
  @Prop isControls: boolean = true;
  onPrepared?: (duration: number) => void; // 视频准备完成时触发该事件
  onUpdate?: (time: number) => void; // 播放进度变化时触发该事件
  private videoController: VideoController = new VideoController();

  build() {
    Column({ space: 10 }) {
      Video({
        src: this.src,
        controller: this.videoController
      })
        .loop(true)// 循环播放
        .objectFit(ImageFit.Cover)// 画面填充模式
        .controls(this.isControls)// 绑定控制条
        .onPrepared((event) => {
          this.onPrepared?.(event.duration); // 获取到总时长后调用
        })
        .onUpdate((event) => {
          this.onUpdate?.(event.time); // 当前视频播放的进度
        })
        .onError(() => {
          console.error('播放失败');
        });
      Row({ space: 10 }) {
        Button('开始播放')
          .onClick(() => {
            this.videoController.start();
          });
        Button('暂停播放')
          .onClick(() => {
            this.videoController.pause();
          });
      };
    }.width('100%')
    .height('90%');
  }
}
```

## 常见FAQ

Q：Video组件的onUpdate回调仅每秒一次，无法满足精细进度监控的需求。

A：Video组件本身无法实现毫秒级刷新。若需更高精度控制，建议采用[AVPlayer](../harmonyos-references/capi-avplayer.md)实现相关功能。
