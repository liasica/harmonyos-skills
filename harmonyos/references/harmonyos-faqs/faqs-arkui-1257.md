---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1257
title: 如何实现组件180°镜面翻转效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现组件180°镜面翻转效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:17+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4427ca4addcaff35cce3265e37cc58c8d9952d6e8eaca2103c15bf777408fc7f
---

## 问题现象

如何为组件添加180°镜面翻转的动画效果？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/dzAGPq1lSaqQtCpR-5tkAA/zh-cn_image_0000002658954729.gif "点击放大")

## 背景知识

* [animateTo](../harmonyos-references/arkts-apis-uicontext-uicontext.md#animateto)：提供animateTo接口来指定由于闭包代码导致的状态变化插入过渡动效。
* [Stack](../harmonyos-references/ts-container-stack.md)：堆叠容器，子组件按照顺序依次入栈，后一个子组件覆盖前一个子组件。
* [rotate](../harmonyos-references/ts-universal-attributes-transformation.md#rotate)：设置组件旋转。
* [zIndex](../harmonyos-references/ts-universal-attributes-z-order.md#zindex)：设置组件的堆叠顺序。

## 解决方案

1. 使用Stack组件进行布局，可以同时设置两个组件内容，但只有一个组件可见，可使页面翻转时交替出现。
2. 设置两个按钮分别用于显示正面和背面，给按钮添加点击事件，在点击事件中使用animateTo方法进行动画过渡。
3. 点击“切换背面”按钮设置rotate为180，zIndex属性值为-1，使其旋转到背面。点击“切换正面”按钮设置rotate为0，zIndex属性值为1，使其旋转到正面。页面旋转交替显示从而实现组件180°镜面翻转效果。

完整示例参考如下：

```screen
@Entry
@Component
struct ReversalIndex {
  @State angle: number = 0;
  @State zIndexNumber: number = 1;
  uiContext: UIContext | undefined = undefined;

  aboutToAppear() {
    this.uiContext = this.getUIContext();
    if (!this.uiContext) {
      console.warn('no uiContext');
      return;
    }
  }

  build() {
    Column({ space: 5 }) {
      Button('切换背面')
        .onClick(() => {
          this.uiContext?.animateTo({ duration: 1000 }, () => {
            // 当动画结束时，将角度设置为180度，并将层级号设置为-1切换到背面
            this.angle = 180;
            this.zIndexNumber = -1;
          });
        });

      Button('切换正面')
        .onClick(() => {
          this.uiContext?.animateTo({ duration: 1000 }, () => {
            // 当动画结束时，将角度设置为0度，并将层级号设置为1切换到正面
            this.angle = 0;
            this.zIndexNumber = 1;
          });
        });

      // 使用Stack布局，可以同时设置两个组件内容，但只有一个组件内容可见
      Stack() {
        Column() {
          Text('背面的内容')
            .fontSize(50);
        }
        .backgroundColor(Color.Pink)
        .width('100%')
        .height('100%')
        .rotate({ y: 2, angle: 180 }); // 设置组件旋转轴向量坐标和旋转角度

        Column() {
          Text('正面的内容')
            .fontSize(50);
        }
        .backgroundColor('#ff709df8')
        .width('100%')
        .height('100%')
        .zIndex(this.zIndexNumber); // 根据zIndexNumber设置层级
      }
      .layoutWeight(1) // 设置布局权重为1
      .rotate({ y: 2, angle: this.angle, perspective: 200 }); // 设置组件旋转轴向量坐标和旋转角度

    }
    .height('100%')
    .width('100%');
  }
}
```

## 常见FAQ

Q：图片可以进行镜面翻转吗？

A：请参考[使用PixelMap完成图像变换](../harmonyos-guides/image-transformation.md#示例代码)。
