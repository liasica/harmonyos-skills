---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1115
title: 播放进度条的进度动画不流畅
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 播放进度条的进度动画不流畅
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:06+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:2af9a1168447cc6f5af3c25acfd80c071d68cc8e04fcddb6fe57f6220c5e7618
---

## 问题现象

视频播放进度条动画卡顿，如何解决该问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/iFFTR4-ESYir3-jWnipbxg/zh-cn_image_0000002658926709.png "点击放大")

## 背景知识

* [Progress](../harmonyos-references/ts-basic-components-progress.md)：进度条组件，用于显示内容加载或操作处理等进度。
* [animateTo](../harmonyos-references/arkts-apis-uicontext-uicontext.md#animateto)：提供animateTo接口来指定由于闭包代码导致的状态变化插入过渡动效。
* [CommonProgressStyleOptions](../harmonyos-references/ts-basic-components-progress.md#commonprogressstyleoptions10)：进度条通用样式选项(enableSmoothEffect)。enableSmoothEffect为进度平滑动效的开关，设置为true携带平滑动效，设置false关闭动效，并可以使用显示动画的方式控制平滑动画。

## 问题定位

1. 使用ArkUI Inspector确认进度条组件的实现方式，确定为Progress组件实现。
2. 检查Progress的value值的实现逻辑，参考以下示例，当value值使用简单的按1s时间自增，进度条便会出现非线性流畅的、跳跃的播放显示。

   ```ts
   Progress({ value: this.value, total: 10, type: ProgressType.Linear })
     .style({ strokeWidth: 10, enableSmoothEffect: true })
     .width('80%')
     .height(150)
     .backgroundColor(Color.Pink)
   Button('start').onClick(() => {
     this.timer = setInterval((() => {
       this.value += 1
     }), 1000)
   })
   ```

## 分析结论

使用Progress进度条组件时，value值使用了简单自增的更新逻辑，导致进度条非线性流畅的播放。

## 修改建议

参考以下示例，使用animation动画自定义实现进度条的更新效果：

```ts
@Entry
@Component
struct ProgressCase {
  @State value: number = 0;
  uiContext: UIContext | undefined = undefined;

  build() {
    Column() {
      Column() {
        Progress({ value: this.value, total: 10, type: ProgressType.Linear })
          .style({ strokeWidth: 10, enableSmoothEffect: true })
          .width('80%')
          .height(150)
          .backgroundColor(Color.Gray)
        Button('start').onClick(() => {
          this.uiContext = this.getUIContext();
          this.uiContext?.animateTo({
            duration: 10 * 1000, // 动画持续时间
            curve: Curve.Linear, // 动画曲线
            playMode: PlayMode.Normal, // 动画播放模式
            onFinish: () => {
              console.info('play end');
            }
          }, () => {
            this.value = 10;
          });
        })
      }.width('100%').height('100%')
    }
  }
}
```
