---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/component-guidelines-albumpicker
title: 使用AlbumPicker组件访问相册列表
breadcrumb: 指南 > 媒体 > Media Library Kit（媒体文件管理服务） > 使用AlbumPicker组件访问相册列表
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:19+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:f22b23a78f75c22e9afab1e56b7da5682f17f6c8b44c3c5ddb2a92205d10989f
---

开发者可以在布局中嵌入AlbumPickerComponent组件，通过此组件，应用无需申请权限，即可访问公共目录中的相册列表。

需配合[使用PhotoPicker组件访问图片/视频](component-guidelines-photoviewpicker.md)一起使用，用户通过AlbumPickerComponent组件选择对应相册并通知PhotoPickerComponent组件刷新成对应相册的图片和视频。

界面效果如图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/g2GO-XZASjyGU6KeCaZ5GA/zh-cn_image_0000002706834600.png)

## 开发步骤

1. 导入相册组件模块文件。

   ```ts
   import {
     AlbumPickerComponent,
     AlbumPickerOptions,
     AlbumInfo,
     PickerColorMode,
     PickerController,
     DataType
   } from '@kit.MediaLibraryKit';
   ```
2. 创建相册组件配置选项实例（AlbumPickerOptions）。

   通过AlbumPickerOptions，开发者可配置相册页主题颜色，详见[AlbumPickerOptions API参考](../harmonyos-references/ohos-file-albumpickercomponent.md#albumpickeroptions)。

   ```ts
   // 用于相册组件初始化时设置参数信息。
   albumOptions: AlbumPickerOptions = new AlbumPickerOptions();
   pickerController: PickerController = new PickerController();
   ```
3. 初始化组件配置选项实例（AlbumPickerOptions）。

   ```ts
   /**
    * 设置相册页颜色模式， 默认AUTO。
    * AUTO：跟随系统的模式，LIGHT：浅色模式，DARK：深色模式。
    */
   this.albumOptions.themeColorMode = PickerColorMode.AUTO;
   ```
4. 创建[AlbumPickerComponent](../harmonyos-references/ohos-file-albumpickercomponent.md#albumpickercomponent)组件。

   ```ts
   AlbumPickerComponent({
     // 设置组件选择选项实例。
     albumPickerOptions: this.albumOptions,

     /**
      *相册被选中回调，返回相册信息。
      * AlbumInfo（uri）
      */
     onAlbumClick: (albumInfo: AlbumInfo): boolean => this.onAlbumClick(albumInfo),
   })
   ```
5. 与PhotoPicker组件联动，将相册URI给到应用，根据相册URI更新PhotoPicker组件宫格页内容。

   ```ts
   private onAlbumClick(albumInfo: AlbumInfo): boolean {
       if (albumInfo?.uri) {
           // 根据相册url更新宫格页内容。
           this.pickerController.setData(DataType.SET_ALBUM_URI, albumInfo.uri);
       }
       return true;
   }
   ```

## 完整示例

```ts
import {
  PhotoPickerComponent,
  AlbumPickerComponent,
  AlbumPickerOptions,
  AlbumInfo,
  PickerColorMode,
  PickerController,
  DataType
} from '@kit.MediaLibraryKit';

@Entry
@Component
struct AlbumPage {
  @State pickerController: PickerController = new PickerController();
  @State Width: string = '100%';
  @State Height: string = '100%';
  @State isShowAlbum: boolean = false;
  @State fontColor: string = '#182431222'
  @State selectedFontColor: string = '#007DFF'
  @State currentIndex: number = 0
  private controller: TabsController = new TabsController();
  albumOptions = new AlbumPickerOptions();
  albumOptions1 = new AlbumPickerOptions();
  albumOptions2 = new AlbumPickerOptions();

  /**
   *相册被选中回调，返回相册信息
   * AlbumInfo（uri）
   */
  private onAlbumClick(albumInfo: AlbumInfo): boolean {
    this.isShowAlbum = false;
    if (albumInfo?.uri) {
      //  根据相册url更新宫格页内容。
      this.pickerController.setData(DataType.SET_ALBUM_URI, albumInfo.uri);
    }
    return true;
  }

  aboutToAppear() {
    /**
     * 设置相册页颜色模式， 默认AUTO。
     * AUTO：跟随系统的模式， LIGHT：浅色模式， DARK：深色模式
     */
    this.albumOptions.themeColorMode = PickerColorMode.AUTO;
    this.albumOptions1.themeColorMode = PickerColorMode.LIGHT;
    this.albumOptions2.themeColorMode = PickerColorMode.DARK;
  }

  // 设置导航栏的样式
  @Builder
  tabBuilder(index: number, name: string) {
    Column() {
      Text(name)
        .fontColor(this.currentIndex === index ? this.selectedFontColor : this.fontColor)
        .fontSize(16)
        .fontWeight(this.currentIndex === index ? 500 : 400)
        .lineHeight(22)
        .margin({ top: 17, bottom: 7 })
      Divider()
        .strokeWidth(2)
        .color('#007DFF')
        .opacity(this.currentIndex === index ? 1 : 0)
    }.width('100%')
  }

  build() {
    Stack() {
      Column() {
        Row() {
          Button("全部相册").width('95%').height('5%').onClick(() => {
            this.isShowAlbum = true;
          })
        }.margin({ top: 40 })
        Column() {
          PhotoPickerComponent({
            pickerController: this.pickerController,
          }).height(this.Height).width(this.Width)
        }.width('100%').height('100%').alignItems(HorizontalAlign.Center).visibility(this.isShowAlbum ? Visibility.None: Visibility.Visible)
      }

      if (this.isShowAlbum) {
        Row() {
          Column() {
            /**
             * 使用3个组件,以便更好展示不同效果。
             * 需要注意的是切换tab会导致AlbumPickerComponent覆盖在PhotoPickerComponent上导致点击事件失效，
             * 设置PhotoPickerComponent不可见可以规避点击失效。
             */
            Tabs({ barPosition: BarPosition.Start, index: this.currentIndex, controller: this.controller }) {
              TabContent() {
                AlbumPickerComponent({
                  albumPickerOptions: this.albumOptions,
                  onAlbumClick: (albumInfo: AlbumInfo): boolean => this.onAlbumClick(albumInfo),
                }).height('100%').width('100%')
              }.tabBar(this.tabBuilder(0, '系统'))
              TabContent() {
                AlbumPickerComponent({
                  albumPickerOptions: this.albumOptions1,
                  onAlbumClick: (albumInfo: AlbumInfo): boolean => this.onAlbumClick(albumInfo),
                }).height('100%').width('100%')
              }.tabBar(this.tabBuilder(1, '浅色'))

              TabContent() {
                AlbumPickerComponent({
                  albumPickerOptions: this.albumOptions2,
                  onAlbumClick: (albumInfo: AlbumInfo): boolean => this.onAlbumClick(albumInfo),
                }).height('100%').width('100%')
              }.tabBar(this.tabBuilder(2, '深色'))
            }
            .vertical(false)
            .barMode(BarMode.Fixed)
            .barWidth('100%')
            .barHeight(56)
            .animationDuration(100)
            .onChange((index: number) => {
              this.currentIndex = index;
            })
            .width('100%')
            .height('100%')
            .backgroundColor('#F1F3F5')
          }.width('100%').height('100%').justifyContent(FlexAlign.Center).alignItems(HorizontalAlign.Center)
        }
        .margin({ top: 40 })
      }
    }
  }
}
```
