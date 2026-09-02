---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-753
title: px2vp单位转换方法及常见问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > px2vp单位转换方法及常见问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:03+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:9d5783e09d08a44da176fc0387d0a434c89a0d09c6638b0e11b592f0f61eb038
---

## 问题现象

在使用px单位进行UI开发时，发现不同设备上实际显示尺寸与设计稿预期效果存在偏差。由于px是物理像素的绝对单位，而不同设备的屏幕像素密度（DPI）不同，导致固定px值的元素在高密度屏幕上显示过小，在低密度屏幕上显示过大。

例如：设计稿在320DPI手机上是30px的按钮，到480DPI的同尺寸手机上，30px的按钮实际显示会小很多。那么将设计稿中的px尺寸转换为HarmonyOS系统vp（虚拟像素）单位，是否有通用的转换公式？

## 背景知识

像素单位：ArkUI为开发者提供4种像素单位，采用**vp为基准数据单位**。

| 名称 | 描述 |
| --- | --- |
| px | 屏幕物理像素单位。 |
| vp | 屏幕密度相关像素，根据屏幕像素密度转换为屏幕物理像素，当数值不带单位时，默认单位vp。说明：vp与px的比例与屏幕像素密度有关。 |
| fp | 字体像素，与vp类似适用屏幕密度变化，随系统字体大小设置变化。 |
| lpx | 视窗逻辑像素单位，lpx单位为实际屏幕宽度与逻辑宽度（通过designWidth配置）的比值，designWidth默认值为720。当designWidth为720时，在实际宽度为1440物理像素的屏幕上，1lpx为2px大小。 |

## 解决方案

* vp是HarmonyOS的长度单位，它转换跟设备的屏幕像素密度有关。**vp具体计算公式为：vp=px/(DPI/160)**。在实际宽度为1440px的屏幕上，1vp约等于3px。
* 使用getUIContext获取UIContext实例，再使用UIContext下的vp2px/px2vp/fp2px/px2fp/lpx2px/px2lpx调用绑定实例的接口。
* 下文将举例比较“220默认值”、“220px”、“220vp”、“vp2px220px”和“px2vp220vp”的宽度区别。本代码涉及详细接口请见：[vp2px](../harmonyos-references/arkts-apis-uicontext-uicontext.md#vp2px12)等像素转换方法。

示例代码如下：

```ts
@Entry
@Component
struct Example {
  build() {
    Column() {
      Flex({ wrap: FlexWrap.Wrap }) {
        Column() {
          Text('width(220)')
            .width(220)
            .height(40)
            .backgroundColor('#f1f3f5')
            .textAlign(TextAlign.Center)
            .fontColor(Color.Black)
            .fontSize('12vp');
        }.margin(5);

        Column() {
          Text('width(\'220px\')')
            .width('220px')
            .height(40)
            .backgroundColor('#f1f3f5')
            .textAlign(TextAlign.Center)
            .fontColor(Color.Black);
        }.margin(5);

        Column() {
          Text('width(\'220vp\')')
            .width('220vp')
            .height(40)
            .backgroundColor('#f1f3f5')
            .textAlign(TextAlign.Center)
            .fontColor(Color.Black)
            .fontSize('12vp');
        }.margin(5);

        Column() {
          Text('width(vp2px(220)')
            .width(this.getUIContext().px2vp(220) + 'px')
            .height(40)
            .backgroundColor('#f1f3f5')
            .textAlign(TextAlign.Center)
            .fontColor(Color.Black)
            .fontSize('7vp')
        }.margin(5);

        Column() {
          Text('width(px2vp(220))')
            .width(this.getUIContext().px2vp(220))
            .height(40)
            .backgroundColor('#f1f3f5')
            .textAlign(TextAlign.Center)
            .fontColor(Color.Black)
            .fontSize('12fp');
        }.margin(5);
      }.width('100%');
    }
    .margin({ top: 200, left: 30 });
  }
}
```

运行结果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/uPT0QkY-Sa6HeOI9iTjbGw/zh-cn_image_0000002684241043.png "点击放大")

## 常见FAQ

Q：既然推荐使用vp，那lpx和designWidth有什么用？

A：vp和lpx在ArkUI中分工明确，vp解决屏幕密度差异问题，保证物理尺寸一致性，lpx解决屏幕尺寸差异问题，保证布局比例一致性。二者缺一不可：仅用vp会导致大屏布局比例失衡（如元素过小），仅用lpx会失去物理尺寸稳定性（如触控区域不一致）。

* vp的价值：同一按钮在6英寸手机和10英寸平板上触控区域物理大小一致（如1cm²），避免高密度屏显示过小。
* lpx+designWidth的价值：设计稿中占满宽度的元素（如720lpx），通过designWidth映射到任意屏幕宽度（如手机720p→占满，平板1440px→仍占满），实现“一次设计，全端等比适配”。

Q：HarmonyOS的vp单位与其他平台的dp有什么联系？

A：HarmonyOS定义的vp和fp，可以直接参照其他平台使用的dp、sp的场景，与之对应起来理解和开发即可。简单来说，涉及尺寸时用vp、dp，涉及字体时用fp、sp。

Q：HarmonyOS中虚拟像素（vp）与物理像素（px）的换算关系是怎样的？

A：可参考[vp2px](../harmonyos-references/arkts-apis-uicontext-uicontext.md#vp2px12)接口下方的说明，px值=vp值×像素密度。

Q：为什么px2lpx会在折叠屏折叠状态和非折叠状态返回值不一致？

A：在折叠设备中，屏幕的物理宽度和分辨率会随着设备的折叠状态（折叠态或非折叠态）而改变。由于lpx的计算基于实际屏幕宽度与逻辑宽度的比值，因此当屏幕宽度变化时，px和lpx之间的转换比例也会随之改变。

Q：windowSizeChange回调返回的size单位是px，如何转换为vp单位？

A：推荐在[windowSizeChange](../harmonyos-references/arkts-apis-window-window.md#onwindowsizechange7)回调中直接使用UIContext的[px2vp](../harmonyos-references/arkts-apis-uicontext-uicontext.md#px2vp12)接口将px值转换为vp值。通过getUIContext()获取UIContext实例后调用px2vp，该接口会绑定当前屏幕上下文，确保转换结果正确且实时，无需手动获取densityPixels或单独监听像素密度变化。不建议使用全局的px2vp/vp2px（已标记废弃），也不建议手动用densityPixels做除法，因为densityPixels可能受系统缩放影响，且需要额外监听display.on('change')，增加复杂度。
