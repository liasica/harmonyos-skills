---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-6
title: 编译报错“Module 'xxx' has no exported member 'yyy'”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Module 'xxx' has no exported member 'yyy'”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:08+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:96986d8d32067eac78e2856008d2d7912d064a235093b2b85231c5bfc43da9ac
---

**问题现象**

Stage模板工程编译构建失败，提示 “Module 'xxx' has no exported member 'yyy'” 并且“yyy”符号是由export \* from 'x.js'语法从js文件中导出。

**解决措施**

由于当前Stage工程编译构建期的语法校验工具对js文件不作检查，导致无法正确识别通过export \* from 'x.js'导出的符号，因此在引用这些符号时会提示“Module 'xxx' has no exported member 'yyy'”的错误信息。

如果遇到类似问题，尝试以下解决方法：

* 方法1（推荐使用）： 使用符号显式导出语法，从js文件中re-export符号 。

  export { yyy } from 'x.js'

* 方法2：新增x.js对应的声明文件（.d.ts），并在引用时不指定后缀。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/9Ms_DRj5RBWI689fzueIPA/zh-cn_image_0000002229758485.png?HW-CC-KV=V1&HW-CC-Date=20260428T002907Z&HW-CC-Expire=86400&HW-CC-Sign=97752C2F9ABC7F419BDA792596DF45975FF05BCE49E00975F3B73DBDC4C03FBB)
