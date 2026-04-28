---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-library-4
title: 关于导入图片的使用权限和问题
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 媒体文件管理（Media Library） > 关于导入图片的使用权限和问题
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:32+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:1045f91d85fac7442eab06dedb7e38069de297206e95c2ac824897f6c1050076
---

**问题描述**

需要导入图片并获取图片地址，然后传递到底层C++代码。经过测试发现，导入后读取图片时失败。

**问题定位**

当前手机不支持在C++层直接打开公共路径。仅支持在TS侧打开后，将文件描述符（fd）传递到C侧，然后使用dopen进行打开。

**参考代码**

将公共路径下的文件保存至沙箱路径，并将文件描述符（fd）传入C侧。C侧通过fd操作文件。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { fileIo } from '@kit.CoreFileKit';
3. import { common } from '@kit.AbilityKit';
4. import { photoAccessHelper } from '@kit.MediaLibraryKit';

6. let context = AppStorage.get("context") as UIContext;
7. let filesDir = context.getHostContext()?.filesDir;
8. function savePictureToContext(){
9. const photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
10. photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE; // Filter and select media file type as IMAGE
11. photoSelectOptions.maxSelectNumber = 5; // Select the maximum number of media files
12. let uris: Array<string> = [];
13. const photoViewPicker = new photoAccessHelper.PhotoViewPicker();
14. photoViewPicker.select(photoSelectOptions).then((photoSelectResult: photoAccessHelper.PhotoSelectResult) => {
15. uris = photoSelectResult.photoUris;
16. console.info('photoViewPicker.select to file succeed and uris are:' + uris);
17. }).catch((err: BusinessError) => {
18. console.error('Invoke photoViewPicker.select failed, code is'+ err.code+', message is '+err.message);
19. })
20. let uri: string = uris[0];
21. let file = fileIo.openSync(uri, fileIo.OpenMode.READ_ONLY);
22. console.info('file fd: ' + file.fd);
23. let fd =file.fd;
24. fileIo.copyFileSync(fd, filesDir + '/test2.jpg')
25. let file2 = fileIo.openSync(filesDir + '/test2.jpg', fileIo.OpenMode.READ_ONLY );
26. let file3 = fileIo.openSync(filesDir + '/test3.jpg', fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
27. // After passing fd in, the C end can call it
28. // ReadFile(file2.fd,file3.fd)
29. }
```

[ImportedImagesPermissionsAndIssues.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/MediaLibraryKit/entry/src/main/ets/pages/ImportedImagesPermissionsAndIssues.ets#L21-L49)
