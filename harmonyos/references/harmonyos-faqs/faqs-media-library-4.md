---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-library-4
title: 关于导入图片的使用权限和问题
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 媒体文件管理（Media Library） > 关于导入图片的使用权限和问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:31+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:db47b0c33aa28d801efee3e0d61070fc6d1c79f1bf5f6845b84f63d6bca9520e
---

**问题描述**

需要导入图片并获取图片地址，然后传递到底层C++代码。经过测试发现，导入后读取图片时失败。

**问题定位**

当前手机不支持在C++层直接打开公共路径。仅支持在TS侧打开后，将文件描述符（fd）传递到C侧，然后使用dopen进行打开。

**参考代码**

将公共路径下的文件保存至沙箱路径，并将文件描述符（fd）传入C侧。C侧通过fd操作文件。

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

let context = AppStorage.get("context") as UIContext;
let filesDir = context.getHostContext()?.filesDir;
async function savePictureToContext() {
  const photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
  photoSelectOptions.MIMEType =
    photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE; // Filter and select media file type as IMAGE
  photoSelectOptions.maxSelectNumber = 5; // Select the maximum number of media files
  let uris: Array<string> = [];
  const photoViewPicker = new photoAccessHelper.PhotoViewPicker();
  let photoSelectResult = await photoViewPicker.select(photoSelectOptions);
  uris = photoSelectResult.photoUris;
  let uri: string = uris[0];
  let file = fileIo.openSync(uri, fileIo.OpenMode.READ_ONLY);
  console.info('file fd: ' + file.fd);
  let fd = file.fd;
  fileIo.copyFileSync(fd, filesDir + '/test2.jpg')
  let file2 = fileIo.openSync(filesDir + '/test2.jpg', fileIo.OpenMode.READ_ONLY);
  let file3 = fileIo.openSync(filesDir + '/test3.jpg', fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
  // After passing fd in, the C end can call it
  // ReadFile(file2.fd,file3.fd)
}
```
