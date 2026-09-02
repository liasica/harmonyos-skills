---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-126
title: 如何解决编译报错“Indexed access is not supported for fields(arkts-no-props-by-index)”的问题
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何解决编译报错“Indexed access is not supported for fields(arkts-no-props-by-index)”的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:55+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:ec0278c77fa88d112e6c1a8d1806b88c178f06b9ced28cc0f37019e6f70c865b
---

**问题现象**

动态调用类或接口的字段会导致编译报错：Indexed access is not supported for fields (arkts-no-props-by-index)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/3d2Vbn9hSBS-TACBWX0GBA/zh-cn_image_0000002654837917.png)

**解决方案**

修改代码：

```typescript
getValue(breakpoint: string): T {
  return Reflect.get(this.options, breakpoint) as T;
}
```
