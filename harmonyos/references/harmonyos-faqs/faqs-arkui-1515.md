---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1515
title: TextTimer展示纯秒数时间格式设置
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > TextTimer展示纯秒数时间格式设置
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:11+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:bc3c3277c02abe16532b9a47dd6c2f33898972014058a5d365b6ff553d6497d6
---

## 问题现象

将TextTimer组件的format设置为'ss'，发现当倒计时大于等于60秒时，显示效果不符合预期：60秒显示为'00'(01:00)，实际希望显示'60'，70秒显示为'10'(01:10)，实际希望显示'70'，没有分钟位的显示。如何设置TextTimer才能让它正确显示'60'、'70'这样的纯秒数样式？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/rdvdL9WYR1GXsWVaArt9yg/zh-cn_image_0000002628606558.gif "点击放大")

## 背景知识

[TextTimer](../harmonyos-references/ts-basic-components-texttimer.md)通过文本显示计时信息并控制其计时器状态的组件，可以自定义显示HH、mm、ss、SS等格式，对于个性化需求，可以使用[contentModifier](../harmonyos-references/ts-basic-components-texttimer.md#contentmodifier12)方法定制TextTimer内容区，开发者需要自定义class实现ContentModifier接口。

## 解决方案

使用contentModifier自定义显示内容，用Text显示剩余秒数。[TextTimerConfiguration](../harmonyos-references/ts-basic-components-texttimer.md#texttimerconfiguration12对象说明)包含了计时器设定时间count和经过时间elapsedTime，count减去elapsedTime即为计时器需要显示的剩余时间。

计算时需要注意单位转换，count单位为ms，elapsedTime为设置格式的最小单位，如format设为'mm:ss'则单位为秒、设为'mm'则单位为分。

```screen
class MyTextTimerModifier implements ContentModifier<TextTimerConfiguration> {
  applyContent(): WrappedBuilder<[TextTimerConfiguration]> {
    return wrapBuilder(buildTextTimer);
  }
}

@Builder
function buildTextTimer(config: TextTimerConfiguration) {
  Column() {
    Stack({ alignContent: Alignment.Center }) {
      Circle({ width: 150, height: 150 })
        .fill(config.started ? (config.isCountDown ? 0xFF232323 : 0xFF717171) : 0xFF929292);
      // 剩余时间：用初始时间减去计时器经过的时间
      Text(Math.max(config.count / 1000 - config.elapsedTime / 100, 0).toFixed(0))
        .fontColor(Color.White);
    };
  };
}

@Entry
@Component
struct MyTextTimerDemo {
  @State count: number = 70000;
  @State myTimerModifier: MyTextTimerModifier = new MyTextTimerModifier();
  countDownTextTimerController: TextTimerController = new TextTimerController();

  build() {
    Column({ space: 20 }) {
      TextTimer({ isCountDown: true, count: this.count, controller: this.countDownTextTimerController })
        .contentModifier(this.myTimerModifier); // 自定义显示的内容
      Row({ space: 10 }) {
        Button('start').onClick(() => this.countDownTextTimerController.start());
        Button('pause').onClick(() => this.countDownTextTimerController.pause());
        Button('reset').onClick(() => this.countDownTextTimerController.reset());
      };
    }
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%');
  }
}
```

## 常见FAQ

Q：TextTimer倒计时结束后怎么执行相应回调？

A：[onTimer](../harmonyos-references/ts-basic-components-texttimer.md#ontimer)：时间文本发生变化时触发该事件。锁屏状态和应用后台状态下不会触发该事件。onTimer(event: (utc: number, elapsedTime: number) => void)。在onTimer回调里判断elapsedTime是否到达设定值，来实现执行相应回调。
