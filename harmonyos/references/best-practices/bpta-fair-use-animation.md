---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-fair-use-animation
title: 动画使用指导
breadcrumb: 最佳实践 > 动画与转场 > 动画使用指导
category: best-practices
scraped_at: 2026-04-28T08:20:02+08:00
doc_updated_at: 2026-03-19
content_hash: sha256:9847db5e28a2987c347b25239b40d4eb90bf1acf74c6f659b0d6fbd38189c9f7
---

## 概述

动画是应用开发中必不可少的部分，它可以使应用程序更加生动和易于互动，一方面可以提升用户体验、增强视觉吸引力，另一方面可以引导用户操作、提高信息传达效率。应用程序中，页面层级间的转场、点击交互、手势操控都可以添加动画。合理使用动画可以通过以下两个方面考虑：

* 提升动画感知流畅度：使用合适的动画能力将UX设计视角转换为开发实现视角，并将设计师提供的动效转化为具体的代码实现。这样可以确保应用在实际使用中达到设计的预期效果，提升动画感知流畅度并提供良好的用户体验。
* 提升动画运行流畅度：优化动画资源的加载和释放，避免内存泄漏和资源浪费；合理使用动画缓存和复用，减少不必要的重复绘制，提高动画的运行效率。

在使用动画时，需要根据具体场景和用户需求进行合理的设计和运用，并且需要注意动画的性能影响，及时采取相应的优化措施。通过合理使用动画，可以提升动画的感知流畅度和运行流畅度，从而提升应用程序的用户体验和性能。

## 提升动画感知流畅度

HarmonyOS动效引力体系，围绕回归本源设计理念，打造了自然、流畅、品质一体的操作体验。基于视觉效果设计，可以将动效划分为特征动效、转场动效、手势动效、微动效、插画动效。在特征动效中呈现出天体运动“力”的既视感；转场动效表现出物体在运动过程中“力”的秩序感；手势动效打造出元素运动互相影响“力”的控制感；微动效和插画动效辅助HarmonyOS动效引力体系，增加用户的操作趣味性和浏览愉悦感。动效要始终围绕操作符合用户心理预期，物体运动符合真实世界，元素表现形态凸显产品的品牌与调性，从用户感知角度提升流畅度。

HarmonyOS系统为开发者提供了丰富的动画能力，在实际开发过程中，需要把上述UX设计视角转换为开发实现视角，即使用HarmonyOS系统提供的动画能力来实现UX设计的场景和动效，一般来说需要采取如下步骤完成视角转换：

1. 了解系统能力：首先，开发者需要深入了解HarmonyOS系统提供的动画能力，包括动画类型和动画相关API。
2. 分析UX设计视角：仔细分析UX设计所提供的动效，理解设计师的意图。
3. 设计动画方案：基于分析的结果，设计出合理的动画方案。确定动画的触发时机、动画的类型和参数等。
4. 使用动画能力：利用HarmonyOS提供的动画能力，如属性动画、路径动画等或者调用三方库，完成设计效果。
5. 调试和优化：在实施动画的过程中，进行调试和优化。确保动画效果流畅，动效符合预期，且满足性能要求。

通过以上步骤，开发者可以将UX设计视角转换为开发实现视角，并将设计师提供的动效转化为具体的代码实现。这样可以确保应用在实际使用中达到设计的预期效果，提升动画感知流畅度并提供良好的用户体验。

**图1** 合理使用动画

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/JsrjW384RUelwlZDLtwsJw/zh-cn_image_0000002229451841.png?HW-CC-KV=V1&HW-CC-Date=20260428T001957Z&HW-CC-Expire=86400&HW-CC-Sign=83BA7A2A77B9AA1EC9D37280804378BD10A3D7B19283CCF7075F9A2413781F92 "点击放大")

### 动效场景设计

在设计动效过程中，要清楚地理解动效在系统中承载的作用，动效能体现页面的流畅过渡、对象的明确提示、元素的层级关系、产品的品牌印象等。

**特征动效**

特征动效主要打造 “天体拟物感知”，提供一种天体拟物的品牌效应和宇宙空间感的交互体验，它将力赋予元素，更直观地传递出形象化、拟物化、动态化的设计理念，在不同场景上表达新颖个性的同时又凸显了独特的产品调性。它可以广泛应用于开场动画、加载动画、下载动画等场景。

特征动效是指在用户界面中突出某个特定元素的动画效果。通过特征动效，可以吸引用户的注意力，提升用户体验。例如，在一个应用程序中，当用户点击”下载”按钮时，渐变显示出进度条并动态加载(如下图所示)。

**图2** 点击特征动效示意  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/eWob5PE9RuikL-DOncvNxQ/zh-cn_image_0000002229337393.gif?HW-CC-KV=V1&HW-CC-Date=20260428T001957Z&HW-CC-Expire=86400&HW-CC-Sign=FB4C1E50ABE2E56FEC02BD843889AE8ECD6A13F2A12E68BF430E111F241F6E6C "点击放大")

**转场动效**

[转场动效](../design-guides/transition-animation-0000001750078488.md)是指在不同页面或视图之间切换时使用的动画效果。通过转场动效，可以平滑地过渡到下一个页面或视图，增加界面间的连贯性和流畅性。

HarmonyOS系统为开发者提供了丰富的转场动效库，使开发者能够轻松实现各种转场动画效果。开发者可以根据具体需求，在应用的不同场景中应用这些转场动效，以提升用户体验和界面的吸引力。需要注意的是，为了最佳的用户体验，开发者应根据界面的功能和特点，合理选择转场动效，并遵循动效的使用准则，以确保转场动效在视觉和交互上的一致性。

**图3** 转场动效示意  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/TLSuJKtmQku_TkOHfeYNfw/zh-cn_image_0000002229451885.gif?HW-CC-KV=V1&HW-CC-Date=20260428T001957Z&HW-CC-Expire=86400&HW-CC-Sign=EADA0A0B4294C610254E5DE6069041967F5747AE7F5F52CF93C338B3CB592329 "点击放大")

**手势动效**

[手势动效](../design-guides/gesture-animation-0000001797038213.md)是指根据用户的手势操作而产生的动画效果。通过手势动效，可以增强用户与设备之间的互动体验。

* 点击：点击的接触过程中有一段100ms~300ms的时长是无反馈状态，为了提升感知体验，可以在按下那一刻即响应动效反馈。这一可先行的触控响应机制强化了界面元素的视觉反馈，为理解界面状态提供了更多的线索信息。
* 滑动：滑动手势是用户进行滑动操作时产生的相应动画效果，例如随手指移动的平滑过渡动画，增强了界面的流畅性。保证对象动效反馈的结果与手势动作的连贯性是滑动手势动效设计的关键。
* 翻动：翻动手势动效通常用于模拟翻书或翻页的效果，用户可以通过拖拽或抛滑手势来翻转页面或切换内容，界面元素会产生相应的翻页动画，提供更真实的交互体验。翻页分为成功与未成功，未成功会停留在当前内容上；成功则显示下一页/几页的内容。为了提示性，翻页也有过界拖拽的场景。
* 夹捏：捏合手势是指双/多指合拢或分开的动作，常用于缩放或旋转对象。手势过程中需要令对象跟随手势做出相应的响应趋势。
* 拖拽：拖拽手势是指手指按下同时进行移动的动作，动效设计了对象通过拖拽行为进行状态转换的整个过程，以确保用户操作的连贯性和流畅性。

**图4** 手势动效示意  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/lamQYETiSwCh2MDwC5Z1ww/zh-cn_image_0000002194011548.gif?HW-CC-KV=V1&HW-CC-Date=20260428T001957Z&HW-CC-Expire=86400&HW-CC-Sign=BA1D40811DA2FF3136B5391790E076631FD0D0AF070CB1E7EC55B20E3E421188 "点击放大")

**微动效**

微动效是指在界面中细微的动画效果，用于增加界面的生动感和交互性。微动效可以体现在按钮的点击效果、图标的变化、文本的出现等。例如，当用户打开某个面板时，可以使用微小的缩放或颜色变化来体现（如图所示）。

**图5** 微动效示意

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/VXUOJ3xKShyKlocUPeroHQ/zh-cn_image_0000002193851976.gif?HW-CC-KV=V1&HW-CC-Date=20260428T001957Z&HW-CC-Expire=86400&HW-CC-Sign=DDA3B06EF29A48185917FE6485C5BDF1AC784CFF1E723E376122A86DFEFAD59A "点击放大")

**插画动效**

插画动效是指在界面中应用的基于插画的动画效果。通过插画动效，可以为界面增添趣味和个性化。例如，在一个游戏应用中，可以使用插画动效来展示角色的动作、表情或者场景的变化（如图所示）。

通过动画的方式丰富视觉元素所要表达的信息，可以引导解读功能信息并串联前后画面，便于用户理解，也使画面表现更富有生命力。

**图6** 插画动效示意  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/QrxUNtnuSj-UoW5ih6tyaw/zh-cn_image_0000002229337377.gif?HW-CC-KV=V1&HW-CC-Date=20260428T001957Z&HW-CC-Expire=86400&HW-CC-Sign=E6D576FC73C57C0945D89E2F2DB38DDD3F87AD1E7E242A9660D2F1D270CCC867 "点击放大")

### 动画能力选型

开发人员接收到设计需求后，需要选择合适的动画能力完成该设计。HarmonyOS为开发者提供了系统能力、资源调用、三方库三种方式，在选择动画能力时，开发者需要考虑目标和需求以及效率和质量，合理选择能够满足需求的工具、追求高效率和高质量的结果导向，帮助应用实现更好的动画效果。

**系统能力**

* [属性动画](../harmonyos-references/ts-animatorproperty.md)：通过更改组件的属性值实现渐变过渡效果，例如缩放、旋转、平移等。支持的属性包括width、height、backgroundColor、opacity、scale、rotate、translate等。
* [显式动画](../harmonyos-references/ts-explicit-animation.md)：可以通过用户的直接操作或应用程序的特定逻辑来触发，例如按钮点击时的缩放动画、列表项展开时的渐变动画等。HarmonyOS提供了全局animateTo显式动画接口来指定由于闭包代码导致状态变化的插入过渡动效。
* [转场动画](../harmonyos-guides/arkts-transition-overview.md)：转场动画可以实现平滑的界面切换效果，例如页面之间的淡入淡出、滑动切换、旋转切换等，增强了界面的连贯性和吸引力。具体使用方法可参考[《合理使用页面间转场》](bpta-page-transition.md)。
* [路径动画](../harmonyos-references/ts-motion-path-animation.md)：指对象沿着指定路径进行移动的动画效果。通过设置路径可以实现视图沿着预定义的路径进行移动，例如曲线运动、圆周运动等，为用户呈现更加生动的交互效果。
* [粒子动画](../harmonyos-references/ts-particle-animation.md)：通过大量小颗粒的运动来形成整体动画效果。通过对粒子在颜色、透明度、大小、速度、加速度、自旋角度等维度变化做动画，来营造一种氛围感。
* [关键帧动画](../harmonyos-references/ts-keyframeanimateto.md)：在[UIContext](../harmonyos-references/arkts-apis-uicontext-uicontext.md)中提供keyframeAnimateTo接口来指定若干个关键帧状态，实现分段的动画。

**资源调用**

* GIF动画：GIF动画可以在特定位置循环播放，为应用界面增添生动的视觉效果。在开发中，可以使用[Image组件](../harmonyos-references/ts-basic-components-image.md)来实现GIF动画的播放。通过在特定位置放置Image组件，并加载GIF格式的图像，开发者可以轻松实现动画效果。
* 帧动画：通过逐帧播放一系列图片来实现动画效果，在开发中可以使用[ImageAnimator组件](../harmonyos-references/ts-basic-components-imageanimator.md)来实现帧动画的播放。开发者可以配置需要播放的图片列表，以及每张图片的播放时长，从而实现精细的动画效果。

**三方库**

* Lottie：解析Adobe After Effects软件通过Bodymovin插件导出的json格式的动画，并在移动设备上进行本地渲染。Lottie动画可以在各种屏幕尺寸和分辨率上呈现，并且支持动画的交互性，通过添加触摸事件或其他用户交互操作，使动画更加生动和具有响应性。
* SVG：通过将SVG图片解析并渲染到页面上并对SVG图片样式动态改变实现动画。OHOS-SVG不仅能够提供高质量的图形呈现，而且还能够实现图形样式的实时更新，为用户带来更加丰富的视觉体验。

### 动画实践案例

**使用显式动画实现特征动效**

* 场景描述

在本场景中，圆形按钮上会依次出现多个水波状圆环，这些圆环从中心向外进行扩散，进而凸显功能，实现效果如图所示。

**图7** 使用显式动画实现水波纹动效  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/wlEjGr12Qa-xbJT-EPT6UA/zh-cn_image_0000002229451877.gif?HW-CC-KV=V1&HW-CC-Date=20260428T001957Z&HW-CC-Expire=86400&HW-CC-Sign=4ADAB0693E5CA05EB3A7D0245D60A9585735F2F73C7A5D2473285AF562CDEC56 "点击放大")

* 实现原理

水波圆环以圆形按钮为中心，将多个圆形图层逐渐向外扩展放大，每个圆形图层的动画开始时间稍微错开，进而形成多个水波圆环依次扩散的效果。其动效实现步骤如下。

1. 实现圆形图层，以圆形图层作为水波圆环的基础形状，并设置相关背景属性。
2. 通过显示动画animateTo实现圆形图层放大的动效，并设置延迟时间。

* 开发步骤

实现圆形图层，通过Stack将圆形图层与Button组件进行重叠。

```
1. @Component
2. struct ButtonWithWaterRipples {
3. @Link isListening: boolean;
4. @State immediatelyOpacity: number = 0.5;
5. @State immediatelyScale: Scale = { x: 1, y: 1 };
6. @State delayOpacity: number = 0.5;
7. @State delayScale: Scale = { x: 1, y: 1 };
8. private readonly BUTTON_SIZE: number = 120;
9. private readonly BUTTON_CLICK_SCALE: number = 0.8;
10. private readonly ANIMATION_DURATION: number = 1300;

12. @Styles
13. ripplesStyle() {
14. .width(this.BUTTON_SIZE * this.BUTTON_CLICK_SCALE)
15. .height(this.BUTTON_SIZE * this.BUTTON_CLICK_SCALE)
16. .borderRadius(this.BUTTON_SIZE * this.BUTTON_CLICK_SCALE / 2)
17. .backgroundColor(Color.Red)
18. }

20. build() {
21. Stack() {
22. Stack()
23. .ripplesStyle()
24. .opacity(this.immediatelyOpacity)
25. .scale(this.immediatelyScale)
26. Stack()
27. .ripplesStyle()
28. .opacity(this.delayOpacity)
29. .scale(this.delayScale)
30. Button() {
31. Image($r('app.media.ic_public_music_filled'))
32. .width($r('app.float.water_ripples_width'))
33. .fillColor(Color.White)
34. }
35. .clickEffect({ level: ClickEffectLevel.HEAVY, scale: this.BUTTON_CLICK_SCALE })
36. .backgroundColor($r('app.color.music_icon'))
37. .type(ButtonType.Circle)
38. .width(this.BUTTON_SIZE)
39. .height(this.BUTTON_SIZE)
40. .zIndex(1)
41. // ...
42. }
43. }
44. }
```

[PageWaterRipples.ets](https://gitcode.com/HarmonyOS_Samples/animation-collection/blob/master/entry/src/main/ets/feature/pageWaterRipples/view/PageWaterRipples.ets#L47-L135)

实现圆形图层的放大动效，并设置延迟时间。

```
1. Button() {
2. Image($r('app.media.ic_public_music_filled'))
3. .width($r('app.float.water_ripples_width'))
4. .fillColor(Color.White)
5. }
6. .clickEffect({ level: ClickEffectLevel.HEAVY, scale: this.BUTTON_CLICK_SCALE })
7. .backgroundColor($r('app.color.music_icon'))
8. .type(ButtonType.Circle)
9. .width(this.BUTTON_SIZE)
10. .height(this.BUTTON_SIZE)
11. .zIndex(1)
12. .onClick(() => {
13. this.isListening = !this.isListening;
14. if (this.isListening) {
15. this.getUIContext().animateTo({
16. duration: this.ANIMATION_DURATION,
17. iterations: CommonConstants.ITERATIONS,
18. curve: Curve.EaseInOut
19. }, () => {
20. this.immediatelyOpacity = CommonConstants.COMMON_NUMBER_0;
21. this.immediatelyScale = {
22. x: CommonConstants.COMMON_NUMBER_6,
23. y: CommonConstants.COMMON_NUMBER_6
24. };
25. })
26. this.getUIContext().animateTo({
27. duration: this.ANIMATION_DURATION,
28. iterations: CommonConstants.ITERATIONS,
29. curve: Curve.EaseInOut,
30. delay: CommonConstants.DELAY_200
31. }, () => {
32. this.delayOpacity = CommonConstants.COMMON_NUMBER_0;
33. this.delayScale = {
34. x: CommonConstants.COMMON_NUMBER_6,
35. y: CommonConstants.COMMON_NUMBER_6
36. };
37. })
38. } else {
39. // Break the animation by modifying the variable with a closure of duration 0.
40. this.getUIContext().animateTo({ duration: CommonConstants.COMMON_NUMBER_0 }, () => {
41. this.immediatelyOpacity = CommonConstants.COMMON_NUMBER;
42. this.delayOpacity = CommonConstants.COMMON_NUMBER;
43. this.immediatelyScale = {
44. x: CommonConstants.COMMON_NUMBER_1,
45. y: CommonConstants.COMMON_NUMBER_1
46. };
47. this.delayScale = {
48. x: CommonConstants.COMMON_NUMBER_1,
49. y: CommonConstants.COMMON_NUMBER_1
50. };
51. })
52. }
53. })
```

[PageWaterRipples.ets](https://gitcode.com/HarmonyOS_Samples/animation-collection/blob/master/entry/src/main/ets/feature/pageWaterRipples/view/PageWaterRipples.ets#L77-L131)

**使用关键帧动画实现微动效**

* 场景描述

如图所示，在本场景中，在登录页面前需要勾选相关的协议，如果未勾选相关协议，提示框将会通过左右移动进行提示。

**图8** 使用关键帧动画实现左右移动提示  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/AVKcgYKVTYS5Ue_kk0g1QA/zh-cn_image_0000002229451869.gif?HW-CC-KV=V1&HW-CC-Date=20260428T001957Z&HW-CC-Expire=86400&HW-CC-Sign=8BDA20A3F055BEB63292E4171096044BF7B3506C5050F6B8AC79C534B88AB5A3 "点击放大")

* 实现原理

提示框左右移动提醒是将提示框进行左移，然后再进行右移，如此往复循环多次。其动效可以分为提示框左移和提示框右移两段，可以使用keyframeAnimateTo接口实现分段的动画效果，实现步骤如下所示。

1. 根据需要实现的动画效果，将动画拆分成若干个关键帧，即将动画进行分段，如本案例中将动画分成提示框左移和提示框右移两段。
2. 根据不同的关键帧设置关键帧状态，即设置该段关键帧动画的持续时间、动画曲线和闭包函数等。
3. 设置动画触发条件，使用通用事件点击、出现等，选择对应需求的触发方式。

* 开发步骤

通过keyframeAnimateTo来设置关键帧动画。

```
1. startAnimation() {
2. if (!this.uiContext) {
3. return;
4. }
5. this.translateX = CONFIGURATION.POSITION_ZERO;
6. this.uiContext.keyframeAnimateTo({ iterations: CONFIGURATION.PLAYBACK_COUNT }, [
7. {
8. duration: CONFIGURATION.ANIMATION_TIME,
9. event: () => {
10. this.translateX = CONFIGURATION.TRANSLATE_OFFSET_X;
11. }
12. },
13. {
14. duration: CONFIGURATION.ANIMATION_TIME,
15. event: () => {
16. this.translateX = CONFIGURATION.POSITION_ZERO;
17. }
18. }
19. ]);
20. }
```

[PageVibrateEffect.ets](https://gitcode.com/HarmonyOS_Samples/animation-collection/blob/master/entry/src/main/ets/feature/pageVibrateEffect/view/PageVibrateEffect.ets#L229-L249)

设置onClick事件，通过onClick事件调用关键帧动画。

```
1. Button($r('app.string.login_in'))
2. .type(ButtonType.Normal)
3. .borderRadius($r('app.integer.comm_border_radius'))
4. .fontColor($r('app.color.ohos_id_color_background'))
5. .fontSize($r('app.integer.login_button_font_size'))
6. .width(Constants.LAYOUT_MAX_PERCENT)
7. .onClick(() => {
8. if (!this.confirm) {
9. this.startVibrate();
10. this.startAnimation();
11. } else {
12. try {
13. this.getUIContext().getPromptAction().showToast({
14. message: $r('app.string.login_text')
15. });
16. } catch (err) {
17. let error = err as BusinessError;
18. hilog.error(0x0000, 'PageVibrateEffect', `error code=${error.code}, message=${error.message}`);
19. }
20. }
21. })
```

[PageVibrateEffect.ets](https://gitcode.com/HarmonyOS_Samples/animation-collection/blob/master/entry/src/main/ets/feature/pageVibrateEffect/view/PageVibrateEffect.ets#L162-L182)

**使用属性动画实现手势动效**

* 场景描述

在本场景中，页面主要分为标题和列表两个部分，当向下滑动列表时，标题会跟随下滑手势扩展显示详细信息，其实现效果如下所示。

**图9** 使用属性动画实现手势动效  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/TtqO0sidQOeeW-5c7mN1bQ/zh-cn_image_0000002229451845.gif?HW-CC-KV=V1&HW-CC-Date=20260428T001957Z&HW-CC-Expire=86400&HW-CC-Sign=860C32B0527FE0DBC5D64E19119F244536477D78E0EEDAB63DBD75880DCCFA62 "点击放大")

* 实现原理

在实现下拉缩放详情中，主要包含了两个部分，分别是列表下拉的手势和下拉后标题和列表的动画，详细实现步骤如下。

1. 处理手势事件：通过onTouch事件记录当前的触摸点，判断当前的手势是否为向上或向下滑动。
2. 通过属性动画animation实现标题缩放的效果：当列表向上或向下滑动时，改变列表的高度，并通过属性动画进行平滑过度，从而实现标题区域缩放的效果。
3. 实现标题内容的平移：在标题区域进行缩放的同时，标题的内容也会同步进行平移，从而实现标题部分整体缩放的效果。

* 开发步骤

实现手势事件方法。当手指按下时，触发TouchType.Down事件记录当前触碰的位置。手指按压态在屏幕上移动时，可以通过当前的位置与初始位置进行比较，判断手势是否为向上或向下滑动，进而变更列表的高度。

```
1. handleTouchEvent(event: TouchEvent): void {
2. switch (event.type) {
3. case TouchType.Down:
4. this.downY = event.touches[0].y;
5. this.lastMoveY = event.touches[0].y;
6. this.isMoving = true;
7. this.duration = Constants.ANIMATE_DURATION_DRAG;
8. break;

10. case TouchType.Move:
11. const delta = event.touches[0].y - this.lastMoveY;
12. this.offsetY = event.touches[0].y - this.downY;
13. if (delta < 0) {
14. this.heightValue = Constants.AREA_HEIGHT_BEFORE;
15. this.isExpanded = false;
16. this.atStart = false;
17. }
18. if (delta > 0 && this.atStart) {
19. this.animateToThrottle(() => {
20. this.heightValue = Constants.AREA_HEIGHT_AFTER;
21. this.isExpanded = true;
22. }, 1000);
23. }
24. this.lastMoveY = event.touches[0].y;
25. break;

27. case TouchType.Cancel:
28. this.isMoving = false;
29. this.duration = Constants.ANIMATE_DURATION_BACK;
30. break;
31. default:
32. break;
33. }
34. }
```

[PageExpandTitle.ets](https://gitcode.com/HarmonyOS_Samples/animation-collection/blob/master/entry/src/main/ets/feature/pageExpandTitle/view/PageExpandTitle.ets#L154-L187)

为列表设置触摸事件onTouch和属性动画，实现标题区域缩放的效果。

```
1. Column() {
2. List({ space: Constants.SEARCH_MEMO_SPACE }) {
3. ListItem() {
4. Search({ placeholder: $r('app.string.search_placeholder') })
5. .width(Constants.LAYOUT_MAX_PERCENT)
6. .height(Constants.LAYOUT_EIGHT_PERCENT)
7. .backgroundColor(Color.White)
8. .enableKeyboardOnFocus(false)
9. }

11. LazyForEach(this.memoData, (item: MemoInfo) => {
12. ListItem() {
13. MemoItem({ memoItem: item })
14. }
15. }, (item: MemoInfo) => JSON.stringify(item))
16. }
17. .scrollBar(BarState.Off)
18. .margin({ left: $r('app.float.layout_10'), right: $r('app.float.layout_10') })
19. .width(Constants.LAYOUT_NINETY_PERCENT)
20. .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
21. .onReachStart(() => {
22. this.atStart = true;
23. })
24. }
25. .width(Constants.LAYOUT_MAX_PERCENT)
26. .height(this.heightValue)
27. .animation({ duration: this.duration, curve: Curve.FastOutLinearIn })
28. .onTouch((event: TouchEvent) => this.handleTouchEvent(event))
```

[PageExpandTitle.ets](https://gitcode.com/HarmonyOS_Samples/animation-collection/blob/master/entry/src/main/ets/feature/pageExpandTitle/view/PageExpandTitle.ets#L90-L117)

通过animation属性动画实现标题内容平移，从而达到标题整体缩放的效果。

```
1. Column() {
2. Row() {
3. Text(!this.isExpanded ? $r('app.string.memo_title') : '')
4. .fontSize($r('app.float.init_title_font_size'))
5. Blank()
6. // Image($r('app.media.is_public_add'))
7. //   .width($r('app.float.menu_pic_layout'))
8. //   .height($r('app.float.menu_pic_layout'))
9. // Image($r('app.media.ic_public_more'))
10. //   .width($r('app.float.menu_pic_layout'))
11. //   .height($r('app.float.menu_pic_layout'))
12. //   .margin({ left: $r('app.float.layout_8') })
13. }
14. .width(Constants.LAYOUT_MAX_PERCENT)
15. .padding($r('app.float.layout_25'))
16. .margin({ top: $r('app.float.layout_10') })
17. .alignItems(VerticalAlign.Center)
18. .translate(this.getMenuTranslateOptions())
19. .animation({ duration: this.duration, curve: Curve.FastOutLinearIn })

21. Column() {
22. Text($r('app.string.memo_title'))
23. .fontSize($r('app.float.expanded_title_font_size'))
24. Text($r('app.string.memo_counts'))
25. .fontSize($r('app.float.memo_counts_font_size'))
26. .fontColor(Color.Grey)
27. }
28. .width(Constants.LAYOUT_MAX_PERCENT)
29. .padding({ left: $r('app.float.layout_25') })
30. .margin({ top: $r('app.float.layout_10') })
31. .alignItems(HorizontalAlign.Start)
32. .translate(this.getTitleTranslateOptions())
33. .scale(this.getTitleScaleOptions())
34. .animation({ duration: this.duration, curve: Curve.FastOutLinearIn })
35. .transition({ type: TransitionType.Insert, translate: { y: Constants.TRANSLATE_Y } })
36. .visibility(this.isExpanded ? Visibility.Visible : Visibility.Hidden)
37. }
38. .height(Constants.LAYOUT_MAX_PERCENT)
39. .width(Constants.LAYOUT_MAX_PERCENT)
```

[PageExpandTitle.ets](https://gitcode.com/HarmonyOS_Samples/animation-collection/blob/master/entry/src/main/ets/feature/pageExpandTitle/view/PageExpandTitle.ets#L48-L86)

### 提升动画感知流畅度总结

在应用开发中，动画可以为用户界面增添生动、流畅的交互效果，提升用户对应用的好感度。然而，滥用动画也会导致应用性能下降，消耗过多的系统资源，甚至影响用户体验。

本文重点描述了如何在特定设计场景下充分利用HarmonyOS提供的动画能力，以确保动画既能够增强用户体验，又不至于对应用性能造成负面影响。开发者需要在实现动画效果时，注意控制动画的复杂度和频率，以节约系统资源，提升应用的性能表现。提升动画感知流畅度需要考虑以下几点：

* 用户体验：动画应该能够提升用户体验，而不是仅仅为了动画而动画。动画应该能够使用户界面更加生动、直观和易于理解，而不应该过于花哨或者繁琐。
* 性能优化：动画的流畅性对于用户体验至关重要。在设计动画时，需要考虑到设备的性能和资源消耗，避免过多的动画效果导致性能下降或者卡顿。
* 可访问性：在设计动画时，需要考虑到一些用户可能存在的视觉或认知障碍。动画效果应该不会影响到用户对应用界面的理解和操作。
* 上下文适应：动画效果应该根据应用的具体场景和功能进行设计，与应用的整体风格和设计语言保持一致。

合理利用HarmonyOS提供的动画能力可以有效提升应用的用户体验和吸引力，但开发者需要在设计和实现过程中综合考虑动画的使用场景、频率以及对系统资源的影响，扬长避短，确保应用的性能和稳定性。

## 提升动画运行流畅度

动画在应用开发中扮演着重要的角色，能够提升用户体验，传达信息，引导用户操作，提升应用品质和增加视觉吸引力。而动画的性能表现也至关重要，优化可以从属性更新和布局等几个方面考虑，尽可能减少冗余刷新。本文将介绍如下5种优化手段，通过这些优化手段的单个使用或组合使用，可以对动画帧率、应用卡顿等方面带来优化，提升性能和用户体验：

* 使用系统提供的动画接口：系统提供的动画接口经过精心设计和优化，能够在不同设备上提供流畅的动画效果，最大程度地减少丢帧率和卡顿现象。
* 使用图形变换属性变化组件布局：通过对组件的图形变换属性进行调整，而不是直接修改组件的布局属性，可以减少不必要的布局计算和重绘操作，从而降低丢帧率，提升动画的流畅度和响应速度。
* 参数相同时使用同一个animateTo：当多个动画的参数相同时，合并它们并使用同一个animateTo方法进行处理能够有效减少不必要的计算和渲染开销。
* 多次animateTo时统一更新状态变量：在进行多次动画操作时，统一更新状态变量可以避免不必要的状态更新和重复渲染，从而减少性能开销。
* 使用renderGroup：在单一页面上存在大量应用动效的组件时，可以使用renderGroup方法来解决卡顿问题，从而提升动画性能。

下文将通过5个测试来验证上述优化方法的收益，以证明这些优化手段的可行性。综合考虑业界共识指标和实际用户使用体验，测试将对比分析如下几个关键指标：

* 丢帧率（Janky Frames）：表示一个时间周期内的丢帧比率，指一个时间周期内有问题的帧比例。HarmonyOS系统要求每一帧都要在11.1ms（90Hz刷新率）内绘制完成，如果页面没有在11.1ms内完成这一帧的绘制，就会出现丢帧。部分丢帧一般用户肉眼是感知不到的，只有出现连续丢帧用户才有明显感知。
* 最大连续丢帧数（maximum successive frame dropping count）：表示从页面开始有响应变化到页面结束刷新的过程中，由于显示器画面刷新频率低于预设的画面帧率而未能正常呈现的最大连续帧数。一般而言，当连续值超过3时，用户可以明显感知到卡顿掉帧，数值越大卡顿时间越长。
* 平均1s大卡顿次数：表示程序运行过程中平均1s出现连续丢3帧以上的卡顿的次数，数值越大用户体验感越差。

测试表明，当系统提供的接口可以实现所需动画效果时，其性能明显优于使用自定义动画实现，自定义动画大量的计算会导致其在应用侧大量丢帧，而系统提供的接口不依赖应用侧计算，更加流畅顺滑；实现位移、缩放、旋转等布局变化动画时，使用图形变换属性替换布局属性实现动画可以将丢帧率从8.1%降至3.7%，且明显减少了大卡顿次数；而多个参数相同的动画闭包同时实现时，将变化属性放入一个动画闭包可以使丢帧率从9.6%降低至4.0%；同样的，避免在两个动画闭包之间更新状态也可以降低动画的丢帧率。

### 使用系统提供的动画接口

一般而言，在HarmonyOS应用开发中，动画设计实现可以通过自定义动画或系统提供的动画接口两种方式来实现。

* 方式一，自定义动画：

  自定义动画是指通过编写自定义的动画逻辑和计算过程来实现特定的动画效果。开发人员可以根据应用的需求和设计要求，使用自定义的动画算法和逻辑来创建独特的动画效果。自定义动画的优势在于可以实现非常个性化的动画效果，并且能够完全控制动画的每一个细节，但需要开发人员具备一定的动画算法和计算能力。
* 方式二，系统动画接口：

  系统动画接口是指通过使用系统提供的动画框架和接口来实现动画效果。在移动应用开发中，通常会使用属性动画来实现各种动画效果。通过可动画属性改变引起UI上产生的连续视觉效果，即为属性动画。属性动画是最基础易懂的动画，ArkUI提供两种属性动画接口[animateTo](../harmonyos-references/arkts-apis-uicontext-uicontext.md#animateto)和[animation](../harmonyos-references/ts-animatorproperty.md)驱动组件属性按照动画曲线等动画参数进行连续的变化，产生属性动画。使用系统提供的动画接口可以简化动画的实现过程，并且能够充分利用系统优化的动画计算和渲染能力，从而提高动画的性能和流畅度。

**场景设计**

针对同一界面多个按钮同时缩放的场景（如下图所示），分别用自定义动画、属性动画、显式动画实现。

**图10** 同一界面多个按钮同时缩放示意图  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/sq4YkuS-T76t4XhbjaWcmw/zh-cn_image_0000002229337385.gif?HW-CC-KV=V1&HW-CC-Date=20260428T001957Z&HW-CC-Expire=86400&HW-CC-Sign=8E46EAEDC698A60ADF6647B617E406287D16701A08AA9CD7BB5EE7BFE9697BA8 "点击放大")

**自定义动画**

播放动画时，系统需要在一个刷新周期内完成动画变化曲线的计算，完成组件布局绘制等操作。使用了自定义动画，动画曲线计算过程很容易引起UI线程高负载，易导致丢帧。

使用自定义动画实现按键缩放，具体实现代码如下：

```
1. @Component
2. export struct CustomAnimation {
3. @State widthSize: number = 80
4. @State heightSize: number = 40
5. @State flag: boolean = true

7. // Custom animation function
8. computeSize() {
9. let duration = 2000
10. // Set the loop cycle
11. let period = 1
12. let widthSizeEnd = 0
13. let heightSizeEnd = 0
14. if (this.flag) {
15. widthSizeEnd = 50
16. heightSizeEnd = 25
17. } else {
18. widthSizeEnd = 80
19. heightSizeEnd = 40
20. }
21. // Calculate loop count
22. let doTimes = duration / period
23. // Calculate the variation per cycle
24. let deltaHeight = (heightSizeEnd - this.heightSize) / doTimes
25. let deltaWeight = (widthSizeEnd - this.widthSize) / doTimes
26. // Loop, with each cycle the component increases in width and height by a portion.
27. for (let i = 1; i <= doTimes; i++) {
28. let t = period * (i);
29. setTimeout(() => {
30. this.heightSize = this.heightSize + deltaHeight
31. this.widthSize = this.widthSize + deltaWeight
32. }, t)
33. }
34. this.flag = !this.flag
35. }

37. build() {
38. Column() {
39. Column() {
40. Row() {
41. Button()
42. .width(this.widthSize)
43. .height(this.heightSize)
44. .margin(20)
45. Button()
46. .width(this.widthSize)
47. .height(this.heightSize)
48. .margin(20)
49. Button()
50. .width(this.widthSize)
51. .height(this.heightSize)
52. .margin(20)
53. }
54. // ...
55. }
56. .height('85%')

58. Column() {
59. Button('Tap me')
60. .width('100%')
61. .onClick(() => {
62. setTimeout(() => {
63. this.computeSize()
64. }, 500)
65. })
66. }
67. .justifyContent(FlexAlign.End)
68. .width('100%')
69. .height('15%')
70. }
71. .padding({
72. left: 16,
73. right: 16,
74. bottom: 16
75. })
76. .width('100%')
77. .height('100%')
78. .justifyContent(FlexAlign.Start)
79. }
80. }
```

[CustomAnimation.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/animation/entry/src/main/ets/pages/CustomAnimation.ets#L17-L186)

**系统动画接口**

系统提供的动画接口，只需设置曲线类型、终点位置、时长等信息，就能够满足常用的动画功能，减少UI主线程的负载。

* 使用属性动画实现按键缩放，具体实现代码如下：

  ```
  1. @Component
  2. export struct PropertyAnimateTo {
  3. @State widthSize: number = 80;
  4. @State heightSize: number = 40;
  5. @State flag: boolean = true;

  7. build() {
  8. Column() {
  9. Column() {
  10. Row() {
  11. Button()
  12. .width(this.widthSize)
  13. .height(this.heightSize)
  14. .animation({
  15. duration: 2000,
  16. curve: Curve.Linear,
  17. delay: 500,
  18. iterations: 1,
  19. playMode: PlayMode.Normal
  20. })
  21. .margin(20)
  22. // ...
  23. }

  25. // ...
  26. }
  27. .height('85%')

  29. Column() {
  30. Button('Tap me')
  31. .width('100%')
  32. .onClick((event?: ClickEvent | undefined) => {
  33. if (this.flag) {
  34. this.widthSize = 50
  35. this.heightSize = 25
  36. } else {
  37. this.widthSize = 80
  38. this.heightSize = 40
  39. }
  40. this.flag = !this.flag
  41. })
  42. }
  43. .height('15%')
  44. }
  45. .padding({
  46. left: 16,
  47. right: 16,
  48. bottom: 16
  49. })
  50. .width('100%')
  51. .height('100%')
  52. .justifyContent(FlexAlign.Start)
  53. }
  54. }
  ```

  [PropertyAnimateTo.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/animation/entry/src/main/ets/pages/PropertyAnimateTo.ets#L17-L275)

* 使用显式动画实现按键缩放，具体实现代码如下：

  ```
  1. @Component
  2. export struct ExplicitAnimateTo {
  3. @State widthSize: number = 80;
  4. @State heightSize: number = 40;
  5. @State flag: boolean = true;

  7. build() {
  8. Column() {
  9. Column() {
  10. Row() {
  11. Button()
  12. .width(this.widthSize)
  13. .height(this.heightSize)
  14. .margin(20)
  15. // ...
  16. }

  18. // ...
  19. }
  20. .height('85%')

  22. Column() {
  23. Button('Tap me')
  24. .width('100%')
  25. .onClick((event?: ClickEvent | undefined) => {
  26. // Animate the width and height properties of the Button component
  27. if (this.flag) {
  28. this.getUIContext().animateTo({
  29. duration: 2000,
  30. curve: Curve.Linear,
  31. delay: 500,
  32. iterations: 1,
  33. playMode: PlayMode.Normal
  34. }, () => {
  35. this.widthSize = 50;
  36. this.heightSize = 25;
  37. })
  38. } else {
  39. this.getUIContext().animateTo({
  40. duration: 2000,
  41. curve: Curve.Linear,
  42. delay: 500,
  43. iterations: 1,
  44. playMode: PlayMode.Normal
  45. }, () => {
  46. this.widthSize = 80;
  47. this.heightSize = 40;
  48. })
  49. }
  50. this.flag = !this.flag;
  51. })
  52. }
  53. .height('15%')
  54. }
  55. .padding({
  56. left: 16,
  57. right: 16,
  58. bottom: 16
  59. })
  60. .width('100%')
  61. .height('100%')
  62. .justifyContent(FlexAlign.Start)
  63. }
  64. }
  ```

  [ExplicitAnimateTo.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/animation/entry/src/main/ets/pages/ExplicitAnimateTo.ets#L17-L180)

**性能分析**

使用DevEco Studio的Profiler工具检测下述指标，得到的数据如下所示：

**表1** **自定义动画、属性动画、显式动画实现相同场景****的指标对比**

|  | 自定义动画 | 属性动画 | 显式动画 |
| --- | --- | --- | --- |
| 丢帧率（%） | 9.2% | 0% | 0% |
| 最大连续丢帧数（帧） | 7 | 0 | 0 |
| 平均1s大卡顿次数（次/s） | 1.50 | 0 | 0 |

分析结论：

1）使用自定义动画实现计算量较大的动画时，丢帧率高达9.2%，最大连续丢失7帧，平均每秒发生大卡顿1.5次。

2）使用系统动画接口实现相同效果时，属性动画接口和显式动画接口都能够达到0丢帧。

这一结果表明，系统动画接口内部实现对开发者是透明的，已经进行了尽可能的性能优化，避免开发者使用自定义动画时产生不必要的性能劣化。自定义动画适合实现个性化的、复杂的动画效果，而系统提供的动画接口则适合实现常见的动画效果并且能够获得更好的性能表现。因此，在动画能够使用系统提供的接口实现的情况下，开发者应尽量使用系统提供的接口实现，保持动画的流畅性和稳定性，提升应用的性能表现。

### 使用图形变换属性变化组件

在应用开发中，改动组件的布局显示可以通过改动布局属性、改动图形变换属性两种方式来实现。

* 方式一，改动布局属性

  常见的布局属性包括位置、大小、内边距、外边距、对齐方式、权重等。当这些布局属性发生改变时，界面将重新布局以适应新的属性值。
* 方式二，改动图形变换属性

  图形变换属性是指对组件布局结果的变换操作，如平移、旋转、缩放等操作。通过改变这些图形变换属性，可以实现对组件布局完成后，在界面上的位置和形态进行动态变换。

布局属性和图形变换属性的可替换关系如下表所示：

**表2**

| 图形变换属性 | 布局属性 |
| --- | --- |
| rotate | / |
| translate | position、offset |
| scale | width、height、Size |
| transform | / |

说明

表格中的对应关系仅供参考，开发者可以自行发掘更多的替代关系。

**场景设计**

针对同一界面多个图片同时缩放并位移的场景（如下图所示），分别通过改变布局属性、改变图形变换属性实现。

**图11** 同一界面多个图片同时缩放并位移示意图  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/KwFYoab3Q3O4d8VPitOwMA/zh-cn_image_0000002193852008.gif?HW-CC-KV=V1&HW-CC-Date=20260428T001957Z&HW-CC-Expire=86400&HW-CC-Sign=94A049DF59EB0743C3DB59718D4C45FFBE68F1395BD05C08B059BCFFC73381B5 "点击放大")

**改变布局属性**

布局属性发生变化时，系统需要重新计算组件的位置和大小，然后进行重新布局。这个过程需要消耗大量的计算资源和时间，尤其是在界面中包含大量组件或者复杂布局时，性能开销会更加明显。

通过组件的width、height、position属性来改变组件大小和位置，具体代码实现如下：

```
1. @Component
2. export struct ImageAnimation {
3. @State imageWidth: number = 60;
4. @State imageHeight: number = 60;
5. @State xPosition: number = 0;
6. @State yPosition: number = 0;
7. @State imageScaleX: number = 1;
8. @State imageScaleY: number = 1;
9. @State imageTranslateX: number = 0;
10. @State imageTranslateY: number = 0;

12. build() {
13. Column() {
14. Row() {
15. Row() {
16. Image($r('app.media.startIcon'))
17. .width(this.imageWidth)
18. .height(this.imageHeight)
19. .position({ x: this.xPosition, y: this.yPosition })
20. .scale({
21. x: this.imageScaleX,
22. y: this.imageScaleY,
23. centerX: 0,
24. centerY: 0
25. })
26. .translate({ x: this.imageTranslateX, y: this.imageTranslateY })
27. }.width('33%')
28. // ...
29. }
30. .height('25%')
31. // ...
32. Column() {
33. Button('Change Layout Properties')
34. .width('100%')
35. // Key Attribute Settings
36. .onClick(() => {
37. // Loop animation by play count
38. for (let i = 0; i < 10; i++) {
39. // Interval playback position, width and height changes
40. if (i % 2 == 0) {
41. setTimeout(() => {
42. this.getUIContext().animateTo({ duration: 1000 }, () => {
43. this.imageWidth = 100;
44. this.imageHeight = 100;
45. this.xPosition = 12;
46. this.yPosition = 12;
47. })
48. }, 1000 * i)
49. } else {
50. setTimeout(() => {
51. this.getUIContext().animateTo({ duration: 1000 }, () => {
52. this.imageWidth = 60;
53. this.imageHeight = 60;
54. this.xPosition = 0;
55. this.yPosition = 0;
56. })
57. }, 1000 * i)
58. }
59. }
60. })
61. Button('Change Image Properties')
62. .width('100%')
63. .margin({ top: 12 })
64. .onClick(() => {
65. // Loop animation by play count
66. for (let i = 0; i < 10; i++) {
67. if (i % 2 == 0) {
68. setTimeout(() => {
69. this.getUIContext().animateTo({ duration: 1000 }, () => {
70. this.imageScaleX = 2;
71. this.imageScaleY = 2;
72. this.imageTranslateX = 12;
73. this.imageTranslateY = 12;
74. })
75. }, 1000 * i)
76. } else {
77. setTimeout(() => {
78. this.getUIContext().animateTo({ duration: 1000 }, () => {
79. this.imageScaleX = 1;
80. this.imageScaleY = 1;
81. this.imageTranslateX = 0;
82. this.imageTranslateY = 0;
83. })
84. }, 1000 * i)
85. }
86. }
87. })
88. }
89. .justifyContent(FlexAlign.End)
90. .height('25%')
91. }
92. .padding({
93. left: 16,
94. right: 16,
95. bottom: 16
96. })
97. .width('100%')
98. .height('100%')
99. .justifyContent(FlexAlign.Start)
100. }
101. }
```

[ImageAnimation.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/animation/entry/src/main/ets/pages/ImageAnimation.ets#L17-L242)

**改变图形变换属性**

图形变换只是对组件的显示效果进行变换，而不会改变其在布局中的位置和大小，因此不会触发重新布局的计算过程。这使得使用图形变换属性来实现动画效果时，能够提升界面的流畅性和性能表现。

通过组件的scale、translate属性来改变组件大小和位置，具体代码实现如下：

```
1. @Component
2. export struct ImageAnimation {
3. @State imageWidth: number = 60;
4. @State imageHeight: number = 60;
5. @State xPosition: number = 0;
6. @State yPosition: number = 0;
7. @State imageScaleX: number = 1;
8. @State imageScaleY: number = 1;
9. @State imageTranslateX: number = 0;
10. @State imageTranslateY: number = 0;

12. build() {
13. Column() {
14. Row() {
15. Row() {
16. Image($r('app.media.startIcon'))
17. .width(this.imageWidth)
18. .height(this.imageHeight)
19. .position({ x: this.xPosition, y: this.yPosition })
20. .scale({
21. x: this.imageScaleX,
22. y: this.imageScaleY,
23. centerX: 0,
24. centerY: 0
25. })
26. .translate({ x: this.imageTranslateX, y: this.imageTranslateY })
27. }.width('33%')
28. // ...
29. }
30. .height('25%')
31. // ...
32. Column() {
33. // ...
34. Button('Change Image Properties')
35. .width('100%')
36. .margin({ top: 12 })
37. .onClick(() => {
38. // Loop animation by play count
39. for (let i = 0; i < 10; i++) {
40. if (i % 2 == 0) {
41. setTimeout(() => {
42. this.getUIContext().animateTo({ duration: 1000 }, () => {
43. this.imageScaleX = 2;
44. this.imageScaleY = 2;
45. this.imageTranslateX = 12;
46. this.imageTranslateY = 12;
47. })
48. }, 1000 * i)
49. } else {
50. setTimeout(() => {
51. this.getUIContext().animateTo({ duration: 1000 }, () => {
52. this.imageScaleX = 1;
53. this.imageScaleY = 1;
54. this.imageTranslateX = 0;
55. this.imageTranslateY = 0;
56. })
57. }, 1000 * i)
58. }
59. }
60. })
61. }
62. .justifyContent(FlexAlign.End)
63. .height('25%')
64. }
65. .padding({
66. left: 16,
67. right: 16,
68. bottom: 16
69. })
70. .width('100%')
71. .height('100%')
72. .justifyContent(FlexAlign.Start)
73. }
74. }
```

[ImageAnimation.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/animation/entry/src/main/ets/pages/ImageAnimation.ets#L18-L243)

**性能分析**

使用DevEco Studio的Profiler工具检测下述指标，得到的数据如下所示：

**表3** **改变布局属性、改变图形变换属性实现****相同场景****的指标对比**

|  | 改变布局属性 | 改变图形变换属性 |
| --- | --- | --- |
| 丢帧率（%） | 8.1% | 3.7% |
| 最大连续丢帧数（帧） | 8 | 2 |
| 平均1s大卡顿次数（次/s） | 0.48 | 0 |

分析结论：

1）使用布局属性改变图片大小和位置时，丢帧率为8.1%，最多连续丢失8帧，平均每秒发生大卡顿0.48次。

2）使用图形变化属性改变图片大小和位置时，丢帧率降到了3.7%，最多连续丢失2帧，在相同时长内没有发生大卡顿。

这一结果表明，使用图形变化属性改变图片大小和位置时，能够显著降低丢帧率和大卡顿的发生频率。界面布局是非常耗时的操作，因此频繁地改动布局属性会导致界面性能下降，出现卡顿现象，影响用户体验。因此，在动画能够使用图形变化属性实现的情况下，开发者应尽量使用图形变化属性实现，保持动画的流畅性和稳定性，提升应用的性能表现。

### 参数相同时使用同一个animateTo

说明

建议开发者优先使用[Code Linter扫描工具](../harmonyos-guides/ide-code-linter.md)进行代码检查，重点关注[@performance/hp-arkui-combine-same-arg-animateto](../harmonyos-guides/ide_hp-arkui-combine-same-arg-animateto.md)规则。若扫描结果中出现该规则相关问题，可参考本章节提供的优化建议进行调整。

每次调用animateTo方法，都会触发一次属性变化，这意味着在每次动画执行时都需要进行动画前后的对比，以确定属性的变化情况。当多次连续调用animateTo时，会增加额外的布局计算和绘制开销，从而降低性能表现。特别是当这些animateTo操作针对同一个组件的属性时，会导致该组件更新的次数增加，进一步影响性能。

在实际开发中，如果多个属性需要以相同的动画参数进行变化，推荐将它们放到同一个动画闭包中执行。通过将多个属性的动画操作合并到同一个动画闭包中，可以减少对组件的多次更新，避免重复的布局计算和绘制操作，提升动画效果的性能。

除了性能方面的优势，将多个属性的动画操作合并到同一个动画闭包中还有助于提高代码的可读性和维护性。通过集中管理相关联的属性变化，可以使代码结构更加清晰，便于后续的维护和修改。

**场景设计**

针对多个相同组件同时修改多个属性的场景（如下图所示），分别使用多个animateTo闭包和一个animateTo闭包实现。

**图12** 多个相同组件同时修改多个属性示意图  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/fmB7iaNET6yuk0wcEjwlNQ/zh-cn_image_0000002229337397.gif?HW-CC-KV=V1&HW-CC-Date=20260428T001957Z&HW-CC-Expire=86400&HW-CC-Sign=60B707967FCA4D655DC96A3D23EE605F99E3D095C032E18DE4BD4E2ADDB75464 "点击放大")

**代码实现**

* 将相同动画参数的状态变量更新放在不同的动画闭包中，具体代码实现如下：

  ```
  1. @Component
  2. export struct MultipleProperties {
  3. @State w:number = 150
  4. @State h:number = 2
  5. @State brightNum:number = 1.5
  6. @State color:Color = Color.Red
  7. // Animation closure 1, set width change
  8. func1() {
  9. this.getUIContext().animateTo({curve: Curve.Sharp, duration: 1000}, () => {
  10. this.w = (this.w === 80 ? 150 : 80);
  11. });
  12. }
  13. // Animation Closure 2, Set Color Change
  14. func2() {
  15. this.getUIContext().animateTo({curve: Curve.Sharp, duration: 1000}, () => {
  16. this.color = (this.color === Color.Yellow ? Color.Red : Color.Yellow);
  17. });
  18. }
  19. // Animation closure 3, set height variation
  20. func3() {
  21. this.getUIContext().animateTo({curve: Curve.Sharp, duration: 1000}, () => {
  22. this.h = (this.h === 2 ? 5 : 2);
  23. });
  24. }
  25. // Animation Closure 4, Set Highlight Variation
  26. func4() {
  27. this.getUIContext().animateTo({curve: Curve.Sharp, duration: 1000}, () => {
  28. this.brightNum= (this.brightNum=== 1.5 ? 1 : 1.5);
  29. });
  30. }
  31. // ...
  32. build() {
  33. Column() {
  34. Row() {
  35. Row() {
  36. Row()
  37. .width(this.w)
  38. .backgroundColor(this.color)
  39. .height(this.h)
  40. .brightness(this.brightNum)
  41. }
  42. .justifyContent(FlexAlign.Center)
  43. .width('50%')

  45. Row() {
  46. Row()
  47. .width(this.w)
  48. .backgroundColor(this.color)
  49. .height(this.h)
  50. .brightness(this.brightNum)
  51. }
  52. .justifyContent(FlexAlign.Center)
  53. .width('50%')
  54. }
  55. .height('25%')
  56. .width('100%')
  57. // ...

  59. Column() {
  60. Button("Tap nFunc")
  61. .width('100%')
  62. // Key Attribute Settings
  63. .onClick(() => {
  64. // Loop animation by play count
  65. for (let i = 0; i < 10; i++) {
  66. setTimeout(() => {
  67. this.func1();
  68. this.func2();
  69. this.func3();
  70. this.func4();
  71. }, 1000 * i)
  72. }
  73. })
  74. // ...
  75. }
  76. .justifyContent(FlexAlign.End)
  77. .height('25%')
  78. }
  79. .padding({
  80. left: 16,
  81. right: 16,
  82. bottom: 16
  83. })
  84. .width('100%')
  85. .height('100%')
  86. .justifyContent(FlexAlign.Start)
  87. }
  88. }
  ```

  [MultipleProperties.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/animation/entry/src/main/ets/pages/MultipleProperties.ets#L17-L183)

* 将相同动画参数的动画合并在一个动画闭包中，具体代码实现如下：

  ```
  1. @Component
  2. export struct MultipleProperties {
  3. @State w:number = 150
  4. @State h:number = 2
  5. @State brightNum:number = 1.5
  6. @State color:Color = Color.Red
  7. // ...
  8. // Unify animation closures while simultaneously setting changes for four properties
  9. func() {
  10. this.getUIContext().animateTo({curve: Curve.Sharp, duration: 1000}, () => {
  11. this.w = (this.w === 80 ? 150 : 80);
  12. this.color = (this.color === Color.Yellow ? Color.Red : Color.Yellow);
  13. this.h = (this.h === 2 ? 5 : 2);
  14. this.brightNum= (this.brightNum=== 1.5 ? 1 : 1.5);
  15. });
  16. }
  17. build() {
  18. Column() {
  19. Row() {
  20. Row() {
  21. Row()
  22. .width(this.w)
  23. .backgroundColor(this.color)
  24. .height(this.h)
  25. .brightness(this.brightNum)
  26. }
  27. .justifyContent(FlexAlign.Center)
  28. .width('50%')

  30. Row() {
  31. Row()
  32. .width(this.w)
  33. .backgroundColor(this.color)
  34. .height(this.h)
  35. .brightness(this.brightNum)
  36. }
  37. .justifyContent(FlexAlign.Center)
  38. .width('50%')
  39. }
  40. .height('25%')
  41. .width('100%')
  42. // ...

  44. Column() {
  45. // ...
  46. Button("Tap oneFunc")
  47. .width('100%')
  48. .margin({ top: 12 })
  49. // Key Attribute Settings
  50. .onClick(() => {
  51. // Loop animation by play count
  52. for (let i = 0; i < 10; i++) {
  53. setTimeout(() => {
  54. this.func();
  55. }, 1000 * i)
  56. }
  57. })
  58. }
  59. .justifyContent(FlexAlign.End)
  60. .height('25%')
  61. }
  62. .padding({
  63. left: 16,
  64. right: 16,
  65. bottom: 16
  66. })
  67. .width('100%')
  68. .height('100%')
  69. .justifyContent(FlexAlign.Start)
  70. }
  71. }
  ```

  [MultipleProperties.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/animation/entry/src/main/ets/pages/MultipleProperties.ets#L18-L182)

**性能分析**

使用DevEco Studio的Profiler工具检测下述指标，得到的数据如下所示：

**表4** **使用多个animateTo闭包和一个animateTo闭包实现****相同场景****的指标对比**

|  | 多个animateTo闭包 | 一个animateTo闭包 |
| --- | --- | --- |
| 丢帧率（%） | 9.6% | 4.0% |
| 最大连续丢帧数（帧） | 9 | 4 |
| 平均1s大卡顿次数（次/s） | 1.01 | 0.24 |

分析结论：

1）将四个属性变化动画分别放在四个animateTo动画闭包中，丢帧率为9.6%，最多连续丢失9帧，平均每秒发生大卡顿1.01次。

2）将四个属性变化动画合入一个animateTo动画闭包中，丢帧率降到了4.0%，最多连续丢失4帧，平均每秒发生大卡顿0.24次。

这一结果表明，将多个属性变化动画合并到同一个animateTo动画闭包中能够显著降低丢帧率和大卡顿的发生频率。合并动画操作可以减少不必要的布局计算和绘制开销，从而提升动画的流畅性和性能表现，有助于优化动画效果的性能。

### 多次animateTo时统一更新状态变量

使用animateTo方法执行动画时，会对执行动画闭包前后的状态进行对比，然后只对差异部分进行动画处理。

在动画执行过程中，脏节点是指在界面上需要进行重新绘制的区域。如果状态发生了变化，ArkUI会跟踪这些变化，并在动画闭包执行前进行状态对比，相关的脏节点会被标记为需要刷新，以便在动画闭包执行前对这些脏节点进行重新绘制。这样，只有发生变化的部分才会被纳入动画处理，而不需要重新绘制整个界面。

这种差异对比的方式能够显著减少不必要的绘制操作，提高动画的性能和流畅度。

**场景设计**

针对多个相同组件修改多个属性进行动画的场景（如下图所示），分别使用在多个animateTo之间更新状态变量、在animateTo之前显式指定属性初值、在animateTo之前使用原始状态实现。

**图13** 多个相同组件修改多个属性示意图  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/Hn7e_gogQumrC2KuNG3jVw/zh-cn_image_0000002193851988.gif?HW-CC-KV=V1&HW-CC-Date=20260428T001957Z&HW-CC-Expire=86400&HW-CC-Sign=3B7FAFF3A024176C8837DA1893C7EF817881FD3BD2A8C6F96326C468B3400D2D "点击放大")

**在多个animateTo之间更新状态变量**

如果多个animateTo之间存在状态更新，会导致执行下一个animateTo之前又存在需要更新的脏节点，可能造成冗余更新，其动画更新流程如下图所示：

**图14** 多个animateTo之间更新状态变量更新流程  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/S7WROQY5QOS-BGk9K1cL2A/zh-cn_image_0000002229337361.png?HW-CC-KV=V1&HW-CC-Date=20260428T001957Z&HW-CC-Expire=86400&HW-CC-Sign=946EF80AF79F2BA149E4DA713702DADBF185481773343B3DD0E6C5C6FD7DA2B6 "点击放大")

在第一个animateTo前，重新设置了w属性，所以Row组件需要更新一次。在第一个animateTo的动画闭包中，改变了w属性，所以Row组件又需要更新一次并对比产生宽高动画。第二个animateTo前，重新设置了color属性，所以Row组件又需要更新一次。在第二个animateTo的动画闭包中，改变了color属性，所以Row组件再更新一次并产生了背景色动画。Row组件总共更新了4次属性。

此外还更改了与动画无关的状态h，如果不需要改变无关状态，则不应改变造成冗余更新。

其具体代码实现如下：

```
1. @Component
2. export struct UpdateMultipleProperties {
3. @State w: number = 100
4. @State h: number = 2
5. @State color: Color = Color.Red

7. build() {
8. Column() {
9. Row() {
10. Row() {
11. Row()
12. .width(this.w)
13. .backgroundColor(this.color)
14. .height(this.h)
15. }
16. .justifyContent(FlexAlign.Center)
17. .width('50%')

19. Row() {
20. Row()
21. .width(this.w)
22. .backgroundColor(this.color)
23. .height(this.h)
24. }
25. .justifyContent(FlexAlign.Center)
26. .width('50%')
27. }
28. .height('25%')
29. .width('100%')

31. // ...
32. Column() {
33. Button('Tap1')
34. .width('100%')
35. .margin({ top: 12 })
36. .onClick(() => {
37. let doTimes = 5;
38. for (let i = 0; i < doTimes; i++) {
39. setTimeout(() => {
40. this.w = 80
41. this.h = 4
42. this.getUIContext().animateTo({ curve: Curve.Sharp, duration: 1000 }, () => {
43. this.w = (this.w === 80 ? 150 : 80);
44. });
45. // Updating state variables between two animateTo calls
46. this.color = Color.Yellow
47. this.getUIContext().animateTo({ curve: Curve.Linear, duration: 2000 }, () => {
48. this.color = (this.color === Color.Yellow ? Color.Red : Color.Yellow);
49. });
50. }, 2000 * i)
51. }
52. })
53. // ...
54. }
55. .justifyContent(FlexAlign.End)
56. .height('25%')
57. }
58. .padding({
59. left: 16,
60. right: 16,
61. bottom: 16
62. })
63. .width('100%')
64. .height('100%')
65. .justifyContent(FlexAlign.Start)
66. }
67. }
```

[UpdateMultipleProperties.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/animation/entry/src/main/ets/pages/UpdateMultipleProperties.ets#L17-L181)

**统一更新状态变量**

* 在animateTo之前显式指定属性初值

在animateTo之前显式的指定所有需要动画的属性初值，统一更新到节点中，然后再做动画，其动画更新流程如下图所示：

**图15** animateTo之前显式指定属性初值更新流程  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/SWQ2C8s3QuSgdjL_JHZvbw/zh-cn_image_0000002194011564.png?HW-CC-KV=V1&HW-CC-Date=20260428T001957Z&HW-CC-Expire=86400&HW-CC-Sign=313E313622F6A1410E43DFFA2F9353061EDAA8D4A6625DDBAC6088702F5A7551 "点击放大")

在第一个animateTo之前，重新设置了w和color属性，所以Row需要更新一次。在第一个animateTo的动画闭包中，改变了w属性，所以Row组件需要更新一次并对比产生宽高动画。在第二个animateTo之前，由于没有执行额外的语句，不存在需要更新的脏状态变量和脏节点，无需更新。在第二个animateTo的动画闭包中，改变了color属性，所以Row组件再更新一次并产生了背景色动画。Row组件总共更新了3次属性。

其具体代码实现如下：

```
1. @Component
2. export struct UpdateMultipleProperties {
3. @State w: number = 100
4. @State h: number = 2
5. @State color: Color = Color.Red

7. build() {
8. Column() {
9. Row() {
10. Row() {
11. Row()
12. .width(this.w)
13. .backgroundColor(this.color)
14. .height(this.h)
15. }
16. .justifyContent(FlexAlign.Center)
17. .width('50%')

19. Row() {
20. Row()
21. .width(this.w)
22. .backgroundColor(this.color)
23. .height(this.h)
24. }
25. .justifyContent(FlexAlign.Center)
26. .width('50%')
27. }
28. .height('25%')
29. .width('100%')

31. // ...
32. Column() {
33. // ...
34. Button('Tap2')
35. .width('100%')
36. .margin({ top: 12 })
37. .onClick(() => {
38. let doTimes = 5;
39. for (let i = 0; i < doTimes; i++) {
40. setTimeout(() => {
41. // Explicitly specify the initial values of all properties to be animated before the animation.
42. this.w = 80
43. this.color = Color.Yellow
44. this.getUIContext().animateTo({ curve: Curve.Sharp, duration: 1000 }, () => {
45. this.w = (this.w === 80 ? 150 : 80);
46. });
47. this.getUIContext().animateTo({ curve: Curve.Linear, duration: 2000 }, () => {
48. this.color = (this.color === Color.Yellow ? Color.Red : Color.Yellow);
49. });
50. // Refresh non-animated properties after animation completes
51. this.h = 5
52. }, 2000 * i)
53. }
54. })
55. // ...
56. }
57. .justifyContent(FlexAlign.End)
58. .height('25%')
59. }
60. .padding({
61. left: 16,
62. right: 16,
63. bottom: 16
64. })
65. .width('100%')
66. .height('100%')
67. .justifyContent(FlexAlign.Start)
68. }
69. }
```

[UpdateMultipleProperties.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/animation/entry/src/main/ets/pages/UpdateMultipleProperties.ets#L18-L182)

* 在animateTo之前使用原始状态

在animateTo之前使用原始状态，让动画从原始状态过渡到指定状态，其动画更新流程如下图所示：

**图16** animateTo之前使用原始状态更新流程  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/QhldDjf8S4qBxgxVZOVxqA/zh-cn_image_0000002229337381.png?HW-CC-KV=V1&HW-CC-Date=20260428T001957Z&HW-CC-Expire=86400&HW-CC-Sign=65F0E34427164C3C59B4E3F5AEC8D1A803FCC0E9D21EA18337422A28CA58957F "点击放大")

在第一个animateTo之前，不存在需要更新的脏状态变量和脏节点，无需更新。在第一个animateTo的动画闭包中，改变了w属性，所以Row组件需要更新一次并对比产生宽高动画。在第二个animateTo之前，由于也没有执行额外的语句，不存在需要更新的脏状态变量和脏节点，无需更新。在第二个animateTo的动画闭包中，改变了color属性，所以Row组件再更新一次并产生了背景色动画。Row组件总共更新了2次属性。

其具体代码实现如下：

```
1. @Component
2. export struct UpdateMultipleProperties {
3. @State w: number = 100
4. @State h: number = 2
5. @State color: Color = Color.Red

7. build() {
8. Column() {
9. Row() {
10. Row() {
11. Row()
12. .width(this.w)
13. .backgroundColor(this.color)
14. .height(this.h)
15. }
16. .justifyContent(FlexAlign.Center)
17. .width('50%')

19. Row() {
20. Row()
21. .width(this.w)
22. .backgroundColor(this.color)
23. .height(this.h)
24. }
25. .justifyContent(FlexAlign.Center)
26. .width('50%')
27. }
28. .height('25%')
29. .width('100%')

31. // ...
32. Column() {
33. // ...
34. Button('Tap3')
35. .width('100%')
36. .margin({ top: 12 })
37. .onClick(() => {
38. let doTimes = 5;
39. for (let i = 0; i < doTimes; i++) {
40. setTimeout(() => {
41. this.getUIContext().animateTo({ curve: Curve.Sharp, duration: 1000 }, () => {
42. this.w = (this.w === 80 ? 150 : 80);
43. });
44. this.getUIContext().animateTo({ curve: Curve.Linear, duration: 2000 }, () => {
45. this.color = (this.color === Color.Yellow ? Color.Red : Color.Yellow);
46. });
47. }, 2000 * i)
48. }
49. })
50. }
51. .justifyContent(FlexAlign.End)
52. .height('25%')
53. }
54. .padding({
55. left: 16,
56. right: 16,
57. bottom: 16
58. })
59. .width('100%')
60. .height('100%')
61. .justifyContent(FlexAlign.Start)
62. }
63. }
```

[UpdateMultipleProperties.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/animation/entry/src/main/ets/pages/UpdateMultipleProperties.ets#L19-L183)

**性能分析**

使用DevEco Studio的Profiler工具检测下述指标，得到的数据如下所示：

**表5** **状态变量更新位置不同的指标对比**

|  | 在多个animateTo之间更新状态变量 | 在animateTo之前显式指定属性初值 | 在animateTo之前使用原始状态 |
| --- | --- | --- | --- |
| 丢帧率（%） | 9.1% | 5.4% | 3.5% |
| 最大连续丢帧数（帧） | 15 | 10 | 5 |
| 平均1s大卡顿次数（次/s） | 0.67 | 0.23 | 0.10 |

分析结论：

1）在多个animateTo之间更新状态变量时，丢帧率高达9.1%，最大连续丢失15帧，平均每秒发生大卡顿0.67次。

2）在animateTo之前显式指定属性初值时，丢帧率降到了5.4%，最多连续丢失10帧，平均每秒发生大卡顿0.23次。

3）在animateTo之前使用原始状态时，丢帧率降到了3.5%，最多连续丢失5帧，平均每秒发生大卡顿0.10次。

在进行属性变化动画时，显式指定属性初值或者使用原始状态作为动画的起始状态能够显著降低丢帧率和大卡顿的发生频率。因此，在进行动画操作时，合理管理状态变量的更新和初始值设定对于优化动画效果的性能至关重要，开发者应根据需要，尽可能地避免在多个animateTo之间更新状态变量，从而提升动画的流畅性和性能表现。

### 使用renderGroup

renderGroup是组件通用方法，它代表了渲染绘制的一个组合。其核心功能就是标记组件，在绘制阶段将组件和其子组件的绘制结果进行合并并缓存，以达到复用的效果，从而降低绘制负载。

首次绘制组件时，若组件被标记为启用renderGroup状态，将对组件和其子组件进行离屏绘制，将绘制结果进行缓存。此后当需要重新绘制组件时，就会优先使用缓存而不必重新绘制，从而降低绘制负载，优化渲染性能。组件渲染流程图如下所示：

**图17** 组件渲染流程图  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/1kCfuMkXRS25kc78YBNdvA/zh-cn_image_0000002229451865.png?HW-CC-KV=V1&HW-CC-Date=20260428T001957Z&HW-CC-Expire=86400&HW-CC-Sign=FEF2D2473CD0ECFD59A15DD9E1564B1B2E1D888C45A8B077ED4DCFB153EA62D1 "点击放大")

在进行缓存更新时，需要满足以下三个条件：

* 组件在当前组件树上。
* 组件renderGroup被标记为true。
* 组件内容被标脏。

在进行缓存清理时，需要满足以下任意条件：

* 组件不存在于组件树上。
* 组件renderGroup被标记为false。

具体缓存管理流程图如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/328a2f-7TMKeWyRttxXpnA/zh-cn_image_0000002194011572.png?HW-CC-KV=V1&HW-CC-Date=20260428T001957Z&HW-CC-Expire=86400&HW-CC-Sign=263C0064129133C7D2010C4E978987E44E7B5A837EFE75CD5365B8B26D68DE98 "点击放大")

说明

为了能使renderGroup功能生效，组件存在以下约束。

* 组件内容固定不变：父组件和其子组件各属性保持固定，不发生变化。如果父组件内容不是固定的，也就是说其子组件中上存在某些属性变化或者样式变化的组件，此时如果使用renderGroup，那么缓存的利用率将大大下降，并且有可能需要不断执行缓存更新逻辑，在这种情况下，不仅不能优化卡顿效果，甚至还可能使卡顿恶化。例如：文本内容使用双向绑定的动态数据；图片资源使用gif格式；使用video组件播放视频。
* 子组件无动效：由父组件统一应用动效，其子组件均无动效。如果子组件上也应用动效，那么子组件相对父组件就不再是静止的，每一帧都有可能需要更新缓存，更新逻辑同样需要消耗系统资源。

**场景设计**

此案例在同一个页面下使用了固定的图片和文本内容，并且每个组件统一使用旋转和缩放的动效，并且重复使用了60个这样的组件。

**图18** renderGroup案例实现图  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/dHi5rAyCTL-Po5yvopH6NA/zh-cn_image_0000002229451857.gif?HW-CC-KV=V1&HW-CC-Date=20260428T001957Z&HW-CC-Expire=86400&HW-CC-Sign=162913CB7A065195F2F485E2B4F97FB09189294F8EC64F171D870B02C61B97EB "点击放大")

**代码实现**

实现页面中需要使用的组件，并设置renderGroup属性，用@StorageLink修饰绑定renderGroupFlag标识。renderGroup属性的设置要满足父组件统一应用动效，子组件无动效，所以，动效在父组件上统一实现，未在IconItem上设置动效。在Flex组件中，Image和Text都无动效设置，所以在最外层Flex上设置renderGroup属性即可。

具体代码如下所示：

```
1. @Component
2. export  struct IconItem {
3. @StorageLink('renderGroupFlag') renderGroupFlag: boolean = false;
4. image: string | Resource = '';
5. text: string | Resource = '';

7. build() {
8. Flex({
9. direction: FlexDirection.Column,
10. justifyContent: FlexAlign.Center,
11. alignContent: FlexAlign.Center
12. }) {
13. Image(this.image)
14. .height(20)
15. .width(20)
16. .objectFit(ImageFit.Contain)
17. .margin({ left: 15 })

19. Text(this.text)
20. .fontSize(10)
21. .fontColor('#182431')
22. .margin({ top: 5 })
23. .width(50)
24. .opacity(0.8)
25. .textAlign(TextAlign.Center)
26. }
27. .backgroundColor('#e3e3e3')
28. .width(50)
29. .height(50)
30. .borderRadius(25)
31. // Call renderGroup within IconItem, false to disable, true to enable.
32. .renderGroup(this.renderGroupFlag)
33. }
34. }
```

[IconItem.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/animation/entry/src/main/ets/pages/IconItem.ets#L17-L50)

实现展示的页面，将控制renderGroup的标识renderGroupFlag通过APPStorage进行存储。

```
1. import { IconItem } from './IconItem'

3. class IconItemSource {
4. image: string | Resource = ''
5. text: string | Resource = ''

7. constructor(image: string | Resource = '', text: string | Resource = '') {
8. this.image = image;
9. this.text = text;
10. }
11. }

13. @Component
14. export struct RenderGroup {
15. @State renderGroupFlag: boolean = false;
16. private iconItemSourceList: IconItemSource[] = [];

18. aboutToAppear() {
19. for (let index = 0; index < 20; index++) {
20. const numStart: number = index * 3;
21. this.iconItemSourceList.push(
22. new IconItemSource($r('app.media.app_icon'), `item${numStart + 1}`),
23. new IconItemSource($r('app.media.app_icon'), `item${numStart + 2}`),
24. new IconItemSource($r('app.media.app_icon'), `item${numStart + 3}`),
25. );
26. }
27. }

29. build() {
30. Column() {
31. Row() {
32. Row() {
33. Text('Example')
34. .fontSize(24)
35. .lineHeight(24)
36. .fontColor(Color.Black)
37. .fontWeight(FontWeight.Bold)
38. .margin({ left: 30 })
39. }

41. // Dynamic switching of renderGroup functionality
42. Stack({ alignContent: Alignment.End }) {
43. Button(this.renderGroupFlag ? 'renderGroup On' : 'renderGroup Off', {
44. type: ButtonType.Normal,
45. stateEffect: true
46. })
47. .fontSize(12)
48. .borderRadius(8)
49. .width(150)
50. .height(30)
51. .margin({ right: 30 })
52. .onClick(() => {
53. this.renderGroupFlag = !this.renderGroupFlag;
54. AppStorage.setOrCreate('renderGroupFlag', this.renderGroupFlag)
55. })
56. }
57. }
58. .height(56)
59. .width('100%')
60. .justifyContent(FlexAlign.SpaceBetween)

62. GridRow({
63. columns: 6,
64. gutter: { x: 0, y: 0 },
65. breakpoints: {
66. value: ['400vp', '600vp', '800vp'],
67. reference: BreakpointsReference.WindowSize
68. },
69. direction: GridRowDirection.Row
70. }) {
71. ForEach(this.iconItemSourceList, (item: IconItemSource) => {
72. GridCol() {
73. IconItem({ image: item.image, text: item.text })
74. .transition(
75. TransitionEffect.scale({ x: 0.5, y: 0.5 })
76. .animation({ duration: 3000, curve: Curve.FastOutSlowIn, iterations: -1 })
77. .combine(TransitionEffect.rotate({ z: 1, angle: 360 }))
78. )
79. }
80. .height(70)
81. .width('25%')
82. })
83. }
84. .width('100%')
85. .height('100%')
86. }
87. .width('100%')
88. .height('100%')
89. .alignItems(HorizontalAlign.Center)
90. }
91. }
```

[RenderGroup.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/animation/entry/src/main/ets/pages/RenderGroup.ets#L17-L107)

**性能分析**

使用DevEco Studio的Profiler工具检测下述指标，得到的数据如下所示：

**表6** 未开启renderGroup、开启renderGroup相同场景的指标对比

|  | 未开启renderGroup | 开启renderGroup |
| --- | --- | --- |
| 丢帧率（%） | 52.3% | 0% |
| 最大连续丢帧数（帧） | 36 | 0 |
| 平均1s大卡顿次数（次/s） | 2.3 | 0 |

分析结论：

1）未开启renderGroup时，在render\_service侧的丢帧率为52.3%，最多连续丢失36帧，平均每秒发生大卡顿2.3次。

2）开启renderGroup时，既没有发生卡顿，也没有发生丢帧的情况，其丢帧率为0%。

这一结果表明，在满足上述的约束后，使用renderGroup时，能够显著降低丢帧率、最大连续丢帧数和平均1s大卡顿次数。因此，在单一页面上存在大量应用动效的组件，且组件和其子组件各属性保持固定、组件统一应用动效时，开发者可以使用renderGroup来提升应用的性能，保证应用及动画的流畅性。

### 提升动画运行流畅度总结

本文通过5个测试验证了使用系统提供的动画接口、使用图形变换属性变化组件布局、参数相同时使用同一个animateTo、多次animateTo时统一更新状态变量、使用renderGroup这五项措施的有效性。

动画的性能表现对于用户体验、设备资源消耗、应用稳定性和流量消耗等方面都具有重要意义：

* 用户体验：流畅的动画能够提升用户体验，使用户感到界面更加生动和直观。相反，卡顿或者延迟的动画会带来不良的体验。
* 设备资源消耗：动画的性能表现会直接影响设备的资源消耗，尤其是CPU和GPU的占用。低性能的动画可能导致设备发热、耗电量增加，甚至影响其他应用的运行。
* 应用稳定性：性能较差的动画可能会导致应用崩溃或者卡顿，影响应用的稳定性和可靠性。
* 节省流量：高性能的动画可以减少数据传输量，对于移动应用来说，这意味着可以节省用户的流量消耗。
* 适应不同设备：不同设备的性能差异很大，提升动画性能可以使应用在各种设备上都能够流畅运行。

在实际开发中，开发人员可以结合本文提出的四项措施，并根据具体场景和需求进行优化，从而达到更好的动画性能表现。

## 合理使用动画总结

在实际开发过程中，开发者应该充分认识到动画对用户体验的重要性。动画不仅可以增强应用的吸引力，还能够提升用户的参与感和操作的直观性。

本文通过两个角度介绍了如何合理使用动画：

* 提升动画感知流畅度：首先，从UX设计视角出发，开发者需要理解动画在用户体验中的作用和意义。其次，开发者需要具备一定的动画实现技术，能够根据设计需求，合理、高效地使用动画能力实现各类动画效果。
* 提升动画运行流畅度：为了进一步提升动画性能，开发者还需要采取一些措施。例如，可以通过使用系统提供的动画接口、使用图形变换属性变化组件布局、参数相同时使用同一个animateTo、多次animateTo时统一更新状态变量等方式，有效减少动画对系统资源的占用，提升动画的流畅度和稳定性。

总之，合理使用动画对于提升用户体验至关重要。开发者需要从UX设计视角转换为开发实现视角，充分认识动画在用户体验中的作用和意义，并通过合理的实现和性能优化来提升动画的效果和稳定性。
