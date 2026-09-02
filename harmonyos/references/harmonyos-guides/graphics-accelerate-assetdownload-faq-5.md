---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-assetdownload-faq-5
title: 如何解析华为CDN场景下manifestUrl对应的xml文件
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > Graphics Accelerate Kit常见问题 > 游戏资源加速服务 > 如何解析华为CDN场景下manifestUrl对应的xml文件
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:22+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:64788b9c2e8978d8f970052350dd4a7f78d41ec99a11012cc025c61cdb225163
---

推荐使用[@ifbear/fast-xml-parser](https://ohpm.openharmony.cn/#/cn/detail/@ifbear%2Ffast-xml-parser)。

执行如下命令行，安装依赖。

```typescript
$ ohpm install @ifbear/fast-xml-parser
```

示例代码：

```typescript
import { XMLParser, XMLBuilder, XMLValidator } from "@ifbear/fast-xml-parser";

const parser = new XMLParser();
let jObj = parser.parse(XMLdata);
```
