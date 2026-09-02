---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1451
title: 如何使用clip接口截断超出组件区域的内容
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何使用clip接口截断超出组件区域的内容
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:10+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:48886faf6f4c6cd6b6f07378471a4a8748081b58691d5e7517096c522116fa41
---

## 问题现象

当设置AlbumPickerComponent组件高度为0时，为何会出现黑色区域？问题代码如下：

```ts
import {
  AlbumInfo, AlbumPickerComponent, AlbumPickerOptions, PickerColorMode
} from '@kit.MediaLibraryKit';

@Entry
@Component
struct ClipTheArea {
  albumPickerOptions: AlbumPickerOptions = new AlbumPickerOptions();

  private onAlbumClick(albumInfo: AlbumInfo): boolean {
    if (albumInfo?.uri) {
    }
    if (albumInfo?.albumName) {
    }
    return true;
  }

  aboutToAppear(): void {
    this.albumPickerOptions.themeColorMode = PickerColorMode.DARK;
  }

  build() {
    Row() {
      Column() {
        Scroll() {
          Column() {
            Column() {
              Text('组件1')
                .fontSize(20);
            }
            .justifyContent(FlexAlign.Center)
            .width('calc(100%- 32px)')
            .height('48%')
            .backgroundColor('#f1f3f5')
            .borderRadius(30)
            .margin({ bottom: 17, left: '16px', right: '16px' });

            Stack() {
              AlbumPickerComponent({
                albumPickerOptions: this.albumPickerOptions,
                onAlbumClick: (albumInfo: AlbumInfo): boolean => this.onAlbumClick(albumInfo),
              }).height(0).border({
                width: '1px',
                style: BorderStyle.Solid,
                color: Color.Red
              });
            }.height(0).border({
              width: '1px',
              style: BorderStyle.Solid,
              color: '#0A59F7'
            })
            .width('calc(100%- 32px)');

            Column() {
              Text('组件2')
                .fontSize(20);
            }
            .justifyContent(FlexAlign.Center)
            .width('calc(100%- 32px)')
            .height('48%')
            .backgroundColor('#f1f3f5')
            .borderRadius(30)
            .margin({ top: 17, left: '16px', right: '16px' });
          };
        }.height('100%');
      }
      .width('100%');
    }
    .height('100%');
  }
}
```

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/dAmLdJlVSCyn-1t-k8LJew/zh-cn_image_0000002628764164.png "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/tL3OB5znRBakE4mUvQQAzw/zh-cn_image_0000002658963483.png "点击放大")

## 背景知识

[clip](../harmonyos-references/ts-universal-attributes-sharp-clipping.md)：形状裁剪clip用于对组件进行裁剪、遮罩处理。其默认值为false表示不对子组件进行裁剪，设置为true可截断超出区域的内容。

## 解决方案

在使用AlbumPickerComponent时，其内部嵌入的UIExtensionComponent组件会有一个默认高度，可以通过设置clip属性值为true来截断超出区域。示例代码如下：

```ts
import {
  AlbumInfo, AlbumPickerComponent, AlbumPickerOptions, PickerColorMode
} from '@kit.MediaLibraryKit';

@Entry
@Component
struct ClipTheArea {
  albumPickerOptions: AlbumPickerOptions = new AlbumPickerOptions();

  private onAlbumClick(albumInfo: AlbumInfo): boolean {
    if (albumInfo?.uri) {
    }
    if (albumInfo?.albumName) {
    }
    return true;
  }

  aboutToAppear(): void {
    this.albumPickerOptions.themeColorMode = PickerColorMode.DARK;
  }

  build() {
    Row() {
      Column() {
        Scroll() {
          Column() {
            Column() {
              Text('组件1')
                .fontSize(20);
            }
            .justifyContent(FlexAlign.Center)
            .width('calc(100%- 32px)')
            .height('48%')
            .backgroundColor('#f1f3f5')
            .borderRadius(30)
            .margin({ bottom: 17, left: '16px', right: '16px' });

            Stack() {
              AlbumPickerComponent({
                albumPickerOptions: this.albumPickerOptions,
                onAlbumClick: (albumInfo: AlbumInfo): boolean => this.onAlbumClick(albumInfo),
              }).height(0).border({
                width: '1px',
                style: BorderStyle.Solid,
                color: Color.Red
              })
                .clip(true); // 设置clip为true可截断超出区域的内容
            }.height(0).border({
              width: '1px',
              style: BorderStyle.Solid,
              color: '#0A59F7'
            })
            .width('calc(100%- 32px)');

            Column() {
              Text('组件2')
                .fontSize(20);
            }
            .justifyContent(FlexAlign.Center)
            .width('calc(100%- 32px)')
            .height('48%')
            .backgroundColor('#f1f3f5')
            .borderRadius(30)
            .margin({ top: 17, left: '16px', right: '16px' });
          };
        }.height('100%');
      }
      .width('100%');
    }
    .height('100%');
  }
}
```
