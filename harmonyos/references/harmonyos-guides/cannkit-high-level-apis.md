---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-high-level-apis
title: 高阶API
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > 自定义算子开发 > 基本概念 > 编程API > 高阶API
category: harmonyos-guides
scraped_at: 2026-04-29T13:41:06+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2f5aa1c0f755018c87464681f53265bb86e14948e1a4999cfb09d02b515d9687
---

高阶API一般是基于单核对常见算法的抽象和封装，用于提高编程开发效率，通常会调用多种基础API实现。高阶API当前仅支持Matmul。

如下图所示，实现一个矩阵乘操作，使用基础API需要的步骤较多，需要关注格式转换、数据切分等逻辑；使用高阶API则无需关注这些逻辑，直接传入输入矩阵，调用接口获取输出即可。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/FVjCoNK_TPu1-45MqhKvkA/zh-cn_image_0000002558765740.png?HW-CC-KV=V1&HW-CC-Date=20260429T054105Z&HW-CC-Expire=86400&HW-CC-Sign=70FA8181BDADCF9C0C8A8BEF3A6B9937DEACD3DC2BE5057EA99EE3288FDDF56C)

注意，在程序中调用高阶API的Tiling接口或者使用高阶API的Tiling结构体参数时，需要引入依赖的头文件，示例如下。

```
1. #include "register/tilingdata_base.h"
2. #include "lib/tiling_api.h"

4. namespace optiling {
5. BEGIN_TILING_DATA_DEF(MatmulCustomTilingData)
6. TILING_DATA_FIELD_DEF_STRUCT(TCubeTiling, cubeTilingData);
7. END_TILING_DATA_DEF;
8. REGISTER_TILING_DATA_CLASS(MatmulCustom, MatmulCustomTilingData);
9. } // namespace optiling
```
