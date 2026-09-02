---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-uicontext-component-snapshot
title: 使用组件截图（ComponentSnapshot）
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > UI系统场景化能力 > 使用组件截图（ComponentSnapshot）
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:19+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6520e70fbeb500d378ba841f42883696a347a4c75459409cd25d0e076d68e87e
---

## 能力介绍

组件截图是将应用内一个组件节点树的渲染结果生成位图（[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)）的能力，支持两种方式：一种是对已挂树显示的组件进行截图，另一种是对通过Builder或ComponentContent实现的离线组件进行截图。

**说明** 

组件截图依赖UI上下文，需要在具备明确上下文的环境中调用，因此请优先使用UIContext的getComponentSnapshot接口返回的[ComponentSnapshot](../harmonyos-references/arkts-apis-uicontext-componentsnapshot.md)对象的接口，不建议直接使用从@kit.ArkUI导入的componentSnapshot接口。

### 对挂树组件截图

对已明确挂树的组件进行截图，可通过[get](../harmonyos-references/arkts-apis-uicontext-componentsnapshot.md#get12-1)或[getSync](../harmonyos-references/arkts-apis-uicontext-componentsnapshot.md#getsync12)实现，传入组件标识（需提前通过.id通用属性配置）以指定组件根节点。系统在通过指定的ID查找待截图组件时，仅遍历已挂树的组件，不对cache或离屏组件进行查找。系统以首个查找到的结果为准，故应用需**确保组件标识ID的唯一性**。

从API version 15开始，在已知组件的[getUniqueId](../harmonyos-references/js-apis-arkui-framenode.md#getuniqueid12)的情况下，也可以使用[getWithUniqueId](../harmonyos-references/arkts-apis-uicontext-componentsnapshot.md#getwithuniqueid15)或[getSyncWithUniqueId](../harmonyos-references/arkts-apis-uicontext-componentsnapshot.md#getsyncwithuniqueid15)接口来实现截图，这可以省去查找组件的过程。

截图仅能获取最近一帧的绘制内容。若在组件触发更新的同时调用截图，更新的渲染内容不会被截取，截图将返回前一帧的绘制内容。

**说明** 

尽量避免在使用截图时触发待截图组件的刷新，防止对截图内容的干扰。

### 对离线组件截图

离线组件是指通过Builder或ComponentContent封装的、尚未挂载到树上的组件，可以使用[createFromBuilder](../harmonyos-references/arkts-apis-uicontext-componentsnapshot.md#createfrombuilder12-1)来实现。从API version 18开始，也可以使用[createFromComponent](../harmonyos-references/arkts-apis-uicontext-componentsnapshot.md#createfromcomponent18)实现离线组件截图。

这些组件不参与真实渲染，因此对其截图需要更长的时间，因为系统必须先进行离线构建、布局及资源加载等操作，在这些操作完成前执行的截图所获位图不符合预期。因此，通常需要通过设置delay参数指定足够的时间，确保系统能够完成这些操作。对于图片资源的加载，建议将图片组件的[syncLoad](../harmonyos-references/ts-basic-components-image.md#syncload8)属性设为 true，以强制同步加载，确保离线组件构建时图片已加载、下载及解码完成，从而确保截图过程中能够正确呈现图片像素。

## 典型使用场景

以下通过几个典型场景来说明组件截图能力的常见使用方式。

### 截取长内容（滚动截图）

较长内容通常使用滚动类容器组件实现。截图时，仅能捕获容器内可见内容，超出边界部分无法截取。若使用[LazyForEach](../harmonyos-references/ts-rendering-control-lazyforeach.md)或[Repeat](../harmonyos-references/ts-rendering-control-repeat.md)，超出显示范围内容亦不会被系统构建及截取。

可利用滚动类容器接口，模拟用户滑动逐页截图，之后按偏移量拼接各页PixelMap位图，以生成完整长图。关键点在于模拟滑动、维护位移与位图关系及实现PixelMap位图读写。

**步骤1：添加滚动控制器及事件监听**

为了能够模拟滚动，以及监听组件滚动的具体[offset](../harmonyos-references/ts-universal-attributes-location.md#offset)，需要为[List](../harmonyos-references/ts-container-list.md)（此处以列表为例）组件添加滚动控制器以及滚动监听。

```typescript
// src/main/ets/view/ScrollSnapshot.ets
@Component
export struct ScrollSnapshot {
  private scroller: Scroller = new Scroller();
  private listComponentWidth: number = 0; // 组件宽度，默认值为0
  private listComponentHeight: number = 0; // 组件高度，默认值为0
  // list组件的当前偏移量
  private curYOffset: number = 0;
  // 每次滚动距离
  private scrollHeight: number = 0;

  // ...
  build() {
    // ...
        Stack() {
          // ...
          // 1.1 绑定滚动控制器，并通过`.id`配置组件唯一标识。
          List({ space: 12, scroller: this.scroller }) {
              LazyForEach(this.dataSource, (item: number) => {
              ListItem() {
                NewsItem({ index: item })
              }
            }, (item: number) => item.toString())
          }
          // ...
          .id(LIST_ID)
          // 1.2 通过回调获取滚动偏移量。
          .onDidScroll(() => {
            this.curYOffset = this.scroller.currentOffset().yOffset;
          })
          .onAreaChange((oldValue, newValue) => {
            // 1.3 获取组件的宽高。
            this.listComponentWidth = newValue.width as number;
            this.listComponentHeight = newValue.height as number;
            this.scrollHeight = this.listComponentHeight;
          })
          // ...
    }
  }
}
```

**步骤2：循环滚动截图并缓存**

通过实现一个递归方法滚动循环截图，并在滚动过程配合一些动效实现。

```typescript
/**
 * 递归滚动截图，直到滚动到底，最后合并所有截图
 */
async scrollSnapAndMerge() {
  try {
    // 记录滚动偏移
    this.scrollYOffsets.push(this.curYOffset - this.yOffsetBefore);
    // 调用组件截图接口，获取list组件的截图
    const pixelMap = await this.getUIContext().getComponentSnapshot().get(LIST_ID);
    // 获取位图像素字节，并保存在数组中
    let area: image.PositionArea =
      await ImageUtils.getSnapshotArea(pixelMap, this.scrollYOffsets, this.listComponentWidth,
        this.listComponentHeight)
    this.areaArray.push(area);

    // 判断是否滚动到底以及用户是否已经强制停止
    if (!this.scroller.isAtEnd() && !this.isClickStop) {
      // 如果没有到底或被停止，则播放一个滚动动效，延迟一段时间后，继续递归截图
      CommonUtils.scrollAnimation(this.scroller, 1000, this.scrollHeight);
      await CommonUtils.sleep(1500);
      await this.scrollSnapAndMerge();
    } else {
      // 当滚动到底时，调用`mergeImage`将所有保存的位图数据进行拼接，返回长截图位图对象
      this.mergedImage =
        await ImageUtils.mergeImage(this.areaArray, this.scrollYOffsets[this.scrollYOffsets.length - 1],
          this.listComponentWidth, this.listComponentHeight);
    }
  } catch (err) {
    let error = err as BusinessError;
    Logger.error(TAG, `scrollSnapAndMerge err, errCode: ${error.code}, error message: ${error.message}`);
  }
}
```

```typescript
// src/main/ets/common/CommonUtils.ets
static scrollAnimation(scroller: Scroller, duration: number, scrollHeight: number): void {
  scroller.scrollTo({
    xOffset: 0,
    yOffset: (scroller.currentOffset().yOffset + scrollHeight),
    animation: {
      duration: duration,
      curve: Curve.Smooth,
      canOverScroll: false
    }
  });
}
```

**步骤3：拼接长截图**

使用image.[createPixelMapSync](../harmonyos-references/arkts-apis-image-imagesource.md#createpixelmapsync12)()方法创建长截图longPixelMap，并遍历之前保存的图像片段数据（this.areaArray），构建image.PositionArea对象area，然后调用longPixelMap.[writePixelsSync](../harmonyos-references/arkts-apis-image-pixelmap.md#writepixelssync12)(area)方法将这些片段逐个写入到正确的位置，从而拼接成一个完整的长截图。

```typescript
static async mergeImage(areaArray: image.PositionArea[], lastOffsetY: number, listWidth: number,
  listHeight: number): Promise<PixelMap> {
  // 创建一个长截图位图对象
  let opts: image.InitializationOptions = {
    editable: true,
    pixelFormat: 4,
    size: {
      width: uiContext?.vp2px(listWidth) || 0,
      height: uiContext?.vp2px(lastOffsetY + listHeight) || 0
    }
  };
  let longPixelMap = image.createPixelMapSync(opts);
  let imgPosition: number = 0;

  for (let i = 0; i < areaArray.length; i++) {
    let readArea = areaArray[i];
    let area: image.PositionArea = {
      pixels: readArea.pixels,
      offset: 0,
      stride: readArea.stride,
      region: {
        size: {
          width: readArea.region.size.width,
          height: readArea.region.size.height
        },
        x: 0,
        y: imgPosition
      }
    }
    imgPosition += readArea.region.size.height;
    try {
      longPixelMap.writePixelsSync(area);
    } catch (err) {
      let error = err as BusinessError;
      Logger.error(TAG, `writePixelsSync err, code: ${error.code}, message: ${error.message}`);
    }
  }
  return longPixelMap;
}
```

**步骤4：保存截图**

使用安全控件[SaveButton](../harmonyos-references/ts-security-components-savebutton.md)实现截图保存到相册。

```typescript
// src/main/ets/view/SnapshotPreview.ets
SaveButton({
  icon: SaveIconStyle.FULL_FILLED,
  text: SaveDescription.SAVE_IMAGE,
  buttonType: ButtonType.Capsule
})
  // ···
  .onClick((event, result) => {
    this.saveSnapshot(result);
  })
```

```typescript
async saveSnapshot(result: SaveButtonOnClickResult): Promise<void> {
  try {
    if (result === SaveButtonOnClickResult.SUCCESS) {
      const helper = photoAccessHelper.getPhotoAccessHelper(this.context);
      const uri = await helper.createAsset(photoAccessHelper.PhotoType.IMAGE, 'png');
      const file = await fileIo.open(uri, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
      try {
        const imagePackerApi: image.ImagePacker = image.createImagePacker();
        const packOpts: image.PackingOption = {
          format: 'image/png',
          quality: 100,
        };
        const data = await imagePackerApi.packToData(this.mergedImage, packOpts);
        fileIo.writeSync(file.fd, data);
        Logger.info(TAG, `Succeeded in packToFile`);
        this.getUIContext().getPromptAction().showToast({
          // 请将$r('app.string.save_album_success')替换为实际资源文件，在本示例中该资源文件的value值为"Saved to album"
          message: $r('app.string.save_album_success'),
          duration: 1800
        })
      } catch (error) {
        let businessError = error as BusinessError;
        Logger.error(TAG,
          `Failed to packToFile. Error code is ${businessError.code}, message is ${businessError.message}`);
      } finally {
        try {
          fileIo.closeSync(file.fd);
        } catch (err) {
          let error = err as BusinessError;
          Logger.error(TAG, `Failed to close file. Error code is ${error.code}, message is ${error.message}`);
        }
      }
    }
    // ...
  } catch (err) {
    let error = err as BusinessError;
    Logger.error(TAG, `saveSnapshot err, errCode: ${error.code}, error message: ${error.message}`);
  }
}
```

**步骤5：保存完成后释放位图**

当位图对象不再使用时，应及时将其赋值为空，例如：this.mergedImage = undefined;。

```typescript
closeSnapPopup(): void {
  // 关闭弹窗
  this.isShowPreview = false;
  // 释放位图对象
  this.mergedImage = undefined;
  // 重置相关参数
  this.snapPopupWidth = 100;
  this.snapPopupHeight = 200;
  this.snapPopupPosition =
    PopupUtils.calcPopupCenter(this.screenWidth, this.screenHeight, this.snapPopupWidth, this.snapPopupHeight);
  this.isLargePreview = false;
}
```

### 封装全局截图接口

如前文所述，截图接口必须在UI上下文明确的位置使用。然而，应用有时希望对不同模块封装统一的全局截图方法。例如，在下述示例中，awardBuilder构建的组件是固定结构的。GlobalStaticSnapshot提供了一个getAwardSnapshot全局方法，能够满足不同模块的需求，对同一固定模式的组件进行截图，从而实现全局截图接口的封装。本示例从API version 18开始支持。

```typescript
import { image } from '@kit.ImageKit';
import { ComponentContent } from '@kit.ArkUI';

export class Params {
  public text: string | undefined | null = '';

  constructor(text: string | undefined | null) {
    this.text = text;
  }
}

@Builder
function awardBuilder(params: Params) {
  Column() {
    Text(params.text)
      .fontSize(90)
      .fontWeight(FontWeight.Bold)
      .margin({ bottom: 36 })
      .width('100%')
      .height('100%')
  }.backgroundColor('#FFF0F0F0')
}

export class GlobalStaticSnapshot {
  /**
   * 一个可以获取固定对象截图的静态方法
   */
  static async getAwardSnapshot(uiContext: UIContext, textParam: Params): Promise<image.PixelMap | undefined> {
    let resultPixmap: image.PixelMap | undefined = undefined
    let contentNode = new ComponentContent(uiContext, wrapBuilder(awardBuilder), textParam);
    await uiContext.getComponentSnapshot()
      .createFromComponent(contentNode, 320, true, { scale: 1, waitUntilRenderFinished: true })
      .then((pixmap: image.PixelMap) => {
        resultPixmap = pixmap;
      })
      .catch((err: Error) => {
        console.error(`error: ${err}`);
      })
    return resultPixmap;
  }
}
```

**完整示例：**

完整示例请参考[长截图](../best-practices/bpta-long-snapshot-practice.md#section1566681910427)。

## 组件截图最佳实践

### 合理控制截图时机

在实现截图功能时，需注意组件的渲染过程非一次性完成。系统在构建与显示组件时，将经过测量、布局、提交指令等多个复杂步骤，最终在一次硬件刷新时呈现于屏幕上。因此，在特定情况下，若在组件刷新后立即调用截图，可能无法获取预期内容或出现截图失败报错。

为了确保截图结果准确，建议在组件完全渲染后再执行截图操作。

**了解组件的绘制状态**

为了确保截图内容符合预期，应该了解代码对界面状态的修改时机，并注意给系统预留处理时间，这通常可以通过增加一定延时来实现。

尽管可以通过inspector上的[ComponentObserver](../harmonyos-references/js-apis-arkui-inspector.md#componentobserver)感知应用组件绘制（draw）送显通知，但需要注意的是，ComponentObserver的组件绘制通知并不意味着系统已经真正将绘制指令执行，这取决于图形系统服务的负载情况。

**明确等待绘制完成**

影响截图预期的主要因素是截图时机与系统服务执行绘制指令的时间差。在发起截图调用时，应用侧之前提交的所有绘制指令可能尚未被图形服务真正执行。为此，可以通过指定[SnapshotOptions](../harmonyos-references/js-apis-arkui-componentsnapshot.md#snapshotoptions12)参数中的waitUntilRenderFinished为true，来确保系统在执行截图请求时等待所有之前的绘制指令均执行完毕，从而截取到更完整的内容。

**说明** 

建议始终开启waitUntilRenderFinished参数。

**了解资源加载对截图的影响**

影响截图预期的另一个常见原因，是图片资源的加载。图片组件支持在线资源链接，也可指定本地资源，且绝大多数图片资源为PNG、JPEG等压缩格式。这些资源需要系统解码为可提交绘制的位图格式，此过程默认在异步IO线程上进行，因此可能由于该过程耗时的不确定性而导致截图不符合预期。

应用可通过以下几种方式进行优化：

1. 自行提前解析图片为PixelMap格式，将PixelMap配置给图片组件；建议优先以此方法进行优化。
2. 配置所使用的图片组件的[syncLoad](../harmonyos-references/ts-basic-components-image.md#syncload8)属性为true来强制同步加载，这样组件被构建时，即可确保资源可以直接被提交；
3. 通过指定延迟时长以及checkImageStatus设置为true，尝试截图，当返回160001错误后，重新加大时长进行截图；

### 及时保存和释放位图对象

为了及时释放资源，当截图接口返回的PixelMap对象不再使用时，应将其赋值为空。

### 合理控制采样精度

请不要截取过大尺寸的图片，截图不建议超过屏幕尺寸大小。当要截取的图片目标长宽超过底层限制时，截图会返回失败，不同设备的底层限制并不相同。可以通过控制SnapshotOptions中的scale参数，减小采样精度，这可以在很大程度上节省内存，并大幅度提高截图的效率。

### 使用其他能力对自渲染场景实现截图

尽管截图只需传入一个组件根节点即可实现对其下所有组件进行截图，但当子组件中存在[Video](../harmonyos-references/ts-media-components-video.md)、[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)或[Web](../harmonyos-references/arkts-basic-components-web.md)组件时，这并不是推荐的截图方式。建议直接使用[image.createPixelMapFromSurface](../harmonyos-references/arkts-apis-image-f.md#imagecreatepixelmapfromsurface11)接口来实现。
