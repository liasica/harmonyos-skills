---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-823
title: Progress滑动评分动效实现
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > Progress滑动评分动效实现
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:23+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9f7f8b5d03bbe78a8d33bc2f43793323c0f5b5b63c12db97bf61495f78b5f97a
---

## 问题现象

如何自定义图案实现滑动评分的动效？

## 背景知识

* [自定义内容](../harmonyos-references/ts-universal-attributes-content-modifier.md)支持通过样式builder自定义特定组件的内容区。
* [Progress](../harmonyos-references/ts-basic-components-progress.md)进度条组件，用于显示内容加载或操作处理等进度。
* [PanGesture](../harmonyos-references/ts-basic-gestures-pangesture.md)滑动手势事件，当滑动的最小距离达到设定的最小值时触发滑动手势事件。

## 解决方案

1. 自定义评分样式。

   ```ts
   //自定义评分样式
   class MyProgressModifier implements ContentModifier<ProgressConfiguration> {
     color: ResourceColor = Color.White;
     outerRadius: number = 500;
     innerRadius: number;
     idList: Array<string> = ['1', '3', '5', '7', '9'];

     constructor(color: ResourceColor, outerRadius: number) {
       this.color = color;
       this.outerRadius = outerRadius;
       this.innerRadius = outerRadius * sin(18) / cos(36);
     }

     // 绘制五角星路径的字符串
     paintingPath(startX: number, startY: number, isHalf: boolean = false, isLeft: boolean = true) {
       let point1: string = `${startX} ${startY}`;
       let point3: string = `${startX - this.outerRadius * cos(18)} ${startY - (sin(18) - 1) * this.outerRadius}`;
       let point5: string = `${startX - this.outerRadius * cos(54)} ${startY - (-sin(54) - 1) * this.outerRadius}`;
       let point7: string = `${startX + this.outerRadius * cos(54)} ${startY - (-sin(54) - 1) * this.outerRadius}`;
       let point9: string = `${startX + this.outerRadius * cos(18)} ${startY - (sin(18) - 1) * this.outerRadius}`;

       let point2: string =
         `${startX - this.innerRadius * cos(54)} ${startY - this.innerRadius * sin(54) + this.outerRadius}`;
       let point4: string =
         `${startX - this.innerRadius * cos(18)} ${startY + this.innerRadius * sin(18) + this.outerRadius}`;
       let point6: string = `${startX} ${startY + this.innerRadius + this.outerRadius}`;
       let point8: string =
         `${startX + this.innerRadius * cos(18)} ${startY + this.innerRadius * sin(18) + this.outerRadius}`;
       let point10: string =
         `${startX + this.innerRadius * cos(54)} ${startY - this.innerRadius * sin(54) + this.outerRadius}`;
       if (!isHalf) {
         return `M${point1} L${point2} L${point3} L${point4} L${point5} L${point6} L${point7} L${point8} L${point9} L${point10} L${point1} Z`;
       }
       if (isLeft) {
         return `M${point1} L${point2} L${point3} L${point4} L${point5} L${point6}`;
       }
       return `M${point6} L${point7} L${point8} L${point9} L${point10} L${point1} `;
     }

     applyContent(): WrappedBuilder<[ProgressConfiguration]> {
       return wrapBuilder(myProgress);
     }
   }
   ```
2. 通过Path路径绘制评分左/右图案，用于表示0.5评分。

   ```ts
   @Builder
   function leftStar(config: ProgressConfiguration, value: number) {
     // 绘制左半部分
     Path()
       .width('100px')
       .height('100%')
       .commands((config.contentModifier as MyProgressModifier).paintingPath(100, 0, true, true))
       .fill(config.enabled && config.value >= value ? (config.contentModifier as MyProgressModifier).color :
         '#1A000000')
       .strokeLineCap(LineCapStyle.Round)
       .strokeLineJoin(LineJoinStyle.Round)
       .strokeWidth(0);
   }

   @Builder
   function rightStar(config: ProgressConfiguration, value: number) {
     // 绘制右半部分
     Path()
       .width('100px')
       .height('100%')
       .commands((config.contentModifier as MyProgressModifier).paintingPath(0, 0, true, false))
       .fill(config.enabled && config.value >= value ? (config.contentModifier as MyProgressModifier).color :
         '#1A000000')
       .strokeLineCap(LineCapStyle.Round)
       .strokeLineJoin(LineJoinStyle.Round)
       .strokeWidth(0);
   }
   ```
3. 手势滑动时相关属性变动处理，并渲染页面。

   ```ts
   Progress({ value: this.currentValue, total: 10 })
     .contentModifier(this.modifier) // 自定义评分栏
     .gesture(
       // 滑动手势x发生变化时修改评分
       PanGesture()
         .onActionStart((event: GestureEvent) => {
           this.progressX = event.fingerList[0].localX;
           this.currentValue = this.context.vp2px(this.progressX) / 100;
         })
         .onActionUpdate((event: GestureEvent) => {
           this.progressX = event.fingerList[0].localX;
           this.currentValue = this.context.vp2px(this.progressX) / 100;
         })
     );
   ```

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/bNMhR760Q5mFgeksBd0EGA/zh-cn_image_0000002658917665.png "点击放大")

完整代码：

```ts
//自定义评分样式
class MyProgressModifier implements ContentModifier<ProgressConfiguration> {
  color: ResourceColor = Color.White;
  outerRadius: number = 500;
  innerRadius: number;
  idList: Array<string> = ['1', '3', '5', '7', '9'];

  constructor(color: ResourceColor, outerRadius: number) {
    this.color = color;
    this.outerRadius = outerRadius;
    this.innerRadius = outerRadius * sin(18) / cos(36);
  }

  // 绘制五角星路径的字符串
  paintingPath(startX: number, startY: number, isHalf: boolean = false, isLeft: boolean = true) {
    let point1: string = `${startX} ${startY}`;
    let point3: string = `${startX - this.outerRadius * cos(18)} ${startY - (sin(18) - 1) * this.outerRadius}`;
    let point5: string = `${startX - this.outerRadius * cos(54)} ${startY - (-sin(54) - 1) * this.outerRadius}`;
    let point7: string = `${startX + this.outerRadius * cos(54)} ${startY - (-sin(54) - 1) * this.outerRadius}`;
    let point9: string = `${startX + this.outerRadius * cos(18)} ${startY - (sin(18) - 1) * this.outerRadius}`;

    let point2: string =
      `${startX - this.innerRadius * cos(54)} ${startY - this.innerRadius * sin(54) + this.outerRadius}`;
    let point4: string =
      `${startX - this.innerRadius * cos(18)} ${startY + this.innerRadius * sin(18) + this.outerRadius}`;
    let point6: string = `${startX} ${startY + this.innerRadius + this.outerRadius}`;
    let point8: string =
      `${startX + this.innerRadius * cos(18)} ${startY + this.innerRadius * sin(18) + this.outerRadius}`;
    let point10: string =
      `${startX + this.innerRadius * cos(54)} ${startY - this.innerRadius * sin(54) + this.outerRadius}`;
    if (!isHalf) {
      return `M${point1} L${point2} L${point3} L${point4} L${point5} L${point6} L${point7} L${point8} L${point9} L${point10} L${point1} Z`;
    }
    if (isLeft) {
      return `M${point1} L${point2} L${point3} L${point4} L${point5} L${point6}`;
    }
    return `M${point6} L${point7} L${point8} L${point9} L${point10} L${point1} `;
  }

  applyContent(): WrappedBuilder<[ProgressConfiguration]> {
    return wrapBuilder(myProgress);
  }
}

@Builder
function leftStar(config: ProgressConfiguration, value: number) {
  // 绘制左半部分
  Path()
    .width('100px')
    .height('100%')
    .commands((config.contentModifier as MyProgressModifier).paintingPath(100, 0, true, true))
    .fill(config.enabled && config.value >= value ? (config.contentModifier as MyProgressModifier).color :
      '#1A000000')
    .strokeLineCap(LineCapStyle.Round)
    .strokeLineJoin(LineJoinStyle.Round)
    .strokeWidth(0);
}

@Builder
function rightStar(config: ProgressConfiguration, value: number) {
  // 绘制右半部分
  Path()
    .width('100px')
    .height('100%')
    .commands((config.contentModifier as MyProgressModifier).paintingPath(0, 0, true, false))
    .fill(config.enabled && config.value >= value ? (config.contentModifier as MyProgressModifier).color :
      '#1A000000')
    .strokeLineCap(LineCapStyle.Round)
    .strokeLineJoin(LineJoinStyle.Round)
    .strokeWidth(0);
}

@Builder
function myProgress(config: ProgressConfiguration) {
  Column({ space: 30 }) {
    Row() {
      Flex({ justifyContent: FlexAlign.Center }) {
        ForEach((config.contentModifier as MyProgressModifier).idList, (item: string) => {
          leftStar(config, Number(item));
          rightStar(config, Number(item) + 1);
        }, (item: string) => item);
      }
      .width('100%')
      .height(80);
    };
  };

  Text('当前评分：').fontSize(20);
  Text(`${config.value / 2}`).fontSize(20);
}

@Entry
@Component
struct CustomRating {
  @State currentValue: number = 0; // 评分
  modifier = new MyProgressModifier('#F7CE00', 80);
  progressX: number = 0; // 单位vp
  context: UIContext = this.getUIContext();

  build() {
    Column() {
      Progress({ value: this.currentValue, total: 10 })
        .contentModifier(this.modifier) // 自定义评分栏
        .gesture(
          // 滑动手势x发生变化时修改评分
          PanGesture()
            .onActionStart((event: GestureEvent) => {
              this.progressX = event.fingerList[0].localX;
              this.currentValue = this.context.vp2px(this.progressX) / 100;
            })
            .onActionUpdate((event: GestureEvent) => {
              this.progressX = event.fingerList[0].localX;
              this.currentValue = this.context.vp2px(this.progressX) / 100;
            })
        );
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center);
  }
}

function cos(d: number) {
  return Math.cos(d * 3.14 / 180);
}

function sin(d: number) {
  return Math.sin(d * 3.14 / 180);
}
```

## 总结

ContentModifier组件的属性类，用来区别不同组件自定义内容区后所需要的不同信息，支持ButtonConfiguration、CheckBoxConfiguration、DataPanelConfiguration、ProgressConfiguration等，偏向于特定组件自定义定制化，可以根据应用场景灵活运用。
