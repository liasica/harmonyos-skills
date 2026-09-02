---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-820
title: 解决修改文本宽度缺乏过渡动画的问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 解决修改文本宽度缺乏过渡动画的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:22+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:608cfa2b29bb6f8af71077ea535f6e1442d076e1af0ec658c26bfc00b19aeaf9
---

## 问题现象

当通过animateTo实现宽度缩放动画（300px变化为50px）时，文字会立即被截断显示为"文…"，随后才开始进行宽度过渡动画，动画过程中文字始终处于截断状态，视觉体验不连贯。问题代码示例参考如下：

```ts
@Entry
@Component
struct AnimateToExample {
  @State textWidth: Length = 300;
  @State flag: boolean = true;

  private onClick2Animate() {
    this.getUIContext().animateTo({
      duration: 3000,
      curve: Curve.Linear,
      playMode: PlayMode.Normal,
      onFinish: () => {
        console.info('play end')
      }
    }, () => {
      this.textWidth = this.flag ? 50 : 200;
      this.flag = !this.flag
    })
  }

  build() {
    Column() {
      Text('文案文案文案文案文案文案文案')
        .width(this.textWidth)
        .maxLines(1)
        .textOverflow({ overflow: TextOverflow.Ellipsis })
        .fontSize(18)
        .height(30)
        .backgroundColor('#f1f3f5')
        .padding(5)
        .textAlign(TextAlign.Center)
        .onClick(() => {
          this.onClick2Animate()
        })
    }.width('100%').height('100%').justifyContent(FlexAlign.Center)
  }
}
```

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/_LSp5llEQmaT67n-WPgeXw/zh-cn_image_0000002658797715.png "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/PU2t9eyIR1a981m7kyX5oQ/zh-cn_image_0000002628558350.png "点击放大")

## 背景知识

* 被[@State](../harmonyos-guides/arkts-state.md)装饰器装饰的变量称为状态变量，使普通变量具备状态属性。当状态变量改变时，会触发其直接绑定的UI组件渲染更新。
* [UIContext](../harmonyos-references/arkts-apis-uicontext-uicontext.md)提供[animateTo](../harmonyos-references/arkts-apis-uicontext-uicontext.md#animateto)接口来指定由于闭包代码导致的状态变化插入过渡动效。
* [AnimatableExtend装饰器](../harmonyos-guides/arkts-animatable-extend.md)：用于自定义可动画的属性方法，在这个属性方法中修改组件不可动画的属性。

## 问题定位

根本原因在于：闭包内的width赋值立即生效，触发文本截断，animateTo只能对已注册的可动画属性产生过渡效果，width属性不具备逐帧动画能力。

```ts
// 问题代码
this.getUIContext.animateTo({...}, () => {
  this.textWidth = 50; // 同步触发重排
})
```

## 分析结论

* 动画时序错位：首先是布局更新（文字截断），接着是动画开始（宽度变化）。
* 属性限制：系统默认不将width识别为可动画属性。
* 解决方案本质：需通过@AnimatableExtend将width转换为逐帧回调的动画属性。

## 修改建议

使用AnimatableExtend装饰器，通过逐帧修改width实现平滑过渡，避免布局更新优先于动画执行。

```ts
// 使用@AnimatableExtend装饰器，自定义可动画属性接口
@AnimatableExtend(Text)
function animatableWidth(width: number) {
  // 调用系统属性接口，逐帧回调函数每帧修改可动画属性的值，实现逐帧布局的效果
  .width(width);
}

@Entry
@Component
struct AnimateDemo {
  @State textWidth: number = 300;

  build() {
    Column() {
      Text('文案文案文案文案文案文案文案文案文案文案文案文案文案文案文案文案文案')
      // 将自定义可动画属性接口设置到组件上
        .animatableWidth(this.textWidth)
        .maxLines(1)
        .textOverflow({ overflow: TextOverflow.Ellipsis })
        .fontSize(18)
        .height(30)
        .backgroundColor('#f1f3f5')
        .padding(5)
        .textAlign(TextAlign.Center)
        // 为自定义可动画属性接口绑定动画
        .animation({ duration: 2000, curve: Curve.Ease })
        .onClick(() => {
          // 改变自定义可动画属性的参数，产生动画
          this.textWidth = this.textWidth === 300 ? 50 : 300;
        });
    }
    .width('100%').height('100%').justifyContent(FlexAlign.Center);
  }
}
```

## 总结

通过@AnimatableExtend将布局属性转换为可插值的动画属性，使系统能在每一帧计算中间值，实现宽度与文字显示的同步过渡。这本质是将CSS属性提升到动画管线层处理，避免布局与动画的时序冲突。
