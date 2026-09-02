---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-general-description
title: 总体说明
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > OpRegistrationData > 总体说明
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6944a64ee5652c03880a6fbad02d76cce99bdb7f5526e81bd1aaf804654a2b41
---

开发人员完成自定义算子的实现代码后，需要进行适配插件的开发将基于第三方框架的算子映射成适配AI处理器的算子，可调用REGISTER\_CUSTOM\_OP宏实现算子转换。在调用REGISTER\_CUSTOM\_OP宏时，以REGISTER\_CUSTOM\_OP开始，以“.”链接FrameworkType、OriginOpType、ParseParamsFn等接口。

例如：

```cpp
REGISTER_CUSTOM_OP("OpType")
   .FrameworkType(TENSORFLOW)
   .OriginOpType("OriginOpType")
   .ParseParamsByOperatorFn(ParseParamFunc)
   .ImplyType(ImplyType::TVM);
```
