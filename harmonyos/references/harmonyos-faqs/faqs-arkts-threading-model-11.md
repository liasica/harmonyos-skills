---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-threading-model-11
title: 如何使用TaskGroup快速实现图片灰度化
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > ArkTS线程模型和并发 > 如何使用TaskGroup快速实现图片灰度化
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:54+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9e0cea91cea69a8ba5370bf812c609d9c81c29aa5e9bbd628117b36dcd464088
---

## 问题现象

在处理像素比较大的图片时，放在单个线程中耗时也很长。如何使用TaskGroup实现分片处理图片？比如图片灰度化。

## 背景知识

* [TaskGroup](../harmonyos-references/js-apis-taskpool.md#taskgroup10)表示任务组，一次执行一组任务，适用于执行一组有关联的任务。如果所有任务正常执行，异步执行完毕后返回所有任务结果的数组，数组中元素的顺序与[addTask](../harmonyos-references/js-apis-taskpool.md#addtask10-1)的顺序相同；如果任意任务失败，则会抛出对应异常。如果任务组中存在多个任务失败的情况，则会抛出第一个失败任务的异常。任务组可以多次执行，但执行后不能新增任务。
* 灰度化是将彩色图像转换为灰度图像的处理过程，其核心原理是通过统一像素点的R、G、B分量值实现色彩空间转换。在该转换过程中，就是将彩色图像转换为每个像素点R、G、B分量值相等的灰度图像。

## 解决方案

将图片的像素数据分片，通过TaskGroup一次执行一组图片灰度化的任务，实现并行处理，达到快速灰度化，具体步骤如下：

1. 读取图片像素数据，分割为四份，添加到TaskGroup中。等待返回数据，并且把数据合并，重新编码为图片，代码示例如下：

   ```ts
   pixelMapGrayScale(pixelMap: PixelMap) {
     // 读取pixelMap的像素数据。
     let width = pixelMap.getImageInfoSync().size.width;
     let height = pixelMap.getImageInfoSync().size.height;
     let readBuffer: ArrayBuffer = new ArrayBuffer(width * height * 4);
     pixelMap.readPixelsToBufferSync(readBuffer);
     // 分成四段并发调度。
     let number: number = 4 * Math.ceil(width * height / 4);
     let buffer1: ArrayBuffer = readBuffer.slice(0, number);
     let buffer2: ArrayBuffer = readBuffer.slice(number, number * 2);
     let buffer3: ArrayBuffer = readBuffer.slice(number * 2, number * 3);
     let buffer4: ArrayBuffer = readBuffer.slice(number * 3);

     let group: taskpool.TaskGroup = new taskpool.TaskGroup();
     group.addTask(imageProcessing, buffer1);
     group.addTask(imageProcessing, buffer2);
     group.addTask(imageProcessing, buffer3);
     group.addTask(imageProcessing, buffer4);

     taskpool.execute(group, taskpool.Priority.HIGH).then((res: Array<Object>) => {
       // 结果数组汇总处理，重新编码为图片。
       console.info('execute res success', res.length);
       let byteBufferTemp: Uint8Array = new Uint8Array(new ArrayBuffer(width * height * 4));
       let offset: number = 0;
       for (let index = 0; index < res.length; index++) {
         const element = res[index] as Uint8Array;
         byteBufferTemp.set(element, offset);
         offset += element.length;
       }
       let color: ArrayBuffer = byteBufferTemp.buffer as ArrayBuffer;
       let opts: image.InitializationOptions =
         {
           editable: true,
           pixelFormat: pixelMap.getImageInfoSync().pixelFormat,
           size: { height: height, width: width }
         };
       this.pixelMapTemp = image.createPixelMapSync(color, opts);
       console.info('execute group success');
     });
   }
   ```
2. 开启图片处理线程，将像素做灰度化，代码示例如下：

   ```ts
   function imageProcessing(dataSlice: ArrayBuffer): Uint8Array {
     // 图像灰度化处理操作
     let byteBuffer: Uint32Array = new Uint32Array(dataSlice);
     let byteBufferTemp: Uint8Array = new Uint8Array(new ArrayBuffer(byteBuffer.length * 4));
     for (let index = 0; index < byteBuffer.length; index++) {
       // 通过移位方式获取RGBA各通道的值。
       let rgb = byteBuffer[index];
       let red = (rgb >> 0) & 0x000000ff;
       let green = (rgb >> 8) & 0x000000ff;
       let blue = (rgb >> 16) & 0x000000ff;
       let alpha = (rgb >> 24) & 0x000000ff;
       // 加权平均算法，获取灰度值。
       let gray = (0.299 * red + 0.587 * green + 0.114 * blue);
       byteBufferTemp[index * 4] = gray;
       byteBufferTemp[index * 4 + 1] = gray;
       byteBufferTemp[index * 4 + 2] = gray;
       byteBufferTemp[index * 4 + 3] = alpha;
     }
     return byteBufferTemp;
   }
   ```

完整示例参考如下：

```ts
import { taskpool } from '@kit.ArkTS';
import { image } from '@kit.ImageKit';
import { common } from '@kit.AbilityKit';

@Concurrent
function imageProcessing(dataSlice: ArrayBuffer): Uint8Array {
  // 图像灰度化处理操作
  let byteBuffer: Uint32Array = new Uint32Array(dataSlice);
  let byteBufferTemp: Uint8Array = new Uint8Array(new ArrayBuffer(byteBuffer.length * 4));
  for (let index = 0; index < byteBuffer.length; index++) {
    // 通过移位方式获取RGBA各通道的值。
    let rgb = byteBuffer[index];
    let red = (rgb >> 0) & 0x000000ff;
    let green = (rgb >> 8) & 0x000000ff;
    let blue = (rgb >> 16) & 0x000000ff;
    let alpha = (rgb >> 24) & 0x000000ff;
    // 加权平均算法，获取灰度值。
    let gray = (0.299 * red + 0.587 * green + 0.114 * blue);
    byteBufferTemp[index * 4] = gray;
    byteBufferTemp[index * 4 + 1] = gray;
    byteBufferTemp[index * 4 + 2] = gray;
    byteBufferTemp[index * 4 + 3] = alpha;
  }
  return byteBufferTemp;
}

@Entry
@Component
struct Index {
  @State pixelMap: image.PixelMap | undefined = undefined;
  @State pixelMapTemp: image.PixelMap | undefined = undefined;

  // 通过rawfile目录下的文件名称创建pixelMap。
  createPixelMapFromFile(url: string) {
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    const fileData: Uint8Array = context.resourceManager.getRawFileContentSync(url);
    // 创建一个可供编辑的图片。
    const buffer = fileData.buffer.slice(fileData.byteOffset, fileData.byteLength + fileData.byteOffset);
    let imageSource = image.createImageSource(buffer);
    const options: image.DecodingOptions = {
      editable: true,
      desiredPixelFormat: image.PixelMapFormat.RGBA_8888,
    };
    let pixelMap: PixelMap = imageSource.createPixelMapSync(options);
    // 资源释放
    imageSource.release();
    return pixelMap;
  }

  pixelMapGrayScale(pixelMap: PixelMap) {
    // 读取pixelMap的像素数据。
    let width = pixelMap.getImageInfoSync().size.width;
    let height = pixelMap.getImageInfoSync().size.height;
    let readBuffer: ArrayBuffer = new ArrayBuffer(width * height * 4);
    pixelMap.readPixelsToBufferSync(readBuffer);
    // 分成四段并发调度。
    let number: number = 4 * Math.ceil(width * height / 4);
    let buffer1: ArrayBuffer = readBuffer.slice(0, number);
    let buffer2: ArrayBuffer = readBuffer.slice(number, number * 2);
    let buffer3: ArrayBuffer = readBuffer.slice(number * 2, number * 3);
    let buffer4: ArrayBuffer = readBuffer.slice(number * 3);

    let group: taskpool.TaskGroup = new taskpool.TaskGroup();
    group.addTask(imageProcessing, buffer1);
    group.addTask(imageProcessing, buffer2);
    group.addTask(imageProcessing, buffer3);
    group.addTask(imageProcessing, buffer4);

    taskpool.execute(group, taskpool.Priority.HIGH).then((res: Array<Object>) => {
      // 结果数组汇总处理，重新编码为图片。
      console.info('execute res success', res.length);
      let byteBufferTemp: Uint8Array = new Uint8Array(new ArrayBuffer(width * height * 4));
      let offset: number = 0;
      for (let index = 0; index < res.length; index++) {
        const element = res[index] as Uint8Array;
        byteBufferTemp.set(element, offset);
        offset += element.length;
      }
      let color: ArrayBuffer = byteBufferTemp.buffer as ArrayBuffer;
      let opts: image.InitializationOptions =
        {
          editable: true,
          pixelFormat: pixelMap.getImageInfoSync().pixelFormat,
          size: { height: height, width: width }
        };
      this.pixelMapTemp = image.createPixelMapSync(color, opts);
      console.info('execute group success');
    });
  }

  aboutToAppear(): void {
    // 通过rawfile目录下的文件名称创建pixelMap，‘testicon.png’是测试图片，开发者需要在rawfile目录替换实际图片
    this.pixelMap = this.createPixelMapFromFile('testicon.png');
  }

  build() {
    Row() {
      Column() {
        Text('原图')
        Image(this.pixelMap)
          .objectFit(ImageFit.Contain)
          .width('30%')
          .height(120)
          .margin({
            top: 3,
            bottom: 3,
            left: 5,
            right: 5
          })
        Text('灰度图')
        Image(this.pixelMapTemp)
          .objectFit(ImageFit.Contain)
          .width('30%')
          .height(120)
          .margin({
            top: 3,
            bottom: 3,
            left: 5,
            right: 5
          })
        Button('加权平均值')
          .backgroundColor('#0D9FFB')
          .margin({
            top: 10,
            bottom: 10,
            left: 5,
            right: 5
          })
          .onClick(() => {
            this.pixelMapGrayScale(this.pixelMap as image.PixelMap);
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

## 常见FAQ

Q：在子线程进行蓝牙通信，需要一直发送，选用哪种线程类型，TaskGroup是否可以？

A：需要常驻的耗时任务建议使用[Worker](../harmonyos-references/js-apis-worker.md)线程。TaskGroup适用于执行一组有关联的耗时较短的任务。

Q：在调用addTask时一直报错：executed taskGroup cannot addTask。原因是什么？

A：在execute之后调用addTask就会产生这样的报错。TaskGroup是一次执行一组任务，适用于执行一组有关联的任务，不要在execute之后调用addTask。

Q：单个TaskGroup中的多个task任务是无序的吗？多个TaskGroup并发的时候是无序的？

A：单个TaskGroup中的多个task任务是无序的，但是返回的结果是按照addTask的顺序返回。多个TaskGroup并发的时候是无序。
