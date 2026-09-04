---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-operator-package-deployment
title: 算子包安装
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > 自定义算子开发 > 算子实现 > 工程化算子开发 > 算子编译安装 > 算子包安装
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:25+08:00
doc_updated_at: 2026-05-12
content_hash: sha256:7e233eb0807d6a88fe51cedd70fc189926a6392eb42138c54b437a46c502fdb6
---

执行算子工程的编译时，编译结果会自动部署到算子包安装目录下。

1. 自定义算子包安装。

   算子编译完成后，会自动将算子交付件安装到DDK指定目录，开发者无需关注。

   ![](https://media:401788444102531874) 

   自定义算子包默认安装路径为${DDK\_INSTALL\_PATH}/tools/platform。
2. 安装后的目录结构如下所示：

   ```text
   platform // 平台插件目录
   ├── kirin9020 // Kirin AI处理器类型
   │   ├── config
   │   │   └── npu_custom_opinfo.json // 算子信息库
   │   ├── lib64
   │   │   └── libcustom_op.so // host侧二进制文件
   │   ├── ops
   │   │   └── impl
   │   │       ├── custom // kernel交付件
   │   │       │   ├── add_custom.cpp
   │   │       │   ├── add_custom.py
   │   │       │   └── op_proto.h
   │   │       └── impl
   │   └── simulator
   └── README.md
   ```
