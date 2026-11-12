---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-hds-tabs-fuzzy-style
title: 设置页签栏的模糊样式
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > 底部页签 > 设置页签栏的模糊样式
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:abe0733dae5c131fc342a46d5c3d815b8e8756e2ae58f16ccc90e9d5091aa2d7
---

## 场景介绍

从6.0.0(20)版本开始，新增支持设置页签栏的模糊样式。

[HdsTabs (底部页签)](../harmonyos-references/ui-design-hdstabs.md)容器组件扩展支持页签栏设置直接模糊和渐变模糊效果。

* 直接模糊

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/bM619ohuSoGcZJpg3hQOrg/zh-cn_image_0000002786359614.png?HW-CC-KV=V1&HW-CC-Date=20261112T233236Z&HW-CC-Expire=31536000000&HW-CC-Sign=EFDE2D195A53755D42E1AE61FE41A0304F9FDEDF5F376B08D316F4456F7D767E)
* 渐变模糊

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/JFQ0eqtZRPC0AUuqD6gxqA/zh-cn_image_0000002815559035.jpg?HW-CC-KV=V1&HW-CC-Date=20261112T233236Z&HW-CC-Expire=31536000000&HW-CC-Sign=F0CDB9D22A30E154DE708D80CC5F9C0F784047268FE0C3B81CAD2877BE951DFB)

## 约束条件

1. 依赖页签栏位于容器底部，barPosition设置为BarPosition.End，vertical设置为false。
2. TabBar叠加在TabContent之上，barOverlap设置为true。
3. 去掉TabBar节点，barBackgroundBlurStyle默认设置的模糊的属性值为BlurStyle.NONE。

## 开发步骤

1. 导入相关模块。

   ```typescript
   // 从6.0.2(22)版本开始，无需手动导入HdsTabsAttribute。具体请参考HdsTabs的导入模块说明。
   import { HdsTabs, HdsTabsAttribute, HdsTabsController } from '@kit.UIDesignKit';
   ```
2. 创建Hds一级容器组件，设置HdsTabs组件的barBackgroundStyle样式，可以自定义模糊的颜色和高度，实现渐变模糊。

   **说明** 

   1. 当开发者通过Tabs组件属性barBackgroundBlurStyle设置模糊时，HdsTabs的默认模糊效果失效。
   2. 当开发者通过Tabs组件属性barBackgroundEffect设置模糊时，HdsTabs的默认模糊效果失效。
   3. 当开发者通过Tabs组件属性barBackgroundColor设置背景色时，HdsTabs的默认模糊效果只有模糊半径生效，模糊半径为80vp。

   ```typescript
   @Entry
   @Component
   struct Index {
     private controller: HdsTabsController = new HdsTabsController();

     build() {
       Column() {
         HdsTabs({ controller: this.controller }) {
           TabContent() {
             Column().width('100%').height('100%').backgroundColor(Color.Pink)
           }
           .tabBar({ icon: $r('app.media.startIcon'), text: '页签1' })

           TabContent() {
             Column().width('100%').height('100%').backgroundColor(Color.Blue)
           }
           .tabBar({ icon: $r('app.media.startIcon'), text: '页签2' })
         }
         .barOverlap(true)
         .barPosition(BarPosition.End)
         .vertical(false)
         .barBackgroundStyle({
           maskColor: Color.Yellow,
           maskHeight: 80
         })
       }
       .width('100%')
       .height('100%')
     }
   }
   ```
