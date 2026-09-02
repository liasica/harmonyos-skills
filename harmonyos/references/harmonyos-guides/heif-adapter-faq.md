---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/heif-adapter-faq
title: 如何处理HEIF图片
breadcrumb: 指南 > 媒体 > Image Kit（图片处理服务） > Image Kit常见问题 > 如何处理HEIF图片
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:46+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:accdf589830db39c0226bc52024382074713cca11b83c8b32b7a855efa129980
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

### 为什么通过PhotoViewPicker或URI获取HEIF图片时得到JPEG图片？

**可能原因**

从API version 20开始，系统在部分访问链路中会将HEIF图片转换为兼容性更好的JPEG图片，以降低应用处理成本并提升兼容性。如果应用已经具备HEIF图片处理能力，但未向系统声明该能力，最终获取到的图片文件可能是系统生成的JPEG兼容副本。

**解决措施**

如果应用需要获取HEIF原图，应显式声明应用支持HEIF图片。通过[PhotoViewPicker](../harmonyos-references/arkts-apis-photoaccesshelper-photoviewpicker.md)获取图片时，可在[PhotoSelectOptions](../harmonyos-references/arkts-apis-photoaccesshelper-class.md#photoselectoptions)中配置assetCompatibleCapability，并通过preferredCompatibleMode指定首选兼容模式。

* assetCompatibleCapability.supportedHighResolution是AssetCompatibleCapability的必填字段，表示应用支持高分辨率资产。
* assetCompatibleCapability.supportedMimeType用于声明应用支持的MIME类型（从API版本26.0.0开始支持），配置image/heic表示应用支持HEIF图片。
* preferredCompatibleMode用于指定资产兼容性模式（从API版本26.0.0开始支持）。应用希望按资产当前格式返回时，可配置为PreferredCompatibleMode.CURRENT；希望始终获得兼容格式时，可配置为PreferredCompatibleMode.COMPATIBLE。

以如何配置PhotoViewPicker以获取HEIF原图为例。

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

function createHeifOriginalSelectOptions(): photoAccessHelper.PhotoSelectOptions {
  const photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
  photoSelectOptions.assetCompatibleCapability = {
    supportedHighResolution: true,
    supportedMimeType: ['image/heic']
  } as photoAccessHelper.AssetCompatibleCapability;
  photoSelectOptions.preferredCompatibleMode = photoAccessHelper.PreferredCompatibleMode.CURRENT;
  return photoSelectOptions;
}

async function selectHeifOriginalWithPhotoViewPicker(): Promise<photoAccessHelper.PhotoSelectResult | undefined> {
  try {
    const photoSelectOptions: photoAccessHelper.PhotoSelectOptions = createHeifOriginalSelectOptions();
    const photoPicker = new photoAccessHelper.PhotoViewPicker();
    const photoSelectResult: photoAccessHelper.PhotoSelectResult = await photoPicker.select(photoSelectOptions);
    console.info(`PhotoViewPicker.select successfully: ${JSON.stringify(photoSelectResult)}`);
    return photoSelectResult;
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    console.error(`PhotoViewPicker.select failed. code: ${err.code}, message: ${err.message}`);
    return undefined;
  }
}
```

获取到[photoAccessHelper.PhotoSelectResult](../harmonyos-references/arkts-apis-photoaccesshelper-class.md#photoselectresult)结果后，应用可使用photoSelectResult.photoUris读取返回URI。

如果应用不通过PhotoViewPicker选择图片，而是通过[PhotoAccessHelper](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md)查询、打开或批量处理媒体资产。例如网盘、备份、内容归档等应用场景，可使用[setAssetCompatibleCapability](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#setassetcompatiblecapability24)接口配置[AssetCompatibleCapability](../harmonyos-references/arkts-apis-photoaccesshelper-i.md#assetcompatiblecapability24)，声明应用支持image/heic。配置后再通过getAssets等接口访问资产。

以打开结果集中的第一条资产为例，实际业务可通过predicates添加筛选条件定位目标资产。

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { dataSharePredicates } from '@kit.ArkData';
import { fileIo } from '@kit.CoreFileKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

async function enableHeifAssetCompatibleCapability(
  phAccessHelper: photoAccessHelper.PhotoAccessHelper
): Promise<void> {
  const capability: photoAccessHelper.AssetCompatibleCapability = {
    supportedHighResolution: true,
    supportedMimeType: ['image/heic']
  };
  await phAccessHelper.setAssetCompatibleCapability(capability);
}

async function openFirstPhotoAssetFd(
  phAccessHelper: photoAccessHelper.PhotoAccessHelper
): Promise<number | undefined> {
  let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> | undefined = undefined;
  try {
    await enableHeifAssetCompatibleCapability(phAccessHelper);

    const fetchOptions: photoAccessHelper.FetchOptions = {
      fetchColumns: [photoAccessHelper.PhotoKeys.URI],
      predicates: new dataSharePredicates.DataSharePredicates()
    };
    fetchResult = await phAccessHelper.getAssets(fetchOptions);
    const asset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
    const file: fileIo.File = fileIo.openSync(asset.uri, fileIo.OpenMode.READ_ONLY);

    // 获取到fd后，可按业务需要进行解码、上传、备份或格式校验，使用完成后由调用方关闭fd。
    return file.fd;
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    console.error(`Open asset failed. code: ${err.code}, message: ${err.message}`);
    return undefined;
  } finally {
    fetchResult?.close();
  }
}
```

### 获取到图片后，为什么格式、文件大小存在异常？部分图片显示不完整？

**可能原因**

应用根据URI后缀、文件后缀名或媒体库[PhotoKeys](../harmonyos-references/arkts-apis-photoaccesshelper-e.md#photokeys)记录的MEDIA\_SUFFIX作为图片文件格式的依据。文件真实格式应以其二进制数据内容为准。

应用根据媒体库[PhotoKeys](../harmonyos-references/arkts-apis-photoaccesshelper-e.md#photokeys)记录的SIZE作为文件大小，但最终获取到的图片文件由于经过兼容性转换，导致文件体积发生了变化。如果此时直接按照原图大小使用该图片文件，由于HEIF图片通常比JPG图片体积更小，仅读取JPG文件的一部分就认为文件结束，会导致图片显示不完整。

**解决措施**

获取图片URI或fd后，使用Image Kit接口读取真实的图片格式、宽高等信息，这些接口会解析图片二进制数据获取准确信息。使用Core File Kit的能力获取文件真实大小。

避免仅根据URI后缀、文件名或媒体库记录判断图片文件属性。对上传、分享、编辑、后处理等关键链路，使用最终拿到的图片文件fd重新校验格式、文件大小。

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { image } from '@kit.ImageKit';

async function getFinalFileSize(file: string | number): Promise<number | undefined> {
  try {
    const stat: fileIo.Stat = await fileIo.stat(file);
    console.info(`file size: ${stat.size}`);
    return stat.size;
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    console.error(`Get file size failed. code: ${err.code}, message: ${err.message}`);
    return undefined;
  }
}

async function getImageInfoByFd(fd: number): Promise<image.ImageInfo | undefined> {
  let imageSource: image.ImageSource | undefined = undefined;
  try {
    imageSource = image.createImageSource(fd);
    const imageInfo: image.ImageInfo = imageSource.getImageInfoSync();
    console.info(`mimeType: ${imageInfo.mimeType}`);
    console.info(`width: ${imageInfo.size.width}, height: ${imageInfo.size.height}`);
    return imageInfo;
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    console.error(`Get image info failed. code: ${err.code}, message: ${err.message}`);
    return undefined;
  } finally {
    await imageSource?.release();
  }
}
```

C/C++应用可参考[使用Image\_NativeModule完成图片解码](image-source-c.md)，通过ImageSource读取图片真实格式、宽高等信息。

对最终打开的文件描述符fd使用fstat，可获取其准确的文件大小。示例代码如下：

```c
#include <errno.h>
#include <stdint.h>
#include <stdio.h>
#include <sys/stat.h>

static int64_t GetFinalFileSizeByFd(int32_t fd)
{
    if (fd < 0) {
        printf("Invalid fd.\n");
        return -1;
    }

    struct stat fileStatus = {0};
    if (fstat(fd, &fileStatus) != 0) {
        printf("fstat failed, errno: %d.\n", errno);
        return -1;
    }

    if (!S_ISREG(fileStatus.st_mode)) {
        printf("The fd does not point to a regular file.\n");
        return -1;
    }

    return (int64_t)fileStatus.st_size;
}
```

### 担心使用HEIF格式图片存在兼容性问题，需使用JPEG或PNG格式的图片，如何操作

可以借助Image Kit的图片编解码能力，将HEIF图片转码成JPEG或PNG格式的图片。

转码的本质是将HEIF图片解码后，把解码的结果重新编码为JPEG或PNG格式的图片。通过配置编码参数，开发者可以更加灵活地控制最终获取到的图片文件格式、图片质量以及图片属性。

转码前建议先按上文方式确认最终拿到的图片文件真实格式，以免进行不必要的编解码操作，带来冗余耗时和性能浪费。

示例代码如下：

```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { image } from '@kit.ImageKit';
import { PromptAction } from '@kit.ArkUI';

const promptAction = new PromptAction();

export async function reEncoding(context : Context, fd : number | undefined) {
  // 首先获取图片文件的fd，创建ImageSource。
  const imageSource : image.ImageSource = image.createImageSource(fd);
  // 创建ImagePacker，以便调用图片编码接口。
  const imagePackerApi = image.createImagePacker();
  // 配置图片编码选项：
  // format应使用标准的mimetype格式，如："image/jpeg"、"image/png"、"image/heic"；
  // quality默认值为0，建议不低于80；本示例统一设置为90，兼顾图片质量和文件体积；
  // needsPackProperties参数，用于控制编码时是否保存图片属性信息。默认值为false，即不保存。
  let packOpts : image.PackingOption = { format:'image/jpeg', quality:90, needsPackProperties:false };
  // 指定图片编码文件的存放路径。
  const filePath : string = context.cacheDir + '/result.jpg';
  try {
    let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
    imagePackerApi.packToFile(imageSource, file.fd, packOpts).then(() => {
      promptAction.showToast({ message: `Succeed to pack the image.`});
      console.info('Succeed to pack the image.');
    }).catch((error : BusinessError) => {
      promptAction.showToast({ message: 'Failed to pack the image. And the error is: ' + error});
      console.error('Failed to pack the image. And the error is: ' + error);
    }).finally(async () => {
      fileIo.closeSync(file.fd);
      await imageSource.release();
      await imagePackerApi.release();
    })
  } catch (error) {
    console.error('Failed to pack the image. And the error is: ' + error);
  }
}
```

如需使用CAPI进行图片转码，应首先创建ImageSource和ImagePacker实例，然后指定编码参数，调用图片编码接口完成转码。详细示例代码可参考[使用Image\_NativeModule完成图片编码](image-packer-c.md)。
