---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-769
title: 如何实现简单列表折叠和展开
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何实现简单列表折叠和展开
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:03+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:be4e3349138eba3eda82e7852912b9e7f843140bd63e9edef8a18de8889a567d
---

## 问题现象

如何实现列表项可折叠和展开，类似QT中TreeWidget组件的效果？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/a4WEaCpCSimmcwT4oo0KrQ/zh-cn_image_0000002628395806.gif "点击放大")

## 背景知识

* [List组件](../harmonyos-references/ts-container-list.md)包含一系列相同宽度的列表项。适合连续、多行呈现同类数据，子组件仅支持[ListItem](../harmonyos-references/ts-container-listitem.md)、[ListItemGroup](../harmonyos-references/ts-container-listitemgroup.md)和[自定义组件](../harmonyos-references/custom-comp.md)。
* [TreeView](../harmonyos-references/ohos-arkui-advanced-treeview.md)作为一种分层显示的列表，适合显示嵌套结构。拥有父列表项和子列表项，可展开或折叠。用于效率型应用，如备忘录、电子邮件、图库中的侧边导航栏中。

## 解决方案

* **方案一**：可以使用TreeView组件实现[简单树视图](../harmonyos-references/ohos-arkui-advanced-treeview.md#示例1设置简单树视图)效果，可以对各节点项目新增、删除、重命名操作，推荐使用此方法。
* **方案二**：可以直接使用List组件构建列表容器，列表ListItem子项中添加Button按钮绑定点击事件和条件判断实现折叠和展开效果。

  ```ts
  @Entry
  @Component
  struct ListTest {
    private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14];
    @State isContentShow: boolean[] = new Array(15).fill(false);
    context: UIContext = this.getUIContext();

    build() {
      Column() {
        List({ initialIndex: 0 }) {
          ForEach(this.arr, (item: number, index: number) => {
            ListItem() {
              Column({ space: 10 }) {
                Row() {
                  Text(item.toString());
                  Button(this.isContentShow[index] ? '收起' : '展开')
                    .onClick(() => {
                      this.context.animateTo({
                        // 设置按钮收起展开动画效果
                        duration: 300,
                        onFinish: () => {
                          console.info('animation end');
                        }
                      }, () => {
                        this.isContentShow[index] = !this.isContentShow[index];
                      });
                    });
                }
                .padding({ left: 16, right: 16 })
                .width('100%')
                .justifyContent(FlexAlign.SpaceBetween);

                if (this.isContentShow[index]) { // 判断当前按钮为“收起”显示内容区域
                  Text('这是内容区域')
                    .backgroundColor('#33000000')
                    .textAlign(TextAlign.Center)
                    .width('100%')
                    .height(100);
                }
              }
              .backgroundColor('#FFFFFF')
              .width('100%')
              .padding({
                top: 12,
                bottom: 12
              })
              .margin({ top: 10 })
              .borderRadius(10);
            };
          }, (item: string) => item.toString());
        }
        .scrollBar(BarState.Off)
        .height('100%')
        .width('100%');
      }
      .backgroundColor('#F1F3F5')
      .padding(12);
    }
  }
  ```
