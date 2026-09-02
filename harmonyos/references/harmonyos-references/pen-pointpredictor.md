---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-pointpredictor
title: PointPredictor（报点预测功能）
breadcrumb: API参考 > 系统 > 硬件 > Pen Kit（手写笔服务） > ArkTS API > PointPredictor（报点预测功能）
category: harmonyos-references
scraped_at: 2026-09-02T14:52:38+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:c8e9f02e7d48667b19802b7ed098642a62db0f7f97a838682afbdd46bd1da8e4
---

本模块提供报点预测能力。通过调用报点预测接口，可以优化应用中手写效果的绘制跟手性，提升应用中手写笔书写场景的跟手体验。

**起始版本：** 5.0.0(12)

## 导入模块

```typescript
import { PointPredictor } from '@kit.Penkit';
```

本模块提供以下方法。

| 方法名称 | 说明 |
| --- | --- |
| [getPredictionPoint](pen-pointpredictor.md#getpredictionpoint) | 获取预测点信息。 |

## getPredictionPoint

getPredictionPoint(event: TouchEvent): TouchPoint

获取预测点信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Stylus.Handwrite

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| event | [TouchEvent](ts-universal-events-touch.md#touchevent对象说明) | 是 | 当前点信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TouchPoint](ts-types.md#touchpoint11) | 预测点信息。 |

**示例：**

```typescript
import { PointPredictor } from '@kit.Penkit';

@Entry
@Component
struct PointPredictorDemo {
  @State actualXCoordinate: number = 0;
  @State actualYCoordinate: number = 0;
  @State predictorXCoordinate: Dimension = 0;
  @State predictorYCoordinate: Dimension = 0;
  pointPredictor: PointPredictor = new PointPredictor();

  aboutToAppear() {
    console.info('getPredictionPoint aboutToAppear');
  }

  aboutToDisappear() {
    console.info('getPredictionPoint aboutToDisappear');
  }

  build() {
    Stack({ alignContent: Alignment.TopEnd }) {
      this.canvas(); // 画布。
    }.height('100%').width('100%')
  }

  // 画布
  @Builder
  canvas() {
    Column() {
      Text('实际点坐标： X: ' + this.actualXCoordinate + ' Y: ' + this.actualYCoordinate).textAlign(TextAlign.Start)
      Text('预测点坐标： X: ' + this.predictorXCoordinate + ' Y: ' + this.predictorYCoordinate)
        .textAlign(TextAlign.Start)
    }.position({ x: 0, y: 0 })
    .alignItems(HorizontalAlign.Start)

    Stack()
      .width('100%')
      .height('100%')
      .onTouch((event: TouchEvent) => {
        switch (event.type) {
          case TouchType.Down: // 按下时，新建一条画图路径。
            break;
          case TouchType.Move: // 使用预测算法进行预测，获得预测点。
            let point = this.pointPredictor?.getPredictionPoint(event);
            this.actualXCoordinate = event.touches[0]?.x;
            this.actualYCoordinate = event.touches[0]?.y;
            this.predictorXCoordinate = point?.x;
            this.predictorYCoordinate = point?.y;
            console.info('pointPredictor 实际点坐标 x:' + event.touches[0]?.x + ' y:' + event.touches[0]?.y);
            console.info('pointPredictor 预测点坐标 x:' + point?.x + '  y:' + point?.y);
            break;
          case TouchType.Up:
            break;
        }
      })
  }
}
```
