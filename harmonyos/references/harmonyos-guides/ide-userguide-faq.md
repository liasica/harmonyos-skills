---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-userguide-faq
title: 常见问题
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 常见问题
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:54+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:3b89344b4074d8f22fcffb62f242409346b57a0feb09c1464bec2c5265e19bba
---

## 批量导入和批量移除so库后，工程同步时提示"Unable to load external compile\_commands.json”

**问题现象**

导入外部工程源码后，工程同步过程弹出“无效的JSON”报错。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/x4-NPXlFSOSG0wLaomOW3g/zh-cn_image_0000002779406778.png)

**可能原因**

compile\_commands.json文件内容格式不正确，不是有效的json文件。

**解决措施**

检查build\_ohos下的compile\_commands.json，确保其内容符合JSON数组格式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/GHfMxLrVR8O-nKPqEa6Ufg/zh-cn_image_0000002779566754.png)
