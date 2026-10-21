---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-long-screenshot
title: 长截图
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > UI系统场景化能力 > 长截图
category: harmonyos-guides
scraped_at: 2026-10-22T07:04:46+08:00
doc_updated_at: 2026-10-21
content_hash: sha256:12fef21bd42f0ae80734fbf0dd89c1537510dcad15ea102e03806b1f82eb7701
---

## 概述

在移动应用中，标准的截图方法仅能捕捉当前屏幕显示的内容，对于超出屏幕可视区域的长页面或文档而言，这种方式显得不够便捷。当用户截图分享和保存（如聊天记录、网页文章、活动海报等）的内容较长的时候，需要用户多次截图来保证内容完整性。为了解决这一问题，本文将介绍长截图功能，使用户能够一键截取整个页面的长图，更轻松地分享和保存信息。

长截图功能适用于支持滚动的UI组件，比如List组件、Scroll组件、Web组件等。本文将以List组件为例来介绍长截图功能的开发，通过控制器[Scroller](../harmonyos-references/ts-container-scroll.md#scroller)，结合UIContext的getComponentSnapshot().[get()](../harmonyos-references/arkts-apis-uicontext-componentsnapshot.md#get12-1)方法，实现长截图功能。

## 实现原理

List组件可以通过模拟用户滚动行为，然后使用getComponentSnapshot().get()方法逐步截取不同位置的画面，将这些画面通过拼接得到长截图。List组件通过[Scroller](../harmonyos-references/ts-container-scroll.md#scroller)的相关API控制组件滚动。

长截图拼接原理如下，将每次滚动新进入屏幕的内容裁剪后，拼接到之前的屏幕截图，依次类推。

**图 1** 长截图拼接原理图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/B4DRM0U3Q4a5hOp6L1StrQ/zh-cn_image_0000002797180345.png)

长截图主要流程如下：

**图 2** 滚动长截图流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/ay5d61zrRXKTpaxFJG_uiw/zh-cn_image_0000002768020366.png)

**说明** 

在长截图的拼接过程中，所有截图会被暂时缓存到内存中。对于无限滚动或数据量较大的场景，应当限制单张截图的高度，以防止过高的内存占用影响应用性能。

## 滚动组件长截图

List、Scroll、Grid、WaterFlow等滚动组件均是通过Scroller来控制组件滚动，本章将以List组件为例来介绍滚动组件长截图的实现。下面介绍了滚动组件两种常见的长截图场景，一键截图和滚动截图。

### 一键截图

**场景描述**

一键截图将组件数据从顶部截取到底部，在截图过程中用户看不到界面的滚动，实现无感知滚动截图。这种方案一般用于分享截图、保存数据量较少的场景。

**实现效果**

点击“一键截图”，会生成整个列表的长截图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/f_YxuNGAROW7BwWmrQHadg/zh-cn_image_0000002797300315.gif)

**开发流程**

1. 给List绑定滚动控制器，添加监听事件。

   1. 为List滚动组件绑定[Scroller](../harmonyos-references/ts-container-scroll.md#scroller)控制器，以控制其滚动行为，并给List组件绑定自定义的id。
   2. 通过[onDidScroll()](../harmonyos-references/ts-container-scroll.md#ondidscroll12)方法实时监听并获取滚动偏移量，确保截图拼接位置的准确性。
   3. 同时，利用[onAreaChange()](../harmonyos-references/ts-universal-component-area-change-event.md#onareachange)事件获取List组件的尺寸，以便精确计算截图区域的大小。

      ```typescript
      @ComponentV2
      export struct ScrollSnapshot {
        @Local sizeInfo: WindowSizeInfo =
          AppStorageV2.connect(WindowSizeInfo, 'windowSizeInfo', () => new WindowSizeInfo()) ?? new WindowSizeInfo();
        // 截图过程中覆盖组件的遮罩图
        @Local componentMaskImage: PixelMap | undefined = undefined;
        // 是否点击停止滚动
        @Local isEnableScroll: boolean = true;
        // 是否显示预览窗口
        @Local isShowPreview: boolean = false;
        // 拼接后的长图
        @Local mergedImage: PixelMap | undefined = undefined;
        // 滚动控制器
        private scroller: Scroller = new Scroller();
        private listComponentWidth: number = 0;
        private listComponentHeight: number = 0;
        // List组件的当前偏移量
        private curYOffset: number = 0;
        private scrollHeight: number = 0;
        // ...
        build() {
          // ...
              Stack() {
                // ...
                List({
                  space: 12,
                  scroller: this.scroller
                })
                // ...
                .id(LIST_ID)
                .onDidScroll(() => {
                  this.curYOffset = this.scroller.currentOffset().yOffset;
                })
                .onAreaChange((oldValue, newValue) => {
                  this.listComponentWidth = newValue.width as number;
                  this.listComponentHeight = newValue.height as number;
                  this.scrollHeight = this.listComponentHeight;
                })
                .onClick(() => {
                  // 点击列表停止滚动
                  if (!this.isEnableScroll) {
                    this.scroller.scrollBy(0, 0);
                    this.isClickStop = true;
                  }
                })
              }
              .width('100%')
              .layoutWeight(1)
              .padding({
                left: 16,
                right: 16,
                top: 16
              })
              .bindContentCover(this.isShowPreview!!, this.previewWindowComponent(),
                {
                  modalTransition: ModalTransition.NONE,
                  onWillDismiss: (action: DismissContentCoverAction) => {
                    if (action.reason === DismissReason.PRESS_BACK) {
                      Logger.info('BindContentCover dismiss reason is back pressed');
                    }
                  }
                })
              Row({ space: 12 }) {
                Button($r('app.string.one_click_snapshot'))
                  .layoutWeight(1)
                  .onClick(() => {
                    this.onceSnapshot();
                  })
                Button($r('app.string.scroll_snapshot'))
                  .layoutWeight(1)
                  .onClick(() => {
                    // 防止用户在截图过程中点击按钮
                    // 导致方法被重复调用而产生异常
                    if (this.scrollYOffsets.length === 0) {
                      this.scrollSnapshot();
                    }
                  })
              }
              .width('100%')
              .padding({
                left: 16,
                right: 16,
                bottom: this.sizeInfo.naviIndicatorHeight + 16,
                top: 12
              })
            }
          }
          .title($r('app.string.title_scroll_snapshot'))
          .backgroundColor($r('sys.color.background_secondary'))
        }
      }
      ```
2. 给List添加遮罩图，初始化滚动位置。

   “一键截图”功能确保在滚动截图过程中用户不会察觉到页面的滚动。通过截取当前屏幕生成遮罩图覆盖列表，并记录此时的滚动偏移量（yOffsetBefore），便于后续完成滚动截图之后，恢复到之前记录的偏移量，使用户无感知页面变化。

   为保证截图的完整性，设置完遮罩图后，同样利用scrollTo()方法将列表暂时滚至顶部，确保截图从最顶端开始。

   ```typescript
   @ComponentV2
   export struct ScrollSnapshot {
     @Local sizeInfo: WindowSizeInfo =
       AppStorageV2.connect(WindowSizeInfo, 'windowSizeInfo', () => new WindowSizeInfo()) ?? new WindowSizeInfo();
     // 截图过程中覆盖组件的遮罩图
     @Local componentMaskImage: PixelMap | undefined = undefined;
     // 是否点击停止滚动
     @Local isEnableScroll: boolean = true;
     // 是否显示预览窗口
     @Local isShowPreview: boolean = false;
     // 拼接后的长图
     @Local mergedImage: PixelMap | undefined = undefined;
     // 滚动控制器
     private scroller: Scroller = new Scroller();
     private listComponentWidth: number = 0;
     private listComponentHeight: number = 0;
     // List组件的当前偏移量
     private curYOffset: number = 0;
     private scrollHeight: number = 0;
     // 截图前备份的组件位置
     private yOffsetBefore: number = 0;
     // ...
     /**
      * 一键截图
      */
     async onceSnapshot() {
       await this.beforeSnapshot();
       await this.snapAndMerge();
       await this.afterSnapshot();
       // ...
     }

     // ...

     async beforeSnapshot() {
       try {
         this.yOffsetBefore = this.curYOffset;
         // 对已加载的List组件截图，作为List组件的封面图
         this.componentMaskImage = await this.getUIContext().getComponentSnapshot().get(LIST_ID);
         this.scroller.scrollTo({
           xOffset: 0,
           yOffset: 0,
           animation: {
             duration: 200
           }
         });
         // ...
         await CommonUtils.sleep(200);
       } catch (err) {
         let error = err as BusinessError;
         Logger.error(TAG, `beforeSnapshot err, errCode: ${error.code}, error message: ${error.message}`);
       }
     }

     async afterSnapshot() {
       this.scroller.scrollTo({
         xOffset: 0,
         yOffset: this.yOffsetBefore,
         animation: {
           duration: 200
         }
       });
       await CommonUtils.sleep(200);
     }

     async afterGeneratorImage() {
       // 延时用于过渡动画
       await CommonUtils.sleep(200);
       this.componentMaskImage = undefined;
       this.scrollYOffsets.length = 0;
       this.areaArray.length = 0;
     }
     // ...
     build() {
       // ...
           Stack() {
             // 截图过程的遮罩层，防止用户察觉到屏幕快速滑动
             // 提升用户体验
             if (this.componentMaskImage) {
               Image(this.componentMaskImage)
               // ...
             }
             List({
               space: 12,
               scroller: this.scroller
             })
             // ...
             .id(LIST_ID)
             .onDidScroll(() => {
               this.curYOffset = this.scroller.currentOffset().yOffset;
             })
             .onAreaChange((oldValue, newValue) => {
               this.listComponentWidth = newValue.width as number;
               this.listComponentHeight = newValue.height as number;
               this.scrollHeight = this.listComponentHeight;
             })
             .onClick(() => {
               // 点击列表停止滚动
               if (!this.isEnableScroll) {
                 this.scroller.scrollBy(0, 0);
                 this.isClickStop = true;
               }
             })
           }
           // ...
     }
   }
   ```
3. 循环滚动截图，裁剪和缓存截图数据。

   1. 记录每次滚动的位置到数组scrollYOffsets中，并使用componentSnapshot.get(LIST\_ID)方法获取当前画面的截图。
   2. 如果非首次截图，则使用[crop](../harmonyos-references/arkts-apis-image-pixelmap.md#crop9)方法截取从底部滚动进来的区域，然后调用pixmap.readPixelsSync(area)方法将截图数据读取到缓冲区域area中，并将area通过集合进行保存，用于后续截图拼接。
   3. 如果页面没有滚动到底部，继续滚动，继续递归调用snapAndMerge()方法进行截图；如果到达底部，则调用mergeImage()方法拼接所有收集到的图像片段，生成完整的长截图；同时还需限制截图的高度，以防过大的截图占用过多内存，影响应用性能，例如这里设置截长截图高度不超过5000。

      ```typescript
      /**
       * 一键截图循环遍历截图并合并
       */
      async snapAndMerge() {
        try {
          this.scrollYOffsets.push(this.curYOffset);
          // 调用组件截图接口获取当前截图
          const pixelMap = await this.getUIContext().getComponentSnapshot().get(LIST_ID);
          // 获取图像像素每行的字节数
          let area: image.PositionArea =
            await ImageUtils.getSnapshotArea(this.getUIContext(), pixelMap, this.scrollYOffsets, this.listComponentWidth,
              this.listComponentHeight);
          this.areaArray.push(area);
          // 循环过程中判断是否已到达底部
          if (!this.scroller.isAtEnd()) {
            CommonUtils.scrollAnimation(this.scroller, 200, this.scrollHeight);
            await CommonUtils.sleep(200);
            await this.snapAndMerge();
          } else {
            this.mergedImage =
              await ImageUtils.mergeImage(this.getUIContext(), this.areaArray,
                this.scrollYOffsets[this.scrollYOffsets.length - 1], this.listComponentHeight);
          }
        } catch (err) {
          let error = err as BusinessError;
          Logger.error(TAG, `snapAndMerge err, errCode: ${error.code}, error message: ${error.message}`);
        }
      }
      ```

      ```typescript
      /**
       * 将截图的PixelMap对象读取到缓冲区
       * @param {PixelMap} pixelMap - 截图的PixelMap
       * @param {number[]} scrollYOffsets - 组件滚动的y轴偏移量数组
       * @param {number} listWidth - List组件宽度
       * @param {number} listHeight - List组件高度
       * @returns {image.PositionArea} 图片缓冲区
       */
      static async getSnapshotArea(uiContext: UIContext, pixelMap: PixelMap, scrollYOffsets: number[], listWidth: number,
        listHeight: number): Promise<image.PositionArea> {
        // 获取图像像素每行的字节数
        let stride = pixelMap.getBytesNumberPerRow();
        // 获取图像像素的总字节数
        let bytesNumber = pixelMap.getPixelBytesNumber();
        let buffer: ArrayBuffer = new ArrayBuffer(bytesNumber);
        // 区域大小，按区域读取。PositionArea表示图像指定区域内的数据。
        let len = scrollYOffsets.length;

        // 除第一次截图不需要裁剪外，其余需要裁剪新增部分
        if (scrollYOffsets.length >= 2) {
          // 实际滚动距离
          let realScrollHeight = scrollYOffsets[len - 1] - scrollYOffsets[len - 2];
          Logger.info(TAG, `getSnapshotArea: realScrollHeight=${realScrollHeight}, listHeight=${listHeight}`);
          if (realScrollHeight > 0 && listHeight - realScrollHeight > 0) {
            let cropRegion: image.Region = {
              x: 0,
              y: Math.ceil(uiContext.vp2px(listHeight - realScrollHeight)),
              size: {
                height: uiContext.vp2px(realScrollHeight),
                width: uiContext.vp2px(listWidth)
              }
            };
            // 裁剪滚动区域
            try {
              await pixelMap.crop(cropRegion);
            } catch (err) {
              let error = err as BusinessError;
              Logger.error(TAG, `crop err, code: ${error.code}, message: ${error.message}`);
            }
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
          // 区域大小，按区域读取。PositionArea表示图像指定区域内的数据。
          area = {
            pixels: buffer,
            offset: 0,
            stride: stride,
            region: {
              size: {
                width: imgInfo.size.width,
                height: imgInfo.size.height
              },
              x: 0,
              y: 0
            }
          }
          // 将数据写入指定区域
          pixelMap.readPixelsSync(area);
        } catch (err) {
          let error = err as BusinessError;
          Logger.error(TAG, `getSnapshotArea err, code: ${error.code}, message: ${error.message}`);
        }
        return area;
      }
      ```
4. 拼接截图片段。

   使用image.createPixelMapSync()方法创建长截图longPixelMap，并遍历之前保存的图像片段数据(this.areaArray)，构建image.PositionArea对象area，然后调用longPixelMap.writePixelsSync(area)方法将这些片段逐个写入到正确的位置，从而拼接成一个完整的长截图。

   ```typescript
   /**
    * 将图片区域数组合并为长截图
    * @param {image.PositionArea[]} areaArray - 截图区域
    * @param {number} lastOffsetY - 最后一次截图的Y轴偏移量
    * @param {number} listWidth - List组件宽度
    * @param {number} listHeight - List组件高度
    * @returns {PixelMap} 合并后的长图
    */
   static async mergeImage(uiContext: UIContext, areaArray: image.PositionArea[], lastOffsetY: number,
     listHeight: number): Promise<PixelMap> {
     // 创建长截图PixelMap
     let opts: image.InitializationOptions = {
       editable: true,
       pixelFormat: PIXEL_FORMAT_RGBA_8888,
       size: {
         // 需要确保PixelMap的宽度大于区域的宽度
         width: ImageUtils.getMaxAreaWidth(areaArray),
         height: uiContext.vp2px(lastOffsetY + listHeight)
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
5. 恢复到截图前的状态，滚动到截图前的位置。

   ```ts
   async afterSnapshot() {
     this.scroller.scrollTo({
       xOffset: 0,
       yOffset: this.yOffsetBefore,
       animation: {
         duration: 200
       }
     });
     await CommonUtils.sleep(200);
   }
   ```
6. 使用安全控件SaveButton保存截图相册。

   通过安全控件[SaveButton](../harmonyos-references/ts-security-components-savebutton.md)结合[@ohos.file.photoAccessHelper (相册管理模块)](../harmonyos-references/js-apis-photoaccesshelper.md)保存截图到相册。

   ```ts
   SaveButton({
     icon: SaveIconStyle.FULL_FILLED,
     text: SaveDescription.SAVE_IMAGE,
     buttonType: ButtonType.Capsule
   })
   // ...
     .onClick((event, result) => {
       this.saveSnapshot(result);
     })
   ```

   ```typescript
   /**
    * 将图片保存到相册
    * @param {SaveButtonOnClickResult} result - 安全控件返回的结果
    */
   async saveSnapshot(result: SaveButtonOnClickResult): Promise<void> {
     try {
       if (result === SaveButtonOnClickResult.SUCCESS) {
         const helper = photoAccessHelper.getPhotoAccessHelper(this.context);
         const uri = await helper.createAsset(photoAccessHelper.PhotoType.IMAGE, 'png');
         // 以URI打开文件以连续写入内容
         const file = await fileIo.open(uri, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
         const imagePackerApi: image.ImagePacker = image.createImagePacker();
         const packOpts: image.PackingOption = {
           format: 'image/png',
           quality: 100,
         };
         imagePackerApi.packToData(this.mergedImage, packOpts).then((data) => {
           fileIo.writeSync(file.fd, data);
           fileIo.closeSync(file.fd);
           Logger.info(TAG, `Succeeded in packToFile`);
           this.getUIContext().getPromptAction().showToast({
             message: $r('app.string.save_album_success'),
             duration: 1800
           })
         }).catch((error: BusinessError) => {
           Logger.error(TAG, `Failed to packToFile. Error code is ${error.code}, message is ${error.message}`);
         });
       }
       // ...
     } catch (err) {
       let error = err as BusinessError;
       Logger.error(TAG, `saveSnapshot err, errCode: ${error.code}, error message: ${error.message}`);
     }
   }
   ```

### 滚动截图

**场景描述**

此方案允许用户控制长截图的起止位置，增加了使用的灵活性。它适用于大数据量场景，方便用户选择性保存滚动组件中的特定数据。

**实现效果**

点击“滚动截图”按钮后，列表将自动滚动。点击列表中的任意条目时，滚动会立即停止，并开始截取从滚动开始到停止这段时间内的数据截图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/d2rmzCf6Qb2OED49IS5rsw/zh-cn_image_0000002767860382.gif)

**功能实现**

“滚动截图”功能的实现流程与前述的“一键截图”一样，因此这里不再重复详述整个过程，而仅聚焦于其中的几个关键差异点，例如滚动的控制和偏移量的记录，分别如下面1和2所描述。

1. 在截图滚动的过程中，为了防止用户手动滚动对截图产生干扰，应禁用列表的手动滚动功能。可以通过设置List组件的[enableScrollInteraction](../harmonyos-references/ts-container-list.md#enablescrollinteraction10)属性来控制是否允许手动滚动。

   当准备开始截图时，将isEnableScroll设置为false以禁用滚动交互。而当用户点击列表项以确定截图结束位置时，使用scroller.scrollBy(0, 0)方法确保列表立即停止滑动。

   ```typescript
   @ComponentV2
   export struct ScrollSnapshot {
     // ...
     /**
      * 滚动截图
      */
     async scrollSnapshot() {
       // 截图过程中设置列表不可手动滚动
       // 以避免对截图造成干扰
       this.isEnableScroll = false;
       // 保存组件当前位置以便恢复
       this.yOffsetBefore = this.curYOffset;
       // 设置提示弹窗居中
       await this.scrollSnapAndMerge();
       // ...
       this.isEnableScroll = true;
       this.isClickStop = false;
     }

     /**
      * 一键截图循环遍历截图并合并
      */
     async snapAndMerge() {
       try {
         this.scrollYOffsets.push(this.curYOffset);
         // 调用组件截图接口获取当前截图
         const pixelMap = await this.getUIContext().getComponentSnapshot().get(LIST_ID);
         // 获取图像像素每行的字节数
         let area: image.PositionArea =
           await ImageUtils.getSnapshotArea(this.getUIContext(), pixelMap, this.scrollYOffsets, this.listComponentWidth,
             this.listComponentHeight);
         this.areaArray.push(area);
         // 循环过程中判断是否已到达底部
         if (!this.scroller.isAtEnd()) {
           CommonUtils.scrollAnimation(this.scroller, 200, this.scrollHeight);
           await CommonUtils.sleep(200);
           await this.snapAndMerge();
         } else {
           this.mergedImage =
             await ImageUtils.mergeImage(this.getUIContext(), this.areaArray,
               this.scrollYOffsets[this.scrollYOffsets.length - 1], this.listComponentHeight);
         }
       } catch (err) {
         let error = err as BusinessError;
         Logger.error(TAG, `snapAndMerge err, errCode: ${error.code}, error message: ${error.message}`);
       }
     }

     /**
      * 滚动截图，循环遍历截图并合并
      */
     async scrollSnapAndMerge() {
       try {
         // 记录滚动偏移量数组
         this.scrollYOffsets.push(this.curYOffset - this.yOffsetBefore);
         Logger.info(TAG, `scrollSnapAndMerge: curYOffset=${this.curYOffset}, yOffsetBefore=${this.yOffsetBefore}, isAtEnd=${this.scroller.isAtEnd()}, scrollHeight=${this.scrollHeight}`);
         // 调用截图接口获取当前截图
         const pixelMap = await this.getUIContext().getComponentSnapshot().get(LIST_ID);
         if (!pixelMap) {
           Logger.error(TAG, 'scrollSnapAndMerge: component snapshot is null');
           return;
         }
         // 获取图像像素每行的字节数
         let area: image.PositionArea =
           await ImageUtils.getSnapshotArea(this.getUIContext(), pixelMap, this.scrollYOffsets, this.listComponentWidth,
             this.listComponentHeight);
         this.areaArray.push(area);

         // 循环过程中判断是否到达底部，且用户未停止截图
         if (!this.scroller.isAtEnd() && !this.isClickStop) {
           // 未滚动到底部，滚动到下一页
           CommonUtils.scrollAnimation(this.scroller, 1000, this.scrollHeight);
           await CommonUtils.sleep(1500);
           await this.scrollSnapAndMerge();
         } else {
           // 滚动到底部后，将每轮滚动获得的缓冲区拼接
           // 生成一张长截图
           this.mergedImage =
             await ImageUtils.mergeImage(this.getUIContext(), this.areaArray,
               this.scrollYOffsets[this.scrollYOffsets.length - 1], this.listComponentHeight);
         }
       } catch (err) {
         let error = err as BusinessError;
         Logger.error(TAG, `scrollSnapAndMerge err, errCode: ${error.code}, message: ${error.message}, stack: ${error.stack ?? ''}`);
       }
     }

     async beforeSnapshot() {
       try {
         this.yOffsetBefore = this.curYOffset;
         // 对已加载的List组件截图，作为List组件的封面图
         this.componentMaskImage = await this.getUIContext().getComponentSnapshot().get(LIST_ID);
         this.scroller.scrollTo({
           xOffset: 0,
           yOffset: 0,
           animation: {
             duration: 200
           }
         });
         this.isShowPreview = true;
         // 延时确保滚动已到达顶部
         await CommonUtils.sleep(200);
       } catch (err) {
         let error = err as BusinessError;
         Logger.error(TAG, `beforeSnapshot err, errCode: ${error.code}, error message: ${error.message}`);
       }
     }

     async afterSnapshot() {
       this.scroller.scrollTo({
         xOffset: 0,
         yOffset: this.yOffsetBefore,
         animation: {
           duration: 200
         }
       });
       await CommonUtils.sleep(200);
     }

     async afterGeneratorImage() {
       // 延时用于过渡动画
       await CommonUtils.sleep(200);
       this.componentMaskImage = undefined;
       this.scrollYOffsets.length = 0;
       this.areaArray.length = 0;
     }

     @Builder
     previewWindowComponent() {
       Column() {
         SnapshotPreview({
           mergedImage: this.mergedImage,
           onMergedImageChange: (value: PixelMap | undefined) => { this.mergedImage = value; },
           isShowPreview: this.isShowPreview,
           onIsShowPreviewChange: (value: boolean) => { this.isShowPreview = value; }
         })
       }
     }
     build() {
       // ...
             List({
               space: 12,
               scroller: this.scroller
             })
             // ...
             .id(LIST_ID)
             .onDidScroll(() => {
               this.curYOffset = this.scroller.currentOffset().yOffset;
             })
             .onAreaChange((oldValue, newValue) => {
               this.listComponentWidth = newValue.width as number;
               this.listComponentHeight = newValue.height as number;
               this.scrollHeight = this.listComponentHeight;
             })
             .onClick(() => {
               // 点击列表停止滚动
               if (!this.isEnableScroll) {
                 this.scroller.scrollBy(0, 0);
                 this.isClickStop = true;
               }
             })
           }
           .width('100%')
           .layoutWeight(1)
           .padding({
             left: 16,
             right: 16,
             top: 16
           })
           .bindContentCover(this.isShowPreview!!, this.previewWindowComponent(),
             {
               modalTransition: ModalTransition.NONE,
               onWillDismiss: (action: DismissContentCoverAction) => {
                 if (action.reason === DismissReason.PRESS_BACK) {
                   Logger.info('BindContentCover dismiss reason is back pressed');
                 }
               }
             })
           // ...
     }
   }
   ```
2. “滚动截图”功能依据当前坐标启动截图过程，因此在记录滚动偏移量时，通过this.curYOffset - this.yOffsetBefore来计算相对于初始位置的变化。

   ```typescript
   /**
    * 滚动截图，循环遍历截图并合并
    */
   async scrollSnapAndMerge() {
     try {
       // 记录滚动偏移量数组
       this.scrollYOffsets.push(this.curYOffset - this.yOffsetBefore);
       Logger.info(TAG, `scrollSnapAndMerge: curYOffset=${this.curYOffset}, yOffsetBefore=${this.yOffsetBefore}, isAtEnd=${this.scroller.isAtEnd()}, scrollHeight=${this.scrollHeight}`);
       // 调用截图接口获取当前截图
       const pixelMap = await this.getUIContext().getComponentSnapshot().get(LIST_ID);
       if (!pixelMap) {
         Logger.error(TAG, 'scrollSnapAndMerge: component snapshot is null');
         return;
       }
       // 获取图像像素每行的字节数
       let area: image.PositionArea =
         await ImageUtils.getSnapshotArea(this.getUIContext(), pixelMap, this.scrollYOffsets, this.listComponentWidth,
           this.listComponentHeight);
       this.areaArray.push(area);

       // 循环过程中判断是否到达底部，且用户未停止截图
       if (!this.scroller.isAtEnd() && !this.isClickStop) {
         // 未滚动到底部，滚动到下一页
         CommonUtils.scrollAnimation(this.scroller, 1000, this.scrollHeight);
         await CommonUtils.sleep(1500);
         await this.scrollSnapAndMerge();
       } else {
         // 滚动到底部后，将每轮滚动获得的缓冲区拼接
         // 生成一张长截图
         this.mergedImage =
           await ImageUtils.mergeImage(this.getUIContext(), this.areaArray,
             this.scrollYOffsets[this.scrollYOffsets.length - 1], this.listComponentHeight);
       }
     } catch (err) {
       let error = err as BusinessError;
       Logger.error(TAG, `scrollSnapAndMerge err, errCode: ${error.code}, message: ${error.message}, stack: ${error.stack ?? ''}`);
     }
   }
   ```
3. 与“一键截图”不同，“滚动截图”在执行过程中不使用遮罩层，用户能够直接看到列表的滚动效果。为了确保流畅的视觉体验，在调用scroller.scrollTo进行滚动时，添加了动画效果，使得滚动更加自然和顺滑。

   ```ts
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

## 示例代码

* [实现长截图功能](https://gitcode.com/harmonyos_samples/LongSnapshotPractice)
