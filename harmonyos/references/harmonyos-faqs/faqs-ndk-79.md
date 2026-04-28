---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-79
title: C侧如何打开文件
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > C侧如何打开文件
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:53+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:1e6881dbb1f408523e41d13661b0ac22645f6827d027dcfd93b2c8b4ee56198d
---

目前手机上不支持在C侧打开公共路径，仅支持在ArkTS侧打开后获取文件描述符（fd），再将fd传递到C侧进行打开。参考如下：

1. 将公共路径的图片转存到沙箱目录：

```
1. import { fileIo} from '@kit.CoreFileKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import testNapi from 'libentry.so';
4. import { common } from '@kit.AbilityKit';
5. import { photoAccessHelper } from '@kit.MediaLibraryKit';
6. import { hilog } from '@kit.PerformanceAnalysisKit';

8. @Entry
9. @Component
10. struct Index {
11. @State message: string = 'Open File';

13. async open() {
14. const photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
15. photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE; // Filter and select media file type as IMAGE
16. photoSelectOptions.maxSelectNumber = 5; // Select the maximum number of media files
17. let uris: Array<string> = [];
18. const photoViewPicker = new photoAccessHelper.PhotoViewPicker();
19. await photoViewPicker.select(photoSelectOptions).then((photoSelectResult: photoAccessHelper.PhotoSelectResult) => {
20. uris = photoSelectResult.photoUris;
21. console.info('photoViewPicker.select to file succeed and uris are:' + uris);
22. }).catch((err: BusinessError) => {
23. console.error(`Invoke photoViewPicker.select failed, code is ${err.code}, message is ${err.message}`);
24. })
25. try {
26. let uri: string = uris[0];
27. let file = fileIo.openSync(uri, fileIo.OpenMode.READ_ONLY);
28. console.info('file fd: ' + file.fd);
29. let fd = file.fd
30. let context = this.getUIContext().getHostContext() as common.UIAbilityContext
31. let filesDir = context.filesDir;
32. fileIo.copyFileSync(fd, filesDir + '/test2.jpg')
33. let file2 = fileIo.openSync(filesDir + '/test2.jpg', fileIo.OpenMode.READ_ONLY);
34. let file3 = fileIo.openSync(filesDir + '/test3.jpg', fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
35. testNapi.ReadFile(file2.fd, file3.fd)
36. } catch (err) {
37. hilog.error(0x0000, 'testTag', `openSync failed, code is ${err.code}, message is ${err.message}`);
38. }
39. }

41. build() {
42. Row() {
43. Column() {
44. Text(this.message)
45. .fontSize(50)
46. .fontWeight(FontWeight.Bold)
47. }
48. .onClick(() => {
49. this.open();
50. })
51. .width('100%')
52. }
53. .height('100%')
54. }
55. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/CSideOpenFile/src/main/ets/pages/Index.ets#L21-L75)

2. 将沙箱目录的test2复制到test3，native操作如下：

```
1. static napi_value OpenFile(unsigned int fd, unsigned int fd2) {
2. OH_LOG_INFO(LOG_APP, "OpenFile");

4. if (fd != -1) {
5. char buffer[4096];
6. ssize_t bytesRead;
7. // Read the file content into the buffer
8. bytesRead = read(fd, buffer, sizeof(buffer));
9. if (bytesRead == -1) {
10. OH_LOG_INFO(LOG_APP, "fail to read file");
11. close(fd); // Close file descriptor
12. return nullptr;
13. }
14. while (bytesRead != 0) {
15. OH_LOG_INFO(LOG_APP, "Read file size %{public}lu", bytesRead);
16. OH_LOG_INFO(LOG_APP, "Read file cg");
17. char *pData1 = buffer;
18. OH_LOG_INFO(LOG_APP, "file content: \n%{public}s", pData1);
19. ssize_t bytesWrite;
20. bytesWrite = write(fd2, pData1, bytesRead);
21. if (bytesWrite == -1) {
22. OH_LOG_INFO(LOG_APP, "Writing file failed");
23. close(fd2); // Close file descriptor
24. return nullptr;
25. }
26. bytesRead = read(fd, buffer, sizeof(buffer));
27. }
28. // Close file descriptor
29. close(fd);
30. close(fd2); // Close file descriptor
31. }
32. return nullptr;
33. }
34. static napi_value ReadFile(napi_env env, napi_callback_info info) {
35. size_t argc = 2;
36. napi_value args[2] = {nullptr};
37. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
38. unsigned int fd = -1;
39. napi_get_value_uint32(env, args[0], &fd);
40. unsigned int fd2 = -1;
41. napi_get_value_uint32(env, args[1], &fd2);
42. OpenFile(fd, fd2);
43. return nullptr;
44. }
```

[napi\_init.cpp](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/Ndk/Ndk2/CSideOpenFile/src/main/cpp/napi_init.cpp#L26-L69)
