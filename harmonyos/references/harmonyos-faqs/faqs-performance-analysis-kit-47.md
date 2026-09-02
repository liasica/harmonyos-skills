---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-47
title: 如何通过hdc命令关闭整个应用
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 如何通过hdc命令关闭整个应用
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:51+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:56e90e1af04cd0633d9edd1f493506925e38a7c395031cee6373cac708254a09
---

可以通过以下命令结束应用：

```powershell
hdc shell aa force-stop <bundleName>
```

返回“force stop process successfully”，表示应用已成功结束。

示例如下：

```powershell
hdc shell aa force-stop com.example.myapplication
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/jOU90SkgS6OY_B70by7CgQ/zh-cn_image_0000002654835777.png "点击放大")

**参考链接**

[aa工具](../harmonyos-guides/aa-tool.md)
