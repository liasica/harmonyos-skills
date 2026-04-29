---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-6
title: 编译报错“Module 'xxx' has no exported member 'yyy'”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Module 'xxx' has no exported member 'yyy'”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:22+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:c298ddbde59c57665eed4fe0d9223aa971fde1b5164b2b261423b82c1bc7b814
---

**问题现象**

Stage模板工程编译构建失败，提示 “Module 'xxx' has no exported member 'yyy'” 并且“yyy”符号是由export \* from 'x.js'语法从js文件中导出。

**解决措施**

由于当前Stage工程编译构建期的语法校验工具对js文件不作检查，导致无法正确识别通过export \* from 'x.js'导出的符号，因此在引用这些符号时会提示“Module 'xxx' has no exported member 'yyy'”的错误信息。

如果遇到类似问题，尝试以下解决方法：

* 方法1（推荐使用）： 使用符号显式导出语法，从js文件中re-export符号 。

  export { yyy } from 'x.js'

* 方法2：新增x.js对应的声明文件（.d.ts），并在引用时不指定后缀。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/9Ms_DRj5RBWI689fzueIPA/zh-cn_image_0000002229758485.png?HW-CC-KV=V1&HW-CC-Date=20260429T062021Z&HW-CC-Expire=86400&HW-CC-Sign=C95B8E8F746C6454A23F69AD1AE11E099BA0168193BE3C83EB3E7D656A6F079F)
