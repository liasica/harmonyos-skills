---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-imageanimator
title: ImageAnimator
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 图片与视频 > ImageAnimator
category: harmonyos-references
scraped_at: 2026-09-02T15:01:04+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1368287995b4517efabf9063656c17c70adca54941748c5b7f07a1ce7ad6f027
---

提供帧动画组件来实现逐帧播放图片的能力，可以配置需要播放的图片列表，每张图片可以配置时长。

**说明** 

* 该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 该组件从API版本26.0.0开始支持[WithTheme](ts-container-with-theme.md)。

## 子组件

无

## 接口

ImageAnimator()

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 属性

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

### images

images(value: Array<ImageFrameInfo>)

设置图片帧信息集合。不支持动态更新，否则可能导致显示错乱、帧切换异常或内存上涨等问题（该属性按非动态更新设计，运行时修改不保证生效）。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Array<[ImageFrameInfo](ts-basic-components-imageanimator.md#imageframeinfo对象说明)> | 是 | 设置图片帧信息集合。每一帧的帧信息(ImageFrameInfo)包含图片路径、图片大小、图片位置和图片播放时长信息，详见[ImageFrameInfo](ts-basic-components-imageanimator.md#imageframeinfo对象说明)对象说明。  默认值：[]  **说明：** 传入数组的内容过大时，内存占用会随之升高。此内存由开发者自行控制。因此，开发者在传入数据前，请充分评估内存消耗情况，以避免内存不足等问题。 |

### state

state(value: AnimationStatus)

控制播放状态。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [AnimationStatus](ts-appendix-enums.md#animationstatus) | 是 | 用于控制播放状态。  默认值：AnimationStatus.Initial |

### duration

duration(value: number)

设置播放时长。当[images](ts-basic-components-imageanimator.md#images)中任意一帧图片设置了单独的duration后，该属性设置无效。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 播放时长。  value为0时，不播放图片。  value平均分配给单张图片的播放时长小于一帧时间，将导致播放异常。  设置为负数时，取默认值1000毫秒。  value的改变只会在下一次循环开始时生效。  单位：毫秒  默认值：1000 |

### reverse

reverse(value: boolean)

设置播放方向。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 播放方向。  false表示从第1张图片播放到最后1张图片，true表示从最后1张图片播放到第1张图片。  动画结束后保留哪一帧还与[fillMode](ts-basic-components-imageanimator.md#fillmode)属性有关，详见fillMode说明。  默认值：false |

### fixedSize

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

preDecode(value: number)

设置预解码的图片数量。

**说明** 

从API version 7开始支持，从API version 9开始废弃。当前无可替代接口。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 预解码的图片数量。例如，设置为2时，播放当前帧时会提前加载后面两张图片至缓存，以提升性能。  默认值：0 |

### fillMode

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

iterations(value: number)

设置播放次数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 默认播放一次；-1表示无限次播放，小于-1的负数取默认值1；浮点数向下取整。  默认值：1 |

### monitorInvisibleArea17+

monitorInvisibleArea(monitorInvisibleArea: boolean)

设置组件是否通过系统[onVisibleAreaChange](ts-universal-component-visible-area-change-event.md#onvisibleareachange)的可见性判定，控制组件的暂停和播放。

**元服务API：** 从API version 17开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| monitorInvisibleArea | boolean | 是 | 当设置为true时，组件将基于系统的[onVisibleAreaChange](ts-universal-component-visible-area-change-event.md#onvisibleareachange)可见性判定，控制组件的暂停和播放。  当组件的运行状态为[AnimationStatus](ts-appendix-enums.md#animationstatus)的Running时，若判定组件不可见，则自动执行暂停操作；若判定为可见，则自动恢复播放。  当设置为false时，组件的暂停和播放不受到onVisibleAreaChange影响。  默认值：false  **说明：**  当该属性由true动态修改为false时，组件将依据当前的[AnimationStatus](ts-appendix-enums.md#animationstatus)状态进行处理。  例如，若当前状态为Running且因[onVisibleAreaChange](ts-universal-component-visible-area-change-event.md#onvisibleareachange)的不可见回调暂停，则在属性由true改为false后，组件会从上次暂停的位置重新开始播放。  由该属性导致的不可见暂停和可见播放操作不会改变用户设置的[state](ts-basic-components-imageanimator.md#state)值。 |

## ImageFrameInfo对象说明

图片帧信息集合。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| src | string | [Resource](ts-types.md#resource)9+ | [PixelMap](ts-image-common.md#pixelmap)12+ | 否 | 否 | 图片路径，图片格式为jpg、jpeg、svg、png、bmp、webp、ico和heif，从API version9开始支持[Resource](ts-types.md#resource)类型的路径，从API version 12开始支持[PixelMap](ts-image-common.md#pixelmap)类型。  **string格式说明：**  - 支持加载本地图片路径和网络图片地址。使用相对路径引用本地图片时，不支持跨包或跨模块调用。resources目录下的文件不支持通过相对路径访问，需使用[Resource](ts-types.md#resource)类型（如$r或$rawfile）来引用，引用方式请参考[加载图片资源](../harmonyos-guides/arkts-graphics-display.md#加载图片资源)。  - 支持http和https网络图片地址，使用网络图片时需要申请权限ohos.permission.INTERNET。  - 支持file://路径前缀的字符串，应用沙箱URI为file://\<bundleName>/\<sandboxPath>。沙箱路径需要使用[fileUri.getUriFromPath(path)](js-apis-file-fileuri.md#fileurigeturifrompath)方法将路径转换为应用沙箱URI，然后传入显示。同时需要保证目录包路径下的文件有可读权限。  - 支持Base64字符串。  **卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。 |
| width | number | string | 否 | 是 | 图片宽度。string类型支持number类型取值的字符串形式，可以附带单位，例如"2"、"2px"。  默认值：0  单位：vp  **卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用 |
| height | number | string | 否 | 是 | 图片高度。string类型支持number类型取值的字符串形式，可以附带单位，例如"2"、"2px"。  默认值：0  单位：vp  **卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用 |
| top | number | string | 否 | 是 | 图片相对于组件左上角的纵向坐标。string类型支持number类型取值的字符串形式，可以附带单位，例如"2"、"2px"。  默认值：0  单位：vp  **卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用 |
| left | number | string | 否 | 是 | 图片相对于组件左上角的横向坐标。string类型支持number类型取值的字符串形式，可以附带单位，例如"2"、"2px"。  默认值：0  单位：vp  **卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用 |
| duration | number | 否 | 是 | 每帧图片的播放时长，单位毫秒。  默认值：0  不支持负数。设置为负数将导致图片在当前帧长时间停留，影响正常播放。 |

## 事件

除支持[通用事件](ts-component-general-events.md)外，还支持以下事件：

### onStart

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

onRepeat(event: () => void)

状态回调，动画重复播放时触发。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | () => void | 是 | 状态回调，动画重复播放时触发。 |

### onCancel

onCancel(event: () => void)

状态回调，动画取消时触发。当state被设置为[AnimationStatus.Initial](ts-appendix-enums.md#animationstatus)时触发；触发后图片显示回到第一帧（正播）或最后一帧（逆播）。与[onFinish](ts-basic-components-imageanimator.md#onfinish)的区别在于：onCancel对应回到Initial初始状态，onFinish对应动画自然结束或停止（Stopped）状态。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | () => void | 是 | 状态回调，动画取消时触发。当state被设置为AnimationStatus.Initial时触发；触发后图片显示回到第一帧（正播）或最后一帧（逆播）。 |

### onFinish

onFinish(event: () => void)

状态回调，动画播放完成时（iterations设置的轮次全部播完且动画自然结束）或者停止播放时（state被切换为[AnimationStatus.Stopped](ts-appendix-enums.md#animationstatus)）触发。当动画处于[AnimationStatus.Initial](ts-appendix-enums.md#animationstatus)状态时返回初始状态不会触发该事件，对应触发的是onCancel。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | () => void | 是 | 状态回调，动画播放完成时（iterations轮次全部播完且动画自然结束）或者停止播放时（state被切换为AnimationStatus.Stopped）触发。 |

## 示例

### 示例1（播放Resource动画）

通过ImageAnimator组件播放Resource动画。

```ts
// xxx.ets
@Entry
@Component
struct ImageAnimatorExample {
  @State state: AnimationStatus = AnimationStatus.Initial;
  @State reverse: boolean = false;
  @State iterations: number = 1;

  build() {
    Column({ space: 10 }) {
      ImageAnimator()
        .images([
          {
            // $r('app.media.img1')需要替换为开发者所需的图像资源文件。
            src: $r('app.media.img1')
          },
          {
            // $r('app.media.img2')需要替换为开发者所需的图像资源文件。
            src: $r('app.media.img2')
          },
          {
            // $r('app.media.img3')需要替换为开发者所需的图像资源文件。
            src: $r('app.media.img3')
          },
          {
            // $r('app.media.img4')需要替换为开发者所需的图像资源文件。
            src: $r('app.media.img4')
          }
        ])
        .duration(4000)
        .state(this.state)
        .reverse(this.reverse)
        .fillMode(FillMode.None)
        .iterations(this.iterations)
        .width(340)
        .height(240)
        .margin({ top: 100 })
        .onStart(() => {
          console.info('Start')
        })
        .onPause(() => {
          console.info('Pause')
        })
        .onRepeat(() => {
          console.info('Repeat')
        })
        .onCancel(() => {
          console.info('Cancel')
        })
        .onFinish(() => {
          console.info('Finish')
          this.state = AnimationStatus.Stopped
        })
      Row() {
        Button('start').width(100).padding(5).onClick(() => {
          this.state = AnimationStatus.Running
        }).margin(5)
        Button('pause').width(100).padding(5).onClick(() => {
          this.state = AnimationStatus.Paused // 显示当前帧图片
        }).margin(5)
        Button('stop').width(100).padding(5).onClick(() => {
          this.state = AnimationStatus.Stopped // 显示动画的起始帧图片
        }).margin(5)
      }

      Row() {
        Button('reverse').width(100).padding(5).onClick(() => {
          this.reverse = !this.reverse
        }).margin(5)
        Button('once').width(100).padding(5).onClick(() => {
          this.iterations = 1
        }).margin(5)
        Button('infinite').width(100).padding(5).onClick(() => {
          this.iterations = -1 // 无限循环播放
        }).margin(5)
      }
    }.width('100%').height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/82sGsr9wThaOgU-4zsCtXA/zh-cn_image_0000002736435173.gif)

### 示例2（播放PixelMap动画）

通过ImageAnimator组件播放PixelMap动画。

```ts
// xxx.ets
import { image } from '@kit.ImageKit';

@Entry
@Component
struct ImageAnimatorExample {
  imagePixelMap: Array<PixelMap> = [];
  @State state: AnimationStatus = AnimationStatus.Initial;
  @State reverse: boolean = false;
  @State iterations: number = 1;
  @State images: Array<ImageFrameInfo> = [];

  async aboutToAppear() {
    // $r('app.media.1')需要替换为开发者所需的图像资源文件。
    this.imagePixelMap.push(await this.getPixmapFromMedia($r('app.media.1')));
    // $r('app.media.2')需要替换为开发者所需的图像资源文件。
    this.imagePixelMap.push(await this.getPixmapFromMedia($r('app.media.2')));
    // $r('app.media.3')需要替换为开发者所需的图像资源文件。
    this.imagePixelMap.push(await this.getPixmapFromMedia($r('app.media.3')));
    // $r('app.media.4')需要替换为开发者所需的图像资源文件。
    this.imagePixelMap.push(await this.getPixmapFromMedia($r('app.media.4')));
    this.images.push({ src: this.imagePixelMap[0] });
    this.images.push({ src: this.imagePixelMap[1] });
    this.images.push({ src: this.imagePixelMap[2] });
    this.images.push({ src: this.imagePixelMap[3] });
  }

  build() {
    Column({ space: 10 }) {
      ImageAnimator()
        .images(this.images)
        .duration(2000)
        .state(this.state)
        .reverse(this.reverse)
        .fillMode(FillMode.None)
        .iterations(this.iterations)
        .width(340)
        .height(240)
        .margin({ top: 100 })
        .onStart(() => {
          console.info('Start');
        })
        .onPause(() => {
          console.info('Pause');
        })
        .onRepeat(() => {
          console.info('Repeat');
        })
        .onCancel(() => {
          console.info('Cancel');
        })
        .onFinish(() => {
          console.info('Finish');
          this.state = AnimationStatus.Stopped;
        })
      Row() {
        Button('start').width(100).padding(5).onClick(() => {
          this.state = AnimationStatus.Running;
        }).margin(5)
        Button('pause').width(100).padding(5).onClick(() => {
          this.state = AnimationStatus.Paused; // 显示当前帧图片
        }).margin(5)
        Button('stop').width(100).padding(5).onClick(() => {
          this.state = AnimationStatus.Stopped; // 显示动画的起始帧图片
        }).margin(5)
      }

      Row() {
        Button('reverse').width(100).padding(5).onClick(() => {
          this.reverse = !this.reverse;
        }).margin(5)
        Button('once').width(100).padding(5).onClick(() => {
          this.iterations = 1;
        }).margin(5)
        Button('infinite').width(100).padding(5).onClick(() => {
          this.iterations = -1; // 无限循环播放
        }).margin(5)
      }
    }.width('100%').height('100%')
  }

  private async getPixmapFromMedia(resource: Resource) {
    let uint8Array = await this.getUIContext().getHostContext()?.resourceManager?.getMediaContent(resource.id);
    let imageSource = image.createImageSource(uint8Array?.buffer.slice(0, uint8Array.buffer.byteLength));
    let createPixelMap: image.PixelMap = await imageSource.createPixelMap({
      desiredPixelFormat: image.PixelMapFormat.RGBA_8888
    });
    await imageSource.release();
    return createPixelMap;
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/Lkffro9gTteRgbQ6FbK1oQ/zh-cn_image_0000002706836026.gif)

### 示例3（设置不可见自动停播）

通过[monitorInvisibleArea](ts-basic-components-imageanimator.md#monitorinvisiblearea17)属性实现了当ImageAnimator的[state](ts-basic-components-imageanimator.md#state)属性为AnimationStatus.Running时，控制组件在不可见时停止播放，在可见时恢复播放。

```ts
@Entry
@Component
struct ImageAnimatorAutoPauseTest {
  scroller: Scroller = new Scroller();
  @State state: AnimationStatus = AnimationStatus.Running;
  @State reverse: boolean = false;
  @State iterations: number = 100;
  @State preCallBack: string = 'Null';
  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

  build() {
    Stack({ alignContent: Alignment.TopStart }) {
      Scroll(this.scroller) {
        Column() {
          ImageAnimator()
            .images([
              {
                // $r('app.media.Clouds')需要替换为开发者所需的图像资源文件。
                src: $r('app.media.Clouds')
              },
              {
                // $r('app.media.landscape')需要替换为开发者所需的图像资源文件。
                src: $r('app.media.landscape')
              },
              {
                // $r('app.media.sky')需要替换为开发者所需的图像资源文件。
                src: $r('app.media.sky')
              },
              {
                // $r('app.media.mountain')需要替换为开发者所需的图像资源文件。
                src: $r('app.media.mountain')
              }
            ])
            .borderRadius(10)
            .monitorInvisibleArea(true)
            .clip(true)
            .duration(4000)
            .state(this.state)
            .reverse(this.reverse)
            .fillMode(FillMode.Forwards)
            .iterations(this.iterations)
            .width(340)
            .height(240)
            .margin({ top: 100 })
            .onStart(() => {
              this.preCallBack = 'Start';
              console.info('ImageAnimator Start');
            })
            .onPause(() => {
              this.preCallBack = 'Pause';
              console.info('ImageAnimator Pause');
            })
            .onRepeat(() => {
              console.info('ImageAnimator Repeat');
            })
            .onCancel(() => {
              console.info('ImageAnimator Cancel');
            })
            .onFinish(() => {
              console.info('ImageAnimator Finish');
            })
          ForEach(this.arr, (item: number) => {
            Text(item.toString())
              .width('90%')
              .height(150)
              .backgroundColor(0xFFFFFF)
              .borderRadius(15)
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .margin({ top: 10 })
          }, (item: number) => item.toString())
        }.width('100%')
      }
      .scrollable(ScrollDirection.Vertical) // 滚动方向纵向
      .scrollBar(BarState.On) // 滚动条常驻显示
      .scrollBarColor(Color.Gray) // 滚动条颜色
      .scrollBarWidth(10) // 滚动条宽度
      .friction(0.6)
      .edgeEffect(EdgeEffect.None)
      .onWillScroll((xOffset: number, yOffset: number, scrollState: ScrollState) => {
        console.info(xOffset + ' ' + yOffset);
      })
      .onScrollEdge((side: Edge) => {
        console.info('To the edge');
      })
      .onScrollStop(() => {
        console.info('Scroll Stop');
      })

      Text('上次触发的回调（Pause/Start）：' + this.preCallBack)
        .margin({ top: 60, left: 20 })
    }.width('100%').height('100%').backgroundColor(0xDCDCDC)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/_Q1hsIMATJKQs58h-EzEDg/zh-cn_image_0000002736315131.gif)
