---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-transition-animation-shared-elements
title: 共享元素转场 (sharedTransition)
category: harmonyos-references
scraped_at: 2026-04-28T08:02:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:066c3b839924ca1a9dfd320f54aaa1a48f084441a619f270575bb2c30510123f
---

可以通过设置组件的sharedTransition属性将该元素标记为共享元素并设置对应的共享元素转场动效。sharedTransition仅发生在[@ohos.router (页面路由)](js-apis-router.md)跳转时。

说明

从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## sharedTransition

PhonePC/2in1TabletTVWearable

sharedTransition(id: string, options?: sharedTransitionOptions): T

设置共享元素转场动效。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 两个页面中id值相同且不为空字符串的组件即为共享元素，在页面转场时可显示共享元素转场动效。 |
| options | [sharedTransitionOptions](ts-transition-animation-shared-elements.md#sharedtransitionoptions) | 否 | 共享元素转场动画参数。不设置时使用默认转场动画参数。各参数具体默认值参考[sharedTransitionOptions](ts-transition-animation-shared-elements.md#sharedtransitionoptions)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## sharedTransitionOptions

PhonePC/2in1TabletTVWearable

共享元素转场动画参数。

说明

type为SharedTransitionEffectType.Exchange时motionPath才会生效。

type为SharedTransitionEffectType.Exchange时，效果为对匹配的共享元素产生位置、大小的过渡（可通过配置组件的border观察），不支持内容的过渡效果。例如，Text组件在两个页面上使用不同的fontSize属性值，即绘制内容有大小差异，在sharedTransition动画结束后的最后一帧，Text的fontSize效果会突变为跳转目标页fontSize的效果。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| duration | number | 否 | 是 | 描述共享元素转场动效播放时长。  默认值：1000  单位：毫秒  取值范围：[0, +∞) |
| curve | [Curve](ts-appendix-enums.md#curve) | string | [ICurve](js-apis-curve.md#icurve9) | 否 | 是 | 动画曲线。  推荐以Curve或ICurve形式指定。  当类型为string时，为动画插值曲线，取值参考[AnimateParam](ts-explicit-animation.md#animateparam对象说明)的curve参数。  默认值：Curve.Linear |
| delay | number | 否 | 是 | 延迟播放时间。  取值范围：[0, +∞)  默认值：0  单位：毫秒 |
| motionPath | [MotionPathOptions](ts-motion-path-animation.md#motionpathoptions) | 否 | 是 | 运动路径信息。 |
| zIndex | number | 否 | 是 | 设置Z轴。  取值范围：(-∞, +∞)  默认值：0 |
| type | [SharedTransitionEffectType](ts-appendix-enums.md#sharedtransitioneffecttype) | 否 | 是 | 动画类型。  默认值：SharedTransitionEffectType.Exchange |

## 示例

PhonePC/2in1TabletTVWearable

示例代码为点击图片跳转页面时，显示共享元素图片的自定义转场动效。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct SharedTransitionExample {

6. build() {
7. Column() {
8. // $r('app.media.ic_health_heart')需要替换为开发者所需的图像资源文件。
9. Image($r('app.media.ic_health_heart')).width(50).height(50).margin({ left: 20, top: 20 })
10. .sharedTransition('sharedImage', { duration: 800, curve: Curve.Linear, delay: 100 })
11. }.width('100%').height('100%').alignItems(HorizontalAlign.Start)
12. .onClick(() => {
13. this.getUIContext().getRouter().pushUrl({ url: 'pages/PageB' })
14. })
15. }

17. pageTransition() {
18. PageTransitionEnter({ type: RouteType.None, duration: 0 })
19. PageTransitionExit({ type: RouteType.None, duration: 0 })
20. }
21. }
```

```
1. // PageB.ets
2. @Entry
3. @Component
4. struct PageBExample {
5. build() {
6. Stack() {
7. // $r('app.media.ic_health_heart')需要替换为开发者所需的图像资源文件。
8. Image($r('app.media.ic_health_heart')).width(150).height(150)
9. .sharedTransition('sharedImage', { duration: 800, curve: Curve.Linear, delay: 100 })
10. }.width('100%').height('100%')
11. }

13. pageTransition() {
14. PageTransitionEnter({ type: RouteType.None, duration: 0 })
15. PageTransitionExit({ type: RouteType.None, duration: 0 })
16. }
17. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/IvpQ2vdbStWzj746_YHyIw/zh-cn_image_0000002552960028.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000217Z&HW-CC-Expire=86400&HW-CC-Sign=C0C3CD2050E698F6F4EC43F0EFAF19C1715C54602A92952EA99C4A909D070B21)
