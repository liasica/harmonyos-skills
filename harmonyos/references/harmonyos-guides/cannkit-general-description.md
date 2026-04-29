---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-general-description
title: 总体说明
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > OpRegistrationData > 总体说明
category: harmonyos-guides
scraped_at: 2026-04-29T13:42:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2eb81ae803e56d09e48cf280c1d01f3a7699bbbefea52de7ed4469278f6228b0
---

开发人员完成自定义算子的实现代码后，需要进行适配插件的开发将基于第三方框架的算子映射成适配AI处理器的算子，可调用REGISTER\_CUSTOM\_OP宏实现算子转换。在调用REGISTER\_CUSTOM\_OP宏时，以REGISTER\_CUSTOM\_OP开始，以“.”链接FrameworkType、OriginOpType、ParseParamsFn等接口。

例如：

```
1. REGISTER_CUSTOM_OP("OpType")
2. .FrameworkType(TENSORFLOW)
3. .OriginOpType("OriginOpType")
4. .ParseParamsByOperatorFn(ParseParamFunc)
5. .ImplyType(ImplyType::TVM);
```
