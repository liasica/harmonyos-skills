---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-attribute-modifier-faq
title: 动态属性设置常见问题
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发调试调优 > UI开发常见问题 > 动态属性设置常见问题
category: harmonyos-guides
scraped_at: 2026-04-29T13:29:00+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:64eeec7761e4eb180931ac04433bb221ccd933fed0da1793ff76828671119187
---

本文档介绍动态属性设置的常见问题并提供参考。

## 使用AttributeModifier设置组件动态属性，出现jscrash

**问题现象**

使用AttributeModifier对组件进行[动态属性设置](../harmonyos-references/ts-universal-attributes-attribute-modifier.md)，设置某些属性后出现[JS Crash](jscrash-guidelines.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/yyg1cCyvQEuLEs93jjWFoQ/zh-cn_image_0000002558764662.png?HW-CC-KV=V1&HW-CC-Date=20260429T052859Z&HW-CC-Expire=86400&HW-CC-Sign=43C11E1DC2662A79D00B4725EE07A320762C930AB9403D2AF6FE84698688E1F2)

**解决措施**

根据提示跳转至报错日志，查看具体的报错原因，进行相应的修改，具体的跳转方法请参考下方示例代码。

**示例代码**

该示例通过Button绑定AttributeModifier，展示了AttributeModifier在设置不支持的属性时会抛出异常的场景，运行示例代码后会出现jscrash报错，参考下方的动图，跳转至具体的报错场景。在本示例中，删除reuseId相关代码即可正常运行。

```
1. // xxx.ets
2. // 设置Button组件属性的自定义AttributeModifier
3. class MyButtonModifier implements AttributeModifier<ButtonAttribute> {

5. applyNormalAttribute(instance: ButtonAttribute): void {
6. instance.reuseId('String') // 删除本行可以让程序正常运行
7. instance.backgroundColor(Color.Red)
8. }
9. }

11. @Entry
12. @Component
13. struct attributeDemo {
14. @State modifier: MyButtonModifier = new MyButtonModifier();

16. build() {
17. Row() {
18. Column() {
19. Button('Button')
20. .attributeModifier(this.modifier)
21. }
22. .width('100%')
23. }
24. .height('100%')
25. }
26. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/2RShMXEGRh64QysGsrbfsg/zh-cn_image_0000002558605006.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052859Z&HW-CC-Expire=86400&HW-CC-Sign=582DFA30B5072AE09C253927B35156F9B73BBEFD131F214E7C98194E5DCA9557)
