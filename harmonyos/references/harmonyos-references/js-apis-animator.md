---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-animator
title: @ohos.animator (动画)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.animator (动画)
category: harmonyos-references
scraped_at: 2026-04-28T08:00:17+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6c0ded2fbaf9497a6b2c23af1268693a3172ddd819600d8337a1bf28ccd71d0c
---

本模块提供组件动画效果，包括定义动画、启动动画和以相反的顺序播放动画等。

说明

* 本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块从API version 9开始支持在ArkTS中使用。
* 该模块不支持在[UIAbility](js-apis-app-ability-uiability.md)的文件声明处使用，即不能在UIAbility的生命周期中调用，需要在创建组件实例后使用。
* 本模块功能依赖UI的执行上下文，不可在[UI上下文不明确](../harmonyos-guides/arkts-global-interface.md#ui上下文不明确)的地方使用，参见[UIContext](arkts-apis-uicontext-uicontext.md)说明。
* 自定义组件中通常会持有一个由[createAnimator](arkts-apis-uicontext-uicontext.md#createanimator)接口返回的[AnimatorResult](js-apis-animator.md#animatorresult)对象，以确保动画对象在动画过程中不被析构，该对象通过回调捕获了自定义组件对象，因此需要在自定义组件销毁时的[aboutToDisappear](ts-custom-component-lifecycle.md#abouttodisappear)生命周期中释放动画对象，以避免因循环依赖导致内存泄漏。详细示例可参考：[基于ArkTS扩展的声明式开发范式](js-apis-animator.md#基于arkts扩展的声明式开发范式)。
* Animator对象析构或主动调用[cancel](js-apis-animator.md#cancel)、[finish](js-apis-animator.md#finish)方法时，都会触发一次额外的[onFrame](js-apis-animator.md#属性)，返回值是动画终点值。因此，如果在动画过程中调用[cancel](js-apis-animator.md#cancel)、[finish](js-apis-animator.md#finish)，会导致属性值在一帧内跳变至终点。若希望动画在中途暂停，可先将onFrame设置为空函数，再调用[finish](js-apis-animator.md#finish)。
* 对于无限循环的Animator动画，即使开发者选项中将全局动画速率设置为0（关闭动画），循环动画仍会继续执行。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { Animator as animator, AnimatorOptions, AnimatorResult, SimpleAnimatorOptions } from '@kit.ArkUI';
```

## Animator

PhonePC/2in1TabletTVWearable

定义Animator类。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### create(deprecated)

PhonePC/2in1TabletTVWearable

create(options: AnimatorOptions): AnimatorResult

创建animator动画结果对象（AnimatorResult）。

说明

* 从API version 9开始支持，从API version 18开始废弃，建议使用[createAnimator](arkts-apis-uicontext-uicontext.md#createanimator)替代。
* 从API version 10开始，可以通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[createAnimator](arkts-apis-uicontext-uicontext.md#createanimator)来明确UI的执行上下文。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [AnimatorOptions](js-apis-animator.md#animatoroptions) | 是 | 定义动画选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AnimatorResult](js-apis-animator.md#animatorresult) | Animator结果接口。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

完整示例请参考[基于ArkTS扩展的声明式开发范式](js-apis-animator.md#基于arkts扩展的声明式开发范式)。

说明

推荐通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[createAnimator](arkts-apis-uicontext-uicontext.md#createanimator)接口明确UI上下文。

```
1. import { Animator as animator, AnimatorOptions } from '@kit.ArkUI';

3. let options: AnimatorOptions = {
4. duration: 1500,
5. easing: "friction",
6. delay: 0,
7. fill: "forwards",
8. direction: "normal",
9. iterations: 3,
10. begin: 200.0,
11. end: 400.0
12. };
13. animator.create(options); // 建议使用 UIContext.createAnimator()接口
```

### create18+

PhonePC/2in1TabletTVWearable

create(options: AnimatorOptions | SimpleAnimatorOptions): AnimatorResult

创建animator动画结果对象（AnimatorResult）。与[create](js-apis-animator.md#createdeprecated)相比，新增对[SimpleAnimatorOptions](js-apis-animator.md#simpleanimatoroptions18)类型入参的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [AnimatorOptions](js-apis-animator.md#animatoroptions) | [SimpleAnimatorOptions](js-apis-animator.md#simpleanimatoroptions18) | 是 | 定义动画参数选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AnimatorResult](js-apis-animator.md#animatorresult) | Animator结果接口。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

完整示例请参考[基于ArkTS扩展的声明式开发范式](js-apis-animator.md#基于arkts扩展的声明式开发范式)。

说明

推荐通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[createAnimator](arkts-apis-uicontext-uicontext.md#createanimator)接口明确UI上下文。

```
1. import { Animator as animator, SimpleAnimatorOptions } from '@kit.ArkUI';
2. let options: SimpleAnimatorOptions = new SimpleAnimatorOptions(100, 200).duration(2000);
3. animator.create(options);// 建议使用 UIContext.createAnimator()接口
```

### createAnimator(deprecated)

PhonePC/2in1TabletTVWearable

createAnimator(options: AnimatorOptions): AnimatorResult

创建动画。

说明

从API version 6开始支持，从API version 9开始废弃，建议使用[create](js-apis-animator.md#createdeprecated)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [AnimatorOptions](js-apis-animator.md#animatoroptions) | 是 | 定义动画选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AnimatorResult](js-apis-animator.md#animatorresult) | Animator结果接口。 |

**示例：**

完整示例请参考[基于ArkTS扩展的声明式开发范式](js-apis-animator.md#基于arkts扩展的声明式开发范式)。

```
1. import { Animator as animator } from '@kit.ArkUI';

3. let options: AnimatorOptions = {
4. // xxx.js文件中不需要强调显式类型AnimatorOptions
5. duration: 1500,
6. easing: "friction",
7. delay: 0,
8. fill: "forwards",
9. direction: "normal",
10. iterations: 3,
11. begin: 200.0,
12. end: 400.0,
13. };
14. this.animator = animator.createAnimator(options);
```

## AnimatorResult

PhonePC/2in1TabletTVWearable

定义Animator结果接口。

### 属性

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| onFrame12+ | (progress: number) => void | 否 | 否 | 接收到帧时回调。  progress表示动画的当前值。取值范围为[AnimatorOptions](js-apis-animator.md#animatoroptions)定义的[begin, end]，默认取值范围为[0, 1]。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| onFinish12+ | () => void | 否 | 否 | 动画完成时回调。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| onCancel12+ | () => void | 否 | 否 | 动画被取消时回调。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| onRepeat12+ | () => void | 否 | 否 | 动画重复时回调。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| onframe(deprecated) | (progress: number) => void | 否 | 否 | 接收到帧时回调。  **说明:** 从API version 6开始支持，从API version 12开始废弃，推荐使用onFrame。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| onfinish(deprecated) | () => void | 否 | 否 | 动画完成时回调。  **说明:** 从API version 6开始支持，从API version 12开始废弃，推荐使用onFinish。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| oncancel(deprecated) | () => void | 否 | 否 | 动画被取消时回调。  **说明:** 从API version 6开始支持，从API version 12开始废弃，推荐使用onCancel。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| onrepeat(deprecated) | () => void | 否 | 否 | 动画重复时回调。  **说明:** 从API version 6开始支持，从API version 12开始废弃，推荐使用onRepeat。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |

### reset9+

PhonePC/2in1TabletTVWearable

reset(options: AnimatorOptions): void

重置当前animator动画参数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [AnimatorOptions](js-apis-animator.md#animatoroptions) | 是 | 定义动画选项。 |

**错误码：**

以下错误码的详细介绍请参考[通用错误码](errorcode-universal.md)和[接口调用异常错误码](errorcode-internal.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | The specified page is not found or the object property list is not obtained. |

**示例：**

```
1. import { AnimatorResult } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct AnimatorTest {
6. private animatorResult: AnimatorResult | undefined = undefined;

8. create() {
9. this.animatorResult = this.getUIContext().createAnimator({
10. duration: 1500,
11. easing: "friction",
12. delay: 0,
13. fill: "forwards",
14. direction: "normal",
15. iterations: 3,
16. begin: 200.0,
17. end: 400.0
18. })
19. this.animatorResult.reset({
20. duration: 1500,
21. easing: "friction",
22. delay: 0,
23. fill: "forwards",
24. direction: "normal",
25. iterations: 5,
26. begin: 200.0,
27. end: 400.0
28. });
29. }

31. build() {
32. // ......
33. }
34. }
```

### reset18+

PhonePC/2in1TabletTVWearable

reset(options: AnimatorOptions | SimpleAnimatorOptions): void

重置当前animator动画参数。与[reset](js-apis-animator.md#reset9)相比，新增对[SimpleAnimatorOptions](js-apis-animator.md#simpleanimatoroptions18)类型入参的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [AnimatorOptions](js-apis-animator.md#animatoroptions) | [SimpleAnimatorOptions](js-apis-animator.md#simpleanimatoroptions18) | 是 | 定义动画选项。 |

**错误码：**

以下错误码的详细介绍请参考[通用错误码](errorcode-universal.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | The specified page is not found or the object property list is not obtained. |

**示例：**

完整示例请参考[基于ArkTS扩展的声明式开发范式](js-apis-animator.md#基于arkts扩展的声明式开发范式)。

```
1. import { Animator as animator, AnimatorResult, AnimatorOptions, SimpleAnimatorOptions } from '@kit.ArkUI';

3. let options: AnimatorOptions = {
4. duration: 1500,
5. easing: "ease",
6. delay: 0,
7. fill: "forwards",
8. direction: "normal",
9. iterations: 1,
10. begin: 100,
11. end: 200
12. };
13. let optionsNew: SimpleAnimatorOptions = new SimpleAnimatorOptions(100, 200)
14. .duration(2000)
15. .iterations(3)
16. .delay(1000);
17. let animatorResult: AnimatorResult = animator.create(options);
18. animatorResult.reset(optionsNew);
```

### play

PhonePC/2in1TabletTVWearable

play(): void

启动动画。动画会保留上一次的播放状态，比如播放状态设置reverse后，再次播放会保留reverse的播放状态。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

完整示例请参考[基于ArkTS扩展的声明式开发范式](js-apis-animator.md#基于arkts扩展的声明式开发范式)。

```
1. animator.play();
```

### finish

PhonePC/2in1TabletTVWearable

finish(): void

结束动画，会触发[onFinish](js-apis-animator.md#属性)回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

完整示例请参考[基于ArkTS扩展的声明式开发范式](js-apis-animator.md#基于arkts扩展的声明式开发范式)。

```
1. animator.finish();
```

### pause

PhonePC/2in1TabletTVWearable

pause(): void

暂停动画。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

完整示例请参考[基于ArkTS扩展的声明式开发范式](js-apis-animator.md#基于arkts扩展的声明式开发范式)。

```
1. animator.pause();
```

### cancel

PhonePC/2in1TabletTVWearable

cancel(): void

取消动画，会触发[onCancel](js-apis-animator.md#属性)回调。此接口和[finish](js-apis-animator.md#finish)接口功能上没有区别，仅触发的回调不同，建议使用finish接口结束动画。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

完整示例请参考[基于ArkTS扩展的声明式开发范式](js-apis-animator.md#基于arkts扩展的声明式开发范式)。

```
1. animator.cancel();
```

### reverse

PhonePC/2in1TabletTVWearable

reverse(): void

以相反的顺序播放动画。使用interpolating-spring曲线时此接口无效。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

完整示例请参考[基于ArkTS扩展的声明式开发范式](js-apis-animator.md#基于arkts扩展的声明式开发范式)。

```
1. animator.reverse();
```

### setExpectedFrameRateRange12+

PhonePC/2in1TabletTVWearable

setExpectedFrameRateRange(rateRange: ExpectedFrameRateRange): void

设置期望的帧率范围。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rateRange | [ExpectedFrameRateRange](ts-explicit-animation.md#expectedframeraterange11) | 是 | 设置期望的帧率范围。 |

说明

开发者通过设置有效的期望帧率后，系统会收集设置的请求帧率，进行决策和分发，在渲染管线上进行分频，尽量能够满足开发者的期望帧率。开发者设置的期望帧率值不能代表最终实际效果，会受限于系统能力和屏幕刷新率。

**示例：**

```
1. import { AnimatorResult } from '@kit.ArkUI';

3. let expectedFrameRate: ExpectedFrameRateRange = {
4. min: 0,
5. max: 120,
6. expected: 30
7. }

9. @Entry
10. @Component
11. struct AnimatorTest {
12. private backAnimator: AnimatorResult | undefined = undefined

14. create() {
15. this.backAnimator = this.getUIContext().createAnimator({
16. duration: 2000,
17. easing: "ease",
18. delay: 0,
19. fill: "forwards",
20. direction: "normal",
21. iterations: 1,
22. begin: 100, // 动画插值起点
23. end: 200 // 动画插值终点
24. })
25. this.backAnimator.setExpectedFrameRateRange(expectedFrameRate);
26. }

28. build() {
29. // ......
30. }
31. }
```

### update(deprecated)

PhonePC/2in1TabletTVWearable

update(options: AnimatorOptions): void

更新当前动画器。

说明

从API version 6开始支持，从API version 9开始废弃。建议使用[reset](js-apis-animator.md#reset9)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [AnimatorOptions](js-apis-animator.md#animatoroptions) | 是 | 定义动画选项。 |

**示例：**

完整示例请参考[基于ArkTS扩展的声明式开发范式](js-apis-animator.md#基于arkts扩展的声明式开发范式)。

```
1. animator.update(options);
```

## AnimatorOptions

PhonePC/2in1TabletTVWearable

定义动画选项。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| duration | number | 否 | 否 | 动画播放的时长，单位毫秒。  取值范围：[0, +∞)  默认值：0 |
| easing | string | 否 | 否 | 动画插值曲线，支持的曲线类型可参考表1。  非法字符串时取:"ease"。 |
| delay | number | 否 | 否 | 动画延时播放时长，单位毫秒，设置为0时，表示不延时。设置为负数时动画提前播放，如果提前播放的时长大于动画总时长，动画直接过渡到终点。  默认值：0 |
| fill | 'none' | 'forwards' | 'backwards' | 'both' | 否 | 否 | 动画执行后是否恢复到初始状态，动画执行后，动画结束时的状态（在最后一个关键帧中定义）将保留。  'none'：在动画执行之前和之后都不会应用任何样式到目标上。  'forwards'：在动画结束后，目标将保留动画结束时的状态（在最后一个关键帧中定义）。  'backwards'：动画将在[AnimatorOptions](js-apis-animator.md#animatoroptions)中的delay期间应用第一个关键帧中定义的值。当[AnimatorOptions](js-apis-animator.md#animatoroptions)中的direction为'normal'或'alternate'时应用from关键帧中的值，当[AnimatorOptions](js-apis-animator.md#animatoroptions)中的direction为'reverse'或'alternate-reverse'时应用to关键帧中的值。  'both'：动画将遵循forwards和backwards的规则，从而在两个方向上扩展动画属性。 |
| direction | 'normal' | 'reverse' | 'alternate' | 'alternate-reverse' | 否 | 否 | 动画播放模式。  'normal'： 动画正向循环播放。  'reverse'： 动画反向循环播放。  'alternate'：动画交替循环播放，奇数次正向播放，偶数次反向播放。  'alternate-reverse'：动画反向交替循环播放，奇数次反向播放，偶数次正向播放。  默认值：'normal' |
| iterations | number | 否 | 否 | 动画播放次数。设置为0时不播放，设置为-1时无限次播放，设置大于0时为播放次数。  **说明:** 设置为除-1外其他负数视为无效取值，无效取值动画默认播放1次。 |
| begin | number | 否 | 否 | 动画插值起点。  **说明:** 会影响[onFrame](js-apis-animator.md#属性)回调的入参值。  默认值：0 |
| end | number | 否 | 否 | 动画插值终点。  **说明:** 会影响[onFrame](js-apis-animator.md#属性)回调的入参值。  默认值：1 |

**表1 支持的曲线类型：**

| 类型 | 说明 |
| --- | --- |
| "linear" | 动画线性变化。 |
| "ease" | 动画开始和结束时的速度较慢，cubic-bezier(0.25, 0.1, 0.25, 1.0)。 |
| "ease-in" | 动画播放速度先慢后快，cubic-bezier(0.42, 0.0, 1.0, 1.0)。 |
| "ease-out" | 动画播放速度先快后慢，cubic-bezier(0.0, 0.0, 0.58, 1.0)。 |
| "ease-in-out" | 动画播放速度先加速后减速，cubic-bezier(0.42, 0.0, 0.58, 1.0)。 |
| "fast-out-slow-in" | 标准曲线，cubic-bezier(0.4, 0.0, 0.2, 1.0)。 |
| "linear-out-slow-in" | 减速曲线，cubic-bezier(0.0, 0.0, 0.2, 1.0)。 |
| "fast-out-linear-in" | 加速曲线，cubic-bezier(0.4, 0.0, 1.0, 1.0)。 |
| "friction" | 阻尼曲线，cubic-bezier(0.2, 0.0, 0.2, 1.0)。 |
| "extreme-deceleration" | 急缓曲线，cubic-bezier(0.0, 0.0, 0.0, 1.0)。 |
| "rhythm" | 节奏曲线，cubic-bezier(0.7, 0.0, 0.2, 1.0)。 |
| "sharp" | 锐利曲线，cubic-bezier(0.33, 0.0, 0.67, 1.0)。 |
| "smooth" | 平滑曲线，cubic-bezier(0.4, 0.0, 0.4, 1.0)。 |
| "cubic-bezier(x1, y1, x2, y2)" | 三次贝塞尔曲线，x1、x2的值必须处于0-1之间。例如"cubic-bezier(0.42, 0.0, 0.58, 1.0)"。 |
| "steps(number, step-position)" | 阶梯曲线，number必须设置，为正整数，step-position参数可选，支持设置start或end，默认值为end。例如"steps(3, start)"。 |
| interpolating-spring(velocity, mass, stiffness, damping) | 插值弹簧曲线。  velocity、mass、stiffness、damping都是数值类型，且mass、stiffness、damping参数均应该大于0，具体参数含义参考[插值弹簧曲线](js-apis-curve.md#curvesinterpolatingspring10)。  使用interpolating-spring时，duration不生效，由弹簧参数决定；fill、direction、iterations设置无效，fill固定设置为"forwards"，direction固定设置为"normal"，iterations固定设置为1，且对animator的[reverse](js-apis-animator.md#reverse)函数调用无效。即animator使用interpolating-spring时只能正向播放1次。  从API version 11开始支持且仅在ArkTS中支持使用。 |

## SimpleAnimatorOptions18+

PhonePC/2in1TabletTVWearable

animator简易动画参数对象。与AnimatorOptions相比，部分动画参数有默认值，可不设置。

### constructor18+

PhonePC/2in1TabletTVWearable

constructor(begin: number, end: number)

SimpleAnimatorOptions的构造函数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| begin | number | 是 | 动画插值起点。 |
| end | number | 是 | 动画插值终点。 |

**示例：**

完整示例请参考[基于ArkTS扩展的声明式开发范式](js-apis-animator.md#基于arkts扩展的声明式开发范式)。

```
1. import { AnimatorResult, SimpleAnimatorOptions } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct AnimatorTest {
6. private animatorResult: AnimatorResult | undefined = undefined;
7. options: SimpleAnimatorOptions = new SimpleAnimatorOptions(100, 200); // 动画插值过程从100到200，其余动画参数使用默认值。

9. create() {
10. this.animatorResult = this.getUIContext().createAnimator(this.options);
11. }

13. build() {
14. // ......
15. }
16. }
```

### duration18+

PhonePC/2in1TabletTVWearable

duration(duration: number): SimpleAnimatorOptions

设置animator动画时长。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| duration | number | 是 | 设置动画时长，单位毫秒。  默认值：1000 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SimpleAnimatorOptions](js-apis-animator.md#simpleanimatoroptions18) | Animator简易动画参数对象。 |

**示例：**

完整示例请参考[基于ArkTS扩展的声明式开发范式](js-apis-animator.md#基于arkts扩展的声明式开发范式)。

```
1. import { AnimatorResult, SimpleAnimatorOptions } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct AnimatorTest {
6. private animatorResult: AnimatorResult | undefined = undefined;
7. options: SimpleAnimatorOptions = new SimpleAnimatorOptions(100, 200).duration(500);

9. create() {
10. this.animatorResult = this.getUIContext().createAnimator(this.options);
11. }

13. build() {
14. // ......
15. }
16. }
```

### easing18+

PhonePC/2in1TabletTVWearable

easing(curve: string): SimpleAnimatorOptions

设置animator动画插值曲线。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| curve | string | 是 | 设置animator动画插值曲线，具体说明参考[AnimatorOptions](js-apis-animator.md#animatoroptions)。  默认值：“ease” |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SimpleAnimatorOptions](js-apis-animator.md#simpleanimatoroptions18) | Animator简易动画参数对象。 |

**示例：**

完整示例请参考[基于ArkTS扩展的声明式开发范式](js-apis-animator.md#基于arkts扩展的声明式开发范式)。

```
1. import { AnimatorResult, SimpleAnimatorOptions } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct AnimatorTest {
6. private animatorResult: AnimatorResult | undefined = undefined;
7. options: SimpleAnimatorOptions = new SimpleAnimatorOptions(100, 200).easing("ease-in");

9. create() {
10. this.animatorResult = this.getUIContext().createAnimator(this.options);
11. }

13. build() {
14. // ......
15. }
16. }
```

### delay18+

PhonePC/2in1TabletTVWearable

delay(delay: number): SimpleAnimatorOptions

设置animator动画播放时延。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| delay | number | 是 | 设置animator动画播放时延，单位毫秒，设置为0时，表示不延时。设置为负数时动画提前播放，如果提前播放的时长大于动画总时长，动画直接过渡到终点。  默认值：0 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SimpleAnimatorOptions](js-apis-animator.md#simpleanimatoroptions18) | Animator简易动画参数对象。 |

**示例：**

完整示例请参考[基于ArkTS扩展的声明式开发范式](js-apis-animator.md#基于arkts扩展的声明式开发范式)。

```
1. import { AnimatorResult, SimpleAnimatorOptions } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct AnimatorTest {
6. private animatorResult: AnimatorResult | undefined = undefined;
7. options: SimpleAnimatorOptions = new SimpleAnimatorOptions(100, 200).delay(500);

9. create() {
10. this.animatorResult = this.getUIContext().createAnimator(this.options);
11. }

13. build() {
14. // ......
15. }
16. }
```

### fill18+

PhonePC/2in1TabletTVWearable

fill(fillMode: [FillMode](ts-appendix-enums.md#fillmode)): SimpleAnimatorOptions

设置animator动画填充方式。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fillMode | [FillMode](ts-appendix-enums.md#fillmode) | 是 | 设置animator动画填充方式，影响动画delay期间和结束时的表现。  默认值：FillMode.Forwards |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SimpleAnimatorOptions](js-apis-animator.md#simpleanimatoroptions18) | Animator简易动画参数对象。 |

**示例：**

完整示例请参考[基于ArkTS扩展的声明式开发范式](js-apis-animator.md#基于arkts扩展的声明式开发范式)。

```
1. import { AnimatorResult, SimpleAnimatorOptions } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct AnimatorTest {
6. private animatorResult: AnimatorResult | undefined = undefined;
7. options: SimpleAnimatorOptions = new SimpleAnimatorOptions(100, 200).fill(FillMode.Forwards);

9. create() {
10. this.animatorResult = this.getUIContext().createAnimator(this.options);
11. }

13. build() {
14. // ......
15. }
16. }
```

### direction18+

PhonePC/2in1TabletTVWearable

direction(direction: [PlayMode](ts-appendix-enums.md#playmode)): SimpleAnimatorOptions

设置animator动画播放方向。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| direction | [PlayMode](ts-appendix-enums.md#playmode) | 是 | 设置animator动画播放方向。  默认值：PlayMode.Normal |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SimpleAnimatorOptions](js-apis-animator.md#simpleanimatoroptions18) | Animator简易动画参数对象。 |

**示例：**

完整示例请参考[基于ArkTS扩展的声明式开发范式](js-apis-animator.md#基于arkts扩展的声明式开发范式)。

```
1. import { AnimatorResult, SimpleAnimatorOptions } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct AnimatorTest {
6. private animatorResult: AnimatorResult | undefined = undefined;
7. options: SimpleAnimatorOptions = new SimpleAnimatorOptions(100, 200).direction(PlayMode.Alternate);

9. create() {
10. this.animatorResult = this.getUIContext().createAnimator(this.options);
11. }

13. build() {
14. // ......
15. }
16. }
```

### iterations18+

PhonePC/2in1TabletTVWearable

iterations(iterations: number): SimpleAnimatorOptions

设置animator动画播放次数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| iterations | number | 是 | 设置animator动画播放次数，设置为0时不播放，设置为-1时无限次播放。  默认值：1 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SimpleAnimatorOptions](js-apis-animator.md#simpleanimatoroptions18) | Animator简易动画参数对象。 |

**示例：**

完整示例请参考[基于ArkTS扩展的声明式开发范式](js-apis-animator.md#基于arkts扩展的声明式开发范式)。

```
1. import { AnimatorResult, SimpleAnimatorOptions } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct AnimatorTest {
6. private animatorResult: AnimatorResult | undefined = undefined;
7. options: SimpleAnimatorOptions = new SimpleAnimatorOptions(100, 200).iterations(3);

9. create() {
10. this.animatorResult = this.getUIContext().createAnimator(this.options);
11. }

13. build() {
14. // ......
15. }
16. }
```

## 完整示例

PhonePC/2in1TabletTVWearable

### 基于JS扩展的类Web开发范式

```
1. <!-- hml -->
2. <div class="container">
3. <div class="Animation" style="height: {{divHeight}}px; width: {{divWidth}}px; background-color: red;" onclick="Show">
4. </div>
5. </div>
```

```
1. import { Animator as animator, AnimatorResult } from '@kit.ArkUI';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let DataTmp: Record<string, Animator> = {
5. 'divWidth': 200,
6. 'divHeight': 200,
7. 'animator': animator
8. }

10. class Tmp {
11. data: animator = DataTmp
12. onInit: Function = () => {
13. }
14. Show: Function = () => {
15. }
16. }

18. class DateT {
19. divWidth: number = 0
20. divHeight: number = 0
21. animator: AnimatorResult | null = null
22. }

24. (Fn: (v: Tmp) => void) => {
25. Fn({
26. data: DataTmp,
27. onInit() {
28. let options: AnimatorOptions = {
29. duration: 1500,
30. easing: "friction",
31. delay: 0,
32. fill: "forwards",
33. direction: "normal",
34. iterations: 2,
35. begin: 200.0,
36. end: 400.0
37. };
38. let DataTmp: DateT = {
39. divWidth: 200,
40. divHeight: 200,
41. animator: null
42. }
43. DataTmp.animator = animator.create(options);
44. },
45. Show() {
46. let options1: AnimatorOptions = {
47. duration: 1500,
48. easing: "friction",
49. delay: 0,
50. fill: "forwards",
51. direction: "normal",
52. iterations: 2,
53. begin: 0,
54. end: 400.0,
55. };
56. let DataTmp: DateT = {
57. divWidth: 200,
58. divHeight: 200,
59. animator: null
60. }
61. try {
62. DataTmp.animator = animator.create(options1);
63. DataTmp.animator.reset(options1);
64. } catch (error) {
65. let message = (error as BusinessError).message
66. let code = (error as BusinessError).code
67. console.error(`Animator reset failed, error code: ${code}, message: ${message}.`);
68. }
69. let _this = DataTmp;
70. if (DataTmp.animator) {
71. DataTmp.animator.onFrame = (value: number) => {
72. _this.divWidth = value;
73. _this.divHeight = value;
74. };
75. DataTmp.animator.play();
76. }
77. }
78. })
79. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/zj_4WU-mRFi-T-P1sjpBow/zh-cn_image_0000002583439443.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000015Z&HW-CC-Expire=86400&HW-CC-Sign=F5C1CEAD70AC6ADCDAF55A33C26A976277791B618D7350C608A1CBA162ABA13C)

### 基于ArkTS扩展的声明式开发范式

说明

推荐通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[createAnimator](arkts-apis-uicontext-uicontext.md#createanimator)接口明确UI上下文。

```
1. import { AnimatorResult } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct AnimatorTest {
6. private TAG: string = '[AnimatorTest]'
7. private backAnimator: AnimatorResult | undefined = undefined
8. private flag: boolean = false
9. @State columnWidth: number = 100
10. @State columnHeight: number = 100

12. create() {
13. this.backAnimator = this.getUIContext().createAnimator({
14. // 建议使用 this.getUIContext().createAnimator()接口
15. duration: 2000,
16. easing: "ease",
17. delay: 0,
18. fill: "forwards",
19. direction: "normal",
20. iterations: 1,
21. begin: 100, // 动画插值起点
22. end: 200 // 动画插值终点
23. })
24. this.backAnimator.onFinish = () => {
25. this.flag = true
26. console.info(this.TAG, 'backAnimator onFinish')
27. }
28. this.backAnimator.onRepeat = () => {
29. console.info(this.TAG, 'backAnimator repeat')
30. }
31. this.backAnimator.onCancel = () => {
32. console.info(this.TAG, 'backAnimator cancel')
33. }
34. this.backAnimator.onFrame = (value: number) => {
35. this.columnWidth = value
36. this.columnHeight = value
37. }
38. }

40. aboutToDisappear() {
41. // 自定义组件消失时调用finish使未完成的动画结束，避免动画继续运行。
42. // 由于backAnimator在onFrame中引用了this, this中保存了backAnimator，
43. // 在自定义组件消失时应该将保存在组件中的backAnimator置空，避免内存泄漏
44. this.backAnimator?.finish();
45. this.backAnimator = undefined;
46. }

48. build() {
49. Column() {
50. Column() {
51. Column()
52. .width(this.columnWidth)
53. .height(this.columnHeight)
54. .backgroundColor(Color.Blue)
55. }
56. .width('100%')
57. .height(300)

59. Column() {
60. Row() {
61. Button('create')
62. .fontSize(30)
63. .fontColor(Color.Black)
64. .onClick(() => {
65. this.create()
66. })
67. }
68. .padding(10)

70. Row() {
71. Button('play')
72. .fontSize(30)
73. .fontColor(Color.Black)
74. .onClick(() => {
75. this.flag = false
76. if (this.backAnimator) {
77. this.backAnimator.play()
78. }
79. })
80. }
81. .padding(10)

83. Row() {
84. Button('pause')
85. .fontSize(30)
86. .fontColor(Color.Black)
87. .onClick(() => {
88. if (this.backAnimator) {
89. this.backAnimator.pause()
90. }
91. })
92. }
93. .padding(10)

95. Row() {
96. Button('finish')
97. .fontSize(30)
98. .fontColor(Color.Black)
99. .onClick(() => {
100. this.flag = true
101. if (this.backAnimator) {
102. this.backAnimator.finish()
103. }
104. })
105. }
106. .padding(10)

108. Row() {
109. Button('reverse')
110. .fontSize(30)
111. .fontColor(Color.Black)
112. .onClick(() => {
113. this.flag = false
114. if (this.backAnimator) {
115. this.backAnimator.reverse()
116. }
117. })
118. }
119. .padding(10)

121. Row() {
122. Button('cancel')
123. .fontSize(30)
124. .fontColor(Color.Black)
125. .onClick(() => {
126. if (this.backAnimator) {
127. this.backAnimator.cancel()
128. }
129. })
130. }
131. .padding(10)

133. Row() {
134. Button('reset')
135. .fontSize(30)
136. .fontColor(Color.Black)
137. .onClick(() => {
138. if (this.flag) {
139. this.flag = false
140. if (this.backAnimator) {
141. this.backAnimator.reset({
142. duration: 3000,
143. easing: "ease-in",
144. delay: 0,
145. fill: "forwards",
146. direction: "alternate",
147. iterations: 3,
148. begin: 100,
149. end: 300
150. })
151. }
152. } else {
153. console.info(this.TAG, 'Animation not ended')
154. }
155. })
156. }
157. .padding(10)
158. }
159. }
160. }
161. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/4aRSNKGeQz-w9-hGw3ZASw/zh-cn_image_0000002552959398.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000015Z&HW-CC-Expire=86400&HW-CC-Sign=FB5640613BC859CC1E179F2BBFD3E9C7674285426194B988040CEC4508CC0238)

### 位移动画示例（简易入参）

```
1. import { AnimatorResult, SimpleAnimatorOptions } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct AnimatorTest {
6. private TAG: string = '[AnimatorTest]'
7. private backAnimator: AnimatorResult | undefined = undefined
8. private flag: boolean = false
9. @State translate_: number = 0

11. create() {
12. this.backAnimator = this.getUIContext()?.createAnimator(
13. new SimpleAnimatorOptions(0, 100)
14. )
15. this.backAnimator.onFinish = () => {
16. this.flag = true
17. console.info(this.TAG, 'backAnimator onFinish')
18. }
19. this.backAnimator.onFrame = (value:number) => {
20. this.translate_ = value
21. }
22. }

24. aboutToDisappear() {
25. // 自定义组件消失时调用finish使未完成的动画结束，避免动画继续运行。
26. // 由于backAnimator在onFrame中引用了this, this中保存了backAnimator，
27. // 在自定义组件消失时应该将保存在组件中的backAnimator置空，避免内存泄漏
28. this.backAnimator?.finish();
29. this.backAnimator = undefined;
30. }

32. build() {
33. Column() {
34. Column() {
35. Column()
36. .width(100)
37. .height(100)
38. .translate({x: this.translate_})
39. .backgroundColor(Color.Green)
40. }
41. .width('100%')
42. .height(300)

44. Column() {
45. Column() {
46. Button('create')
47. .fontSize(30)
48. .fontColor(Color.White)
49. .onClick(() => {
50. this.create()
51. })
52. }
53. .padding(10)

55. Column() {
56. Button('play')
57. .fontSize(30)
58. .fontColor(Color.White)
59. .onClick(() => {
60. this.flag = false
61. if(this.backAnimator){
62. this.backAnimator.play()
63. }
64. })
65. }
66. .padding(10)

68. Column() {
69. Button('reset')
70. .fontSize(30)
71. .fontColor(Color.White)
72. .onClick(() => {
73. if (this.flag) {
74. this.flag = false
75. if(this.backAnimator){
76. this.backAnimator.reset(
77. new SimpleAnimatorOptions(0, -100)
78. .duration(2000)
79. .easing("ease-in")
80. .fill(FillMode.Forwards)
81. .direction(PlayMode.Alternate)
82. .iterations(2)
83. )
84. }
85. } else {
86. console.info(this.TAG, 'Animation not ended')
87. }
88. })
89. }
90. .padding(10)
91. }
92. }
93. }
94. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/GbDiTL17RC2mpgSOGKtAVw/zh-cn_image_0000002583479399.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000015Z&HW-CC-Expire=86400&HW-CC-Sign=D92794E8C014D4CC3F8CC3938FE0990F4A1C71D6AFFD1DA6CA5AE0CAC82AF876)
