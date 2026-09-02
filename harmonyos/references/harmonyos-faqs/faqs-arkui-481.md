---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-481
title: 组件截图（ComponentSnapshot）返回错误码100001，可能原因为截图尺寸过大，文档说明其与具体硬件限制有关，如何查看具体限制是多少
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 组件截图（ComponentSnapshot）返回错误码100001，可能原因为截图尺寸过大，文档说明其与具体硬件限制有关，如何查看具体限制是多少
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:28+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8fdb86c5d8beb72ad8464a16b8fc7ecf5ef2d97859ba756087163b88e9b98be5
---

硬件限制因平台而异，可以通过如下命令进行查看：

```powershell
hdc shell hidumper -s 10 -a 'vktextureLimit'
```

常见值为“width: 8192 height: 8192”，表示最大绘制纹理尺寸的长宽都需要在8192像素以内。比较待截图组件的尺寸，以便确认截图失败是否为该原因导致，如果是，请调整所截图组件的大小，或实现为滚动截图后自行拼接。实现请参考[截取长内容（滚动截图）](../harmonyos-guides/arkts-uicontext-component-snapshot.md#截取长内容滚动截图)和[长截图](../best-practices/bpta-long-snapshot-practice.md)。

如需实现离屏组件的长截图，可参考以下实现：

```ts
// src/main/ets/utils/Utils.ets
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';

export class Utils {
  static sleep(ms: number): Promise<void> {
    return new Promise(resolve => setTimeout(resolve, ms));
  }

  // Calculate the valid screenshot area
  static async getSnapshotArea(context: UIContext, pixelMap: PixelMap, scrollYOffsets: number[], listWidth: number,
    listHeight: number): Promise<image.PositionArea> {
    let stride = pixelMap.getBytesNumberPerRow();
    let bytesNumber = pixelMap.getPixelBytesNumber();
    let buffer: ArrayBuffer = new ArrayBuffer(bytesNumber);
    let len = scrollYOffsets.length;

    if (scrollYOffsets.length >= 2) {
      let realScrollHeight = scrollYOffsets[len-1] - scrollYOffsets[len-2];
      if (listHeight - realScrollHeight > 0) {
        let cropRegion: image.Region = {
          x: 0,
          y: context.vp2px(listHeight - realScrollHeight) || 0,
          size: {
            height: context.vp2px(realScrollHeight) || 0,
            width: context.vp2px(listWidth) || 0
          }
        };
        await pixelMap.crop(cropRegion);
      }
    }

    let area: image.PositionArea = {
      pixels: buffer,
      offset: 0,
      stride: stride,
      region: {
        size: {
          width: 0,
          height: 0
        },
        x: 0,
        y: 0
      }
    }

    try {
      let imgInfo = pixelMap.getImageInfoSync();
      area.region.size.width = imgInfo.size.width;
      area.region.size.height = imgInfo.size.height;
      pixelMap.readPixelsSync(area);
    } catch (err) {
      let error = err as BusinessError;
      console.error(`getSnapshotArea err, code:${error.code}, message: ${error.message}`);
    }
    return area;
  }

  // Graphic splicing
  static async mergeImage(context: UIContext, areaArray: image.PositionArea[], lastOffsetY: number, listWidth: number,
    listHeight: number): Promise<PixelMap> {
    let opts: image.InitializationOptions = {
      editable: true,
      pixelFormat: 4,
      size: {
        width: context.vp2px(listWidth) || 0,
        height: context.vp2px(lastOffsetY + listHeight) || 0
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
        console.error(`writePixelsSync err, code:${error.code}, message: ${error.message}`);
      }
    }
    return longPixelMap;
  }
}
```

```ts
// src/main/ets/pages/Index.ets
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { Utils } from '../utils/Utils';

export class MyDataSource {
  private _data: string[] = [];
  private _listeners: DataChangeListener[] = [];

  pushData(data: string): void {
    this._data.push(data);
    this._listeners.forEach(listener => {
      listener.onDataAdd(this._data.length - 1);
    })
  }

  getAllData(): string[] {
    return this._data;
  }

  totalCount(): number {
    return this._data.length;
  }

  getData(index: number): string {
    return this._data[index];
  }

  registerDataChangeListener(listener: DataChangeListener): void {
    this._listeners.push(listener);
  }

  unregisterDataChangeListener(listener: DataChangeListener): void {
    const index = this._listeners.indexOf(listener);
    if (index != -1) {
      this._listeners.splice(index, 1);
    }
  }
}

@Entry
@Component
struct SnapshotExample {
  private scroller: Scroller = new Scroller();
  private listComponentWidth: number = 0;
  private listComponentHeight: number = 0;
  @State mergedImage: PixelMap | undefined = undefined;
  private areaArray: image.PositionArea[] = [];
  private scrollYOffsets: number[] = [];
  private data: MyDataSource = new MyDataSource();
  private listId: string = 'LIST_ID';

  aboutToAppear(): void {
    for (let i = 0; i < 50; i++) {
      this.data.pushData(`Hello ${i}`);
    }
  }

  async onceSnapshot() {
    await this.beforeSnapshot();
    await this.snapAndMerge();
    this.afterGeneratorImage();
  }

  async snapAndMerge() {
    try {
      // Record the current scrolling position
      this.scrollYOffsets.push(this.scroller.currentOffset().yOffset);
      // Take a screenshot of the current display part of the component
      const pixelMap = await this.getUIContext().getComponentSnapshot().get(this.listId);
      // Calculate the valid screenshot area
      let area: image.PositionArea =
        await Utils.getSnapshotArea(this.getUIContext(), pixelMap, this.scrollYOffsets, this.listComponentWidth,
          this.listComponentHeight);
      this.areaArray.push(area);
      // Determine whether to scroll to the bottom
      if (!this.scroller.isAtEnd()) {
        // Not to the bottom: Scroll down by one screen height
        this.scroller.scrollTo({
          xOffset: 0,
          yOffset: (this.scroller.currentOffset().yOffset + this.listComponentHeight),
          animation: {
            duration: 200
          }
        });
        await Utils.sleep(200);
        await this.snapAndMerge();
      } else {
        this.mergedImage =
          await Utils.mergeImage(this.getUIContext(), this.areaArray, this.scrollYOffsets[this.scrollYOffsets.length-1],
            this.listComponentWidth, this.listComponentHeight);
      }
    } catch (err) {
      let error = err as BusinessError;
      console.error(`snapAndMerge err, code:${error.code}, message: ${error.message}`);
    }
  }

  async beforeSnapshot() {
    try {
      this.scroller.scrollTo({
        xOffset: 0,
        yOffset: 0,
        animation: {
          duration: 200
        }
      });
      await Utils.sleep(200);
    } catch (err) {
      let error = err as BusinessError;
      console.error(`beforeSnapshot err, code:${error.code}, message: ${error.message}`);
    }
  }

  afterGeneratorImage() {
    this.scrollYOffsets.length = 0;
    this.areaArray.length = 0;
  }

  build() {
    Column({ space: 12 }) {
      Button('Click to get the snapshot')
        .onClick(() => {
          this.onceSnapshot();
        })
      Stack() {
        // Screenshot component
        List({ space: 12, scroller: this.scroller }) {
          LazyForEach(this.data, (item: string) => {
            ListItem() {
              Row() {
                Text(item)
                  .fontSize(50)
                  .height(50)
              }
            }
          }, (item: number) => item.toString())
        }
        .scrollBar(BarState.Off)
        .cachedCount(3)
        .width('100%')
        .height('100%')
        .backgroundColor($r('sys.color.background_secondary'))
        .id(this.listId)
        .onAreaChange((oldValue, newValue) => {
          this.listComponentWidth = newValue.width as number;
          this.listComponentHeight = newValue.height as number;
        })
        // Set the Z-sequence to -1 to ensure that this component is invisible
        .zIndex(-1)

        // Use a mask to cover the screenshot area
        Column()
          .width('100%').height('100%').backgroundColor(Color.White)
        // Long screenshot
        Scroll() {
          Image(this.mergedImage)
        }
      }
      .width('100%')
      .layoutWeight(1)
    }
  }
}
```
