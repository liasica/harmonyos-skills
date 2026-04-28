---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-theme
title: 设置主题样式
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > JS服务卡片UI组件 > 框架说明 > 设置主题样式
category: harmonyos-references
scraped_at: 2026-04-28T08:03:34+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:24d9373e2d4c78f8f2e90dc99f21110ea9d52e41aeee54e1707e796a1fbbee32
---

卡片目前支持修改的主题样式如下：

| 名称 | 描述 |
| --- | --- |
| app\_background | 设置卡片背景颜色。默认为纯白色。 |

修改主题样式需要在widget文件夹下手动创建与pages同级的resources文件夹，在widget/resources/styles/default.json文件中配置主题样式。例如，修改卡片默认的背景色为浅灰色：

```
1. {
2. "style": {
3. "app_background": "#dcdcdc"
4. }
5. }
```
