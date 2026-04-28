---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/share-access-one-step
title: 目标设备接收分享数据一步直达体验
breadcrumb: 指南 > 应用服务 > Share Kit（分享服务） > Share Kit体验规范 > 目标设备接收分享数据一步直达体验
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:58+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e9b3c25b15ef1644e53a815cd2ee58a0982c7723eb4f2ddfb7e47f1b5b665797
---

为保证华为分享目标设备接收体验更优，规范分享数据接收时的直达体验，目标设备接收到分享数据后，将按照如下规则处理：

| 接收能力 | 数据类型 | 存储位置 | 预览方式 |
| --- | --- | --- | --- |
| 一步直达 | 媒体类型（仅包含图片和视频文件） | PC/2in1设备：文件管理“华为分享”目录。  其他设备：图库“华为分享”相册。 | PC/2in1设备：文件管理界面中文件高亮显示。  其他设备：图库大图预览。 |
| 一步直达 | 链接类型，  Applinking | 不涉及 | 直达对应的应用。如应用未安装，拉起浏览器或应用市场（以AppLinking配置为准）。 |
| 一步直达 | 链接类型，Deeplink | 不涉及 | 直达对应的应用。如应用未安装，弹窗提示用户。 |
| 一步直达 | 链接类型，  普通链接（除系统可识别的特殊链接外的其他http/https链接） | 不涉及 | 直达浏览器打开对应的链接。 |
| 一步直达 | 纯文本类型 | 文件管理“华为分享”目录，以txt格式文件保存。 | 使用文件预览打开。 |
| 一步直达 | 文件类型 | 文件管理“华为分享”目录。 | PC/2in1设备：文件管理界面中文件高亮显示。  其他设备：单文件使用文件预览，多文件高亮显示。 |
| 一步直达 | 自定义类型（除系统已预置的utd类型之外） | 文件管理“华为分享”目录。 | 有可打开应用直接打开，无可打开应用弹出提示。 |
| 沙箱接收 | 仅支持文件类型（包含系统已预置的文件类型及自定义类型文件） | 应用沙箱指定目录。 | 应用自行处理预览方式。 |

## 指定应用直达

从6.0.0(20) Beta3版本开始，碰一碰分享支持指定应用拉起的能力。

除以上系统默认直达方式外，同开发者账号下应用支持以下拉起规则：

* 同包名应用优先直达。若接收端已安装和发送端相同的应用，且支持拉起（满足[隐式匹配原理](explicit-implicit-want-mappings.md#隐式want匹配原理)）该应用，则优先拉起同包名应用。
* 同开发者账号(developerId相同)下的应用可通过[module.json5配置文件](module-configuration-file.md)配置实现优先拉起指定应用。

### 能力限制

* 仅支持同开发者账号（developerId相同）下的应用。
* 不支持媒体类文件和压缩包类型的分享数据。
* 不支持多文件（2个及以上）的分享数据。
* 仅支持碰一碰分享能力。

### 配置示例

通过在配置文件（src/main/module.json5）中配置[metadata](module-configuration-file.md#metadata标签)标签实现。

* shareType：用于分组匹配，当发送端应用和接收端应用配置相同的shareType值时，匹配规则才可生效。仅支持配置一项，配置多项时，仅第一项生效。
* shareBundleName：指定打开应用的包名，可配置多项。当shareType相同时，按数组排列顺序匹配第一个已安装且支持拉起（满足[隐式匹配原理](explicit-implicit-want-mappings.md#隐式want匹配原理)）的应用，并优先拉起该应用。

```
1. {
2. "module": {
3. "abilities": [
4. {
5. "name": "EntryAbility",
6. "srcEntry": "./ets/entryability/EntryAbility.ets",
7. "startWindowIcon": "$media:launcher",
8. "startWindowBackground": "$color:start_window_background",
9. "exported": true,
10. "skills": [
11. {
12. "entities": [
13. "entity.system.home",
14. ],
15. "actions": [
16. "ohos.want.action.viewData"
17. ],
18. "uris": [
19. {
20. "scheme": "file",
21. "linkFeature": "FileOpen",
22. "type": "org.openxmlformats.wordprocessingml.document",
23. "maxFileSupported": 1
24. }
25. ],
26. "domainVerify": true
27. }
28. ]
29. },
30. ],
31. "metadata": [
32. {
33. "name": "shareType",
34. "value": "sharekitModel",
35. },
36. {
37. "name": "shareBundleName",
38. "value": "com.example.sharekitPhone",
39. },
40. {
41. "name": "shareBundleName",
42. "value": "com.example.sharekitPc",
43. }
44. ]
45. }
46. }
```
