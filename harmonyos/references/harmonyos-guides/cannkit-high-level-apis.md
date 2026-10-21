---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-high-level-apis
title: 高阶API
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > 自定义算子开发 > 基本概念 > 编程API > 高阶API
category: harmonyos-guides
scraped_at: 2026-10-22T07:06:03+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:97fdfc69fb9b5600eb98c60e0cfe1a07d8021e07fcaacee7a948604cfe9eda3f
---

高阶API一般是基于单核对常见算法的抽象和封装，用于提高编程开发效率，通常会调用多种基础API实现。高阶API当前仅支持Matmul。

如下图所示，实现一个矩阵乘操作，使用基础API需要的步骤较多，需要关注格式转换、数据切分等逻辑；使用高阶API则无需关注这些逻辑，直接传入输入矩阵，调用接口获取输出即可。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/-ST9wEukQ3e5-tPeoT19EQ/zh-cn_image_0000002768021782.png)

注意，在程序中调用高阶API的Tiling接口或者使用高阶API的Tiling结构体参数时，需要引入依赖的头文件，示例如下。

```cpp
#include "register/tilingdata_base.h"
#include "lib/tiling_api.h"
 
namespace optiling {
BEGIN_TILING_DATA_DEF(MatmulCustomTilingData)
TILING_DATA_FIELD_DEF_STRUCT(TCubeTiling, cubeTilingData);
END_TILING_DATA_DEF;
REGISTER_TILING_DATA_CLASS(MatmulCustom, MatmulCustomTilingData);
} // namespace optiling
```
