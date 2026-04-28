---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-faq-2
title: 开启超帧外插模式后运动物体边缘出现严重拖影现象，可能的原因是什么？
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:45+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4a7f2bc4211b5f06aff5db491a5995d187da40ce93999e18f3c58ef86e8ceefd
---

由于外插模式需要标记模板缓冲（Stencil Buffer）的第8位用于区分静态物体和动态物体，即静态物体模板值第8位标记成0，动态物体模板值第8位标记成1，模板缓冲的低7位模板值开发者可自行设置。如果标记错误或漏标记，可能会在动态物体边缘产生严重的拖影现象。

**现象描述**

Demo中运动角色出现头身分离等严重拖影现象，角色头部向右偏。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/FLzqv1CcQ02AMNJqHeqdsQ/zh-cn_image_0000002583478731.png?HW-CC-KV=V1&HW-CC-Date=20260427T234742Z&HW-CC-Expire=86400&HW-CC-Sign=B28961E77D76BB5EB56F929142DF33A9078E136C6A1A559BA33AA98EF224E6F4)

**原因分析**

通过抓帧查看模板缓冲中的模板值，发现头发区域模板值为0，身体区域模板值为0x80。由于角色头、身均属于运动目标区域，应该将所有运动物体区域的模板值第8位标记为1。错误的头部区域模板值导致超帧效果出现头身分离的严重拖影现象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/4KoKmM_4TniCET4c8tE48Q/zh-cn_image_0000002552799082.png?HW-CC-KV=V1&HW-CC-Date=20260427T234742Z&HW-CC-Expire=86400&HW-CC-Sign=CFDB4C43D57F8ED8C14A00D47BCF79AC625F1C5E7C0146F6275707BF89655FE4)

**处理步骤**

基于分析结论，造成头身分离拖影现象的主要原因是运动区域模板值未统一标记为1xxx xxxx。因此将运动角色头发和面部区域的模板值统一改为0x80，保持和身体模板值一致，头身分离的拖影现象消失，效果如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/V9Es-kA2QVK5M-JU5PQSMQ/zh-cn_image_0000002583438777.png?HW-CC-KV=V1&HW-CC-Date=20260427T234742Z&HW-CC-Expire=86400&HW-CC-Sign=9FB026A31B7B813F69B065B7E0EBDE02DE9113941DFEC7B02CCF59604587494A)

**代码示例**

检查动态物体材质Shader中的模板值是否设置正确，即静态物体模板值标记为0xxx xxxx，动态物体模板值标记为1xxx xxxx。

```
1. Shader "Standard_with_stencil"
2. {
3. Properties
4. {
5. /* ... */
6. _LightingStencilRef("Lighting Stencil Reference", Float) = 128 // 将动态物体材质模板值改为1xxx xxxx，消除头身分离现象
7. [Enum(UnityEngine.Rendering.CompareFunction)] _LightingStencilComp("Lighting Stencil Comparison", Float) = 8
8. _StencilReadMask("Stencil Read Mask", Float) = 255
9. _StencilWriteMask("Stencil Write Mask", Float) = 255
10. }
11. SubShader
12. {
13. /* ... */
14. Pass
15. {
16. /* ... */
17. Stencil
18. {
19. Ref[_LightingStencilRef]
20. Comp[_LightingStencilComp]
21. ReadMask[_StencilReadMask]
22. WriteMask[_StencilWriteMask]
23. Pass Replace
24. }
25. }
26. }
27. }
```

说明

不同管线的Shader中需要配置模板值的Pass不同，如下：

* 团结引擎URP管线

  在每个有DepthOnly或DepthNormals的Pass中，即出现Tags {"LightMode" = "DepthOnly" }或Tags {"LightMode" = "DepthNormals" }的Pass，配置模板值。
* 团结引擎Build-in管线

  在每个有ForwardBase或ForwardAdd的Pass中，即出现Tags {"LightMode" = "ForwardBase" }或Tags {"LightMode" = "ForwardAdd" }的Pass，配置模板值。
