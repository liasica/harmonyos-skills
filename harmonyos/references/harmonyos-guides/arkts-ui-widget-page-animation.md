---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-widget-page-animation
title: ArkTS卡片为组件添加动效
breadcrumb: 指南 > 应用框架 > Form Kit（卡片开发服务） > ArkTS卡片开发（推荐） > ArkTS卡片提供方开发指导 > ArkTS卡片UI界面开发 > ArkTS卡片为组件添加动效
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:26+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:ad2145c1cf572b7eceb68d2cec1eb334802a538cef8427455b730739e8b7efbe
---

ArkTS卡片开放了使用动画效果的能力，支持[显式动画](../harmonyos-references/ts-explicit-animation.md)、[属性动画](../harmonyos-references/ts-animatorproperty.md)、[组件内转场](../harmonyos-references/ts-transition-animation-component.md)能力。ArkTS卡片使用动画效果时具有以下限制：

**表1** 动效参数限制

| 名称 | 参数说明 | 限制描述 |
| --- | --- | --- |
| duration | 动画播放时长 | 限制最长的动效播放时长为1秒，当设置大于1秒的时间时，动效时长仍为1秒。 |
| tempo | 动画播放速度 | 卡片中禁止设置此参数，使用默认值1。 |
| delay | 动画延迟执行的时长 | 卡片中禁止设置此参数，使用默认值0毫秒。 |
| iterations | 动画播放次数 | 卡片中禁止设置此参数，使用默认值1次。 |

说明

静态卡片不支持使用动效能力。

## 组件自身动效

以下示例代码使用[animation](../harmonyos-references/ts-animatorproperty.md)接口实现了按钮旋转的动画效果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/x5kBx2ucQhCn0fxH4DR9ew/zh-cn_image_0000002583438337.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234125Z&HW-CC-Expire=86400&HW-CC-Sign=E8186A8E53BC9C14F065E8A3FF64ACE973AD7490C75CFF43794EE3252D4269B7)

```
1. @Entry
2. @Component
3. struct AnimationCard {
4. @State rotateAngle: number = 0;

6. build() {
7. Row() {
8. Button('change rotate angle')
9. .height('20%')
10. .width('90%')
11. .margin('5%')
12. .onClick(() => {
13. this.rotateAngle = (this.rotateAngle === 0 ? 90 : 0);
14. })
15. .rotate({ angle: this.rotateAngle })
16. .animation({
17. curve: Curve.EaseOut,
18. playMode: PlayMode.Normal,
19. })
20. }.height('100%')
21. .alignItems(VerticalAlign.Center)
22. }
23. }
```

## 组件转场动效

以下示例代码使用[transition](../harmonyos-references/ts-transition-animation-component.md)接口实现了在卡片内图片出现与消失的动画效果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/bDx7-_NQRfOQKK92KL2_Bg/zh-cn_image_0000002552958292.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234125Z&HW-CC-Expire=86400&HW-CC-Sign=BCA62A3361340E2E20F30350E01C76956D751724A081C682A5B90A1069C4AC35)

```
1. // entry/src/main/ets/widget/pages/TransitionEffectExample1.ets
2. @Entry
3. @Component
4. struct TransitionEffectExample1 {
5. @State flag: boolean = true;
6. @State show: string = 'show';

8. build() {
9. Column() {
10. Button(this.show).width(80).height(30).margin(30)
11. .onClick(() => {
12. // 点击Button控制Image的显示和消失
13. if (this.flag) {
14. this.show = 'hide';
15. } else {
16. this.show = 'show';
17. }
18. this.flag = !this.flag;
19. })
20. if (this.flag) {
21. // Image的显示和消失配置为相同的过渡效果（出现和消失互为逆过程）
22. // 出现时从指定的透明度为0、绕z轴旋转180°的状态，变为默认的透明度为1、旋转角为0的状态，透明度与旋转动画时长都为1000ms
23. // 消失时从默认的透明度为1、旋转角为0的状态，变为指定的透明度为0、绕z轴旋转180°的状态，透明度与旋转动画时长都为1000ms
24. // $r('app.media.testImg')需要替换开发者所需的图像资源文件
25. Image($r('app.media.testImg')).width(200).height(200)
26. .transition(TransitionEffect.OPACITY.animation({ duration: 1000, curve: Curve.Ease }).combine(
27. TransitionEffect.rotate({ z: 1, angle: 180 })
28. ))
29. }
30. }.width('100%')
31. }
32. }
```
