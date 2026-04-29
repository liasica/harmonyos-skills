---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-animation
title: 动画概述
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用动画 > 动画概述
category: harmonyos-guides
scraped_at: 2026-04-29T13:28:08+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:75beb0753131fb40a51624eb0ac226a4b02d4adbdc0bce6af70b21792a4288b7
---

UI（用户界面）是用户与设备进行交互的界面，包含各种可视化组件（如按钮、列表等）。属性作为接口，用于控制组件的行为，属性值的变化会引起UI的变化。动画可在UI发生改变时，添加流畅的过渡效果，使属性值从起始状态逐渐变化到终点状态，避免因瞬间变化造成的突兀感，保持用户的视觉焦点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/uNsRpYuaSSWtpjiM4Norjw/zh-cn_image_0000002558604814.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052806Z&HW-CC-Expire=86400&HW-CC-Sign=4DCA13F0FE9D8919E084B17026E2E401730D04686C3572C608591CCEF8F09A4B)

动画的目的包括：

* 使界面的过渡自然流畅。
* 增强用户从界面获得的反馈感和互动感。
* 在内容加载等场景中，增加用户的耐心，缓解等待带来的不适感。
* 引导用户了解和操作设备。

在需要为UI变化添加过渡的场景，都可以使用动画，如开机、应用启动退出、下拉进入控制中心等。这些动画可向用户提供关于其操作的反馈，并有助于让用户始终关注界面。

ArkUI中提供多种动画接口（[属性动画](arkts-attribute-animation-overview.md)、[转场动画](arkts-transition-overview.md)等），用于驱动属性值按照设定的动画参数，从起始值逐渐变化到终点值。尽管变化过程中参数值并非绝对的连续，而是具有一定的离散性。但由于人眼会产生视觉暂留，所以最终看到的就是一个“连续”的动画。UI的一次改变称为一个动画帧，对应一次屏幕刷新。决定动画流畅度的一个重要指标就是帧率FPS（Frames Per Second），即每秒的动画帧数，帧率越高则动画就会越流畅。ArkUI中，动画参数包含了如动画时长、动画曲线等参数。[动画曲线](arkts-traditional-curve.md)作为主要因素，决定了属性值变化的规律。以线性动画曲线为例，在动画时长内，属性值将从起点值匀速变化到终点值。属性过快或过慢的变化，都可能带来不好的视觉感受，影响用户体验。因此动画参数特别是动画曲线，需要结合场景和曲线特点进行设计和调整。

动画接口驱动属性值按照动画参数决定的规律，从原来的状态连续过渡到新的状态，进而在UI上产生连续的视觉效果。本文将按照如下结构，提供各种动画的使用方法和注意事项，使开发者快速学习动画。

* [属性动画](arkts-attribute-animation-overview.md)：最基础的动画类型，按照动画参数逐帧驱动属性的变化，产生一帧帧的动画效果。除其中的自定义属性动画外，动画过程的驱动由系统完成，应用侧不感知动画过程。
* [转场动画](arkts-transition-overview.md)：为组件在出现和消失时添加过渡动画。为了保证动画一致性，部分接口动画曲线已内置，不支持开发者自定义。

  + 不建议在应用内使用[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)组合所有的界面：UIAbility是一个任务，会在多任务界面独立显示为一个卡片，UIAbility之间的跳转相当于任务之间的跳转。以应用内查看大图场景为例，不建议调用图库的UIAbility来打开图片查看大图，因为这会导致任务的跳转，图库的UIAbility也会加入多任务界面中。正确的方式是应用内构建大图组件，通过模态转场去调起大图组件，一个任务内的所有的界面都在一个UIAbility内闭环。
  + 导航转场中，应使用[Navigation](../harmonyos-references/ts-basic-components-navigation.md)组件实现转场动画。过去的page+[router](../harmonyos-references/js-apis-router.md)方式在实现导航转场过程中，因为page和page之间相互独立，其联动动画效果受限。不仅容易导致页面之间的割裂，并且不支持一次开发多端部署。
* [粒子动画](arkts-particle-animation.md)：介绍粒子动画的原理及使用方法。
* [组件动画](arkts-component-animation.md)：组件提供默认动效（如[List](../harmonyos-references/ts-container-list.md)的滑动动效）便于开发者使用，同时部分组件还支持定制化动效。
* [动画曲线](arkts-traditional-curve.md)：介绍传统曲线和弹簧曲线的特点和使用方式。动画曲线影响属性值的运动规律，进而决定界面的动画效果。
* [动画衔接](arkts-animation-smoothing.md)：介绍如何实现动画与动画之间、手势与动画之间的自然过渡。
* [动画效果](arkts-blur-effect.md)：介绍模糊、大阴影和颜色渐变等高阶效果接口的使用方法。
* [帧动画](arkts-animator.md)：系统侧提供在动画过程中的插值结果，由开发者每帧修改属性值产生动画，相比于属性动画，有可实现暂停的优点，但性能不如属性动画。
