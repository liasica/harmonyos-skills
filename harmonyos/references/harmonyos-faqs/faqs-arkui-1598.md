---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1598
title: 如何取消Swiper指示器的默认边距
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何取消Swiper指示器的默认边距
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:50+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:50bfc6a74665d24fc043d90866ab415f4fb11884cb05baa6f7c94dc5ec0eb6a7
---

## 问题现象

使用Swiper组件的DotIndicator构建导航指示器，并将导航点底部相对于Swiper的位置属性bottom设置为0，该指示器无法完全贴底，具体演示如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/gY1_0Kd0S9SCwibdxzO7HQ/zh-cn_image_0000002628613328.png "点击放大")

上下左右存在留白，如何实现可以去除内边距的导航指示器效果？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/sRlkmNzxS1qFXPhPJ1mItg/zh-cn_image_0000002658972541.gif "点击放大")

## 背景知识

* [DotIndicator](../harmonyos-references/ts-container-swiper.md#dotindicator10)构造圆点指示器的样式，继承自API10中[Indicator](../harmonyos-references/ts-container-swiper.md#indicator10)。由于导航点有默认交互区域，交互区域高度为32vp，所以无法让显示部分完全贴底。在API19中提供了新的[bottom](../harmonyos-references/ts-container-swiper.md#bottom19)接口，可以忽略指示器的默认高度实现去除内边距的效果。
* 在API15中将Swiper中的指示器单独分割，新增了导航与切换组件[Indicator](../harmonyos-references/ts-swiper-components-indicator.md)，同时也在Swiper内新增了API15的[indicator](../harmonyos-references/ts-container-swiper.md#indicator15)属性，可以实现Indicator组件绑定Swiper内的Indicator属性，也可以单独使用Indicator组件。
* [Stack](../harmonyos-guides/arkts-layout-development-stack-layout.md)是HarmonyOS提供的一种堆叠容器，子组件按照顺序依次入栈，后一个子组件覆盖前一个子组件。

## 解决方案

* **方案一：采用API19的bottom接口。**

  通过bottom接口，可以实现指示器与底部间距为0。实现方式详见：[示例9](../harmonyos-references/ts-container-swiper.md#示例9演示导航点space与bottom)。
* **方案二：自定义Indicator。**

  当前DotIndicator的规格固定存在内边距，无法满足问题需求。可以通过以下步骤实现无内边距的导航指示器效果：

1. 在Stack组件中创建Swiper轮播组件与导航点Column组件。
2. 使用[LazyForEach](../harmonyos-references/ts-rendering-control-lazyforeach.md)循环渲染Column组件，并设置合适的高度和外边距，例如在Stack组件内设置[alignContent](../harmonyos-references/ts-container-stack.md#aligncontent)参数为[Alignment](../harmonyos-references/ts-appendix-enums.md#alignment).Bottom，表示底部对齐，也可以采用[位置设置](../harmonyos-references/ts-universal-attributes-location.md)的方式，直接指定指示器位置。
3. 将index的值与currentIndex作比较，当两者相同时，改变Column的宽度与颜色，以此实现导航点效果。

具体参考代码如下所示：

```screen
@Entry
@Component
struct SwiperExample {
  private swiperController: SwiperController = new SwiperController();
  @State arr: string[] = ['1', '2', '3', '4', '5', '6'];
  @State currentIndex: number = 0;

  build() {
    Column({ space: 5 }) {
      Stack({ alignContent: Alignment.Bottom }) {
        Swiper(this.swiperController) {
          ForEach(this.arr, (item: string) => {
            Text(item)
              .width('90%')
              .height(200)
              .backgroundColor(0xAFEEEE)
              .textAlign(TextAlign.Center)
              .fontSize(30);
          }, (item: string) => item);
        }
        .cachedCount(2)
        .index(0)
        .indicator(false)
        .onChange((index: number) => {
          this.currentIndex = index;
        });

        Row() {
          ForEach(this.arr, (item: string, index: number) => {
            Column()
              .width(this.currentIndex === index ? 15 : 5)
              .height(5)
              .margin(5)
              .backgroundColor(this.currentIndex === index ? Color.Gray : Color.White);
          }, (item: string) => item);
        };
      };
    }
    .width('100%')
    .height('100%');
  }
}
```

方案二运行效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/LEYIs8L2Q9WSGFE-0abQtA/zh-cn_image_0000002658852587.png "点击放大")

* **方案三：采用API15中Indicator组件。**

  Indicator组件采用的依旧是Swiper中的默认指示器样式，一样有32vp的交互高度限制，不过该组件将Swiper与指示器单独分割，可以通过Column组件单独封装指示器，再通过clip属性裁剪，控制Indicator组件高度，其它的与方案二类似采用Stack组件封装。

  具体参考代码如下所示：

  ```screen
  @Entry
  @Component
  struct DotIndicatorDemo {
    private indicatorController: IndicatorComponentController = new IndicatorComponentController();
    private swiperController: SwiperController = new SwiperController();
    @State list: string[] = ['1', '2', '3', '4', '5', '6'];

    build() {
      Stack({ alignContent: Alignment.Bottom }) {
        Swiper(this.swiperController) {
          ForEach(this.list, (item: string) => {
            Text(item)
              .width('90%')
              .height(200)
              .backgroundColor(0xAFEEEE)
              .textAlign(TextAlign.Center)
              .fontSize(30);
          }, (item: string) => item);
        }
        .cachedCount(2)
        .index(0)
        .indicator(this.indicatorController);

        Column() {
          IndicatorComponent(this.indicatorController)
            .style(
              new DotIndicator()
                .itemWidth(10)
                .itemHeight(10)
                .selectedItemWidth(20)
                .selectedItemHeight(10)
                .color(Color.White)
                .selectedColor(Color.Gray)
            );
        }
        .height(25)
        .clip(true);
      }
      .width('100%');
    }
  }
  ```

  方案三运行效果图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/x2em69MFQGSUELXeUw1X2w/zh-cn_image_0000002628773228.png "点击放大")

**说明** 

若方案三指示器背景为透明，不使用clip裁剪也可。同时若背景颜色为透明，也可采用margin属性，设置底部为负值达成类似消除内边距的效果。

## 常见FAQ

Q：如何实现Swiper指示器居左下角显示？

A：可以直接方案二采用位置设置的方式对自定义指示器位置进行定位，或采用自带指示器通过方案一，方案三消除内边距再进行左下角对齐。

Q：如何修改Swiper指示器自带样式圆点的颜色？

A：DotIndicator中.color设置未选中的圆点颜色，.selectedColor属性设置选中的圆点颜色。

Q：如何实现Swiper指示器显示在Swiper外侧？

A：方案二、方案三去掉Stack层叠组件替换为Column组件，默认从上往下排列即可。

## 总结

| 方案 | 位置 | 样式 | 简易程度 |
| --- | --- | --- | --- |
| 方案一 | Swiper内部 | 自带默认样式。 | 简单。 |
| 方案二 | 任意位置 | 多种自定义样式。 | 根据自定义样式的复杂程度攀升。 |
| 方案三 | 任意位置 | 自带默认样式基础上可以增加指示器背景颜色等通用属性（在绑定Swiper组件的情况下height/width等部分通用属性及自身部分属性暂不生效）。 | 一般。 |
