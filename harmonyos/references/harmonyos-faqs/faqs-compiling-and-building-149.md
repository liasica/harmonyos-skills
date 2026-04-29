---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-149
title: 编译报错“The 'tag' keyword is not allowed for 'version' at 'xxx/oh-package.json5'”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“The 'tag' keyword is not allowed for 'version' at 'xxx/oh-package.json5'”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:56+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:926f0fb74cf207563dd33dae49233ba03602eb5d99fcb278ac41e138db9225ed
---

**错误描述**

oh-package.json5文件中的version字段不能包含tag标签。

**可能原因**

使用parameterFile参数化配置版本号时，oh-package.json5文件中的version字段不能包含tag标签。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/5Zdw4K39TUOZHHiG3-sGNg/zh-cn_image_0000002229604173.png?HW-CC-KV=V1&HW-CC-Date=20260429T062054Z&HW-CC-Expire=86400&HW-CC-Sign=91CB31465519B252CFF1AB9AB3F78B84A52E7EB9C77FC1C3C6EB22E046C864EF)

**解决措施**

当oh-package.json5文件中的version字段引用parameterFile时，开发者不应使用tag标签。
