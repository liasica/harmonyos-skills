---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-traditional-curve
title: 传统曲线
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用动画 > 动画曲线 > 传统曲线
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:51+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a952e8ad8f814a07b69d3929e13bdc15fb0c20d263a06a197b557258d480a677
---

传统曲线基于数学公式，创造形状符合开发者预期的动画曲线。以三阶贝塞尔曲线[curves.cubicBezierCurve](../harmonyos-references/js-apis-curve.md#curvescubicbeziercurve9)为代表，通过调整曲线控制点，可以改变曲线形状，从而带来缓入、缓出等动画效果。对于同一条传统曲线，由于不具备物理含义，其形状不会因为用户行为发生任何改变，缺少物理动画的自然感和生动感。建议优先采用物理曲线创建动画，将传统曲线作为辅助用于极少数必要场景中。

ArkUI提供了贝塞尔曲线、阶梯曲线等传统曲线接口，开发者可参照[插值计算](../harmonyos-references/js-apis-curve.md)进行查阅。

传统曲线的示例和效果如下：

```typescript
class TraditionalCurve {
  public title: string;
  public curve: Curve;
  public color: Color | string;

  constructor(title: string, curve: Curve, color: Color | string = '') {
    this.title = title;
    this.curve = curve;
    this.color = color;
  }
}

const traditionalCurves: TraditionalCurve[] = [
  new TraditionalCurve(' Linear', Curve.Linear, '#317AF7'),
  new TraditionalCurve(' Ease', Curve.Ease, '#D94838'),
  new TraditionalCurve(' EaseIn', Curve.EaseIn, '#DB6B42'),
  new TraditionalCurve(' EaseOut', Curve.EaseOut, '#5BA854'),
  new TraditionalCurve(' EaseInOut', Curve.EaseInOut, '#317AF7'),
  new TraditionalCurve(' FastOutSlowIn', Curve.FastOutSlowIn, '#D94838')
]

@Entry
@Component
struct CurveDemo {
  @State dRotate: number = 0; // 旋转角度

  build() {
    Column() {
      // 曲线图例
      Grid() {
        ForEach(traditionalCurves, (item: TraditionalCurve) => {
          GridItem() {
            Column() {
              Row()
                .width(30)
                .height(30)
                .borderRadius(15)
                .backgroundColor(item.color)
              Text(item.title)
                .fontSize(15)
                .fontColor(0x909399)
            }
            .width('100%')
          }
        })
      }
      .columnsTemplate('1fr 1fr 1fr')
      .rowsTemplate('1fr 1fr 1fr 1fr 1fr')
      .padding(10)
      .width('100%')
      .height(300)
      .margin({ top: 50 })

      Stack() {
        // 摆动管道
        Row()
          .width(290)
          .height(290)
          .border({
            width: 15,
            color: 0xE6E8EB,
            radius: 145
          })

        ForEach(traditionalCurves, (item: TraditionalCurve) => {
          // 小球
          Column() {
            Row()
              .width(30)
              .height(30)
              .borderRadius(15)
              .backgroundColor(item.color)
          }
          .width(20)
          .height(300)
          .rotate({ angle: this.dRotate })
          .animation({
            duration: 2000,
            iterations: -1,
            curve: item.curve,
            delay: 100
          })
        })
      }
      .width('100%')
      .height(200)
      .onClick(() => {
        this.dRotate ? null : this.dRotate = 360;
      })
    }
    .width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/g-VLp0bGTamIwLRIpeuWwA/zh-cn_image_0000002706673858.gif)
