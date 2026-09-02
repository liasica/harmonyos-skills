---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1293
title: Text组件显示转义字符异常
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > Text组件显示转义字符异常
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:22+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:dacdf024c566498a7619b785a2913d4d47e4409977c545ca81a2e7f9376d2eaa
---

## 问题现象

从后端服务器返回的带有转义字符（如‘\n’和‘\r’分别代表换行和回车）的字符串，使用Text组件展示时，未能按照预计进行换行。

问题代码示例参考如下：

```ts
@Entry
@Component
struct TextIndex1 {
  private message: string = '1.个人VIP会员仅支持观看全部同步课程； \\n' +
    '2.开通个人装扮等';

  build() {
    Column() {
      Text(this.message);
    }
    .margin({ left: '16px', right: '16px' });
  }
}
```

问题效果预览：

例子中‘\n’并未实现换行：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/r746AjwTSn2nxbAI7o_CqA/zh-cn_image_0000002628597978.png "点击放大")

## 背景知识

[Text](../harmonyos-references/ts-basic-components-text.md)组件是HarmonyOS中用于显示文本的组件，支持多种属性设置，包括但不限于字体大小、颜色、对齐方式、断行规则等，用于实现所需的展示效果。

## 问题定位

1. 确认数据样本放在本地是否可以正常换行。
2. 此类问题多是后台返回的数据有问题，通常后台返回这种‘\n’类型的字符时会添加转义符。

## 分析结论

转义字符解析后缺少了去转义的步骤。

## 修改建议

对后台返回的数据进行去转义处理。以问题代码为例，从后端服务器返回的数据在‘\n’前添加了转义符‘\’，需要剔除冗余转义符‘\’。

```ts
@Entry
@Component
struct TextIndex2 {
  private message: string = '1.个人VIP会员仅支持观看全部同步课程；\\n' +
    '2.开通个人装扮等';

  build() {
    Column({ space: 10 }) {
      Text(this.message.replace('\\n', '\n'));
    }
    .margin({ top: 30 })
    .width('100%')
    .alignItems(HorizontalAlign.Center);
  }
}
```
