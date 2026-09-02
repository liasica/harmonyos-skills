---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-previewer-arkui
title: 查看ArkUI预览效果
breadcrumb: 指南 > 编写与调试应用 > 界面预览 > 查看ArkUI预览效果
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:30ed840fbf63dd826cbf3fccf8e48cd090f061c39719fd60b32cc477b434421b
---

ArkUI预览支持页面预览、组件预览、多断点预览和卡片预览，下图中左侧图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/48oVMaf8RdubSELHyAPlGA/zh-cn_image_0000002701823670.png)为页面预览，中间图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/WUnKUuHaT9-m77Vd1G2edg/zh-cn_image_0000002701663744.png)为组件预览，右侧图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/TxlNrM-uQeG0af_U3dXCdg/zh-cn_image_0000002701823666.png)为多断点预览，卡片预览在创建卡片文件后可直接预览。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/4FuFRa_GSSmOT8YIu4sHBw/zh-cn_image_0000002701823668.png)

## 页面预览

ArkTS应用/元服务支持页面预览。页面预览通过在工程的ets文件头部添加@Entry实现。

@Entry的使用参考如下示例：

```ts
@Entry
@Component
struct Index {
  @State message: string = 'Hello World'

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

## 组件预览

ArkTS应用/元服务支持组件预览。组件预览支持实时预览，不支持动态图和动态预览。组件预览通过在组件前添加注解@Preview实现，在单个源文件中，最多可以使用10个@Preview装饰自定义组件。

@Preview的使用参考如下示例：

```ts
@Preview({
  title: 'ContentTable'
})
@Component
struct ContentTablePreview {
  build() {
    Flex() {
      ContentTable({ foodItem: getDefaultFoodData() })
    }
  }
}
```

以上示例的组件预览效果如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/tZo03B0GRf6g4WSiNizC5Q/zh-cn_image_0000002701663746.gif "点击放大")

组件预览默认的预览设备为Phone，若您想查看不同的设备，或者不同的屏幕形状，或者不同设备语言等情况下的组件预览效果，可以通过设置@Preview的参数，指定预览设备的相关属性。若不设置@Preview的参数，默认的设备属性如下所示：

```ts
@Preview({
  title: 'Component1',  //预览组件的名称
  deviceType: 'phone',  //指定当前组件预览渲染的设备类型，默认为Phone
  width: 1080,  //预览设备的宽度，单位：px
  height: 2340,  //预览设备的长度，单位：px
  colorMode: 'light',  //显示的亮暗模式，当前支持取值为light
  dpi: 480,  //预览设备的屏幕DPI值
  locale: 'zh_CN',  //预览设备的语言，如zh_CN、en_US等
  orientation: 'portrait',  //预览设备的横竖屏状态，取值为portrait或landscape
  roundScreen: false  //设备的屏幕形状是否为圆形
})
```

请注意，如果被预览的组件是依赖参数注入的组件，建议的预览方式是：定义一个组件片段，在该片段中声明将要预览的组件，以及该组件依赖的入参，并在组件片段上标注@Preview注解，以表明将预览该片段中的内容。例如，要预览如下组件：

```ts
@Component
struct Title {
  @Prop context: string; 
  build() {
    Text(this.context)
  }
}
```

建议按如下方式预览：

```ts
@Preview
@Component    //定义组件片段TitlePreview
struct TitlePreview {
  build() {
    Title({ context: 'MyTitle' })    //在该片段中声明将要预览的组件Title，以及该组件依赖的入参 {context: 'MyTitle'}
  }
}
```

## 多断点预览

从26.0.0版本开始，ArkTS应用/元服务支持多断点预览，可以同时展示8个典型档位[断点](../best-practices/bpta-multi-device-responsive-layout.md#section1532120147301)的预览画面。在多断点预览模式下，不支持实时预览和极速预览；如果图片太大或图片太多，预览时可能无法显示。

多断点预览通过在工程的ets文件头部添加@Entry实现，示例如下：

```ts
@Entry
@Component
struct Index {
  @State message: string = 'Hello World'

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

以上示例的多断点预览效果如下图所示，会展示8个典型档位断点下的预览效果：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/l7IhmGX6StmJ8-mqtZX9IQ/zh-cn_image_0000002701823664.gif "点击放大")

每个断点预览画面上均可点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/NniN-VlERKe-iPjzilZ0vw/zh-cn_image_0000002701823662.png)查看该断点档位下的组件树。

支持代码编辑器、UI界面和组件树三者之间的联动：

* 选中预览器UI界面中的组件，则组件树上对应的组件将被选中，同时代码编辑器中的布局文件中对应的代码块高亮显示。
* 选中布局文件中的代码块，则在UI界面会高亮显示，组件树上的组件节点也会呈现被选中的状态。
* 选中组件树中的组件，则对应的代码块和UI界面也会高亮显示。
* 不支持修改属性面板上的组件属性。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/Qrc_fJlJQX6Dz8NIdmqBtA/zh-cn_image_0000002701663740.gif "点击放大")

## 卡片预览

创建卡片并选中卡片文件后，点击右侧边栏**Previewer**按钮即可预览卡片。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/Xl1ae4n8TYe9jz2Lu58opg/zh-cn_image_0000002701663742.png "点击放大")
