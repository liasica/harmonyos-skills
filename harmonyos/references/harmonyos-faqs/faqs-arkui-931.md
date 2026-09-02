---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-931
title: 如何实现组件向上移动时被幕布遮挡的效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现组件向上移动时被幕布遮挡的效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:22+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:7406c035486ec1a08c323a8da7e025839f830c0051b0b7546c9e376786a14aa1
---

## 问题现象

组件初始在幕布下方，如何实现点击后该组件缓慢运动直至被幕布组件完全遮挡的效果？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/fo3-EzbqTv2RjICO37s_8w/zh-cn_image_0000002628400344.gif "点击放大")

## 背景知识

* HarmonyOS提供全局[animateTo](../harmonyos-references/arkts-apis-uicontext-uicontext.md#animateto)显式动画接口来指定由于闭包代码导致的状态变化插入过渡动效。同属性动画，布局类改变宽高的动画，内容都是直接到终点状态，例如文字、Canvas的内容等，如果要内容跟随宽高变化，可以使用renderFit属性配置。
* [zIndex](../harmonyos-references/ts-universal-attributes-z-order.md#zindex)用于设置组件的堆叠顺序。同一容器中兄弟组件显示层级关系。zIndex值越大，显示层级越高，即zIndex值大的组件会覆盖在zIndex值小的组件上方。
* [translate](../harmonyos-references/ts-universal-attributes-transformation.md#translate)可设置组件平移效果，平移参考坐标系原点为所修饰组件的左上角点。

## 解决方案

1. 将幕布组件的zIndex值设置为100，目标组件的zIndex值设置为50。
2. 为目标组件添加onClick点击事件，在该事件中通过getUIContext方法获取UIContext实例对象，并调用animateTo方法，将组件的纵坐标设置为230，实现目标组件向上平移的效果。
3. 由于幕布组件的zIndex值更高，因此运动组件在接触到幕布组件的下缘时就会慢慢消失，产生被幕布遮罩的视觉效果。

完整示例参考如下：

```ts
@Entry
@Component
struct CurtainCoverageDemo {
  @State y: number = 400;

  build() {
    Column() {
      // 模拟幕布
      Column() {
        Text('幕布组件')
          .textAlign(TextAlign.Center)
          .align(Alignment.Center);
      }
      .justifyContent(FlexAlign.Center)

      .size({ width: '100%', height: 100 })
      .position({
        top: 250
      })
      .zIndex(100)
      .backgroundColor('#f0f2f4');

      // 被遮罩的运动组件
      Row() {
        Text()
          .size({ width: 60, height: 60 })
          .fontSize(12)
          .fontColor('#81D3F8')
          .borderRadius(40)
          .backgroundColor('#1d52c2')
          .zIndex(50);
      }
      .size({ width: 60, height: 60 })
      .margin({ top: 50 })
      .translate({ y: this.y }) // 向上平移
      .onClick(() => {
        setTimeout(() => {
          this.getUIContext().animateTo({ duration: 1000 }, () => {
            this.y = 230;
          });
        }, 1000);
      });
    }
    .width('100%')
    .height('100%')
    .backgroundColor(Color.White);
  }
}
```

## 总结

zIndex可设置组件的堆叠顺序，zIndex值大的组件会覆盖在zIndex值小的组件上方。
