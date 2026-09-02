---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-623
title: 应用统计的视频播放时长比实际播放时长少
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 应用统计的视频播放时长比实际播放时长少
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:01+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a34faa464d71bb86aa9820dcd77cfd1c04ea03905e3d5d67342e3274a946e995
---

## 问题现象

应用统计的视频播放时长比实际播放时长少。

例如：实际播放时间为40分钟，但是统计显示只有30分钟。

## 背景知识

* [Video组件](../harmonyos-references/ts-media-components-video.md)：Video组件是用于播放视频文件并控制其播放状态的组件。
* [onFinish事件](../harmonyos-references/ts-media-components-video.md#onfinish)：播放结束时触发Video组件的'onFinish'事件回调。
* [setInterval](../harmonyos-references/js-apis-timer.md#setinterval)：Timer模块提供的定时器能力。重复调用一个函数，在每次调用之间具有固定的时间延迟。

## 问题定位

1. 定位到更新播放时长数据的代码。

   ```ts
    // 更新播放时长数据
    const currentTime = Date.now();
    this.playTime += (currentTime - this.startTime ) / 6000;
    this.startTime = currentTime;
   ```
2. 确认更新播放时长数据的代码在Video组件的'onFinish'事件回调中。

   ```ts
   // 播放完成事件
   .onFinish(() => {
      // 其他业务逻辑
      // 更新播放时长变量
      const currentTime = Date.now();
      this.playTime += (currentTime - this.startTime ) / 6000;
      this.startTime = currentTime;
    })
   ```

## 分析结论

应用在Video组件的onFinish事件中更新播放时长，导致视频不停止播放时时长数据无法正常更新。

## 修改建议

播放视频时设置定时器，及时同步时长数据，避免播放时长更新不及时。

应根据具体业务需要设置定时器触发间隔，此处以10秒钟更新一次时长为例：

```ts
@Entry
@Component
struct PlayTimeFixPage {
  @State playTime: number = 0; // 单位：毫秒
  private startTime: number = Date.now();
  private timer: number = -1;

  aboutToAppear() {
    this.timer = setInterval(() => {
      const now = Date.now();
      this.playTime += (now - this.startTime);
      this.startTime = now;
    }, 10000);
  }

  aboutToDisappear() {
    clearInterval(this.timer);
  }

  /* 工具：毫秒 → 时:分:秒 */
  formatTime(ms: number): string {
    const total = Math.floor(ms / 1000);
    const h = Math.floor(total / 3600).toString().padStart(2, '0');
    const m = Math.floor((total % 3600) / 60).toString().padStart(2, '0');
    const s = (total % 60).toString().padStart(2, '0');
    return `${h}:${m}:${s}`;
  }

  build() {
    Column({ space: 20 }) {
      Text(`播放时长：${this.formatTime(this.playTime)}`)
        .fontSize(24);
      Text('10 秒同步一次')
        .fontSize(14)
        .fontColor('#999');
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center);
  }
}
```
