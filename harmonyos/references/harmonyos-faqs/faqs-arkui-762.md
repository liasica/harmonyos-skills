---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-762
title: 如何实现组件弹簧拉伸回缩动效
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现组件弹簧拉伸回缩动效
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:22+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:44b55edcca084f71c5144eddd1c3a8d5407827d51d9979d5aeb6f35486f50bd8
---

## 问题现象

如何实现组件弹簧动效？即滑动时不是边缘回弹，而是组件向滑动方向放大，滑动结束后回缩。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/Xh51fsFaSJGVwZiVmMChcg/zh-cn_image_0000002658795063.png "点击放大")

## 背景知识

* [PanGesture](../harmonyos-guides/arkts-gesture-events-single-gesture.md#滑动手势pangesture)：滑动手势用于触发滑动手势事件，滑动达到最小滑动距离（默认值为5vp）时滑动手势识别成功。通过滑动手势的实时回调更新组件状态达成弹簧动效。
* [scale](../harmonyos-references/ts-universal-attributes-transformation.md#scale18)：设置组件缩放。通过控制组件的缩放中心点以及缩放大小实现动效。
* [animateTo](../harmonyos-references/ts-explicit-animation.md)：提供全局animateTo显式动画接口来指定由于闭包代码导致的状态变化插入过渡动效。

## 解决方案

1. 给组件绑定滑动手势，设置移动和手指抬起时的回调。
2. 滑动过程中使用百分比的形式保证缩放连续性以及边界效果。
3. 滑动结束，使用[onActionEnd](../harmonyos-references/ts-basic-gestures-pangesture.md#onactionend)设置滑动手势结束回调，将缩放比例设置回原大小。

示例代码参考如下：

```ts
@Entry
@Component
struct SpringAnimation {
  data: Array<number> = [0, 1, 2, 3, 4, 5];
  @State scaleNumber: number = 1;

  build() {
    Column({ space: 10 }) {
      // 构建内容组件
      ForEach(this.data, (index: number) => {
        Column() {
          Text('欢迎使用HarmonyOS-' + index);
        }
        .height('10%')
        .width('90%')
        .borderRadius(12)
        .backgroundColor('#f1f3f5')
        .alignItems(HorizontalAlign.Center)
        .justifyContent(FlexAlign.Center)
        .scale({ y: 1 / this.scaleNumber, centerY: 0 });
      });
    }
    .height('100%')
    .width('100%')
    .scale({ y: this.scaleNumber, centerY: 0 }) // 设置纵向拉伸以及拉伸中心点
    .gesture(
      PanGesture()
        .onActionUpdate((event) => {
          // 通过滑动距离设置拉伸倍率
          if (event.offsetX > 0 && event.offsetX < 100) {
            // 向下滑动且控制最大响应滑动距离100和最大伸缩倍率1.5
            this.scaleNumber = event.offsetX * 0.005 + 1;
          }
        })
        .onActionEnd(() => {
          // 拉伸结束后返回原大小
          this.getUIContext()?.animateTo({
            duration: 200,
            playMode: PlayMode.Normal,
          }, () => {
            this.scaleNumber = 1;
          });
        })
    );
  }
}
```
