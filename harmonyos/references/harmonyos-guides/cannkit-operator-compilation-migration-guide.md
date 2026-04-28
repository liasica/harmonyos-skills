---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-operator-compilation-migration-guide
title: 算子编译迁移指导
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC昇腾到麒麟兼容性迁移指南 > Ascend910B/Ascend910C到KirinX90/Kirin9030迁移指导 > 算子编译迁移指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:24+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c51962c75ec234b05dc37c76e1ae2c298a0c9d1508cf4a14cfeb3ac088dbd2fc
---

进行算子编译时，开发者需要感知不同架构、不同的AI处理器型号。

* 异构编译场景：当前KirinX90/Kirin9030不支持异构编译。
* 标准自定义算子工程的场景：开发者需要在进行算子原型定义时，通过AddConfig接口注册算子支持的AI处理器型号以及相关的配置信息。AddConfig接口原型如下：soc参数表示AI处理器型号，aicore\_config表示其他配置信息。

  ```
  1. void AddConfig(const char *soc);
  2. void AddConfig(const char *soc, OpAICoreConfig &aicore_config);
  ```

  所以需要在算子原型定义里，添加算子支持的AI处理器型号：KirinX90/Kirin9030。另外，算子工程目录下编译配置项文件CMakePresets.json中的ASCEND\_COMPUTE\_UNIT字段改成需要编译的新平台AI处理器型号。

  ```
  1. // ...
  2. namespace ops {
  3. class AddCustom : public OpDef {
  4. public:
  5. AddCustom(const char* name) : OpDef(name)
  6. {
  7. // ...
  8. this->AICore().AddConfig("ascend910b");
  9. // 示例：添加KirinX90处理器系列
  10. this->AICore().AddConfig("kirinx90");
  11. }
  12. };
  13. OP_ADD(AddCustom);
  14. } // namespace ops
  ```
