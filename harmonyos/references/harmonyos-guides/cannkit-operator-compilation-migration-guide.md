---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-operator-compilation-migration-guide
title: 算子编译迁移指导
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC昇腾到麒麟兼容性迁移指南 > Ascend910B/Ascend910C到KirinX90/Kirin9030迁移指导 > 算子编译迁移指导
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:44+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1044d837ec68149da03c7739aa071f995e215b8f97784d7e66f9f113a0121c73
---

进行算子编译时，开发者需要感知不同架构、不同的AI处理器型号。

* 异构编译场景：当前KirinX90/Kirin9030不支持异构编译。
* 标准自定义算子工程的场景：开发者需要在进行算子原型定义时，通过AddConfig接口注册算子支持的AI处理器型号以及相关的配置信息。AddConfig接口原型如下：soc参数表示AI处理器型号，aicore\_config表示其他配置信息。

  ```cpp
  void AddConfig(const char *soc);
  void AddConfig(const char *soc, OpAICoreConfig &aicore_config);
  ```

  所以需要在算子原型定义里，添加算子支持的AI处理器型号：KirinX90/Kirin9030。另外，算子工程目录下编译配置项文件CMakePresets.json中的ASCEND\_COMPUTE\_UNIT字段改成需要编译的新平台AI处理器型号。

  ```cpp
  // ...
  namespace ops {
  class AddCustom : public OpDef {
  public:
      AddCustom(const char* name) : OpDef(name)
      {
          // ...
          this->AICore().AddConfig("ascend910b");
          // 示例：添加KirinX90处理器系列
          this->AICore().AddConfig("kirinx90");
      }
  };
  OP_ADD(AddCustom);
  } // namespace ops
  ```
