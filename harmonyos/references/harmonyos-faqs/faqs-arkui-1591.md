---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1591
title: 如何实现类似其他平台popwindow弹窗效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现类似其他平台popwindow弹窗效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:21+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:db2772066cf8902e6350f4d8623fcd76fe8c0670ec9a039bda20cccde3c901bc
---

## 问题现象

如何实现类似其他平台popwindow弹窗效果？点击标题栏文字，下拉弹出对应的选择内容弹窗。

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/ALYdWSrZRb-XBZ_ULSA79Q/zh-cn_image_0000002658849571.png "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/ug8xBnfkRRy-ktFw6XKZoQ/zh-cn_image_0000002628770206.gif "点击放大")

## 背景知识

[Popup弹窗](../harmonyos-references/ts-universal-attributes-popup.md)：给组件绑定Popup弹窗，并设置弹窗内容，交互逻辑和显示状态。

## 解决方案

使用Popup弹窗可以实现类似其他平台popwindow弹窗效果。

```screen
@Component
@Entry
struct PopupDemoForPopWindow {
  private arr: string[] =
    ['全部', '三元区', '沙县区', '明溪县', '清流县', '宁化县', '大田县', '尤溪县', '将乐县', '泰宁县', '建宁县',
      '永安市'];
  private arrTitle: string[] = ['区县', '全部', '开始时间', '结束时间'];
  @State handlePopup: boolean = false;

  @Builder
  OverlayNode() {
    Column() {
    }.width('100%').height('100%').alignItems(HorizontalAlign.Center)
    .backgroundColor('rgba(0,0,0,0.2)');
  }

  @Builder
  CustomItem(str: string) {
    Column() {
      Text(str)
        .fontColor(Color.Red)
        .width(80)
        .height(50);
    }
    .width('100%');
  }

  @Builder
  customDialogBuilder() {
    Flex({ direction: FlexDirection.Row, wrap: FlexWrap.Wrap }) {
      ForEach(this.arr, (item: string) => {
        Text(item).height(40).onClick(() => {
          this.handlePopup = !this.handlePopup;
        }).width('25%').textAlign(TextAlign.Center);
      });
    }
    .width('100%')
  }

  build() {
    Column() {
      Line()
        .width('100%')
        .height(1)
        .bindPopup(this.handlePopup, {
          builder: this.customDialogBuilder(),
          enableArrow: false,
          radius: 0,
          width: '100%',
          targetSpace: 39,
          onStateChange: (e) => {
            if (!e.isVisible) {
              this.handlePopup = false;
            }
          }
        });
      Row() {
        Flex({ direction: FlexDirection.Row, wrap: FlexWrap.Wrap }) {
          ForEach(this.arrTitle, (item: string, index: number) => {
            Text(item).height(60)
              .onClick(() => {
                if (index === 0) {
                  this.handlePopup = !this.handlePopup;
                }
              })
              .width('25%').textAlign(TextAlign.Center);
          });
        };
      }
      .backgroundColor('#F2F2F2')
      .height(40);

      Stack() {
        Column() {
          Text('我是内容');
        };

        Column() {
        }
        .width('100%')
        .height('100%')
        .alignItems(HorizontalAlign.Center)
        .backgroundColor('rgba(0,0,0,0.2)')
        .visibility(this.handlePopup === false ? Visibility.Hidden : Visibility.Visible);
      };
    }
    .backgroundColor(Color.White)
    .width('100%')
    .height('100%');
  }
}
```
