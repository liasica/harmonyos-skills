---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/heif-adapter-faq
title: 如何处理HEIF图片
breadcrumb: 指南 > 媒体 > Image Kit（图片处理服务） > Image Kit常见问题 > 如何处理HEIF图片
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:21+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d9248403a20cbcec4e95d6e704a5d0028fb175f3ff3ea6db30eda1dc5b018ed1
---

## HEIF图片介绍

HEIF图片（High Efficiency Image File Format，HEIF，也称高效图像文件格式），是一个用于单张图像或图像序列的文件格式。它由动态影像专家小组（MPEG）开发，并在MPEG-H Part 12（ISO/IEC 23008-12）中定义。

目前主流的HEIF图片均使用HEVC（H.265）编码，这也是系统当前支持的HEIF图片。HEIF图片在压缩效率上具有明显优势，能够在保证图像质量的同时显著减小文件体积，通常比JPEG节省约50%的存储空间。

系统从API12开始支持HEIF图片的编解码与显示，如果应用基于系统Image Kit、ArkUI Image组件、ArkWeb等模块实现图片处理功能，则可以像处理JPEG、PNG等格式的图片一样，处理HEIF图片。

HEIF图片解码可参考：[图片解码指南（ArkTS）](image-decoding.md)和[图片解码指南（C/C++）](image-source-c.md)。

HEIF图片显示可参考：[ArkUI Image组件图片显示](arkts-graphics-display.md)。

HEIF图片编码可参考：[图片编码指南（ArkTS）](image-encoding.md)和[图片编码指南（C/C++）](image-packer-c.md)。

ArkWeb图片上传可参考：[使用Web组件上传文件](web-file-upload.md)。

## 常见问题

### 上传HEIF图片时提示：“不支持的格式”

可以使用ImageSource[属性](../harmonyos-references/arkts-apis-image-imagesource.md#属性)中的supportedFormats和ImagePacker[属性](../harmonyos-references/arkts-apis-image-imagepacker.md#属性)中的supportedFormats，来查看系统支持编解码的图片格式。只要查询到的结果中包含"image/heic"，即代表该设备支持HEIF图片编解码。

系统侧不会拦截HEIF图片上传，若HEIF图片上传不成功，可能的原因是：应用对后缀名为.heic、.heif、.HEIC、.HEIF的图片文件做了过滤限制。

对于使用系统图片处理能力的应用，只需要解除过滤限制，即可正常上传、显示HEIF图片。

如果应用不希望使用HEIF图片，可以借助[Image Kit](image-overview.md)提供的图片编解码能力，自行[将HEIF图片转码为JPEG或PNG格式的图片](heif-adapter-faq.md#担心使用heif格式图片存在兼容性问题需使用jpeg或png格式的图片如何操作)。

当应用没有使用系统提供的图片处理能力，且自身无法处理HEIF图片时，还可以选择使用[Media Library Kit](photoaccesshelper-overview.md)提供的媒体资源访问能力，这时系统会主动将HEIF图片转码为JPEG图片。

### 为什么选择的是HEIF图片，实际上获取到的却是JPEG图片？

当使用[媒体文件管理服务](photoaccesshelper-overview.md)或[URI（Uniform Resource Identifier）](core-file-kit-intro.md#亮点特征)访问HEIF图片时，系统会自动将HEIF图片转码为兼容性相对更好的JPEG图片，且保证转码前后图片携带的元数据信息一致。

如果想直接获取最原始的HEIF图片，建议使用[文件基础服务](core-file-kit-intro.md)获取HEIF图片的[文件描述符FD（File Descriptor）](core-file-kit-intro.md#亮点特征)。

### 担心使用HEIF格式图片存在兼容性问题，需使用JPEG或PNG格式的图片，如何操作

可以借助Image Kit的图片编解码能力，将HEIF图片转码成JPEG或PNG格式的图片。

转码的本质是将HEIF图片解码后，把解码的结果重新编码为JPEG或PNG格式的图片。通过配置编码参数，开发者可以更加灵活地控制最终获取到的图片文件格式、图片质量以及图片属性。

示例代码如下：

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { fileIo as fs } from '@kit.CoreFileKit';
3. import { image } from '@kit.ImageKit';
4. import { PromptAction } from '@kit.ArkUI';

6. const promptAction = new PromptAction();

8. export async function reEncoding(context : Context, fd : number | undefined) {
9. // 首先获取图片文件的fd，创建ImageSource。
10. const imageSource : image.ImageSource = image.createImageSource(fd);
11. // 创建ImagePacker，以便调用图片编码接口。
12. const imagePackerApi = image.createImagePacker();
13. // 配置图片编码选项：
14. // format应使用标准的mimetype格式，如："image/jpeg"、"image/png"、"image/heic"；
15. // quality推荐设置为80，在保证较好的图片质量的同时，可以使编码后的图片文件体积更小；
16. // needsPackProperties参数，用于控制编码时是否保存图片属性信息。默认值为false，即不保存。
17. let packOpts : image.PackingOption = { format:'image/jpeg', quality:80, needsPackProperties:false };
18. // 指定图片编码文件的存放路径。
19. const filePath : string = context.cacheDir + '/result.jpg';
20. try {
21. let file = fs.openSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE);
22. imagePackerApi.packToFile(imageSource, file.fd, packOpts).then(() => {
23. promptAction.showToast({ message: `Succeed to pack the image.`});
24. console.info('Succeed to pack the image.');
25. }).catch((error : BusinessError) => {
26. promptAction.showToast({ message: 'Failed to pack the image. And the error is: ' + error});
27. console.error('Failed to pack the image. And the error is: ' + error);
28. }).finally(()=>{
29. fs.closeSync(file.fd);
30. })
31. } catch (error) {
32. console.error('Failed to pack the image. And the error is: ' + error);
33. }
34. }
```

[TranscodingUtility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageArkTSSample/entry/src/main/ets/tools/TranscodingUtility.ets#L15-L46)

如需使用CAPI进行图片转码，应首先创建ImageSource和ImagePacker实例，然后指定编码参数，调用图片编码接口完成转码。详细示例代码可参考[使用Image\_NativeModule完成图片编码](image-packer-c.md)。
