---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-imageanimator
title: ImageAnimator
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 图片与视频 > ImageAnimator
category: harmonyos-references
scraped_at: 2026-04-29T13:52:17+08:00
doc_updated_at: 2026-04-10
content_hash: sha256:cef8295f092863bb4071e1c1c891cffa8f65049688e614bea470b67c66638eb2
---

提供帧动画组件来实现逐帧播放图片的能力，可以配置需要播放的图片列表，每张图片可以配置时长。

说明

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

PhonePC/2in1TabletTVWearable

无

## 接口

PhonePC/2in1TabletTVWearable

ImageAnimator()

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

### images

PhonePC/2in1TabletTVWearable

images(value: Array<ImageFrameInfo>)

设置图片帧信息集合。不支持动态更新。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Array<[ImageFrameInfo](ts-basic-components-imageanimator.md#imageframeinfo对象说明)> | 是 | 设置图片帧信息集合。每一帧的帧信息(ImageFrameInfo)包含图片路径、图片大小、图片位置和图片播放时长信息，详见[ImageFrameInfo](ts-basic-components-imageanimator.md#imageframeinfo对象说明)对象说明。  默认值：[]  **说明：** 传入数组的内容过大时，内存占用会随之升高。此内存由开发者自行控制。因此，开发者在传入数据前，请充分评估内存消耗情况，以避免内存不足等问题。 |

### state

PhonePC/2in1TabletTVWearable

state(value: AnimationStatus)

控制播放状态。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [AnimationStatus](ts-appendix-enums.md#animationstatus) | 是 | 默认为初始状态，用于控制播放状态。  默认值：AnimationStatus.Initial |

### duration

PhonePC/2in1TabletTVWearable

duration(value: number)

设置播放时长。当Images中任意一帧图片设置了单独的duration后，该属性设置无效。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 播放时长。  value为0时，不播放图片。  value平均分配给单张图片的播放时长小于一帧时间，将导致播放异常。  设置为负数时，取默认值。  value的改变只会在下一次循环开始时生效。  单位：毫秒  默认值：1000ms |

### reverse

PhonePC/2in1TabletTVWearable

reverse(value: boolean)

设置播放方向。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 播放方向。  false表示从第1张图片播放到最后1张图片，true表示从最后1张图片播放到第1张图片。  默认值：false |

### fixedSize

PhonePC/2in1TabletTVWearable

fixedSize(value: boolean)

设置图片大小是否固定为组件大小。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 设置图片大小是否固定为组件大小。 true表示图片大小与组件大小一致，此时设置图片的width 、height 、top 和left属性无效。false表示每一张图片的width 、height 、top和left属性都要单独设置。图片宽高与组件宽高不一致时，图片不会被拉伸。  默认值：true |

### preDecode(deprecated)

PhonePC/2in1TabletTVWearable

preDecode(value: number)

设置预解码的图片数量。

说明

从API version 7开始支持，从API version 9开始废弃。当前无可替代接口。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 预解码的图片数量。例如，设置为2时，播放当前页时会提前加载后面两张图片至缓存，以提升性能。  默认值：0 |

### fillMode

PhonePC/2in1TabletTVWearable

fillMode(value: FillMode)

设置当前播放方向下，动画开始前和结束后的状态。动画结束后的状态由fillMode和reverse属性共同决定。例如，fillMode为Forwards表示停止时维持动画最后一个关键帧的状态，若reverse为false则维持正播的最后一帧，即最后一张图，若reverse为true则维持逆播的最后一帧，即第一张图。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [FillMode](ts-appendix-enums.md#fillmode) | 是 | 当前播放方向下，动画开始前和结束后的状态。  默认值：FillMode.Forwards |

### iterations

PhonePC/2in1TabletTVWearable

iterations(value: number)

设置播放次数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 默认播放一次，设置为-1时表示无限次播放，设置为小于-1的负数时取默认值。设置为浮点数时，数值向下取整。  默认值：1 |

### monitorInvisibleArea17+

PhonePC/2in1TabletTVWearable

monitorInvisibleArea(monitorInvisibleArea: boolean)

设置组件是否通过系统[onVisibleAreaChange](ts-universal-component-visible-area-change-event.md#onvisibleareachange)的可见性判定，控制组件的暂停和播放。

**元服务API：** 从API version 17开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| monitorInvisibleArea | boolean | 是 | 当设置为true时，组件将基于系统的[onVisibleAreaChange](ts-universal-component-visible-area-change-event.md#onvisibleareachange)可见性判定，控制组件的暂停和播放。  当组件的运行状态为[AnimationStatus](ts-appendix-enums.md#animationstatus)的Running时，若判定组件不可见，则自动执行暂停操作；若判定为可见，则自动恢复播放。  当设置为false时，组件的暂停和播放不受到onVisibleAreaChange影响。  默认值：false  **说明：**  当该属性由true动态修改为false时，组件将依据当前的[AnimationStatus](ts-appendix-enums.md#animationstatus)状态进行处理。  例如，若当前状态为Running且因[onVisibleAreaChange](ts-universal-component-visible-area-change-event.md#onvisibleareachange)的不可见回调暂停，则在属性由true改为false后，组件会从上次暂停的位置重新开始播放。  由该属性导致的不可见暂停和可见暂停操作不会改变用户设置的[state](ts-basic-components-imageanimator.md#state)值。 |

## ImageFrameInfo对象说明

PhonePC/2in1TabletTVWearable

图片帧信息集合。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| src | string | [Resource](ts-types.md#resource)9+ | [PixelMap](ts-image-common.md#pixelmap)12+ | 否 | 否 | 图片路径，图片格式为jpg、jpeg、svg、png、bmp、webp、ico和heif，从API version9开始支持[Resource](ts-types.md#resource)类型的路径，从API version 12开始支持[PixelMap](ts-image-common.md#pixelmap)类型。  **卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。 |
| width | number | string | 否 | 是 | 图片宽度。string类型支持number类型取值的字符串形式，可以附带单位，例如"2"、"2px"。  默认值：0  单位：vp  **卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用 |
| height | number | string | 否 | 是 | 图片高度。string类型支持number类型取值的字符串形式，可以附带单位，例如"2"、"2px"。  默认值：0  单位：vp  **卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用 |
| top | number | string | 否 | 是 | 图片相对于组件左上角的纵向坐标。string类型支持number类型取值的字符串形式，可以附带单位，例如"2"、"2px"。  默认值：0  单位：vp  **卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用 |
| left | number | string | 否 | 是 | 图片相对于组件左上角的横向坐标。string类型支持number类型取值的字符串形式，可以附带单位，例如"2"、"2px"。  默认值：0  单位：vp  **卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用 |
| duration | number | 否 | 是 | 每帧图片的播放时长，单位毫秒。  默认值：0  不支持负数。设置为负数将导致图片在当前帧长时间停留，影响正常播放。 |

## 事件

PhonePC/2in1TabletTVWearable

除支持[通用事件](ts-component-general-events.md)外，还支持以下事件：

### onStart

PhonePC/2in1TabletTVWearable

onStart(event: () => void)

状态回调，动画开始播放时触发。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | () => void | 是 | 状态回调，动画开始播放时触发。 |

### onPause

PhonePC/2in1TabletTVWearable

onPause(event: () => void)

状态回调，动画暂停播放时触发。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | () => void | 是 | 状态回调，动画暂停播放时触发。 |

### onRepeat

PhonePC/2in1TabletTVWearable

onRepeat(event: () => void)

状态回调，动画重复播放时触发。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | () => void | 是 | 状态回调，动画重复播放时触发。 |

### onCancel

PhonePC/2in1TabletTVWearable

onCancel(event: () => void)

状态回调，动画返回最初状态时触发。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | () => void | 是 | 状态回调，动画返回最初状态时触发。 |

### onFinish

PhonePC/2in1TabletTVWearable

onFinish(event: () => void)

状态回调，动画播放完成时或者停止播放时触发。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | () => void | 是 | 状态回调，动画播放完成时或者停止播放时触发。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（播放Resource动画）

通过ImageAnimator组件播放Resource动画。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ImageAnimatorExample {
5. @State state: AnimationStatus = AnimationStatus.Initial;
6. @State reverse: boolean = false;
7. @State iterations: number = 1;

9. build() {
10. Column({ space: 10 }) {
11. ImageAnimator()
12. .images([
13. {
14. // $r('app.media.img1')需要替换为开发者所需的图像资源文件。
15. src: $r('app.media.img1')
16. },
17. {
18. // $r('app.media.img2')需要替换为开发者所需的图像资源文件。
19. src: $r('app.media.img2')
20. },
21. {
22. // $r('app.media.img3')需要替换为开发者所需的图像资源文件。
23. src: $r('app.media.img3')
24. },
25. {
26. // $r('app.media.img4')需要替换为开发者所需的图像资源文件。
27. src: $r('app.media.img4')
28. }
29. ])
30. .duration(4000)
31. .state(this.state)
32. .reverse(this.reverse)
33. .fillMode(FillMode.None)
34. .iterations(this.iterations)
35. .width(340)
36. .height(240)
37. .margin({ top: 100 })
38. .onStart(() => {
39. console.info('Start')
40. })
41. .onPause(() => {
42. console.info('Pause')
43. })
44. .onRepeat(() => {
45. console.info('Repeat')
46. })
47. .onCancel(() => {
48. console.info('Cancel')
49. })
50. .onFinish(() => {
51. console.info('Finish')
52. this.state = AnimationStatus.Stopped
53. })
54. Row() {
55. Button('start').width(100).padding(5).onClick(() => {
56. this.state = AnimationStatus.Running
57. }).margin(5)
58. Button('pause').width(100).padding(5).onClick(() => {
59. this.state = AnimationStatus.Paused // 显示当前帧图片
60. }).margin(5)
61. Button('stop').width(100).padding(5).onClick(() => {
62. this.state = AnimationStatus.Stopped // 显示动画的起始帧图片
63. }).margin(5)
64. }

66. Row() {
67. Button('reverse').width(100).padding(5).onClick(() => {
68. this.reverse = !this.reverse
69. }).margin(5)
70. Button('once').width(100).padding(5).onClick(() => {
71. this.iterations = 1
72. }).margin(5)
73. Button('infinite').width(100).padding(5).onClick(() => {
74. this.iterations = -1 // 无限循环播放
75. }).margin(5)
76. }
77. }.width('100%').height('100%')
78. }
79. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/lw1D5DUqQyeBY9BLX8ojFQ/zh-cn_image_0000002589326235.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055214Z&HW-CC-Expire=86400&HW-CC-Sign=854E8A29A44D4DFD05DE35130A3BDBA66A7C977DD4B4822E3D04ECD5A400F052)

### 示例2（播放PixelMap动画）

通过ImageAnimator组件播放PixelMap动画。

```
1. // xxx.ets
2. import { image } from '@kit.ImageKit';

4. @Entry
5. @Component
6. struct ImageAnimatorExample {
7. imagePixelMap: Array<PixelMap> = [];
8. @State state: AnimationStatus = AnimationStatus.Initial;
9. @State reverse: boolean = false;
10. @State iterations: number = 1;
11. @State images: Array<ImageFrameInfo> = [];

13. async aboutToAppear() {
14. // $r('app.media.1')需要替换为开发者所需的图像资源文件。
15. this.imagePixelMap.push(await this.getPixmapFromMedia($r('app.media.1')));
16. // $r('app.media.2')需要替换为开发者所需的图像资源文件。
17. this.imagePixelMap.push(await this.getPixmapFromMedia($r('app.media.2')));
18. // $r('app.media.3')需要替换为开发者所需的图像资源文件。
19. this.imagePixelMap.push(await this.getPixmapFromMedia($r('app.media.3')));
20. // $r('app.media.4')需要替换为开发者所需的图像资源文件。
21. this.imagePixelMap.push(await this.getPixmapFromMedia($r('app.media.4')));
22. this.images.push({ src: this.imagePixelMap[0] });
23. this.images.push({ src: this.imagePixelMap[1] });
24. this.images.push({ src: this.imagePixelMap[2] });
25. this.images.push({ src: this.imagePixelMap[3] });
26. }

28. build() {
29. Column({ space: 10 }) {
30. ImageAnimator()
31. .images(this.images)
32. .duration(2000)
33. .state(this.state)
34. .reverse(this.reverse)
35. .fillMode(FillMode.None)
36. .iterations(this.iterations)
37. .width(340)
38. .height(240)
39. .margin({ top: 100 })
40. .onStart(() => {
41. console.info('Start');
42. })
43. .onPause(() => {
44. console.info('Pause');
45. })
46. .onRepeat(() => {
47. console.info('Repeat');
48. })
49. .onCancel(() => {
50. console.info('Cancel');
51. })
52. .onFinish(() => {
53. console.info('Finish');
54. this.state = AnimationStatus.Stopped;
55. })
56. Row() {
57. Button('start').width(100).padding(5).onClick(() => {
58. this.state = AnimationStatus.Running;
59. }).margin(5)
60. Button('pause').width(100).padding(5).onClick(() => {
61. this.state = AnimationStatus.Paused; // 显示当前帧图片
62. }).margin(5)
63. Button('stop').width(100).padding(5).onClick(() => {
64. this.state = AnimationStatus.Stopped; // 显示动画的起始帧图片
65. }).margin(5)
66. }

68. Row() {
69. Button('reverse').width(100).padding(5).onClick(() => {
70. this.reverse = !this.reverse;
71. }).margin(5)
72. Button('once').width(100).padding(5).onClick(() => {
73. this.iterations = 1;
74. }).margin(5)
75. Button('infinite').width(100).padding(5).onClick(() => {
76. this.iterations = -1; // 无限循环播放
77. }).margin(5)
78. }
79. }.width('100%').height('100%')
80. }

82. private async getPixmapFromMedia(resource: Resource) {
83. let unit8Array = await this.getUIContext().getHostContext()?.resourceManager?.getMediaContent(resource.id);
84. let imageSource = image.createImageSource(unit8Array?.buffer.slice(0, unit8Array.buffer.byteLength));
85. let createPixelMap: image.PixelMap = await imageSource.createPixelMap({
86. desiredPixelFormat: image.PixelMapFormat.RGBA_8888
87. });
88. await imageSource.release();
89. return createPixelMap;
90. }
91. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/QKlUgQ1jSmyrOuQBcLtZGQ/zh-cn_image_0000002589246177.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055214Z&HW-CC-Expire=86400&HW-CC-Sign=0A2760047B789C74C13EAB8230A876C8B96B816FDBC31E4C1F88FD1951710CDD)

### 示例3（设置不可见自动停播）

通过[monitorInvisibleArea](ts-basic-components-imageanimator.md#monitorinvisiblearea17)属性实现了当ImageAnimator的[state](ts-basic-components-imageanimator.md#state)属性为AnimationStatus.Running时，控制组件在不可见时停止播放，在可见时恢复播放。

```
1. @Entry
2. @Component
3. struct ImageAnimatorAutoPauseTest {
4. scroller: Scroller = new Scroller();
5. @State state: AnimationStatus = AnimationStatus.Running;
6. @State reverse: boolean = false;
7. @State iterations: number = 100;
8. @State preCallBack: string = 'Null';
9. private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

11. build() {
12. Stack({ alignContent: Alignment.TopStart }) {
13. Scroll(this.scroller) {
14. Column() {
15. ImageAnimator()
16. .images([
17. {
18. // $r('app.media.Clouds')需要替换为开发者所需的图像资源文件。
19. src: $r('app.media.Clouds')
20. },
21. {
22. // $r('app.media.landscape')需要替换为开发者所需的图像资源文件。
23. src: $r('app.media.landscape')
24. },
25. {
26. // $r('app.media.sky')需要替换为开发者所需的图像资源文件。
27. src: $r('app.media.sky')
28. },
29. {
30. // $r('app.media.mountain')需要替换为开发者所需的图像资源文件。
31. src: $r('app.media.mountain')
32. }
33. ])
34. .borderRadius(10)
35. .monitorInvisibleArea(true)
36. .clip(true)
37. .duration(4000)
38. .state(this.state)
39. .reverse(this.reverse)
40. .fillMode(FillMode.Forwards)
41. .iterations(this.iterations)
42. .width(340)
43. .height(240)
44. .margin({ top: 100 })
45. .onStart(() => {
46. this.preCallBack = 'Start';
47. console.info('ImageAnimator Start');
48. })
49. .onPause(() => {
50. this.preCallBack = 'Pause';
51. console.info('ImageAnimator Pause');
52. })
53. .onRepeat(() => {
54. console.info('ImageAnimator Repeat');
55. })
56. .onCancel(() => {
57. console.info('ImageAnimator Cancel');
58. })
59. .onFinish(() => {
60. console.info('ImageAnimator Finish');
61. })
62. ForEach(this.arr, (item: number) => {
63. Text(item.toString())
64. .width('90%')
65. .height(150)
66. .backgroundColor(0xFFFFFF)
67. .borderRadius(15)
68. .fontSize(16)
69. .textAlign(TextAlign.Center)
70. .margin({ top: 10 })
71. }, (item: string) => item)
72. }.width('100%')
73. }
74. .scrollable(ScrollDirection.Vertical) // 滚动方向纵向
75. .scrollBar(BarState.On) // 滚动条常驻显示
76. .scrollBarColor(Color.Gray) // 滚动条颜色
77. .scrollBarWidth(10) // 滚动条宽度
78. .friction(0.6)
79. .edgeEffect(EdgeEffect.None)
80. .onWillScroll((xOffset: number, yOffset: number, scrollState: ScrollState) => {
81. console.info(xOffset + ' ' + yOffset);
82. })
83. .onScrollEdge((side: Edge) => {
84. console.info('To the edge');
85. })
86. .onScrollStop(() => {
87. console.info('Scroll Stop');
88. })

90. Text('上次触发的回调（Pause/Start）：' + this.preCallBack)
91. .margin({ top: 60, left: 20 })
92. }.width('100%').height('100%').backgroundColor(0xDCDCDC)
93. }
94. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/OkS32ogEStueZ8_TDo0mGw/zh-cn_image_0000002558766370.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055214Z&HW-CC-Expire=86400&HW-CC-Sign=0D4C43797FFA21F6EAE49115145A7DE6CDEAD34332BC147BB48AF82D477BC91E)
