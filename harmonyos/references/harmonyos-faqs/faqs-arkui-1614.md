---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1614
title: 页面返回动画过长，无法流畅滑动
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 页面返回动画过长，无法流畅滑动
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:16+08:00
doc_updated_at: 2026-07-31
content_hash: sha256:8ed256a6d9e9de70e760238577eabcadb3dfd943ca8db94fa63628962c6aa15c
---

## 问题现象

PC端应用全屏，选择右上角三个点，点击返回，返回页面的动画时间较长，滑动不流畅。

## 背景知识

* [组件内转场](../harmonyos-references/ts-transition-animation-component.md)主要通过transition属性配置转场参数，在组件插入和删除时显示过渡动效，主要用于容器组件中的子组件插入和删除时，提升用户体验。
* OPACITY:为组件添加透明度转场效果，出现时透明度从0到1、消失时透明度从1到0，相当于TransitionEffect.opacity(0)。

## 问题定位

检查代码，应用设置了转场动效，使用的动画转场模式为fade即返回一个透明度变化的动画效果。需要排查动画中的duration是否设置合理，具体存在问题代码如下：

```ts
getTransitionEffect() {
  if (this.descriptor.rawProps.animationType === "slide") {
    return TransitionEffect.move(TransitionEdge.BOTTOM).animation({
      duration: 2000
    });
  } else {
    if (this.descriptor.rawProps.animationType === "fade") {
      return TransitionEffect.OPACITY.animation({
        duration: 2000 // duration设置了2000ms导致转场不流畅
      });
    } else {
      return TransitionEffect.IDENTITY;
    }
  }
};
```

## 分析结论

动画持续时间为2000ms，时间较长，导致转场动画不流畅。

## 修改建议

* 修改动画时长。缩短动画时长至合适的值（如300ms），确保页面返回时流畅滑动。
* 不使用转场动效，直接使用组件导航Navigation方式进行页面跳转。可以参考[Navigation页面跳转](../harmonyos-guides/arkts-navigation-navigation.md)。
