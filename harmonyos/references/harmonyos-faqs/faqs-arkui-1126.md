---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1126
title: List展示不全
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > List展示不全
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:54+08:00
doc_updated_at: 2026-08-26
content_hash: sha256:6f98e0105d5eaaf48db1a2e20a04a79d49021a01d3da87b912aa0b82a96aeab7
---

## 问题现象

List组件与其他组件同级并且List子组件总尺寸超过List父组件尺寸时，会导致ListItem部分内容顶出父组件显示区域外，上滑至底部时其内容展示不全。问题代码如下：

```ts
@Entry
@Component
struct ListDisplay {
  build() {
    Column() {
      Text('我是一级容器Column的Text组件')
        .fontSize(18)
        .width('100%')
        .height(200)
        .textAlign(TextAlign.Center)
        .backgroundColor('#ffdfe2e2');
      List() {
        ForEach([1, 2, 3, 4, 5, 6, 7], (item: number) => {
          ListItem() {
            Row() {
              Text(item + '').fontSize(18);
            }
            .width('92%')
            .height(200)
            .justifyContent(FlexAlign.Center)
            .backgroundColor('#ffdfe2e2')
            .margin({ top: 16, right: 16, left: 16 })
            .borderRadius(10);
          };
        });
      }.scrollBar(BarState.Off);
    }
    .height('100%')
    .width('100%');
  }
}
```

问题效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/_o0b_y14TEerWC07nWrGjw/zh-cn_image_0000002719103535.png "点击放大")

## 背景知识

* [height](../harmonyos-references/ts-universal-attributes-size.md#height)：用于设置组件自身的高度，缺省时使用元素自身内容需要的高度。若子组件的高大于父组件的高，则会超出父组件的范围。
* [margin](../harmonyos-references/ts-universal-attributes-size.md#margin)：用于设置组件的外边距属性。
* [layoutWeight](../harmonyos-references/ts-universal-attributes-size.md#layoutweight)：用于设置组件的布局权重，使组件在父容器（Row/Column/Flex）的主轴方向按照权重分配尺寸。父容器尺寸确定时，不设置layoutWeight属性或者layoutWeight属性生效值为0的元素优先占位，这些元素占位后在主轴留下的空间称为主轴剩余空间。设置了layoutWeight属性且layoutWeight属性生效值大于0的子元素会从主轴剩余空间中按照各自所设置的权重占比分配尺寸，分配时会忽略元素本身的尺寸设置。
* [Flex](../harmonyos-references/ts-container-flex.md)组件：是以弹性方式布局子组件的容器组件，提供更加有效的方式对容器内的子元素进行排列、对齐和分配剩余空间。
* [contentStartOffset](../harmonyos-references/ts-container-list.md#contentstartoffset11)：设置内容区域起始偏移量。
* [contentEndOffset](../harmonyos-references/ts-container-list.md#contentendoffset11)：设置内容区末尾偏移量。

## 问题定位

1. 首先观察到List组件未设置高度，根据height属性说明：**height缺省时使用元素自身内容需要的高度**。所以List组件高度为子组件之和200vp\*7。
2. 之后根据官网List指南的[约束](../harmonyos-guides/arkts-layout-development-create-list.md#约束)得知，当子组件主轴方向总尺寸超过List父组件尺寸时，List主轴方向尺寸适应List的父组件尺寸，而200vp\*7>父组件高度100%，所以List组件高度为屏幕高度，示意图如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/4yfb5grfR0Kl3FMB7fmqyA/zh-cn_image_0000002689385794.png "点击放大")
3. 再然后根据layoutWeight布局说明：**不设置layoutWeight属性或者layoutWeight属性生效值为0的元素优先占位**。所以List组件会在剩余空间内占位，导致List组件被下压，下压后List组件就有部分区域会超过当前屏幕高度，所以造成List展示不全现象。
4. 最后可以利用ArkUI Inspector可以看到List组件超出屏幕范围，超出的距离刚好是上面Text组件占据高度200vp：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/XlyWlf4hQlCt3L9YrCC0Dg/zh-cn_image_0000002719105259.png "点击放大")

## 分析结论

当List组件上面有其他元素并且List子组件高度之和超出屏幕范围时，会导致List组件被下压，造成List展示不全的问题。

## 修改建议

* **方案一：给List组件设置高度。**

  设置固定高度以后List组件就会在限定的范围内滑动，比如设置300vp后List组件就在300vp内进行滑动：

  ```ts
  @Entry
  @Component
  struct ListDisplayOne {
    build() {
      Column() {
        Text('我是一级容器Column的Text组件')
          .fontSize(18)
          .width('100%')
          .height(200)
          .textAlign(TextAlign.Center)
          .backgroundColor('#ffdfe2e2')
        List() {
          ForEach([1, 2, 3, 4, 5, 6, 7], (item: number) => {
            ListItem() {
              Row() {
                Text(item + '').fontSize(18);
              }
              .width('92%')
              .height(200)
              .justifyContent(FlexAlign.Center)
              .backgroundColor('#ffdfe2e2')
              .margin({ top: 16, right: 16, left: 16 })
              .borderRadius(10);
            };
          });
        }.scrollBar(BarState.Off).height(300)
      }
      .height('100%')
      .width('100%');
    }
  }
  ```

  **说明** 

  上文300vp只是演示效果，具体数值看业务需要；若height值超过剩余屏幕高度，比如1000vp，则设置无效。

  或者利用calc特性计算List组件在主轴方向剩余高度：

  ```ts
  @Entry
  @Component
  struct ListDisplayTwo {
    build() {
      Column() {
        Text('我是一级容器Column的Text组件')
          .fontSize(18)
          .width('100%')
          .height(200)
          .textAlign(TextAlign.Center)
          .backgroundColor('#ffdfe2e2')
        List() {
          ForEach([1, 2, 3, 4, 5, 6, 7], (item: number) => {
            ListItem() {
              Row() {
                Text(item + '').fontSize(18);
              }
              .width('92%')
              .height(200)
              .justifyContent(FlexAlign.Center)
              .backgroundColor('#ffdfe2e2')
              .margin({ top: 16, right: 16, left: 16 })
              .borderRadius(10);
            };
          });
        }.scrollBar(BarState.Off).height('calc(100% - 200vp)')
      }
      .height('100%')
      .width('100%')
    }
  }
  ```

  **说明** 

  calc公式中200vp的高度为List上面Text组件的高度。

* **方案二：给List组件设置layoutWeight属性。**

  在主轴剩余空间内，设置了layoutWeight属性的子元素与兄弟元素会在主轴方向按照权重分配尺寸。给List组件设置layoutWeight属性即可：

  ```ts
  @Entry
  @Component
  struct ListDisplayThree {
    build() {
      Column() {
        Text('我是一级容器Column的Text组件')
          .fontSize(18)
          .width('100%')
          .height(200)
          .textAlign(TextAlign.Center)
          .backgroundColor('#ffdfe2e2')
        List() {
          ForEach([1, 2, 3, 4, 5, 6, 7], (item: number) => {
            ListItem() {
              Row() {
                Text(item + '').fontSize(18)
              }
              .width('92%')
              .height(200)
              .justifyContent(FlexAlign.Center)
              .backgroundColor('#ffdfe2e2')
              .margin({ top: 16, right: 16, left: 16 })
              .borderRadius(10);
            };
          });
        }.scrollBar(BarState.Off).layoutWeight(1)

      }
      .height('100%')
      .width('100%')
    }
  }
  ```

  **说明** 

  以上场景Text组件后面只有List组件，故layoutWeight设置无论何值都行，不过一般都会设置成layoutWeight(1)。

* **方案三：给List组件设置margin属性。**

  利用ArkUI Inspector可以看到List组件超出屏幕范围，超出的距离刚好是上面Text组件占据高度200vp。而margin属性就是用于设置组件的外边距，所以给List组件设置margin底部200vp即可：

  ```ts
  @Entry
  @Component
  struct ListDisplayFour {
    build() {
      Column() {
        Text('我是一级容器Column的Text组件')
          .fontSize(18)
          .width('100%')
          .height(200)
          .textAlign(TextAlign.Center)
          .backgroundColor('#ffdfe2e2')
        List() {
          ForEach([1, 2, 3, 4, 5, 6, 7], (item: number) => {
            ListItem() {
              Row() {
                Text(item + '').fontSize(18);
              }
              .width('92%')
              .height(200)
              .justifyContent(FlexAlign.Center)
              .backgroundColor('#ffdfe2e2')
              .margin({ top: 16, right: 16, left: 16 })
              .borderRadius(10);
            };
          });
        }.scrollBar(BarState.Off).margin({ bottom: 200 })

      }
      .height('100%')
      .width('100%')
    }
  }
  ```

* **方案四：使用Flex布局。**

  Flex组件提供更加有效的方式对容器中的子元素进行排列、对齐和分配剩余空间，设置FlexWrap.NoWrap即可让子元素尽可能约束在容器内：

  ```ts
  @Entry
  @Component
  struct ListDisplayFive {
    build() {
      Flex({ wrap: FlexWrap.NoWrap, alignItems: ItemAlign.Center, direction: FlexDirection.Column }) {
        Text('我是一级容器Column的Text组件')
          .fontSize(18)
          .width('100%')
          .height(200)
          .textAlign(TextAlign.Center)
          .backgroundColor('#ffdfe2e2')
        List() {
          ForEach([1, 2, 3, 4, 5, 6, 7], (item: number) => {
            ListItem() {
              Row() {
                Text(item + '').fontSize(18)
              }
              .width('92%')
              .height(200)
              .justifyContent(FlexAlign.Center)
              .backgroundColor('#ffdfe2e2')
              .margin({ top: 16, right: 16, left: 16 })
              .borderRadius(10);
            };
          });
        }.scrollBar(BarState.Off);
      }
      .height('100%')
      .width('100%')
    }
  }
  ```
* **方案五：给List组件设置contentEndOffset属性。**

  设置内容区域末尾偏移量。

  ```ts
  @Entry
  @Component
  struct ListDisplaySix {
    build() {
      Column() {
        Text('我是一级容器Column的Text组件')
          .fontSize(18)
          .width('100%')
          .height(200)
          .textAlign(TextAlign.Center)
          .backgroundColor('#ffdfe2e2')
        List() {
          ForEach([1, 2, 3, 4, 5, 6, 7], (item: number) => {
            ListItem() {
              Row() {
                Text(item + '').fontSize(18)
              }
              .width('92%')
              .height(200)
              .justifyContent(FlexAlign.Center)
              .backgroundColor('#ffdfe2e2')
              .margin({ top: 16, right: 16, left: 16 })
              .borderRadius(10);
            };
          });
        }.scrollBar(BarState.Off).contentStartOffset(0).contentEndOffset(200)
      }
      .height('100%')
      .width('100%')
    }
  }
  ```

  以上方案均可修复List展示不全问题，修正效果如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/ULs_nYLyQ7GEKZW1dtCFjg/zh-cn_image_0000002689396764.png "点击放大")

## 常见FAQ

Q：List组件被父容器组件包裹，父容器组件有同级组件时，单纯给List设置layoutWeight不生效该如何解决？

A：这是由于没有给List的父组件设置高度所致，给父容器也加上layoutWeight即可。

Q：calc(100%-\${DefParam.topRectHeight + DefParam.bottomRectHeight+56})，使用以上方法计算高度时，获取的高度异常。

A：calc中的参数需统一单位计算，其中的56未明确单位，会导致单位不统一。修正如下：

calc(100% - ${DefParam.topRectHeight + DefParam.bottomRectHeight}vp - 56vp)。

Q：List组件高度被动态压缩时，如何保持最新的ListItem可见？

A：可以使用[contentStartOffset](../harmonyos-references/ts-container-list.md#contentstartoffset11)属性设置内容区域起始偏移量，将偏移值设置为新增组件的高度，使List滚动到对应位置，确保最新的ListItem保持可见。

## 总结

List组件由于其滚动特性一般不会设置其高度，而当List在父容器内有其他兄弟节点处于上方并且List组件高度超出屏幕范围时，就会造成List展示不全问题，本文提供五种方案进行解决，五种方案对比如下，开发者可以自行根据对比进行选择：

| 方案 | 原理 | 场景说明 |
| --- | --- | --- |
| 设置height | 约束List组件的高度 | 固定高度会限制List只能在有限范围内展示，根据实际业务需要；利用calc计算设置动态高度等同于layoutWeight效果，但需要获悉上面节点的高度使用较为麻烦 |
| 设置layoutWeight | 在主轴剩余空间内分配List尺寸 | 应用场景最多，使用最方便，推荐使用 |
| 设置margin | 设置List组件的外边距 | 需要获悉上面节点的高度，有其他方向margin设置需求时可以搭配使用；若下方还有节点则会设置失败，局限性较大 |
| 使用Flex布局 | 利用弹性布局特性 | FlexWrap.NoWrap不换行时List默认能展示完全；FlexWrap.Wrap换行时必须搭配height属性使用，否则List内容会向右溢出 |
| 设置contentEndOffset属性 | 设置内容区偏移量 | 列表滚动到末尾位置时，列表内容与列表显示区域边界保留指定距离 |
