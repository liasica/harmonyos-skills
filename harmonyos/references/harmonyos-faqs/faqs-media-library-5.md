---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-library-5
title: 如何选择文件保存路径
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 媒体文件管理（Media Library） > 如何选择文件保存路径
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:32+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:433481ffd56d7852f54c1e0520c6ad7d249f0c07b942d4cfd1dbcf179058e226
---

官网中保存用户文件提供的方法是FilePicker需要拉起系统应用，再由用户选择具体路径保存文件的，参考文档：[保存用户文件](../harmonyos-guides/save-user-file.md)。

保存文件到媒体库时，使用SaveButton控件，示例如下：

```
1. import { photoAccessHelper } from '@kit.MediaLibraryKit';
2. import { fileIo } from '@kit.CoreFileKit';

4. @Entry
5. @Component
6. struct WebComponent {
7. build() {
8. Row() {
9. Column() {
10. Image($r('app.media.startIcon'))
11. .height(200)
12. .width(200)
13. SaveButton().onClick(async (event: ClickEvent, result: SaveButtonOnClickResult) => {
14. if (result === SaveButtonOnClickResult.SUCCESS) {
15. try {
16. const context = this.getUIContext().getHostContext()!;
17. let helper = photoAccessHelper.getPhotoAccessHelper(context);
18. // Create image files through the Create Asset interface within 10 seconds after the nClick trigger, and revoke the Create Asset permission after 10 seconds.
19. let uri = await helper.createAsset(photoAccessHelper.PhotoType.IMAGE, 'jpg');
20. // Using URI to open files allows for continuous writing of content without time constraints during the writing process
21. let file = await fileIo.open(uri, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
22. try {
23. context.resourceManager.getMediaContent($r('app.media.startIcon').id, 0)
24. .then(async value => {
25. let media = value.buffer;
26. // Write to the media library file
27. await fileIo.write(file.fd, media);
28. await fileIo.close(file.fd);
29. this.getUIContext().showAlertDialog({ message: 'Saved to album!' });
30. });
31. } catch (err) {
32. console.error('error is ' + JSON.stringify(err))
33. }
34. } catch (error) {
35. console.error('error is ' + JSON.stringify(error));
36. }
37. } else {
38. this.getUIContext().showAlertDialog({ message: 'Failed to set permissions' })
39. }
40. })
41. }
42. .width('100%')
43. }
44. .height('100%')
45. }
46. }
```

[SelectFileSavePath.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/MediaLibraryKit/entry/src/main/ets/pages/SelectFileSavePath.ets#L21-L66)
