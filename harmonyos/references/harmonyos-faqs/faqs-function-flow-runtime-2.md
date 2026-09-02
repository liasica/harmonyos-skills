---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-function-flow-runtime-2
title: 是否有让进程睡眠的API
breadcrumb: FAQ > 应用框架开发 > NDK开发 > 任务并发调度（Function Flow Runtime） > 是否有让进程睡眠的API
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:58+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b8190b245eddfb43bccc6a00b68c14e51b1b710c9e47d8c8158b25efa6ca80f5
---

## 问题现象

HarmonyOS中是否有让进程睡眠的API？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/PLQD5NteSWujekbW5MzmQg/zh-cn_image_0000002628899080.gif "点击放大")

## 背景知识

[setTimeout](../harmonyos-references/js-apis-timer.md#settimeout)可以设置一个定时器，该定时器在定时器到期后执行一个函数。

## 解决方案

HarmonyOS中未直接提供进程睡眠的API。

方案一：可以通过setTimeout方法间接实现睡眠效果，参考如下sleep方法。

方案二：使用Atomics.wait来达到sleep效果，参考如下sleepAtomics方法。

```screen
@Entry
@Component
struct SleepPage {
  @State message: string = 'Hello World';

  // 睡眠等待方法，time为睡眠时间，单位毫秒
  sleep(time: number): Promise<void> {
    return new Promise(resolve => setTimeout(resolve, time));
  }

  sleepAtomics(time: number) {
    let sharedBuf = new SharedArrayBuffer(4);
    let sharedArr = new Int32Array(sharedBuf);
    Atomics.wait(sharedArr, 0, 0, time);
    this.message = 'Atomics 3000';
  }

  build() {
    Column() {
      Text(this.message)
        .id('SleepPageHelloWorld')
        .fontSize('50fp')
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          this.message = 'Welcome';
        })
      Button('Sleep修改message')
        .onClick(async () => {
          // 等待3秒
          await this.sleep(3000);
          this.message = 'SLEEP 3000';
        })
        .margin({ top: 20 });

      Button('sleepAtomics修改message')
        .onClick(async () => {
          // 等待3秒
          this.sleepAtomics(3000);
        })
        .margin({ top: 20 });
    }
    .height('100%')
    .width('100%');
  }
}
```
