---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-714
title: 如何实现右侧滑出弹窗并选择弹窗中的选项
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现右侧滑出弹窗并选择弹窗中的选项
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:17+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:2a66d809a50e9bb4ef9c239ac1c9ab076f3fcc5c4c85fc5e1d9505cfc5d4915e
---

## 问题现象

如何实现右侧滑出弹窗并选择弹窗中的选项，例如音乐播放场景，点击打开播放列表后，右侧滑出歌曲列表的弹窗，选择歌曲后界面播放对应歌曲。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/hHpjQa95SauubRk7HATRvA/zh-cn_image_0000002658914227.png "点击放大")

## 背景知识

* [CustomDialog](../harmonyos-references/ts-methods-custom-dialog-box.md)是HarmonyOS提供的一种自定义弹窗组件，该组件可用于广告、中奖、警告、软件更新等与用户交互响应操作。开发者可以通过CustomDialogController类显示自定义弹出框。
* [transition](../harmonyos-references/ts-transition-animation-component.md)可配置转场参数，显示组件的过渡动效。使用该属性可在容器组件中的子组件插入和删除时提升用户体验。
* 哈希表是一种用于存储键值对的基本数据结构，它通过把关键码值映射到表中一个位置来访问记录，可加快查找的速度。

## 解决方案

使用哈希表通过歌曲名称获取歌手以及专辑封面的信息，并使用自定义弹窗实现播放列表的效果，通过给自定义弹窗添加transition动效，指定效果为右侧滑出可实现需求。具体步骤如下：

1. 创建哈希表并初始化，用来存储歌曲数据。

   ```ts
   private mapName = new Map<string, string>();
   ```
2. 哈希表中插入数据，其中mapName用于查找歌曲及歌手名称。

   ```ts
   this.mapName.set('Mirage', 'ZSinger-Mirage');
   this.mapName.set('My Sugar', 'BSinger-My Sugar');
   this.mapName.set('Lover', 'CSinger-Lover');
   ```
3. 通过自定义弹窗实现播放列表效果，给自定义弹窗添加transition动效，指定效果为右侧滑出，并在自定义弹窗定义@Link playingSong参数，并为该组件中添加onClick事件，其中item作为参数，使用get方法获取playingSong的值，以实现主页面和自定义页面的播放歌曲参数的双向传递。

   ```ts
   @CustomDialog
   export struct CustomDialogExample {
     controller: CustomDialogController;
     @State showFlag: Visibility = Visibility.Visible;
     private isAutoCancel: boolean = false;
     private selectList: string[] =
       ['Mirage', 'My Sugar', 'Lover'];
     @Link playingSong: string | undefined;
     @Link playingImg: string | undefined;
     private mapName = new Map<string, string>();

     build() {
       Column() {
         Column() {
           Text('播放列表')
             .fontSize(24)
             .margin({ bottom: 20 });
           List({ space: 20 }) {
             ForEach(this.selectList, (item: string) => {
               ListItem() {
                 Row() {
                   Text(item)
                     .fontSize(20)
                     .fontColor(this.playingSong === item ? Color.Orange : Color.Black);
                 }
                 .onClick(() => {
                   this.playingSong = this.mapName.get(item);
                 });
               };
             }, (index: number) => index.toString());
           }
           .divider({ strokeWidth: 1, color: Color.Gray });
         }
         .padding(20)
         .backgroundColor('#FFFFFF')
         .width(140)
         .height('80%')
         .borderRadius(16);
       }
       .justifyContent(FlexAlign.Center)
       .alignItems(HorizontalAlign.End)
       .width('100%')
       .height('100%')
       .onClick(() => {
         if (this.isAutoCancel) {
           this.cancel();
         }
       })
       .visibility(this.showFlag)
       .transition(TransitionEffect.OPACITY
         .animation({ duration: 500 })
         .combine(TransitionEffect.move(TransitionEdge.END)));
     }

     cancel() {
       this.showFlag = Visibility.Hidden;
       setTimeout(() => {
         this.controller.close();
       }, 400);
     }
   }
   ```

完整示例参考如下：

```ts
@Entry
@Component
struct CustomDialogPage {
  @State playingImg: string = '';
  private isAutoCancel: boolean = true;
  @State playingSong: string = '当前没有播放歌曲';
  private mapName = new Map<string, string>();
  dialogController: CustomDialogController = new CustomDialogController({
    builder: CustomDialogExample({
      isAutoCancel: this.isAutoCancel,
      playingSong: this.playingSong,
      playingImg: this.playingImg,
      mapName: this.mapName
    }),
    autoCancel: this.isAutoCancel,
    customStyle: true
  });

  aboutToAppear(): void {
    this.init();
  }

  init() {
    this.mapName.set('Mirage', 'ZSinger-Mirage');
    this.mapName.set('My Sugar', 'BSinger-My Sugar');
    this.mapName.set('Lover', 'CSinger-Lover');
  }

  build() {
    Row() {
      Column({ space: 10 }) {
        Button('打开播放列表')
          .onClick(() => {
            this.dialogController.open();
          });
        Text('正在播放中')
          .fontSize(22)
          .fontWeight(700);
        Text(this.playingSong);
        Image($r(this.playingImg))
          .height(250)
          .width(250);
      }
      .width('100%');
    }
    .height('100%');
  }
}

@CustomDialog
export struct CustomDialogExample {
  controller: CustomDialogController;
  @State showFlag: Visibility = Visibility.Visible;
  private isAutoCancel: boolean = false;
  private selectList: string[] =
    ['Mirage', 'My Sugar', 'Lover'];
  @Link playingSong: string | undefined;
  @Link playingImg: string | undefined;
  private mapName = new Map<string, string>();

  build() {
    Column() {
      Column() {
        Text('播放列表')
          .fontSize(24)
          .margin({ bottom: 20 });
        List({ space: 20 }) {
          ForEach(this.selectList, (item: string) => {
            ListItem() {
              Row() {
                Text(item)
                  .fontSize(20)
                  .fontColor(this.playingSong === item ? Color.Orange : Color.Black);
              }
              .onClick(() => {
                this.playingSong = this.mapName.get(item);
              });
            };
          }, (index: number) => index.toString());
        }
        .divider({ strokeWidth: 1, color: Color.Gray });
      }
      .padding(20)
      .backgroundColor('#FFFFFF')
      .width(140)
      .height('80%')
      .borderRadius(16);
    }
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.End)
    .width('100%')
    .height('100%')
    .onClick(() => {
      if (this.isAutoCancel) {
        this.cancel();
      }
    })
    .visibility(this.showFlag)
    .transition(TransitionEffect.OPACITY
      .animation({ duration: 500 })
      .combine(TransitionEffect.move(TransitionEdge.END)));
  }

  cancel() {
    this.showFlag = Visibility.Hidden;
    setTimeout(() => {
      this.controller.close();
    }, 400);
  }
}
```
