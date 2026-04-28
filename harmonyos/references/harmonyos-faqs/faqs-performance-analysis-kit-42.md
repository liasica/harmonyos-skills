---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-42
title: 如何解决Mac电脑不能识别hdc命令的问题
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 如何解决Mac电脑不能识别hdc命令的问题
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:18+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:94c7400ba69a6e302173e327af29eeaa1e0da1ee509ace5153cf1a44425838ec
---

1. 环境变量因素的解决方法参考如下：
   1. 点击屏幕左上角的苹果图标，转到系统设置中的“用户与群组”。
   2. 按住Ctrl键，点击左侧窗格中的用户账户名称，然后选择“高级选项”。
   3. 点击"Login Shell"下拉框，然后选择"/bin/bash"以将Bash作为默认shell。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/WduVOVmtSGirJ-30a8DIxw/zh-cn_image_0000002194318532.png?HW-CC-KV=V1&HW-CC-Date=20260428T002317Z&HW-CC-Expire=86400&HW-CC-Sign=188CDB9EEA5626A43966770B51EB7626DB2ED93B7D1220469E28CC8C3AF7044E "点击放大")
2. 非环境变量因素的解决方法参见：
   1. 打开终端，输入 cd ~。
   2. 使用 sudo vim .bash\_profile 命令编辑文件。
   3. 在文档底部输入：

      export PATH=${PATH}:Sdk/default/base/toolchains

      按下Esc键退出，然后在下方输入:wq保存并退出。
   4. 运行 source .bash\_profile 命令以加载环境变量。
   5. 输入 hdc -v，显示版本信息即表示可用。

   **参考链接：**

   [常见问题](../harmonyos-guides/hdc.md#常见问题)
