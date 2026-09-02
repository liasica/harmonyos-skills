---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-easygo-parallel
title: 平行视界
breadcrumb: 最佳实践 > 一次开发，多端部署 > 多设备界面开发 > 兼容方案 > 平行视界
category: best-practices
scraped_at: 2026-09-02T15:03:18+08:00
doc_updated_at: 2026-08-26
content_hash: sha256:096aaa42655598902f6ad44a7d2343f84ffbb820406a95faf03dfde8f9e1bf4f
---

## 概述

平行视界是针对应用在未适配[分栏布局](bpta-multi-device-page-layout.md#section11897247142110)的场景下，通过标准化配置实现宽屏、大屏设备分栏显示的系统级兼容方案。开启平行视界并分栏显示时，应用会在一个窗口中同时显示两个页面，默认情况下，两页按1:1平分窗口，如下图所示。从API版本23开始，支持开发者自配置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/w_kLZgkITxq3fke2zOwmBg/zh-cn_image_0000002693538162.jpg "点击放大")

平行视界适用于办公、邮箱、IM即时通讯、电商等需要频繁切换页面的应用。当前平行视界支持两种路由模式：导航模式和购物模式。以购物类应用在双折叠上运行为例：

* 导航模式：左侧主页（商品分类页）保持不变，右侧展示所选分类的商品或具体商品详情，后续相关操作均在右侧进行；
* 购物模式：页面路由跳转时右侧页面始终向左推入，屏幕右侧展示路由栈**栈顶页面**，左侧展示路由栈**次栈顶页面**。

| 路由模式 | 导航模式 | 购物模式 |
| --- | --- | --- |
| 效果图 |  |  |

本文面向中高级开发者，在开始学习之前，请完成以下前置操作：

1. 环境要求：安装最新版DevEco Studio，确保SDK版本不低于6.1.0(23)。
2. 知识储备：了解鸿蒙开发基础，掌握[分栏布局](bpta-multi-device-page-layout.md#section11897247142110)、[设置组件导航和页面路由](../harmonyos-guides/arkts-set-navigation-routing.md)等相关知识。

本文主要内容如下：

1. [开发步骤](bpta-easygo-parallel.md#section721050143619)：针对API 23及以上版本，详细介绍平行视界的完整适配流程。
2. [配置内容说明](bpta-easygo-parallel.md#section9181949173215)：深入讲解平行视界核心配置文件中各关键参数的含义、取值范围及配置规则，为开发者提供清晰、规范的配置指引。
3. [典型开发场景](bpta-easygo-parallel.md#section1356213482715)：以[Navigation](../harmonyos-references/ts-basic-components-navigation.md)路由实现的购物类应用为载体，围绕平行视界高频应用场景，提供可复用的场景化解决方案。
4. [常见问题](bpta-easygo-parallel.md#section4428734132210)：梳理平行视界开发中的高频问题，剖析问题产生的核心原因，并给出解决方案及避坑建议，帮助开发者高效解决实战中的各项问题。
5. [示例代码](bpta-easygo-parallel.md#section6283822152518)：提供可直接运行的项目代码，供开发者下载，结合本文内容配合使用。

## 开发步骤

1. 增加配置文件。

   在profile目录下创建兼容方案的配置文件easy\_go.json（示例文件名，可自行命名）。在[module.json5配置文件](../harmonyos-guides/module-configuration-file.md)中添加easyGo字段，并指向引用的easy\_go.json配置文件。当前仅支持在entry模块下配置，配置后应用级生效。如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/bHYa44egSy2UC0pXBmBiVg/zh-cn_image_0000002693698030.png "点击放大")
2. 在easy\_go.json配置文件中，配置平行视界的相关属性，详情可参考[配置内容说明](bpta-easygo-parallel.md#section9181949173215)。

## 配置内容说明

easy\_go.json是一个标准的Object类型JSON文件，整体结构分为两层。第一层配置设备类型；第二层配置对应设备类型下的显示模式。

### 设备类型

一层配置，设置平行视界在不同设备类型下的表现。

```json
{ 
  "common": {},
  "phone": {},
  "tablet": {}
}
```

| 字段名 | 说明 | 可选 | 字段类型 |
| --- | --- | --- | --- |
| common | 通用设备配置，为所有设备类型提供基础默认配置。 | 否 | displayModeOptions |
| phone | phone类型设备上生效的配置，配置后common配置在phone类型设备上不再生效。 | 是 | displayModeOptions |
| tablet | tablet类型设备上生效的配置，配置后common配置在tablet类型设备上不再生效。  **说明：**  自由多窗模式下，暂不支持平行视界。 | 是 | displayModeOptions |

### 显示模式

二层配置displayModeOptions字段，设置平行视界的显示模式，内部字段说明如下：

| 字段名 | 说明 | 可选 |
| --- | --- | --- |
| wideWindowMode | 控制应用在比直板机宽的长方形宽屏窗口（>= 600vp，宽/高 > 1.2）上的显示方式。 | 否 |
| squareWindowMode | 控制应用在比直板机宽的方形宽屏窗口（>= 600vp，高/宽 <= 1.2，宽/高 <= 1.2）上的显示方式。 | 是 |
| routerSplitOptions | 平行视界使用Router分栏时的配置。 | 是 |
| navigationSplitOptions | 平行视界使用Navigation分栏时的配置。 | 是 |

wideWindowMode/squareWindowMode内部字段说明：

| 字段名 | 说明 |
| --- | --- |
| navigationSplit | 代表应用路由由navigation组件实现，必须配合navigationSplitOptions字段一起使用。 |
| routerSplit | 代表应用路由由router模块实现，必须配合routerSplitOptions字段一起使用。 |
| original | 关闭窗口显示模式的兼容运行行为。 |

routerSplitOptions/navigationSplitOptions内部可包含的字段说明：

| 字段名 | 说明 | 数据类型 | 可选 |
| --- | --- | --- | --- |
| homePage | 主页名称，不配置时系统采用默认的策略进行主页识别。  **说明：**  对于Navigation路由，如果将NavDestination做为主页，则配置为NavDestination的name；如果将Navigation首页作为主页，则配置为"navBar"。建议将Navigation实际主页配置为homePage。  对于Router路由，配置为页面绝对路径，由配置文件中pages列表提供，例如"pages/Index"。 | 字符串 | 是 |
| relatedPage | 关联页名称，不配置时没有关联页能力。  **说明：**   * 内容的格式和homePage保持一致。 * 必须有homePage才能配置relatedPage。 * 不支持传递参数，建议配置无需动态参数的静态页面作为关联页。 | 字符串 | 是 |
| enableReducedContainerSize | 是否开启虚拟容器能力，默认值为false。  - false：lpx单位、页面中横向断点、窗口宽度尺寸及屏幕宽度尺寸将使用原始尺寸进行计算。  - true： lpx单位、页面中横向断点、窗口宽度尺寸及屏幕宽度尺寸均使用原始尺寸的缩小比例，按照右侧页面尺寸计算。  **说明：**   * 开启后在平行视界分栏时，整个应用内生效。 * 平行视界退出分栏时（如：进入全屏页）自动失效。 * 配置窗口分屏支持平行视界时，屏幕宽度尺寸将使用原始尺寸进行计算。 | 布尔值 | 是 |
| fullScreenPages | 支持全屏显示的页面数组，跳转到数组中的页面时，退出分栏显示。默认值为空数组。  **说明：**  数组中每一项内容的格式和homePage保持一致，且不能和homePage、relatedPage重复。 | 字符串数组 | 是 |
| supportLandscapeFullscreen | 应用主动请求横屏时是否全屏显示，默认值为true。  - true： 当应用主动请求横屏时，会退出分栏全屏显示。  - false： 当应用主动请求横屏时，仍然保持平行视界效果。 | 布尔值 | 是 |
| dialogSupportSplit | Dialog是否支持分栏显示，默认值为true。  - false：弹窗居中显示。  - true：弹窗在右半屏显示。 | 布尔值 | 是 |
| wideSplit | 比直板机宽的长方形窗口（>= 600vp，宽/高>1.2）上的配置参数，包含字段：ratio、isDraggable。  从API版本26.0.0开始，支持该标签。 | 对象 | 是 |
| squareSplit | 比直板机宽的方形窗口（>= 600vp，高/宽 <= 1.2，宽/高 <= 1.2）上的配置参数，包含字段：ratio、isDraggable。  从API版本26.0.0开始，支持该标签。 | 对象 | 是 |
| mode | 路由模式，类型为非空整数，默认值为1。  - 0：购物模式。  - 1：导航模式。  从API版本26.0.0开始，支持该标签。 | 数值 | 是 |
| pagePairs | 配置页面跳转关系对，仅在导航模式下生效。  数组中的每个对象是一个{from, to} 跳转关系对，用于配置从from页面跳转到to页面时触发分栏（from页面在左，to页面在右）。  从API版本26.0.0开始，支持该标签。 | 对象数组 | 是 |
| transPages | 过渡页面，在购物模式下生效，配置此标签的页面将固定在右侧显示，不支持右推左。默认值为空数组。  **说明：**  NavDestination类型为NavDestinationMode.DIALOG（可参考[NavDestinationMode枚举说明](../harmonyos-references/ts-basic-components-navdestination.md#navdestinationmode枚举说明11)）的页面，默认属于过渡页面。  数组中每一项内容的格式和homePage保持一致，且不能和homePage、relatedPage、fullScreenPages重复。  从API版本26.0.0开始，支持该标签。 | 字符串数组 | 是 |
| splitDividerColor | 分割线颜色，支持配置深浅色模式，包含可选字段：light和dark。  从API版本26.0.0开始，支持该标签。 | 对象 | 是 |
| drawableRectHook | [WindowProperties](../harmonyos-references/arkts-apis-window-i.md#windowproperties).drawableRect是否开启页面级容器能力，默认值为false  - false：Window.drawableRect将使用原始尺寸进行计算。  - true：Window.drawableRect将使用原始尺寸的缩小比例，按照右侧页面尺寸计算。  从API版本26.0.0开始，支持该标签。 | 布尔值 | 是 |
| enableInSplitScreen | 是否支持在窗口分屏场景进入平行视界，默认值为false。  - false：分屏时始终不进入平行视界。  - true：分屏时窗口宽高若满足条件则进入平行视界。  从API版本26.0.0开始，支持该标签。 | 布尔值 | 是 |

navigationSplitOptions中可额外包含如下几个字段：

| 字段名 | 说明 | 数据类型 | 可选 |
| --- | --- | --- | --- |
| homeNavigationId | 分栏Navigation的[id](../harmonyos-references/ts-universal-attributes-component-id.md#id)（组件通用属性），不配置时使用最外层Navigation进行分栏。  推荐开发者配置为做全局路由的Navigation的id，如果配置为其他Navigation，可能会导致布局异常。 | 字符串 | 是 |
| disablePlaceholder | 是否隐藏占位页，默认值为false。  - false：不隐藏占位页。  - true：隐藏占位页。 | 布尔值 | 是 |
| disableDivider | 是否隐藏分割线，默认值为false。  - false：不隐藏分割线。  - true：隐藏分割线。 | 布尔值 | 是 |

wideSplit/squareSplit内部字段说明：

| 字段名 | 说明 | 数据类型 | 可选 |
| --- | --- | --- | --- |
| ratio | 左右页面比例，数据格式为"正整数 | 正整数"，范围限制在1:2到2:1之间，未配置时默认为1:1，配置超出范围时默认为范围边界值。  从API版本26开始，支持该标签。 | 字符串 | 是 |
| isDraggable | 是否开启分栏拖拽功能，默认值为false。  - false：不开启分栏拖拽功能。  - true：开启分栏拖拽功能。开启后ratio字段失效，默认分栏比例为1:1，使用三档吸附，在1:2、1:1和2:1之间可以进行拖动。  从API版本26.0.0开始，支持该标签。 | 布尔值 | 是 |

pagePairs内部可以包含多对from和to字段，两个字段必须成对出现：

| 字段名 | 说明 | 数据类型 | 可选 |
| --- | --- | --- | --- |
| from | 触发分栏显示的源页面，格式和homePage保持一致。  从API版本26.0.0开始，支持该标签。 | 字符串 | 否 |
| to | 触发分栏显示的目的页面，格式和homePage保持一致，配置为"\*"表示任意页面。  从API版本26.0.0开始，支持该标签。 | 字符串 | 否 |

splitDividerColor内部字段说明：

| 字段名 | 说明 | 数据类型 | 可选 |
| --- | --- | --- | --- |
| light | 浅色模式颜色，类型为十六进制字符串，格式为#AARRGGBB。  从API版本26.0.0开始，支持该标签。 | 字符串 | 是 |
| dark | 深色模式颜色，类型为十六进制字符串，格式为#AARRGGBB。  从API版本26.0.0开始，支持该标签。 | 字符串 | 是 |

**说明** 

* routerSplitOptions和navigationSplitOptions不能同时存在。开启平行视界后，混用Router和Navigation会导致部分行为异常，因此不建议在启用平行视界的应用中混用两种路由框架。
* 分割线颜色默认支持深浅色模式。如果应用不适配深色模式，需要配置light和dark为相同颜色。

### 配置示例

1. Router路由下，为通用设备配置平行视界效果。
   * 通过common为通用设备配置平行视界效果。
   * 将wideWindowMode及squareWindowMode字段设置为"routerSplit"，代表应用路由由Router模块实现。
   * 配置routerSplitOptions字段，按需设置主页、关联页、全屏页等字段。

   ```json
   {
     "common": {
       "displayModeOptions": {
         "wideWindowMode": "routerSplit",
         "squareWindowMode": "routerSplit",
         "routerSplitOptions": {
           "homePage": "pages/Index",
           "relatedPage": "pages/CategoryPage",
           "fullScreenPages": [
             "pages/FullScreenImagePage"
           ],
           "supportLandscapeFullscreen": true,
           "enableReducedContainerSize": true
         }
       }
     }
   }
   ```
2. Navigation路由下，为通用设备配置平行视界效果。
   * 通过common为通用设备配置平行视界效果。
   * 将wideWindowMode及squareWindowMode字段设置为"navigationSplit"，代表应用路由由Navigation组件实现。
   * 配置navigationSplitOptions字段，按需设置主页、关联页、全屏页、路由模式等字段。在平板/三折叠等长方形窗口下设置左右屏幕比例为1：2，在双折叠等方形窗口下设置左右屏幕比例为1：1。

   ```json
   {
     "common": {
       "displayModeOptions": {
         "wideWindowMode": "navigationSplit",
         "squareWindowMode": "navigationSplit",
         "navigationSplitOptions": {
           "homePage": "navBar",
           "relatedPage": "CategoryPage",
           "fullScreenPages": [
             "FullScreenImagePage"
           ],
           "supportLandscapeFullscreen": true,
           "enableReducedContainerSize": true,
           "wideSplit": {
             "ratio": "1 | 2"
           },
           "squareSplit": {
             "ratio": "1 | 1"
           },
           "mode": 0,
           "splitDividerColor": {
             "light": "#33FFFFFF",
             "dark": "#33000000"
           },
           "drawableRectHook": true,
           "enableInSplitScreen": true
         }
       }
     }
   }
   ```
3. 以Navigation路由为例，为tablet设备单独关闭平行视界效果。
   * 增加tablet设备配置。
   * 将wideWindowMode、squareWindowMode字段设置为"original"，关闭窗口显示模式的兼容运行行为。

   ```json
   {
     "common": {
       "displayModeOptions": {
         "wideWindowMode": "navigationSplit",
         "squareWindowMode": "navigationSplit",
         "navigationSplitOptions": {
           "homePage": "CategoryPage",
           "fullScreenPages": [
             "FullScreenImagePage"
           ],
           "supportLandscapeFullscreen": true,
           "enableReducedContainerSize": false
         }
       }
     },
     "tablet": {
       "displayModeOptions": {
         "wideWindowMode": "original",
         "squareWindowMode": "original"
       }
     }
   }
   ```

## 典型开发场景

本章以Navigation路由实现的购物类应用为载体，介绍平行视界适配开发中的七个典型场景，并讲解如何通过easy\_go.json配置文件进行配置。

### 配置主页与关联页

**场景描述**

默认情况下，系统会将应用的某个页面识别为主页，但是该机制在有些场景下不能准确识别主页。建议开发者主动配置主页，需要的话，还可以配置关联页。

例如在购物类应用中，开发者可以将首页设置为主页，首个商品分类页设置为启动关联页。

| 场景 | 同时配置主页和关联页 | 只配置主页 |
| --- | --- | --- |
| 效果图 |  |  |

**实现原理**

平行视界提供配置主页及关联页能力。通过homePage属性设置主页，通过relatedPage属性设置关联页。

**开发步骤**

在easy\_go.json配置文件中，将homePage属性设置为"navBar"，表示将Navigation首页设置为主页。将relatedPage属性设置为"CategoryPage"，表示将分类页设置为关联页。具体配置文件如下：

```json
{
  "common": {
    "displayModeOptions": {
      "wideWindowMode": "navigationSplit",
      "squareWindowMode": "navigationSplit",
      "navigationSplitOptions": {
        "homePage": "navBar",
        "relatedPage": "CategoryPage"
      }
    }
  }
}
```

### 配置路由模式

**场景描述**

购物类应用中，用户浏览路径通常层层深入，即从商品分类进入商品列表进行筛选比较，最终进入商品详情页完成商品挑选。相比左侧主页保持不变的导航模式，在购物模式下，页面路由跳转时右侧页面始终向左推入，屏幕右侧展示路由栈栈顶页面，左侧展示路由栈次栈顶页面，更贴合“层层深入、随时回退”的浏览体验。如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/UgllZ2k2R9auTNDpcSl--Q/zh-cn_image_0000002723337523.gif "点击放大")

**实现原理**

从API版本26.0.0开始，平行视界支持通过mode字段设置路由模式。

**开发步骤**

在easy\_go.json配置文件中，将mode属性设置为0，表示将路由模式设置为购物模式。具体配置文件如下：

```json
{
  "common": {
    "displayModeOptions": {
      "wideWindowMode": "navigationSplit",
      "squareWindowMode": "navigationSplit",
      "navigationSplitOptions": {
        "homePage": "navBar",
        "relatedPage": "CategoryPage",
        "mode": 0
      }
    }
  }
}
```

### 设置过渡页面

**场景描述**

购物模式下，页面路由跳转时右侧页面始终向左推入，屏幕右侧展示路由栈栈顶页面，左侧展示路由栈次栈顶页面。但是由于某些页面（如地址编辑页）属于临时编辑操作，将此类页面固定在右侧显示，左侧分栏内容保持不变，交互体验更连贯。如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/DpgydxqPQe2M1x4QJA2s4w/zh-cn_image_0000002693698032.gif "点击放大")

**实现原理**

从API版本26.0.0开始，平行视界提供配置过渡页面能力。通过transPages属性设置过渡页。

**开发步骤**

在easy\_go.json配置文件的transPages字段中，加入地址编辑页面。具体配置文件如下：

```json
{
  "common": {
    "displayModeOptions": {
      ...
      "navigationSplitOptions": {
        "homePage": "navBar",
        "relatedPage": "CategoryPage",
        "mode": 0,
        "transPages": [
          "AddressEditPage"
        ]
      }
    }
  }
}
```

### 路由跳转过程请求全屏

**场景描述**

在商品详情页，为清晰呈现商品细节，点击商品图片后，需将图片全屏展示。如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/WcVm4Rd9QgigW6IGxOyn3w/zh-cn_image_0000002693538166.gif "点击放大")

**实现原理**

平行视界提供了全屏页能力，支持通过fullScreenPages字段指定全屏页。配置后，对应页面展示时，将暂时退出分栏模式，切换为全屏显示。页面隐藏时，恢复分栏显示。

**开发步骤**

在平行视界配置文件的fullScreenPages字段中，加入图片浏览页。

```json
{
  "common": {
    "displayModeOptions": {
      "navigationSplitOptions": {
        ...
        "fullScreenPages": [
          "FullScreenImagePage"
        ]
      }
    }
  }
}
```

### 路由跳转过程请求横屏显示

**场景描述**

在商品详情页中，“参数对比”、“配置表”类图片往往需要横屏展示，以解决竖屏模式下文字过小等问题。如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/C4mjOnIiR4y2y4KhF8aArg/zh-cn_image_0000002723217603.gif "点击放大")

**实现原理**

平行视界支持通过配置supportLandscapeFullscreen字段实现横屏时全屏显示页面。在easy\_go.json配置文件中配置该字段值为true后，当应用请求横屏时，会退出分栏，全屏展示页面。

**开发步骤**

在easy\_go.json配置文件中，将supportLandscapeFullscreen属性设置为true，配置后，当页面申请横屏时，将退出分栏模式，切换为全屏显示。

```json
{
  "common": {
    "displayModeOptions": {
      "navigationSplitOptions": {
        ...
        "supportLandscapeFullscreen": true
      }
    }
  }
}
```

### 开启虚拟容器能力

**场景描述**

在开启平行视界并分栏显示时，一个窗口内部会同时显示两个页面，两个页面默认按照1:1平分窗口大小。如果页面内的元素布局使用窗口宽度，可能会导致UI元素超出页面范围被截断，开发者可以开启虚拟容器能力，此时lpx单位、页面中横向断点、窗口宽度尺寸和屏幕宽度尺寸将使用原始尺寸的一半进行计算。

**开发步骤**

在easy\_go.json配置文件中，将enableReducedContainerSize属性设置为true，获取平行视界后的断点。

```json
{
  "common": {
    "displayModeOptions": {
      "navigationSplitOptions": {
        ...
        "enableReducedContainerSize": true
      }
    }
  }
}
```

### 平行视界场景下触发应用内分屏

**场景描述**

在平板或三折叠三屏态（G态）等大屏设备上，当应用已进入平行视界分栏显示（左侧主页、右侧商品详情页）时，若用户希望在浏览商品详情的同时，打开其他页面进行比价、查询物流等操作，可以在商品详情页顶部提供分屏入口。用户点击后以主窗口形式进入系统窗口分屏，并在分屏窗口中继续保持平行视界效果，实现一边浏览商品一边使用其他应用的多任务体验。如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/1lzvGVgVSNa_WWFYOYk6Tg/zh-cn_image_0000002723337525.gif "点击放大")

**实现原理**

默认情况下，平行视界在窗口分屏场景下不会生效。平行视界提供enableInSplitScreen字段，配置为true后，当应用进入窗口分屏时，若分屏窗口宽高满足条件，则继续保持平行视界分栏显示。

**开发步骤**

1. 在easy\_go.json配置文件中，将enableInSplitScreen属性设置为true。配置后，应用在窗口分屏场景下若宽高满足条件，将继续保持平行视界效果。

   ```json
   {
     "common": {
       "displayModeOptions": {
         "navigationSplitOptions": {
           ...
           "enableInSplitScreen": true
         }
       }
     }
   }
   ```
2. 在商品详情页顶部添加分屏按钮。通过[isEasySplit](../harmonyos-references/arkts-apis-uicontext-uicontext.md#iseasysplit24)()接口判断当前是否处于平行视界分栏态，通过[windowStatusType](../harmonyos-references/arkts-apis-window-e.md#windowstatustype11)判断是否已处于窗口分屏，仅在分栏态且未分屏时显示按钮。

   ```typescript
   Row() {
     Image($r('app.media.ic_split_screen'))
       .width(24)
       .height(24)
   }
   // ...
   .onClick(() => {
     this.startSplitScreen();
   })
   .visibility(this.mainWindowInfo.windowStatusType !== window.WindowStatusType.SPLIT_SCREEN &&
     this.getUIContext().isEasySplit() ? Visibility.Visible : Visibility.None)
   ```
3. 在按钮点击事件中，调用[startAbility](../harmonyos-references/js-apis-inner-application-appserviceextensioncontext.md#startability)()接口拉起应用新的实例，并指定窗口分屏模式及主窗口占比，使应用以主窗口形式进入系统分屏。

   ```typescript
   private startSplitScreen(): void {
     try {
       const context = this.getUIContext().getHostContext() as common.UIAbilityContext;
       context.startAbility({
         bundleName: CommonConstants.BUNDLE_NAME,
         abilityName: 'EntryAbility',
       }, {
         windowMode: AbilityConstant.WindowMode.WINDOW_MODE_SPLIT_PRIMARY,
         splitRatio: window.SplitRatioPreference.PRIMARY_DOMINANT
       }).then(() => {
         hilog.info(0x0000, 'testTag', 'Succeeded in starting split screen mode.');
       }).catch((err: BusinessError) => {
         hilog.error(0x0000, 'testTag', `Failed to start split screen mode. Code: ${err.code}, message: ${err.message}`);
       });
     } catch (error) {
       let err = error as BusinessError;
       hilog.error(0x0000, 'testTag', `Failed to start split screen mode. Code: ${err.code}, message: ${err.message}`);
     }
   }
   ```

## 常见问题

### UI元素超出页面范围，页面元素被截断

**问题描述**

开启平行视界并分栏显示时，页面内的元素超出页面范围，导致被截断，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/ovosN1riRMWmgUQzV7hZlQ/zh-cn_image_0000002693698036.png "点击放大")

**原因分析**

在开启平行视界并分栏显示时，一个窗口内部会同时显示两个页面，两个页面默认按照1:1平分窗口大小。如果页面内的元素布局使用窗口宽度，可能会导致UI元素超出页面范围。

**解决方案**

建议采取以下策略：

1. 优先使用系统组件的自适应布局能力：[自适应布局](bpta-multi-device-adaptive-layout.md)。
2. 开启虚拟容器能力，在平行视界配置文件中，将enableReducedContainerSize设置为true。此时，lpx单位、页面中横向断点、窗口宽度尺寸和屏幕宽度尺寸将使用原始尺寸的一半进行计算。
3. 使用页面大小获取接口和无感监听能力：

   [on('navDestinationUpdate')](../harmonyos-references/arkts-apis-uicontext-uiobserver.md#onnavdestinationupdate11)：监听[NavDestination](../harmonyos-references/ts-basic-components-navdestination.md)组件的状态变化，API 23版本及以上，返回的当前NavDestination组件状态中会包含NavDestination组件的大小。

   [on('routerPageUpdate')](../harmonyos-references/arkts-apis-uicontext-uiobserver.md#onrouterpageupdate11)： 监听Router中page页面的状态变化，API 23版本及以上，返回的当前Router页面的信息中会包含routerPage页面的大小。

   [onRouterPageSizeChange](../harmonyos-references/arkts-apis-uicontext-uiobserver.md#onrouterpagesizechange23)()： 当可见的Router页面大小发生变化时，会触发该回调函数。

   [onNavDestinationSizeChange](../harmonyos-references/arkts-apis-uicontext-uiobserver.md#onnavdestinationsizechange23)()：当可见的NavDestination大小发生变化时，会触发该回调函数。

### 组件复用场景下，同一资源只在一个页面中显示

**问题描述**

左右两个分栏页面中，同一资源只在一页面中显示，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/s28grHcZREexWkSWKzaqFQ/zh-cn_image_0000002693538168.gif "点击放大")

**原因分析**

如果左右两个分栏页面利用ArkUI的组件复用机制（例如：[NodeContainer](../harmonyos-references/ts-basic-components-nodecontainer.md)）共用了同一个UI资源，会导致对应的资源同一时刻只能在一个页面中显示。

**解决方案**

建议改为两边页面使用独立的UI资源，互不影响，详情请参考[自定义组件复用开发实践](../harmonyos-guides/arkts-component_reuse.md)。

### 使用页面级窗口策略不生效

**问题描述**

平行视界场景下，使用NavDestination组件提供的[preferredOrientation](../harmonyos-references/ts-basic-components-navdestination.md#preferredorientation19)属性设置页面方向时，未生效。

**原因分析**

平行视界场景下，会同时显示左右两个页面，两个页面方向需要一致。

**解决方案**

推荐使用窗口级方案，通过window提供的[setPreferredOrientation](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9)()接口设置窗口策略。

### 应用设置一镜到底等转场效果不生效

**问题描述**

平行视界场景下，应用设置的[一镜到底](../design-guides/transition-animation-0000001750078488.md#section76611627132514)等转场效果不生效。

**原因分析**

应用接入平行视界后，系统会屏蔽或修改部分场景动效。如：

1. Router类型的平行视界，系统会屏蔽所有自定义转场。
2. Navigation类型的平行视界，在主页首次跳转到二级页面或者二级页面返回到首页时，系统会屏蔽所有转场，默认无动画跳转；购物模式场景下，系统会屏蔽自定义转场，默认右推左或左推右实现平移转场。

**解决方案**

平行视界场景下，涉及到以上转场场景时，建议关闭自定义转场，遵循系统默认效果。

### 运行时无法仅通过配置预知运行平行视界分栏模式

**问题描述**

开发者在应用运行时需要判断当前是否处于平行视界分栏模式。

**原因分析**

平行视界的分栏模式由平行视界的配置和设备窗口形态共同决定，应用运行过程中，窗口大小变化、分屏等操作可能导致分栏模式切换，开发者无法仅通过静态配置预知运行时的分栏模式。

**解决方案**

通过UIContext提供的[isEasySplit](../harmonyos-references/arkts-apis-uicontext-uicontext.md#iseasysplit24)()接口在运行时查询。该接口从API版本24开始支持，返回boolean类型值：true表示处于分栏模式，false表示未处于分栏模式。

## 示例代码

[平行视界](https://gitcode.com/HarmonyOS_Samples/easygo-parallel-shopping)
