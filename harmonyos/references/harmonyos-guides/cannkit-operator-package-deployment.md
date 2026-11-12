---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-operator-package-deployment
title: AscendC算子包安装
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 自定义算子开发 > AscendC算子开发 > AscendC算子实现 > AscendC算子工程开发 > AscendC算子工程编译安装 > AscendC算子包安装
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:42+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:2a8b1273044fc1f622e0731ddf26cd86b74f6db5efe9979bf1576f16e7a2b309
---

执行算子工程的编译时，编译结果会自动部署到算子包安装目录下。

1. 自定义算子包安装。

   算子编译完成后，会自动将算子交付件安装到CANN指定目录，开发者无需关注。

   **说明** 

   自定义算子包默认安装路径为${install\_path}/cann-${cann\_version}/opp/vendors/。
2. 安装后的目录结构如下所示：

   ```text
   ├── opp    //算子库目录
   │   ├── vendors     //自定义算子所在目录
   │       ├── config.ini
   │       └── vendor_name1   // 存储对应厂商部署的自定义算子，此名字为编译自定义算子安装包时配置的vendor_name，若未配置，默认值为customize
   │           ├── framework     //自定义算子插件库
   │           ├── op_api
   │           │   ├── include
   │           │   │  └── aclnn_xx.h      //算子调用API声明文件
   │           │   └── lib
   │           │       └── libcust_opapi.so
   │           ├── op_impl
   │           │   └── ai_core
   │           │       └── tbe
   │           │           ├── config
   │           │           ├── vendor_name1_impl    //自定义算子实现代码文件
   │           │           │   └── dynamic
   │           │           │       ├── xx.cpp
   │           │           │       └── xx.py
   │           │           ├── kernel     //自定义算子二进制文件
   │           │           │   └── ${soc_version}     //昇腾AI处理器类型
   │           │           │   └── config
   │           │           └── op_tiling
   │           │               ├── lib
   │           │               └── liboptiling.so
   │           └── op_proto     //自定义算子原型库所在目录
   │                ├── inc
   │                │   └── op_proto.h
   │                └── lib
   │       ├── vendor_name2   // 存储厂商vendor_name2部署的自定义算子
   ```
