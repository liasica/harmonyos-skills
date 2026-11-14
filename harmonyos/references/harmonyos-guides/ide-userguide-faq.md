---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-userguide-faq
title: 常见问题
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 常见问题
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:49+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:a73c222d7c2cd4ad45e13b15ed2972afee29ad54cc163cdf2c62a8694dcb2490
---

## 批量导入和批量移除so库后，工程同步时提示"Unable to load external compile\_commands.json”

**问题现象**

导入外部工程源码后，工程同步过程弹出“无效的JSON”报错。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/Czl-VhEJQambefYZH7eawQ/zh-cn_image_0000002779406778.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=C8AF75E73C26C913DE75F1260B2901CA65B912C30C4A7D7CD3256DD931666771)

**可能原因**

compile\_commands.json文件内容格式不正确，不是有效的json文件。

**解决措施**

检查build\_ohos下的compile\_commands.json，确保其内容符合JSON数组格式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/JWyOo3OVQVOaqnbG3tpRAQ/zh-cn_image_0000002779566754.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=3C2276B3CCDDF12FEFEDB93CFFAC209F954EA8B91B1EF1F8B5CB3B22800829EF)
