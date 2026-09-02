---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-122
title: "解决上传文件时报错提示assertion (isArray) failed: not array的问题"
breadcrumb: "FAQ > 系统开发 > 网络 > 网络（Network） > 解决上传文件时报错提示assertion (isArray) failed: not array的问题"
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:37+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:82dc38c1a7cc119aab26a6b933be9dec0514906df236a6555cd4ce40686e478d
---

## 问题现象

用request.uploadFile报错assertion (isArray) failed: not array。报错代码如下：

```screen
uploadimgWrong() {
  let uploadConfig: request.UploadConfig = {
    // 此处修改为正确的服务器url
    url: "",
    header: { 'Content-Type': 'multipart/form-data', "Accept": "*/*" },
    method: "POST",
    files: this.fileList,
    data: [{
      name: "email",
      value: 'xxxx',
    }, {
      name: "phone",
      value: 'xxxxxxxx',
    }, {
      name: "content",
      value: '测试',
    }, {
      name: "type",
      value: '4',
    }],
  };
  try {
    request.uploadFile(this.getUIContext().getHostContext(),
      uploadConfig,
      (err: BusinessError, uploadTask: request.UploadTask) => {
        if (err) {
          return;
        }
        let upCompleteCallback = () => {
        };
        uploadTask.on('complete', upCompleteCallback);
        let upFailCallback = () => {
        };
        uploadTask.on('fail', upFailCallback);
      });
  } catch (err) {
    hilog.error(DOMAIN, 'testTag', 'Failed to uploadFile', JSON.stringify(err));
  }

}
```

## 背景知识

[request.uploadFile](../harmonyos-references/js-apis-request.md#requestuploadfile9-1)：创建并启动一个上传任务，使用callback异步回调，支持HTTP协议。通过[on('complete'|'fail')](../harmonyos-references/js-apis-request.md#oncomplete--fail9)可获取任务上传时的成功信息或错误信息。

[UploadConfig](../harmonyos-references/js-apis-request.md#uploadconfig)：上传任务的配置信息。

## 问题定位

[UploadConfig](../harmonyos-references/js-apis-request.md#uploadconfig)中的参数files用的是[File](../harmonyos-references/js-apis-request.md#file)，而问题代码中用到的file是自定义的类。所以在上传文件时报错assertion (isArray) failed: not array。

## 分析结论

在上传文件时，传入的UploadConfig要做到每个入参都能对应上。

## 修改建议

声明一个Array<request.File>，赋值后以传入到uploadConfig中。示例代码如下：

```screen
uploadimgRight() {
  let files: Array<request.File> = [];
  for (let i = 0; i < this.fileList.length; i++) {
    files.push({
      filename: this.fileList[i].filename,
      name: this.fileList[i].name,
      type: this.fileList[i].type,
      uri: this.fileList[i].uri
    });
  }
  let uploadConfig: request.UploadConfig = {
    // 此处修改为正确的服务器url
    url: "",
    header: { 'Content-Type': 'multipart/form-data', "Accept": "*/*" },
    method: "POST",
    files: files,
    data: [{
      name: "email",
      value: 'xxx',
    }, {
      name: "phone",
      value: 'xxxx',
    }, {
      name: "content",
      value: '测试',
    }, {
      name: "type",
      value: '4',
    }],
  };

  request.uploadFile(this.getUIContext().getHostContext(),
    uploadConfig,
    (err: BusinessError, uploadTask: request.UploadTask) => {
      if (err) {
        return;
      }
      let upCompleteCallback = (taskStates: Array<request.TaskState>) => {
        for (let i = 0; i < taskStates.length; i++) {
          console.info("upOnComplete taskState:" + JSON.stringify(taskStates[i]));
        }
      };
      uploadTask.on('complete', upCompleteCallback);
      let upFailCallback = () => {
      };
      uploadTask.on('fail', upFailCallback);
    });

}
```

全量代码如下：

```screen
import { BusinessError, request } from '@kit.BasicServicesKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import fs from '@ohos.file.fs';
import { image } from '@kit.ImageKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const MAX_SIZE = 800;
const DOMAIN = 0x0000;

@Entry
@ComponentV2
export struct AskQuestion {
  @Local refreshing: boolean = false;
  @Local refreshOffset: number = 0;
  @Local refreshState: RefreshStatus = RefreshStatus.Inactive;
  @Local scroller: Scroller = new Scroller();
  @Local fileList: Datafile[] = [];
  @Local data: myData = {};

  aboutToAppear() {
  }

  uploadimgRight() {
    let files: Array<request.File> = [];
    for (let i = 0; i < this.fileList.length; i++) {
      files.push({
        filename: this.fileList[i].filename,
        name: this.fileList[i].name,
        type: this.fileList[i].type,
        uri: this.fileList[i].uri
      });
    }
    let uploadConfig: request.UploadConfig = {
      // 此处修改为正确的服务器url
      url: "",
      header: { 'Content-Type': 'multipart/form-data', "Accept": "*/*" },
      method: "POST",
      files: files,
      data: [{
        name: "email",
        value: 'xxx',
      }, {
        name: "phone",
        value: 'xxxx',
      }, {
        name: "content",
        value: '测试',
      }, {
        name: "type",
        value: '4',
      }],
    };

    request.uploadFile(this.getUIContext().getHostContext(),
      uploadConfig,
      (err: BusinessError, uploadTask: request.UploadTask) => {
        if (err) {
          return;
        }
        let upCompleteCallback = (taskStates: Array<request.TaskState>) => {
          for (let i = 0; i < taskStates.length; i++) {
            console.info("upOnComplete taskState:" + JSON.stringify(taskStates[i]));
          }
        };
        uploadTask.on('complete', upCompleteCallback);
        let upFailCallback = () => {
        };
        uploadTask.on('fail', upFailCallback);
      });

  }

  uploadimgWrong() {
    let uploadConfig: request.UploadConfig = {
      // 此处修改为正确的服务器url
      url: "",
      header: { 'Content-Type': 'multipart/form-data', "Accept": "*/*" },
      method: "POST",
      files: this.fileList,
      data: [{
        name: "email",
        value: 'xxxx',
      }, {
        name: "phone",
        value: 'xxxxxxxx',
      }, {
        name: "content",
        value: '测试',
      }, {
        name: "type",
        value: '4',
      }],
    };
    try {
      request.uploadFile(this.getUIContext().getHostContext(),
        uploadConfig,
        (err: BusinessError, uploadTask: request.UploadTask) => {
          if (err) {
            return;
          }
          let upCompleteCallback = () => {
          };
          uploadTask.on('complete', upCompleteCallback);
          let upFailCallback = () => {
          };
          uploadTask.on('fail', upFailCallback);
        });
    } catch (err) {
      hilog.error(DOMAIN, 'testTag', 'Failed to uploadFile', JSON.stringify(err));
    }

  }

  build() {
    Column() {

      Column() {
        Row() {
          Text('上传图片错误').onClick(() => {
            this.uploadimgWrong();
          });
          Text('上传图片正确').onClick(() => {
            this.uploadimgRight();
          });
          Text("选择图片").onClick(() => {
            example({
              selectOptions: {
                maxSelectNumber: 5,
                selectType: "image",
              },
              onSuccess: (uris) => {
                this.fileList = uris;
              },
              onError: () => {
              },
              extraParam: '自定义参数值'
            }, this.getUIContext().getHostContext()?.cacheDir);
          });
        }.width("100%")
        .justifyContent(FlexAlign.SpaceBetween);

        List({ scroller: this.scroller }) {
          ForEach(this.fileList, (item: Datafile) => {
            ListItem() {
              Image(item.uri).width(40).height(40);
            };
          });
        }
        .layoutWeight(1);

        Image("file://" + this.getUIContext().getHostContext()?.cacheDir + "IMG_20250704_102801.jpg")
          .width(40)
          .height(40); //只有当有file的时候才能展示图片，使用internal://cache/ 无法展示
      }.padding({ left: 10, right: 10 });
    }.height("100%");

  }
}

class Datafile {
  filename: string = "";
  name: string = "";
  uri: string = "";
  type: string = "";
  url?: string = "";
}

class myData {
  email?: string = "";
  phone?: number = 0;
  content?: string = "";
  type?: number = 0;
  courseId?: number = 0;
}

export async function example(config: ExampleConfig, cacheDir?: string) {
  const photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();

  if (config.selectOptions.selectType == "image") {
    photoSelectOptions.MIMEType =
      photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
  } else if (config.selectOptions.selectType == "video") {
    photoSelectOptions.MIMEType =
      photoAccessHelper.PhotoViewMIMETypes.VIDEO_TYPE;
  } else if (config.selectOptions.selectType == "all") {
    photoSelectOptions.MIMEType =
      photoAccessHelper.PhotoViewMIMETypes.IMAGE_VIDEO_TYPE;
  }

  photoSelectOptions.maxSelectNumber =
    config.selectOptions.maxSelectNumber;

  const photoViewPicker = new photoAccessHelper.PhotoViewPicker();
  photoViewPicker.select(photoSelectOptions)
    .then(async (photoSelectResult: photoAccessHelper.PhotoSelectResult) => {
      const uris = photoSelectResult.photoUris;
      const fileList: Datafile[] = [];

      // 使用Promise.all处理多个文件
      await Promise.all(uris.map(async (item) => {

        const filename = item.split('/').pop() || "";
        const lastDotIndex = filename.lastIndexOf('.');
        const name = lastDotIndex === -1 ? filename : filename.substring(0, lastDotIndex);

        // 只对图片进行压缩处理
        if (photoSelectOptions.MIMEType === photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE ||
          photoSelectOptions.MIMEType === photoAccessHelper.PhotoViewMIMETypes.IMAGE_VIDEO_TYPE) {
          const compressedFile = await processImage(item, filename, name, cacheDir);
          fileList.push(compressedFile);
        } else {
          // 非图片文件直接复制
          try {
            const fileHandle = fs.openSync(item, fs.OpenMode.READ_ONLY);
            fs.copyFileSync(fileHandle.fd, `${cacheDir}/${filename}`);
            fs.closeSync(fileHandle);
          } catch (er) {
            hilog.error(DOMAIN, 'testTag', 'Failed to uploadFile', JSON.stringify(er));
          }

          fileList.push({
            filename: name,
            name: name,
            type: "image/jpeg",
            uri: "internal://cache/" + filename,
            url: "file://" + cacheDir + "/" + filename
          });
        }

      }));

      config.onSuccess(fileList);

    })
    .catch((err: BusinessError) => {
      config.onError(err);
    });
}

async function processImage(uri: string, filename: string, name: string, cacheDir?: string): Promise<Datafile> {
  const outputPath = `${cacheDir}/${filename}`;
  // 1. 获取原始图片信息
  const fileHandle = fs.openSync(uri, fs.OpenMode.READ_ONLY);
  const imageSource = image.createImageSource(fileHandle.fd);
  const imageInfo = await imageSource.getImageInfo();
  fs.closeSync(fileHandle);
  let width = imageInfo.size.width;
  let height = imageInfo.size.height;

  // 2. 计算缩放比例
  if (width > MAX_SIZE || height > MAX_SIZE) {
    const scaleRatio = Math.min(MAX_SIZE / width, MAX_SIZE / height);
    width = Math.floor(width * scaleRatio);
    height = Math.floor(height * scaleRatio);

    // 3. 重新打开文件进行压缩
    const fileHandleForProcess = fs.openSync(uri, fs.OpenMode.READ_ONLY);
    const imageSourceForProcess = image.createImageSource(fileHandleForProcess.fd);

    // 4. 创建压缩选项
    const decodingOptions: ESObject = {
      desiredSize: ({ width: MAX_SIZE, height: MAX_SIZE } as desiredSize),
      rotateDegrees: 0,
      editable: false,
      desiredPixelFormat: image.PixelMapFormat.RGBA_8888,
    };

    // 5. 创建像素图并压缩
    const pixelMap = await imageSourceForProcess.createPixelMap(decodingOptions);
    const imagePacker = image.createImagePacker();
    const packOptions: ESObject = {
      format: 'image/jpeg', // 可根据需要调整格式
      quality: 80, // 压缩质量 (0-100)
    };

    // 6. 保存压缩后的图片
    const arrayBuffer = await imagePacker.packToData(pixelMap, packOptions);
    const uint8Array = new Uint8Array(arrayBuffer);

    // 3. 写入文件（严格正确的写法）
    const fd = fs.openSync(outputPath, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE);
    fs.writeSync(fd.fd, uint8Array.buffer, {
      length: uint8Array.byteLength  // 必须指定长度！
    });
    fs.closeSync(fd);

    // 7. 释放资源
    pixelMap.release();
    imageSourceForProcess.release();
    fs.closeSync(fileHandleForProcess);
  } else {
    // 无需压缩，直接复制
    const fileHandle = fs.openSync(uri, fs.OpenMode.READ_ONLY);
    fs.copyFileSync(fileHandle.fd, outputPath);
    fs.closeSync(fileHandle);
  }

  return {
    filename: name,
    name: name,
    type: "image/jpeg",
    uri: "internal://cache/" + filename,
    url: "file://" + cacheDir + "/" + filename
  };

}

export interface ExampleConfig {
  selectOptions: select;
  onSuccess: SuccessCallback;
  onError: ErrorCallback;
  extraParam?: string;
}

interface select {
  maxSelectNumber: number;
  selectType: string;
}

type SuccessCallback = (uris: Datafile[]) => void;
type ErrorCallback = (error: BusinessError) => void;

// 处理图片压缩
interface desiredSize {
  width: number;
  height: number;
}
```
