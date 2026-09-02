---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1545
title: 如何使用layoutWeight属性设置子元素尺寸权重
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何使用layoutWeight属性设置子元素尺寸权重
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:11+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ed9e7145c53504d2d6af57f5c0e1994eabc8a6f1b0ecab410268eb372ab7faef
---

## 问题现象

如何使子组件按一定比例在父容器中进行尺寸分配？

## 背景知识

[layoutWeight](../harmonyos-references/ts-universal-attributes-size.md#layoutweight)(value: number | string)：设置组件的布局权重，使组件在父容器（Row/Column/Flex）的主轴方向按照权重分配尺寸。

* 父容器尺寸确定时，不设置layoutWeight属性或者layoutWeight属性生效值为0的元素优先占位，这些元素占位后在主轴留下的空间称为主轴剩余空间。设置了layoutWeight属性且layoutWeight属性生效值大于0的子元素会从主轴剩余空间中按照各自所设置的权重占比分配尺寸，分配时会忽略元素本身的尺寸设置。
* 仅在Row/Column/Flex布局中生效。
* 如果容器中有子元素设置了layoutWeight属性，且设置的属性值大于0，则所有子元素不会再基于flexShrink和flexGrow布局。

## 解决方案

通过[layoutWeight](../harmonyos-references/ts-universal-attributes-size.md#layoutweight)属性动态调整子元素尺寸占比的核心容器，适用于需要灵活布局的场景，下列方案以[Row](../harmonyos-references/ts-container-row.md)、[Column](../harmonyos-references/ts-container-column.md)为例，分别展示水平和竖直方向上layoutWeight的分配方法。

* Row容器：**水平布局**（从左到右），通过layoutWeight设置子元素在**水平方向**的占比。

  ```ts
  @Entry
  @Component
  struct BottomWithBar {
    build() {
      Column() {
        Row() {
          Row() {
            Text('左侧');
          }
          .justifyContent(FlexAlign.Center)
          .height('50%') // 因为是Row()组件。所以设置高度以便观察
          .backgroundColor('#F1F3F5')
          .layoutWeight(2); // 占据2/3宽度
          Row() {
            Text('右侧');
          }
          .justifyContent(FlexAlign.Center)
          .height('50%') // 因为是Row()组件。所以设置高度以便观察
          .backgroundColor('#E5E5EA')
          .layoutWeight(1); // 占据1/3宽度
        };
      }
      .width('100%')
      .height('100%');
    }
  }
  ```

  效果图：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/8M0zNtbGSnmoNR-LpUc3Mw/zh-cn_image_0000002628609224.png "点击放大")
* Column容器：**垂直布局**（从上到下），通过layoutWeight设置子元素在**垂直方向**的占比。

  ```ts
  @Entry
  @Component
  struct BottomWithBar2 {
    build() {
      Column() {
        Column() {
          Row() {
            Text('顶部');
          }
          .justifyContent(FlexAlign.Center)
          .width('50%') // 因为是Column()组件。所以设置宽度以便观察
          .backgroundColor('#F1F3F5')
          .layoutWeight(1); // 占据1/2高度
          Row() {
            Text('底部');
          }
          .justifyContent(FlexAlign.Center)
          .width('50%') // 因为是Column()组件。所以设置宽度以便观察
          .backgroundColor('#E5E5EA')
          .layoutWeight(1); // 占据1/2高度
        };
      }
      .width('100%')
      .height('100%');
    }
  }
  ```

  效果图：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/UFBDsRhgQdSHozRnvtMC7A/zh-cn_image_0000002628769122.png "点击放大")

## 常见FAQ

Q：如何指定组件到屏幕边缘的距离。例如：Row容器中存在左侧Text，右侧TextInput两个子组件，要求左侧Text组件宽度固定，右侧TextInput宽度自适应，并且Text组件距离左边屏幕边缘和TextInput组件距离右侧屏幕边缘的距离均为16vp。

A：将Row组件的宽度设为屏幕宽度，左右内边距为16vp，Text设为固定宽度，TextInput添加layoutWeight属性即可。

示例代码如下：

```ts
@Entry
@Component
struct Index3 {
  controller: TextInputController = new TextInputController();

  build() {
    Row({ space: 16 }) {
      Text('示例文本')
        .textAlign(TextAlign.Center)
        .backgroundColor('#F1F3F5')
        .borderRadius(20)
        .height(40)
        .width(80)
        .font({ size: 16, weight: 500 })
        .fontColor('#182431');

      TextInput({ placeholder: 'input your word...', controller: this.controller })
        .placeholderColor(Color.Grey)
        .placeholderFont({ size: 14, weight: 400 })
        .caretColor(Color.Blue)
        .layoutWeight(1);
    }
    .padding({ left: 16, right: 16 })
    .height('100%')
    .width('100%')
    .justifyContent(FlexAlign.Center);
  };
}
```
