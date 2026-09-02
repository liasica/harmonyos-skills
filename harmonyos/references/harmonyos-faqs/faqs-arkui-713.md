---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-713
title: 实现多个长度不一的子组件中间组件居中显示的功能
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 实现多个长度不一的子组件中间组件居中显示的功能
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:17+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f51004d35fcf09d6bbb0315d31939240a822399f509a17002ae226c0c26727de
---

## 问题现象

Row组件内采用两端对齐，中间的组件不居中，如何实现中间的组件居中显示的功能？

问题代码示例参考如下：

```ts
@Entry
@Component
struct RowPageOne {
  build() {
    Row() {
      Image($r('app.media.background'))
        .width(16)
      Text('公交线路查询')
        .fontSize(16)
        .fontColor('#333333')
        .fontWeight(FontWeight.Medium)
      Text('一段长文本')
    }
    .width('100%')
    .margin({ bottom: 17 })
    .justifyContent(FlexAlign.SpaceBetween)
  }
}
```

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/nINXnLjYSymuexJWTOGaCw/zh-cn_image_0000002658914223.png "点击放大")

## 背景知识

* [Stack组件](../harmonyos-references/ts-container-stack.md)：堆叠容器，子组件按照顺序依次入栈，后一个子组件覆盖前一个子组件。
* [FlexAlign](../harmonyos-references/ts-appendix-enums.md#flexalign)：该参数能通过[justifyContent](../harmonyos-references/ts-container-row.md#justifycontent8)属性设置子组件的对齐属性。对SpaceBetween、SpaceAround和SpaceEvenly三种对齐方式的理解。

| 对齐方式 | 区别 | 效果 |
| --- | --- | --- |
| SpaceBetween | 所有子元素沿主轴方向均匀分配，第一个子元素和最后一个子元素与父元素两端对齐，相邻元素之间分隔距离相同。 |  |
| SpaceAround | 所有子元素沿主轴方向均匀分配，各子元素两端分隔距离相同。 |  |
| SpaceEvenly | 所有子元素沿主轴方向等间距布局，相邻子元素之间的间距、第一个子元素和最后一个子元素与父元素两端间距均相等。 |  |

* [layoutWeight](../harmonyos-references/ts-universal-attributes-size.md#layoutweight)：该通用属性可以设置子组件占父组件剩余空间的比例，例如父组件总高度130vp，已经被占据了30vp的情况下，剩下的组件可以通过该属性中参数的值按比例分配剩下的空间。

## 问题定位

FlexAlign.SpaceBetween：Flex主轴方向均匀分配弹性元素，相邻元素之间距离相同。第一个元素与行首对齐，最后一个元素与行尾对齐。该方式会使子组件之间间距相等，当其子组件长度不一致时，并不能实现居中显示的效果。

## 分析结论

由于子组件长度不一致，所以FlexAlign.SpaceBetween无法实现中间组件居中显示的效果。

## 修改建议

* **方案一**：通过Stack组件将需要对齐的子组件单独居中布局，其它子组件两端布局。

  ```ts
  @Entry
  @Component
  struct OptionOne {
    build() {
      Stack() {
        // 其它子组件两端布局
        Row() {
          Image($r('app.media.startIcon'))
            .width(16);
          Text('A');
        }
        .width('100%')
        .justifyContent(FlexAlign.SpaceBetween);

        // 单独居中布局，此处Stack组件默认顶部居中
        Text('公交线路查询')
          .fontSize(16)
          .fontColor('#333333')
          .fontWeight(FontWeight.Medium);
      }
      .height('100%');
    }
  }
  ```
* **方案二**：每个子组件单独用Row/Column等组件封装，并通过width/layoutWeight属性设置两端百分比宽度。

  ```ts
  @Entry
  @Component
  struct OptionTwo {
    build() {
      Column() {
        Row() {
          Row() {
            Image($r('app.media.startIcon'))
              .width(16);
          }
          .justifyContent(FlexAlign.Start)
          .layoutWeight(5); // 父组件剩余部分占据一半的宽度
          Text('公交线路查询')
            .fontSize(16)
            .fontColor('#333333')
            .textAlign(TextAlign.Center) // 文本居中显示
            .width('80%') // 限制Text文本宽度避免挤占其它组件空间
            .fontWeight(FontWeight.Medium);
          Row() {
            Text('A');
          }
          .justifyContent(FlexAlign.End)
          .layoutWeight(5); // 父组件剩余部分占据一半的宽度
        }
        .width('100%')
        .margin({ bottom: 17 })
        .justifyContent(FlexAlign.Center);
      }
      .height('100%')
      .justifyContent(FlexAlign.Center);
    }
  }
  ```
* **方案三**：使用RelativeContainer相对布局，单独通过[alignRules](../harmonyos-references/ts-universal-attributes-location.md#alignrules9)属性设置每个子组件布局位置。

  ```ts
  @Entry
  @Component
  struct OptionThree {
    build() {
      RelativeContainer() {
        Image($r('app.media.startIcon'))
          .width(16)
          .id('img')
          .alignRules({
            top: { anchor: '__container__', align: VerticalAlign.Center },
            left: { anchor: '__container__', align: HorizontalAlign.Start }
          });
        Row() {
          Text('公交线路查询')
            .fontSize(16)
            .fontColor('#333333')
            .fontWeight(FontWeight.Medium);
        }
        .alignRules({
          top: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .id('title');

        Text('A')
          .id('text')
          .alignRules({
            top: { anchor: '__container__', align: VerticalAlign.Center },
            right: { anchor: '__container__', align: HorizontalAlign.End }
          });
      }
      .height('100%')
      .width('100%')
      .margin({ bottom: 17 });
    }
  }
  ```

## 总结

| 方案 | 优缺点 | 适用场景 |
| --- | --- | --- |
| 方案一、方案三 | 该方式子组件过长时会导致文字图标重叠现象。 | 适用于文本较短场景。 |
| 方案二 | 该方式两端组件的百分比宽度必须相等，当文本较长时不会出现重叠现象。 | 长/短文本场景均适用。 |

综上所述，若文本长度不确定时，推荐使用方案二实现居中功能。
