---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-command-line-tool-29
title: ohpm unpublish ${name} -f命令执行失败
breadcrumb: FAQ > DevEco Studio > 命令行工具 > ohpm unpublish ${name} -f命令执行失败
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:58+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:70d93ef4cb453a94f295d7075dcc404663380c663561f00f3fcf40b12035fd70
---

## 问题现象

执行命令“ohpm unpublish ${name} -f”下架三方库失败，异常信息：

```ts
ERROR: HttpCode 400 The OHPM package has been depended on by other components
ERROR: Unpublish failed, detail: The "Unpublish" request to url "https://ohom.openharmony.cn/ohpm/XXX" has failed
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/tRwq0h5kSzi_NeQAeNXNbQ/zh-cn_image_0000002658928949.png "点击放大")

## 背景知识

* [ohpm unpublish](../harmonyos-guides/ide-ohpm-unpublish.md)：下架已发布的三方库。
* [命令格式](../harmonyos-guides/ide-ohpm-unpublish.md#zh-cn_topic_0000001745217274_命令格式)：ohpm unpublish [options] [<@group>]<pkg>[@<version>]。
* [功能描述](../harmonyos-guides/ide-ohpm-unpublish.md#zh-cn_topic_0000001745217274_功能描述)：
  + 从OpenHarmony三方库中心仓下架已经发布并审核通过上架的三方库。
  + 若不指定版本，则默认下架三方库的所有版本，并且需要加上-f配置参数；全部版本均下架后，在24h内则不允许重新发布相同名称的三方库。
  + 若下架了某个版本，该版本号不允许再次使用，后续发布必须使用新的版本号。
  + 若此三方库被其它三方库依赖，则不删除，而是打上deprecated的标签；若没有被依赖，则直接删除。

## 问题定位

* 由异常描述可知，下架失败的原因为被其他三方库依赖。
* 进入想要被下架的三方库的OpenHarmony三方库中心仓主页，在“被依赖”页签，可以看到有其他三方库依赖该三方库。
* 经确认，依赖该三方库的为历史版本，在最新的版本中已经解除对被依赖三方库的依赖关系。
* 删除有依赖关系的历史版本后，unpublish命令执行成功。

## 分析结论

unpublish命令执行失败原因在于还有依赖关系未删除。

## 修改建议

下架三方库，先根据“被依赖”页签递归删除被依赖项中的依赖关系，再执行对目标三方库的下架操作。

## 总结

unpublish命令不会直接下架目标三方库，避免因为依赖关系导致其他的库也不可用，若有依赖关系则无法被删除，会打上deprecated的标签。
