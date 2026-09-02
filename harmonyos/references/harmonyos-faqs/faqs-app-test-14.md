---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-14
title: Hypium框架中的BY.XPath指令为何获取不到控件
breadcrumb: FAQ > DevEco Studio > 应用测试 > Hypium框架中的BY.XPath指令为何获取不到控件
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:36+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:1ea52c2232cc40ab3c110170248aa1a597b306521907453ed5b2119e04381ae8
---

## 问题现象

在使用[DevEco Testing Hypium](../harmonyos-guides/hypium-python-guidelines.md#section16890204264419)框架时，通过BY.xpath来点击详情按钮，报错控件获取失败。代码如下：

问题代码示例参考如下：

```python
component = driver.touch(BY.xpath("/root/Navigation/NavBar/NavBarContent/NavRouter/Stack/Column/List/ListItem[5]/Column/Column/Row/Row[2]/SymbolGlyph"))
```

工程组件结构如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/4sSKvQSTQ36BVvqePBpGaw/zh-cn_image_0000002658928757.png "点击放大")

## 背景知识

* [API使用方法](../harmonyos-guides/hypium-python-guidelines.md#section4598236435)：
  + 控件查看：可使用DevEco Testing Hypium插件中的UiViewer工具查看控件的各种属性。
  + 控件查找：Hypium中的定位操作目标的方式主要分三大类型，包括控件属性定位，图片匹配定位以及比例坐标定位。根据操作目标的定位准确性，首选方式为控件属性定位，次选图片匹配定位。当无法使用前两类方式定位时，可以选择比例坐标定位操作目标。其中控件属性定位通过BY选择器对象来实现。
* BY.xpath使用要点：

  **说明** 

  XPath不能和其他匹配器一起使用，且通过XPath查找控件相对较慢。

## 问题定位

从图中能够看到脚本里混用了BY.type和BY.xpath匹配器，违反了XPath选择器的使用限制。

## 分析结论

测试脚本里BY.xpath与BY.type匹配器混用导致BY.xpath匹配器失效。

## 修改建议

将测试脚本里的BY选择器都统一为BY.xpath或者将脚本中的BY.xpath换成其他的BY选择器。
