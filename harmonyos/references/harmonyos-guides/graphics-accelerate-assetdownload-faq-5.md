---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-assetdownload-faq-5
title: 如何解析华为CDN场景下manifestUrl对应的xml文件？
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > Graphics Accelerate Kit常见问题 > 游戏资源加速服务 > 如何解析华为CDN场景下manifestUrl对应的xml文件？
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:47+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3ead15f37e1060be1621efb970098dd18ced5b97af38291bc4774c9a243517a6
---

推荐使用[@ifbear/fast-xml-parser](https://ohpm.openharmony.cn/#/cn/detail/@ifbear%2Ffast-xml-parser)。

执行如下命令行，安装依赖。

```
1. To use as package dependency $ ohpm install @ifbear/fast-xml-parser
```

示例代码：

```
1. const { XMLParser, XMLBuilder, XMLValidator} = require("fast-xml-parser");

3. const parser = new XMLParser();
4. let jObj = parser.parse(XMLdata);
```
