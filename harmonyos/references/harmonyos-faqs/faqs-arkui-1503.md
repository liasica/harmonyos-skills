---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1503
title: App内图片触发非预期拖拽的交互问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > App内图片触发非预期拖拽的交互问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:11+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:7a75ba09da68cc4afbac7117f7396e1e5b3e7f6227146f44248a8f71e426a53e
---

## 问题现象

某些场景下的图片，如PC自由多窗模式下，左侧导航页签图标可以拖动，与使用习惯不符合。异常效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/mtp43iQtREuhcnJWGvs_vQ/zh-cn_image_0000002658965761.png "点击放大")

## 背景知识

* [Tabs](../harmonyos-references/ts-container-tabs.md)：通过页签进行内容视图切换的容器组件，每个页签对应一个内容视图。
* [Image](../harmonyos-references/ts-basic-components-image.md)：图片组件，常用于在应用中显示图片。Image支持加载PixelMap、ResourceStr和DrawableDescriptor类型的数据源，支持png、jpg、jpeg、bmp、svg、webp、gif和heif类型的图片格式，不支持apng和svga格式。
* [draggable](../harmonyos-references/ts-basic-components-image.md#draggable9)：设置组件默认拖拽效果。默认值为true，组件可拖拽，绑定的长按手势不生效。若需要设置自定义手势，则需要将draggable设置为false。设置为false之后，拖拽类事件不再触发。
* [拖拽实现原理](../best-practices/bpta-unified-drag-and-drop.md)：拖拽流程可以分为三部分：发起拖拽、拖拽中和释放拖拽。其中，拖出方通过draggable()和onDragStart()等接口处理拖出数据，拖入方通过allowDrop()和onDrop()等接口处理拖入数据。

## 问题定位

1. 使用DevEco Testing-实用工具-UIViewer查看页面布局，发现菜单栏Tabs组件下使用了Image组件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/ELLWFYk_Ruiup1aXsweyjw/zh-cn_image_0000002628606550.png "点击放大")
2. 排查代码Image组件中draggable属性值是否为可拖拽状态。Image的draggable设置为true或者未设置，图片都是可拖动。示例代码如下：

   ```ts
   Image($r('sys.media.ohos_ic_public_albums')) // 本地资源，需自行替换
     .width(24)
     .height(24)
     .objectFit(ImageFit.Fill)
     .margin({ bottom: 8 })
   ```

## 分析结论

Image组件中未设置draggable属性，该属性默认为true，组件可拖拽。

## 修改建议

给Image组件设置draggable属性为false，使拖拽类事件不再触发。示例代码如下：

```ts
@Entry
@Component
struct TabImageExample {
  private currentIndex: number = 0;
  @State selectedIndex: number = 0;
  private controller: TabsController = new TabsController();
  private data: number[] = [];

  aboutToAppear(): void {
    for (let i = 0; i < 4; i++) {
      this.data.push(i);
    }
  }

  @Builder
  tabBuilder(index: number) {
    Column() {
      Image($r('sys.media.ohos_ic_public_albums')) // 本地资源，需自行替换
        .width(24)
        .height(24)
        .objectFit(ImageFit.Fill)
        .margin({ bottom: 8 })
        .draggable(false);

      Text(`页签${index}`)
        .fontWeight(this.selectedIndex === index ? FontWeight.Bold : FontWeight.Normal)
        .fontSize(16)
        .fontWeight(this.selectedIndex === index ? 500 : 400);
    }
    .width('100%');
  }

  build() {
    Column() {
      Tabs({ barPosition: BarPosition.Start, index: this.currentIndex, controller: this.controller }) {
        ForEach(this.data, (item: number) => {
          TabContent() {
            Column() {
              Text(`页签${item}`)
                .fontSize(20);
            }
            .width('100%')
            .height('100%')
            .justifyContent(FlexAlign.Center)
            .backgroundColor('#E5E5EA');
          }.tabBar(this.tabBuilder(item));
        });
      }
      .vertical(true)
      .barMode(BarMode.Fixed)
      .barWidth(100)
      .barHeight('100%')
      .animationDuration(400)
      .onAnimationStart((targetIndex: number) => {
        this.selectedIndex = targetIndex;
      })
      .width('100%')
      .height('100%')
      .backgroundColor('#F1F3F5');
    }
    .width('100%');
  }
}
```

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/X_OiIAcrTseMaQNGFg_NxQ/zh-cn_image_0000002658845799.png "点击放大")
