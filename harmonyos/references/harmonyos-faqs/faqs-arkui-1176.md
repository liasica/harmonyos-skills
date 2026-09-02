---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1176
title: 如何解决页面上大量动效组件导致页面卡顿的问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何解决页面上大量动效组件导致页面卡顿的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:07+08:00
doc_updated_at: 2026-08-27
content_hash: sha256:c7bdb9040f6af927579e6da9842cefc760412ee8ce629a3436d913c56098588d
---

## 问题现象

页面上存在大量动效组件时，由于频繁的重绘或复杂的渲染操作，导致帧率下降，出现丢帧现象，影响用户体验。如何解决该问题？

问题代码示例参考如下：

```ts
@Entry
@Component
struct Index {
  @State imageAngle: number = 0
  arr: number[] = Array.from(Array(100), (item: number) => {
    return item
  })
  // 定义动画组件
  @Builder
  windmill() {
    Stack() {
      Image($r('app.media.startIcon')).width(50).height(50) // 'app.media.startIcon'仅作示例，请替换为实际使用的资源
        .rotate({ z: 1, angle: this.imageAngle })
          // 旋转动画
        .onAppear(() => {
          this.getUIContext().animateTo({
            duration: 1000,
            curve: Curve.Linear,
            iterations: -1
          }, () => {
            this.imageAngle = 3600
          })
        })
    }
  }

  build() {
    Column() {
      // 使用网格布局，循环渲染动画组件。
      Grid() {
        ForEach(this.arr, () => {
          GridItem() {
            this.windmill()
          }
        })
      }.columnsTemplate('1fr 1fr 1fr 1fr 1fr')
    }
    .height('100%')
    .width('100%')
  }
}
```

## 背景知识

[renderGroup](../harmonyos-guides/arkts-animation-usage-guide.md#使用rendergroup)是组件通用方法，它代表了渲染绘制的一个组合。其核心功能就是标记组件，在绘制阶段将组件和其子组件的绘制结果进行合并并缓存，以达到复用的效果，从而降低绘制负载。

## 解决方案

页面上存在大量动效组件时，使用renderGroup解决卡顿，提升动画性能。启用renderGroup后，在绘制阶段将组件和其子组件的绘制结果进行合并并缓存，以达到复用的效果，从而降低绘制负载，优化渲染性能。

1. 为了满足renderGroup属性的设置要满足父组件统一应用动效，子组件无动效的限制，将动效在父组件上统一实现。

   ```ts
   Stack() {
     Image($r('app.media.startIcon')).width(50).height(50); // 'app.media.startIcon'仅作示例，请替换为实际使用的资源
   }
   // 实现旋转效果
   .rotate({ z: 1, angle: this.imageAngle })
   // 父组件统一应用动效
   .onAppear(() => {
     this.getUIContext().animateTo({
       duration: 5000,
       curve: Curve.Linear,
       iterations: -1
     }, () => {
       this.imageAngle = 3600;
     });
   })
   ```
2. 在最外层Stack组件上开启renderGroup属性，实现绘制结果进行合并并缓存，以达到复用。

   ```ts
   // 开启renderGroup属性
   .renderGroup(true);
   ```
3. 使用网格布局，循环渲染动画组件。

   ```ts
   Grid() {
     ForEach(this.arr, () => {
       GridItem() {
         this.windmill();
       }
     })
   }.columnsTemplate('1fr 1fr 1fr 1fr 1fr');
   ```
4. 完整示例参考如下：

   ```screen
   @Entry
   @Component
   struct AnimatedRotations {
     @State imageAngle: number = 0;
     arr: number[] = Array.from(Array(100), (item: number) => {
       return item;
     });

     @Builder
     windmill() {
       Stack() {
         Image($r('app.media.startIcon')).width(50).height(50); // 'app.media.startIcon'仅作示例，请替换为实际使用的资源
       }
       // 实现旋转效果
       .rotate({ z: 1, angle: this.imageAngle })
       // 父组件统一应用动效
       .onAppear(() => {
         this.getUIContext().animateTo({
           duration: 5000,
           curve: Curve.Linear,
           iterations: -1
         }, () => {
           this.imageAngle = 3600;
         });
       })
       // 开启renderGroup属性
       .renderGroup(true);
     };

     build() {
       Column() {
         // 使用网格布局，循环渲染动画组件。
         Grid() {
           ForEach(this.arr, () => {
             GridItem() {
               this.windmill();
             }
           })
         }.columnsTemplate('1fr 1fr 1fr 1fr 1fr');
       }
       .height('100%')
       .width('100%')
     }
   }
   ```

   效果对比如下：

   |  | 优化前 | 优化后 |
   | --- | --- | --- |
   | 丢帧数与卡顿 |  |  |

## 常见FAQ

Q：开启renderGroup配置后，页面卡顿效果未解决，可能是什么原因？

A：为了能使renderGroup功能生效，组件存在以下约束：

* 组件内容固定不变：父组件和其子组件各属性保持固定，不发生变化。
* 子组件无动效：由父组件统一应用动效，其子组件均无动效。
