---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/appgallery-attribution-strategy
title: 管理归因策略
breadcrumb: 指南 > 应用服务 > AppGallery Kit（应用市场服务） > 应用归因服务 > 开发准备 > 管理归因策略
category: harmonyos-guides
scraped_at: 2026-04-29T13:37:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:75c0aaf86418983533196c1b7f107003cc95ac06ddc170074a68beef9fbf5a73
---

通过归因策略管理，支持开发者在应用归因云端管理台维护可归因的分发平台及归因优先级、归因窗口期、归因节点设置，从而提升归因能力拓展性，适配开发者多样化归因诉求。

**开发者角色的合作伙伴在归因策略管理页面可以做如下操作**：

新增、编辑、查看、删除归因策略，创建完成即可生效（生效时间24小时）。

点击左侧归因策略管理菜单栏，进入归因策略管理页面，开发者基于推广应用、转化事件等维度进行归因策略的维护，所有的归因策略都是基于开发者下具体某个推广应用配置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/XnYO5IdhS8SiuXZi9nYerg/zh-cn_image_0000002558765288.png?HW-CC-KV=V1&HW-CC-Date=20260429T053712Z&HW-CC-Expire=86400&HW-CC-Sign=7A3EB99F3E17F6DA0E059B7817CDA477EC16227B0914162DA9A3A8F9BFAD2902)

说明

支持在列表点滑块左右切换表示“暂停”和“启用”。

## 新增

在归因策略管理页面点击“新增”按钮，进入“新增归因策略”页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/rfg4j3F1SZ-MUNOY2igKaA/zh-cn_image_0000002558605632.png?HW-CC-KV=V1&HW-CC-Date=20260429T053712Z&HW-CC-Expire=86400&HW-CC-Sign=659CF1FE47A24C4DF30EBEA60FF9AA39FD7A51C2AD5EE502F862A17A6A3114C3)

参数填写说明如下：

| 名称 | 参数 | 其他说明 |
| --- | --- | --- |
| 归因策略名称 | 文本输入框，必填，支持输入最多30个字符，用于填写归因策略名称。 | \_ |
| 推广应用 | 该参数为下拉多选框，必填，支持全选。  值范围：注册在归因角色下的所有推广应用名称。  可选项仅限HarmonyOS应用。 | 若有多个推广应用，支持下拉框输入关键字查询匹配。 |
| 转化事件 | 该参数为下拉多选框，选填，支持全选。  值范围：全部有效的标准转化事件和该推广应用下有效的自定义转化事件。 | 提供搜索框，以事件名称搜索，方便选择转化事件；支持以转化事件类型辅助筛选。 |
| 归因窗口期 | 数字输入框，必填；推广应用+转化事件维度的归因窗口期。  值范围：(0,180】,单位天，默认值：7。 | \_ |
| 激活后归因 | 单选勾选框，选填，默认值：勾选 。 | \_ |
| 激活后归因窗口期 | 数字输入框，必填，“激活后归因”开关打开后可见，否则隐藏。  值范围：(0,180】,单位天，默认值：7。 | \_ |
| 归因模型 | 下拉单选框，必填。  **说明：** 目前暂支持：“末次归因”。 | \_ |
| 归因优先级 | 归因优先级维护页面，显示所有已维护的分发平台，开发者只需维护对应的优先级即可。  通过“+”新增归因优先级行数配置不同分发平台的归因优先级，可以通过点击向上、向下箭头调整已选中分发平台优先级，也通过“x”删除当前归因优先级。每一级支持配置多个分发平台（不限个数），每个分发平台只能有一个归因优先级。  值范围：【1,10】，和分发平台最大量一致，值越小优先级越高。 | \_ |
| 分发平台 | 该参数为下拉多选框，选填，默认为空。  值范围：应用归因服务上注册的有效的分发平台。 | 提供搜索框，支持按照分发平台名称搜索后筛选匹配结果展示，并支持选中搜索结果。 |

说明

开发者创建归因策略上限为20条，即最多同时有20条生效的归因策略记录。

## 编辑

在归因策略管理页面点击右侧“编辑”按钮，弹出窗口期维护页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/L93Ae3rwQLW3lCuZlkWAdg/zh-cn_image_0000002589325159.png?HW-CC-KV=V1&HW-CC-Date=20260429T053712Z&HW-CC-Expire=86400&HW-CC-Sign=61A5061FDA1F3B79DA1AF1EC444DA52D064D24587B0B1F6CEA34F7A685CEF8D9)

维护完成后，点击“确认”即可生成有效记录，若点击“取消”，则不创建相应记录。

## 查看

在归因策略管理页面点击右侧“查看”按钮，弹出归因策略查看页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/1tK0cYSeQFqgf7hl-0prpw/zh-cn_image_0000002589245095.png?HW-CC-KV=V1&HW-CC-Date=20260429T053712Z&HW-CC-Expire=86400&HW-CC-Sign=CF9D4EB3F5E0A07B3BCED44E9C36A6EBF6E04E20D765E21188F6927262ABA27B)

可点击“编辑”按钮进入编辑页面，或点击“取消”关闭当前页面返回列表页面。

## 删除

在归因策略管理页面点击右侧“删除”按钮：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/itPLjDfoQP-usGKBg5nm8Q/zh-cn_image_0000002558765290.png?HW-CC-KV=V1&HW-CC-Date=20260429T053712Z&HW-CC-Expire=86400&HW-CC-Sign=11BFFFAF90AAC1C792F3C302933128529A62F738B2AD5C89605C0E4D5E38BAB1)

点击确认该记录状态变为“删除”，删除状态的记录仅可查看。

说明

新增、编辑、查看、删除等操作，无需审批，新增、编辑成功即为“启用”，支持在列表点滑块切换“暂停”和“启用”，删除完成即为“删除”。
