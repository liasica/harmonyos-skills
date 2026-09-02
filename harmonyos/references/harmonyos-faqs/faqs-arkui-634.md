---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-634
title: animation播放动画异常突变
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > animation播放动画异常突变
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:21+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:002188324b576682fe36d9d2f48038310d4453fda7222748adc3491b00f2de5b
---

## 问题现象

转场动画期望由大缩小，且动画连贯流畅。但是实际的情况是，当页面显示发生转场，页面中圆初始显示为小的状态，待延时结束，再突然变大，然后由大缓慢缩小。其中突然变大导致整体效果不连贯，如何实现转场动画从页面开始显示，圆一直保持大的状态到延时结束，然后缩小？

问题代码示例参考如下：

```ts
@Entry
@ComponentV2
struct ShackHand {
  @Param serverActive: boolean = false
  // 动画点信息
  @Local colorArray: Array<JumpTrans> = [
    new JumpTrans('#8002ECFC', 500),
    new JumpTrans('#802d2de3', 1000),
    new JumpTrans('#8002ECFC', 1500),
    new JumpTrans('#802d2de3', 2000),
    new JumpTrans('#8002ECFC', 2500),
  ]

  build() {
    RelativeContainer() {
      ForEach(this.colorArray, (jump: JumpTrans, index: number) => {
        Circle({ width: '180lpx', height: '180lpx' })
          .stroke(Color.White)
          .margin({
            left: index * 30
          })
          .strokeWidth('5lpx')
          .fill(jump.color)
          .transition(generateEffect(jump.delay)) // 设置动画效果
      })

    }
    .backgroundColor(Color.Black)
    .width('600lpx')
    .height('600lpx')

  }
}

// 动画效果
function generateEffect(delay: number): TransitionEffect {
  return TransitionEffect.scale({ x: 0.1, y: 0.1 })
    .animation({
      duration: 1000,
      playMode: PlayMode.Reverse, // 动画反向播放
      delay: delay
    })

}

// 信息类
class JumpTrans {
  color: ResourceColor
  delay: number

  constructor(color: ResourceColor, delay: number) {
    this.color = color
    this.delay = delay
  }
}
```

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/UAFfOda8S3G5Mzf8b-sYwA/zh-cn_image_0000002628394280.gif "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/AsEgnbwFS02KATkuWlin1Q/zh-cn_image_0000002658913495.gif "点击放大")

## 背景知识

* [组件内转场 (transition)](../harmonyos-references/ts-transition-animation-component.md)主要通过transition属性配置转场参数，在组件插入和删除时显示过渡动效，主要用于容器组件中的子组件插入和删除时，提升用户体验。
* [属性动画 (animation)](../harmonyos-references/ts-animatorproperty.md)组件的某些通用属性变化时，可以通过属性动画实现渐变过渡效果，提升用户体验。其中[delay](../harmonyos-references/js-apis-animator.md#delay18)属性用于设置动画延迟播放时间，[PlayMode](../harmonyos-references/ts-appendix-enums.md#playmode)用于设置动画的播放方式。

## 问题定位

该问题涉及动画播放的两个阶段：

* 动画之前形态：transition会在转场动画播放前保持设置的动画初始形态，即scale({ x: 0.1, y: 0.1 })。因为delay延迟了动画播放，所以这个形态会展示到UI。
* 动画开始形态：因为使用了PlayMode.Reverse动画反向播放，所以动画的开始形态变成了scale({ x: 1, y: 1 })。

由上述可知动画播放之前形态和动画开始形态有较大差距，因此出现突兀变化。

## 分析结论

delay和PlayMode.Reverse属性设置不当会导致动画播放前出现组件形态的突兀变化，因此不建议组合使用。

## 修改建议

若有延时效果，建议使用PlayMode.Normal，同时动画效果与目标状态翻转设置一下即可。

完整示例参考如下：

```ts
@Entry
@ComponentV2
struct JumpTransCustom {
  // 动画数据
  @Local colorArray: Array<JumpTrans> = [
    new JumpTrans('#8002ECFC', 500),
    new JumpTrans('#802d2de3', 1000),
    new JumpTrans('#8002ECFC', 1500),
    new JumpTrans('#802d2de3', 2000),
    new JumpTrans('#8002ECFC', 2500),
  ];

  build() {
    Column() {
      RelativeContainer() {
        ForEach(this.colorArray, (jump: JumpTrans, index: number) => {
          Circle({ width: '180lpx', height: '180lpx' })
            .stroke(Color.White)
            .margin({
              left: index * 30
            })
            .strokeWidth('5lpx')
            .fill(jump.color)
            .transition(generateEffect(jump.delay))  // 调用动画函数
            .scale({ x: 0.1, y: 0.1 });
        });
      }
      .backgroundColor(Color.Black)
      .width('600lpx')
      .height('600lpx');
    };
  }
}

// 动画效果
function generateEffect(delay: number): TransitionEffect {
  return TransitionEffect.scale({ x: 8, y: 8 })
    .animation({
      duration: 1000,
      playMode: PlayMode.Normal,
      delay: delay
    });
}

// 数据类
class JumpTrans {
  color: ResourceColor;
  delay: number;

  constructor(color: ResourceColor, delay: number) {
    this.color = color;
    this.delay = delay;
  }
}
```
