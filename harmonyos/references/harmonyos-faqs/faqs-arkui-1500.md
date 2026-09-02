---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1500
title: 首页数据加载慢导致页面布局波动
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 首页数据加载慢导致页面布局波动
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:15+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ce4ebda9ff9b3364e5291eac175d34e2a65bb1c64f78b2a35c6450c0813630fc
---

## 问题现象

启动应用后，页面居中显示默认图片，间隔一小段时间后突然出现数字列表，图片上移，页面内容跳变。

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/tYcLpYkCQ0KKEIKIEo9hvQ/zh-cn_image_0000002628606546.png "点击放大")

## 背景知识

* [List](../harmonyos-references/ts-container-list.md)：列表包含一系列相同宽度的列表项。适合连续、多行呈现同类数据，例如图片和文本。
* [Swiper](../harmonyos-references/ts-container-swiper.md)：滑块视图容器，提供子组件滑动轮播显示的能力。
* [height](../harmonyos-references/ts-universal-attributes-size.md#height)：设置组件自身的高度，缺省时使用元素自身内容需要的高度。

## 问题定位

1. 通过DevEco Testing的UIView工具查看页面UI结构。页面中使用了List组件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/io2b5SeJRrmIG_3ofCbhOA/zh-cn_image_0000002658845795.png "点击放大")
2. 筛选http以及http\_exec相关的日志，确认日志中链接是页面中显示的数据（图片、文本等）来源，且网络请求耗时较长。

   ```txt
   07-09 16:39:01.782   C015B0/xxxx/NETSTACK: [http_exec.cpp:499] taskid=-2147483551, size:90050, dns:4.813, connect:42.008, tls:54.322, firstSend:0.347, firstRecv:1537.666, total:1640.032...
   07-09 16:39:01.997   A03D00/JSAPP    I    url：https://xxx.xxxx.com/xxx
   ```
3. 当不设置容器高度，则容器高度取决于子组件高度。当网络内容还未加载出来时，容器高度是0，其他非网络数据组件就会保持原有大小。当数据加载成功后，容器组件高度变化，造成页面部分区域内容闪烁。问题示例代码如下，其中使用setTimeout模拟网络数据加载慢：

   ```ts
   @Entry
   @Component
   struct Index {
     @State data: Array<number> = []

     onPageShow(): void {
       // 使用setTimeout模拟网络数据加载慢
       setTimeout(() => {
         this.data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
       }, 2000)
     }

     build() {
       Column() {
         Image($r('app.media.startIcon'))
           .height(50)
           .width(50)
         Image($r('app.media.startIcon'))
           .height(50)
           .width(50)
         List({ space: 10 }) {
           ForEach(this.data, (item: number) => {
             ListItem() {
               Text(item.toString())
                 .height(30)
             }
           })
         }
         .alignListItem(ListItemAlign.Center)

       }
       .alignItems(HorizontalAlign.Center)
       .justifyContent(FlexAlign.Center)
       .height('100%')
     }
   }
   ```

## 分析结论

由于网络加载时延，导致数据产生不及时，所需数据的组件高度为零，后续数据加载成功后，组件高度发生变化，导致界面布局突变。

## 修改建议

优化数据加载时的显示效果。可以参考以下方案：

* 使用骨架屏效果，参考[LazyForEach实现骨架屏预加载效果](faqs-arkui-705.md)。
* 通过height属性预先设置容器高度，防止因容器高度变动导致的页面布局波动。
* 添加显隐判断，当数据加载成功后再显示页面。
