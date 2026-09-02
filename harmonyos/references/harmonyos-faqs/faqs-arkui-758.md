---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-758
title: List实现树视图
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > List实现树视图
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:22+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:15db4fab1e8e6dbb1ce8901392baee5839bfb89a6ec31d1c56e437cdca171cab
---

## 问题现象

列表如何实现树视图折叠交互，并支持展开/折叠父项查看子项？示例图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/xCZdCvrgQy6jVjz_wAZIdg/zh-cn_image_0000002658795051.png "点击放大")

## 背景知识

[List](../harmonyos-references/ts-container-list.md)列表是一种容器组件，包含一系列相同宽度的列表项，[ListItem](../harmonyos-references/ts-container-listitem.md)是构成列表的基础单位，用来展示列表具体内容。

## 解决方案

* **方案一**：
  1. 通过List与ListItem搭建标准化垂直列表架构，每个列表项均作为独立单元参与布局。
  2. 借助[Column](../harmonyos-references/ts-container-column.md)实现列表项内的纵向层级堆叠。

  ```screen
  @Entry
  @Component
  struct ListTest {
    private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
    @State isContentShow: boolean = true;
    @State selectItem: number = 0;
    uiContext: UIContext | undefined = undefined;

    aboutToAppear() {
      this.uiContext = this.getUIContext();
      if (!this.uiContext) {
        console.warn('no uiContext');
        return;
      }
    }

    build() {
      Column() {
        List({ initialIndex: 0 }) {
          ForEach(this.arr, (item: number, index: number) => {
            ListItem() {
              Column() {
                Row() {
                  Text(item.toString());
                  Button(this.isContentShow && this.selectItem === item ? '收起' : '展开')
                    .onClick(() => {
                      console.info('index', index);
                      this.uiContext?.animateTo({
                        duration: 300,
                        onFinish: () => {
                          console.info('animation end');
                        }
                      }, () => {
                        this.isContentShow = !this.isContentShow;
                        this.selectItem = item;
                      });
                    });
                }
                .width('100%')
                .justifyContent(FlexAlign.SpaceBetween);

                if (this.isContentShow && this.selectItem === item) {
                  Text('这是内容区域')
                    .backgroundColor(Color.Gray)
                    .width('100%')
                    .height(100);
                }
              }
              .backgroundColor(0xFFFFFF)
              .width('100%')
              .padding({
                top: 12,
                bottom: 12
              })
              .margin({ top: 10 });
            };
          }, (item: string) => item.toString());
        }
        .scrollBar(BarState.Off)
        .height('100%')
        .width('100%');
      }
      .backgroundColor(0xF1F3F5)
      .padding(12);
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/kNbgKl7WQb6x_aYvFla_Qg/zh-cn_image_0000002628555684.png "点击放大")
* **方案二**：

  参考[TreeView](../harmonyos-references/ohos-arkui-advanced-treeview.md)，作为一种分层显示的列表，适合显示嵌套结构。拥有父列表项和子列表项，可展开或折叠。

  ```screen
  import { TreeController, TreeView } from '@kit.ArkUI';

  @Entry
  @Component
  struct Index {
    private treeController: TreeController = new TreeController();
    clickId: number = 0;

    aboutToAppear(): void {
      this.treeController
        .addNode({
          parentNodeId: -1,
          currentNodeId: 1,
          isFolder: true,
          primaryTitle: '目录1',
          secondaryTitle: '2'
        })
        .addNode({
          parentNodeId: 1,
          currentNodeId: 2,
          isFolder: false,
          primaryTitle: '项目1_1'
        })
        .addNode({
          parentNodeId: 1,
          currentNodeId: 3,
          isFolder: false,
          primaryTitle: '项目1_2'
        })
        .addNode({
          parentNodeId: -1,
          currentNodeId: 24,
          isFolder: false,
          primaryTitle: '项目2'
        })
        .addNode({
          parentNodeId: -1,
          currentNodeId: 32,
          isFolder: true,
          primaryTitle: '目录3',
          secondaryTitle: '0'
        })
        .addNode({
          parentNodeId: 32,
          currentNodeId: 35,
          isFolder: true,
          primaryTitle: '目录3-1',
          secondaryTitle: '0'
        })
        .addNode({
          parentNodeId: -1,
          currentNodeId: 33,
          isFolder: true,
          primaryTitle: '目录4',
          secondaryTitle: '0'
        })
        .addNode({
          parentNodeId: 33,
          currentNodeId: 34,
          isFolder: false,
          primaryTitle: '项目5'
        })
        .buildDone();
      this.treeController.refreshNode(-1, '父节点', '子节点');
    }

    build() {
      Column() {
        SideBarContainer(SideBarContainerType.Embed) {
          TreeView({ treeController: this.treeController });
        }
        .sideBarWidth('100%')
        .focusable(true)
        .showControlButton(false)
        .showSideBar(true);
      };
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/IGMME5YXQx2ICj_jtKGMVA/zh-cn_image_0000002658915007.gif "点击放大")
