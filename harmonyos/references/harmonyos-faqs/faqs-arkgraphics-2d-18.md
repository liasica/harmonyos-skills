---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkgraphics-2d-18
title: 实现图片旋转、缩放裁剪预览效果
breadcrumb: FAQ > 图形开发 > 2D图形（ArkGraphics 2D） > 实现图片旋转、缩放裁剪预览效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:46+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:98cf97754afb5d00730db0971fc79ac6b4dfa8ba3d2427d4a8209a622c05583a
---

## 问题现象

在开发中需要实现对图片的旋转、缩放，裁剪出指定的区域，如何实现？

## 背景知识

* [PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)：图像像素类，可以有效地存储图像的原始数据，使其可以方便地进行图像变换，如裁剪、缩放、偏移、旋转、翻转等。
* [PinchGesture](../harmonyos-references/ts-basic-gestures-pinchgesture.md)：捏合手势事件，用于图片放大缩小。
* [PanGesture](../harmonyos-references/ts-basic-gestures-pangesture.md)：滑动手势事件，用于图片平移。
* [Canvas](../harmonyos-references/ts-components-canvas-canvas.md)：画布组件，用于自定义绘制裁剪图形。

## 解决方案

1. 使用Canvas组件绘制裁剪框，自定义裁剪区域大小。

   ```ts
   Canvas(this.context)
     .width('100%')
     .height('100%')
     .backgroundColor(Color.Transparent)
     .onReady(() => {
       if (this.context == null) {
         return;
       }
       let height = this.context.height;
       let width = this.context.width;
       this.context.fillStyle = this.model.maskColor;
       this.context.fillRect(0, 0, width, height);
       // 把中间的取景框透出来
       this.context.globalCompositeOperation = 'destination-out';
       this.context.fillStyle = 'white';
       let frameWidthInVp = this.getUIContext().px2vp(this.model.frameWidth);
       let frameHeightInVp = this.getUIContext().px2vp(this.model.getFrameHeight());
       let x = (width - this.getUIContext().px2vp(this.model.frameWidth)) / 2;
       let y = (height - this.getUIContext().px2vp(this.model.getFrameHeight())) / 2;
       this.context.fillRect(x, y, frameWidthInVp, frameHeightInVp);
       // 画出取景框边线，使边界明显一点
       this.context.globalCompositeOperation = 'source-over';
       this.context.strokeStyle = this.model.strokeColor;
       this.context.strokeRect(x, y, frameWidthInVp, frameHeightInVp);
     })
     .enabled(false);
   ```
2. 给图片添加平移、捏合手势，用于移动图片指定区域到裁剪框中。

   ```ts
   .gesture(
     GestureGroup(GestureMode.Parallel,
       // 拖动手势
       PanGesture({})
         .onActionStart(() => {
           this.startOffsetX = this.model.offsetX;
           this.startOffsetY = this.model.offsetY;
         })
         .onActionUpdate((event: GestureEvent) => {
           if (event) {
             if (this.model.panEnabled) {
               let distanceX: number = this.startOffsetX;
               let distanceY: number = this.startOffsetY;
               // 根据旋转角度调整移动方向
               const rotation = this.model.rotation;
               if (rotation === 0) {
                 // 0度旋转：正常移动
                 distanceX += this.getUIContext().vp2px(event.offsetX) / this.model.scale;
                 distanceY += this.getUIContext().vp2px(event.offsetY) / this.model.scale;
                 this.model.offsetX = distanceX;
                 this.model.offsetY = distanceY;
               } else if (rotation === 90) {
                 // 90度旋转：X和Y方向交换，Y方向取反
                 distanceX += this.getUIContext().vp2px(event.offsetY) / this.model.scale;
                 distanceY -= this.getUIContext().vp2px(event.offsetX) / this.model.scale;
                 this.model.offsetX = distanceX;
                 this.model.offsetY = distanceY;
               } else if (rotation === 180) {
                 // 180度旋转：X和Y方向都取反
                 distanceX -= this.getUIContext().vp2px(event.offsetX) / this.model.scale;
                 distanceY -= this.getUIContext().vp2px(event.offsetY) / this.model.scale;
                 this.model.offsetX = distanceX;
                 this.model.offsetY = distanceY;
               } else if (rotation === 270) {
                 // 270度旋转：X和Y方向交换，X方向取反
                 distanceX -= this.getUIContext().vp2px(event.offsetY) / this.model.scale;
                 distanceY += this.getUIContext().vp2px(event.offsetX) / this.model.scale;
                 this.model.offsetX = distanceX;
                 this.model.offsetY = distanceY;
               }
               this.model.offsetX = distanceX;
               this.model.offsetY = distanceY;
               this.updateMatrix();
             }
           }
         })
         .onActionEnd(() => {
           this.checkImageAdapt();
         }),
       // 缩放手势处理
       PinchGesture({ fingers: 2 })
         .onActionStart(() => {
           this.tempScale = this.model.scale;
         })
         .onActionUpdate((event) => {
           if (event) {
             if (!this.model.zoomEnabled) {
               return;
             }
             this.zoomTo(this.tempScale * event.scale, this.model.rotation);
           }
         })
         .onActionEnd(() => {
           this.checkImageAdapt();
         }),
       RotationGesture({ fingers: 3 })
         .onActionStart(() => {
           this.tempRotate = this.model.rotation;
         })
         .onActionUpdate((event) => {
           if (event) {
             if (!this.model.zoomEnabled) {
               return;
             }
             this.zoomTo(1, this.tempRotate + event.angle);
           }
         })
         .onActionEnd(() => {
           this.checkImageAdapt();
         })
     )
   );
   ```
3. 根据手势结果，调整图片位置，确保图片填满裁剪框。

   ```ts
   private checkImageAdapt() {
     let offsetX = this.model.offsetX;
     let offsetY = this.model.offsetY;
     let scale = this.model.scale;
     hilog.info(0, 'CropPage', `offsetX: ${offsetX}, offsetY: ${offsetY}, scale: ${scale}`);

     // 图片适配控件的时候也进行了缩放，计算出这个缩放比例
     let widthScale = this.model.componentWidth / this.model.imageWidth;
     let heightScale = this.model.componentHeight / this.model.imageHeight;
     let adaptScale = Math.min(widthScale, heightScale);
     hilog.info(0, 'CropPage',
       `Image scale ${adaptScale} while attaching the component[${this.model.componentWidth}, ${this.model.componentHeight}]`);

     // 经过两次缩放(适配控件、手势)后，图片的实际显示大小
     let showWidth = this.model.imageWidth * adaptScale * this.model.scale;
     let showHeight = this.model.imageHeight * adaptScale * this.model.scale;

     if (this.model.rotation === 0) {
       showWidth = this.model.imageWidth * adaptScale * this.model.scale;
       showHeight = this.model.imageHeight * adaptScale * this.model.scale;
     } else if (this.model.rotation === 90) {
       showWidth = this.model.imageHeight * adaptScale * this.model.scale;
       showHeight = this.model.imageWidth * adaptScale * this.model.scale;
     } else if (this.model.rotation === 180) {
       showWidth = this.model.imageWidth * adaptScale * this.model.scale;
       showHeight = this.model.imageHeight * adaptScale * this.model.scale;
     } else if (this.model.rotation === 270) {
       showWidth = this.model.imageHeight * adaptScale * this.model.scale;
       showHeight = this.model.imageWidth * adaptScale * this.model.scale;
     }
     let imageX = (this.model.componentWidth - showWidth) / 2;
     let imageY = (this.model.componentHeight - showHeight) / 2;
     hilog.info(0, 'CropPage', `Image left top is (${imageX}, ${imageY})`);

     // 取景框的左上角坐标
     let frameX = (this.model.componentWidth - this.model.frameWidth) / 2;
     let frameY = (this.model.componentHeight - this.model.getFrameHeight()) / 2;
     hilog.info(0, 'CropPage', `Frame left top is (${frameX}, ${frameY})`);

     // 图片左上角坐标
     let showX = imageX + offsetX * scale;
     let showY = imageY + offsetY * scale;
     hilog.info(0, 'CropPage', `Image show at (${showX}, ${showY})`);

     if (this.model.rotation === 0) {
       showX = imageX + offsetX * scale;
       showY = imageY + offsetY * scale;
     } else if (this.model.rotation === 90) {
       showX = imageX - offsetY * scale;
       showY = imageY + offsetX * scale;
     } else if (this.model.rotation === 180) {
       showX = imageX - offsetX * scale;
       showY = imageY - offsetY * scale;
     } else if (this.model.rotation === 270) {
       showX = imageX + offsetY * scale;
       showY = imageY - offsetX * scale;
     }

     // 图片缩放后，大小不足以填满取景框
     if (this.model.frameWidth > showWidth || this.model.getFrameHeight() > showHeight) {
       let xScale = this.model.frameWidth / showWidth;
       let yScale = this.model.getFrameHeight() / showHeight;
       let newScale = Math.max(xScale, yScale);
       this.model.scale = this.model.scale * newScale;
       showX *= newScale;
       showY *= newScale;
     }

     // 调整x轴方向位置，使图像填满取景框
     if (showX > frameX) {
       showX = frameX;
     } else if (showX + showWidth < frameX + this.model.frameWidth) {
       showX = frameX + this.model.frameWidth - showWidth;
     }
     // 调整y轴方向位置，使图像填满取景框
     if (showY > frameY) {
       showY = frameY;
     } else if (showY + showHeight < frameY + this.model.getFrameHeight()) {
       showY = frameY + this.model.getFrameHeight() - showHeight;
     }
     this.model.offsetX = (showX - imageX) / scale;
     this.model.offsetY = (showY - imageY) / scale;

     if (this.model.rotation === 0) {
       this.model.offsetX = (showX - imageX) / scale;
       this.model.offsetY = (showY - imageY) / scale;
     } else if (this.model.rotation === 90) {
       this.model.offsetX = (showY - imageY) / scale;
       this.model.offsetY = -(showX - imageX) / scale;
     } else if (this.model.rotation === 180) {
       this.model.offsetX = -(showX - imageX) / scale;
       this.model.offsetY = -(showY - imageY) / scale;
     } else if (this.model.rotation === 270) {
       this.model.offsetX = -(showY - imageY) / scale;
       this.model.offsetY = (showX - imageX) / scale;
     }
     this.updateMatrix();
   }

   public updateMatrix(): void {
     this.matrix = Matrix4.identity()
       .translate({ x: this.model.offsetX, y: this.model.offsetY })
       .rotate({ z: 1, angle: this.model.rotation })
       .scale({ x: this.model.scale, y: this.model.scale });
   }
   ```
4. 根据缩放比例、平移位置和裁剪区域坐标裁剪图片。

   ```ts
   public async crop(): Promise<image.PixelMap> {
     if (!this.src || this.src === '') {
     throw new Error('Please set src first');
   }
   if (this.imageWidth === 0 || this.imageHeight === 0) {
     throw new Error('The image is not loaded');
   }

   // 打开图片文件
   let file = fs.openSync(this.src, fs.OpenMode.READ_ONLY);
   let imageSource: image.ImageSource = image.createImageSource(file.fd);
   let decodingOptions: image.DecodingOptions = {
     editable: true,
     desiredPixelFormat: image.PixelMapFormat.RGBA_8888,
   };

   // 创建pixelMap
   let pm = await imageSource.createPixelMap(decodingOptions);

   // 获取原始图像尺寸
   let originalWidth = this.imageWidth;
   let originalHeight = this.imageHeight;

   // 第一步：先旋转整个图像（注意：rotateSync 会修改图像尺寸）
   if (this.rotation !== 0) {
     pm.rotateSync(this.rotation);

     // 更新图像尺寸（90度和270度旋转会交换宽高）
     if (this.rotation === 90 || this.rotation === 270) {
       let tmp_wh = originalWidth;
       originalWidth = originalHeight;
       originalHeight = tmp_wh;
     }
   }

   // 第二步：计算缩放比例与裁剪区域
   // 图片适配控件时的缩放比例
   let widthScale = this.componentWidth / this.imageWidth;
   let heightScale = this.componentHeight / this.imageHeight;
   let adaptScale = Math.min(widthScale, heightScale);

   // 总缩放比例 = 适配缩放 × 手势缩放
   let totalScale = adaptScale * this.scale;

   // 旋转 90° 或 270° 时，图像宽高交换，缩放比例应基于新方向
   let totalRotateScale = totalScale;

   // 仅在 90°/270° 时，使用 totalRotateScale 作为裁剪坐标换算比例
   if (this.rotation === 90 || this.rotation === 270) {
     totalRotateScale = totalScale;
   }

   // 计算图片在组件中的实际显示大小
   let showWidth = originalWidth * totalScale;
   let showHeight = originalHeight * totalScale;

   // 图片左上角坐标（基于组件坐标系）
   let imageX = (this.componentWidth - showWidth) / 2;
   let imageY = (this.componentHeight - showHeight) / 2;

   // 取景框左上角坐标（基于组件坐标系）
   let frameX = (this.componentWidth - this.frameWidth) / 2;
   let frameY = (this.componentHeight - this.getFrameHeight()) / 2;

   // 图片在组件中实际显示的位置（考虑旋转后的偏移）
   let showX = 0, showY = 0;

   if (this.rotation === 0) {
     showX = imageX + this.offsetX * this.scale;
     showY = imageY + this.offsetY * this.scale;
   } else if (this.rotation === 90) {
     showX = imageX - this.offsetY * this.scale;
     showY = imageY + this.offsetX * this.scale;
   } else if (this.rotation === 180) {
     showX = imageX - this.offsetX * this.scale;
     showY = imageY - this.offsetY * this.scale;
   } else if (this.rotation === 270) {
     showX = imageX + this.offsetY * this.scale;
     showY = imageY - this.offsetX * this.scale;
   }

   // 计算裁剪区域坐标（基于旋转后图像的像素坐标）
   let x = 0, y = 0, cropWidth = 0, cropHeight = 0;
   if (this.rotation === 0 || this.rotation === 180) {
     // 0° 和 180°：宽高不变，使用 totalScale
     x = (frameX - showX) / totalScale;
     y = (frameY - showY) / totalScale;
     cropWidth = this.frameWidth / totalScale;
     cropHeight = this.getFrameHeight() / totalScale;
   } else if (this.rotation === 90 || this.rotation === 270) {
     // 90° 和 270°：宽高交换，使用 totalRotateScale（即 totalScale）
     x = (frameX - showX) / totalRotateScale;
     y = (frameY - showY) / totalRotateScale;
     cropWidth = this.frameWidth / totalRotateScale;
     cropHeight = this.getFrameHeight() / totalRotateScale;
   }

   // 确保裁剪区域不超出图像边界
   x = Math.max(0, Math.min(x, originalWidth - cropWidth));
   y = Math.max(0, Math.min(y, originalHeight - cropHeight));
   cropWidth = Math.min(cropWidth, originalWidth);
   cropHeight = Math.min(cropHeight, originalHeight);

   // 裁剪图像（基于旋转后图像的像素坐标）
   let region: image.Region = {
     x: x,
     y: y,
     size: {
       width: cropWidth,
       height: cropHeight
     }
   };
   pm.cropSync(region);
   return pm;
   };
   ```

完整示例参考如下：

```ts
import { image } from '@kit.ImageKit';
import fs from '@ohos.file.fs';

interface ImageLoadedEvent {
  width: number;
  height: number;
  componentWidth: number;
  componentHeight: number;
  loadingStatus: number;
  contentWidth: number;
  contentHeight: number;
  contentOffsetX: number;
  contentOffsetY: number;
}

export interface ImageLoadEventListener {

  onImageLoaded(msg: ImageLoadedEvent): void;

  onImageLoadError(error: ImageError): void;
}

export class CropModel {
  /**
   * 图片uri
   * 目前支持string，其他形式需要先转换成路径
   */
  src: string = '';
  /**
   * 图片预览
   */
  previewSource: string | Resource = '';
  /**
   * 是否可以拖动
   */
  panEnabled: boolean = true;
  /**
   * 是否可以缩放
   */
  zoomEnabled: boolean = true;
  /**
   * 取景框宽度
   */
  frameWidth = 600;
  frameHeight = 600;
  /**
   * 取景框宽高比
   */
  frameRatio = 1;
  /**
   * 遮罩颜色
   */
  maskColor: string = '#AA000000';
  /**
   * 取景框边框颜色
   */
  strokeColor: string = '#FFFFFF';
  /**
   * 图片加载监听
   */
  imageLoadEventListener: ImageLoadEventListener | null = null;
  /// 以下变量不要手动赋值 ///
  /**
   * 图片宽度，加载完成之后才会赋值
   */
  imageWidth: number = 0;
  /**
   * 图片高度，加载完成之后才会赋值
   */
  imageHeight: number = 0;
  /**
   * 控件宽度
   */
  componentWidth: number = 0;
  /**
   * 控件高度
   */
  componentHeight: number = 0;
  /**
   * 手势缩放比例
   * 图片经过了两重缩放，一是适配控件的时候进行了缩放，二是手势操作的时候进行了缩放
   */
  scale: number = 1;
  rotation: number = 0;
  /**
   * x轴方向偏移量
   */
  offsetX: number = 0;
  /**
   * y轴方向偏移量
   */
  offsetY: number = 0;

  constructor() {
  }

  public setImage(src: string, previewSource?: string | Resource): CropModel {
    this.src = src;
    if (!!previewSource) {
      this.previewSource = previewSource;
    }
    return this;
  }

  public setScale(scale: number): CropModel {
    this.scale = scale;
    return this;
  }

  public isPanEnabled(): boolean {
    return this.panEnabled;
  }

  public setPanEnabled(panEnabled: boolean): CropModel {
    this.panEnabled = panEnabled;
    return this;
  }

  public setZoomEnabled(zoomEnabled: boolean): CropModel {
    this.zoomEnabled = zoomEnabled;
    return this;
  }

  public setFrameWidth(frameWidth: number): CropModel {
    this.frameWidth = frameWidth;
    return this;
  }

  public setFrameRatio(frameRatio: number): CropModel {
    this.frameRatio = frameRatio;
    return this;
  }

  public setMaskColor(color: string): CropModel {
    this.maskColor = color;
    return this;
  }

  public setStrokeColor(color: string): CropModel {
    this.strokeColor = color;
    return this;
  }

  public setImageLoadEventListener(listener: ImageLoadEventListener): CropModel {
    this.imageLoadEventListener = listener;
    return this;
  }

  public getScale(): number {
    return this.scale;
  }

  public isZoomEnabled(): boolean {
    return this.zoomEnabled;
  }

  public getImageWidth(): number {
    return this.imageWidth;
  }

  public getImageHeight(): number {
    return this.imageHeight;
  }

  public getFrameHeight() {
    return this.frameHeight;
  }

  public reset(): void {
    this.scale = 1;
    this.offsetX = 0;
    this.offsetY = 0;
  }
  public async crop(): Promise<image.PixelMap> {
    if (!this.src || this.src === '') {
      throw new Error('Please set src first');
    }
    if (this.imageWidth === 0 || this.imageHeight === 0) {
      throw new Error('The image is not loaded');
    }

    // 打开图片文件
    let file = fs.openSync(this.src, fs.OpenMode.READ_ONLY);
    let imageSource: image.ImageSource = image.createImageSource(file.fd);
    let decodingOptions: image.DecodingOptions = {
      editable: true,
      desiredPixelFormat: image.PixelMapFormat.RGBA_8888,
    };

    // 创建pixelMap
    let pm = await imageSource.createPixelMap(decodingOptions);

    // 获取原始图像尺寸
    let originalWidth = this.imageWidth;
    let originalHeight = this.imageHeight;

    // 第一步：先旋转整个图像（注意：rotateSync 会修改图像尺寸）
    if (this.rotation !== 0) {
      pm.rotateSync(this.rotation);

      // 更新图像尺寸（90度和270度旋转会交换宽高）
      if (this.rotation === 90 || this.rotation === 270) {
        let tmp_wh = originalWidth;
        originalWidth = originalHeight;
        originalHeight = tmp_wh;
      }
    }

    // 第二步：计算缩放比例与裁剪区域
    // 图片适配控件时的缩放比例
    let widthScale = this.componentWidth / this.imageWidth;
    let heightScale = this.componentHeight / this.imageHeight;
    let adaptScale = Math.min(widthScale, heightScale);

    // 总缩放比例 = 适配缩放 × 手势缩放
    let totalScale = adaptScale * this.scale;

    // 旋转 90° 或 270° 时，图像宽高交换，缩放比例应基于新方向
    let totalRotateScale = totalScale;

    // 仅在 90°/270° 时，使用 totalRotateScale 作为裁剪坐标换算比例
    if (this.rotation === 90 || this.rotation === 270) {
      totalRotateScale = totalScale;
    }

    // 计算图片在组件中的实际显示大小
    let showWidth = originalWidth * totalScale;
    let showHeight = originalHeight * totalScale;

    // 图片左上角坐标（基于组件坐标系）
    let imageX = (this.componentWidth - showWidth) / 2;
    let imageY = (this.componentHeight - showHeight) / 2;

    // 取景框左上角坐标（基于组件坐标系）
    let frameX = (this.componentWidth - this.frameWidth) / 2;
    let frameY = (this.componentHeight - this.getFrameHeight()) / 2;

    // 图片在组件中实际显示的位置（考虑旋转后的偏移）
    let showX = 0, showY = 0;

    if (this.rotation === 0) {
      showX = imageX + this.offsetX * this.scale;
      showY = imageY + this.offsetY * this.scale;
    } else if (this.rotation === 90) {
      showX = imageX - this.offsetY * this.scale;
      showY = imageY + this.offsetX * this.scale;
    } else if (this.rotation === 180) {
      showX = imageX - this.offsetX * this.scale;
      showY = imageY - this.offsetY * this.scale;
    } else if (this.rotation === 270) {
      showX = imageX + this.offsetY * this.scale;
      showY = imageY - this.offsetX * this.scale;
    }

    // 计算裁剪区域坐标（基于旋转后图像的像素坐标）
    let x = 0, y = 0, cropWidth = 0, cropHeight = 0;
    if (this.rotation === 0 || this.rotation === 180) {
      // 0° 和 180°：宽高不变，使用 totalScale
      x = (frameX - showX) / totalScale;
      y = (frameY - showY) / totalScale;
      cropWidth = this.frameWidth / totalScale;
      cropHeight = this.getFrameHeight() / totalScale;
    } else if (this.rotation === 90 || this.rotation === 270) {
      // 90° 和 270°：宽高交换，使用 totalRotateScale（即 totalScale）
      x = (frameX - showX) / totalRotateScale;
      y = (frameY - showY) / totalRotateScale;
      cropWidth = this.frameWidth / totalRotateScale;
      cropHeight = this.getFrameHeight() / totalRotateScale;
    }

    // 确保裁剪区域不超出图像边界
    x = Math.max(0, Math.min(x, originalWidth - cropWidth));
    y = Math.max(0, Math.min(y, originalHeight - cropHeight));
    cropWidth = Math.min(cropWidth, originalWidth);
    cropHeight = Math.min(cropHeight, originalHeight);

    // 裁剪图像（基于旋转后图像的像素坐标）
    let region: image.Region = {
      x: x,
      y: y,
      size: {
        width: cropWidth,
        height: cropHeight
      }
    };
    pm.cropSync(region);
    return pm;
  };
}
```

```ts
import { CropModel } from '../models/CropModel';
import Matrix4 from '@ohos.matrix4';
import { hilog } from '@kit.PerformanceAnalysisKit';
import photoAccessHelper from '@ohos.file.photoAccessHelper';

@Entry
@Component
export struct Index {
  @State pm: PixelMap | undefined = undefined;
  @State model: CropModel = new CropModel();
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  @State private matrix: object = Matrix4.identity()
    .translate({ x: 0, y: 0 })
    .rotate({ x: 0, y: 0, z: 1, angle: 0 })
    .scale({ x: this.model.scale, y: this.model.scale });
  /** 临时变量，无需手动赋值 **/
  private tempScale = 1;
  private tempRotate = 0;
  /** 临时变量，无需手动赋值 **/
  private startOffsetX: number = 0;
  /** 临时变量，无需手动赋值 **/
  private startOffsetY: number = 0;

  build() {
    Column() {
      Stack() {
        Image(this.model.src)
          .width('100%')
          .height('100%')
          .alt(this.model.previewSource)
          .objectFit(ImageFit.Contain)
          .transform(this.matrix)
          .onComplete((msg) => {
            if (msg) { // 图片加载成功
              this.model.imageWidth = msg.width;
              this.model.imageHeight = msg.height;
              this.model.componentWidth = msg.componentWidth;
              this.model.componentHeight = msg.componentHeight;
              this.checkImageAdapt();
              if (this.model.imageLoadEventListener !== null && msg.loadingStatus === 1) {
                this.model.imageLoadEventListener.onImageLoaded(msg);
              }
            }
          })
          .onError((error) => {
            if (this.model.imageLoadEventListener != null) {
              this.model.imageLoadEventListener.onImageLoadError(error);
            }
          });
        Canvas(this.context)
          .width('100%')
          .height('100%')
          .backgroundColor(Color.Transparent)
          .onReady(() => {
            if (this.context == null) {
              return;
            }
            let height = this.context.height;
            let width = this.context.width;
            this.context.fillStyle = this.model.maskColor;
            this.context.fillRect(0, 0, width, height);
            // 把中间的取景框透出来
            this.context.globalCompositeOperation = 'destination-out';
            this.context.fillStyle = 'white';
            let frameWidthInVp = this.getUIContext().px2vp(this.model.frameWidth);
            let frameHeightInVp = this.getUIContext().px2vp(this.model.getFrameHeight());
            let x = (width - this.getUIContext().px2vp(this.model.frameWidth)) / 2;
            let y = (height - this.getUIContext().px2vp(this.model.getFrameHeight())) / 2;
            this.context.fillRect(x, y, frameWidthInVp, frameHeightInVp);
            // 画出取景框边线，使边界明显一点
            this.context.globalCompositeOperation = 'source-over';
            this.context.strokeStyle = this.model.strokeColor;
            this.context.strokeRect(x, y, frameWidthInVp, frameHeightInVp);
          })
          .enabled(false);
      }
      .clip(true)
      .width('100%')
      .layoutWeight(1)
      .backgroundColor('#00000080')
      .priorityGesture(
        TapGesture({ count: 2, fingers: 1 })
          .onAction((event: GestureEvent) => {
            if (!event) {
              return;
            }
            if (this.model.zoomEnabled) {
              if (this.model.scale !== 1) {
                this.model.scale = 1;
                this.model.reset();
                this.updateMatrix();
              } else {
                this.zoomTo(2, 0);
              }
              if (this.model.rotation !== 0) {
                this.model.rotation = 0;
                this.model.reset();
                this.updateMatrix();
              }
            }
            this.checkImageAdapt();
          })
      )
      .gesture(
        GestureGroup(GestureMode.Parallel,
          // 拖动手势
          PanGesture({})
            .onActionStart(() => {
              this.startOffsetX = this.model.offsetX;
              this.startOffsetY = this.model.offsetY;
            })
            .onActionUpdate((event: GestureEvent) => {
              if (event) {
                if (this.model.panEnabled) {
                  let distanceX: number = this.startOffsetX;
                  let distanceY: number = this.startOffsetY;
                  // 根据旋转角度调整移动方向
                  const rotation = this.model.rotation;
                  if (rotation === 0) {
                    // 0度旋转：正常移动
                    distanceX += this.getUIContext().vp2px(event.offsetX) / this.model.scale;
                    distanceY += this.getUIContext().vp2px(event.offsetY) / this.model.scale;
                    this.model.offsetX = distanceX;
                    this.model.offsetY = distanceY;
                  } else if (rotation === 90) {
                    // 90度旋转：X和Y方向交换，Y方向取反
                    distanceX += this.getUIContext().vp2px(event.offsetY) / this.model.scale;
                    distanceY -= this.getUIContext().vp2px(event.offsetX) / this.model.scale;
                    this.model.offsetX = distanceX;
                    this.model.offsetY = distanceY;
                  } else if (rotation === 180) {
                    // 180度旋转：X和Y方向都取反
                    distanceX -= this.getUIContext().vp2px(event.offsetX) / this.model.scale;
                    distanceY -= this.getUIContext().vp2px(event.offsetY) / this.model.scale;
                    this.model.offsetX = distanceX;
                    this.model.offsetY = distanceY;
                  } else if (rotation === 270) {
                    // 270度旋转：X和Y方向交换，X方向取反
                    distanceX -= this.getUIContext().vp2px(event.offsetY) / this.model.scale;
                    distanceY += this.getUIContext().vp2px(event.offsetX) / this.model.scale;
                    this.model.offsetX = distanceX;
                    this.model.offsetY = distanceY;
                  }
                  this.model.offsetX = distanceX;
                  this.model.offsetY = distanceY;
                  this.updateMatrix();
                }
              }
            })
            .onActionEnd(() => {
              this.checkImageAdapt();
            }),
          // 缩放手势处理
          PinchGesture({ fingers: 2 })
            .onActionStart(() => {
              this.tempScale = this.model.scale;
            })
            .onActionUpdate((event) => {
              if (event) {
                if (!this.model.zoomEnabled) {
                  return;
                }
                this.zoomTo(this.tempScale * event.scale, this.model.rotation);
              }
            })
            .onActionEnd(() => {
              this.checkImageAdapt();
            }),
          RotationGesture({ fingers: 3 })
            .onActionStart(() => {
              this.tempRotate = this.model.rotation;
            })
            .onActionUpdate((event) => {
              if (event) {
                if (!this.model.zoomEnabled) {
                  return;
                }
                this.zoomTo(1, this.tempRotate + event.angle);
              }
            })
            .onActionEnd(() => {
              this.checkImageAdapt();
            })
        )
      );
      Column() {
        Row({ space: 20 }) {
          Button('选择相册图片').onClick(async () => {
            let photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
            photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
            photoSelectOptions.maxSelectNumber = 1;
            let photoPicker = new photoAccessHelper.PhotoViewPicker();
            let photoSelectResult = await photoPicker.select(photoSelectOptions);
            let selectedUri = photoSelectResult.photoUris[0];
            this.model.setImage(selectedUri)
              .setFrameWidth(1000)
              .setFrameRatio(1);
          })
          Button('旋转')
            .onClick(() => {
              this.rotateImage(90);
            })
          Button('裁剪预览').onClick(async () => {
            this.pm = await this.model.crop();
          })
        }
        .width('100%')
        .height(50)

        Image(this.pm)
          .width('300lpx')
          .height('300lpx')

      }
      .width('100%')
      .height('30%')
    }
    .height('100%')
    .width('100%')
  }

  /**
   * 检查手势操作后，图片是否填满取景框，没填满则进行调整
   */
  private checkImageAdapt() {
    let offsetX = this.model.offsetX;
    let offsetY = this.model.offsetY;
    let scale = this.model.scale;
    hilog.info(0, 'CropPage', `offsetX: ${offsetX}, offsetY: ${offsetY}, scale: ${scale}`);

    // 图片适配控件的时候也进行了缩放，计算出这个缩放比例
    let widthScale = this.model.componentWidth / this.model.imageWidth;
    let heightScale = this.model.componentHeight / this.model.imageHeight;
    let adaptScale = Math.min(widthScale, heightScale);
    hilog.info(0, 'CropPage',
      `Image scale ${adaptScale} while attaching the component[${this.model.componentWidth}, ${this.model.componentHeight}]`);

    // 经过两次缩放(适配控件、手势)后，图片的实际显示大小
    let showWidth = this.model.imageWidth * adaptScale * this.model.scale;
    let showHeight = this.model.imageHeight * adaptScale * this.model.scale;

    if (this.model.rotation === 0) {
      showWidth = this.model.imageWidth * adaptScale * this.model.scale;
      showHeight = this.model.imageHeight * adaptScale * this.model.scale;
    } else if (this.model.rotation === 90) {
      showWidth = this.model.imageHeight * adaptScale * this.model.scale;
      showHeight = this.model.imageWidth * adaptScale * this.model.scale;
    } else if (this.model.rotation === 180) {
      showWidth = this.model.imageWidth * adaptScale * this.model.scale;
      showHeight = this.model.imageHeight * adaptScale * this.model.scale;
    } else if (this.model.rotation === 270) {
      showWidth = this.model.imageHeight * adaptScale * this.model.scale;
      showHeight = this.model.imageWidth * adaptScale * this.model.scale;
    }
    let imageX = (this.model.componentWidth - showWidth) / 2;
    let imageY = (this.model.componentHeight - showHeight) / 2;
    hilog.info(0, 'CropPage', `Image left top is (${imageX}, ${imageY})`);

    // 取景框的左上角坐标
    let frameX = (this.model.componentWidth - this.model.frameWidth) / 2;
    let frameY = (this.model.componentHeight - this.model.getFrameHeight()) / 2;
    hilog.info(0, 'CropPage', `Frame left top is (${frameX}, ${frameY})`);

    // 图片左上角坐标
    let showX = imageX + offsetX * scale;
    let showY = imageY + offsetY * scale;
    hilog.info(0, 'CropPage', `Image show at (${showX}, ${showY})`);

    if (this.model.rotation === 0) {
      showX = imageX + offsetX * scale;
      showY = imageY + offsetY * scale;
    } else if (this.model.rotation === 90) {
      showX = imageX - offsetY * scale;
      showY = imageY + offsetX * scale;
    } else if (this.model.rotation === 180) {
      showX = imageX - offsetX * scale;
      showY = imageY - offsetY * scale;
    } else if (this.model.rotation === 270) {
      showX = imageX + offsetY * scale;
      showY = imageY - offsetX * scale;
    }

    // 图片缩放后，大小不足以填满取景框
    if (this.model.frameWidth > showWidth || this.model.getFrameHeight() > showHeight) {
      let xScale = this.model.frameWidth / showWidth;
      let yScale = this.model.getFrameHeight() / showHeight;
      let newScale = Math.max(xScale, yScale);
      this.model.scale = this.model.scale * newScale;
      showX *= newScale;
      showY *= newScale;
    }

    // 调整x轴方向位置，使图像填满取景框
    if (showX > frameX) {
      showX = frameX;
    } else if (showX + showWidth < frameX + this.model.frameWidth) {
      showX = frameX + this.model.frameWidth - showWidth;
    }
    // 调整y轴方向位置，使图像填满取景框
    if (showY > frameY) {
      showY = frameY;
    } else if (showY + showHeight < frameY + this.model.getFrameHeight()) {
      showY = frameY + this.model.getFrameHeight() - showHeight;
    }
    this.model.offsetX = (showX - imageX) / scale;
    this.model.offsetY = (showY - imageY) / scale;

    if (this.model.rotation === 0) {
      this.model.offsetX = (showX - imageX) / scale;
      this.model.offsetY = (showY - imageY) / scale;
    } else if (this.model.rotation === 90) {
      this.model.offsetX = (showY - imageY) / scale;
      this.model.offsetY = -(showX - imageX) / scale;
    } else if (this.model.rotation === 180) {
      this.model.offsetX = -(showX - imageX) / scale;
      this.model.offsetY = -(showY - imageY) / scale;
    } else if (this.model.rotation === 270) {
      this.model.offsetX = -(showY - imageY) / scale;
      this.model.offsetY = (showX - imageX) / scale;
    }
    this.updateMatrix();
  }

  public updateMatrix(): void {
    this.matrix = Matrix4.identity()
      .translate({ x: this.model.offsetX, y: this.model.offsetY })
      .rotate({ z: 1, angle: this.model.rotation })
      .scale({ x: this.model.scale, y: this.model.scale });
  }

  public zoomTo(scale: number, rotate: number): void {
    this.model.scale = scale;
    this.model.rotation = rotate;
    this.updateMatrix();
  }

  //旋转图片方法
  public rotateImage(degrees: number): void {
    this.model.rotation += degrees;
    if (this.model.rotation >= 360) {
      this.model.rotation = 0;
    }
    this.updateMatrix();
    this.checkImageAdapt();
  }
}
```

## 总结

将裁剪组件裁剪后的图片转换为PixelMap对象并存储在一个局部变量中，用户可自定义使用该PixelMap图片数据对象。
