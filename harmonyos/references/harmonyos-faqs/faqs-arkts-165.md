---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-165
title: 离开页面时如何销毁所有的setTimeout
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 离开页面时如何销毁所有的setTimeout
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:53+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:46aa31952fce62f806b6d4a8e9ea6d774511d5fb2e70e04dabedf49cc93f6518
---

## 问题现象

在一个页面上设置多个[setTimeout](../harmonyos-references/js-apis-timer.md)定时器，如果存在未执行结束的，在离开页面再次打开这个页面后，setTimeout会接着被运行，关闭页面时如何销毁所有的setTimeout？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/ZHipDr-hSD-GsXlD37iwgg/zh-cn_image_0000002659138343.gif "点击放大")

## 背景知识

setTimeout：设置一个定时器，该定时器在定时器到期后执行一个函数并在回调被执行后自动删除，或使用[clearTimeout](../harmonyos-references/js-apis-timer.md#cleartimeout)接口手动删除。

## 解决方案

目前没有可以清理所有定时器的API，可以使用一个全局数组来存储所有定时器的ID，并在路由跳转、应用进入后台等场景时循环清除这些定时器。

```ts
@Entry
@Component
struct clearAllTimeouts1 {
  timeouts: number[] = [];
  @State content: number = 0;
  @State clickNum: number = 0;

  clearAllTimeouts(timeouts: number[]) {
    timeouts?.forEach(timeoutId => {
      clearTimeout(timeoutId); // 按照定时器ID循环清除定时器
    });
    this.timeouts = []; // 初始化数组
  }

  onPageHide() {
    this.clearAllTimeouts(this.timeouts); // 离开页面时清除所有定时器
  }

  build() {
    Row() {
      Column({ space: 20 }) {
        Button('create')
          .onClick(() => {
            this.clickNum++;
            let newTimeoutId = setTimeout(() => {
              this.content++;
            }, 2000);
            this.timeouts.push(newTimeoutId);
          });
        Button('clear')
          .onClick(() => {
            this.clickNum = 0;
            this.content = 0;
            this.clearAllTimeouts(this.timeouts); // 主动触发清除所有定时器
          });
        Text('点击了' + this.clickNum + '次按钮');
        Text('创建了' + this.content + '个定时器');
      }
      .width('100%');
    }
    .height('100%');
  }
}
```
