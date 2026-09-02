---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-form-16
title: 如何在服务卡片上实现分钟级刷新的效果
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 卡片开发（Form） > 如何在服务卡片上实现分钟级刷新的效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:56+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3669393803ced0bc61aa7a9b8144407934d2d229d982eb488f35a6f22314abc0
---

## 问题现象

服务卡片配置被动刷新时，如果采用定时刷新，最小刷新时间间隔为30分钟；如果采用定点刷新，最多可设置24个时间。如何在服务卡片中实现分钟级刷新的效果？

## 背景知识

* [Form Kit（卡片开发框架）](../harmonyos-guides/formkit-overview.md)提供了一种在桌面、锁屏等系统应用上嵌入显示应用信息的开发框架和API，可以将应用内用户关注的重要信息或常用操作抽取到服务卡片（简称“卡片”）上，通过将卡片添加到桌面、锁屏等系统应用上，以达到信息展示、服务直达的便捷体验效果。
* [ArkTS卡片被动刷新：](../harmonyos-guides/arkts-ui-widget-passive-refresh.md)
  + 定时刷新：表示在一定时间间隔内调用onUpdateForm的生命周期回调函数自动刷新卡片内容。定时刷新有配额限制，每张卡片每天最多通过定时方式触发刷新50次。
  + 定点刷新：表示在每天的某个特定时间点自动刷新卡片内容，最多可设置24个时间。
* [TextClock组件](../harmonyos-references/ts-basic-components-textclock.md)通过文本将当前系统时间显示在设备上。从API version 11开始，该组件支持在ArkTS卡片中使用。当时间变化时，会触发[onDateChange](../harmonyos-references/ts-basic-components-textclock.md#ondatechange)回调，组件不可见时不回调。卡片中使用时，该事件回调间隔为分钟。

## 解决方案

由于卡片被动刷新的次数有限，无法直接在服务卡片上实现分钟级刷新的效果。如果引入TextClock组件后，可通过监听onDateChange回调函数间接实现服务卡片刷新，事件回调间隔为分钟。

示例卡片采用动态时间显示（每分钟刷新并记录日志）和模拟时钟指针旋转（每次刷新旋转30度），同时实时展示刷新次数统计。示例代码如下：

```ts
@Entry
@Component
struct DiawidgetCard {
  @State num: number = 0; // 记录刷新次数

  build() {
    Column() {
      Text(`当前刷新次数为：${this.num}`);
      TextClock()
        .onDateChange((value: number) => {
          const unixTimestamp = value;
          const milliseconds = unixTimestamp * 1000; // 转换为毫秒
          const date = new Date(milliseconds);
          // 获取时间各部分
          const year = date.getFullYear(); // 年份
          const month = date.getMonth() + 1; // 月份(0-11→1-12)
          const day = date.getDate(); // 日期
          const hours = date.getHours(); // 小时
          const minutes = date.getMinutes(); // 分钟
          console.info('当前卡片时间更新为', `${year}-${month}-${day} ${hours}:${minutes}`);
          this.num++;
        })
        // 用于控制组件是否展示
        .visibility(Visibility.Visible);
      Stack() {
        Image($r('sys.media.ohos_ic_public_clock')) // 'sys.media.ohos_ic_public_clock'仅作示例，请替换为实际使用的资源
          .width(100)
          .offset({
            x: -1,
            y: 20
          });
        Row()
          .rotate({
            x: 0,
            y: 0,
            z: 1,
            centerX: '0%',
            centerY: '100%',
            angle: this.num * 30
          })
          .width(2).height(40).backgroundColor(Color.Black);
      };
    }
    .width('100%')
    .height('100%');
  }
}
```

## 常见FAQ

Q：系统时钟应用可以实现秒级刷新卡片，如何实现类似效果？

A：系统时钟应用使用AnalogClock组件，该组件为系统组件，暂不对三方应用开放。

Q：非系统应用是否可以实现秒级刷新卡片？

A：受卡片系统规格约束，三方应用不支持秒级刷新卡片。对于前期突破该规则的应用，近期将进行整改。

Q：服务卡片应用主动刷新机制是否有刷新次数限制？

A：主动刷新机制目前没有次数限制。
