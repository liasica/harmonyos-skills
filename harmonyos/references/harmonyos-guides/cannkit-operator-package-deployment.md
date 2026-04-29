---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-operator-package-deployment
title: 算子包安装
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > 自定义算子开发 > 算子实现 > 工程化算子开发 > 算子编译安装 > 算子包安装
category: harmonyos-guides
scraped_at: 2026-04-29T13:41:11+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fa77e3c0c6e9e993be7cabe63769f5e0488952ebe072d2c96c753d28d4b568ed
---

执行算子工程的编译时，编译结果会自动部署到算子包安装目录下。

1. 自定义算子包安装。

   算子编译完成后，会自动将算子交付件安装到DDK指定目录，开发者无需关注。

   说明

   自定义算子包默认安装路径为${DDK\_INSTALL\_PATH}/tools/platform。
2. 安装后的目录结构如下所示：

   ```
   1. platform                            // 平台插件目录
   2. ├── kirin9020                       // Kirin AI处理器类型
   3. │   ├── config
   4. │   │   └── npu_custom_opinfo.json  // 算子信息库
   5. │   ├── lib64
   6. │   │   └── libcustom_op.so         // host侧二进制文件
   7. │   ├── ops
   8. │   │   └── impl
   9. │   │       ├── custom              // kernel交付件
   10. │   │       │   ├── add_custom.cpp
   11. │   │       │   ├── add_custom.py
   12. │   │       │   └── op_proto.h
   13. │   │       └── impl
   14. │   └── simulator
   15. └── README.md
   ```
