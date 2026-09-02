---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-701
title: Row组件内Text内容溢出
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > Row组件内Text内容溢出
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:16+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:2dbec1d4d02d1ebfcf56be98fafb4656f7859900f32d6498d6112c6ddd7beb75
---

## 问题现象

Row组件内布局了多个Text组件，其中一个Text组件长度较长，导致后面的组件超出Row组件，内容溢出屏幕，部分Text组件没有展示。

示例代码如下：

```ts
@Entry
@Component
struct Index {
  build() {
    Column() {
      Row({ space: 5 }) {
        Image($r('app.media.startIcon'))
          .width(20)
          .height(20)
        Text('The text component is used to display a piece of textual information.Support universal attributes and universal text attributes.')
          .fontSize(15)
          .maxLines(1)
          .textOverflow({ overflow: TextOverflow.Ellipsis })
        Text('Hello world')
          .fontColor('#999999')
          .borderWidth(1)
          .borderColor('#ff3880ff')
          .borderRadius(2)
          .maxLines(1)
      }
      .height(30)
      .width('100%')
      .backgroundColor('#14000000')
    }
    .padding({left:16,right:16})
    .height('100%')
    .width('100%')
    .justifyContent(FlexAlign.Center)
  }
}
```

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/l7y06ql-S1WCM4WwKC6fuA/zh-cn_image_0000002628394986.png "点击放大")

可以观察到，当第二个子组件为长文本时，后面的其他子组件都无法显示出来。

## 背景知识

* [textOverflow](../harmonyos-references/ts-basic-components-text.md#textoverflow)用于设置文本超长时的显示方式，[TextOverflow](../harmonyos-references/ts-appendix-enums.md#textoverflow).Ellipsis效果是文本超长时显示不下的文本用省略号代替，需要搭配[maxLines](../harmonyos-references/ts-basic-components-text.md#maxlines)属性使用。
* [width](../harmonyos-references/ts-universal-attributes-size.md#width)属性用于设置组件自身的宽度或水平方向布局策略，**缺省时使用元素自身内容需要的宽度**。若子组件的宽大于父组件的宽，则会超出父组件的范围。
* [layoutWeight](../harmonyos-references/ts-universal-attributes-size.md#layoutweight)方法用于设置组件的布局权重，使用该属性的组件在父容器（Row/Column/Flex）的主轴方向按照权重分配尺寸。
* [constraintSize](../harmonyos-references/ts-universal-attributes-size.md#constraintsize)属性用于设置约束尺寸，组件布局时，进行尺寸范围限制。constraintSize的优先级高于width和height。
* [Flex](../harmonyos-references/ts-container-flex.md)是以弹性方式布局子组件的容器组件，提供更加有效的方式对容器内的子元素进行排列、对齐和分配剩余空间。

## 解决方案

上文示例中Row组件虽然设置了第二个Text组件的textOverflow属性和maxLines属性，但是并没有设置width属性，所以导致Text组件超出Row组件的范围。有以下解决方法：

* **方案一**：给长文本子组件设置宽度width。

  ```ts
  @Entry
  @Component
  struct Page1 {
    build() {
      Column() {
        Row({ space: 5 }) {
          Image($r('app.media.startIcon'))
            .width(20)
            .height(20);
          Text('The text component is used to display a piece of textual information.Support universal attributes and universal text attributes.')
            .fontSize(15)
            .width('65%')
            .maxLines(1)
            .textOverflow({ overflow: TextOverflow.Ellipsis });
          Text('Hello world')
            .fontColor('#999999')
            .borderWidth(1)
            .borderColor('#ff3880ff')
            .borderRadius(2)
            .maxLines(1);
        }
        .height(30)
        .width('100%')
        .backgroundColor('#14000000');
      }
      .padding({ left: 16, right: 16 })
      .height('100%')
      .width('100%')
      .justifyContent(FlexAlign.Center);
    }
  }
  ```
* **方案二**：给子组件设置layoutWeight属性来设置组件的布局权重来分配剩余空间，在当前场景下，为保证第二个Text组件能完整显示，采用了5:2的比例进行空间分配。

  ```ts
  @Entry
  @Component
  struct Page2 {
    build() {
      Column() {
        Row({ space: 5 }) {
          Image($r('app.media.startIcon'))
            .width(20)
            .height(20);
          Text('The text component is used to display a piece of textual information.Support universal attributes and universal text attributes.')
            .fontSize(15)
            .maxLines(1)
            .textOverflow({ overflow: TextOverflow.Ellipsis })
            .layoutWeight(5); // 占5/7剩余空间
          Text('Hello world')
            .fontColor('#999999')
            .borderWidth(1)
            .borderColor('#ff3880ff')
            .borderRadius(2)
            .maxLines(1)
            .layoutWeight(2); // 占2/7剩余空间
        }
        .height(30)
        .width('100%')
        .backgroundColor('#14000000');
      }
      .padding({ left: 16, right: 16 })
      .height('100%')
      .width('100%')
      .justifyContent(FlexAlign.Center);
    }
  }
  ```
* **方案三**：通过设置constraintSize属性限制各子组件的最大/最小宽度，保证每个子组件达到预期的显示效果。

  ```ts
  @Entry
  @Component
  struct Page3 {
    build() {
      Column() {
        Row({ space: 5 }) {
          Image($r('app.media.startIcon'))
            .constraintSize({ maxWidth: '10%' })
            .height(20);
          Text('The text component is used to display a piece of textual information.Support universal attributes and universal text attributes.')
            .fontSize(15)
            .maxLines(1)
            .constraintSize({ maxWidth: '65%' })
            .textOverflow({ overflow: TextOverflow.Ellipsis });
          Text('Hello world')
            .fontColor('#999999')
            .borderWidth(1)
            .borderColor('#ff3880ff')
            .borderRadius(2)
            .maxLines(1)
            .constraintSize({ minWidth: '25%' });
        }
        .height(30)
        .width('100%')
        .backgroundColor('#14000000');
      }
      .padding({ left: 16, right: 16 })
      .height('100%')
      .width('100%')
      .justifyContent(FlexAlign.Center);
    }
  }
  ```
* **方案四**：使用calc计算方法来设置组件宽度。

  ```ts
  @Entry
  @Component
  struct Page4 {
    build() {
      Column() {
        Row({ space: 5 }) {
          Image($r('app.media.startIcon'))
            .width(20)
            .height(20);
          Text('The text component is used to display a piece of textual information.Support universal attributes and universal text attributes.')
            .fontSize(15)
            .fontColor(Color.Black)
            .maxLines(1)
            .width('calc(100% - 100vp - 20vp)') // 父组件宽度减去另外两个子组件宽度
            .textOverflow({ overflow: TextOverflow.Ellipsis });
          Text('Hello world')
            .fontColor('#999999')
            .borderWidth(1)
            .borderColor('#ff3880ff')
            .borderRadius(2)
            .maxLines(1);
        }
        .height(30)
        .width('100%')
        .backgroundColor('#14000000');
      }
      .padding({ left: 16, right: 16 })
      .height('100%')
      .width('100%')
      .justifyContent(FlexAlign.Center);
    }
  }
  ```
* **方案五**：改用Flex布局，通过设置FlexWrap.NoWrap可以让Flex容器的子组件尽可能约束在容器内。

  ```ts
  import { LengthMetrics } from '@kit.ArkUI';

  @Entry
  @Component
  struct Page5 {
    build() {
      Column() {
        Flex({ wrap: FlexWrap.NoWrap, alignItems: ItemAlign.Center, space: { main: LengthMetrics.px(10) } }) {
          Image($r('app.media.startIcon'))
            .width(22)
            .height(20);
          Text('The text component is used to display a piece of textual information.Support universal attributes and universal text attributes.')
            .fontSize(15)
            .maxLines(1)
            .textOverflow({ overflow: TextOverflow.Ellipsis })
            .layoutWeight(1);
          Text('Hello world')
            .fontColor('#999999')
            .borderWidth(1)
            .borderColor('#ff3880ff')
            .borderRadius(2)
            .maxLines(1);
        }
        .height(30)
        .width('100%')
        .backgroundColor('#14000000');
      }
      .padding({ left: 16, right: 16 })
      .height('100%')
      .width('100%')
      .justifyContent(FlexAlign.Center);
    }
  }
  ```

## 总结

| 方案 | 优点 | 缺点 |
| --- | --- | --- |
| 人为限制宽度width | 尺寸控制准确。 | * 需要手动调试。 * 只能适应当前分辨率。 |
| layoutweight按比例划分 | 动态分配剩余空间。 | 仅在父容器主轴方向存在剩余空间时生效。 |
| constraintSize尺寸限制 | 尺寸控制准确并且无需手动调试。 | 只能约束该组件自身尺寸范围，需要多次使用。 |
| calc计算 | 通过计算得到组件的宽度，尺寸控制准确并且无需手动调试。 | 需要知道其他子组件的宽度。 |
| 使用Flex布局 | 系统自行分配空间，无需手动调试。 | * 无法保证各组件完整度。 * 改变了布局。 |

## 常见FAQ

Q：此场景下可以使用文本计算能力吗？

A：经过测试不能，此场景为文本过长时用省略号，文本计算方法[measureText](../harmonyos-references/arkts-apis-uicontext-measureutils.md#measuretext12)会计算出文本的总长度，不适用于当前场景。
