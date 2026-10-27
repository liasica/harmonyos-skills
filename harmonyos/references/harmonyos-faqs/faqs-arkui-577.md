---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-577
title: 如何实现通过滑动操作让组件消失和重现
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何实现通过滑动操作让组件消失和重现
category: harmonyos-faqs
scraped_at: 2026-10-28T07:47:07+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:c61babf5a16f32ea83d2be6e96c2becdfc307e63b4e7105de4d37366f4715fb1
---

## 问题现象

如何实现通过滑动操作让组件消失和重现的功能，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/cBWEC9ddSMOCF4R1buZ35g/zh-cn_image_0000002628392484.png "点击放大")

## 背景知识

* [PanGesture](../harmonyos-references/ts-basic-gestures-pangesture.md#pangesture15)创建滑动手势对象。
* [onActionUpdate](../harmonyos-references/ts-basic-gestures-pangesture.md#onactionupdate)设置滑动手势更新回调，[onActionEnd](../harmonyos-references/ts-basic-gestures-pangesture.md#onactionend)设置滑动手势结束回调。
* [offset](../harmonyos-references/ts-universal-attributes-location.md#offset)是HarmonyOS提供的一种相对偏移量，组件相对原本的布局位置进行偏移。和position一起使用时，position生效，offset不生效。

## 解决方案

1. 为Row组件添加offset属性，参数为offsetX，用于定义组件在X轴上的偏移量。
2. 添加onActionUpdate方法，用于在手势移动过程中实现组件的平滑滚动。
3. 添加onActionEnd方法，在手势移动结束后用于实现组件位置的确定和透明度渐变效果。

完整代码如下所示：

```ts
@Entry
@Component
struct TransitionEffectPage {
  // 组件往右的偏移量
  @State offsetX: number = 0;
  @State opacityNum: number = 0;

  build() {
    Column() {
      Row() {
        Column() {
        }
        .justifyContent(FlexAlign.Center)
        .backgroundColor(Color.White)
        .width('100%')
        .height(200);

        Row() {
          // 图片资源仅作展示，根据实际替换
          Image($r('app.media.vip_sn_star'))
            .width(200)
            .height(200)
            .opacity(this.opacityNum);
        }
        .margin({ top: 24 });
      }
      .offset({ x: this.offsetX })
      .gesture(
        // 平移手势，滑动最小距离为5vp时识别成功。
        PanGesture({ direction: PanDirection.Horizontal, distance: 1 })
        // Pan手势移动过程中回调
          .onActionUpdate((event: GestureEvent) => {
            if (event.offsetX < 0) {
              this.offsetX = event.offsetX;
            } else {
              this.offsetX = -290 + event.offsetX;
            }
          })
          .onActionEnd(() => {
            // 控制组件滑出屏幕外
            if (this.offsetX > -60) {
              this.getUIContext()?.animateTo({
                duration: 300,
              }, () => {
                this.opacityNum = 0;
                this.offsetX = 0;
              });
            }
            // 控制组件滑动到中央
            else {
              this.getUIContext()?.animateTo({
                duration: 300,
              }, () => {
                this.opacityNum = 1;
                this.offsetX = -290;
              });
            }
          })
      );
    }
    .width('100%')
    .height('100%');
  }
}
```

效果图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/ensxkgSURuOznEwMVvySiA/zh-cn_image_0000002658911703.png "点击放大")
