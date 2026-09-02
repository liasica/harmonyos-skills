---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-file-upload
title: 使用Web组件上传文件
breadcrumb: 指南 > 应用框架 > ArkWeb（方舟Web） > 管理网页文件上传与下载 > 使用Web组件上传文件
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:23+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:eed9b4f4396f8460d80c86b4ec3583a3e887456502c3789c62106c8b09fb0aa6
---

Web组件支持前端页面选择文件上传功能，应用开发者可以使用[onShowFileSelector()](../harmonyos-references/arkts-basic-components-web-events.md#onshowfileselector9)接口来处理前端页面文件上传的请求，如果应用开发者不做任何处理，ArkWeb会提供默认行为来处理前端页面文件上传的请求。应用开发者也可以通过获取到的前端数据，自定义拉起Picker。

## 使用onShowFileSelector拉起文件管理器

下面的示例中，当用户在前端页面点击文件上传按钮，应用侧在[onShowFileSelector()](../harmonyos-references/arkts-basic-components-web-events.md#onshowfileselector9)接口中收到文件上传请求，在此接口中开发者将上传的本地文件路径设置给前端页面。

* 应用侧代码。

```typescript
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { picker } from '@kit.CoreFileKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: $rawfile('local.html'), controller: this.controller })
        .onShowFileSelector((event) => {
          console.info('MyFileUploader onShowFileSelector invoked');
          const documentSelectOptions = new picker.DocumentSelectOptions();
          let uri: string | null = null;
          const documentViewPicker = new picker.DocumentViewPicker();
          documentViewPicker.select(documentSelectOptions).then((documentSelectResult) => {
            uri = documentSelectResult[0];
            console.info('documentViewPicker.select to file succeed and uri is:' + uri);
            if (event) {
              event.result.handleFileList([uri]);
            }
          }).catch((err: BusinessError) => {
            console.error(`Invoke documentViewPicker.select failed, code is ${err.code}, message is ${err.message}`);
          })
          return true;
        })
    }
  }
}
```

* local.html页面代码。

  ```html
  <!DOCTYPE html>
  <html>
  <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width" />
      <title>Document</title>
  </head>

  <body>
  <!-- 点击上传文件按钮 -->
  <input type="file"><br>
  </body>
  </html>
  ```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/zrVfz-YLRXWPOuldqN_2vg/zh-cn_image_0000002736433229.gif)

## 使用onShowFileSelector拉起图库

下面的示例中，当用户在前端页面点击文件上传按钮，应用侧在[onShowFileSelector()](../harmonyos-references/arkts-basic-components-web-events.md#onshowfileselector9)接口中收到文件上传请求，在此接口中开发者将上传的本地图片路径设置给前端页面。

* 应用侧代码。

  ```ts
  // xxx.ets
  import { webview } from '@kit.ArkWeb';
  import { photoAccessHelper } from '@kit.MediaLibraryKit';

  @Entry
  @Component
  struct WebComponent {
    controller: webview.WebviewController = new webview.WebviewController();

    async selectFile(result: FileSelectorResult): Promise<void> {
      let photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
      let photoPicker = new photoAccessHelper.PhotoViewPicker();
      // 过滤选择媒体文件类型为IMAGE_VIDEO
      photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_VIDEO_TYPE;
      // 设置最大选择数量
      photoSelectOptions.maxSelectNumber = 5;
      let chooseFile: photoAccessHelper.PhotoSelectResult = await photoPicker.select(photoSelectOptions);
      // 获取选择的文件列表
      result.handleFileList(chooseFile.photoUris);
    }

    build() {
      Column() {
        Web({ src: $rawfile('local.html'), controller: this.controller })
          .onShowFileSelector((event) => {
            if (event) {
              this.selectFile(event.result);
            }
            return true;
          })
      }
    }
  }
  ```
* local.html页面代码。

  ```html
  <!DOCTYPE html>
  <html>
  <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width" />
      <title>Document</title>
  </head>

  <body>
  <!-- 点击上传文件按钮 -->
  <input type="file"><br>
  </body>
  </html>
  ```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/RlfV_mp9RLOUnS1qmQfcPw/zh-cn_image_0000002706834074.gif)

## 使用onShowFileSelector拉起相机

Web组件支持前端页面上传图片文件时调用相机即时拍照，应用开发者可以使用[onShowFileSelector()](../harmonyos-references/arkts-basic-components-web-events.md#onshowfileselector9)接口来处理前端页面文件上传的请求并自行拉起相机，如果应用开发者不做任何处理，ArkWeb会提供默认行为来处理前端页面调用相机的请求。

此示例中，应用侧通过监听[onShowFileSelector](../harmonyos-references/arkts-basic-components-web-events.md#onshowfileselector9)事件并返回true拦截ArkWeb默认弹窗，并调用系统CameraPicker拉起相机。应用可以通过获取AcceptType对不同类型的目标文件做更精细的筛选。

```ts
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { camera, cameraPicker } from '@kit.CameraKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

async function openCamera(callback: Callback<string>, uiContext: UIContext) {
  let mContext = uiContext.getHostContext() as common.Context;
  try {
    let pickerProfile: cameraPicker.PickerProfile = {
      cameraPosition: camera.CameraPosition.CAMERA_POSITION_BACK
    };
    let pickerResult: cameraPicker.PickerResult = await cameraPicker.pick(mContext,
      [cameraPicker.PickerMediaType.PHOTO, cameraPicker.PickerMediaType.VIDEO], pickerProfile);
    callback(pickerResult.resultUri);
  } catch (error) {
    let err = error as BusinessError;
    console.error(`the pick call failed. error code: ${err.code}`);
  }
}

@Entry
@Component
struct Index {
  webviewController: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: $rawfile("webCamera.html"), controller: this.webviewController })
        .onShowFileSelector((event) => {
            //开发者可以通过event.fileSelector.getAcceptType()和event.fileSelector.isCapture()判断文件类型，并有选择地做出筛选以拉起不同的文件选择器
            openCamera((result) => {
                if (event) {
                console.info('Title is ' + event.fileSelector.getTitle());
                console.info('Mode is ' + event.fileSelector.getMode());
                console.info('Accept types are ' + event.fileSelector.getAcceptType());
                console.info('Capture is ' + event.fileSelector.isCapture());
                event.result.handleFileList([result]);
                }
            }, this.getUIContext())
            return true;
        })
    }
    .height('100%')
    .width('100%')
  }
}
```

HTML页面代码

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WebCamera</title>
</head>
<body>
    <input type="file" name="photo" id="photo"><br>
    <img style="display: none;width:200px;" id="img">
    <script>
        let photo = document.getElementById("photo");
        photo.addEventListener("change", preViewImg)

        function preViewImg(event) {
            let fileReader = new FileReader();
            let img = document.getElementById("img");
            fileReader.addEventListener(
                "load",
                () => {
                    // 将图像文件转换为 Base64 字符串
                    img.src = fileReader.result;
                    img.style.display = "block";
                },
                false
            );
            if (event.target.files && event.target.files[0]) {
              fileReader.readAsDataURL(event.target.files[0]);
            } else {
              console.error("File not exist.");
            }
        }
    </script>
</body>
</html>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/vHttoJmuQfygsc-M4G0DCg/zh-cn_image_0000002736313183.gif)

## 使用ArkWeb默认的方式处理文件上传请求

accept属性是一个字符串，它定义了文件input应该接受的文件类型。这个字符串是一个以逗号为分隔的唯一文件类型说明符列表。由于给定的文件类型可以用多种方式指定，因此当你需要给定格式的文件时，提供一组完整的类型指定符是非常有用的。

capture属性是一个字符串，如果accept属性指出了input是图片或者视频类型，则它指定了使用哪个摄像头去获取这些数据。值user表示应该使用前置摄像头和（或）麦克风。值environment表示应该使用后置摄像头和（或）麦克风。如果缺少此属性，则用户代理可以自由决定做什么。如果请求的前置模式不可用，则用户代理可能退回到其首选的默认模式。

当指定布尔类型属性multiple时，文件input允许用户选择多个文件。

示例页面内有数个文件选择器，分别设置了不同的accept及capture属性，这两个属性对相机的影响如下：

| accept | capture | 文件选择器行为 |
| --- | --- | --- |
| 仅包含图片类型 | 设置为"environment"或"user" | 直接拉起相机拍照模式。 |
| 仅包含图片类型 | 不设置 | 先拉起弹窗，用户选择拍照后拉起相机拍照模式。 |
| 仅包含视频类型 | 设置为"environment"或"user" | 直接拉起相机录像模式。 |
| 仅包含视频类型 | 不设置 | 先拉起弹窗，用户选择录像后拉起相机录像模式。 |
| 包含图片和视频类型 | 设置为"environment"或"user" | 直接拉起相机拍照模式，可录像。 |
| 包含图片和视频类型 | 不设置 | 先拉起弹窗，用户选择拍照后拉起相机拍照模式，可录像。 |
| 不设置图片或视频类型 | 设置为"environment"或"user" | 直接拉起相机拍照模式，可录像。 |
| 不设置图片或视频类型 | 不设置 | 先拉起弹窗，用户选择拍照后拉起相机拍照模式，可录像。 |
| 不包含图片或视频类型 | 设置为"environment"或"user" | 直接拉起文件选择，不可拉起相机。 |
| 不包含图片或视频类型 | 不设置 | 直接拉起文件选择，不可拉起相机。 |

当前ArkWeb识别的文件类型有

* 图片：tif, xbm, tiff, pjp, jfif, bmp, avif, apng, ico, webp, svg, gif, svgz, jpg, jpeg, png, pjpeg
* 视频：mp4, mpg, mpeg, m4v, ogm, ogv, webm

**说明** 

ArkWeb默认仅拉起相机后置摄像头，值'user'不会被处理成拉起前置摄像头。如有需要，请在应用侧通过[onShowFileSelector()](../harmonyos-references/arkts-basic-components-web-events.md#onshowfileselector9)接口另行处理。

HTML页面代码

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WebCamera</title>
</head>
<body>
    <input type="file" name="picture" id="picture" accept="image/*"><br>
    <img style="display: none;width:200px" id="img">
    <script>
        let picture = document.getElementById("picture");
        picture.addEventListener("change", preViewImg)

        function preViewImg(event) {
            let fileReader = new FileReader();
            let img = document.getElementById("img");
            fileReader.addEventListener(
                "load",
                () => {
                    // 将图像文件转换为 Base64 字符串
                    img.src = fileReader.result;
                    img.style.display = "block";
                },
                false
            );
            if (event.target.files && event.target.files[0]) {
              fileReader.readAsDataURL(event.target.files[0]);
            } else {
              console.error("File not exist.");
            }
        }
    </script>
</body>
</html>
```

应用侧代码

```ts
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct Index {
  webviewController: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: $rawfile("webCamera.html"), controller: this.webviewController })
    }
    .height('100%')
    .width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/Z5tVKu-ATceKOGpXLiztMg/zh-cn_image_0000002706674140.gif)

## 自定义处理JS接口拉起的文件请求

从API version 23开始，在OnShowFileSelectorEvent的FileSelectorParam中新增接口getSuggestedName()、getDefaultPath()、getDescriptions()、isAcceptAllOptionExcluded()。

新增接口对上传保存文件能力进行了增强，以对标W3C能力，用于支持用户获取到HTML前端通过showSaveFilePicker、showOpenFilePicker、showDirectoryPicker等方法传递的option参数（参考下方加载的html文件）里的数据。

API version 23 新增支持如下option中的成员：

suggestedName对应接口[getSuggestedName](../harmonyos-references/arkts-basic-components-web-fileselectorparam.md#getsuggestedname23)。

description对应接口[getDescriptions](../harmonyos-references/arkts-basic-components-web-fileselectorparam.md#getdescriptions23)。

excludeAcceptAllOption对应接口[isAcceptAllOptionExcluded](../harmonyos-references/arkts-basic-components-web-fileselectorparam.md#isacceptalloptionexcluded23)。

startIn对应接口[getDefaultPath](../harmonyos-references/arkts-basic-components-web-fileselectorparam.md#getdefaultpath23)。

types对应接口[getAcceptableFileTypes](../harmonyos-references/arkts-basic-components-web-fileselectorparam.md#getacceptablefiletypes23)。

index.html代码。

```html
<!DOCTYPE html>
<html>
<head>
    <title>文件保存测试</title>
</head>
<body>
<button onclick="saveFile()">保存文件</button>
<div id="result"></div>

<script>
    async function saveFile() {
        const options = {
            startIn: 'documents',
            suggestedName: 'example.txt',
            types: [
                {
                    description: '文本文件',
                    accept: {'text/plain': ['.txt','.text','.doc','.docx'],
                             'video/mp4': ['.mp4','.avi','.av1','.vp9']}
                },
                {
                    description: '视频',
                    accept: {'video/mp4': ['.mp4','.avi','.av1','.vp9']}
                }
            ],
            excludeAcceptAllOption: true
        };

        try {
            const fileHandle = await window.showSaveFilePicker(options);
        } catch (error) {
            if (error.name !== 'AbortError') {
                document.getElementById('result').innerHTML =
                    `错误: ${error.message}`;
            }
        }
    }
</script>
</body>
</html>
```

应用侧代码。

```ts
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { picker } from '@kit.CoreFileKit';
let defaultPublicPath = 'storage/Users/currentUser/';
let defaultBasePath = 'file://docs/';
let wellKnownDirectoryMap = new Map<string, string>([
    ['desktop', defaultPublicPath + 'desktop'],
    ['documents', defaultPublicPath + 'documents'],
    ['downloads', defaultPublicPath + 'download'],
    ['music', defaultPublicPath + 'music'],
    ['pictures', defaultPublicPath + 'images'],
    ['videos', defaultPublicPath + 'videos'],
]);

function getUri(path : string) {
  let publicDir = wellKnownDirectoryMap.get(path);
  if (publicDir !== undefined) {
    path = publicDir;
  }
  return defaultBasePath + path;
}

function getFileName(name : string) {
  let fileName = name;
  let lastDotIndex = name.lastIndexOf('.');
  if (lastDotIndex !== -1) {
    fileName = name.substring(0, lastDotIndex);
  }
  return fileName;
}

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .onShowFileSelector((event) => {
          console.info('onShowFileSelector Suggested Name is ' + event.fileSelector.getSuggestedName());
          console.info('onShowFileSelector Default Path is ' + event.fileSelector.getDefaultPath());
          console.info('onShowFileSelector Descriptions are ' + event.fileSelector.getDescriptions());
          console.info('onShowFileSelector AcceptAllOptionExcluded is ' + event.fileSelector.isAcceptAllOptionExcluded());
          const documentSaveOptions = new picker.DocumentSaveOptions();
          documentSaveOptions.newFileNames = new Array<string>();
          documentSaveOptions.newFileNames.push(getFileName(event.fileSelector.getSuggestedName()));
          documentSaveOptions.defaultFilePathUri = getUri(event.fileSelector.getDefaultPath());
          let accepts : Array<Array<AcceptableFileType>> = event.fileSelector.getAcceptableFileTypes();
          let descriptions : Array<string> = event.fileSelector.getDescriptions();
          documentSaveOptions.fileSuffixChoices = new Array<string>();
          let n = accepts.length;
          for (let i = 0; i < n; i++) {
            let m = accepts[i].length;
            let extList = Array<string>();
            for (let j = 0; j < m; j++) {
              extList.push(accepts[i][j].acceptableType.join(','));
            }
            let ext = extList.join(',');
            let desc = descriptions[i] + '(' + ext + ')' + '|';
            documentSaveOptions.fileSuffixChoices.push(desc + ext);
          }
          if (!event.fileSelector.isAcceptAllOptionExcluded()) {
            documentSaveOptions.fileSuffixChoices.push('所有文件(*.*)' + '|' + '*.*');
          }
          let uri: string | null = null;
          const documentViewPicker = new picker.DocumentViewPicker();
          documentViewPicker.save(documentSaveOptions).then((documentSelectResult) => {
            uri = documentSelectResult[0];
            console.info('documentViewPicker.save to file succeed and uri is:' + uri);
            if (event) {
              event.result.handleFileList([uri]);
            }
          }).catch((err: BusinessError) => {
            console.error(`Invoke documentViewPicker.save failed, code is ${err.code}, message is ${err.message}`);
          })
          return true;
        })
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/E37Fcwn6RQ-JTB_92f31hQ/zh-cn_image_0000002736433231.gif)

样例以HTML中的showSaveFilePicker()配合ArkTS中documentViewPicker.save()方法为例。

需注意：

1. HTML中的showOpenFilePicker、showDirectoryPicker方法的入参option与showSaveFilePicker的入参option的成员存在差异。
2. ETS中如调用[documentViewPicker.select()](../harmonyos-references/js-apis-file-picker.md#select)方法需配合[picker.DocumentSelectOptions](../harmonyos-references/js-apis-file-picker.md#documentselectoptions)对象为Picker传参，而非[picker.DocumentSaveOptions](../harmonyos-references/js-apis-file-picker.md#documentsaveoptions)对象，请参见[@ohos.file.picker (选择器)](../harmonyos-references/js-apis-file-picker.md)。

## 常见问题

### onShowFileSelector配合ArkWeb默认弹窗使用

用户点击文件上传按钮后，程序优先执行onShowFileSelector中的回调进行逻辑处理，应用开发者可根据处理结果选择返回false以触发ArkWeb默认弹窗，此时应避免同时触发应用侧的其他Picker；若开发者选择返回true，则拦截ArkWeb默认弹窗并仅执行自定义行为。

### 回调中getAcceptType和getMimeTypes的区别

getAcceptType返回的是accept属性值全量转换为文件扩展名所组成的字符串数组，getMimeTypes返回的是accept属性值用逗号拆分后所组成的字符串数组。

如若accept属性值为video/mp4, .png，则getAcceptType返回.mp4, .m4v; .png，getMimeTypes返回video/mp4; .png。

### ArkWeb默认弹窗的说明

选项“图片”会拉起图库，根据accept属性值不同，用户可以选择上传图片或视频；选项“拍照”会拉起相机，根据accept属性值不同，用户可以选择拍照或录像；选项“文件”会拉起文件管理器，用户可以上传任意内容。

### handleFileList的使用说明

该函数将选择的文件路径提交给ArkWeb，入参主要有两种类型：

1. file协议路径，目前只支持前缀为file://media/、file://docs/的公共路径和file://<packageName>/的应用包名路径，其他file协议路径无权限。
2. 沙箱目录，具体参考[应用沙箱目录](app-sandbox-directory.md)。
