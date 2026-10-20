---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkui-uimana-faq-0004
title: ArkUI-Row组件布局问题排查
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 常见问题 > ArkUI-Row组件布局问题排查
category: harmonyos-faqs
scraped_at: 2026-10-21T07:11:09+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:32bb1431f6774e9bc7425a139ac63e1d5580a623ba4581d559d0d9996b5f89b5
---

**Q：Row组件内布局了多个Text组件，其中一个Text组件长度较长，导致后面的组件超出Row组件，内容溢出屏幕，部分Text组件没有展示。示例代码如下：**

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/r68QL4EdSF-1gUmb3P8pyQ/zh-cn_image_0000002793760225.png "点击放大")

可以观察到，当第二个子组件为长文本时，后面的其他子组件都无法显示出来。

**A**：上文示例中Row组件虽然设置了第二个Text组件的textOverflow属性和maxLines属性，但是并没有设置width属性，所以导致Text组件超出Row组件的范围。有以下解决方法：

* 方案一：给长文本子组件设置宽度width。

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
* 方案二：给子组件设置layoutWeight属性来设置组件的布局权重来分配剩余空间，在当前场景下，为保证第二个Text组件能完整显示，采用了5：2的比例进行空间分配。

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
* 方案三：通过设置constraintSize属性限制各子组件的最大/最小宽度，保证每个子组件达到预期的显示效果。

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
* 方案四：使用calc计算方法来设置组件宽度。

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
* 方案五：改用Flex布局，通过设置FlexWrap.NoWrap可以让Flex容器的子组件尽可能约束在容器内。

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

**Q：此场景下可以使用文本计算能力吗？**

**A**：经过测试不能，此场景为文本过长时用省略号，文本计算方法[measureText](../harmonyos-references/arkts-apis-uicontext-measureutils.md#measuretext12)会计算出文本的总长度，不适用于当前场景。

**Q：Row组件中存放一个Text组件和一个TextInput组件，给Row组件设置padding并未生效，该如何解决？问题代码如下：**

```ts
@Entry
@Component
struct PageOne {
  build() {
    Column() {
      Row() {
        Text('文本');
        TextInput({ placeholder: '输入' })
          .maxLines(3)
          .type(InputType.Password)
          .height(40)
          .backgroundColor('#DFE1E3');
      }
      .height(60)
      .margin({ left: 16, right: 16 })
      .padding({ left: 20, right: 20 })
      .backgroundColor('#EBEDEF');
    }
    .width('100%')
    .height('100%');
  }
}
```

问题效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/S5_GczyHRX6y8Ar5rYtZWg/zh-cn_image_0000002793680765.png "点击放大")

**A**：针对padding属性未生效问题，给TextInput组件设置layoutWeight(1)属性即可。详情请参考如下示例代码：

```ts
@Entry
@Component
struct PageTwo {
  build() {
    Column() {
      Row() {
        Text('文本');
        TextInput({ placeholder: '输入' })
          .maxLines(3)
          .type(InputType.Password)
          .height(40)
          .backgroundColor('#DFE1E3')
          .layoutWeight(1);
      }
      .height(60)
      .margin({ left: 16, right: 16 })
      .padding({ left: 20, right: 20 })
      .backgroundColor('#EBEDEF');
    }
    .width('100%')
    .height('100%');
  }
}
```

效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/dXWGiFG6RrGAgWKbXodqJQ/zh-cn_image_0000002764442424.png "点击放大")
