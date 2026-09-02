---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-purax-7
title: 在折叠屏展开态打开应用后折叠，页面内容显示不全
breadcrumb: FAQ > 多设备场景 > 手机 > Pura X常见问题 > 在折叠屏展开态打开应用后折叠，页面内容显示不全
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:48+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:5e5c7cf0e2af4f63ea1ba84b1cb86365a355ad137872a54da78ebda4239f7a17
---

## 问题现象

折叠屏，展开态打开应用后折叠，页面内部分区域内容显示不全。

## 背景知识

* [占比能力](../best-practices/bpta-multi-device-adaptive-layout.md#占比能力)：占比能力是指子组件的宽高按照预设的比例，随父容器组件发生变化。通过layoutWeight属性配置互为兄弟关系的组件在父容器主轴方向的布局权重。
* [Row](../harmonyos-references/ts-container-row.md)组件的[justifyContent](../harmonyos-references/ts-container-row.md#justifycontent8)属性可设置子组件在水平方向上的对齐格式。
* [自适应布局](../best-practices/bpta-multi-device-adaptive-layout.md)：针对常见的开发场景，方舟开发框架提炼了七种自适应布局能力，这些布局可以独立使用，[DevEco Testing](../harmonyos-guides/get-familiar.md)中实用工具分栏其中的工具，可获取设备快照、控件树信息及控件节点属性，辅助自动化脚本开发。也可多种布局叠加使用。
* UIViewer：[DevEco Testing](../harmonyos-guides/get-familiar.md)中实用工具分栏其中的工具，可获取设备快照、控件树信息及控件节点属性，辅助自动化脚本开发。

## 问题定位

使用UIViewer查看展开态打开应用的页面布局与折叠后的页面布局，发现显示异常的组件，在折叠前后width和height没有发生变化。

## 分析结论

由于折叠后窗口宽度变小，而组件的宽度在折叠前后未发生变化，未自适应页面宽度布局，所以部分内容就无法显示出来。

## 修改建议

以下是简单的采用自适应布局中的占比能力均分子组件宽度或者采用父组件的横向对齐格式为FlexAlign.SpaceAround实现子组件自适应均分父组件宽度的方案。其余最佳适配实践方案可参考[官方示例](../best-practices/bpta-foldable-guide.md)。

* 占比能力均分子组件宽度：

  ```screen
  @Entry
  @Component
  struct Divide1 {
    build() {
      Row() {
        Text('1')
          .backgroundColor('#F1F3F5')
          .layoutWeight(1)
          .textAlign(TextAlign.Center)
          .height(50);
        Text('2')
          .backgroundColor('#E5E5EA')
          .layoutWeight(1)
          .textAlign(TextAlign.Center)
          .height(50);
        Text('3')
          .backgroundColor('#D1D1D6')
          .layoutWeight(1)
          .textAlign(TextAlign.Center)
          .height(50);
      }
      .width('100%');
    }
  }
  ```
* 采用父组件的横向对齐格式为FlexAlign.SpaceAround：

  ```screen
  @Entry
  @Component
  struct Divide2 {
    build() {
      Row() {
        Text('1')
          .height(50)
          .width(100)
          .backgroundColor('#F1F3F5');
        Text('2')
          .height(50)
          .width(100)
          .backgroundColor('#E5E5EA');
        Text('3')
          .height(50)
          .width(100)
          .backgroundColor('#D1D1D6');
      }
      .justifyContent(FlexAlign.SpaceAround)
      .width('100%');
    }
  }
  ```
