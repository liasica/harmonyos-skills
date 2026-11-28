---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-userguide-faq
title: 常见问题
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 常见问题
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:29+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:be20a165034f56af316895fbc6f825a41fee0f19fd621238c2b1a1a1cf17f4e6
---

## 批量导入和批量移除so库后，工程同步时提示"Unable to load external compile\_commands.json”

**问题现象**

导入外部工程源码后，工程同步过程弹出“无效的JSON”报错。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/DebRnzpeToabt1TPhBQ1nA/zh-cn_image_0000002779406778.png?HW-CC-KV=V1&HW-CC-Date=20261128T023429Z&HW-CC-Expire=31536000000&HW-CC-Sign=FFF023060C3640EB7A038E76995F45B67C9618F61E16396E5FFE9552D9A11F28)

**可能原因**

compile\_commands.json文件内容格式不正确，不是有效的json文件。

**解决措施**

检查build\_ohos下的compile\_commands.json，确保其内容符合JSON数组格式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/a6kJDi_sT7KQfR4SdFM63Q/zh-cn_image_0000002779566754.png?HW-CC-KV=V1&HW-CC-Date=20261128T023429Z&HW-CC-Expire=31536000000&HW-CC-Sign=A0A676BFCCF1A16DEEB82207392301B799633E80337D638B471C774DEB80CBA5)
