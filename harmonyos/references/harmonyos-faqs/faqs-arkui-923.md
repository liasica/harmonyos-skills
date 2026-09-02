---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-923
title: 如何解决给Image组件设置resizable在不同设备上显示不一致问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何解决给Image组件设置resizable在不同设备上显示不一致问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:20+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8b7bb60cd91ccc011da2680bee60a4a0a054bc2df389e7a313da3eb92142e571
---

## 问题现象

使用resizable设置top、right、bottom、left，单位是vp，在PC设备和手机设备上箭头拉伸效果存在差异。

问题代码如下：

```ts
@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  build() {
    RelativeContainer() {
      Image($r('app.media.test')) // 运行时需替换为实际的资源文件
        .width(300)
        .height(200)
        .resizable({
          slice: {
            top: this.getUIContext().px2vp(84),
            bottom: this.getUIContext().px2vp(38),
            left: this.getUIContext().px2vp(10),
            right: this.getUIContext().px2vp(28)
          }
        })
    }
    .height('100%')
    .width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/cI5JzUpARCa86dwQDnpovA/zh-cn_image_0000002658799569.png "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/t-q03u4fSsaXtbuSMs-7BQ/zh-cn_image_0000002628560216.png "点击放大")

## 背景知识

* 设置[EdgeWidths](../harmonyos-references/ts-types.md#edgewidths9)对象中的，传入数字时默认为[VP](../harmonyos-references/ts-types.md#vp10)单位，但在不同设备上[VP](../harmonyos-references/ts-types.md#vp10)单位会被解析成不同大小的[PX](../harmonyos-references/ts-types.md#px10)单位。
* 屏幕像素单位：px。屏幕上的实际像素，1px代表手机屏幕上的一个像素点。
* 虚拟像素单位：vp。屏幕密度相关像素，根据屏幕像素密度转换为屏幕物理像素，当数值不带单位时，默认单位vp。vp与px的比例与屏幕像素密度有关。

## 问题定位

问题代码中top、right、bottom、left设置的数值单位是vp，Image组件宽高数值单位也是vp，因为不同设备的像素密度不同，所以在不同设备上vp单位会被解析成不同大小的px单位。推测由于PC设备上聊天气泡单行文本组件最小高度小于气泡图片物理高度，导致图片显示被压缩。

## 分析结论

vp向px转换的系数是根据设备的像素密度决定的，但是气泡图片大小是真实的物理像素，当渲染的画布小于实际图片的大小时，图片在这个空间里就被压缩了。

## 修改建议

从当前设备环境考虑，PC设备应是应用运行的最低密度环境，气泡的最小高度应该是单行文本高度，在手机上单行文本高度是130，在PC上单行文本高度是76，而图片高度是123，因此在PC设备上会出现图片被压缩的现象。最优解决方案是更换背景图片，保证图片的高度要小于这个控件的最小物理高度，建议换一张高度小于76的气泡图片背景图。

## 常见FAQ

Q：用2in1的模拟器打印了单行组件高度是50px，把图片高度换成50px后显示正常没有被压缩，按照这个方式处理在物理设备上是否会有压缩问题？

A：要保证气泡高度小于物理设备上组件的高度，正常情况下是不会有压缩问题的。
