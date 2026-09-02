---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-677
title: 如何实现自定义UI单选功能
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何实现自定义UI单选功能
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:02+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:40f2df2aa37a64e905e7ca9526fa311b10339bbb4898a36bcac2ab594a3d04f1
---

## 问题现象

实现一个单选组件，要求：①绘制指示图标，②选中项需显示高亮状态。

效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/pgh2B1e6QyCCgQFDE8Q0oQ/zh-cn_image_0000002658914057.png)

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/lNYZA2K7T2OyTwCcCkcLxg/zh-cn_image_0000002658794107.gif "点击放大")

## 背景知识

* [Polygon](../harmonyos-references/ts-drawing-components-polygon.md)：多边形绘制组件。
* [Stack](../harmonyos-references/js-service-widget-container-stack.md)：堆叠容器，子组件按照顺序依次入栈，后一个子组件覆盖前一个子组件。

## 解决方案

采用Stack容器实现层叠布局，通过@State变量控制Polygon绘制的三角形指示图标显示与隐藏状态，结合条件渲染，实现选中时的高亮切换效果。

```ts
@Entry
@Component
struct RadioPage {
  @State select: string = 'SELECT_OPTION_1'; // SELECT_OPTION_1为选项一，SELECT_OPTION_2为选项二

  @Builder
  commonUI(selectValue:string,imageUrl:string,context:string) {
    Stack() {
      Row() {
        Image($r(imageUrl))
          .width(40)
          .height(40)
        Text(context)
      }
      .width(150)
      .padding(5)
      .borderRadius(5)
      .border({ width: 1, color: this.select === selectValue ? '#ff5892de' : '#ffc4cac7' }) // 根据select变量判断选中的border颜色
      .backgroundColor(this.select === selectValue? '#ff5892de' : '#ffc4cac7') // 根据select变量判断选中的backgroundColor颜色
      .justifyContent(FlexAlign.Center)

      if (this.select === selectValue) {
        // 三角形指示图标
        Polygon({ width: 20, height: 20 })
          .points([[10, 10], [15, 0], [20, 10]])
          .fill('#ff5892de')
          .position({ top: -10, left: 10 })
      }
    }
    .onClick(() => {
      this.select = selectValue;
    })
  }

  build() {
    Column() {
      Flex({ justifyContent: FlexAlign.SpaceBetween }) {
        // 选项一
        this.commonUI('SELECT_OPTION_1','app.media.startIcon','选项一');
        // 选项二
        this.commonUI('SELECT_OPTION_2','app.media.startIcon','选项二');
      }
      .padding(10)
      .height(100)
      .width('100%')
    }
  }
}
```
