---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1249
title: 横竖屏切换，一二级页面显示不全有截断
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 横竖屏切换，一二级页面显示不全有截断
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:15+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a25e6bcae5cbf0eff2d9e2190b2ac11d2658a30f192b83ec86c64b7e442cd04f
---

## 问题现象

横竖屏切换，页面显示不全有截断。

## 背景知识

横竖屏切换需要在module.json5中配置[orientation](../harmonyos-references/arkts-apis-window-e.md#orientation9)属性。如果应用是竖屏应用，建议配置portrait为默认旋转策略。如果应用是横屏应用，例如，对于游戏类应用，启动时默认为横屏，存在以下两种情况：

1. 仅支持横屏，建议配置landscape为默认旋转策略。
2. 支持在横屏和反向横屏中切换，建议设置为auto\_rotation\_landscape。

除此之外还需要通过窗口监听横竖屏变化对页面布局和组件适配进行动态设置。具体可参考[横竖屏切换](../best-practices/bpta-landscape-and-portrait-development.md)。

## 问题定位

1. 当窗口宽度或高度的最小值小于348vp时，可能导致布局无法自适应横竖屏切换，出现内容截断或挤压。检查当前窗口全屏尺寸是否符合设备要求（以MatePad Pro为例，平板窗口全屏时尺寸通常为711\*1137vp，需满足最小348vp阈值）。
2. 检查module.json5中是否正确声明orientation属性。
3. 检查是否在需要强制横竖屏的页面（如视频播放页），未调用[setPreferredOrientation](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9)方法动态调整。

   ```ts
   // 示例代码：动态设置竖屏
   this.windowClass.setPreferredOrientation(window.Orientation.USER_ROTATION_PORTRAIT)
   ```
4. 检查是否未针对横竖屏差异设计响应式布局：
   * 组件使用百分比布局替代固定尺寸。
   * 结合栅格系统实现断点适配（如GridRow组件）。

## 分析结论

可能有以下几种原因：

1. 窗口尺寸不足。
2. 旋转策略配置错误。
3. 布局适配不足。

## 修改建议

1. 通过on('windowSizeChange')监听窗口尺寸变化实现动态布局调整，参考[通过断点刷新UI](../best-practices/bpta-multi-device-responsive-layout.md#section175001836203617)。
2. 旋转策略配置可参考[配置module.json5的orientation字段](../best-practices/bpta-landscape-and-portrait-development.md#section1188593118171)。
3. 使用百分比布局替代固定尺寸。以Search组件和List组件结合为例，如果将List组件设置为固定高度，那么在横屏转为竖屏时会出现截断现象。若设置为百分比高度或者设置layoutWeight(1)占用剩余空间则可以避免被截断的现象。

```ts
@Entry
@Component
struct FourPage {
  @State changeValue: string = '';
  @State submitValue: string = '';
  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14];
  controller: SearchController = new SearchController();

  build() {
    Column() {
      Search({ value: this.changeValue, placeholder: 'Type to search...', controller: this.controller })
        .searchButton('SEARCH')
        .width('95%')
        .height(40)
        .backgroundColor('#F5F5F5')
        .placeholderColor(Color.Grey)
        .placeholderFont({ size: 14, weight: 400 })
        .textFont({ size: 14, weight: 400 })
        .onSubmit((value: string) => {
          this.submitValue = value;
        })
        .onChange((value: string) => {
          this.changeValue = value;
        })
        .margin(20);

      List({ space: 20, initialIndex: 0 }) {
        ForEach(this.arr, (item: number) => {
          ListItem() {
            Text('' + item)
              .width('100%')
              .height(100)
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .borderRadius(10)
              .backgroundColor(Color.Gray);
          };
        }, (item: string) => item);
      }
      .width('90%')
      .scrollBar(BarState.Off)
      .layoutWeight(1); // 设置占用剩余空间

    }
    .width('100%')
    .height('100%');
  }
}
```
