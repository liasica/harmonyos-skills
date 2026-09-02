---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1519
title: 如何使用List组件实现聊天列表功能
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何使用List组件实现聊天列表功能
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:48+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:88581098daffe6104c355e56343f1269ad7805f68ce8966ebbbdd622cbaf6f77
---

## 问题现象

聊天列表是即时通讯中比较重要的功能，如何使用List组件实现聊天列表功能？

## 背景知识

[List](../harmonyos-guides/arkts-layout-development-create-list.md)组件应用于多种场景，如商品展示、聊天页面、发票页面等。[@Watch](../harmonyos-guides/arkts-watch.md)应用于对状态变量的监听，如果需要关注某个状态变量的值是否改变，可以使用@Watch为状态变量设置回调函数。

## 解决方案

* **场景一**：**收到新数据时从底部开始显示**。
  + **实现原理：** 使用[@Watch](../harmonyos-guides/arkts-watch.md)监听数据源的变化，当数据源变化时，若List不在最底部显示，则将List自动滚到最底部。
  + **示例代码：**

    ```ts
    @Component
    struct Chat {
      // 这个列表代表聊天内容，每次发送和接收消息时，把聊天内容加入这个列表。当监听到列表发生变化时，执行函数scrollerBottom，把list滑动到最底部。
      @Prop @Watch('scrollerBottom') list: string[] = [];
      scroller: Scroller = new Scroller();

      scrollerBottom() {
        this.scroller.scrollEdge(Edge.Bottom);
      }

      build() {
        // initialIndex代表列表生成时，从第几个索引值开始展示，选择最后一个索引值，就实现了显示最底部的消息。scroller代表绑定滚动事件，配合List监听，实现发送和接收消息，都能滚动到最底部。
        List({ initialIndex: this.list.length - 1, scroller: this.scroller }) {
          ForEach(this.list, (item: string) => {
            ListItem() {
              Text(item)
                .width('100%')
                .margin(5)
                .textAlign(TextAlign.Center)
            }
          });
        }
        .width('100%')
        .height('100%');
      }
    }

    @Entry
    @Component
    struct ListChat {
      @State message: string[] = [];
      count: number = 0;

      build() {
        Column(){
          Column() {
            Chat({ list: this.message })
              .width('90%')
              .borderRadius(12)
              .backgroundColor('#F1F3F5');
            Button('新增消息')
              .onClick(() => {
                this.message.push('新消息' + (this.count++).toString());
              })
              .width('90%')
              .margin({ top: 20 })
              .backgroundColor('#0A59F7');
          }
          .height('50%')
          .width('100%')
        }
        .justifyContent(FlexAlign.Center).height('100%')
        .alignItems(HorizontalAlign.Center);
      }
    }
    ```
  + **效果图：**

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/J-_5ct6UTX6zSbMg1ZTeng/zh-cn_image_0000002658846237.png "点击放大")
* **场景二**：**消息列表从底部开始加载，点击按钮回到最新位置**。
  + **实现原理：** 将List组件的[stackFromEnd](../harmonyos-references/ts-container-list.md#stackfromend19)属性设置为true可以实现列表从底部开始布局加载，给[scrollEdge](../harmonyos-references/ts-container-scroll.md#scrolledge)绑定List底部边界，实现跳转回到最新位置。

    **须知** 

    属性stackFromEnd从API version 19开始支持使用。
  + **示例代码：**

    ```ts
    @Entry
    @Component
    struct ListBottom {
      @State listContent: Array<string> = ['旧消息'];
      listScroller: ListScroller = new ListScroller();

      build() {
        Column() {
          List({ space: 10, scroller: this.listScroller }) {
            ForEach(this.listContent, (value: string) => {
              ListItem() {
                Text(value);
              }
              .width('90%')
              .height(200)
              .border({
                width: 0,
                radius: 20,
              })
              .backgroundColor(Color.White);
            });
          }
          .width('100%')
          .height('82%')
          .stackFromEnd(true) // 设置为true表示列表从底部开始布局
          .alignListItem(ListItemAlign.Center)
          .scrollBar(BarState.Off)

          Column() {
            Button('新增消息')
              .onClick(() => {
                this.listContent.push('新消息' + this.listContent.length.toString());
              })
              .width('100%')
              .margin({ top:8 ,bottom:5})

            Button('回到最新位置')
              .onClick(() => {
                this.listScroller.scrollEdge(Edge.Bottom); // 将列表滚动到底部边界位置
              })
              .width('100%')
              .margin({top:8,bottom:20})
          }
          .width('90%')
          .justifyContent(FlexAlign.SpaceAround);
        }
        .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM,SafeAreaEdge.TOP])
        .backgroundColor('#F1F3F5')
        .width('100%')
        .height('100%')
        .justifyContent(FlexAlign.SpaceBetween);
      }
    }
    ```
  + **效果图：**

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/sHiaTu25TnaS9EUBS-KNpQ/zh-cn_image_0000002628766878.png "点击放大")

## 常见FAQ

Q：如何解决插入图片发生闪烁问题？

A：可以使用syncLoad属性解决，具体可以参考[社区解决方案](https://developer.huawei.com/consumer/cn/blog/topic/03154617617506006)。
