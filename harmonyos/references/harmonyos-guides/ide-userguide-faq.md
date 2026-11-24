---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-userguide-faq
title: 常见问题
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 常见问题
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:22+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:85a59a52a50cfb53c5d988fd30753c414174698b376237ece5986a0929409824
---

## 批量导入和批量移除so库后，工程同步时提示"Unable to load external compile\_commands.json”

**问题现象**

导入外部工程源码后，工程同步过程弹出“无效的JSON”报错。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/C6flOeP4QfS0VPGpSinIeA/zh-cn_image_0000002779406778.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=79205BEF4EC42E7BFF47E41BC9E0E3D5E3E1CA1F3C10D29359DBE6CF70445F51)

**可能原因**

compile\_commands.json文件内容格式不正确，不是有效的json文件。

**解决措施**

检查build\_ohos下的compile\_commands.json，确保其内容符合JSON数组格式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/3wFoSHRaQWuatdr6Dg-YAg/zh-cn_image_0000002779566754.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=DB7AFE29E5F91F8FE3C7F492C12CB2E9800D62E6F1E7DA333164B1E78B58483E)
