---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkgraphics3d-b065
title: ArkGraphics 3D
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Beta引入的API > ArkGraphics 3D
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:15+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:ccb97d09ddf5d9799a84992995312a981dafd6d6436ed66dea4aa3d6e307f8cd
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 函数变更 | 类名：Scene；  API声明：static load(uri?: Resource): Promise<Scene>;  差异内容：uri?: Resource | 类名：Scene；  API声明：static load(uri?: ResourceStr): Promise<Scene>;  差异内容：uri?: ResourceStr | api/graphics3d/Scene.d.ts |
| 属性变更 | 类名：SceneResourceParameters；  API声明：uri?: Resource;  差异内容：Resource | 类名：SceneResourceParameters；  API声明：uri?: ResourceStr;  差异内容：ResourceStr | api/graphics3d/Scene.d.ts |
| 属性变更 | 类名：SceneResource；  API声明：readonly uri?: Resource;  差异内容：Resource | 类名：SceneResource；  API声明：readonly uri?: ResourceStr;  差异内容：ResourceStr | api/graphics3d/SceneResources.d.ts |
