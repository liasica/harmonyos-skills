---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-877
title: 应用内展示时间和系统时间不一致
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 应用内展示时间和系统时间不一致
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:04+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:552503e83e5605de914205b9fabd8eecb7c7c49dc063ce893549ef35ff7978bc
---

## 问题现象

应用使用一段时间后，页面时间和系统时间不一致，比系统时间慢。

## 背景知识

[TextClock](../harmonyos-references/ts-basic-components-textclock.md)：通过文本将当前系统时间显示在设备上。支持不同时区的时间显示，最高精度到秒级。

## 问题定位

1. 应用在有操作事件的情况下，通过关键词“time”过滤日志，可以看到如下日志，且时间是同步系统时间的：

   ```shell
   07-21 22:12:11.281   64146-64146   C03F01/com.hm.example/NAPI  com.hm.example  I     [(:141)(ClearTimer)] DeleteTimer ID: 169, count: 75
   ```
2. 应用在无操作事件情况下，无上述日志打印，说明此时应用不会更新时间，从而导致页面时间和系统时间不一致，比系统时间慢。
3. 应用从当前页面回到已加载过的页面，显示时间依旧为老时间，非系统当前时间。

## 分析结论

应用的时间同步靠时间定时器任务刷新，但时间定时器任务的触发依赖用户操作事件，所以需要使用不依赖定时任务的方式实时刷新时间。

## 修改建议

HarmonyOS系统提供了TextClock组件，可以将当前系统时间实时显示在设备上，参考代码：

```ts
@Entry
@Component
struct TextClockDemo {
  controller: TextClockController = new TextClockController();

  build() {
    Column() {
      // 显示东八区的系统时间，精确到秒。
      TextClock({ timeZoneOffset: -8, controller: this.controller })
        .format('HH:mm:ss') // 24小时制：HH:mm:ss
        .margin(20)
        .fontSize(30);
    }
    .height('100%')
    .width('100%')
    .justifyContent(FlexAlign.SpaceAround);
  }
}
```
