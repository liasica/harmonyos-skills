---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-852
title: 应用加载页面时有短暂的白屏
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 应用加载页面时有短暂的白屏
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:15+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:220b50e7a33bc021acc819b296ab02c2e24e059c79f7e09322c1a3c6a63b4d95
---

## 问题现象

进入应用某个页面，需等待数据请求完成，在请求完成前，页面一直显示空白内容，导致页面白屏近2s后才会加载出页面内容。

## 背景知识

* [骨架屏](https://developer.huawei.com/consumer/cn/forum/topic/0212160177586717601?fid=0109140870620153026)用于在数据未完全加载之前占位页面，减少用户等待焦虑，加强用户体验。
* 在[数据源保持不变](../harmonyos-guides/arkts-rendering-control-foreach.md#数据源不变)的场景中，数据源可以直接采用基本数据类型。例如，在页面加载状态时，可以使用骨架屏列表进行渲染展示。
* 可以使用[linearGradient](../harmonyos-references/ts-universal-attributes-gradient-color.md#lineargradient)+[translate](../harmonyos-references/ts-universal-attributes-transformation.md#translate) +[animation](../harmonyos-references/ts-animatorproperty.md)+[onAppear](../harmonyos-references/ts-universal-events-show-hide.md#onappear)实现骨架屏的闪光效果。

## 问题定位

* 排查是否有使用linearGradient属性，设置骨架屏的渐变背景色。
* 排查是否使用translate属性、animation属性以及onAppear事件，实现骨架屏的加载动画。

若上述功能均未实现，则判断未使用骨架屏功能。

## 分析结论

没有使用骨架屏功能，导致应用加载的页面白屏2s左右才加载出内容，体验不好，造成等待焦虑。

## 修改建议

进入应用后，需要等待加载完成的页面都建议使用骨架屏功能。也可以参考[骨架屏示例](https://gitee.com/harmonyos-cases/cases/tree/master/CommonAppDevelopment/feature/skeletondiagram)。

核心代码如下：

```ts
@Entry
@Component
struct SkeletonExample {
  @State translateX: string = '-100%';
  widthValue: number = 28;
  heightValue: number = 100;

  build() {
    Column({ space: 10 }) {
      Stack() {
        // 背景
        Text()
          .height(this.widthValue)
          .width(this.heightValue)
          .backgroundColor('rgba(220,220,220,1)')

        // 动画
        Text()
          .height(this.widthValue)
          .width(this.heightValue)
          .translate({ x: this.translateX })
          .onAppear(() => {
            this.translateX = '100%';
          })
          .animation({
            duration: 1500,
            iterations: -1
          })
          .linearGradient({
            angle: 90,
            colors: [
              ['rgba(255,255,255,0)', 0],
              ['rgba(255,255,255,1)', 0.5],
              ['rgba(255,255,255,0)', 1]
            ]
          })
      }

      Stack() {
        // 背景
        Text()
          .height(this.widthValue)
          .width(this.heightValue)
          .backgroundColor('rgba(220,220,220,1)')

        // 动画
        Text()
          .height(this.widthValue)
          .width(this.heightValue)
          .translate({ x: this.translateX })
          .onAppear(() => {
            this.translateX = '100%';
          })
          .animation({
            duration: 1500,
            iterations: -1
          })
          .linearGradient({
            angle: 90,
            colors: [
              ['rgba(255,255,255,0)', 0],
              ['rgba(255,255,255,1)', 0.5],
              ['rgba(255,255,255,0)', 1]
            ]
          })
      }

      Stack() {
        // 背景
        Text()
          .height(this.widthValue)
          .width(this.heightValue)
          .backgroundColor('rgba(220,220,220,1)')

        // 动画
        Text()
          .height(this.widthValue)
          .width(this.heightValue)
          .translate({ x: this.translateX })
          .onAppear(() => {
            this.translateX = '100%';
          })
          .animation({
            duration: 1500,
            iterations: -1
          })
          .linearGradient({
            angle: 90,
            colors: [
              ['rgba(255,255,255,0)', 0],
              ['rgba(255,255,255,1)', 0.5],
              ['rgba(255,255,255,0)', 1]
            ]
          })
      }
    }
    .width('100%')
    .height('100%')
  }
}
```
