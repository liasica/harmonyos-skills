---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-image-31
title: 图片像素错误导致显示异常
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 图片处理（Image） > 图片像素错误导致显示异常
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:42+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:8e7a8f2328f5726f0d7aa21f2c87fe9e2e5d68273a6b815de06eae0686dfbfa8
---

## 问题现象

对图片进行处理(如编解码、相机流数据处理等)，出现显示错误或花屏等现象。

## 背景知识

* 数据对齐：在计算机读取数据时存在数据对齐，计算机一般都为32位或者64位，故一般数据对齐都为4字节或8字节的整数倍。如果数据非4字节或8字节对齐，就会需要额外花销来处理，为了避免这种额外的开销，一般会使用0或者其它数据在未对齐的数据末尾进行填充对齐。
* 宽高：图像数据中有效的宽高。
* 宽高跨距：跨距（Stride），是图像存储在内存中，每一行数据所占空间的真实大小，它大于或等于通过图像分辨率宽度计算的字节长度。由于内存对齐的缘故，方便提取数据，每行数据的字节数可能要求为一个数的倍数，这时不足的字节数由padding填充。（Stride = width + padding）

在可编程位图中有两种表示方式为RGB和YUV，RGB的色彩空间以三原色来组合表示一个像素点，YUV格式色彩空间以亮度，色调，色饱和度来表示一个像素点。RGB色彩空间更适合图像采集和显示，YUV空间更适合编码和存储。在存储和编码之前，RGB图像要转换为YUV图像，而YUV图像在显示之前一般有必要转换回RGB。

## 解决方案

使用图片解析软件或手动读取图片数据分析比较。

* **场景一**：图片颜色显示不正确：

  问题现象：图像正常显示但图像中颜色显示错误。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/dQbOfdnwSRGuqkcC-xn6sg/zh-cn_image_0000002658911809.png)
  1. 在Native侧创建PixelMap传递给ArkTS的Image组件进行展示时，报出colorspace的错误，图片颜色显示错误。
  2. 在使用createPixelMap创建PixelMap发现图片变黄了。
  3. 使用readPixelsToBuffer和readPixels读取像素的排列格式不同，图片显示的颜色不同。

  效果预览如下：正常显示如图一，加载渲染显示如图二。

  图一：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/WbCpmrgUQauR9hrwcn4XZQ/zh-cn_image_0000002628392600.png "点击放大")

  图二：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/0_SxZ477TaSNCAVIcyjYZA/zh-cn_image_0000002658791867.png "点击放大")

  原因分析：颜色显示错误如RGB用BGR的像素格式去解析渲染，会导致原本R红色通道的值变为B蓝色通道的值，B蓝色通道的值变为R红色通道的值，导致最终颜色错误。

  例如原本图片的像素格式为RGB888（每个颜色通道8bit大小，一个像素3字节），其中的一个像素以16进制标识为#ff0000（红色），现在以BGR的方式去解析渲染导致该像素的红色通道和蓝色通道数值对调，变为#0000ff（蓝色）。

  解决方案：与场景二相同。
* **场景二**：图片颜色错乱，像素点明亮可见：

  问题现象：图像未正常显示，颜色错乱，像素点明亮可见。

  效果预览如下：正常显示如图三，渲染显示后如图四。

  图三：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/Sq2yllvNRrOAWHSsxGle4w/zh-cn_image_0000002628552492.png "点击放大")

  图四：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/uhlWgeVJTX6RJ0MAymuM-w/zh-cn_image_0000002658911811.png "点击放大")

  原因分析：如果图像中有多种颜色，颜色显示错误错乱，无法正常显示可见图片，并有清晰可见且规则排列的点，则需要确认色彩空间的表示是否错误。

  + 解析图片使用的色彩空间表示错误，RGB（RGBA）与YUV通道错误表示，导致颜色错误杂乱，像素点明显，假设以RGB888像素格式的图片的其中3个像素点的数据现在以YUV格式或者BGRA8888等打乱像素点数据的方式渲染解析，会导致图片无法识别，像素点错乱。
  + 使用readPixelsToBuffer是整段buffer的读取，所以是按照原PixelMap的像素格式读的；而readPixels是区域读取，读出来的固定都是BGRA\_8888格式。

  YUV色彩空间格式只有图片的数据信息，无文件头等，打开时需要指定YUV的像素排列方式和宽高。可以使用相关的图片查看软件打开并尝试RGB或YUV的色彩空间的不同样点排列格式，来确认图片正确的格式。

  解决方案：确定好相关像素格式后，可由正确的像素格式渲染图片，如创建PixelMap时初始化缓冲区中的像素格式需要由[InitializationOptions.srcPixelFormat](../harmonyos-references/arkts-apis-image-i.md#initializationoptions8)指定（默认值为BGRA\_8888）。

  获取PixelMap图片信息可通过[getImageInfo(): Promise<ImageInfo>](../harmonyos-references/arkts-apis-image-pixelmap.md#getimageinfo7)函数或者[getImageInfo(callback: AsyncCallback<ImageInfo>): void](../harmonyos-references/arkts-apis-image-pixelmap.md#getimageinfo7-1)函数来得到图像像素信息，前者以Promise形式返回获取的图像像素信息，后者以callback形式返回获取的图像像素信息。

  ```ts
  pixelMap.getImageInfo().then( (value:image.ImageInfo) => {
    this.pixelmapSize = pixelMap.getPixelBytesNumber();
    console.info(TAG + 'pixelmapBytes: '+ pixelMap.getPixelBytesNumber());
    console.info(TAG + 'width: ' + value.size.width + ' height: '+value.size.height+' stride: '+value.stride+' format: '+ value.pixelFormat+ ' MIME '+value.mimeType);
  });
  ```

  createPixelMap创建PixelMap，像素格式默认为BGRA排列，将排列RGBA改为BGRA即可，若想在读取图片数据后进行其他操作，需要在图片解析后判断下一步操作需要哪种像素排列格式，将格式转换后进行操作，最后重新创建PixelMap需要将格式更改为BGRA再用createPixelMap创建。

  ```ts
  rgbaToBgra(src: Uint8Array, dst: Uint8Array, length: number) {
    for (let i = 0; i < length; i += 4) {
      // 取出R、G、B、A四个字节
      const r = src[i];
      const g = src[i + 1];
      const b = src[i + 2];
      const a = src[i + 3];
      // 将B、G、R、A写入dst
      dst[i] = b;
      dst[i + 1] = g;
      dst[i + 2] = r;
      dst[i + 3] = a;
    }
  }
  ```

  完整示例参考如下：

  ```ts
  import { image } from '@kit.ImageKit';
  import { BusinessError } from '@kit.BasicServicesKit';

  const TAG = 'pixelTest';

  @Entry
  @Component
  struct pixelTest {
    message: string = 'pixelTest';
    @State bitmap: image.PixelMap | undefined = undefined;
    pixelmapSize: number = 0;
    // 单个像素的RGBA变换
    rgbaToBgra(src: Uint8Array, dst: Uint8Array, length: number) {
      for (let i = 0; i < length; i += 4) {
        // 取出R、G、B、A四个字节
        const r = src[i];
        const g = src[i + 1];
        const b = src[i + 2];
        const a = src[i + 3];
        // 将B、G、R、A写入dst
        dst[i] = b;
        dst[i + 1] = g;
        dst[i + 2] = r;
        dst[i + 3] = a;
      }
    }
    // pixelmap转换格式
    build() {
      Row() {
        Column() {
          Image(this.bitmap)

          Text(this.message)
            .fontSize($r('app.float.page_text_font_size'))
            .fontWeight(FontWeight.Bold)
            .onClick(async () => {
              // xxx.png替换为rawfile目录下的图像
              let imageRawFileDescriptor = await this.getUIContext().getHostContext()?.resourceManager.getRawFd('xxx.png');
              const imageSource: image.ImageSource = image.createImageSource(imageRawFileDescriptor);
              let decodeingOptions: image.DecodingOptions = {
                editable: true,
                desiredPixelFormat: image.PixelMapFormat.RGBA_8888,
              };

              await imageSource.createPixelMap(decodeingOptions).then( (pixelMap: image.PixelMap) => {
                console.info('Succeeded in creating PixelMap');
                this.bitmap = pixelMap;
                pixelMap.getImageInfo().then( (value:image.ImageInfo) => {
                  this.pixelmapSize = pixelMap.getPixelBytesNumber();
                  console.info(`${TAG} pixelmapBytes ${pixelMap.getPixelBytesNumber()}`);
                  console.info(`${TAG} width: ${value.size.width} height: ${value.size.height} stride: ${value.stride}
                  format: ${value.pixelFormat} MIME: ${value.mimeType}`);
                });

                // 改换pixelmap的format
                const readBuffer:ArrayBuffer = new ArrayBuffer(400000); // 读取的字节数需根据图片调整 如果使用pixelmapSize初始化buffer 需要确保pixelmapSize在此之前已被赋值
                if(this.bitmap !== undefined){
                  this.bitmap.readPixelsToBuffer(readBuffer, (error: BusinessError) => {
                    if (error) {
                      console.error(`Failed to read image pixel data. code is ${error.code}, message is ${error.message}`); // 不符合条件则进入。
                      return;
                    } else {
                      console.info('Succeeded in reading image pixel data.'); // 符合条件则进入。
                    }
                  });
                } else {
                  console.error('this bitmap is undefined');
                  return;
                }
                let srcUint8Array = new Uint8Array(readBuffer);
                console.info(`${TAG} srcbuffer: ${srcUint8Array}`);

                let dstUint8Array = new Uint8Array(400000); // 读取的字节数需根据图片调整
                this.rgbaToBgra(srcUint8Array, dstUint8Array, 400000); // 读取的字节数需根据图片调整
                console.info(`${TAG} dstbuffer: ${dstUint8Array}`);
              });
            })
        }
        .width('100%')
      }
      .height('100%')
    }
  }
  ```

* **场景三**：图片出现撕裂条纹：

  问题现象：图片呈明显的斜条纹撕裂：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/frw3V_MBR26PZILhcp4BJg/zh-cn_image_0000002628392604.png)

  常见跨距花屏场景：
  + 相机预览中发生跨距异常。
  + 编解码跨距异常花屏。

  原因分析：在图像渲染时，若宽高和padding被错误的对齐，会导致图片出现斜条纹：

  假设图片对齐为8，宽为6，跨距为8，填充为2，正常显示如下图：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/uwlP7bMKTMOLt_5aWKUDaA/zh-cn_image_0000002658791869.png)

  当跨距设置错误时会出现下面两种情况：

  + 当padding填充不够时（假设为1），因为对齐为8此时会读取8个像素数据，现在只有1个padding，此时就会把第二行的像素数据多读取一个如下图所示：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/cxAcroscQwKqjnJiD3-9Xw/zh-cn_image_0000002628552496.png)

  此时画面因为像素的错位显示呈现出左下往右上的撕裂斜条纹。

  + 同理此时跨距过大，即padding填充过多时（假设为3）会导致多的一个填充被下一行像素数据读取如下图所示：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/pPHrojJFRLmmhPMn8cdJTQ/zh-cn_image_0000002658911813.png)

  此时画面因为像素的错位显示呈现出左上往右下的撕裂斜条纹。

  解决方案：

  + 相机预览中发生跨距异常：[相机预览花屏解决方案](../harmonyos-guides/camera-preview-glitch-solution.md)。
  + 编解码跨距异常花屏（[编码文档](../harmonyos-guides/video-encoding.md#buffer模式)/[解码文档](../harmonyos-guides/video-decoding.md#buffer模式)拷贝YUV图像时设置跨距）。

## 常见FAQ

Q：编解码的对齐字节是多少（如何获取编码图像跨距/步长）？

A：根据不同的硬件限制，编解码器自动对齐的字节不同，可以使用[OH\_VideoEncoder\_GetInputDescription](../harmonyos-references/capi-native-avcodec-videoencoder-h.md#oh_videoencoder_getinputdescription)查询得到AVformat，再用[OH\_AVFormat\_GetIntValue](../harmonyos-references/capi-native-avformat-h.md#oh_avformat_getintvalue)获取[OH\_MD\_KEY\_VIDEO\_STRIDE](../harmonyos-references/capi-codecbase.md#视频专有的键值对)的值进行处理。详细处理方式参考视频编码文档中的[调用OH\_VideoEncoder\_PushInputBuffer写入编码图像](../harmonyos-guides/video-encoding.md#buffer模式)步骤。

Q：HarmonyOS中PixelMap支持什么像素格式？

A：PixelMap的像素格式参考[PixelMapFormat](../harmonyos-references/arkts-apis-image-e.md#pixelmapformat7)。

## 总结

渲染图片错误花屏通常由对图片数据的错误处理导致。

| 现象 | 像素错误情况 | 常见原因 | 处理方式 |
| --- | --- | --- | --- |
| 图片颜色错误 | 像素点内颜色通道错误 | 像素中颜色通道顺序错误（如图片像素以BGR的方式储存但以RGB的方式读取渲染） | 更换图片像素通道的解析顺序 |
| 图片颜色杂乱且像素点清晰可见 | 每个像素点的数据异常 | 图片色彩空间/图片像素格式错误（如RGB的色彩空间采用YUV解析/RGB类型的像素格式使用RGBA的像素解析） | 以正确的色彩空间和像素格式解析渲染图片 |
| 图片撕裂有规则的斜条纹 | 图片上像素点的个数错误 | 图片的宽高跨距处理不正确 | 确认字节对齐大小，添加或删除填充使图片跨距对齐 |
