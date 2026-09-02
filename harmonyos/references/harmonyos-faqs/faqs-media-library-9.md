---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-library-9
title: 打开PhotoViewPicker时默认选中上次选中的图片
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 媒体文件管理（Media Library） > 打开PhotoViewPicker时默认选中上次选中的图片
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:31+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:48aecdc79a6020fe3f3b403095fe5b3cd50aeb07bd06489c568f27a7004a2e24
---

## 问题现象

通过Media Library Kit的PhotoViewPicker实现选择系统相册图片，之前选择的图片没有默认选中。

预期效果：选择图片->完成提交->下次进入标记选中状态（不完成提交下次进入不选中）。

实际效果：选择图片->完成提交->下次进入未标记选中状态。

## 背景知识

通过[PhotoViewPicker](../harmonyos-references/arkts-apis-photoaccesshelper-photoviewpicker.md)选择系统相册图片时，可以使用PhotoSelectOptions属性控制选择的媒体文件类型、数量、预选择文件数据、推荐的媒体文件等。

## 解决方案

PhotoViewPicker选择图片时不会对选择结果进行记录，建议可以自行保存每次选择的图片uri，再通过PhotoSelectOptions属性设置预选的图片数据。

1. 将每次选择的图片uri缓存到数组preSelected中。
2. 通过PhotoSelectOptions中preselectedUris属性，将缓存的uri设置为预选择的图片。

完整示例代码如下：

```ts
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  private preSelected: string[] = [];

  build() {
    Column() {
      Button('Select')
        .padding(10)
        .fontSize(40)
        .onClick(() => {
          let photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
          photoSelectOptions.maxSelectNumber = 9;
          photoSelectOptions.preselectedUris = this.preSelected;
          photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_VIDEO_TYPE;
          let photoViewPicker = new photoAccessHelper.PhotoViewPicker();
          photoViewPicker.select(photoSelectOptions)
            .then((photoSelectResult: photoAccessHelper.PhotoSelectResult) => {
              this.preSelected = photoSelectResult.photoUris;
            })
            .catch((err: BusinessError) => {
              console.error(`Invoke photoViewPicker.select failed, code is ${err.code}, message is ${err.message}`);
            });
        });
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Center);
  }
}
```

如果preselectedUris中预选择的图片已被删除，select接口不会报异常，也不会影响未删除的图片被默认选中。

目前PhotoViewPicker不支持将预选择的图片集中显示在列表头部，如果上次选中的图片是分散的，再次进入默认选中的图片仍然是分散的。
