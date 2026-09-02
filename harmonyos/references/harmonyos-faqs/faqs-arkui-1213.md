---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1213
title: 利用Flex布局实现子项的展开与折叠
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 利用Flex布局实现子项的展开与折叠
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:07+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f28b30f79f420e19433867aebfd98eecb2f107e0ef6dd5e6bd2242133a2644e8
---

## 问题现象

如何让Flex布局可以折叠与展开？场景如下：Flex可以设置折叠时显示的行数。当子组件布局会超过设置的行数时，按照设置的行数展示，并且可以通过展开/折叠按钮控制Flex展示部分或全部子组件；当子组件布局行数未超过设置的行数时，按照子组件当前布局行数展示，并且不显示展开/折叠按钮。

## 背景知识

* [Flex](../harmonyos-references/ts-container-flex.md)是以弹性方式布局子组件的容器组件，提供更加有效的方式对容器内的子元素进行排列、对齐和分配剩余空间。
* [aboutToAppear](../harmonyos-references/ts-custom-component-lifecycle.md#abouttoappear)生命周期函数在创建自定义组件的新实例后，在执行其build()函数之前执行。
* [constraintSize](../harmonyos-references/ts-universal-attributes-size.md#constraintsize)方法设置约束尺寸，组件布局时，进行尺寸范围限制。
* [measureText](../harmonyos-references/arkts-apis-uicontext-measureutils.md#measuretext12)用于计算指定文本的宽度。
* [display.getDefaultDisplaySync](../harmonyos-references/js-apis-display.md#displaygetdefaultdisplaysync9)获取当前默认的display对象。[display](../harmonyos-references/js-apis-display.md#display)屏幕实例。描述display对象的属性和方法。
* [clip](../harmonyos-references/ts-universal-attributes-sharp-clipping.md#clip18)可设置对子组件超出当前组件范围外的区域进行裁剪。设置为true时超出部分将不会显示。

## 解决方案

* 方案一：设置Flex组件的高度控制显示的部分，并通过clip裁剪多余子项实现展开与折叠。
  1. 通过子组件高度、Flex的属性、以及折叠状态下展示的行数计算，获取折叠状态下Flex组件的高度；
  2. 通过屏幕宽度计算Flex组件宽，从而得到每一行Flex组件布局时的可用宽度，使用measureText方法计算文本宽度，获取子组件宽度；
  3. 根据子组件占用的行数进行判断是否展示展开/折叠按钮。当子组件折叠时按照1中得到的高度设置Flex高度，展开时高度设置为'auto'，实现展开/折叠。

  完整代码如下：

  ```ts
  import { display, LengthMetrics, MeasureUtils } from '@kit.ArkUI';

  @Component
  struct TextItem {
    @Prop text: string;

    build() {
      Text(this.text)
        .textAlign(TextAlign.Center)
        .maxLines(1)
        .height(30) // 文本框高度30
        .padding({ left: 8, right: 8 })
        .constraintSize({ minWidth: 60, maxWidth: '100%' }) // 文本框的宽度限制
        .backgroundColor('#f1f3f5')
        .borderRadius(5);
    }
  }

  @Entry
  @Component
  struct Page1 {
    uiContext: UIContext = this.getUIContext();
    measureUtils: MeasureUtils = this.uiContext.getMeasureUtils();
    textList: string[] =
      ['11111', '2222222', '3333333', '444', '555555', '6666', '7777777', '88888', '999999999999', '000']; // Flex子组件文本内容
    textItemHeight: number = 30; // 子组件的高度
    foldLine: number = 2; // 默认折叠行数，不到折叠行数时按当前Flex行数，超过会自动折叠到行数
    // Flex折叠状态高度，文本框高度 * 2行 + Flex每行之间的space + Flex上下内间距 + Flex边框
    defaultFlexHeight: number = this.textItemHeight * this.foldLine + (this.foldLine - 1) * 16 + 10 * 2 + 2;
    lineWidth: number = 0; // Flex组件每行可布局宽度
    @State showButton: boolean = false; // 是否展示折叠按钮，行数超过默认折叠行数展示按钮
    @State flexState: string = '展开'; // Flex组件状态，展开/折叠

    getShowButtonValue() {
      let line = 1; // 子组件占用行数
      let countWidth = 0; // 当前行子组件已占用宽度
      this.textList.forEach((item) => {
        if (line <= this.foldLine) { // 行数还未达到需要折叠的行，继续计算布局
          let textWidth = this.uiContext.px2vp(this.measureUtils.measureText({
            textContent: item,
            fontSize: '16fp'
          }));
          // 子组件的宽度，最小60vp，最大占一整行
          let itemWidth =
            (textWidth + 16) < 60 ? 60 : (textWidth + 16 > this.lineWidth ? this.lineWidth : (textWidth + 16));
          if (countWidth === 0) {
            countWidth = itemWidth; // 第一个子组件Flex没有主轴方向子组件间距
          } else {
            if (countWidth + itemWidth + 10 <= this.lineWidth) {
              countWidth = countWidth + itemWidth + 10;
            } else {
              line++; // 换行
              countWidth = itemWidth; // 子组件放到新的一行
            }
          }
        }
      });
      // 不超过折叠行数时不显示按钮，否则展示按钮
      if (line <= this.foldLine) {
        this.showButton = false;
      } else {
        this.showButton = true;
      }
    }

    aboutToAppear(): void {
      let displayClass = display.getDefaultDisplaySync();
      this.lineWidth = this.uiContext.px2vp(displayClass.width) * 0.9 - 2 - 2 * 10;
      this.getShowButtonValue();
    }

    build() {
      Column() {
        Flex({
          wrap: FlexWrap.Wrap,
          space: {
            main: LengthMetrics.vp(10), // 主轴方向间距10
            cross: LengthMetrics.vp(16)
          }
        }) {
          ForEach(this.textList, (item: string) => {
            TextItem({ text: item });
          });
        }
        .width('90%')
        .clip(true)
        .padding(10) // Flex布局上下左右内间距为10
        .border({ color: '#888888', radius: 10, width: 1 })
        .height((this.flexState === '折叠' ? this.defaultFlexHeight : 'auto'));

        Button(this.flexState === '展开' ? '折叠' : '展开')
          .onClick(() => {
            if (this.flexState === '展开') {
              this.flexState = '折叠';
            } else {
              this.flexState = '展开';
            }
          }).margin({ top: 10 })
          .visibility(this.showButton ? Visibility.Visible : Visibility.Hidden);
      }
      .width('100%')
      .height('100%');
    }
  }
  ```

  效果图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/IcC0rj5US6CiZsifnadJjQ/zh-cn_image_0000002628753484.png "点击放大")

* 方案二：获取Flex展示的最后一个子组件索引，通过部分渲染的方式实现展开与折叠。
  1. 通过屏幕宽度计算Flex组件宽，从而得到每一行Flex组件布局时的可用宽度，使用measureText方法计算文本宽度，获取子组件宽度；
  2. 对折叠前几行进行计算，当子组件换行时超过折叠行数记录当前子组件的索引-1，获取折叠状态下最后一个子组件索引；
  3. 在Flex组件中渲染子组件时添加判断条件。当Flex状态为展开状态时，渲染全部子组件。切换为折叠状态时，渲染记录索引前的组件。

  完整代码如下：

  ```ts
  import { display, LengthMetrics, MeasureUtils } from '@kit.ArkUI';

  @Component
  struct TextItem {
    @Prop text: string;

    build() {
      Text(this.text)
        .textAlign(TextAlign.Center)
        .maxLines(1)
        .height(30) // 文本框高度30
        .padding({ left: 8, right: 8 })
        .constraintSize({ minWidth: 60, maxWidth: '100%' }) // 文本框的宽度限制
        .backgroundColor('#f1f3f5')
        .borderRadius(5);
    }
  }

  @Entry
  @Component
  struct Page2 {
    uiContext: UIContext = this.getUIContext();
    measureUtils: MeasureUtils = this.uiContext.getMeasureUtils();
    textList: string[] =
      ['11111', '2222222', '3333333', '444', '555555', '6666', '7777777', '88888', '999999999999', '000']; // Flex子组件文本内容
    textItemHeight: number = 30; // 子组件的高度
    foldLine: number = 2; // 默认折叠行数，不到折叠行数时按当前Flex行数，超过会自动折叠到行数
    lineWidth: number = 0; // Flex组件每行可布局宽度
    @State foldIndex: number = 0; // 折叠时最后一个子组件的索引
    @State showButton: boolean = false; // 是否展示折叠按钮，行数超过默认折叠行数展示
    @State flexState: string = '展开'; // Flex组件状态，展开/折叠

    getFoldIndex() {
      this.showButton = false;
      let line = 1; // 占用行数
      let countWidth = 0; // 当前行子组件已占用宽度
      this.textList.forEach((item, index) => {
        if (line <= this.foldLine) { // 行数还未达到需要折叠的行，继续计算布局
          let textWidth = this.uiContext.px2vp(this.measureUtils.measureText({
            textContent: item,
            fontSize: '16fp'
          }));
          // 子组件的宽度，最小60vp，最大占一整行
          let itemWidth =
            (textWidth + 16) < 60 ? 60 : (textWidth + 16 > this.lineWidth ? this.lineWidth : (textWidth + 16));
          if (countWidth === 0) {
            countWidth = itemWidth; // 第一个子组件Flex没有主轴方向子组件间距
          } else {
            if (countWidth + itemWidth + 10 <= this.lineWidth) {
              countWidth = countWidth + itemWidth + 10;
            } else {
              line++; // 换行
              countWidth = itemWidth; // 子组件放到新的一行
              if (line > this.foldLine) {
                this.foldIndex = index - 1; // 换行刚好超过折叠行数时，获取当前子组件索引-1
                this.showButton = true;
              }
            }
          }
        }
      });
    }

    aboutToAppear(): void {
      let displayClass = display.getDefaultDisplaySync();
      // 计算Flex组件每行可布局宽度，屏幕宽 * 0.9 - Flex边框2 - 左右内边距各10
      this.lineWidth = this.uiContext.px2vp(displayClass.width) * 0.9 - 2 - 2 * 10;
      this.getFoldIndex(); // 获取Flex折叠时展示的最后一个子组件的索引值
    }

    build() {
      Column() {
        Flex({
          wrap: FlexWrap.Wrap,
          space: {
            main: LengthMetrics.vp(10), // 主轴方向间距10
            cross: LengthMetrics.vp(16)
          }
        }) {
          ForEach(this.textList, (item: string, index: number) => {
            if (this.flexState === '展开' || index <= this.foldIndex) { // 展开状态全展示，折叠状态展示部分
              TextItem({ text: item });
            }
          });
        }
        .width('90%')
        .clip(true)
        .padding(10) // Flex布局上下左右内间距为10
        .border({ color: '#888888', radius: 10, width: 1 });

        Button(this.flexState === '展开' ? '折叠' : '展开')
          .onClick(() => {
            if (this.flexState === '展开') {
              this.flexState = '折叠';
            } else {
              this.flexState = '展开';
            }
          }).margin({ top: 10 })
          .visibility(this.showButton ? Visibility.Visible : Visibility.Hidden);
      }
      .width('100%')
      .height('100%');
    }
  }
  ```

  效果图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/3TV2EJ5VSIu4kZvvH4Qlqg/zh-cn_image_0000002658952797.png "点击放大")
